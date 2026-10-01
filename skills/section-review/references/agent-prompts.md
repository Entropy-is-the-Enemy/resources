# Agent prompts

Verbatim briefs for the three agent roles. Fill the bracketed slots; do not paraphrase the rest.
Every agent gets the pack folder path and the constraints file path. Agents write only where
the brief says; the orchestrator does the apply.

## 1. Diagnosis agent (always)

```
Read the pack and constraints in full: [pack path], [constraints path].
Scope: [section title] in [document].

(1) Structure and readability. Per paragraph: the question it answers, word count, figure count,
whether it lands or trails, what it repeats from other paragraphs or documents in the pack. Then:
is the order the order the reader needs; where does the reader get lost; how does the form compare
with the sibling section in the pack.

(2) Facts and consistency. Recompute every sum, difference, and percent from the printed figures.
Check every figure and claim against the pack. Quote exact text for anything unsupported,
contradictory, stale, or on a different basis from the same figure elsewhere; when two figures
differ by basis, say so and name both bases.

(3) Mechanical checks per the constraints file.

(4) Verdict, one of: PRINT AS IS / LIGHT EDIT / RESTRUCTURE.
  LIGHT EDIT: numbered list, one line each, exact before and exact after text.
  RESTRUCTURE: the new order, headings, what is cut; no prose draft.
Then the strongest reason for the verdict and the strongest objection to it.

Quote text exactly. No em dashes in your output. Save your full report to
[pack path]/diagnosis.md and write to no other file.
```

## 2. Style agent (RESTRUCTURE only; load the `sounds-like-you` skill first)

```
Read the pack, constraints, and [pack path]/diagnosis.md in full.
Produce a full restructured draft of [section title] in the author's voice per the loaded style
skill, applying every diagnosis fix (order, cuts, corrections). Facts: only what the pack supports;
every constraints-file fact present in substance; every hedge kept. Register per constraints.
After the draft, list each change you made beyond the diagnosis fixes with a one-line reason.
Mark each paragraph with its style tag from the pack ([Normal], [ListBullet], [Heading2], etc.).
Save to [pack path]/draft-style.md and write to no other file.
```

Optional `narrative-register` variant (only if the author asked for it or the piece is narrative): same brief,
load `narrative-register` instead, add "The style draft's facts are the ceiling: add none. Leave lists,
specs, figures, and hedges literal; work only on narrative prose." Save to `draft-voice.md`.

## 3. Verifier / synthesizer agent

```
Read the pack, constraints, [pack path]/diagnosis.md, and every draft in [pack path]
(draft-style.md[, draft-voice.md]).

Part A. Verify each draft line by line. Every claim traces to the pack or to the constraints
file; for any fact imported from a source document that the section did not previously print,
say whether the source supports it exactly and whether a reader needs it to decide anything;
default to dropping it. Every constraints-file fact present in substance. Consistency with every
other place the pack shows the subject appearing. Mechanics per constraints.

Part B. Resolve every difference between drafts with a one-line reason. Rules: plain over vivid;
shorter when the facts are equal; keep every hedge; drop imported detail that changes no reader
decision; never resolve an internal contradiction by choosing, list it for the author.

Part C. Produce, in this order: findings per draft; resolutions; the FINAL text with style tags;
items only the author can confirm (numbered); a self-check (word count before and after,
mechanics, each constraints fact located by paragraph, imported facts kept and why).

Save to [pack path]/final.md and write nothing else. No em dashes in your output.
```

## Notes on running them

- Diagnosis and verifier are read-only on the document; only the orchestrator edits it.
- One section per diagnosis agent. Three short sections can share one agent if they share a pack.
- The prompts above were the ones used on the run that produced this skill; if a change to them
  improves results, change them here, not ad hoc in the session.
