---
name: sub-agent-ops
description: >
  Design and launch orchestrated agent runs: select the architecture (single
  agent plus Skills, a workflow, or a multi-agent pattern), pick the topology
  and run mode (eval-grade or production), build sealed briefs, present a run
  plan, and spawn on your confirmation. Trigger on "sub-agent-ops", "spin
  up sub-agents", "fan out", "fan this out", "parallelize this", "launch
  agents", "run these as separate agents", "orchestrate this", "design a run",
  "should I use sub-agents for this", or when you describe work with many
  independent units (N profiles, N documents, N variants) or ask for
  independent verification or variance measurement. Lane boundary: if a
  dedicated test-suite runner owns execution, defer to it and stop. This skill
  orchestrates session work; it never invokes other skills and is never invoked
  by them. Do not trigger for single-unit judgment work with no isolation
  value; Step 0 and Step 1 exist to say no to those.
---

# Sub-Agent Ops

Turn a job into a designed, disclosed, launched agent run. This skill covers the design and orchestration of sub-agent runs from within a session: it decides whether to spawn, which pattern and mode to use, how to seal briefs, and how to collect and disclose results.

Style: no em dashes in any generated file.

## Step 0: Architecture check (is a multi-agent run even right?)

Before asking whether to spawn, ask what shape the job wants. Answer four questions:

1. **Control needed?** High (regulated, auditable, safety-critical) favors a single agent or a sequential workflow with gates; low (research, brainstorming) tolerates more autonomy.
2. **Domain complexity?** Single domain favors a single agent; multiple distinct domains that must coordinate favor multi-agent.
3. **Resource ceiling?** Multi-agent runs cost far more tokens; tight budgets favor a single agent or a lean workflow.
4. **Depth of expertise?** An established single domain is often a single agent plus Skills; several deep domains that interlock favor specialists.

Most work is a single agent plus Skills, or a plain workflow, and should never reach a spawn. High-control or single-domain work: say so and stop. Open-ended, multi-directional, or isolation-critical work: continue to Step 1. The honest "keep it a single agent" is part of the product, same as the honest no below.

## Step 1: Spawn check

Spawn only if at least one holds:

1. **Isolation has evidentiary value.** The output is worth more because the executor could not see something (criteria, grader intent, prior drafts).
2. **Fan-out width.** Many independent units of the same job.
3. **Context protection.** The job would flood this context with raw material when only conclusions are needed.
4. **Variance measurement.** Repeated runs need fresh contexts; one agent repeating itself anchors on its first answer.

**Cost must clear the value bar.** A fan-out costs roughly N times a single agent (N = agent count; each runs its own context window). Multi-agent architectures run several times a single agent's cost in the general case and win decisively only on genuinely multi-directional work. Meeting a criterion is necessary, not sufficient: if breadth or isolation value does not clear the N-times cost, stay inline.

If none holds, say so plainly, name the inline alternative, and stop. Stay inline when the task is one unit of judgment-shaped work, when the needed context is this conversation itself, or when the briefing would be longer than the work.

## Step 2: Pick the pattern

Climb the ladder only as far as the job needs. Most jobs stop at the first two rungs.

| Pattern | Use when | Core rule |
|---|---|---|
| Single agent + Skills | One coherent domain, open-ended path | No spawn; equip with Skills first |
| Sequential workflow | Fixed stages, each feeds the next | Predefined control flow; gate between stages |
| Fan-out executor | N independent units, judged after | Blind executors, orchestrator holds all judgment |
| Routing | Inputs split into distinct classes | Classify first, send to a specialist path |
| Evaluator-optimizer | Clear criteria, iteration lifts quality | Generator revises; fresh-context evaluator each round; cap at 2-4 cycles |
| Pipeline | Staged transformation, fresh eyes per stage | Each stage sees only its input artifact, not upstream reasoning; checkpoint between stages (error compounds, 0.95^n) |
| Independent verifier | Finished work needs fresh-context checking | Verifier gets sources, never the producer's reasoning |
| Hierarchical / supervisory | A supervisor delegates to specialists | Subagents are tools; supervisor synthesizes |
| Proxy executor | Agent stands in for a runtime or person you cannot drive | Disclose what the proxy tests and what it does not |
| Collaborative / peer | Coordination emergence is the goal, independence is NOT claimed | Peers share context; forfeits the isolation credential, so use rarely and disclose |

**Patterns compose.** A fan-out commonly feeds an independent verifier; most real runs are hybrids. Picking one row does not forbid a second stage.

## Step 2b: Pick the mode

- **Eval-grade** (default when isolation has evidentiary value, variance is measured, or outputs will be graded or compared): full ceremony. Withholding, pre-registered judgment standard, contamination caveats, provisional verdicts.
- **Production** (throughput, coverage, or parallel speed on work that is not graded against withheld criteria): lighter. No grading rubric and no withholding-for-contamination; executors may see the goal. State a plain acceptance note instead of a judgment standard.

**Non-negotiable in both modes:** the Step 4 gate, the cost check, dry-run on all state-changing calls, verify-do-not-trust, partial-failure disclosure, and the disclosure header. Withholding still applies in production mode whenever any independence claim will later be made; if you will claim it, you are in eval-grade for that unit. Production mode is a lighter path, never a loophole around the isolation discipline.

## Step 3: Design the run

Build the run plan using `references/run-plan-template.md`. Decide, in order:

1. **Units and runs.** What one unit is; how many agents; runs per unit (runs > 1 means that many separate agents, never one agent asked to repeat itself).
2. **Withholding (eval-grade).** Whatever the output is judged against stays out of the brief: criteria, rubric, grader intent, sibling angles, orchestrator purpose. State explicitly what each agent will NOT see. In production mode, state that withholding is off and why independence is not claimed.
3. **Isolation level.** same-session / cross-session inputs / sub-agent with withholding. Disclosed, never hidden.
4. **Tool surface.** Read-only calls may run live. Any state-changing call (create, update, delete, send) is dry-run: the agent states the exact call and full payload, then continues as if it succeeded. List every case simulated. No live writes against production systems during evaluation or experimentation, ever.
5. **Completeness floor.** The minimum clean units for the verdict to stand. Set before launch.
6. **Briefs.** One sealed brief per agent from the template: deliverable format stated explicitly (one message back, not a conversation), a return-size ceiling (return conclusions, not raw dumps), paths instead of pasted content where the agent can read files itself, execution-mode rules whenever tools are touched.

## Step 4: Confirm gate, mandatory

Present the run plan to the user: architecture verdict, pattern, mode, agent count, what is withheld, isolation level, simulated-case list, completeness floor, rough cost (state N and the N-times token cost; confirm the job is multi-directional or isolation-critical enough to justify it). In eval-grade, present the judgment standard (what outputs are scored against): draft it, have the user ratify or correct it here, minimum one written sentence even for eyeball runs, never blank, fixed before launch so it cannot drift. In production mode, present the one-line acceptance note instead. Do not launch until the user confirms. No exceptions, including read-only runs.

## Step 5: Launch

For wide runs, default to a pilot batch: launch 2-3, checkpoint with the user, then fan the rest (skip only for small or unattended-by-design runs). Spawn independent agents; batch independent spawns in parallel. Fresh context per unit; never continue an existing agent across units whose independence will later be claimed. Continue an agent only when accumulated context is the asset and independence is not claimed.

## Step 6: Collect, verify, disclose

- **Persist before judging.** When outputs will be graded or compared, write raw outputs to a working file keyed by unit id before any judgment forms. The audit trail is the product.
- **Protect the orchestrator's context.** The persisted file is also context hygiene: at synthesis, read slices or per-unit summaries, never reload all N raw outputs into the live window. For very wide runs, summarize per unit before synthesizing across units. This is the supervisor-context-overflow failure mode: an orchestrator that inhales every raw return degrades its own reasoning.
- **Never take executor say-so.** Any agent claim that something exists in a source gets mechanically verified (grep, read) before it supports a conclusion.
- **Tally completeness.** Count returned / errored / unusable by unit id. If the floor is missed, the verdict is INCOMPLETE (not merely provisional) and says so. Errored and unusable units are named, never dropped silently.
- **Checkpoint judgment-heavy runs.** Before grading or synthesizing a large run, surface 2 to 3 raw outputs to the user. Where a checkpoint cannot be held, mark every verdict PROVISIONAL and say so loudly.
- **Disclose in the deliverable header:** architecture verdict, pattern, mode, agent count, isolation level, contamination caveats, simulated cases, proxy caveat if any, completeness (returned N of M, errored, unusable), checkpoint status. Hiding or softening a caveat is the cardinal anti-pattern; the disclosure is the credential.

## Anti-patterns

- Reaching Step 1 without the Step 0 architecture check (spawning where a single agent plus Skills would do).
- Spawning for single-unit judgment work the spawn check should have refused.
- One agent asked to repeat itself for variance.
- Criteria, rubric, or grader intent leaking into an eval-grade executor brief.
- Production mode used where an independence claim will be made.
- Launching without the Step 4 gate.
- Live writes from any agent during an eval or experiment.
- Reloading all raw outputs into the orchestrator context on a wide run.
- Dropping errored or unusable units silently; judging past a missed completeness floor without saying INCOMPLETE.
- Softened or omitted disclosure of isolation level, simulation, mode, or proxy caveats.
- Grading standard set or changed after outputs are seen.
- Orchestrating another skill's internal work (if a dedicated runner owns execution, defer).
