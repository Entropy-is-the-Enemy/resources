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
  drafts prose and never adds argument beyond labeled proposals. If the input contains no arguable
  claim, it says so and stops rather than producing a structure.
---

# Bones

## What this skill does

Bones strips a piece down to the skeleton that carries its argument, so the same thinking can become a
talk, a workshop module, a shorter post, or a section of something larger, without a rewrite.

## Intake: is anything actually being argued?

Before you produce anything, check the input for an arguable claim: something asserted that a
reasonable reader could dispute. Do this ahead of picking a mode; it gates both.

If there is no such claim, say so plainly and stop. No output block. A fragment, a title, a topic
label, or a stretch of description with nothing argued in it has no bones, and the five-element format
will accept every one of them without complaint. Name what you were given, name what is missing, stop
there. Stopping is a finished run, not a failed one.

## The five elements

Every run produces exactly these, in this order.

**1. The core claim.** One sentence. What this piece argues, not what it is about. "Why teams buy the
wrong tools" is a topic; "teams buy tools to fix bottlenecks they have not located" is a claim.

This element fails in two directions. If what you extract is a topic, you have not found the core yet,
and that is itself a useful finding. If the source proves more than one claim, state each claim
separately and recommend splitting the source into that many units. Do not merge them. Report the
multi-claim finding in place of a merged core, and run the other elements per unit only if asked.

**2. The moves.** The ordered steps that prove the claim. Not the section headings, and not a summary
of each paragraph. A move is a job the piece does: establishes the stakes, names the common wrong
answer, presents the counterexample, generalizes it. Three to seven of them, in the order they appear.

**3. The load-bearing parts.** Which moves cannot be cut without the proof collapsing. Usually a small
set, and often a pair held together, such as a mechanism and the example that makes it visible.
Everything not on this list is cuttable first.

**4. The line that travels.** The one sentence from the piece that survives on its own, out of
context, in someone else's mouth. Quote it exactly. If there is not one, say there is not one; that is
a real finding.

**5. The chain.** The argument as one line of arrows. `bottleneck unlocated -> tool bought -> queue
visible -> queue still slow -> visibility is not throughput.` If the chain does not read as a chain,
the piece has a structural gap and the arrow where it breaks is exactly where.

## Scope: what level you run at

Run one pass at the level of the unit you were handed. Its major internal divisions are the moves at
that level: hand over a section and its paragraph-level jobs are the moves, hand over an essay and its
sections are, hand over a five-part series and each part is.

Do not flatten a multi-part source into one enormous move list, and do not recurse into every part
unasked. When a part looks like it carries structure worth its own pass, offer that pass and wait to
be asked.

## Modes

Establish which mode you are in first thing after intake. There are two, extract and skeleton, and you
never mix them silently; a source that needs both is handled element by element under Mixed input
below.

### Extract mode

The piece exists. You are reading it and reporting what is there.

**The faithful-only rule: quote, never invent.** Every element must be traceable to text in the
source. If the piece never states its core claim outright, say so and quote the closest thing to it,
labeled as the closest thing rather than presented as the claim. If there is no portable line, write
"no portable line yet." Do not compose one.

### Skeleton mode

No draft exists. You have a one-line outline entry, a title, or a rough intent, and you are proposing
a structure forward.

**Label every element proposed.** Not as a disclaimer at the top. On each element, so that a reader
skimming the middle of the output cannot mistake a proposal for an extraction.

**The quotable line gets a stronger label than the rest.** Propose one line, no more, and do not give
it the ordinary proposed label. Mark it invented: it exists in no source. Frame it as the bar the
drafted line has to match or beat, not as a line to ship.

### Mixed input

Most real sources are part drafted and part intent. Do not pick one mode for the whole run. Apply the
faithful-only rule to the drafted portion and the skeleton discipline to the rest, in one pass, and
carry the label on each individual element rather than on the run.

## The load-bearing test

For each move, ask: **if I cut this, does the proof still stand?**

- If yes, it is support. Illustration, texture, an additional example, a caveat. Valuable in a long
  piece, first to go in a short one.
- If no, it is load-bearing. It stays in every format, including the ten-minute version.

The result is a ranked cut list, which is what takes a four-thousand-word essay to a fifteen-minute
talk. Watch for two moves that are individually cuttable but jointly load-bearing, and flag them as a
pair; cutting one costs more than the list suggests.

## Output format

```
MODE: extract | skeleton | mixed
                            [mixed: label every element below individually]

CORE CLAIM
  <one sentence>            [proposed, in skeleton mode]
  [or: this source proves N claims, listed - split it into N units, do not merge]

MOVES
  1. <the job this section does>
  2. ...

LOAD-BEARING
  <which moves, and one line on why the proof needs each>
  <flag any jointly-load-bearing pairs>

THE LINE THAT TRAVELS
  "<quoted exactly>"        [or: no portable line yet]
  [skeleton mode: one suggested line, marked INVENTED, not found in any source,
   offered as the bar the drafted line has to match or beat]

THE CHAIN
  <a -> b -> c -> d>

NOTES
  <structural gaps, unproven moves, the arrow that does not connect>
  <any part worth a deeper pass, offered rather than produced>
```

Keep it on one screen.

## Worked example (invented, extract mode)

**Source:** a long post arguing that onboarding documentation fails because the builders write it.

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

## Boundaries

Bones reads structure and reports it. It does not draft prose, edit voice, generate ideas, verify
facts, or judge whether the argument is any good. It is not an outline generator for a piece nobody
has thought about yet: input with nothing argued in it stops at intake, in either mode.
