# Run Plan and Sealed Brief Templates

Use both verbatim as structure; fill every field. A field that does not apply gets "none", never silence.

## Run plan (presented at the Step 4 gate)

```
## Run plan: <job name>

| Field | Value |
|---|---|
| Architecture verdict | why a multi-agent run beats a single agent + Skills or a plain workflow (Step 0) |
| Pattern | single-agent / sequential / fan-out executor / routing / evaluator-optimizer / pipeline / independent verifier / hierarchical / proxy / collaborative |
| Mode | eval-grade / production (production forfeits withholding; state why independence is not claimed) |
| Spawn criteria met | which of the four, one line each |
| Units | what one unit is, and the count |
| Agents | total agents (units x runs per unit) |
| Runs per unit | n (each run is a separate agent) |
| Withheld from executors | eval-grade: explicit list (criteria, rubric, intent, sibling angles). production: "none, independence not claimed" |
| Judgment standard / acceptance note | eval-grade: what outputs are scored against, drafted then ratified at the gate, minimum one written sentence, never blank. production: one-line acceptance note |
| Isolation level | same-session / cross-session inputs / sub-agent with withholding |
| Tool surface | read-only live; state-changing calls dry-run |
| Simulated cases | list, or none |
| Proxy caveat | what the proxy tests and what it does not, or none |
| Completeness floor | minimum clean units for the verdict to stand |
| Checkpoint plan | pilot batch (2-3 first) y/n; raw outputs surfaced before judgment y/n; if no, verdicts PROVISIONAL |
| Output destination | working file path for raw outputs, keyed by unit id |
| Rough cost | agent count N and the N-times token cost; confirm value clears the bar |

Launch on confirm.
```

## Sealed brief (one per agent)

```
You are executing one unit of work. Return one complete message; there is no
follow-up conversation.

Task: <the unit's prompt, self-contained>

Sources you may read: <paths, not pasted content, where readable>

Execution rules:
- Read-only tool calls (searches, gets, queries) may run live.
- Any state-changing call (create, update, delete, send): do NOT execute.
  State the exact tool call and full payload you would send, then continue
  as if it succeeded.
- If a source is missing or unreadable, say so and continue with what you
  have; never fabricate source content.

Deliverable format: <exact structure of the message to return>
Return-size ceiling: <return conclusions, not raw dumps; cap at <size>>
```

Withholding check before sending each brief (eval-grade): confirm it contains no acceptance criteria, no grading rubric, no statement of what the orchestrator is testing, no reference to other agents' angles or outputs (pipeline stages receive the upstream artifact only, not upstream reasoning). In production mode, withholding is off by declaration; if any independence claim will be made about a unit, that unit is eval-grade and the check applies.

## Deliverable header (disclosure block for the final output)

```
| Architecture | <why multi-agent over single> |
| Execution | <pattern>, <mode>, <n> agents, <runs> per unit |
| Isolation | <level>; <contamination caveats> |
| Simulated | <cases or none> |
| Proxy caveat | <or none> |
| Completeness | returned <N> of <M>; errored <ids>; unusable <ids>; floor met y/n |
| Checkpoint | held <date> / NOT HELD, verdicts provisional |
| Raw outputs | <path> |
```
# Run Plan and Sealed Brief Templates

Use both verbatim as structure; fill every field. A field that does not apply gets "none", never silence.

## Run plan (presented at the Step 4 gate)

```
## Run plan: <job name>

| Field | Value |
|---|---|
| Architecture verdict | why a multi-agent run beats a single agent + Skills or a plain workflow (Step 0) |
| Pattern | single-agent / sequential / fan-out executor / routing / evaluator-optimizer / pipeline / independent verifier / hierarchical / proxy / collaborative |
| Mode | eval-grade / production (production forfeits withholding; state why independence is not claimed) |
| Spawn criteria met | which of the four, one line each |
| Units | what one unit is, and the count |
| Agents | total agents (units x runs per unit) |
| Runs per unit | n (each run is a separate agent) |
| Withheld from executors | eval-grade: explicit list (criteria, rubric, intent, sibling angles). production: "none, independence not claimed" |
| Judgment standard / acceptance note | eval-grade: what outputs are scored against, drafted then ratified at the gate, minimum one written sentence, never blank. production: one-line acceptance note |
| Isolation level | same-session / cross-session inputs / sub-agent with withholding |
| Tool surface | read-only live; state-changing calls dry-run |
| Simulated cases | list, or none |
| Proxy caveat | what the proxy tests and what it does not, or none |
| Completeness floor | minimum clean units for the verdict to stand |
| Checkpoint plan | pilot batch (2-3 first) y/n; raw outputs surfaced before judgment y/n; if no, verdicts PROVISIONAL |
| Output destination | working file path for raw outputs, keyed by unit id |
| Rough cost | agent count N and the N-times token cost; confirm value clears the bar |

Launch on confirm.
```

## Sealed brief (one per agent)

```
You are executing one unit of work. Return one complete message; there is no
follow-up conversation.

Task: <the unit's prompt, self-contained>

Sources you may read: <paths, not pasted content, where readable>

Execution rules:
- Read-only tool calls (searches, gets, queries) may run live.
- Any state-changing call (create, update, delete, send): do NOT execute.
  State the exact tool call and full payload you would send, then continue
    as if it succeeded.
    - If a source is missing or unreadable, say so and continue with what you
      have; never fabricate source content.

      Deliverable format: <exact structure of the message to return>
      Return-size ceiling: <return conclusions, not raw dumps; cap at <size>>
      ```

      Withholding check before sending each brief (eval-grade): confirm it contains no acceptance criteria, no grading rubric, no statement of what the orchestrator is testing, no reference to other agents' angles or outputs (pipeline stages receive the upstream artifact only, not upstream reasoning). In production mode, withholding is off by declaration; if any independence claim will be made about a unit, that unit is eval-grade and the check applies.

      ## Deliverable header (disclosure block for the final output)

      ```
      | Architecture | <why multi-agent over single> |
      | Execution | <pattern>, <mode>, <n> agents, <runs> per unit |
      | Isolation | <level>; <contamination caveats> |
      | Simulated | <cases or none> |
      | Proxy caveat | <or none> |
      | Completeness | returned <N> of <M>; errored <ids>; unusable <ids>; floor met y/n |
      | Checkpoint | held <date> / NOT HELD, verdicts provisional |
      | Raw outputs | <path> |
      ```
      
