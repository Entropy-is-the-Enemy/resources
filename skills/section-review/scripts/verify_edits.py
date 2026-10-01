#!/usr/bin/env python3
"""Deterministic post-apply check for section-review. Exit 0 = clean, 1 = findings.

    verify_edits.py FILE --backup BACKUP --edits edits.json [--section "Heading text"]
                    [--allow-em-dash] [--allow-contractions] [--allow-first-person]
                    [--must-contain phrases.txt]

edits.json: a list of {"old": "...", "new": "..."} objects.
  old only  -> deletion (old must be absent after)
  new only  -> insertion (new must appear exactly once after)
  both      -> replacement (new once, old absent, unless old is a substring of new)
  Matching is on visible text. Paragraph text is compared whole; a value may be a sentence
  inside a paragraph, which is checked by substring.

Checks, in order:
  1. every "new" present exactly once in FILE; every "old" absent
  2. diff against BACKUP confined to --section (heading text); zero changed blocks elsewhere
  3. mechanics on the changed text only: em dashes, contractions, first person, double spaces,
     unbalanced quotes or parentheses, trailing whitespace
  4. every line of --must-contain (facts on the author's authority) present in FILE, substring match

Works on .docx (via docx_tools.py beside this script) and on .md / .txt.
"""
import sys, os, re, json, argparse, difflib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

CONTRACTIONS = re.compile(r"\b(?:\w+n't|\w+'re|\w+'ve|\w+'ll|\w+'d|I'm|it's|that's|there's|here's|what's|who's|let's)\b", re.I)
FIRST_PERSON = re.compile(r"\b(?:I|I'm|I've|I'll|my|mine|myself|we|we're|we've|we'll|our|ours|us)\b")

def load_blocks(path):
    """[(heading, text)] for docx or text files."""
    if path.lower().endswith(".docx"):
        import docx_tools as dt
        return [(b[0], b[2]) for b in dt.iter_blocks(path)]
    out = []; head = "(top)"
    with open(path, encoding="utf-8") as f:
        for line in f:
            t = line.rstrip("\n")
            if not t.strip():
                continue
            if re.match(r"^#{1,6}\s", t):
                head = re.sub(r"^#{1,6}\s+", "", t).strip()
            out.append((head, t.strip()))
    return out

def full_text(blocks):
    return "\n".join(t for _, t in blocks)

def mechanics(text, args):
    f = []
    if not args.allow_em_dash and ("\u2014" in text or "\u2013" in text):
        f.append("em/en dash present")
    if not args.allow_contractions and CONTRACTIONS.search(text):
        f.append("contraction: " + CONTRACTIONS.search(text).group(0))
    if not args.allow_first_person and FIRST_PERSON.search(text):
        f.append("first person: " + FIRST_PERSON.search(text).group(0))
    if "  " in text:
        f.append("double space")
    if text.count("(") != text.count(")"):
        f.append("unbalanced parentheses")
    if text.count("“") != text.count("”"):
        f.append("unbalanced curly quotes")
    if text != text.rstrip():
        f.append("trailing whitespace")
    return f

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file"); ap.add_argument("--backup", required=True); ap.add_argument("--edits", required=True)
    ap.add_argument("--section"); ap.add_argument("--must-contain")
    ap.add_argument("--allow-em-dash", action="store_true"); ap.add_argument("--allow-contractions", action="store_true")
    ap.add_argument("--allow-first-person", action="store_true")
    args = ap.parse_args()

    with open(args.edits, encoding="utf-8") as f:
        edits = json.load(f)
    new_blocks = load_blocks(args.file); old_blocks = load_blocks(args.backup)
    new_text = full_text(new_blocks)
    findings = []

    # 1. new once, old absent
    for i, e in enumerate(edits, 1):
        new = e.get("new"); old = e.get("old")
        if new:
            n = new_text.count(new)
            if n != 1:
                findings.append(f"edit {i}: new text found {n} times (want 1): {new[:80]}")
        if old and not (new and old in new):
            if old in new_text:
                findings.append(f"edit {i}: old text still present: {old[:80]}")

    # 2. diff confined to section
    ok = [t for _, t in old_blocks]; nk = [t for _, t in new_blocks]
    sm = difflib.SequenceMatcher(None, ok, nk, autojunk=False)
    changed = []  # (heading, text) of blocks added or changed
    outside = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        for h, t in new_blocks[j1:j2]:
            changed.append((h, t))
            if args.section and h != args.section:
                outside += 1; findings.append(f"changed outside section [{h}]: {t[:80]}")
        for h, t in old_blocks[i1:i2]:
            if args.section and h != args.section and tag == "delete":
                outside += 1; findings.append(f"removed outside section [{h}]: {t[:80]}")

    # 3. mechanics on changed text only
    for h, t in changed:
        for m in mechanics(t, args):
            findings.append(f"mechanics [{h}] {m}: {t[:80]}")

    # 4. ruled facts present
    if args.must_contain:
        with open(args.must_contain, encoding="utf-8") as f:
            for line in f:
                p = line.strip()
                if p and p not in new_text:
                    findings.append(f"ruled fact missing: {p[:80]}")

    print(f"edits checked: {len(edits)}; blocks changed: {len(changed)}; outside section: {outside}")
    for x in findings:
        print("FAIL " + x)
    print("CLEAN" if not findings else f"{len(findings)} finding(s)")
    sys.exit(0 if not findings else 1)

if __name__ == "__main__":
    main()
