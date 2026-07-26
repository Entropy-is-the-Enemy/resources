---
name: red-team-reflex
description: >
  Stress-test a persuasive document as its harshest credible reader before you send it. For anything
  written to win a yes: a pitch, a proposal, a funding request, a board memo, a cover letter, a grant
  application, an internal recommendation. Names the actual decision-maker, walks five adversarial
  reader personas, runs an overclaim scan, triages every attack down to the single objection that
  would flip the decision, prescribes a concrete move for each survivor, and issues a ship, fix, or
  hold call. Trigger on "red team this," "poke holes in this," "will this survive," "what will they
  say no to," "before I send this," or "stress-test this pitch." Run this BEFORE fact-verification and
  before any voice or polish pass. Do NOT use for documents that only inform, for creative work, or
  for a decision you are making rather than one you are asking someone else to make.
---

# Red-Team Reflex

## What this skill does

A persuasive document has three separate ways to fail, and people usually check them in the wrong
order.

1. **The argument does not survive the room.** A hostile but credible reader has one objection you
   did not answer, and it ends the conversation.
2. **A fact is wrong.** A number, a source, a claim about the current state of the world.
3. **The voice does not land.** Wrong register, wrong altitude, wrong for this reader.

Red-Team Reflex owns the first one, and it goes first. Verifying facts in an argument that does not
survive is wasted work, and polishing the prose is worse than wasted, because a well-written document
gets sent.

## Step 1: Name the veto-holder

Not "the audience." Not "a skeptical reader." The specific person or role who can say no, and whose no
ends it.

For that person, answer three things:

- **What can they actually say no to?** Sometimes it is the whole ask. Often it is one component, and
  the rest survives. Knowing which changes what you defend.
- **What are they protecting?** Budget, headcount, their own status, their boss's opinion of them,
  downside risk, a prior decision they made that this implicitly criticizes. This is the real
  objection engine, and it is almost never the one stated out loud.
- **What does saying yes cost them if it goes wrong?** A person who bears no downside reads
  differently from one who owns the failure. If the cost is personal, your document is competing
  against their instinct to do nothing, which is always the safest available option.

If you cannot name a specific veto-holder, stop and find out who it is. A red-team against a generic
skeptic produces generic objections, and generic objections are the ones you already thought of.

## Step 2: Walk the five readers

A fixed palette, walked in order. The point of a fixed set is that you cannot skip the uncomfortable
one, which is exactly what an unstructured reread does every time.

**The skeptic.** Does not believe the central claim. Attacks the evidence: is it enough, is it
representative, does it actually show what you say it shows. Asks what would have to be true for this
to work and whether you have shown that any of it is.

**The busy skimmer.** Reads the first line, the headings, and the numbers, then decides. Attacks the
structure: is the ask visible in the first ten seconds, or buried on page two after the context you
thought was necessary. If the skimmer would come away with the wrong idea, the document has already
failed for a large share of real readers.

**The motivated rival.** Wants this to not happen, for reasons of their own. Attacks selectively and
in bad faith: quotes the weakest sentence, reads the ambiguous clause the worst way, points at what
you left out. Ask what single sentence they would pull out and read aloud.

**The domain expert.** Knows the field better than you. Attacks precision: the term used loosely, the
step that is harder than you implied, the well-known complication you did not mention. The damage here
is not the specific error, it is that one visible imprecision makes the reader discount everything
else.

**The cynic.** Does not attack the argument, attacks the motive. Why is this person really asking?
What do they get? Is this a solution looking for a problem, or a budget looking for a justification?
Uncomfortable, and usually the persona that finds the thing everyone else was too polite to name.

Generate attacks freely at this stage. Do not filter, rank, or answer yet.

## Step 3: The overclaim scan

Separate pass, because overclaiming is a different failure from being wrong and it is caught by a
different kind of reading.

Look for:

- **Sample-of-one claims stated as patterns.** "This approach works" resting on one instance.
  Right-size it: one instance, stated as one instance, is credible. One instance stated as a pattern
  invites the reader to go looking for counterexamples.
- **Loaded words doing argumentative work.** Obviously, clearly, simply, everyone knows, it goes
  without saying. These signal a step that was skipped rather than proven, and a hostile reader reads
  them as a tell.
- **Superlatives and absolutes.** Only, never, always, best, first. Each one is a target, and each one
  is usually unnecessary to the argument it decorates.
- **Precision that is not real.** A figure carried to two decimals from an estimate. False precision
  reads as either sloppiness or manipulation, and the reader does not stop to figure out which.

## Step 4: Triage to the kill-shot

You now have a pile of attacks. Most do not matter. The work is finding the one that does.

**Run a pre-mortem.** Assume it is six weeks later and the answer was no. Write the one-sentence
reason. Not a list. The single most likely story of the rejection. That sentence usually contains the
kill-shot.

**Rank by weakest link, not by frequency.** An argument fails at its weakest load-bearing point, not
at whatever attracted the most attacks. Three objections to a decorative paragraph matter less than
one objection to the premise everything else rests on.

**Output the kill-shot plus the top two or three.** Everything else gets dropped, not filed. A list of
fourteen concerns is a way of avoiding the ranking, and it lets the author fix the easy ones and feel
finished.

## Step 5: Prescribe a move

Every surviving objection gets exactly one of five prescriptions. Naming the move is the whole value;
"this is a weakness" is not actionable.

- **Pre-empt.** Raise it yourself, before the reader gets there, and answer it. Costs you a paragraph.
  Buys you the credibility of having seen it coming. Correct when the objection is obvious and the
  answer is good.
- **Harden.** The claim is right but under-supported. Add the evidence. Correct when you have the
  evidence and simply did not include it.
- **Cut.** The claim is not load-bearing and it is attracting fire. Delete it. The most under-used move
  by a wide margin, because cutting feels like losing ground.
- **Reframe.** The objection is fatal to the argument as posed, but the underlying ask survives a
  different framing. Correct when the reader is objecting to your characterization rather than your
  request.
- **Accept and arm.** The weakness is real and cannot be fixed in the document. Do not paper over it.
  Prepare the answer for when it is raised in the room, and hand that answer to whoever will be
  standing there.

## Step 6: The verdict

One of three, stated first:

- **SHIP.** Survives the room. No fatal objection with an unaddressed prescription.
- **SHIP WITH FIXES.** The prescriptions are all pre-empt, harden, or cut, and none requires rethinking
  the ask. List them in order.
- **HOLD.** The kill-shot requires a reframe, or the ask itself does not survive contact with what the
  veto-holder is protecting. Sending it now spends a chance you do not get back.

The hold verdict is the one this gate exists to make possible. A document you can still improve is
worth more than a document already read.

## Output format

1. **Verdict**, one line, with the reason.
2. **The veto-holder** and what they are protecting.
3. **The kill-shot**: the objection, which reader found it, and the prescription.
4. **Top two or three survivors**, same shape.
5. **Overclaim scan**, only the hits, quoted.
6. **Answers to have ready**, for anything marked accept-and-arm.

Keep it shorter than the document under review.

## Worked example (invented)

**Input:** a one-page internal proposal asking a department head to fund a part-time contractor to
clear a documentation backlog.

> **Verdict: SHIP WITH FIXES.** The ask survives, but the skimmer never finds it and one number is
> doing more work than it can hold.
>
> **Veto-holder:** the department head. Protecting headcount precedent more than the dollars. A
> contractor who becomes permanent is the outcome she has been burned by before.
>
> **Kill-shot** (motivated rival, and she will think it herself): nothing in the proposal says what
> happens when the contract ends. Read uncharitably, this is a headcount request wearing a contractor
> costume. **Prescription: pre-empt.** One sentence naming the end date and what state the
> documentation is in when it arrives, placed before the ask, not after it.
>
> **Survivors**
> - Busy skimmer: the ask appears in the last paragraph of a page whose first two paragraphs are
>   background on how the backlog accumulated. **Cut** the history to one clause and lead with the ask.
> - Skeptic: "the team loses about a day a week to this" is the load-bearing number and it is
>   unsourced. **Harden**, or restate it as the estimate it is.
> - Domain expert: the proposal treats the backlog as a writing problem. Anyone who has done this knows
>   the bottleneck is review, not drafting, and a contractor cannot review. **Accept and arm.**
>
> **Overclaim scan**
> - "Obviously this pays for itself." Loaded word carrying the entire cost argument. Show it or cut it.
> - "The only way to clear this." Absolute, and untrue; a freeze on new documentation would also do it.
>
> **Answers to have ready**
> - If she asks who reviews the contractor's output: name the reviewer and the hours it costs them,
>   before she works out that you did not account for it.

Note the kill-shot. It was not a flaw in the argument. It was the thing she is protecting, which the
document never addressed because the author was thinking about documentation.

## Boundaries

Red-Team Reflex tests whether an argument survives. It does not verify facts, numbers, or citations,
and it does not fix voice or polish prose; those are separate passes, and they run after this one. It
is also the wrong instrument for a decision you are making yourself rather than asking someone else to
approve, where the useful posture is finding the strongest objection to your own thinking rather than
predicting someone else's.
