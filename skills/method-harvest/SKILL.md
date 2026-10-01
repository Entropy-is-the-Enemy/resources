---
name: method-harvest
description: >
  Session-close capture of reusable METHOD from work just done, drafted as short knowledge-base
  notes and written only on the user's go. Trigger on a wrap cue ("that's a wrap", "closing this
  out", "done for today") or an explicit call ("method harvest", "harvest the method", "anything
  reusable in this session", "what should we keep from this"). Detects up to three candidates,
  strips them to the concept, states how much evidence stands behind each, and files nothing
  without approval. Reporting "nothing reusable here" is a correct result. NOT for posts or social
  content (content-harvest), NOT for merging material the user hands over (kb-integrate), NOT for
  corrections learned from editing a draft (edit-harvest), NOT for one-off facts with no reuse.
---

# Method Harvest

A working session solves a problem, and the way it solved it is usually the most valuable thing in
the transcript. Then the chat closes and the method goes with it. The next time the same kind of
problem comes up, it is solved again from scratch, a little differently, and nothing compounds.

This skill is a short pass at the end of a session. It reads back over the work just done, pulls out
the few pieces of method that would change how the next similar job runs, and drafts each one as a
small note for your knowledge base. Nothing is written until you say so.

House style: no em dashes in anything this skill writes.

## Why it needs a cue

A skill fires on a message, not on the silent end of a conversation. So the trigger is a short wrap
phrase you type at close. The skill carries the whole procedure; the phrase is all you have to
remember. If your setup supports it, add a one-line reminder to whatever closes your sessions
("at wrap, offer method-harvest") so it does not depend on memory alone.

## Procedure

### 1. Scan for method, not facts

A candidate is something that would change how the NEXT job of this kind runs:

- a decision rule ("when the vendor quote has no unit price, ask for one before comparing")
- a sequence that worked, in order, with the step that matters most named
- a template or checklist that came out of the work
- a number with its reason ("two review rounds, because the third never changed a decision")
- a failure with a named cause, and what to do instead

A fact with no reuse is not a candidate. Neither is something the session merely discussed. Take
**three candidates at most**. If nothing qualifies, say "nothing reusable here" and stop. An empty
harvest is a valid result, never a prompt to manufacture a note.

### 2. Read the house rules of the knowledge base first

Before drafting, read whatever governs your knowledge base: a spec, an index, a README. Follow its
note format, its length limit, and its rule for where a topic lives. If it has none, use these
defaults:

- **One home per concept.** If a note on this already exists, propose an edit to it, not a second
  note. If another area needs it, that area links to it; it never gets a copy.
- **Short.** One concept per note, readable in two minutes.
- **Resolve the destination from the index,** never from memory. If the right home is unclear, say
  so in the gate line and let the user pick.

### 3. Draft each note

Each draft carries:

- **A title that is the concept,** not the project ("Ask for the unit price before comparing
  quotes", not "Notes from the office move").
- **When to use it,** written as the situations someone would be in when they need it. This is the
  field that makes the note findable later; a topic label is not enough.
- **The method itself,** in steps or rules.
- **The evidence base, stated plainly.** "Applied once, one project, 2026-10." A method that worked
  once is a hypothesis, and the note says so. Do not write single-use method as settled doctrine.

Two rules are not optional:

- **Publish the concept, hold the instance.** Strip every identifying specific before drafting: no
  client, employer, or colleague names, no internal figures, no product names, no detail that would
  let a reader work out whose work this was. If the method cannot be stated without the specifics,
  do not draft it. Mark it `[HELD: reason]` and leave the decision to the user.
- **Invent nothing.** Every step in a note traces to something that actually happened in the
  session. If a step was assumed rather than seen to work, label it `(assumed)`.

### 4. Gate, then write

Present the drafts in the conversation, each with a one-line gate:

> Note 1: "Ask for the unit price before comparing quotes" to `purchasing/`, new note, evidence: once.

The user approves each note with a one-line go, or edits it, or drops it. On go, write the note
to the resolved home, rebuild the index if the knowledge base has one, and confirm the new note
appears in it. No go, no write.

### 5. Close the loop

If the session also hit a moment where a note was needed and did not exist, record that gap
wherever the knowledge base tracks missing material. A list of what you went looking for and did
not find is the best map of what to harvest next.

## Worked example (invented)

A session spent the afternoon reconciling three vendor quotes for an office move. At wrap, the user
types "that's a wrap."

The skill finds two candidates and declines a third:

1. **Ask for the unit price before comparing quotes.** Two of the three quotes were lump sums; the
   comparison only became possible after both vendors broke them out. Decision rule, applied once.
2. **Compare on the total for the full term, not the first-year price.** One quote was cheapest in
   year one and most expensive over three years. Decision rule, applied once.
3. Declined: the name of the vendor that was chosen. A fact, not a method.

Both go to the gate. The user approves the first, folds the second into the first as a second rule,
and the skill writes one note under `purchasing/` and rebuilds the index.

## Boundaries

- **NOT content-harvest.** If the moment is something worth posting about, that skill owns it.
- **NOT kb-integrate.** When the user hands over outside material (a book, a transcript, an article)
  to fold into the knowledge base, that skill owns the merge. This one captures method from work the
  session itself just did.
- **NOT edit-harvest.** Corrections learned from the gap between a draft and what shipped belong
  there.
- **Detects and drafts only.** It never restructures the knowledge base, never creates new top-level
  areas without the user's say-so, and never decides that a harvested note is ready to teach or
  publish. That call stays with the user.

## Kill criterion

If, after three or four sessions of the kind this was meant for, the harvest is always empty or
always trivial, stop using it. That is a finding too: the reusable method is not where you expected
it to be.
