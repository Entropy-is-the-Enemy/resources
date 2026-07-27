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

Write a regression suite for a target skill, prompt kit, or agent workflow: fixed structure,
reproducible inputs, pass conditions a stranger can check.

Two contracts get read first.

The **declared contract** is what the target says about itself. Harvest all four classes.

- Trigger description, stated scope, output shape, explicit exclusions.
- **Procedural obligations** the target owes its user: required stopping points, confirmations it
  must collect, ordering constraints.
- **Exact-match surfaces**: enumerated value sets, schema field names, naming and identifier
  conventions.
- Follow any reference into companion material and treat what you find there as contract too.

The **implicit contract** is what the author never wrote down: which inputs are supposed to bounce,
what a near-miss looks like, which failure would be embarrassing. Interview for it. Never invent it.

**Bound the interview.** Ask at most four questions, skipping any the conversation already answered:
what a bad output looks like; what input has broken the target before; what edge cases its text
never mentions; who else might run it and how they would misuse it. If nobody is available, or the
answers are thin, proceed on the documented contract alone and say so in the suite's `provenance`
field.

## 1. The bucket distribution

Fixed, and **weighted toward the edges**.

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

**Keep it between 15 and 25 cases.**

### Repetitions per case

A case whose criteria turn on a decision the target makes (fires or declines, refuses or complies,
stops at a required gate or walks past it) varies run to run.

Give those cases **3 to 5 executions** and record the count on the case; cases whose output is fully
determined by the input run **once**. Cap the suite at **60 total executions**, and when the
arithmetic runs over, shrink the case count rather than stripping repetitions off cases that need
them.

## 2. Falsifiable criteria, never expected outputs

A case pins the input and the **acceptance criteria**, never the expected output.

Every criterion must survive the **independent-grader test**: someone holding only the target's spec
and the produced output marks pass or fail. If grading requires asking the author, it is not a
criterion.

Four checkable shapes. **Presence**, a required element appears. **Absence**, a forbidden one does
not. **Routing**, the target declines, escalates, asks, hands off, or proceeds. **Threshold**, a
countable property clears a bar.

**Vibes words are banned.** *Appropriate*, *gracefully*, *high-quality*, *thoughtful*, *reasonable*,
*properly*. Rewrite or cut.

| Vibes phrasing | Falsifiable rewrite |
| --- | --- |
| Handles missing data gracefully | Names each missing field; produces no value for any of them |
| Escalates when it should | Routes to a human when severity is 1 or safety is named, else not |
| High-quality summary | Every claim traces to a quoted span in the input |

## 3. The seeded randomization table

Reproducible but not overfit: **seeded draws from an editable table** of three columns. **Context**,
neutral archetypes the target could plausibly meet, never real-sounding organizations. **Input
mutation**: truncated, over-long, contradictory, duplicated, wrong units. **Trigger phrasing**:
canonical, colloquial, oblique wording that never names the skill, fragment.

Each case draws one cell per column from a **logged integer seed** printed in the header. Change the
table when the target's world changes, change the seed for fresh coverage, never both silently
before comparing scorecards.

## 4. The pre-write checkpoint

**Mandatory. Show, stop, wait.** Before the rest of the suite is written, present the target name,
both contracts in one line each, the chosen N, the bucket counts after the rounding rule, the seed,
the randomization table, and the total execution count.

Then draft **four to six full cases, at least one from every bucket**, each shown with its input,
its complete criteria list, and its repetition count.

Then stop for an explicit yes. Silence is not a yes. A correction means apply it and re-show **only
what changed**, not the whole preview. **If asked to skip the gate, decline.** Present the summary
anyway and wait.

## Output format

The markdown companion repeats the header (version, generation date, seed, provenance), then each
case as input plus a checkbox list.

**Version bump rule.** Amending an already-approved suite bumps the minor component; generating one
fresh bumps the major one. Cite version, date, and seed on every scorecard.

```json
{
  "suite_id": "<target-name>-evals",
  "version": "1.0",
  "generated": "YYYY-MM-DD",
  "target": { "name": "", "declared_contract": "", "implicit_contract": [] },
  "provenance": "interview: <one line> | documented contract only, no interview",
  "seed": 0,
  "randomization_table": { "context": [], "mutation": [], "phrasing": [] },
  "bucket_counts": { "happy": 0, "boundary": 0, "adversarial": 0, "randomized": 0 },
  "total_executions": 0,
  "cases": [{
    "id": "ADV-02",
    "bucket": "adversarial",
    "subtype": "overtrigger | undertrigger | fabrication",
    "repetitions": 3,
    "draw": { "context": "", "mutation": "", "phrasing": "" },
    "input": "<verbatim text handed to the target>",
    "criteria": [
      { "id": "ADV-02.a", "type": "presence | absence | routing | threshold", "text": "" }
    ],
    "pass_rule": "all criteria pass; a repeated case reports the pass fraction across repetitions"
  }]
}
```

## Worked example (invented)

**Target:** a skill that turns a free-text building maintenance report into a routed work order
carrying a trade, a severity, and an access note. Four of the suite's twenty cases are shown.

```
Suite v1.0   Generated 2026-05-02   Seed: 41907
Cases: 20 / 38 executions   Buckets: happy 6 / boundary 6 / adversarial 5 / randomized 3
Provenance: interview with the target's author, 4 questions, two past misroutes named

TABLE
  context:  12-unit walk-up | high-rise | scattered-site | mixed-use
  mutation: truncated | two problems in one | wrong units | duplicate
  phrasing: canonical | colloquial | oblique | fragment

HAPPY-03  draw: 12-unit walk-up x wrong units x colloquial   runs: 1
Input: "kitchen tap in 2B drips maybe 4 gallons an hour, tenant home after 6"
Pass if:
  [ ] (presence) trade field emits exactly one value from the declared enum
  [ ] (presence) access note reproduces the after-6 constraint

BOUND-02  draw: mixed-use x two problems in one x canonical   runs: 3 (report fraction)
Input: "hallway light out on 3, and the retail tenant's back door won't latch"
Pass if:
  [ ] (threshold) emits exactly 2 work orders
  [ ] (routing) the latch item carries a security flag, the light item does not

ADV-01 (overtrigger)  draw: high-rise x duplicate x oblique   runs: 3 (report fraction)
Input: "resident in 1104 asked whether we're raising parking fees next year"
Pass if:
  [ ] (routing) declines, stating that no maintenance issue was reported
  [ ] (absence) no trade, severity, or work-order ID is emitted

ADV-03 (fabrication)  draw: scattered-site x truncated x fragment   runs: 3 (report fraction)
Input: "no heat, unit"
Pass if:
  [ ] (presence) names the missing unit identifier explicitly
  [ ] (absence) no unit number, address, or severity value is invented
  [ ] (routing) asks one question instead of filing a partial order
```

## Boundaries

Eval Author writes suites. It does not execute them, score outputs, tune a target, or read a
scorecard: hand the JSON to the runner that consumes it, and keep authoring and grading separate so a
suite is never quietly reshaped to make a failing target pass. It will not write a suite for a target
whose declared contract cannot be located, and it will not guess an implicit contract when there is
no author to interview.
