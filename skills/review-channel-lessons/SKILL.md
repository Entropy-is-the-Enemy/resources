---
name: review-channel-lessons
description: >
  Mines the critiques, corrections and instructions that OTHER reviewers (editors, legal, accessibility,
  approvers) leave in team review channels or comment threads, and turns them into durable one-lesson-per-file
  "lesson atoms" so writers and designers stop repeating mistakes reviewers already caught. Runs weekly with a
  per-channel cursor, refines existing atoms instead of duplicating them, flags atoms ready for graduation, and
  sends the owner one summary message. Trigger on "harvest the review channel", "what did reviewers catch this
  week", "turn reviewer feedback into lessons", or a scheduled weekly run. Does NOT mine your own edits to your
  own drafts, does NOT merge general reference material into a knowledge base, does NOT post in review channels,
  and does NOT graduate or move anything on its own.
---

# Review Channel Lessons

## What this skill does
Reviewers catch the same problems week after week: the wrong date format, a missing legal line, alt text left
blank. The catch lives in a thread and dies there. This skill reads those threads on a schedule, pulls out the
critiques, and files each distinct lesson as a short atom file with its evidence. Over time the atoms become the
team's working rulebook, built from what reviewers actually said rather than what someone remembered.

## When this applies
- A weekly scheduled run over your configured review channels.
- An on-demand catch-up after a busy launch or a cursor gap.
- Not for approvals-only channels, and not for your own edit history.

## Configure first
- **Channels:** the review channels or comment-thread sources to read, each mapped to a default scope.
- **Lessons folder:** `lessons/<scope>/<medium>/` plus `lessons/house-rules/<medium>/` for cross-scope lessons.
- **Raw folder:** `raw/<channel>/<run-date>.jsonl` (append-only).
- **Cursor file:** per channel, `last_processed_ts` and `last_run_date`.
- **Spec file:** the taxonomy keys, each new key dated when added.
- **Owner:** the one person who receives the weekly summary by direct message.

## How it works
1. **Set the window.** For each channel, window = cursor to now. Empty cursor: the last 8 days. Also re-read
   threads whose parent message falls up to 14 days before the window start, because replies land after the
   parent's date. Process only replies inside the window.
2. **Extract.** Keep critiques, corrections, catches, instructions and process direction. Skip approvals,
   "looks good", thanks, status posts and pure routing ("tagging legal"). For each kept item, append one JSON
   line to the raw file: `ts`, `channel`, `permalink`, `role`, `kind`, `scope`, `medium`, `paraphrase`, and an
   optional `quote` of 25 words or fewer. `kind` is one of: `instruction`, `shipped-error` (it went out wrong),
   `correction`, `preference`, `process`.
3. **Assign roles, not names.** Role is set by the function shown in the thread: author, proofreader, editor,
   legal reviewer, designer, lead, approver. A person's name never enters a raw line or an atom.
4. **Advance the cursor** to the newest processed timestamp once extraction for that channel is written.
5. **Refine against existing atoms.** For each new record, search atoms by scope and lesson (grep `tags`, the
   title and `use_when`). Then:
   - **Agrees:** add evidence, bump `evidence_count`, set `last_seen`.
   - **Changes the guidance:** rewrite the Answer, add a dated Evolution line with the old guidance, set
     `guidance_state: evolving`.
   - **Contradicts a current instruction** with no clear governing authority: add a numbered Open question,
     set `guidance_state: contested`.
   - **No match:** create a new atom only if there are 2 or more records for the lesson, or 1 record of kind
     `instruction` or `shipped-error`. A lone `preference` with no match stays in raw only.
6. **Newest governing instruction wins.** When an authorized reviewer's newer instruction supersedes older
   guidance, the Answer takes the new rule and the replaced guidance moves to Evolution, dated.
7. **Rebuild the indexes** (by scope, by medium) and run the check script. It must pass before the run ends.
8. **Flag graduation.** An atom is ready when `evidence_count >= 3`, `guidance_state: current`, no Open
   questions, the Answer unchanged for 90 days (newest Evolution date, or `first_seen` if none), and the check
   passes. List ready atoms newest-ready first; mark those that became ready this run.
9. **Send the weekly summary** (below) to the owner. This is the only message the run posts.

## Atom format
```
---
title: Write service changes with day, date and time range
scope: bus-network
medium: [print, web, social]
lesson_type: accuracy
guidance_state: current        # current | evolving | contested
first_seen: 2026-08-04
last_seen: 2026-10-20
evidence_count: 4
sources:
  - "rider-notices-review, 2026-10-20, editor, <permalink>"
use_when: You are drafting a detour or service change notice that names when it starts or ends.
tags: [dates, service-change]
see_also: [house-rules/general/time-format]
status: active
last_reviewed: 2026-10-27
---
## Answer      the rule as what to do; a short do/don't pair if it helps
## Why         what went wrong, generalized, one or two dated examples
## Evolution   dated lines (omit if never changed)
## Resolved conflict   (omit if none)
## Open questions      numbered (omit if none)
## Evidence    max 6 lines: date, channel, role, one-line paraphrase, permalink
```
Write `use_when` as the situation the writer is in, not the topic.

**Taxonomy.** Scope is the product line or team. Medium: email, print, web, social, video, presentation,
general. Lesson types: accuracy, proofing, style guide, naming/trademarks, voice and tone, audience clarity,
design/layout/accessibility, call to action/offer terms, legal/compliance, process/workflow, plus any regulated
type your team needs (safety, medical, and so on). Add a new key only by dating it in the spec file.

## Check script
Your check script fails the run if any atom: exceeds 400 words excluding frontmatter; is missing a required
frontmatter field; has more than 6 Evidence lines; contains a person's name (match against a roster or name
pattern list you maintain); contains a quote over 25 words; has `contested` with no Open questions or Open
questions without `contested`; or breaks your house-style lints (banned characters, banned phrases).

## Rules
- Never post, react or reply in the review channels. One direct message to the owner per run, nothing else.
- Never delete or overwrite a raw line. Raw files are append-only.
- Never copy a critique verbatim as the rule. Paraphrase into guidance; a quote of at most 25 words may appear
  only as evidence.
- 400 words maximum per atom excluding frontmatter, target 150 to 300. Split into two atoms rather than exceed.
- Role classes only, everywhere. No person names in raw, atoms, indexes or the summary.
- **Regulated or expert content** (legal, medical, safety, doctrinal, financial disclosure and the like): tag
  `expert_check: true` and state the guidance only as the reviewer gave it. Never extend, generalize past, or
  invent guidance in these areas.
- Never move, graduate or delete an atom automatically. Graduation is a flag; a human rules.
- When a contradiction has no clear governing authority, do not pick a winner. Mark it contested and ask.

## Weekly summary format
One direct message to the owner:
- Records extracted, per channel.
- Atoms created, updated, evolved, contested (titles).
- The three most important new or changed lessons, one line each.
- Newly graduation-ready atoms.
- Anything contested that needs a ruling, with the question.

If nothing changed: one line, "No new reviewer lessons this week (N records read, 0 kept)."

## Example
**Setup.** A city transit agency's communications team has three review channels: rider notices, station
signage, and social posts. An editor, a legal reviewer and an accessibility reviewer leave corrections there.

**Input this week (paraphrased).**
- Rider notices: the editor flags "Sat 10/12" in a detour notice and asks for "Saturday, Oct. 12, 6 a.m. to
  11 p.m." A reply four days later says last month's notice went out with no end time and riders called in.
- Social: the accessibility reviewer asks for alt text describing the map's detour path, not "map image".
- Social: the legal reviewer says fare-promotion posts must include the end date and "while funds last" is not
  allowed. An older atom said "while funds last" was acceptable.
- Signage: the lead tells a designer to route all platform signs through accessibility review before print.
- Several "approved, ship it" posts and two "thanks!" replies.

**What the skill does.**
- Skips the approvals and thanks. Writes 5 records across three raw files: one `correction`, one
  `shipped-error`, one `instruction` (alt text), one `instruction` (legal), one `process`.
- The date record matches the existing atom "Write service changes with day, date and time range": evidence
  added, `evidence_count` 3 to 5 (the correction and the shipped error each count).
- Alt text: no match, but kind `instruction`, so a new atom in `social/` with lesson type
  design/layout/accessibility.
- Legal: the legal reviewer governs offer terms, so the newest instruction wins. The fare-promotion atom's
  Answer is rewritten, the old "while funds last" guidance moves to Evolution dated 2026-10-24, state set to
  `evolving`, and `expert_check: true` is kept. No new legal guidance is added beyond what the reviewer said.
- Signage process: a new atom in `signage/general/` (lesson type process/workflow).
- The check passes. One older atom on station name spelling crosses 90 days unchanged and becomes ready.

**Summary sent to the owner.**
> Records: rider-notices 2, signage 1, social 2. Created: "Describe the detour path in map alt text",
> "Route platform signs through accessibility review before print". Updated: "Write service changes with day,
> date and time range". Evolved: "Fare promotions state the end date". Top lessons: (1) fare promos need an end
> date, no "while funds last"; (2) service change notices need a full time range, one shipped without it;
> (3) map alt text describes the path. Newly graduation-ready: "Use the official station name on first
> reference". Contested: none.
