---
name: trace-review
description: >
  Run a TRACE quality-control review on AI-generated output before you share, send, publish, or act on
  it. TRACE is a five-point review: Truth, Relevance, Accuracy of tone and audience, Completeness, and
  Ethics and risk. Use this whenever you want to check, verify, QC, proof, fact-check, pressure-test, or
  sanity-check an AI draft, or ask things like "is this safe to send," "can I publish this," "what's
  wrong with this," "review this output," or "did the AI get this right," even when you do not say the
  word "TRACE." Also trigger when you name any single dimension (truth, relevance, tone, audience,
  completeness, ethics, hallucination, bias, staleness). This is the BROAD first-pass review that
  produces a verify-list and refuses to certify facts. For DEEP single-fact, number, or citation
  verification on a high-stakes piece, escalate to a dedicated fact-verification pass instead. Works on
  any AI output, in any professional field, on any AI tool.
---

# TRACE Review

## What this skill does

TRACE is a structured five-point quality-control review for any AI-generated output, applied before
that output is shared, sent, published, or acted on. Its core principle: AI output quality is not the
AI's responsibility, it is the human's. This skill makes that responsibility fast and repeatable.

To run it, you paste the AI output and, ideally, the original prompt it was meant to answer and who it
is for. The review names the specific places a human needs to look before putting their name on the
work. It does not certify that the output is correct.

One thing to hold onto: the model running this review is itself an AI, with the same failure modes it
is checking for. It can be wrong, and it cannot prove a fact is true. Treat its findings as a sharp
first pass that points a human to what to verify, never as a final sign-off. Saying "I cannot confirm
this, here is what to check" is more honest, and more useful, than quietly assuming a claim is fine.

**Where this stops and a deeper pass begins.** TRACE is the broad first pass across all five
dimensions. It produces a verify-list and refuses to certify facts. When a piece is high-stakes and
turns on a specific fact, number, quote, or citation that must be confirmed against a primary source,
that deep single-fact verification is a separate, dedicated job. Run TRACE first to surface what needs
checking, then escalate the load-bearing items to a dedicated fact-verification pass.

## Choose the review depth first

Match the effort to the stakes. The goal is a check that fits the risk, not a two-hour audit on every
draft.

- **Quick pass** (low stakes, internal, easily reversible): scan all five dimensions, report only real
  issues, skip exhaustive claim-by-claim verification. Keep it short.
- **Full pass** (the default; anything leaving the team or informing a decision): work through all five
  dimensions in order and flag every issue with a severity.
- **High-stakes pass** (legal, clinical, financial, safety, regulatory, on-the-record, or anything
  irreversible): a full pass, plus a hard rule that nothing ships until every factual claim is verified
  against a primary source by a named human and every field-specific red line is checked.

If you have not signaled the stakes, infer them from the field and audience, then say which depth you
are applying so it can be overridden.

## Step 1: Get the context TRACE needs

Two of the five dimensions cannot be judged in a vacuum. Relevance needs the original problem; tone and
audience needs the intended reader. So before reviewing, confirm four things. If they are already clear
from the conversation, restate your understanding in one line and proceed. If the essentials are missing,
ask up to three short questions, then move on. Do not stall waiting for perfect inputs.

1. **The output** to review (the AI-generated text itself).
2. **The original problem or prompt** it was meant to solve. Trace the request back to the root problem
   it is really trying to solve, not just the surface request. You cannot judge relevance without this.
3. **The audience and channel**: who reads this, where, and how on-the-record it is.
4. **The field and its constraints**: the domain (so you know its red lines), the stakes, and whether any
   confidential, personal, or regulated data is involved.

If you are handed only the output, make your best-guess assumptions for items 2 to 4, label them
clearly as assumptions, and review against them. A surfaced assumption that can be corrected is useful.
Do NOT stall for the missing context and do NOT park the verdict as "pending" or "REVISE pending
context": proceed on the labeled assumptions and issue a real verdict (SHIP / REVISE / DO NOT USE) tied
to the findings, noting it is conditional on the assumptions holding.

## Step 2: Keep the five failure modes in view

These are the recurring ways AI output goes wrong. Use them as the lens while working through TRACE, and
tag every issue you find with the mode it represents. Naming the mode teaches you to spot it next time.

- **Hallucination**: states false information with full confidence; invents citations, statistics, quotes,
  or events that do not exist.
- **Bias and framing**: reflects skewed patterns from training data; favors certain groups, perspectives,
  or default assumptions.
- **Staleness**: relies on information from before the model's training cutoff; cites superseded rules,
  prices, or facts as if current.
- **Misframing**: solves the literal prompt instead of the intended problem; technically responsive,
  actually off-target.
- **Overconfidence**: omits uncertainty, caveats, and limits; rarely says "I don't know" unless pushed.

## Step 3: Apply TRACE

Work through all five in order. For each one the job is the same: name specific issues, quote the exact
text, say why it matters for this audience and field, tag the failure mode, and rate severity as
**Blocker**, **Should-fix**, or **Minor**. Be concrete. "Verify the statistics" is weak. "The 73% figure
in paragraph 2 has no source and I cannot confirm it, treat as unverified" is useful.

**T, Truth.** Is every factual claim verifiable against a primary source? Pull out named sources,
statistics, citations, dates, names, quotes, and any specific claim about the world. For each, do one of
two things: verify it only if you have a genuinely reliable way to (and say how), or list it as needing
human verification with a note on what to check and where to check it. Be most skeptical of precise
numbers, research findings, legal and policy statements, and anything suspiciously convenient. You cannot
certify truth; your value here is separating "checked" from "must be checked" so nothing rides through
assumed-true. When a Truth item is load-bearing and the stakes are high, do not just flag it: escalate it
to a dedicated deep fact-verification pass to confirm it against a primary source.

**R, Relevance.** Does the output actually answer the problem from Step 1, including the root problem and
not a near neighbor? Re-read the original ask. Watch for misframing: a fluent answer to a slightly
different question. Note anything on-topic but off-target, and anything actually needed that the output
quietly skipped.

**A, Accuracy of tone and audience.** Is the tone, reading level, framing, and assumed knowledge right
for the specific reader and channel? Would this audience (a patient, a juror, an executive, a recruit, a
customer, a layperson) understand it without confusion or take offense? Flag jargon, wrong register,
cultural or demographic assumptions, and anything that reads as off-brand or off-voice for the sender.
This is the dimension communicators are judged on most, so weight it accordingly. When persuasion or
adversarial framing is load-bearing, hand that check to a dedicated adversarial pre-ship review.

**C, Completeness.** Is anything important missing? AI tends to produce confident, complete-sounding
output that omits caveats, edge cases, counterpoints, required disclosures, or necessary context. Ask
the diagnostic question: what would an expert in this field expect to see here that is not present?
Omissions are often more dangerous than visible errors, because nothing flags them for you.

**E, Ethics and risk.** Could this cause harm if used as-is? Check three things by name. Privacy: does it
expose identifiable individuals, confidential, or protected information? Fairness: does it treat relevant
groups equitably, free of the bias mode above? Accountability: is the human decision-maker clear, and is
AI involvement disclosed where it should be? Then state the field's specific red lines, because every
field has them, and check the output against those.

## Output format

Return the review in this shape. Lead with the verdict so a busy reader gets the answer in one line, then
give the detail.

**Verdict**, one of:

- **SHIP**: no blockers; minor notes optional.
- **REVISE**: fixable issues, listed below.
- **DO NOT USE**: a blocker that makes the output unsafe as-is, such as a likely hallucination presented
  as fact, a privacy or ethics breach, or an answer to the wrong problem.

Then:

1. **Why**, one line.
2. **The five dimensions**, each with findings (or "clear"), failure-mode tags, severity, and quoted text.
3. **Must-fix before use**: the blockers and should-fixes as a short action list.
4. **Verify before trusting**: the Truth items a human must confirm against a primary source, each with
   what to check.
5. **Accountability**: name, or prompt for naming, the human who owns the decision to use this, and note
   whether AI involvement should be disclosed.

Keep it scannable, and match the length of the review to the stakes. A quick pass should be a few lines.

## How this fits a workflow

TRACE is not only a one-time check. It is the quality checkpoint inside a repeatable AI workflow. The
same review can be run by hand on a single draft, built into a team's "before it leaves us" step with a
named reviewer, or written into a workflow's standard operating procedure as a tailored checklist of that
output type's most common red flags. Capture the recurring flags for your specific output type, so the
check gets faster and more consistent every time you run it.

## Example (abbreviated)

**Input:** you paste an AI-written competitive analysis of three SaaS platforms, with market-share
percentages, intended as a one-page memo for your board. You mention only "review this."

**A good review opens like this:**

> Assumptions (please correct): original ask was a board-level read on competitive risk; audience is your
> board; field is general business, low regulatory stakes but a real decision rides on it. Applying a
> full pass.
>
> **Verdict: REVISE.** Strong structure, but the numbers are unsourced and it answers a narrower question
> than a board needs.
>
> - **T, Truth (Blocker to verify):** "Competitor A holds 41% market share" and the other two figures
>   have no source. I cannot confirm them; this reads like a confident estimate (hallucination risk).
>   These are load-bearing for a board decision, so escalate them to a deep fact-verification pass against
>   a named market report before this goes near a board.
> - **R, Relevance (Should-fix, misframing):** the memo compares features in depth, but a board reading
>   on "competitive risk" will want pricing pressure and switching risk, which are barely touched.
> - **A, Tone and audience (Should-fix):** several passages are written for a product manager, not a
>   board (for example "native webhook support"). Raise the altitude and cut the jargon.
> - **C, Completeness (Should-fix):** the newest entrant, the one your board asked about last quarter, is
>   not mentioned at all.
> - **E, Ethics and risk (Minor):** a confident ranking with no stated methodology. Add one line on how
>   the ranking was derived so no one over-trusts it.
>
> **Must-fix before use:** source the three share figures; add pricing and switching risk; raise the tone
> to board level; add the missing competitor.
> **Verify before trusting:** the three market-share percentages (primary source: a current market report,
> not the model's memory).
> **Accountability:** you own the decision to send this; note in the memo that the draft was AI-assisted.

Keep real reviews this concrete. Specific, quoted, and tagged beats a generic checklist every time.
