---
name: eval-scorer
description: >
  Run an existing test suite against a live skill or prompt and produce a fixed-format scorecard:
  per-case PASS/PARTIAL/FAIL verdicts, variance across repeated runs, failure patterns clustered by
  cause with one highest-leverage fix each, and a disposition of ship, iterate, or investigate.
  Trigger on "run the evals," "grade this skill," "score it against the suite," or "did my changes
  regress anything." REQUIRES an existing suite as input, a JSON file of cases carrying prompts and
  acceptance criteria. With no suite it stops and says so rather than inventing cases, because a
  grader that writes its own test is grading itself. Does NOT author suites, edit the target under
  test, or tune prompts until cases pass.
---

# Eval Scorer

## What this skill does

This is the grading half of a build-and-test toolchain: something else authors the suite, this skill
runs every case against the live target and scores it. The governing principle: **an honest FAIL is
worth more than a generous PASS.** Its corollary: a verdict you could not actually observe is worth
less than no verdict at all.

## The input contract and the run loop

**Required fields per case.** A case missing any of these is unrunnable: report it SKIPPED, name the
missing field, keep going.

- `id`: stable across runs
- `prompt`: the exact user input, verbatim, never paraphrased at run time
- `bucket`: core, edge, adversarial, negative, format
- `criteria`: ordered observable conditions, each independently checkable
- `expect_trigger`: true or false. Negative cases assert the target should stay quiet
- `repeats`: how many independent executions this case gets. No default is supplied

Optional: `state_changing` (default false). Honor the repeat count each case declares and never
substitute one of your own; a case that omits `repeats` is SKIPPED like any missing field.

**Pre-flight gate.** All four checks pass before the first case is dispatched. Any one failing stops
the run and reports which check failed, by name. A single unrunnable case does not trip the gate; it
goes SKIPPED inside the loop as usual.

1. The suite file parses, and carries its top-level metadata: suite id, case count, case list.
2. The target is located, and confirmed to be the live artifact the suite names, not a stale copy and
   not a same-named file shadowing it from elsewhere. Verify, never assume.
3. The target's identity is captured: name, version or content hash, last-modified date, suite id.
4. Execution mode is decided per case in advance, with the list of cases that will be simulated fixed
   before the first dispatch, never mid-loop.

**The loop.** For each case in suite order: dispatch, capture the raw output, store it untouched, move
on. Do not grade inside the loop, fix a failing target and rerun it, or reorder cases to lead with the
impressive ones. Grading is a separate pass over the stored outputs.

**Dry-run every state-changing action.** If a case would send a message, write a file, update a
record, or call an external system, the target names the action and its arguments instead of
performing it, and you grade the intent. For every simulated case, check whether any criterion
depends on observing what the real action would have returned, and mark the case weakened if one does.

## Isolation

**Each case runs in an isolated agent that receives the prompt and nothing else.** Not the criteria.
Not the bucket label. Not the case id. Not the other cases. Not the fact that this is a test.

A case declaring `repeats` above one gets that many separate, independently initialized executions.
One execution asked to answer the same prompt several times does not satisfy the count, nor does a
warmed context reused across repetitions.

A model that can see the criteria will satisfy them. Isolation also stops state leaking: case 7 must
not benefit from a correction absorbed in case 3, or from its own third repeat.

**When true isolation is impossible, say so in the report.** Run anyway, in the strictest arrangement
available, and put the caveat in the header: which cases shared context, which way the bias runs.

**Human checkpoint before grading.** Stop after capture. Put three to five raw outputs in front of a
person and ask one question: are these real responses to these prompts.

## Grading, variance, and failure patterns

**Verdicts.** Grade against the criteria only, one line of quoted evidence per verdict. Ties break
toward the harsher verdict.

- **PASS**: every criterion met. One miss is not a pass.
- **PARTIAL**: core behavior present but a criterion unmet, or the right output with a defect: a
  missing section, a skipped confirmation.
- **FAIL**: core behavior absent, wrong, or fabricated, or the target fired on a negative case or
  stayed silent on a positive one.

**FLAGGED criteria.** A criterion that cannot be judged as written is flagged, not failed: it is
self-contradictory, unobservable in what the case actually elicited, or asserts something the prompt
never made possible. Write one line on why it is unjudgeable, attribute it to the suite rather than
the target, route it to whoever owns the suite, and grade the case on its remaining criteria. The
harsh tie-break applies to judgeable criteria only.

**Variance rule.** Any case with `repeats > 1` scores on its worst run, spread reported. Three PASS
and one FAIL is a FAIL with variance flagged, not 75 percent. A verdict that changes across repeats is
itself a finding, usually an ambiguous instruction.

**Failure patterns.** Cluster every PARTIAL and FAIL.

- **Overtriggering**: fires on negative cases, or on work it does not own
- **Undertriggering**: silent inside its stated scope
- **Fabrication**: invents a value, source, or field the input never supplied
- **Missing checkpoint**: acts where the criteria require confirmation
- **Lane drift**: starts the right task, finishes a different one
- **Format violation**: correct substance, wrong shape

Each cluster gets exactly **one** fix, an imperative naming the text to change, and it must be the
highest-leverage one.

## Output format

```
EVAL SCORECARD
Target: <name> | version <v> | modified <yyyy-mm-dd>
Suite: <id> | <n> cases | repeats: <r>
Isolation: full | partial (<which cases shared context, bias direction>)
Simulated: <case ids> | weakened: <ids whose criteria needed the un-observed result>
Checkpoint: raw outputs reviewed by <role> before grading

SCORE
  PASS <n>  PARTIAL <n>  FAIL <n>  SKIPPED <n>   (<n> of <n> run)
  by bucket: core <p/t> | edge <p/t> | adversarial <p/t> | negative <p/t> | format <p/t>

CASES
  <id>  <bucket>  <PASS|PARTIAL|FAIL|SKIPPED>  [variance: <n>/<r> agree]
     evidence: "<quoted from output>"
     unmet: <criterion, if any>

FAILURE PATTERNS
  1. <pattern name> (<case ids>)
     fix: <one imperative sentence>

FLAGGED CRITERIA (suite defects, not target failures)
  <case id>: <criterion> - <why it cannot be judged as written>

VARIANCE NOTES
  <cases whose verdict changed across repeats, and the likely ambiguity>

DISPOSITION: SHIP | ITERATE | INVESTIGATE
  <one sentence of why>
```

**SHIP**: core and negative buckets clean, no FAIL. **ITERATE**: failures cluster into named patterns
with fixes. **INVESTIGATE**: incoherent results, wide variance, or checkpoint doubt about the harness.
Investigate is not a soft iterate; it means do not trust the scorecard yet.

A run whose only shortfalls are flagged criteria does not fall to ITERATE; the disposition sentence
says the fix belongs to the suite.

## Worked example (invented)

```
EVAL SCORECARD
Target: weather-hold | version 0.4 | modified 2031-05-02
Suite: pool-closure-v2 | 14 cases | repeats: 3
Isolation: full (fresh context per case and per repeat, criteria withheld)
Simulated: C-03, C-08 (closure notices) | weakened: C-08
Checkpoint: 4 raw outputs reviewed by the aquatics lead before grading

SCORE
  PASS 8  PARTIAL 3  FAIL 2  SKIPPED 1   (13 of 14 run)
  by bucket: core 4/4 | edge 2/4 | adversarial 1/2 | negative 1/3 | format 0/1

CASES
  C-07  negative     FAIL   [variance: 2/3 agree]
     evidence: "Recommend closure." (input: light drizzle, 74F, no advisory)
     unmet: must not recommend closure absent a listed hazard
  C-11  adversarial  FAIL
     evidence: "Wind gusts near 40 mph." (feed reported gusts as unavailable)
     unmet: no value may be stated that the feed did not provide
  C-14  edge         SKIPPED (no `criteria` field)
  (the 8 PASS and 3 PARTIAL cases are omitted here for brevity; a real
  scorecard lists every case that ran)

FAILURE PATTERNS
  1. Overtriggering on mild weather (C-05, C-07)
     fix: replace "conditions that may be unsafe" with the four named hazards and
     require one by name before any closure recommendation.
  2. Fabrication on missing feed values (C-11)
     fix: add "if a field reads unavailable, write unavailable; never estimate it."
  3. Format violation (C-09, C-12)
     fix: move the notice template above the reasoning section.

FLAGGED CRITERIA (suite defects, not target failures)
  C-08: "confirms the notice reached every listed site" - the notice was simulated,
  so there is no delivery result to observe; unjudgeable as written.

VARIANCE NOTES
  C-07 flipped on 2 of 3 independent runs. "Use judgment on borderline days" makes
  the drizzle case genuinely ambiguous rather than merely wrong.

DISPOSITION: ITERATE
  Core logic is sound; every failure traces to three fixable lines of instruction.
  C-08 is a suite repair and belongs to the suite's owner.
```

## Boundaries

This skill executes and grades. It does not author cases, repair a malformed suite, supply a default
run count, edit the target, tune prompts until cases pass, or grade taste. Suite design belongs to the
step that produced the file. If the suite is thin, say so and grade what is there. If a target passes
every criterion and the output is still bad, the criteria are incomplete, and that finding goes to the
suite's owner.
