---
name: eval-author
description: >
  Generate a randomized, edge-weighted regression test suite for a production skill, prompt kit, or
  agent workflow. Reads the target's declared contract, interviews for the implicit contract, then
  emits 15 to 25 cases across a fixed bucket distribution (happy path, boundary, adversarial,
  domain-randomized), each paired with falsifiable acceptance criteria rather than expected outputs,
  drawn from a seeded randomization table, gated by a checkpoint before anything is written. Trigger
  on "write evals for this," "build me a test suite for this skill," "how do I know if this prompt
  still works," "regression tests for my agent," "eval suite," or after any material edit to a skill
  others depend on. Outputs JSON plus a markdown companion. Does NOT execute the suite, score
  outputs, or fix the target: authoring and running are separate jobs owned by different tools.
---

# Eval Author

## What this skill does

Skills rot silently. You tighten one instruction, three unrelated behaviors drift, and you find out
weeks later from a bad output nobody flagged. Software solved this with regression tests, and the
move carries over given the discipline you would give a test file: fixed structure, reproducible
inputs, pass conditions a stranger can check. Eval Author writes the suite; it does not run it.

Two contracts get read first. The **declared contract** is what the target says about itself:
trigger description, stated scope, output format, explicit exclusions. The **implicit contract** is
what the author never wrote down: which inputs are supposed to bounce, what a near-miss looks like,
which failure would be embarrassing rather than merely wrong. The second is where the good cases
live, and it only comes out by asking. Interview for it. Never invent it.

## 1. The bucket distribution

Fixed, and **weighted toward the edges**, because happy-path cases keep passing while the thing
quietly breaks.

| Bucket | Share | What it tests |
| --- | --- | --- |
| Happy path | 30% | The declared job on clean, in-scope input |
| Boundary | 30% | Ambiguous scope, partial input, missing fields, extremes, two plausible routes |
| Adversarial | 25% | Overtriggering, undertriggering, fabrication |
| Domain-randomized | 15% | The declared job in a context the author never had in mind |

Adversarial splits three ways and **all three subtypes must appear**. *Overtriggering*: an input
that resembles the trigger but is out of scope, so the target should decline. *Undertriggering*: an
in-scope input phrased so it does not resemble the trigger, so the target should still fire.
*Fabrication*: an input missing something the target needs, so the target should name the gap rather
than fill it.

**Rounding rule.** For suite size N, multiply by each share and take the floor. Assign leftovers in
this order until they run out: adversarial, boundary, happy, randomized. Then enforce three floors:
one case per adversarial subtype, one randomized case, two happy-path cases. If a floor conflicts
with the arithmetic at small N, raise N rather than break the floor.

**Keep it between 15 and 25 cases.** A suite that takes two sessions gets run once and never again.
And one sloppy case poisons the whole scorecard: a criterion nobody trusts turns every future red
into an argument about the test.

## 2. Falsifiable criteria, never expected outputs

A case pins the input and the **acceptance criteria**, never the expected output. Pinning the output
tests similarity to one author's phrasing, and forces a suite rewrite every time the target's wording
improves.

Every criterion must survive the **independent-grader test**: someone holding only the target's spec
and the produced output marks pass or fail, with no access to what you meant. If grading requires
asking the author, it is not a criterion.

Four checkable shapes. **Presence**, a required element appears. **Absence**, a forbidden one does
not. **Routing**, the target declines, escalates, asks, hands off, or proceeds. **Threshold**, a
countable property clears a bar.

**Vibes words are banned.** *Appropriate*, *gracefully*, *high-quality*, *thoughtful*, *reasonable*,
*properly*. Each stands in for a property you have not identified yet. Rewrite it or cut it.

| Vibes phrasing | Falsifiable rewrite |
| --- | --- |
| Handles missing data gracefully | Names each missing field; produces no value for any of them |
| Escalates when it should | Routes to a human when severity is 1 or safety is named, else not |
| High-quality summary | Every claim traces to a quoted span in the input |

## 3. The seeded randomization table

Reproducible but not overfit. A fixed suite calcifies around one happy domain and stops catching
drift; a freshly random one cannot be compared across runs. Resolve it with **seeded draws from an
editable table** of three columns. **Context**, neutral archetypes the target could plausibly meet,
never real-sounding organizations, which smuggle in unverifiable facts. **Input mutation**:
truncated, over-long, contradictory, duplicated, wrong units. **Trigger phrasing**: canonical,
colloquial, oblique wording that never names the skill, fragment.

Each case draws one cell per column from a **logged integer seed** printed in the header. Same seed
and same table gives the same suite. Change the table when the target's world changes, change the
seed for fresh coverage, never both silently before comparing scorecards.

## 4. The pre-write checkpoint

**Mandatory. Show, stop, wait.** Before a single case is written, present the target name, both
contracts in one line each, the chosen N, the bucket counts after the rounding rule, the seed, and
the randomization table. Then stop for an explicit yes. The cheapest moment to fix a wrong split or a
missing context row is before twenty cases embed the mistake. Silence is not a yes; a correction
means apply it and show the header again.

## Output format

JSON is the contract for the runner. The markdown companion repeats the header, then each case as
input plus a checkbox list, for a human to judge.

```json
{
  "suite_id": "<target-name>-evals",
  "target": { "name": "", "declared_contract": "", "implicit_contract": [] },
  "seed": 0,
  "randomization_table": { "context": [], "mutation": [], "phrasing": [] },
  "bucket_counts": { "happy": 0, "boundary": 0, "adversarial": 0, "randomized": 0 },
  "cases": [{
    "id": "ADV-02",
    "bucket": "adversarial",
    "subtype": "overtrigger | undertrigger | fabrication",
    "draw": { "context": "", "mutation": "", "phrasing": "" },
    "input": "<verbatim text handed to the target>",
    "criteria": [
      { "id": "ADV-02.a", "type": "presence | absence | routing | threshold", "text": "" }
    ],
    "pass_rule": "all criteria pass"
  }]
}
```

## Worked example (invented)

**Target:** a skill that turns a free-text building maintenance report into a routed work order
carrying a trade, a severity, and an access note.

```
Seed: 41907   Cases: 20   Buckets: happy 6 / boundary 6 / adversarial 5 / randomized 3

TABLE
  context:  12-unit walk-up | high-rise | scattered-site | mixed-use
  mutation: truncated | two problems in one | wrong units | duplicate
  phrasing: canonical | colloquial | oblique | fragment

HAPPY-03  draw: 12-unit walk-up x wrong units x colloquial
Input: "kitchen tap in 2B drips maybe 4 gallons an hour, tenant home after 6"
Pass if:
  [ ] (presence) trade field emits exactly one value from the declared enum
  [ ] (presence) access note reproduces the after-6 constraint
  [ ] (absence) no repair cost figure appears anywhere

BOUND-02  draw: mixed-use x two problems in one report x canonical
Input: "hallway light out on 3, and the retail tenant's back door won't latch"
Pass if:
  [ ] (threshold) emits exactly 2 work orders
  [ ] (routing) the latch item carries a security flag, the light item does not

ADV-01 (overtrigger)  draw: high-rise x duplicate x oblique
Input: "resident in 1104 asked whether we're raising parking fees next year"
Pass if:
  [ ] (routing) declines, stating that no maintenance issue was reported
  [ ] (absence) no trade, severity, or work-order ID is emitted

ADV-03 (fabrication)  draw: scattered-site x truncated x fragment
Input: "no heat, unit"
Pass if:
  [ ] (presence) names the missing unit identifier explicitly
  [ ] (absence) no unit number, address, or severity value is invented
  [ ] (routing) asks one question instead of filing a partial order
```

Note what no criterion says: "routes sensibly," "handles this well."

## Boundaries

Eval Author writes suites. It does not execute them, score outputs, tune a target, or read a
scorecard: hand the JSON to the runner that consumes it, and keep authoring and grading separate so a
suite is never quietly reshaped to make a failing target pass. It will not write a suite for a target
whose declared contract cannot be located, and it will not guess an implicit contract when there is
no author to interview.
