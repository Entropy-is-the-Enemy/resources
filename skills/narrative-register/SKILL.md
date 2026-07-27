---
name: narrative-register
description: >
  Rewrite selected narrative passages into the plain-style narrative-nonfiction register: concrete
  nouns, hard active verbs, short propulsive rhythm, stakes and scene pushed forward, wry restraint.
  An on-demand layer applied to named paragraphs, deliberately separate from your own house voice.
  Trigger on "give this a narrative pass," "run the narrative register on the opener," "make this read
  like narrative nonfiction," or "put some scene in the stakes paragraph." Do NOT apply it to tables,
  specs, figures, defined terms, dosages, tolerances, warranty, contract, safety, or disclosure
  language, or any passage where a reader will act on an exact value. Stop and ask before restyling
  anything written in an identified person's own voice. Do NOT apply it to a whole document by default
  or fold it into your standing voice.
---

# Narrative Register

## What this skill does

A prose style is a theme, not a personality transplant. This skill treats one specific nonfiction
register as a callable layer you apply to named passages and take off again, the way you apply a
visual theme to a chart and leave the numbers alone.

The register: concrete over abstract, scene over summary, a human with a problem instead of an entity
with an initiative, verbs that do physical work, a flat funny line delivered without a wink.

The skill is not the register. It is the discipline around it: a scope map, a device budget, a
fidelity rule, a guard that makes the register yield to the document's own rules. Nearly every
purple-prose failure is a scope failure, not a taste failure. The writing was fine. It landed on a
specification.

## Order of operations

1. Calibrate on the worked pairs below and match their moves before you consult the rule list. The
   pairs are the target; the measured rules are the checklist you run afterward. A register transfers
   through pairs, not through descriptions of itself.
2. Read the target's own style rules and note them before rewriting a line, not after.
3. Print the scope map. Halt on anything marked ASK.
4. Rewrite passage by passage.
5. Count the devices, check the house-style yields, then read source against output for claims,
   numbers, names, dates, and causal links.

## Scope: where the layer lands and where it is frozen

Classify every block as APPLY, ASK, or FREEZE and print the map before rewriting a sentence. Short
jobs are where a warranty clause gets swept in.

**APPLY**: narrative openers, stakes paragraphs, "why this matters" lines, transitions, case
anecdotes, closers, any prose whose job is to make a reader keep reading.

**ASK**: any passage speaking in an identified person's own voice, quoted or not. A signed letter, a
founder's note, an attributed testimonial, a first-person account under a byline. Restyling it puts a
borrowed register in a named person's mouth and misrepresents them even when every fact survives.
Print it in the map and stop. Neither silently rewrite nor silently skip: get an explicit yes per
passage, then treat it as APPLY.

**FREEZE**: tables, captions, code, defined terms, any sentence carrying a number a reader will act
on, dosages, tolerances, specs, warranty and contract clauses, regulatory and disclosure language,
safety instructions, quotations, names, dates, citations.

**When the call is close, freeze.** A block you cannot confidently sort goes to FREEZE with reason
`ambiguous`, named in the map so the user can override it. A missed improvement costs one more
request; a styled clause that should never have been touched can cost more.

**Adjacency rule.** A frozen clause inside an applied paragraph freezes the clause, not the paragraph.
Rewrite around it and carry it verbatim. If the sentence cannot be rewritten without touching it,
leave the sentence alone and say so.

**Fidelity rule: the register adds nothing.** It may reorder, cut, re-verb, compress. It may not add a
fact, number, name, motive, inner thought, causal claim, or detail of weather, clothing, or gesture
absent from the source. Verb intensity counts as content here, so the plainer-verb test below is part
of this rule. Invented interiority is the most seductive failure: it reads exactly like good writing.
If a scene wants a detail the source lacks, report the gap.

## The devices, with per-document budgets

Named, falsifiable, counted. Budgets assume about 1,000 words of APPLY text.

- **Cold open**, drop the reader into motion, no warm-up. Budget 1.
- **Reversal beat**, set an expectation, invert it in the next sentence. Budget 2. The engine, and the
  fastest to spoil.
- **Deadpan understatement**, a large consequence stated flatly and small. Budget 2.
- **Named human**, a person or role carries the stakes, not an institution. Budget 3.
- **Rhythm drop**, a sentence under eight words right after one over twenty-five. Budget 3.
- **Wry aside**, dry judgment tucked in a subordinate clause, never a joke on its own. Budget 2.
- **Concrete triad**, three nameable items in a row, no abstractions. Budget 1.
- **Late payoff**, withhold the point one beat past where it is expected. Budget 1.

Measured rules, checked by counting, not feel:

- **Sentence-length variance.** Per applied paragraph: one sentence under eight words, fifteen words
  of spread between longest and shortest, never three consecutive sentences within four words of each
  other.
- **Verb hardness.** At most 15 percent of main verbs are forms of "to be" or "to have." Zero adverbs
  propping weak verbs ("moved quickly" becomes "bolted"). Nominalizations go back to verbs: "made a
  determination" becomes "decided."
- **The plainer-verb test.** After swapping in a harder verb, ask whether a plainer one carries the
  same meaning. If it does, the harder verb is decoration and it goes. An intensified verb claims
  magnitude, speed, or force: where the source supports only "walked out," "stormed out" has added a
  fact while posing as style. The hardness quota is a floor, not a license, and the fidelity block
  names any verb you rejected as overstated.
- **Concrete noun ratio.** At least 60 percent of content nouns name something a reader could
  photograph, count, or shake hands with.
- **Adjective ceiling.** One per noun, never two stacked.

Anti-devices, always zero: foreshadowing tells, sermonizing, exclamation points, rhetorical questions
as transitions.

## Frequency, pooling, and the house-style guard

**Once is a move, twice is a tic.** A device at double budget reads as impression, not craft. Count
each device by name before shipping and report the counts. Over budget, cut the weakest instance.

**Pool budgets when layers stack.** Two layers each spending two reversal beats gives a document four,
which reads like parody. Shared budgets, not additive ones. Split the passages first, one layer taking
openers and closers, the other the middle stakes, and print the split.

**The document's rules win.** If the target bans a punctuation mark, forbids fragments, caps paragraph
length, or requires passive construction for procedural steps, the register yields without argument.
When a rule blocks a device, note the substitution rather than dropping the rule.

**Keep six eval fixtures and rerun them after any rule change**: a tolerance clause mid-paragraph
(survives verbatim), a passage seeded with five reversal beats (over budget), a decision with no
stated reason (no motive), a bare table (declined), a signed first-person note (halted, not
rewritten), and a flat line about an ordinary errand, where the plain verb survives and any energetic
substitute is a failure.

## Output format

```
SCOPE MAP
  APPLY:  <first words of each applied passage>
  ASK:    <passages in an identified person's own voice, held pending explicit confirmation>
  FREEZE: <blocks, reason: spec | number | defined term | legal | safety | quote | ambiguous>

LAYER SPLIT (if stacking)
  <which layer owns which passages, how the pooled budget divides>

REWRITE
  <applied passages only, frozen clauses carried verbatim>

DEVICE COUNT
  cold open 1/1 | reversal 2/2 | deadpan 1/2 | named human 2/3
  rhythm drop 3/3 | wry aside 1/2 | triad 0/1 | late payoff 1/1
  be/have verbs 11% | concrete nouns 68% | over budget: none

HOUSE-STYLE YIELDS
  <rule, device blocked, what ran instead>

MEANING CHECK
  Source and output read side by side. Claims, numbers, names, dates, causal links: unchanged.
  <this line is always printed, including when the fidelity block below is empty>

FIDELITY
  <what the scene wanted and the source did not supply, never invented; verbs rejected as overstated>
```

## Worked example (invented)

All figures come from the source brief. Nothing is added.

```
PAIR 1  (stakes paragraph, APPLY)

BEFORE
  The terminal's throughput challenges were largely attributable to the aging crane fleet, and
  management determined that a phased replacement program would be necessary to remain
  competitive.

AFTER
  Four of the six cranes at Berth 9 were older than the men running them. On a good night they
  moved twenty-two boxes an hour. The port ninety miles down the coast moved thirty-four. Nobody
  there needed a consultant to explain what happens to a port that loses a shipping line. They
  had all watched it happen to somebody else. The cranes had to go.

  devices: cold open, rhythm drop, deadpan ("the cranes had to go")


PAIR 2  (case anecdote, APPLY)

BEFORE
  Following identification of elevated lead levels, the utility initiated a service line
  inventory and prioritized replacements per regulatory guidance, with substantial
  completion targeted for year four.

AFTER
  The utility knew it had lead pipes. It did not know where. So four people spent nine months
  with a pocketknife and a refrigerator magnet, house to house, scratching a coin-sized patch
  on the pipe where it entered the basement. Soft and shiny meant lead. If the magnet stuck, it
  was steel. That was the whole test, and it is how a city of ninety thousand found out which
  kitchen taps to worry about. Four years to pull them all, if nothing goes wrong.

  devices: reversal beat, concrete triad, rhythm drop, late payoff, deadpan


PAIR 3  (FREEZE boundary)

SOURCE
  Coverage is void if the pump is operated at a suction lift exceeding 7.6 m or if impeller
  clearance falls outside 0.20 to 0.35 mm.

AFTER
  Identical. Carried verbatim.

  The register wanted "run it outside spec and you own it." Shorter, warmer, wrong: it drops
  the lift figure, the clearance range, and the word void, the only word a court cares about.
```

## Boundaries

This layer styles prose. It does not report, verify, fact-check, restructure an argument, or decide
what a document should say. It never runs by default, because a register applied everywhere stops
being a layer and becomes your voice. The register belongs to the document, not to a person: lending
it to a named human's own words takes their operator's explicit yes. Applied to a spec, a disclosure,
or a dosage, it is not a style choice. It is a defect.
