---
name: tasks-of-record
description: >
  Operate a personal task system where one plain-text file is the single source of truth and every app
  is a read-only mirror of it. Covers the row schema and status vocabulary, stable IDs that are never
  reused, a capture buffer that keeps raw input out of the curated list, an inbox-as-queue discipline
  where labels and archiving hold the state, and a fingerprint-hash check that detects out-of-band
  edits to a mirror before a one-way sync overwrites them. Trigger on "what's on my list," "add this to
  my tasks," "why do these keep coming back," "my task app and my notes disagree," "set up my task
  system," or "triage what I captured." Reads and writes one task file and reports what it changed.
  Does NOT decide your priorities for you, plan a quarter, manage a team's work, or run a project
  schedule with dependencies.
---

# Tasks of Record

## What this skill does

Most personal task systems fail at the same seam. The list lives in an app. Work happens somewhere
else: a text file, a notebook, an inbox. Opening the app is an extra step, so it gets
skipped, so the app drifts, so it stops being trusted, so it gets opened even less. The system does
not collapse dramatically. It just quietly stops being true.

The fix is to stop trying to keep two systems in agreement.

**One file is the record. Everything else is a mirror, and mirrors are read-only.** Conflict resolution
becomes trivial, because one side always wins by definition. The mobile app is still there, still
useful, still glanceable on a train. It just has no authority.

## The file

Plain text or markdown, in whatever folder you actually work in. One table. Seven columns, fixed:

| Column | Rule |
|---|---|
| **ID** | Area prefix plus a number, assigned once, never reused. `WRK-041` stays `WRK-041` after it is done, and no future task ever gets that number. |
| **Area** | One of a small fixed set you define. Keep it under about eight, or the set stops sorting anything. |
| **Task** | One line, starting with a verb. If it needs two lines it is a project, and projects get their own row that points at a document. |
| **Status** | From the fixed vocabulary below. Nothing invented in the moment. |
| **Next** | The literal next physical action. "Email Dana the revised span table," not "handle the beam issue." |
| **Waiting on** | A name and a date, or empty. Never a vague "them." |
| **Due** | A real external deadline, or empty. Not an aspiration. Aspirations in this column are why people stop believing the column. |

**Status vocabulary, fixed:**

- `NOW` in progress today. Cap this at three or it means nothing.
- `NEXT` ready to start, nothing blocking.
- `WAITING` blocked on a named person, with a date.
- `SOMEDAY` real but not now. Reviewed weekly, not daily.
- `DONE` finished. Stays in the file until a periodic sweep clears it, which is a batch operation and
  so gated like one.

Three disciplines make the vocabulary hold:

- **`WAITING` requires a name and a date.** A `WAITING` row with neither is a row you are avoiding.
  Force the field and the avoidance becomes visible.
- **A note you sent to yourself is never `WAITING`.** It is in your court. This sounds obvious and is
  the single most common way people hide work from themselves.
- **A stale `WAITING` gets a disposition, not another flag.** Surface one and offer three choices,
  then write the one picked: chase it now, escalate to someone who can break it, or accept it is not
  moving and drop it to `SOMEDAY`. Never surface the same blocked row stale twice with no disposition
  logged.

**Write procedure, in this order:**

1. Locate the row by ID and replace the specific cell by unique match. Never regenerate the file from
   an in-memory copy; a misparse rewrites rows you never touched and there is no second copy.
2. Update that row's timestamp, then the file-level last-modified marker.
3. Only then push the changed rows to any mirror.

**If the write to the file fails, do not push to any mirror. Report the error.** Otherwise the mirror
holds a state the record never held, the exact inversion this design exists to prevent, and the
fingerprint cannot catch it, because the mirror looks internally consistent.

**Confirmation gates**, because completing and deleting are what remove rows from view:

- Never mark a row `DONE` without an explicit yes.
- When the reference is text rather than an ID ("mark the invoice one done"), echo the matched ID and
  the full task line, and get the yes before writing.
- If two or more rows match, list them and ask which. Never take the closest.
- Any batch operation that removes rows states its count and criterion, then waits for a yes.

## The capture buffer

Raw capture and curated list are different things and must not share a section.

Anything arriving fast goes into a `## Inbox` block at the top of the file: no ID, no status, no
schema, just the text. Nothing in the Inbox is a task yet.

Triage moves items out, and triage has exactly four outcomes:

1. **Promote.** It gets an ID, an area, a status, and a next action. It joins the table.
2. **Merge.** It is a detail on an existing row. Fold it in, cite the ID, delete the capture.
3. **Defer.** It is real but not a task yet. It goes to `SOMEDAY` with an ID.
4. **Drop.** Delete it. Say so in the run report, so dropping stays a decision rather than a leak.

Nothing enters the curated table without passing through triage. This is what keeps a capture habit
from destroying the list it is feeding.

## The inbox as the live queue

The second half of the system is the email inbox, treated not as a message store but as the action
queue it already is.

**The state lives in labels and in whether the message is in the inbox at all.**

- A message in the inbox is unhandled. That is the only meaning inbox membership carries.
- Handled means archived. Not read, not starred. Archived, and therefore gone from tomorrow's view.
- Waiting on someone means labeled and archived. It leaves the inbox and is retrievable by label.
  This is the move that stops the same three threads reappearing every morning for a month.
- A follow-up you owe gets its own label and stays in the inbox, because it is yours.

The feedback loop that makes it work: when a task file row moves to `WAITING`, the corresponding
thread gets labeled and archived in the same pass. When a `WAITING` row resolves, the label comes off.
The two surfaces stay aligned because one action updates both, not because anything syncs.

## Mirrors and the fingerprint check

A read-only mirror is only safe if it is actually read-only, and people edit mirrors. They check a box
on their phone. Then the next push silently overwrites it and something real is lost.

So each pushed record carries an ETag-style fingerprint of the fields as they were pushed. Ordinary
optimistic concurrency control, not a new mechanism.

1. **On push**, compute a short hash over the exact field values being written, and store it inside the
   mirror record, in a field nobody reads. Something like `[WRK-041|a3f9c2]`.
2. **On the next push**, recompute the hash from the mirror record's current field values.
3. **If the mirror record carries no stored fingerprint**, there is no baseline and so no evidence of
   an out-of-band edit. Write the fields, attach a fresh fingerprint, and do not flag a conflict.
   Unfingerprinted records are normal: they predate the scheme, or a capture path that does not hash
   wrote them. Only a fingerprint that is present and disagrees is a conflict.
4. **If it matches**, nobody touched the mirror. Overwrite freely.
5. **If it does not match**, someone edited out of band. **Do not overwrite.** Log the conflict with
   the field-level difference, leave the mirror record alone this cycle, and surface it in the report.

The source of truth still wins, always. The fingerprint does not create a two-way sync. It converts
silent data loss into a visible decision, which is all a one-way sync can honestly offer.

## Ranking

When asked what to work on, rank by consequence, not by age or by due date alone. In this order:

- **Deadline.** Hard external dates inside the horizon, soonest first.
- **Dependency.** Work that unblocks someone else outranks work that only serves you.
- **Decay.** Things that get materially harder or more expensive with time.
- **Balance.** Everything else, spread across areas, so one area does not starve for a month.

Surface a small number. A ranked list of thirty is an unranked list.

## Output format

```
TODAY
  NOW      <ID>  <task>                      <due or blocking note>
  NEXT     <ID>  <task>
  WAITING  <ID>  <task>   on <name> since <date>   <age flag if stale>

TRIAGE
  Promoted: <n>   <ID> <- "<capture text>"
  Merged:   <n>   into <ID>
  Deferred: <n>   <ID> to SOMEDAY
  Dropped:  <n>   "<capture text>"

INBOX QUEUE
  Unhandled: <n>
  Owed by you: <n>  <subject, age>
  Waiting on others: <n>  <subject, who, age>
  Stale (over <n> days): <list>

MIRROR SYNC
  Pushed: <n>
  Conflicts: <n>
    <ID> field <name>: file has "<x>", mirror has "<y>". Not overwritten.

CHANGES WRITTEN
  <every edit made to the file, one line each>
```

## Worked example (invented)

**Input:** a freelance structural engineer running three concurrent projects, asking what is on the
list on a Monday morning. Four items sitting in the capture buffer.

```
TODAY
  NOW      BRG-018  Stamp the revised span calcs for the pedestrian bridge   due Wed, hard
  NOW      RES-007  Send Dana the foundation detail                          blocking the contractor
  NEXT     BRG-019  Reconcile the surveyor's grade against the site plan
  NEXT     ADM-012  Renew the professional liability policy                  due in 16 days
  WAITING  RES-005  Soils report                on Kestrel Geotech since Jul 09   17 days, STALE
  WAITING  BRG-016  Fabricator shop drawings    on Meridian Steel since Jul 21    5 days

TRIAGE
  Promoted: 2
    BRG-020 <- "check whether the handrail spec changed in the 2024 code"
    ADM-013 <- "invoice the residential job for June"
  Merged:   1
    into RES-007 <- "Dana asked for the detail in metric too"
  Deferred: 1
    ADM-014 to SOMEDAY <- "look into whether a second license state is worth it"

INBOX QUEUE
  Unhandled: 6
  Owed by you: 1
    "Re: bridge stamp timing" from the county, 3 days
  Waiting on others: 2
    "Soils report status" to Kestrel, 17 days   -> matches RES-005, both stale
    "Shop drawings" to Meridian, 5 days
  Stale (over 14 days): the Kestrel thread and RES-005 are one blockage on two
    surfaces. One nudge clears both. Disposition: chase now.

MIRROR SYNC
  Pushed: 11
  Conflicts: 1
    BRG-016 field Status: file has "WAITING", mirror has "DONE". Not overwritten.

CHANGES WRITTEN
  Added BRG-020, ADM-013, ADM-014
  Merged the metric-units note into RES-007 Next
  Flagged RES-005 stale at 17 days
  Cleared the Inbox block
```

## Boundaries

This runs a personal task file. It does not decide what matters to you, set your goals, plan a quarter,
or tell you which of two real priorities to pick. It ranks by consequence and surfaces the list; the
choosing is yours.

It is not a project manager. No dependency graphs, no critical path, no resource leveling, no team
assignment. A row that needs those things should point at a project document that has them.

It will not write to a mirror when the fingerprint disagrees, even when asked, because that is the one
rule holding the whole one-way arrangement together. It will not complete or delete a row on inference
alone.

## Prior art and attribution

This is a synthesis, not an invention, and the parts are worth naming.

The status vocabulary (NEXT, WAITING, SOMEDAY) and the capture-then-triage Inbox step are adapted from
David Allen's Getting Things Done. Getting Things Done and GTD are registered trademarks of the David
Allen Company. This skill is not affiliated with, endorsed by, or certified by them, and its author is
not a certified GTD coach or trainer. For the original methodology see gettingthingsdone.com. The
specific five-state sequence is close to the long-standing Emacs Org-mode GTD keyword set documented by
Bernt Hansen at doc.norang.ca/org-mode.html.

"One file has authority, apps are mirrors" follows Steph Ango's *File over app* and the local-first
software ideals set out by Kleppmann and colleagues at Ink and Switch.

The mirror fingerprint is an ETag-style conditional write, which is optimistic concurrency control and
decades old.

Other prior art in this space: todo.txt and Taskwarrior, whose IDs are reused when tasks leave the
working set, where here they never are.
