---
name: section-review
description: >-
  Multi-agent review of one section of a formal document before the author proofs or sends it: a
  diagnosis agent recomputes every figure, checks every claim against a review pack, and returns
  PRINT AS IS / LIGHT EDIT / RESTRUCTURE with quoted evidence; on RESTRUCTURE, style and verifier
  agents produce a traced FINAL; on the author's go the edit is applied in place behind a backup, verified
  deterministically, and logged. Trigger on "/section-review", "is this section worth proofing",
  "does this section need work", "this reads worse than before", "review this section", "proof
  pass on [section]", or when proofing a business plan, memo, proposal, investor update,
  case write-up, or any deadline document whose readers will check the numbers. One section at a
  time. NOT whole-document fact verification (airtight, run after), NOT broad AI-output QC
  (trace-review), NOT hostile-reader testing (red-team-reflex), NOT answer-first reordering
  (answer-first), NOT building from nothing (line-by-line).
---

# section-review

One question: is this section worth the author's proofing time as written, or does it need work first?
Answer with evidence, then on the author's go do the work in place and log it. The unit is one section.
House constraint: no em dashes in anything this skill writes.

Read `references/lessons.md` before briefing the first agent. Prompts are verbatim in
`references/agent-prompts.md`; the constraints file shape is `references/constraints-template.md`;
`scripts/` holds the docx helpers and the verifier.

## 0. Pack

1. Read what governs the project: memory file, handoff, README, prior rulings. Rulings already
   taken are not re-asked.
2. Re-read the document from disk. Authors edit between messages; a text dump from earlier is stale.
3. Build the pack in a scratch folder (`<scratch>/section-review/<section-slug>/`):
   - the section text with paragraph and style tags (`scripts/docx_tools.py dump FILE`, or the
     markdown as is)
   - a sibling section that sets the form the reader expects
   - every other place the document mentions the same subject (grep the dump)
   - related documents that must stay consistent
   - the source the section was built from (research memo, model, data export, build log)
4. Write `constraints.md` from the template: audience, register, number and naming conventions,
   facts on the author's authority that must survive in substance, rulings not to re-open, sources, the
   project's backup pattern and edit log path. Anything not in the file is not enforced.

## 1. Diagnosis (always)

One agent per section, read-only, briefed with the diagnosis prompt. It reports, quoting exact text:

- **Structure:** per paragraph, the question it answers, word and figure counts, lands or trails,
  what it repeats elsewhere; whether the order is the reader's order; where the reader gets lost;
  form against the sibling.
- **Facts and consistency:** every sum and percent recomputed from printed figures; every claim
  checked against the pack; unsupported, contradictory, stale, or different-basis figures flagged
  with the basis named.
- **Mechanics** per the constraints file.
- **Verdict:** PRINT AS IS / LIGHT EDIT (numbered, exact before and after) / RESTRUCTURE (new
  order, headings, cuts; no prose). Strongest reason and strongest objection.

Output saved to `diagnosis.md` in the pack. Read it whole before deciding anything.

## 2. Style passes (RESTRUCTURE only)

- **Style agent** with `sounds-like-you` loaded: full restructured draft in the author's voice applying
  every diagnosis fix; lists each change beyond them with a reason. Saves `draft-style.md`.
- **Voice agent** with `narrative-register` loaded, only if the author asked for it or the piece is narrative: register
  pass on narrative prose; the style draft's facts are the ceiling; lists, specs, figures, and
  hedges stay literal. Saves `draft-voice.md`.
- **Verifier / synthesizer:** traces every claim in every draft to the pack; drops imported detail
  that changes no reader decision; keeps every hedge and every author-authority fact; resolves
  differences with one-line reasons (plain over vivid, shorter when facts are equal); produces the
  FINAL with style tags plus the numbered list of items only the author can confirm. Saves `final.md`.

LIGHT EDIT skips this section; the diagnosis list is the edit list.

## 3. Present to the author and wait

In this order, nothing else:

1. Verdict, one line.
2. Why, three to five bullets quoting the diagnosis.
3. The FINAL text (restructure) or the numbered edit list (light edit).
4. Decisions only the author can make, numbered. Internal contradictions and different-basis figures go
   here as the author's rulings, never resolved by guess.
5. What apply will do: file, backup name, script name, verify command.

Wait for go. "Go" plus answers to the numbered items is the trigger; partial answers mean apply
only what is unblocked and list what waits.

## 4. Apply in place

1. Back up first: `<name>.pre-<tag>-<YYYYMMDD>-<n>.<ext>` beside the file, or the project's
   pattern from the constraints file.
2. Write an `edits.json` (`[{"old": ..., "new": ...}]`) from the edit list or FINAL; it drives
   the verifier and is the record of what changed.
3. Apply with the right tool:
   - **docx:** a short script importing `scripts/docx_tools.py`. Match paragraphs by full visible
     text (`para_replace`, or `replace_para` + `mkpara` with `ppr_of` when formatting is mixed);
     clone the sibling's `pPr` for new bullets; set table cells by index with `cell_set`, which
     asserts the current text first. Never string-replace a number in raw XML.
   - **markdown / plain text:** edit directly with the file tools.
   Save the apply script in the pack; name it in the log.
4. Verify: `scripts/verify_edits.py FILE --backup BACKUP --edits edits.json --section "<heading>"
   [--must-contain facts.txt]`. It asserts every new text present once, every old text absent,
   zero changed blocks outside the section, mechanics clean on changed text, every ruled fact
   present. A FAIL is fixed and re-run, never explained away.
5. Inspect the file, not only the dump, if a table or list style was touched.

## 5. Log

Append to the project edit log and the handoff (if one is open): section, verdict, what changed,
figures corrected, rulings taken, backup name, apply script name, verify result, what stays open.
Project memory gets one line only if a ruling or lesson will matter next session. Report to the author in
five lines.

## Rules

- **Read-only until go.** Agents never touch the document; only step 4 edits, only after the author's go.
- **Evidence or nothing.** Every finding quotes exact text; every arithmetic flag shows the
  recomputation. "Reads awkwardly" without a quoted line is not a finding.
- **Bases before contradictions.** Two figures that differ are checked for basis first; only
  same-basis disagreement is a contradiction.
- **Source before change.** An unsourced figure is grepped in build logs, briefs, audits, and the
  source document before a change is proposed.
- **Restructure is the expensive verdict.** It is where new errors come from; on deadline, the
  agent's objection to its own RESTRUCTURE verdict is read before the verdict is accepted.
- **Scope holds.** One section. A finding about another section is reported as a one-line pointer,
  not fixed.

## Boundaries

- **NOT airtight.** Airtight is whole-document deep fact and number verification with confidence
  calibration before something leaves under the author's name. This skill checks one section's facts as
  part of a structure verdict. When the document is done, run airtight on the whole; do not run it
  inside this unit.
- **NOT trace-review.** Trace-review is a broad five-dimension QC of AI output. This is a
  structural and arithmetic pass on a section of a human document with a decision at the end.
- **NOT red-team-reflex.** That asks how a hostile reader attacks the argument. This asks whether
  the section is worth proofing as written.
- **NOT answer-first.** That reorders a decision document answer-first and never touches
  facts. This may reorder a section, but only as one outcome of a diagnosis that also checks the
  numbers, and it applies the edit.
- **NOT line-by-line.** That builds. This reviews and repairs an existing section.
- **NOT sub-agent-ops.** The agent pattern here is fixed (diagnosis, optional style and voice,
  verifier); no run design is needed. Spawn directly.
- **sounds-like-you and narrative-register** are loaded by the style and voice agents when a
  RESTRUCTURE calls for them; they are not separate passes.
