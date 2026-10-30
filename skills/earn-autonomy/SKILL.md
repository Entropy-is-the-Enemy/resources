---
name: earn-autonomy
description: >
  Decide with logged evidence, not gut feel or the calendar, whether an AI agent may make one specific
  judgment call alone (routing, assignment, triage, prioritizing). The agent proposes, a human decides,
  both are recorded side by side, every disagreement becomes a written rule, and autonomy is granted
  only by an explicit human ruling at a pre-committed review point, class by class.
  Trigger on "can the agent just do this on its own", "should we let it auto-assign", "stop making me
  approve every one", "is it ready to run unsupervised", or when setting up a new agent that routes or
  assigns work. Does NOT cover model training, offline evaluation datasets, permissions or access
  control setup, or tasks where a wrong action is irreversible and costly (keep those human).
---

# Earn Autonomy

## What this skill does

An agent that routes or assigns work is usually given autonomy in one of two bad ways: someone decides it "seems fine" after a few weeks, or it never gets autonomy because nobody can say what "good enough" means. This skill replaces both with a record.

Until a call is graduated, the agent proposes and a human decides. Every proposal and every decision goes into a log. Every disagreement is treated as a question, and the human's answer becomes a rule the agent applies next time. At a review point you set in advance, you measure agreement against a bar you set in advance, and the human rules. Autonomy can be granted for some item classes and withheld for others, and it can be taken back.

## When this applies

- One named decision: "which of four vets gets this appointment request", "which queue gets this ticket", "which lead goes to which rep".
- The decision repeats often enough to collect a sample (dozens of items over weeks, not three a year).
- A human currently makes the call and can say why.

If you cannot name the single decision, stop and narrow it first. "Run the front desk" is not one decision.

## Configure before you start

Write these down in the log file header before the first item. Do not change them after you see results.

1. **The decision**, in one sentence.
2. **The review point**: how many items before you compute agreement. About 20 is a workable default.
3. **The agreement threshold**: for example, 90 percent overall and no class below 80 percent.
4. **Which item classes count**, and how you will label them (new client, existing client, urgent, no signal, and so on). State which items are excluded and why.
5. **Where the log lives**: an internal file or table, not a team channel.

Pre-committing is the point. A bar written after seeing the number will drift to fit the number.

## The shadow log

One row per item. A CSV or a table works:

```
date,item_id,class,agent_pick,signals_used,human_pick,match,human_reason,rule_version
2026-03-02,REQ-0141,existing,Vet B,"saw pet 2025-11, dental",Vet B,yes,,r1
2026-03-02,REQ-0142,existing,Vet A,"owner field = Vet A",Vet C,no,"owner field set in bulk import, Vet C sees this pet",r1
```

- `signals_used` is what the agent actually relied on, so you can see when a signal misleads.
- `human_reason` is required whenever `match` is no.
- `rule_version` is the rule set in force when the agent proposed. Bump it every time a rule changes.

## How it works

1. **Propose in a fixed format.** Every proposal uses the same shape so the human can approve in one glance:
   `REQ-0143 | existing client | Proposed: Vet B | Because: saw this pet within 6 months for same issue | Approve / Change to ___`
   While in shadow, the agent never acts on an item before the human rules. No reply means no decision, not approval.
2. **Log both picks.** Record the agent's pick, the signals, and the human's pick, then mark the match.
3. **Ask on every mismatch.** A mismatch is a question, not a score. Ask the human why, in one line, and record the answer.
4. **Turn the answer into a rule.** Write it so the agent can apply it next time, then bump `rule_version`. Reasons usually take one of these shapes:
   - **Recency window**: a relationship older than N months is not a relationship.
   - **Scope-specific claims**: owning one kind of work gives no claim on a different kind.
   - **Balance when no signal is live**: lean toward whoever needs the work, keep everyone in the mix.
   - **Artifact signals**: a field that looks strong but is not, such as an owner field set by a bulk assignment on one date, which says nothing about the actual relationship.
   - **Already handled**: check whether the item is being handled somewhere (a recent digest or log naming who is on it) before proposing.
5. **Report agreement two ways.** Overall, and since the latest rule change. Old mismatches made under old rules overstate the current gap.
6. **At the review point:** compute agreement, split it by item class, and cluster mismatches by reason. Bring the human three things: the numbers against the pre-committed bar, the per-class split, and the open reason clusters.
7. **The human rules, explicitly.** Passing the threshold does not grant autonomy by itself. The human may keep the agent review-first past the threshold. Record the ruling and its reason in the log, whichever way it goes.
8. **Grant by class.** The agent acts alone on classes where it agrees reliably and keeps proposing on ambiguous classes: no signal, conflicting signals, likely but unconfirmed identity matches.
9. **Keep sampling after graduation.** Log a share of autonomous decisions (for example 1 in 10) for spot review so drift shows up. Any reversal by the human drops that class back to proposing, and the count restarts for that class.

## Rules

- One decision per log. Do not pool different calls into one agreement number.
- Thresholds, review point, and class definitions are fixed before the first item.
- Count only agent-vs-human agreement. Never count the agent agreeing with itself, a rerun, or a second model.
- Silence is not approval. An unanswered proposal stays open.
- The agent never acts on a shadow item before the human rules.
- Every mismatch gets a recorded reason. A mismatch with no reason is unfinished work, not data.
- Sensitive details (client names, health or account details) stay in the internal log, never in public or team channels. Proposals posted to a shared channel use item IDs.
- Autonomy is per class and revocable. One reversal sends that class back to proposing.

**Anti-patterns to refuse:**
- Granting autonomy because "it's been a few weeks."
- Moving the threshold after seeing the number.
- Treating a quiet approver as agreement.
- Reporting only the overall number when one class is dragging or carrying it.

## Example

**Setup.** A veterinary practice group with four vets wants an agent to assign incoming appointment requests without the practice manager checking each one. Pre-committed: review at 40 items (above the 20 default, so each class gets a real sample); a class graduates at 90 percent agreement on at least 10 items in that class. Classes: existing client, new client.

**Shadow period.** The agent proposes each assignment in the fixed format; the manager approves or changes it. Three mismatches arrive in the first 12 items:
- Agent picked Vet A because the client record's owner field said Vet A. Manager picked Vet C: "That field was set in one bulk import. Vet C has seen this dog four times." New rule (r2): ignore owner fields whose timestamp matches a bulk-import date; use visit history.
- Agent picked Vet B, who saw the cat two years ago. Manager picked Vet D: "Two years is not a relationship." New rule (r3): visits older than 12 months do not count.
- Agent picked Vet B for a surgery follow-up because Vet B handles the pet's dental care. Manager picked the surgeon: "Dental gives no claim on surgery." New rule (r4): claims are scoped to the type of work.

**Review at 40 items.**
```
Overall:          33/40 = 82%
Since r4:         17/18 = 94%
Existing client:  27/30 = 90%   (passes)
New client:        6/10 = 60%   (fails)
Mismatch reasons: bulk-import field (1), stale visit (1),
                  scope (1), load balance on new clients (4)
```

**Ruling.** Only existing clients clear the pre-committed bar. The manager rules, with the reason logged: the agent assigns existing-client requests alone; new-client requests stay propose-first, and a balance rule (r5: with no live signal, offer the vet with the lightest booked week, rotating ties) is written from the four load-balance mismatches. One in ten autonomous assignments is logged for spot review. Two weeks later the manager reverses one existing-client assignment, and that class drops back to proposing until it clears the bar again.
