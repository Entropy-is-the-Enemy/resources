---
name: bones
description: >
  Strip a piece of writing down to its load-bearing structure so it can be reused in another format
  without rewriting it. Produces five things: the one core claim, the ordered moves that prove it, the
  parts that cannot be cut, the single line worth quoting, and a one-line chain. Has two modes.
  EXTRACT mode reverse-outlines existing drafted prose and quotes only what is there. SKELETON mode
  builds a proposed structure forward from a one-line outline entry when no draft exists, labeling
  every element proposed. Trigger on "find the bones," "give me the bones of this," "reverse outline
  this," "break this down to the core claim and the steps," "what's load-bearing here," or when
  someone wants to lift a long essay into a talk, a workshop, or a module. Reads and reports; never
  drafts prose and never adds argument beyond labeled proposals.
---

# Bones

## What this skill does

A finished essay is expensive to write and cheap to reuse, but only if you can see its structure.

Bones strips a piece down to the skeleton that carries its argument, so the same thinking can become a
talk, a workshop module, a shorter post, or a section of something larger, without anyone rewriting it
from the source material. It reads and reports. It does not draft.

## The five elements

Every run produces exactly these, in this order.

**1. The core claim.** One sentence. What this piece argues, not what it is about. "Why teams buy the
wrong tools" is a topic; "teams buy tools to fix bottlenecks they have not located" is a claim. If
what you extract is a topic, you have not found the core yet, and that is itself a useful finding
about the piece.

**2. The moves.** The ordered steps that prove the claim. Not the section headings, and not a summary
of each paragraph. A move is a job the piece does: establishes the stakes, names the common wrong
answer, presents the counterexample, generalizes it. Three to seven of them, in the order they appear.

**3. The load-bearing parts.** Which moves cannot be cut without the proof collapsing. Usually a small
set, and often a pair, because arguments frequently rest on two things held together (a mechanism and
an example, or two distinct failure modes that jointly rule out the alternative). Everything not on
this list is cuttable first, and that is what makes the whole exercise useful.

**4. The line that travels.** The one sentence from the piece that survives on its own, out of
context, in someone else's mouth. Quote it exactly. If there is not one, say there is not one; that is
a real finding and usually the most actionable thing in the whole output.

**5. The chain.** The argument as one line of arrows. `bottleneck unlocated -> tool bought -> queue
visible -> queue still slow -> visibility is not throughput.` If the chain does not read as a chain,
the piece has a structural gap and the arrow where it breaks is exactly where.

## The two modes

Which mode you are in is the first thing to establish, and mixing them is the failure this skill
exists to prevent.

### Extract mode

The piece exists. You are reading it and reporting what is there.

**The faithful-only rule: quote, never invent.** Every element must be traceable to text in the
source. If the piece never states its core claim outright, say so and quote the closest thing to it,
labeled as the closest thing rather than presented as the claim. If there is no portable line, write
"no portable line yet." Do not compose one.

This rule feels overly strict until the first time an extraction quietly improves a piece and someone
builds a talk on an argument the essay never actually made. Naming a gap is the output, not a failure
to produce output.

### Skeleton mode

No draft exists. You have a one-line outline entry, a title, or a rough intent, and you are proposing
a structure forward.

**Label every element proposed.** Not as a disclaimer at the top. On each element, so that a reader
skimming the middle of the output cannot mistake a proposal for an extraction.

A proposal presented as an extraction is the exact error this rule exists to catch, and it is easy to
commit because the two outputs look identical on the page. The difference is entirely in whether the
words came from a source or from you.

## The load-bearing test

This is the compression heuristic, and it is what makes bones useful rather than merely tidy.

For each move, ask: **if I cut this, does the proof still stand?**

- If yes, it is support. Illustration, texture, an additional example, a caveat. Valuable in a long
  piece, first to go in a short one.
- If no, it is load-bearing. It stays in every format, including the ten-minute version.

The result is a ranked cut list, which is what you actually need to take a four-thousand-word essay to
a fifteen-minute talk. Without it, compression happens by proportional trimming, which shortens
everything and weakens the argument evenly instead of preserving the parts that carry it.

Watch for the common case: two moves that are individually cuttable but jointly load-bearing. Two
worked examples where either one alone reads as an anecdote and both together read as a pattern. Flag
these as a pair, because cutting one is a bigger loss than the list suggests.

## Output format

```
MODE: extract | skeleton

CORE CLAIM
  <one sentence>            [proposed, in skeleton mode]

MOVES
  1. <the job this section does>
  2. ...

LOAD-BEARING
  <which moves, and one line on why the proof needs each>
  <flag any jointly-load-bearing pairs>

THE LINE THAT TRAVELS
  "<quoted exactly>"        [or: no portable line yet]

THE CHAIN
  <a -> b -> c -> d>

NOTES
  <structural gaps, unproven moves, the arrow that does not connect>
```

Keep it on one screen. Bones that run two pages have stopped being bones.

## Worked example (invented, extract mode)

**Source:** a long post arguing that most onboarding documentation fails because it is written by the
people who built the thing.

```
MODE: extract

CORE CLAIM
  Onboarding docs written by builders fail because builders cannot see the steps they have
  automated in their own heads.

MOVES
  1. Opens on a new hire stuck for two days on a step the doc calls "obvious."
  2. Names the usual explanation (the doc is incomplete) and rejects it.
  3. Introduces the mechanism: expertise compresses steps until they stop being visible.
  4. Second case, a different team, same shape, to establish it is not a one-off.
  5. Generalizes to the rule: the person who should write it is the last person who learned it.

LOAD-BEARING
  Moves 3 and 5. Three supplies the mechanism, without which the piece is two anecdotes.
  Five is the payload; everything before it exists to earn it.
  Moves 1 and 4 are a JOINT pair: either case alone reads as an anecdote, both together read
  as a pattern. Cutting one costs more than the list implies.

THE LINE THAT TRAVELS
  "The person who should write the onboarding doc is the last person who needed it."

THE CHAIN
  builder writes doc -> expertise has compressed the hard steps -> compressed steps go
  unwritten -> new hire stalls exactly there -> hand the pen to the most recent hire

NOTES
  Move 2 asserts that incompleteness is not the explanation but never rules it out. The
  argument works anyway because move 3 supplies a better mechanism, but a hostile reader
  stops at that arrow.
```

Note what the extraction does not do. It does not fix move 2, does not improve the quoted line, and
does not supply the rebuttal the piece is missing. It reports the gap and leaves the writing to the
writer.

## Boundaries

Bones reads structure and reports it. It does not draft prose, edit voice, generate ideas, verify
facts, or judge whether the argument is any good. It is not an outline generator for a piece nobody
has thought about yet; skeleton mode needs a real intent to build from, or it produces a plausible
shape with nothing inside it.
