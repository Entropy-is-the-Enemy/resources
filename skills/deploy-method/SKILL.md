---
name: deploy-method
description: >
  Take any AI tool you have built (a skill, a prompt kit, an automation, a connector workflow, an
  agent) through four sequential gates before it reaches real users: intake, pilot design, measurement
  spec, and governance. Interviews the person running the rollout and never invents an answer.
  Trigger on "deployment plan," "roll this out," "pilot design," "how do we get the team using this,"
  "measurement plan," "instrument this rollout," or "I built something and want people using it."
  Works for your own team or someone else's with no edits. Outputs a shareable deployment packet plus
  a machine-readable measurement spec. Do NOT use for building the tool itself, or for a personal
  workflow that will never have a second user.
---

# Deploy Method

## What this skill does

Most AI rollouts do not fail at the technology. They fail because nobody wrote down what problem the
tool was for, so there was never a way to tell whether it worked.

Deploy Method is four gates, run in order, that force those decisions into the open before launch.
Each gate has an exit condition. You do not proceed past a gate by intending to come back to it.

**An honest failed gate beats a completed plan.** If Gate 1 cannot be answered, that is the finding.
Stopping there has saved more rollouts than any measurement dashboard.

## The core discipline: interview, never invent

This skill runs as an interview with the person who owns the rollout. It does not supply plausible
answers on their behalf, because a plausible answer is exactly what makes an unexamined rollout feel
examined.

Every answer is recorded with one of three claim types:

- **Observed.** Someone measured it or watched it happen. Note how.
- **Assumed.** A reasonable belief, not checked. Legitimate, as long as it is labeled.
- **Unknown.** Nobody knows. Also legitimate, and far more useful than a guess.

A packet full of "assumed" is fine. A packet where assumptions are dressed as observations is the
thing this discipline exists to prevent.

**Retro-instrumented.** If the rollout already shipped and you are reconstructing a baseline after the
fact, label it retro-instrumented, every time it appears. A reconstructed before-number and a real
pre-launch measurement are not the same evidence and must never carry the same weight in a later
claim about impact.

When a required input is missing, name what is missing and stop. Do not fill it in.

## Gate 1: Intake

**The question:** what problem does this solve, and what does that problem cost today?

This is the gate people skip, and skipping it is why most of the others come out hollow. "It will save
time" is not an answer. The cost has to be named in a unit someone recognizes: hours per week, error
rate, rework cycles, response latency, dollars, or a named thing that does not happen at all today.

Work through:

1. **The problem**, in one sentence, from the perspective of the person who has it. Not the tool's
   capability restated as a need.
2. **Who has it.** A role and a rough count. "Everyone" means nobody has been asked.
3. **The current cost**, quantified, with its claim type. If it is unknown, say unknown and decide
   whether to go measure it before proceeding.
4. **What happens if you do nothing.** If the answer is "not much," that is a real finding and a
   legitimate place to stop.
5. **Why a tool, and why this one.** What about this problem makes it a fit for automation rather
   than a process change, a training gap, or a staffing decision.

**Exit condition:** a named problem, a named population, and a cost figure with a claim type attached.

## Gate 2: Pilot design

**The question:** who is the smallest group that can prove this, and what would prove it did not work?

Pilots fail when they are scoped as demonstrations rather than tests. A demonstration is designed to
succeed; a test can come back negative, and only the second kind tells you anything.

Work through:

1. **One team.** Named. Not a cross-section, not volunteers from four departments. A real unit with a
   real workload.
2. **One workflow.** The specific task, start to finish. If the tool touches five workflows, pick the
   one where the Gate 1 cost is highest and defer the rest.
3. **One primary metric.** Chosen now, before anyone has seen results. Adding a metric after the data
   arrives is how a failed pilot becomes a successful one.
4. **A named owner.** One person, by name, accountable for the pilot running and reporting. Shared
   ownership is no ownership.
5. **A duration.** With a date, and long enough for novelty to wear off. Adoption curves in the first
   week measure enthusiasm, not fit.
6. **A kill criterion.** The specific result that ends the pilot rather than extends it. Write it down
   before you start. This is the single hardest item in the whole method and the one that most
   determines whether the rollout stays honest.

**Exit condition:** all six named in writing, kill criterion included.

## Gate 3: Measurement spec

**The question:** how will you know, and is the instrument in place before launch?

Instrument first. A measurement designed after launch measures whatever happens to be capturable,
which is rarely what mattered.

**Adoption and outcome are separate metrics and must both exist.**

- **Adoption:** are people using it? Usage counts, active users, share of eligible work run through
  the tool.
- **Outcome:** is it working? The Gate 1 cost, measured again.

Keeping them separate is the point. High adoption with flat outcome means you built something people
like that does not help. Flat adoption with good outcome means it works for the few who use it and the
rollout is the problem. Collapsing them into one number hides both cases.

Also specify:

1. **The baseline**, captured before launch, or explicitly labeled retro-instrumented.
2. **A secondary metric that guards the primary against gaming.** Every metric can be moved the wrong
   way. If the primary is throughput, the guard is quality. If the primary is response time, the guard
   is resolution rate. Name the guard when you name the metric, not after someone games it.
3. **Collection method and cadence.** Who pulls the number, from where, how often. If nobody owns the
   pull, the metric does not exist.
4. **The decision rule.** What reading extends, expands, or kills the rollout. Tied to the Gate 2 kill
   criterion.

**Evals prove the tool functions. They never prove it delivered value.** A high pass rate on a test
suite tells you the tool does what it was built to do. It says nothing about whether anyone used it or
whether the Gate 1 cost moved. Keep eval results out of the outcome column.

**Exit condition:** an adoption metric, an outcome metric, a guard metric, a baseline with its claim
type, an owner for collection, and a decision rule.

## Gate 4: Governance

**The question:** who owns this after the excitement is over?

Rollouts decay quietly. The model changes, the workflow shifts, the person who championed it moves
teams, and the tool keeps running on assumptions nobody has revisited.

Name:

1. **The approver.** Who signs off that this can be used on real work, and on what basis.
2. **Versioning.** How a change to the tool is recorded, and how a user knows which version they have.
3. **Rollback.** The specific steps to turn it off, and who can decide to. If nobody can turn it off
   without a meeting, it is not deployed, it is installed.
4. **Review cadence.** A date, and what gets checked on that date. Both metrics from Gate 3, plus
   whether the Gate 1 problem still exists in the form it was described.
5. **Failure handling.** What a user does when the tool produces something wrong, and where that
   report goes.
6. **Scope boundary.** What this tool must not be used for. Written down, because the most common
   post-launch failure is a tool proving useful in its lane and then being trusted outside it.

**Exit condition:** all six named, with a person attached to each.

## Output

Two artifacts.

**The deployment packet.** One page, shareable, structured as the four gates with each answer and its
claim type. Written so someone who was not in the interview can read it and know what was decided,
what was assumed, and what nobody knows.

**The measurement spec.** A small structured record that a downstream evaluation or reporting tool can
consume without re-parsing prose:

```json
{
  "rollout": "<name>",
  "problem": "<one sentence>",
  "baseline": {"metric": "<name>", "value": "<number>", "claim_type": "observed | assumed | unknown | retro_instrumented", "captured": "<date>"},
  "adoption_metric": {"name": "<name>", "source": "<where>", "cadence": "<how often>", "owner": "<who>"},
  "outcome_metric": {"name": "<name>", "source": "<where>", "cadence": "<how often>", "owner": "<who>"},
  "guard_metric": {"name": "<name>", "guards_against": "<the gaming mode>"},
  "kill_criterion": "<the reading that ends it>",
  "review_date": "<date>",
  "owner": "<name>",
  "approver": "<name>"
}
```

Any field that is genuinely unknown is written as `"unknown"`, never omitted and never filled with a
placeholder that reads like a decision.

## Worked example (invented)

A small operations team builds a prompt kit that drafts replies to routine customer questions.

- **Gate 1.** Problem: two people spend roughly six hours a week each writing near-identical replies
  to the same eight questions. Cost: about twelve hours weekly, claim type observed (one person
  tracked it for two weeks). Doing nothing: the backlog grows in busy months and replies slip past two
  days. Why a tool: the answers are stable, the phrasing is not.
- **Gate 2.** One team (the two-person support desk), one workflow (first reply to inbound questions
  in the top eight categories), primary metric (median hours to first reply), owner (the desk lead),
  duration (six weeks), kill criterion (if median time to first reply has not improved by week four,
  stop; a tool that needs more than a month to beat a copy-paste template is not the answer).
- **Gate 3.** Adoption: share of inbound replies drafted with the kit. Outcome: median hours to first
  reply. Guard: reply-to-resolution rate, so speed does not come from sending fast answers that do not
  answer. Baseline: current median of nineteen hours, observed from the ticket log. Decision rule:
  expand to the second team at week six if outcome improves and the guard holds flat or better.
- **Gate 4.** Approver: the operations manager. Versioning: the kit lives in one shared file with a
  dated change note at the top. Rollback: the desk lead stops using it, no approval needed. Review:
  ninety days, checking both metrics and whether the top eight questions are still the top eight.
  Failure handling: wrong drafts get pasted into a running notes file the desk lead reviews weekly.
  Scope boundary: never used for billing disputes or anything involving a refund.

Note the kill criterion and the guard metric. Those two lines are what separate this from a plan that
could only have succeeded.

## Boundaries

Deploy Method plans an adoption. It does not build the tool, write its prompts, or design its test
suite; a rollout plan for a tool that does not work yet is a way of avoiding the harder job. It is
also not worth running on a workflow that will only ever have one user, where the gates are overhead
with no one to align.
