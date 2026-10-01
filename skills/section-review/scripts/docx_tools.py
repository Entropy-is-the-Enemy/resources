#!/usr/bin/env python3
"""Minimal, dependency-free .docx helpers for section-review's apply step.

Library use (import docx_tools as dt):
    z, x = dt.load("plan.docx")            # x is word/document.xml as str
    x = dt.para_replace(x, old, new)        # match a paragraph by visible text, rebuild its runs
    ppr = dt.ppr_of(x, "key text")          # paragraph properties (style, numbering) of a paragraph
    x = dt.replace_para(x, "key text", [dt.mkpara(ppr, "new text", bold_lead="Lead. ")])
    x = dt.insert_after(x, "key text", [dt.mkpara(ppr, "another paragraph")])
    x = dt.cell_set(x, t=3, r=2, k=1, old="41%", new="43%")   # table cell by index, asserts current text
    dt.save("plan.docx", z, x)

CLI:
    docx_tools.py dump FILE            # [P12|Heading2] text ... / [TABLE 3] / [T3R1] a | b | c
    docx_tools.py diff OLD NEW         # block-level diff with word-level markup on changed paragraphs

Rules the helpers enforce: never string-replace a number in raw XML (use para_replace or cell_set,
which match on visible text and keep the paragraph's own properties and the first run's formatting).
"""
import sys, re, os, zipfile, shutil, difflib, tempfile
import xml.dom.minidom
from xml.sax.saxutils import escape, unescape
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

# ---------- load / save ----------

def load(f):
    z = zipfile.ZipFile(f)
    return z, z.read("word/document.xml").decode()

def save(f, zin, x):
    """Validate XML, rewrite the package with the new document.xml, atomically replace f."""
    xml.dom.minidom.parseString(x.encode())
    fd, tmp = tempfile.mkstemp(suffix=".docx", dir=os.path.dirname(os.path.abspath(f)) or ".")
    os.close(fd)
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for it in zin.infolist():
            d = zin.read(it.filename)
            if it.filename == "word/document.xml":
                d = x.encode()
            zout.writestr(it, d)
    zin.close()
    shutil.move(tmp, f)

# ---------- text helpers ----------

def txt(s):
    """Visible text of an XML fragment (tags stripped, entities still escaped)."""
    return re.sub(r"<[^>]+>", "", s)

def strip_ids(s):
    return re.sub(r' w14:(paraId|textId)="[0-9A-F]+"', "", s)

def rep(x, a, b, n=1):
    """Raw replace with an exact-count assertion. Text only; never use for numbers inside runs."""
    assert x.count(a) == n, (a[:60], x.count(a))
    return x.replace(a, b)

# ---------- paragraphs ----------

def _para_spans(x):
    for m in re.finditer(r"<w:p(?: [^>]*)?>.*?</w:p>", x, flags=re.S):
        yield m.span()

def para_bounds(x, key, nth=0):
    """(s, e) of the nth paragraph whose visible text contains key."""
    hits = [(s, e) for s, e in _para_spans(x) if key in unescape(txt(x[s:e]))]
    assert hits, "paragraph not found: " + key[:60]
    return hits[nth]

def para_count(x, key):
    return sum(1 for s, e in _para_spans(x) if key in unescape(txt(x[s:e])))

def ppr_of(x, key):
    s, e = para_bounds(x, key)
    m = re.search(r"<w:pPr>.*?</w:pPr>", x[s:e], flags=re.S)
    return m.group(0) if m else ""

def rpr_of(x, key):
    """rPr of the first run of the paragraph containing key ('' if none)."""
    s, e = para_bounds(x, key)
    runs = re.findall(r"<w:r(?: [^>]*)?>.*?</w:r>", x[s:e], flags=re.S)
    if not runs:
        return ""
    m = re.search(r"<w:rPr>.*?</w:rPr>", runs[0], flags=re.S)
    return m.group(0) if m else ""

def mkpara(ppr, text, bold_lead=None, rpr=""):
    """New paragraph with the given pPr; optional bold lead-in run; optional rPr for the body run."""
    runs = ""
    if bold_lead:
        runs += f'<w:r><w:rPr><w:b/></w:rPr><w:t xml:space="preserve">{escape(bold_lead)}</w:t></w:r>'
    runs += f'<w:r>{rpr}<w:t xml:space="preserve">{escape(text)}</w:t></w:r>'
    return "<w:p>" + ppr + runs + "</w:p>"

def para_replace(x, a, b):
    """Replace visible text a with b inside the one paragraph that contains it.
    Runs with a single shared rPr are merged; mixed formatting raises so the caller
    can rebuild the paragraph explicitly with replace_para + mkpara."""
    s, e = para_bounds(x, a)
    assert para_count(x, a) == 1, "text appears in more than one paragraph: " + a[:60]
    seg = x[s:e]
    t = unescape(txt(seg))
    runs = re.findall(r"<w:r(?: [^>]*)?>.*?</w:r>", seg, flags=re.S)
    rprs = set((re.search(r"<w:rPr>.*?</w:rPr>", r, flags=re.S).group(0) if "<w:rPr>" in r else "") for r in runs)
    if len(rprs) != 1:
        raise AssertionError("mixed formatting in paragraph, rebuild it explicitly: " + t[:60])
    rpr = rprs.pop()
    first = seg.find(runs[0]); last = seg.rfind(runs[-1]) + len(runs[-1])
    newseg = seg[:first] + f'<w:r>{rpr}<w:t xml:space="preserve">{escape(t.replace(a, b))}</w:t></w:r>' + seg[last:]
    return x[:s] + newseg + x[e:]

def replace_para(x, key, paras):
    s, e = para_bounds(x, key)
    return x[:s] + "".join(paras) + x[e:]

def insert_after(x, key, paras):
    s, e = para_bounds(x, key)
    return x[:e] + "".join(paras) + x[e:]

def insert_before(x, key, paras):
    s, e = para_bounds(x, key)
    return x[:s] + "".join(paras) + x[s:]

def delete_para(x, key):
    s, e = para_bounds(x, key)
    return x[:s] + x[e:]

# ---------- blocks and tables ----------

def blocks(x, open_tag, close_tag):
    """Top-level (s, e) spans of nested elements, e.g. blocks(x, '<w:tbl>', '</w:tbl>')."""
    out = []; pos = 0; stem = open_tag[:-1]
    while True:
        s = x.find(stem, pos)
        if s < 0:
            break
        if x[s + len(stem)] not in (">", " "):
            pos = s + 1; continue
        depth = 0; i = s
        while True:
            a = x.find(stem, i); b = x.find(close_tag, i)
            if a >= 0 and a < b and x[a + len(stem)] in (">", " "):
                depth += 1; i = a + 1
            else:
                depth -= 1; i = b + len(close_tag)
                if depth == 0:
                    break
        out.append((s, i)); pos = i
    return out

def set_cell_text(cx, new):
    """Replace all runs in a cell with one run carrying the first run's rPr."""
    runs = [m.span() for m in re.finditer(r"<w:r(?: [^>]*)?>.*?</w:r>", cx, flags=re.S)]
    if not runs:
        return cx.replace("</w:p>", f'<w:r><w:t xml:space="preserve">{escape(new)}</w:t></w:r></w:p>', 1)
    first = cx[runs[0][0]:runs[0][1]]
    m = re.search(r"<w:rPr>.*?</w:rPr>", first, flags=re.S); rpr = m.group(0) if m else ""
    newrun = f'<w:r>{rpr}<w:t xml:space="preserve">{escape(new)}</w:t></w:r>' if new != "" else ""
    return cx[:runs[0][0]] + newrun + cx[runs[-1][1]:]

def cell_set(x, t, r, k, old, new):
    """Table t (1-based), row r, cell k (0-based): assert visible text == old, then set new."""
    tb = blocks(x, "<w:tbl>", "</w:tbl>")[t - 1]; tx = x[tb[0]:tb[1]]
    rows = blocks(tx, "<w:tr>", "</w:tr>"); rs, re_ = rows[r]; rx = tx[rs:re_]
    cells = blocks(rx, "<w:tc>", "</w:tc>"); cs, ce = cells[k]; cx = rx[cs:ce]
    cur = unescape(txt(cx))
    assert cur.strip() == old.strip(), (f"T{t}R{r}C{k}", cur, old)
    ncx = set_cell_text(cx, new)
    nrx = rx[:cs] + ncx + rx[ce:]; ntx = tx[:rs] + nrx + tx[re_:]
    return x[:tb[0]] + ntx + x[tb[1]:]

# ---------- dump / diff (ElementTree based, read only) ----------

def _et_text(el):
    return "".join(t.text or "" for t in el.iter(W + "t"))

def iter_blocks(path):
    """Yield (heading, kind, text, style) for every non-empty paragraph and table row, in order."""
    z = zipfile.ZipFile(path); root = ET.fromstring(z.read("word/document.xml")); body = root.find(W + "body")
    head = "(top)"; ti = 0; pi = 0
    for el in body:
        if el.tag == W + "p":
            pi += 1
            s = el.find(W + "pPr/" + W + "pStyle"); st = s.get(W + "val") if s is not None else ""
            t = _et_text(el).strip()
            if not t:
                continue
            if st.startswith("Heading") or st == "Title":
                head = t
            if el.find(".//" + W + "drawing") is not None:
                t += " [IMAGE]"
            yield (head, "P", t, st, pi)
        elif el.tag == W + "tbl":
            ti += 1
            for ri, row in enumerate(el.findall(W + "tr")):
                yield (head, "T", " | ".join(_et_text(c).strip() for c in row.findall(W + "tc")), f"table{ti}r{ri}", ti)

def dump(path):
    last_t = None
    for head, kind, t, st, idx in iter_blocks(path):
        if kind == "P":
            print(f"[P{idx}{'|' + st if st else ''}] {t}")
        else:
            if idx != last_t:
                print(f"[TABLE {idx}]"); last_t = idx
            print(f"  [{st.upper().replace('TABLE', 'T').replace('R', 'R')}] {t}")

def _wdiff(a, b):
    aw = a.split(); bw = b.split(); out = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, aw, bw, autojunk=False).get_opcodes():
        if tag == "equal":
            seg = aw[i1:i2]
            if len(seg) > 14:
                seg = seg[:6] + ["..."] + seg[-6:]
            out += seg
        if tag in ("replace", "delete"):
            out.append("[-" + " ".join(aw[i1:i2]) + "-]")
        if tag in ("replace", "insert"):
            out.append("{+" + " ".join(bw[j1:j2]) + "+}")
    return " ".join(out)

def diff(old_path, new_path, section=None):
    """Block-level diff. Returns (lines, changed_outside_section_count)."""
    old = [b for b in iter_blocks(old_path)]; new = [b for b in iter_blocks(new_path)]
    ok = [b[2] for b in old]; nk = [b[2] for b in new]
    sm = difflib.SequenceMatcher(None, ok, nk, autojunk=False)
    lines = []; outside = 0
    def note(head, s):
        nonlocal outside
        if section is not None and head != section:
            outside += 1
        lines.append(f"[{head}] {s}")
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        olds = old[i1:i2]; news = new[j1:j2]; used = set()
        for ob in olds:
            best = None; bs = 0
            for k, nb in enumerate(news):
                if k in used:
                    continue
                r = difflib.SequenceMatcher(None, ob[2], nb[2]).ratio()
                if r > bs:
                    bs, best = r, k
            if best is not None and bs > 0.45:
                used.add(best); nb = news[best]
                note(nb[0], f"CHANGED {'row' if nb[1] == 'T' else 'paragraph'}: {_wdiff(ob[2], nb[2])}")
            else:
                note(ob[0], f"REMOVED {'row' if ob[1] == 'T' else 'paragraph'}: {ob[2][:300]}")
        for k, nb in enumerate(news):
            if k not in used:
                note(nb[0], f"ADDED {'row' if nb[1] == 'T' else 'paragraph'}: {nb[2][:300]}")
    lines.append(f"blocks compared: {len(old)} old, {len(new)} new")
    return lines, outside

if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "dump":
        dump(sys.argv[2])
    elif len(sys.argv) >= 4 and sys.argv[1] == "diff":
        lines, _ = diff(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else None)
        print("\n".join(lines))
    else:
        print(__doc__); sys.exit(1)
