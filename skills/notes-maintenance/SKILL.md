---
name: notes-maintenance
description: >
  Keeps a large shared folder of markdown notes current through unattended scheduled runs (a morning write
  pass, midday check passes) and an on-demand review with the folder's owner, without letting automation
  rewrite meaning. Trigger on "run the morning pass", "check the notes folder", "what's in the review queue",
  "review the queue with me", or a scheduled maintenance run. Does NOT delete files, send messages, edit
  schedules, or make any content edit beyond the two mechanical kinds listed below.
---

# Notes Maintenance

## What this skill does
A notes folder used by several people drifts: reference files bloat, the same fact lives in three places, figures go stale, decisions get buried. This skill runs maintenance on a schedule while keeping meaning under human control. Unattended runs do only two mechanical edits, each proven lossless. Everything else becomes a proposal on a generated review-queue page, acted on only when the owner rules on it.

## When this applies
- **Write pass** (early morning, once a day): the only run that edits content.
- **Check pass** (midday, e.g. twice): read-only except generated pages and stale indexes.
- **Review with the human** (on demand): works the queue item by item.

## Configure first
Set these once: the folder root; the age cutoff for condensing (e.g. 60 days); the reference-file size limit (e.g. 50 KB); the name of each folder's history-log file; the run log path; the generated page paths (health dashboard, rulings ledger, review queue); the canonical figures file; and whether the folder is under version control.

## The toolkit
One script, one command per call. If your tool calls have time limits, never chain commands; a scan of a big folder can take about 90 seconds.

- `lock`: create a lock file with run type and start time. If one exists, print "run in progress" with its contents and exit non-zero.
- `unlock`: remove the lock file. Safe to call if absent.
- `scan`: walk the folder, record per-file path, size, modified time, dated sections, and top-block date. List files modified in the last 15 minutes as SKIPPED (a live session may be editing them). Every later command honors this skip list.
- `substitute --rule <id> [--dry]`: apply one owner-ruled vocabulary substitution (e.g. a vendor brand name to a generic term) everywhere, leaving IDs and times untouched. Copies each file before writing.
- `condense [--dry | --apply <files>]`: in reference files over the size limit, move dated sections older than the cutoff, verbatim, into that folder's history-log file and leave one pointer line ("Sections before DATE moved to history-log.md"). Copies each file before writing. Dry mode prints, per file, size before and after and a missing-token count.
- `health`: write the health dashboard.
- `rulings`: write the rulings ledger.
- `queue`: write the review queue.
- `lint`: report broken pointers, malformed headings, stray backup files, and orientation files missing per folder. Never fixes anything.
- `index --check | --refresh <folders>`: per top-level folder, report whether its index file is stale; refresh only named folders. Never creates an index.

**Token-set check (both edit commands).** Extract every number, date, and ID from the old text. Each must appear in the new text plus the receiving file. If any token is missing, refuse to write that file and report the missing tokens.

## How it works

### Write pass
1. `lock`. If another run is in progress, stop and say so.
2. `scan`.
3. `substitute` for each ruled rule.
4. `condense --dry`, then `condense --apply` with only the files whose check shows 0 missing.
5. `index --check`, then `index --refresh` with only the stale folders.
6. `rulings`, `health`, `queue`.
7. Append one dated entry to the run log (format below).
8. `unlock`.
9. Reply in a few short lines, then the top 5 open action items, overdue first.

### Check pass
1. `lock`, `scan`, `index --check`, `index --refresh` on stale folders, `health`, `queue`, `unlock`.
2. No content edits, no run-log entry.
3. Report only what changed since the morning: new overdue items, new intake items, newly oversized files, indexes refreshed. If nothing changed, one line.

### Review with the human
For each queue item:
1. Send the plan: the facts, the exact proposed lines, and for a duplicated fact, the one home it should live in.
2. Ask, recommended option first. Act only on a ruling.
3. Before each edit, copy the file to `Archive/superseded-DATE/` beside it.
4. After each edit, prove nothing was lost: run the token-set check against the archived copy. The only tokens allowed to disappear are ones the ruling explicitly retires.
5. Record the ruling in the owner's exact words. Never summarize it into different words.
6. If the folder is not under version control, record every move in a dated manifest (old path, new path, reason).
7. If the owner rules a figure, add a row to the canonical figures file.

## Generated pages
- **Health dashboard**: open action items (overdue first), intake count, oversized files, stale top blocks, folders missing orientation files, stray backup files, lint results, broken pointers.
- **Rulings ledger**: every line marked RULED, STANDING, or TRAP anywhere in the folder, verbatim, with file and line number. Every past decision has one place to be found.
- **Review queue**: every proposal, each with file, reason, and exact proposed text. Proposal types: top-block rewrites, condense plans the script cannot do, one-home moves of duplicated facts, figure corrections, lint fixes, new index files, memory index fixes.

## Canonical figures file
A TSV with three columns: `label`, `wrong_pattern`, `ok_pattern`. `health` flags any line matching `wrong_pattern` unless it also matches `ok_pattern` (e.g. a line that quotes the old figure as history). Rows are added only from the owner's rulings.

## Run log entry
```
## 2026-03-14 write pass
Changed: substitution R2 in 4 files; condensed instrument-log.md
Size: instrument-log.md 71 KB -> 38 KB
Indexes refreshed: protocols/, meetings/
Counts: 3 overdue, 7 intake, 2 oversized, 11 queue items
Skipped: decisions.md (modified 6 min before scan)
```

## Rules
- Every run starts with `lock` and ends with `unlock`.
- If any command fails: `unlock`, stop, report the error verbatim. Do not retry or work around it.
- Skip any file modified in the last 15 minutes.
- Unattended content edits are limited to the ruled substitution and condensing. Both copy the file first and both refuse on any missing token.
- Never create an index unattended; missing ones go to the queue.
- Everything else is a proposal until the owner rules.
- Never delete a file, send any message, or edit any schedule.

## Example
A university lab keeps a shared notes folder: `protocols/`, `meetings/`, `instruments/`, and `decisions.md`, used by the PI and six students. The PI ruled last month: replace the centrifuge maker's brand name with "the benchtop centrifuge" everywhere.

**Morning write pass, 05:30.** `lock` succeeds. `scan` takes 80 seconds and marks `decisions.md` SKIPPED (a student edited it at 05:22). `substitute` changes 4 protocol files; "Spin at 4,000 rpm for 12 min (run ID CF-0412)" keeps every number and ID. `condense --dry` reports `instruments/instrument-log.md` at 71 KB with 0 missing and `meetings/notes.md` with 1 missing (sample ID S-117), so only the instrument log is applied and the notes file goes to the queue as a condense plan. Its pre-January sections move verbatim to `instruments/history-log.md`. `index --check` flags `protocols/` and `meetings/`; both refresh. `analysis/` has no index, so it goes to the queue. The reply:

```
Write pass done. 4 files substituted, 1 condensed (71 KB to 38 KB), 2 indexes refreshed.
Skipped decisions.md (live edit). Queue: 11 items.
Top 5: 1. OVERDUE calibrate plate reader (due Mar 10) ...
```

**Midday check pass.** Nothing edited. Reply: "Since morning: 1 new intake note, protocols/ index refreshed."

**Review with the PI.** Queue item: the freezer setpoint appears as -80 C in `protocols/storage.md` and -70 C in two meeting notes. You propose `protocols/storage.md` as the one home, show the exact replacement line for each meeting note (a pointer to the home), and recommend that option first. The PI rules: "-80 C is correct; -70 C was the old freezer." You archive both meeting notes to `meetings/Archive/superseded-2026-03-14/`, edit, run the token check, record the ruling verbatim, write the manifest row, and add a figures row: `freezer setpoint`, `-70 C`, `old freezer`.
