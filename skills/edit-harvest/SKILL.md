---
name: edit-harvest
description: >
  Capture the diff between a draft the model produced and the version you actually shipped, then turn
  each meaningful change into a reusable drafting correction that future drafts consult before writing.
  Each correction is scoped to a situation, gated on a one-line yes from you, and filed as a candidate
  until the same mistake-class recurs. Trigger on "harvest my edits," "what did I change," "learn from
  this edit," "diff my final against the draft," or right after you finish editing something the model
  drafted. Fires only on a human cue, never automatically, never on an ambient session-ended signal,
  and never revises a stored correction unasked.
---

# Edit Harvest

## What this skill does

The highest-signal training data for a model's voice is not a style guide you wrote about how you
write. It is the diff between what it drafted and what you shipped.

That is not a new observation. Learning a person's latent preferences from the edits they make to a
model's output is an established line of research, and this skill claims none of it. What it adds is
the discipline around the capture: an abstraction step, a human gate, and a bar that keeps a single
edit from becoming a permanent rule.

A style guide describes intent. The diff is evidence of behavior: the hedge you deleted because it
sounded evasive, the paragraph you moved because the reader needed the number first, the example you
swapped because the second one landed. Those decisions are already made and already correct. Edit
harvest reads the diff, abstracts each real change into a rule that applies before writing rather than
after, and files it where your drafting step retrieves it. The unit of value is a correction the model
never has to be given twice.

## What counts as a harvestable edit

Most changes in a diff are noise, and harvesting noise poisons the store faster than harvesting nothing
fills it: every stored rule constrains the next draft.

**Noise.** Typo fixes. Facts specific to one document (a date, a headcount, a name the model could not
have known). Formatting it was never told about. A one-time request from a particular reader.

**Signal.** Changes that reveal a standing preference:

- **Hedges deleted.** "may potentially," "we believe," "it could be argued." A deleted hedge is a
  register correction, not a word choice.
- **Claims softened or hardened.** A qualifier added or removed locates where your calibration differs
  from the model's default.
- **Systematic reordering.** Conclusion up, caveat down, example before principle. Order changes are
  structural and generalize hard.
- **Examples swapped.** The generic case replaced by a specific one, or a specific one replaced because
  it gave away more than you wanted to give away.
- **Openings rewritten wholesale**, or a vocabulary you never use appearing again. Either is one rule,
  not fifteen edits.

The test: **would this change be correct on a different document of the same kind?** If yes, it is a
rule. If no, it is a fix, and fixes are not stored.

## Abstraction: rule, why, use_when

A captured edit is not the rule. The edit is one instance; the rule is what it instantiates. Each
harvested correction gets exactly three fields.

**rule.** What to do differently, phrased as an instruction to a drafter, not a description of what
happened. "Open with the concrete change before any framing" is a rule. "The opening got rewritten"
is a diary entry.

**why.** One line on the mechanism, and not decoration. A rule with no stated why cannot be overridden
intelligently when a situation calls for the opposite, and cannot be spotted as a duplicate of one
already stored.

**use_when.** The retrieval key, and the field that decides whether the store stays useful at scale.
Scope by **situation, not by source document.** "Short notices to a general audience" is a situation.
"The service-change email from last Tuesday" is a document, and a correction keyed to a document is
never retrieved again. Write use_when as a condition a future task can check against itself: audience,
format, stakes, length, or channel. Situation scoping keeps a growing store cheap. A drafting step
pulls only the corrections whose use_when matches the task in front of it, so two hundred corrections
cost the same at draft time as twelve.

## The recurrence bar and the approval gate

A self-improving store has one characteristic failure: **overfitting.** A single mood, unusual reader,
or tired evening becomes a permanent constraint on everything written after. Two mechanisms prevent
it.

**The lifecycle: candidate, then active.** A new correction is filed as a `candidate`, which is
advisory: drafting steps may read it and are not bound by it. It becomes `active`, which is binding,
only when the same mistake-class appears in a second independent harvest, or when you explicitly
promote it. Most candidates are never promoted, and that is the mechanism working.

**The human gate.** Nothing is written without a one-line yes from you: the skill proposes the
abstracted correction and you answer yes, no, or amend. Silence is not consent, and five proposals
need five answers.

The skill **never auto-revises** a stored correction. If a new harvest contradicts one, it surfaces the
conflict and asks. A store that quietly rewrites itself is one you can no longer reason about.

## Where corrections live

Corrections go to a single flat store, one record each, in a plain file the drafting step reads at
draft time. A neutral default is `captures/corrections.md`.

**Defer sharding.** One file is easier to grep, diff, and audit than twelve, and the pull is to split
far too early. Split only at a real size threshold, and when you do, prefer a **generated index over
one source file** to hand-splitting into many. A generated index cannot drift from its source;
hand-split files always do, and reconciling them becomes its own job.

Retrieval belongs to the drafting step, which filters on use_when and applies matching `active` records
as constraints and matching `candidate` records as hints. Edit harvest only writes.

## Output format

One record per correction, appended to the store.

```
### <short handle for the mistake-class>
status:    candidate | active
use_when:  <situation: audience, format, stakes>
rule:      <instruction to a drafter, imperative, one or two lines>
why:       <the mechanism, one line>
seen:      <count of independent harvests showing this class>
drafted:   "<the line as the model wrote it>"
shipped:   "<the line as you shipped it>"
```

Keep `drafted` and `shipped` to the shortest span that shows the change. They let a reader check the
abstraction against evidence, and are not there to archive anything.

## Worked example (invented)

**Context:** the model drafted a rider notice for a regional ferry operator announcing a reduced
winter timetable. The shipped version came back reordered.

```
DIFF SUMMARY
  3 changes. 1 noise (a dock name corrected), 2 signal. One shown; the other
  was a deleted hedge, filed the same way.

### buried-lede-in-notices
status:    candidate
use_when:  short operational notices to a general audience, any channel
rule:      Open with the concrete change and its effective date. Move context,
           rationale, and apology below the first paragraph.
why:       A reader of a notice is scanning for what changes and when; framing
           placed before the fact makes them hunt for it.
seen:      1
drafted:   "As part of our ongoing commitment to reliable year-round service,
           we have been reviewing seasonal demand across the network."
shipped:   "From 3 November, the 07:15 and 19:40 sailings will not run on
           weekdays. All other sailings are unchanged."

PROPOSED. Reply yes / no / amend for each.
```

Note what the harvest does not do. It does not store the dock-name fix, and does not key the rule to
"the ferry notice," which would make it unretrievable. And it does not promote to `active` on first
sighting, however right the rule looks, because obviousness on one document is the signal that
overfits.

## Boundaries

Edit harvest observes and files. It does not draft, does not rewrite your shipped version, and does not
apply corrections at draft time; that belongs to your drafting step, and keeping the two separate lets
you audit the store with no writing task in flight. It captures corrections to drafting behavior, not
standing definitions in your house-voice layer.

It does not run without a cue from you, and does not fire on session end, on file save, or on any
ambient event. It does not write a correction you have not approved in a line of your own, and does not
edit a stored one on its own initiative. If the diff holds nothing but typos, the correct output is to
say so and store nothing.
