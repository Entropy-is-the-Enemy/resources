---
name: sub-agent-ops
description: >
  Design and launch orchestrated agent runs: select the architecture (single
  agent plus Skills, a workflow, or a multi-agent pattern), pick the pattern
  and run mode (eval-grade or production), seal the worker packets, present a
  run plan, and spawn on your confirmation. Trigger on "sub-agent-ops", "spin
  up sub-agents", "fan out", "fan this out", "parallelize", "launch
  agents", "run these as separate agents", "orchestrate this", "design a run",
  "should I use sub-agents for this", or when you describe work with many
  independent units (N profiles, N documents, N variants) or ask for
  independent verification or variance measurement. Lane boundary: if a
  dedicated test-suite runner owns execution, defer to it and stop. This skill
  orchestrates session work; it never invokes other skills and is never invoked
  by them. Do not trigger for single-unit judgment work with no isolation
  value; Step 0 and Step 1 exist to refuse those.
---

# Sub-Agent Ops

Turn a job into a designed, disclosed, launched agent run.

Style: no em dashes in generated files.

## Step 0: Architecture check (is a multi-agent run even right?)

Before asking whether to spawn, ask what shape the job wants:

1. **Control needed?** High (regulated, auditable, safety-critical) favors one agent or a gated workflow; low (research, brainstorming) tolerates autonomy.
2. **Domain complexity?** One domain favors one agent; distinct domains that must coordinate favor multi-agent.
3. **Resource ceiling?** Multi-agent runs cost far more tokens; tight budgets favor a lean workflow.
4. **Depth of expertise?** One established domain is usually one agent plus Skills; several deep domains that interlock favor specialists.

Most work is a single agent plus Skills, or a plain workflow, and never reaches a spawn. High-control or single-domain work: say so and stop. Open-ended, multi-directional, or isolation-critical work: continue to Step 1.

## Step 1: Spawn check

Spawn only if at least one holds:

1. **Isolation has evidentiary value.** The output is worth more because the executor could not see something (criteria, grader intent, prior drafts).
2. **Fan-out width.** Many independent units of the same job.
3. **Context protection.** The job would flood this context with raw material when only conclusions are needed.
4. **Variance measurement.** Repeated runs need fresh contexts; one agent repeating itself anchors on its first answer.

**Cost must clear the value bar.** A fan-out costs roughly N times a single agent (N = agent count, each with its own context window) and wins decisively only on genuinely multi-directional work. Meeting a criterion is necessary, not sufficient.

If none holds, say so plainly, name the inline alternative, and stop. One unit of judgment-shaped work, context that lives in this conversation, and a briefing longer than the work all stay inline.

## Step 2: Pick the pattern

Climb only as far as the job needs; most jobs stop at the first two rungs.

| Pattern | Use when | Core rule |
|---|---|---|
| Single agent + Skills | One coherent domain, open-ended path | No spawn; equip with Skills first |
| Sequential workflow | Fixed stages, each feeds the next | Predefined control flow; gate between stages |
| Fan-out executor | N independent units, judged after | Blind executors, orchestrator holds all judgment |
| Routing | Inputs split into distinct classes | Classify first, send to a specialist path |
| Evaluator-optimizer | Clear criteria, iteration lifts quality | Generator revises; fresh-context evaluator each round; cap at 2-4 cycles |
| Pipeline | Staged transformation, fresh eyes per stage | Each stage sees only its input artifact, never upstream reasoning; checkpoint between stages (error compounds, 0.95^n) |
| Independent verifier | Finished work needs fresh-context checking | Verifier gets sources, never the producer's reasoning |
| Hierarchical / supervisory | A supervisor delegates to specialists | Subagents are tools; supervisor synthesizes |
| Proxy executor | Agent stands in for a runtime or person you cannot drive | Disclose what the proxy tests and what it does not |
| Collaborative / peer | Coordination emergence is the goal, independence is NOT claimed | Peers share context; forfeits the isolation credential, so use rarely |

**Patterns compose.** A fan-out commonly feeds an independent verifier; one row does not forbid a second stage.

## Step 2b: Pick the mode

- **Eval-grade** (default when isolation has evidentiary value, variance is measured, or outputs will be graded or compared): full ceremony. Withholding, pre-registered judgment standard, contamination caveats, provisional verdicts.
- **Production** (throughput, coverage, or speed on work not graded against withheld criteria): lighter. No rubric and no withholding-for-contamination; executors may see the goal. State a plain acceptance note instead.

**Non-negotiable in both modes:** the Step 4 gate, the Step 4b leak check, the cost check, dry-run on all state-changing calls, verify-do-not-trust, partial-failure disclosure, the disclosure header. Withholding still applies in production wherever an independence claim will be made; if you will claim it, that unit is eval-grade. Production is a lighter path, never a loophole.

## Step 3: Design the run

Fill the Step 4 plan block as you go, deciding in order:

1. **Units and runs.** What one unit is, and runs per unit (runs > 1 means that many separate agents, never one agent asked to repeat itself).
2. **Withholding (eval-grade).** Whatever the output is judged against stays out of the packet: criteria, rubric, grader intent, sibling angles, orchestrator purpose. In production mode, state that withholding is off and why independence is not claimed.
3. **Isolation level.** same-session / cross-session inputs / sub-agent with withholding. Disclosed, never hidden.
4. **Tool surface.** Read-only calls may run live. Any state-changing call (create, update, delete, send) is dry-run: state the exact call and full payload, then continue as if it succeeded. No live writes against production systems during evaluation, ever.
5. **Completeness floor.** Minimum clean units for the verdict to stand, set before launch.
6. **Packets.** One sealed packet per agent, every field present:

```
Unit id:        <id>
Task:           <what to produce; no statement of what is being tested>
Inputs:         <paths, not pasted content, where the agent can read files>
Deliverable:    <format; one message back, not a conversation>
Return ceiling: <size cap; conclusions, not raw dumps>
Tool rules:     <read-only calls live; every state-changing call dry-run>
Missing inputs: report any unreadable or missing input, continue with what
                is available, never manufacture source content
```

A return reporting a missing input marks that unit degraded in the Step 6 tally.

## Step 4: Confirm gate, mandatory

Present this plan and do not launch until the user confirms. No exceptions, including read-only runs. **Every field is answered.** A field that does not apply gets an explicit "none" or "N/A because ...", never a blank and never a dropped row; silence is not a value.

```
Architecture:       <spawn, or stay inline and why>
Pattern:            <row from Step 2, plus any second stage>
Mode:               <eval-grade or production>
Agent count:        <U> units x <R> runs per unit = <N> agents
Withheld:           <list, or "nothing, independence not claimed">
Isolation level:    <same-session / cross-session inputs / sealed sub-agent>
Simulated cases:    <every state-changing call to be dry-run, or "none">
Completeness floor: <minimum clean units for the verdict to stand>
Cost:               <N>x a single agent, justified because <...>
Judgment standard:  <eval-grade: what outputs are scored against>
Acceptance note:    <production: what good enough means>
Pilot checkpoint:   <yes, batch of n / no, so all verdicts ship PROVISIONAL>
Raw returns to:     <path, written before judging>
```

The count line shows its arithmetic, so an agent count that disagrees with the stated fan-out is visible on the page. Draft the judgment standard yourself and have the user ratify it here, one sentence minimum even for eyeball runs, fixed before launch so it cannot drift. Skipping the committed checkpoint is a change to an approved plan and gets reported as one.

## Step 4b: Leak check before sending, mandatory

Withholding decided is not withholding done, and the second act is where leakage is caught. Before any spawn, re-read the literal text of each finished packet and confirm none of these appears in it:

- the completeness floor or acceptance bar
- the judgment standard or scoring scheme
- any statement of what is being tested or why the run exists
- any reference to a sibling agent's angle, packet, or output

A staged handoff passes the prior stage's output artifact only, never its reasoning. Production mode turns this check off by declaration only: any unit carrying a later independence claim gets the check regardless of declared mode.

## Step 5: Launch

Honor the pilot commitment from the gate: launch the first batch, checkpoint, then fan the rest. Batch independent spawns in parallel. Fresh context per unit; continue an existing agent only where accumulated context is the asset and independence is not claimed.

## Step 6: Collect, verify, disclose

- **Persist before judging.** Write raw returns to the path committed at the gate, keyed by unit id, before any judgment forms. The audit trail is the product.
- **Protect the orchestrator's context.** At synthesis, read slices or per-unit summaries from that file, never all N raw returns into the live window; an orchestrator that inhales everything degrades its own reasoning.
- **Never take executor say-so.** Any claim that something exists in a source gets mechanically verified (grep, read) before it supports a conclusion.
- **Tally completeness.** Count returned / errored / unusable / degraded by unit id. If the floor is missed, the verdict is INCOMPLETE, not merely provisional. Failed units are named, never dropped silently.
- **Hold the checkpoint you committed to.** Surface 2 to 3 raw returns before grading or synthesizing. Where it is not held, every verdict is PROVISIONAL and says so.
- **Front the deliverable with this header.** Same no-blank rule as the plan, and it bites hardest on the caveat rows, where a blank is what a softened caveat looks like:

```
Architecture:   <verdict and pattern>
Mode:           <eval-grade or production>
Agents:         <N> (<U> units x <R> runs)
Isolation:      <level>
Withheld:       <list, or "nothing, independence not claimed">
Simulated:      <cases dry-run, or "none, read-only run">
Proxy caveat:   <what the proxy tests and does not, or "no proxy used">
Contamination:  <caveats, or "none known">
Completeness:   returned <n> of <M>, errored <n>, unusable <n>, degraded <n>
Checkpoint:     held on <n> returns, or NOT HELD so verdicts are PROVISIONAL
Raw returns:    <path>
```

The disclosure is the credential.

## Anti-patterns

- Skipping the Step 0 architecture check, or spawning for single-unit judgment work Step 1 should have refused.
- One agent asked to repeat itself for variance.
- Criteria, rubric, or grader intent leaking into an eval-grade packet.
- Sending packets that were never re-read against the Step 4b leak list.
- A worker inventing the content of a source it could not read, instead of reporting the gap.
- Production mode used where an independence claim will be made.
- Launching without the Step 4 gate.
- A blank or dropped row in the plan or the disclosure header.
- Live writes from any agent during an eval or experiment.
- Reloading all raw outputs into the orchestrator context on a wide run.
- Dropping errored or unusable units silently; judging past a missed completeness floor without saying INCOMPLETE.
- Softening the disclosure of isolation level, simulation, mode, or proxy caveats.
- Grading standard set or changed after outputs are seen.
- Orchestrating another skill's internal work (if a dedicated runner owns execution, defer).
