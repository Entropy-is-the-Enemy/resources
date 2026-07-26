---
name: kb-integrate
description: >
  Integrate new material into a reference knowledge base the way you would merge code: decide whether
  it earns a place at all, search for collisions before writing, split it into single-concept atom
  files under a hard word ceiling, resolve its owner through a router table rather than a hardcoded
  path, flag genuine contradictions for a human instead of reconciling them, regenerate the index from
  frontmatter, and append an audit row. Holds anything met only once as a candidate, out of the index,
  until a second independent encounter promotes it. Trigger on "add this to the knowledge base," "integrate these
  notes," "file this," "does this already exist in there," "why does the same thing appear in three
  places," or when a batch of captured material needs to be graduated from raw intake into curated
  reference. Does NOT answer questions from the knowledge base, summarize it, resolve contradictions
  on its own authority, or hand-edit a generated index.
---

# KB Integrate

## What this skill does

Knowledge bases do not fail by getting too small. They fail by accumulating four half-versions of the
same idea in four places, none of which know about the others, until nobody trusts any of them and
everyone goes back to asking a person.

That is a duplication and drift problem, and software named the fix decades ago: DRY. One definition
lives in one place. Everything else imports it. The index is generated, never maintained by hand.
Nothing lands without a review step.

This skill runs a knowledge base on those rules.

## Lineage

The atom is not new. One concept per note is the Principle of Atomicity, named by Christian Tietze at
zettelkasten.de in 2013, descended from Niklas Luhmann's Zettelkasten and carried into English by
Sonke Ahrens' *How to Take Smart Notes* (2017) and Andy Matuschak's evergreen-notes essays. Matuschak
also drew the software analogy first, in "Evergreen note titles are like APIs." The one-parent rule is
DRY applied to prose: Hunt and Thomas, *The Pragmatic Programmer* (1999), "every piece of knowledge
must have a single, unambiguous, authoritative representation within a system." The router table is an
ordinary level of indirection and belongs to nobody.

What this file adds is operational. Tietze treats atomicity as a compass; this treats it as a hard
numeric ceiling used as a split detector. On top of that: a worthiness gate with an explicit
not-knowledge exit, contradictions flagged and never reconciled, and one audit row per run. Those are
the parts worth arguing with.

## The atom

One concept, one file.

- **A hard word ceiling.** Pick a number, four hundred is a reasonable default, and enforce it. The
  ceiling is not about brevity. It is a detector: a file that will not fit is two concepts wearing one
  filename, and the correct fix is to split it, not to raise the limit.
- **Frontmatter carries everything the system needs.** Title, one-line description, owning domain,
  source, date, `status` (candidate or active), and any links to related atoms. Everything mechanical
  is derived from these fields, so a missing field is a real error rather than a cosmetic one.
- **The one-parent rule.** Every concept has exactly one home. If it is relevant in three places, the
  other two link to it. They do not restate it, not even briefly, because a brief restatement is the
  seed of the drift.

The one-parent rule is the load-bearing one and the one people break first, usually with good
intentions: the summary in the other file was only two sentences. Two sentences is how it starts. Six
months later the two sentences say something the parent no longer says, and nobody knows which is
current.

## The generated index

The directory listing is built from the atoms' frontmatter, on demand, by a script. It is a build
artifact.

- **Never hand-edit it.** An index someone can edit is an index that will disagree with reality, and
  it will disagree silently, which is worse than not having one.
- **An active atom missing from the index is a frontmatter bug**, not an index bug. Fix the atom.
  Candidates are absent by design and are not bugs.
- **Regenerate at the end of every integration run**, and report the delta: active atoms, candidates
  held out, which domains changed.

## The router table

Between anything that asks the knowledge base a question and the content itself, put a lookup table:
topic to owning domain. This is not a map of content. It holds no prose and no curated link lists, only
topic-to-owner mappings.

```
finances, dues, grants          ->  operations
wheel truing, drivetrain, brakes ->  mechanics
volunteer onboarding, waivers    ->  membership
class curriculum, ride leading   ->  education
```

Callers resolve the path through the table. They never hardcode a folder. Two consequences, and the
second is the reason it is worth the file:

1. Reassigning ownership of a topic is a one-line edit, and everything downstream follows.
2. You can reorganize the whole corpus without breaking every reference to it, which means you will
   actually reorganize it when it needs it, instead of living with a structure you outgrew.

An unroutable topic is a finding, not an error to paper over. It means either the topic belongs to a
domain you have not defined, or it is not knowledge-base material at all.

## The integration run

Raw intake and curated knowledge are different bodies of material and must live in different places.
Material moves between them through an explicit, human-gated step. Nothing graduates automatically.

**Step 1: worthiness.** Three outcomes only.

- **Integrate.** A durable fact, method, framework, or figure that will be worth retrieving later.
- **Drop.** True but not worth keeping, or already common knowledge in this corpus.
- **Not knowledge.** It is a task, a decision, a preference, or an instruction. Route it to whatever
  system holds those. Knowledge bases fill up with to-do items when this outcome is missing.

Say the outcome out loud for every item. Silent drops are how a corpus develops holes nobody can see.

**Step 2: collision search.** Before writing anything, search the existing corpus for the item's key
terms and their obvious synonyms. Four possible results:

- **No hit.** New **candidate** atom. See the recurrence bar below.
- **Hit on a candidate.** The same idea has now arrived twice, from two independent encounters. Promote
  it: full atom, into the index.
- **Hit, and the new material is the same thing.** Do not create a second atom. Either strengthen the
  existing one or drop the new material, and say which.
- **Hit, and the new material is adjacent.** New atom, with a link, and a link added back from the
  existing one. Bidirectional, or the new atom is an orphan the day after it is written.

**The recurrence bar.** A knowledge base that files everything on first sight is a pile. So an item
that survives the worthiness gate and hits nothing does not become reference immediately. It becomes a
**candidate**: a real atom file, marked `status: candidate` in frontmatter, **excluded from the
generated index**, and visible only to the collision search. A second independent encounter promotes
it to `status: active` and it enters the index.

Two consequences worth the cost. One-off facts stop hardening into permanent reference, because
nothing you met once is retrievable yet. And the collision search gets something useful to hit on the
second pass instead of reporting "no hit, new atom" twice and leaving you two near-duplicates.

The bar does not apply to material you deliberately went and got. A document you sought out because
you needed it is not a chance encounter, and it goes in active. The bar is for things that drifted
past you.

**Step 3: contradiction flag.** If the new material disagrees with something already in the corpus,
**do not reconcile it.** Write the flag into both atoms, name both sources and both dates, and surface
it in the run report for a human to resolve.

This is a hard rule and the temptation to break it is constant, because the newer source usually looks
more authoritative. Sometimes it is wrong. An automatic reconciliation destroys the older claim with no
record that a choice was made. A flag costs one line and preserves the fork.

**Step 4: attribution.** Every atom names where it came from, in frontmatter: the document, the
conversation, the publication, with a date. An atom with no source is an assertion, and in a year
nobody will be able to tell whether it was researched or assumed.

**Step 5: audit row.** One line per integration run, appended to a log: date, items in, integrated,
dropped, not-knowledge, collisions found, contradictions flagged. The log is what lets you answer
"when did this get in here and who put it there" without archaeology.

## Output format

```
WORTHINESS
  Integrate:     <n> (<n> active, <n> candidate)   Promoted: <n>
  Drop:          <n>   <item> because <reason>
  Not knowledge: <n>   <item> -> <where it should go instead>

COLLISIONS
  "<key term>" -> <n> hits
    <existing atom>: SAME, strengthened / new material dropped
    <existing atom>: ADJACENT, linked both directions

CONTRADICTIONS FLAGGED (not resolved)
  <atom A> says <claim>          [source, date]
  <atom B> says <conflicting>    [source, date]
  Flag written into both. Needs a human.

ATOMS WRITTEN
  <slug>   <domain>   <status>   <word count>/<ceiling>   source: <where it came from>
  <slug>   PROMOTED candidate -> active: second encounter via <what hit it>
  <slug>   SPLIT from the above: exceeded the ceiling at <n> words, two concepts

ROUTER
  Unroutable topics: <list, or none>

INDEX
  Regenerated. <n> active atoms, <+n> this run. Candidates held out: <n>. Domains: <list>

AUDIT
  <the log line appended>
```

## Worked example (invented)

**Input:** a bicycle repair co-op has a shared drive full of captured notes from workshops, supplier
emails, and a departing volunteer's handover document. Seven items are up for integration.

```
WORTHINESS
  Integrate:     5 (4 active, 1 candidate)
  Drop:          2
    "Spring 2024 tune-up special was $45" because it is a superseded price, not a method.
    "Marco prefers the blue torque wrench" because it is a preference, not knowledge, and
      Marco left in March.
  Not knowledge: 1
    "Order two more truing stands before the fall class" -> this is a task. It belongs in
      whatever the co-op uses to track purchasing, not here.

COLLISIONS
  "torque" -> 3 hits
    fastener-torque-basics: SAME as the new supplier note on general practice. New
      material dropped, nothing added.
    disc-rotor-bolt-torque: ADJACENT. The supplier note gives a rotor-specific figure the
      general atom does not cover. Linked both directions.
  "wheel tension" -> 1 hit
    spoke-tension-by-rim-depth: ADJACENT to the new material on re-tensioning versus
      rebuilding. Linked both directions.
  "waiver" -> 0 hits. New atom.

CONTRADICTIONS FLAGGED (not resolved)
  spoke-tension-by-rim-depth says a wheel with three or more broken spokes should be
    rebuilt rather than re-tensioned.
    [source: 2023 workshop notes, 2023-09-12]
  The handover document says the shop's practice is to re-tension up to five broken
    spokes on entry-level rims because the labor difference matters at co-op prices.
    [source: volunteer handover, 2026-06-30]
  Flag written into both atoms. Both may be right for different rims and different
    volunteer skill levels, which is exactly the judgment call this skill must not make.
    Needs a human. Suggested resolver: the mechanics domain owner.

ATOMS WRITTEN
  disc-rotor-bolt-torque-update   mechanics   active     118/400   supplier email 2026-07-14
    PROMOTED candidate -> active: the rotor figure was filed as a candidate in March off a
    forum thread. Second independent encounter, so it is real. This is the bar working.
  wheel-rebuild-vs-retension      mechanics   active     287/400   volunteer handover
    Active on arrival: the handover was requested, not stumbled into.
  minor-participation-waiver      membership  active     206/400   volunteer handover
  waiver-storage-and-retention    membership  active     174/400   SPLIT from the above: the
    combined draft hit 431 words and was two concepts, what the waiver must contain and
    how long signed copies are kept. Split, linked.
  chain-wear-checking-interval    mechanics   candidate  96/400    workshop aside
    One mechanic's rule of thumb, mentioned once. Held out of the index. If it comes up
    again from anyone else, it promotes.

ROUTER
  Unroutable topics: 1. "insurance certificate renewal" matched no domain. It is real and
    it is nobody's, which usually means the domain set is missing one. Surfacing rather
    than forcing it into operations.

INDEX
  Regenerated. 213 active atoms, +4 this run. Candidates held out: 9. Domains: mechanics,
    membership.

AUDIT
  2026-07-26 | in 7 | integrated 5 (4 active, 1 candidate) | promoted 1 | dropped 2 |
    not-knowledge 1 | collisions 3 |
    contradictions 1 | splits 1
```

The contradiction is the most valuable line in that report and it is the one an automated merge would
have erased. The newer document would have won on recency, and a real disagreement about when a wheel
is worth saving would have quietly become policy.

## Boundaries

This skill files knowledge. It does not answer questions from the corpus, summarize it, or use it to
draft anything. Retrieval is a different job.

It never resolves a contradiction on its own authority, even when one source is obviously more recent
or more official. Recency is not correctness and the flag is cheap. The closest prior art for that rule
is not a knowledge-management method at all: it is the wiki maintenance tag, which names both claims
and takes the disagreement to a human rather than silently picking a winner.

It does not hand-edit a generated index, does not create a second home for a concept that already has
one, and does not raise a word ceiling to make a file fit. Each of those is the system telling you
something, and overriding it is how the rot starts.
