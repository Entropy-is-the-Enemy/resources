---
name: safe-workbook-edit
description: >
  Changes a live .xlsx or .xlsm workbook that other people depend on (formulas, macros, styles, data
  validation, conditional formats, named ranges, pivots) by editing the sheet XML inside the zip directly,
  then proves that only the intended cells changed. Trigger on "add these rows to the shared workbook",
  "update the budget sheet without breaking it", "append entries to the tracker spreadsheet", or any
  scripted write to a spreadsheet a team opens in a desktop spreadsheet app. Does NOT build new workbooks,
  restructure sheets, add formulas or pivots, or handle read-only reporting (use a read-only script for that).
---

# Safe Workbook Edit

## What this skill does

A shared workbook is infrastructure. People rely on its macros, dropdowns, highlighting rules and formulas. The common way to script a change, loading the file with a general spreadsheet library and saving it again, rewrites the whole package. That resave commonly drops or alters things the library does not fully model: VBA projects (unless explicitly kept), data validation and conditional format extensions, charts, pivot caches, comments, and styles.

This skill avoids the resave. You open the workbook as a zip, edit only the `<c>` cell elements you mean to change, copy every other part through byte for byte, and then diff every cell of every sheet before and after. If anything other than your target cells moved, you restore and stop.

## When this applies

- The file is .xlsx or .xlsm and someone else opens it in a desktop spreadsheet app.
- The change is a small, bounded write: add rows, fill cells, correct values.
- You can name the exact cells you intend to change before you start.

If the change needs new formulas, new sheets, or structural edits, stop and hand it to a human in the app.

## How it works

1. **Check preconditions.** If an Office lock file (`~$` plus the workbook name) sits beside the file, or the file was modified in the last 5 minutes, someone may have it open: stop and report. Then search the target sheet for the rows you are about to add (for example by their unique ID column). If they already exist, report "already present" and stop. Every pass must be safe to rerun.

2. **Make a restore point.** Copy the original into a dated archive folder beside it, for example `_archive/2026-03-14/Budget.xlsm`, and record its SHA-256. Never edit the only copy.

3. **Locate the sheet part.** `xl/workbook.xml` lists `<sheet name="..." r:id="rIdN">`. `xl/_rels/workbook.xml.rels` maps `rIdN` to a part such as `worksheets/sheet3.xml`. Read `xl/sharedStrings.xml` so you can resolve text: a cell with `t="s"` holds an index into its `<si>` list.

4. **Find the next empty pre-styled rows.** Shared workbooks usually carry rows that exist with style attributes but no values (`<c r="A41" s="12"/>`). Write into those so new rows inherit borders, number formats, validation and conditional formatting ranges. If no pre-styled rows remain, stop: extending ranges is a structural change.

5. **Convert types deliberately.**
   - Dates are serial numbers in the 1900 date system: serial 1 is 1900-01-01. The format treats 1900 as a leap year (serial 60 is a nonexistent 1900-02-29), so from serial 61 onward naive day counting from 1900-01-01 is off by one. For any modern date, `serial = (date - 1899-12-30).days`. Check your conversion against one existing row before writing.
   - Codes with leading zeros, account strings, or IDs that look numeric go in as text. `00417` written as a number becomes `417`.
   - Prices and quantities go in as numbers, never as text.

6. **Write the cells.** Replace only the target `<c>` elements. Keep each cell's `s` attribute. For text, use an inline string (`t="inlineStr"` with `<is><t>...</t></is>`), or append an `<si>` to sharedStrings and update `uniqueCount` (number of `<si>` entries) and `count` (total references across the workbook). Do not compute formula results yourself. Instead set `<calcPr fullCalcOnLoad="1"/>` (add the attribute to the existing `calcPr` in `workbook.xml`) so the app recalculates every formula on open.

7. **Repackage.** Write a new zip that copies every unchanged entry byte for byte, in the original order, and replaces only the parts you edited. Save to a temp name, then swap it into place.

8. **Prove the change.** Extract every cell of every sheet from the restore point and from the new file as `(sheet, ref) -> (style, type, formula, value)` and diff. The set of changed keys must equal the set of intended cells exactly. Any other difference, including a lost style index or a changed formula: restore from the restore point and stop.

9. **Smoke test.** The zip opens, every XML part parses, and optionally a headless converter opens the file without error. Report the result as "changed, not yet opened in the app". A human opens and saves it once in the real application, which also completes the recalculation.

10. **Log the pass.** Append one line to a pass log beside the workbook.

## Snippets

Locate a sheet's XML part (standard library only):

```python
import zipfile, xml.etree.ElementTree as ET
M = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
z = zipfile.ZipFile(path)
wb = ET.fromstring(z.read("xl/workbook.xml"))
rid = next(s.get(R + "id") for s in wb.iter(M + "sheet") if s.get("name") == "PO Log")
rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
target = next(r.get("Target") for r in rels if r.get("Id") == rid)
part = "xl/" + target.lstrip("/").removeprefix("xl/")
```

Parse to read; attribute order varies between writers, so do not locate things with ordered regexes.

Build an inline-string cell that keeps the row's style:

```python
from xml.sax.saxutils import escape
def text_cell(ref, style, text):
    return f'<c r="{ref}" s="{style}" t="inlineStr"><is><t>{escape(text)}</t></is></c>'
```

Dump every cell for the diff:

```python
import xml.etree.ElementTree as ET
NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
def dump(path):
    out, z = {}, zipfile.ZipFile(path)
    for n in z.namelist():
        if n.startswith("xl/worksheets/") and n.endswith(".xml"):
            for c in ET.fromstring(z.read(n)).iter(NS + "c"):
                f, v = c.find(NS + "f"), c.find(NS + "v")
                t = "".join(x.text or "" for x in c.iter(NS + "t"))
                out[(n, c.get("r"))] = (c.get("s"), c.get("t"),
                    f.text if f is not None else None,
                    v.text if v is not None else t)
    return out
changed = {k for k in dump(old).keys() | dump(new).keys()
           if dump(old).get(k) != dump(new).get(k)}
assert changed == intended, changed - intended
```

Cache the two dumps in real use; the shorthand above reparses for brevity. If you appended to sharedStrings, resolve `t="s"` indexes to text before comparing, or existing cells will look unchanged while new ones look odd.

## Rules

- Never load-and-resave the workbook with a general spreadsheet library.
- Never write while a lock file exists or within 5 minutes of the last modification.
- Never edit without a restore point and its recorded hash.
- Never drop or change a cell's `s` attribute.
- Never write a computed formula result into a `<v>`. Set `fullCalcOnLoad="1"` and let the app calculate.
- Never store an identifier as a number or an amount as text.
- Any unintended diff means restore and stop. Do not try to patch the patch.
- Never call the job done until a human has opened and saved it in the app.
- Other automations that only read the workbook use a read-only script that opens the zip and never writes.

## Pass log format

One line per pass in `workbook-pass-log.md` beside the workbook:

```
2026-03-14 | Budget.xlsm | sheet "PO Log" rows 41-43 added (PO-0417, PO-0418, PO-0419) | restore: _archive/2026-03-14/Budget.xlsm sha256 3f9a... | diff: 18 cells changed, 18 intended, 0 other | status: changed, not yet opened in app
```

## Example

**Input.** A small school district keeps `District Budget FY.xlsm` on a shared drive. It has macros that build monthly reports, a dropdown for funding source, and red highlighting when a line exceeds its allocation. You are asked to add three purchase orders: classroom chromebooks, science lab supplies, and a bus tire replacement.

**What you do.**
1. No `~$District Budget FY.xlsm` exists and the file was last saved yesterday. None of PO-0417 to PO-0419 appear in column A.
2. Copy the file to `_archive/2026-03-14/` and record its hash.
3. `workbook.xml` maps "PO Log" to `rId4`, which the rels file points to `worksheets/sheet4.xml`.
4. Rows 41 to 60 exist with styles and no values. Use rows 41 to 43.
5. Order dates convert to serials (2026-03-10 becomes 46091; existing row 40 shows 2026-03-02 as 46083, which matches). Account code `0150-610` goes in as text. Amounts go in as numbers.
6. Write 18 cells (six columns by three rows), keeping each `s`, and set `fullCalcOnLoad="1"`.
7. Repackage, with `vbaProject.bin` and every other part copied unchanged.
8. Diff: 18 changed keys, all intended, none other.
9. Zip opens, all XML parses.

**Output.** A short report: "Added PO-0417 to PO-0419 to PO Log rows 41 to 43. Diff clean (18 of 18 intended). Restore point at `_archive/2026-03-14/`. Changed, not yet opened in the app: please open, let it recalculate, and save once." Plus the pass log line.
