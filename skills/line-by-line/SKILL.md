---
name: line-by-line
description: "Build a critically important deliverable in strict end-first, walkable-step order, one unit at a time. Use this whenever the stakes are high enough that getting it right beats getting it fast: a slide deck, a proposal, a paper, a board memo, a pitch, a grant application, a launch doc, any artifact where a wrong structure is expensive to unwind. Trigger explicitly on \"line-by-line\", \"build this line by line\", \"one unit at a time\", \"end first\", or \"walk this with me\". Also trigger on your own whenever the user starts building a high-stakes deliverable and has not asked for a quick one-pass draft, even if they never name the method. Do NOT use for quick drafts, throwaway text, brainstorming, or work the user explicitly wants done fast in a single pass."
---

# Line by Line

A method for building high-stakes deliverables without building the wrong thing fast.

## Why this exists

The usual failure mode on an important deliverable is momentum. You propose a full outline, pre-draft the sections, jump to format, and race ahead. It feels productive. But if the structure is wrong, every drafted section is wasted, and the person you are building for only discovers the problem at the end, when it is most expensive to fix.

Line-by-line trades momentum for walkability. You build the deliverable out of order, on purpose, so the destination is fixed before you take a single step toward it, and every step is checked against whether the audience can actually make it.

## The core discipline: build out of order

Do not build front to back. Build like this:

1. **End first. Build the last unit first.** Define exactly where the audience must arrive, then build that final unit (the last slide, the closing ask, the conclusion). Everything else will aim at it. See "Pin the end" below for how to state it precisely. If you cannot state the end precisely, stop and pin it down with the user before building anything else.

2. **Then the start. Build the first real unit next.** Define exactly where the audience actually is right now, honestly, not where you wish they were. Build the opening unit (the first slide after the cover, the opening frame) around that true starting point.

3. **Then the most walkable step.** Ask: what is the single most realistic step from where they are toward where they must arrive? The decision criterion is not "most impressive" and not "what I would find easy." It is: can the *weakest member of the audience* take this step from the unit before it? (See "The rule under the rule" for that test in full.) Pick the step that clears that bar and moves the audience the furthest. Build that unit next.

4. **Then bridge, one honest step at a time.** Keep adding the next most walkable step, always checking the path still holds from the start to the end. Fill the middle one unit at a time.

## Pin the end

The end is the hardest and most important thing to get right, so state it before you build anything. The end is pinned when you can name the exact state the audience must be in when the deliverable is done, in the owner's own words, precisely enough that you could check whether a given attendee reached it. That is the definition of done.

To extract it, ask the owner:

- **Arrival state.** When this is over and it worked, what does each audience member now understand, believe, or be able to do that they could not before?
- **The one thing.** If they remember or do only one thing, what is it? What is the single load-bearing outcome?
- **The observable proof.** How would we know, from the outside, that a given person actually got there? What would they say or do?
- **The failure line.** What is the outcome that means this did not work, even if the room seemed happy?

Capture the answer as a short arrival state, in parts, so every earlier unit has a fixed target to aim at. Use this template model (from the worked example in `references/worked-example.md`, a beginner tutorial deck):

> By the end, each attendee will (a) understand the key distinction the tool turns on, (b) know when it is worth using, (c) have named a few real tasks worth handing off, and (d) have started building the first one in the room.

The owner defines the end in their own words. The method does not guess it.

## The rule under the rule

It is less about momentum and more about walkability. Every step must be one the *weakest member of the audience* can take from the step before it. Design each unit against that person: the least-prepared reader, the most skeptical buyer, the beginner in the room. If a step only works for the strongest, the path is broken, no matter how good the step looks on its own. This is the decision criterion step 3 uses to choose the most walkable step.

## How to work it with the user

- **One unit at a time.** For each unit: what content is in, what is out, and does it earn its place. Iterate that single unit with the user until it is agreed. Do not touch the next one until the current one is settled.
- **Do not run ahead.** No proposing a full skeleton. No pre-drafting multiple units. No jumping to format, layout, or visual representation before the content is agreed. These moves feel efficient and they are the exact failure this method exists to prevent.
- **Surface the strongest objection.** When the user states a direction you think is weak, say so before agreeing, then build what they decide. A settled call gets your best execution, not silent compliance and not relitigation.
- **Persist a build log.** Record each agreed unit as you go, in a running document, so nothing is lost and the work can be handed off mid-stream. Note what was decided and why, so settled questions are not reopened.
- **Verify as you build, not at the end.** If a unit rests on a fact, a number, or a source, ground it when you build that unit, not in a cleanup pass later. A false load-bearing claim discovered late can collapse the structure built on top of it.

## When the end changes mid-build

The end can move. New information lands, the owner reframes the ask, the audience turns out to be different than assumed. When it does, do not patch forward from where you are. Do this:

1. **Re-pin the end.** Run the "Pin the end" extraction again against the new reality and write the new arrival state into the build log, replacing the old one.
2. **Re-walk the downstream units.** Every unit that was built to aim at the old end is now suspect. Walk them in order and check each against the new end: does this step still move the audience toward where they must now arrive, and can the weakest member still take it?
3. **Rework only what broke.** Keep units that still hold. Rework the ones that were resting on the old destination. Because you built one unit at a time against a fixed end, this is a targeted repair, not a rebuild.

## When a unit fails verification

If grounding a unit shows a load-bearing claim, number, or source is false or cannot be sourced, stop. Do not build the next unit on top of it.

1. **Correct or drop the claim.** Either replace it with a true, sourced claim, or remove it and let the unit stand on what survives. Do not ship a maybe.
2. **Re-check what rests on it.** Any later unit that assumed the false claim is now suspect. Walk those units and confirm each still holds without it. If one no longer holds, treat it as a failed unit too and repeat.
3. **Log the correction.** Note what was false, what replaced it, and which units were re-checked, so the same claim is not reintroduced downstream.

## Gate before shipping

When the units are built and the path is walkable end to end, run a final pass before the deliverable goes out. This gate does not replace any dedicated end-of-process gates you already run. At the gate, **hand off** to a dedicated fact-and-number verification pass, an adversarial pre-ship review, and a voice-and-style pass, and let each do its full job. What follows is only a brief inline summary of what those passes must cover and in what order; it is a checklist for the handoff, not a substitute for it. Order matters:

1. **Facts.** Hand off to a fact and number verification pass: every load-bearing claim, number, and citation is true and sourced. Flag anything volatile to re-verify close to delivery.
2. **Adversarial read.** Hand off to an adversarial pre-ship review: the argument survives a skeptical member of the audience. Find the objection that would kill it and make sure the piece answers it.
3. **Voice and tone, last.** Hand off to a voice and style pass last, so fact and structure edits cannot reintroduce off-tone or machine-sounding writing.
4. **Final scan.** One last read for anything that should not ship: confidential material, loose ends, broken references.
5. **The owner ships.** The method drafts; the human holds the final send.

Voice goes last on purpose. If you polish tone first, later fact and structure edits will undo it.

## Anti-patterns (what this method is built to stop)

- Proposing the whole structure up front "to align," then discovering the destination was wrong after sections are drafted.
- Pre-drafting several units before the first is agreed.
- Jumping to layout, visual style, or format before the content earns its place.
- Building the impressive step instead of the walkable one, and losing the weakest audience member.
- Saving all verification for the end, then finding a load-bearing claim was false after the structure was already built on it.

## Worked example

See `references/worked-example.md` for a full walkthrough: building a 60-minute beginner tutorial deck end-first, one walkable slide at a time, with each unit grounded as it was built. It closes by pricing the alternative, naming three mid-build corrections and what a front-to-back build would have cost at each one.
