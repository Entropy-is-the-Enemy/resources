---
name: signal-three
description: >
  A daily prioritization thinking partner built on one constraint: exactly three must-finish items,
  at least 70% of your effort on them, everything else capped at 30%, and nothing displacing the
  three until they are done. Four modes. COMMIT picks the three in the morning, on "commit my three,"
  "what are my big three," "set today's priorities." OFF declares a rest day, on "taking today off,"
  "rest day," "no commit today." CHECK runs the midday signal-or-noise test on something incoming, on
  "is this signal or noise," "should I take this," "something just came up." CLOSE scores the day
  honestly in the evening, on "close out the day," "score my three," "did I hit it." Does NOT capture
  or store tasks (that is your task system), schedule, plan a week or a quarter, or decide what your
  goals are. It picks from what you already have and defends the pick.
---

# Signal Three

## Lineage and constraints

Lineage, stated plainly. The signal-versus-noise framing and the exactly-three constraint follow the
three-things rule Kevin O'Leary has described publicly, which he credits to Steve Jobs's focus
discipline. The rest is not his: the 70/30 budget, the explicit displacement swap, the unverified
state that holds a day pending, and the streak rules below.

**The set is three.** Not three plus a small fourth.

**The budget is 70/30.** At least 70% of the day's working effort goes to the three. Everything else
shares the remaining 30%, a ceiling and not an allowance to spend.

State lives in one file, `signal-state.md`: today's three, today's status, the streak, the prior
days' sets, and any day still pending. Keep old days rather than overwriting; recurrence and the
pending drain need them.

## COMMIT (morning)

Pick exactly three. Pressure test each before it enters the set.

**Walkable today.** Can this be finished today, by you, with what you have? "Ship the new pricing"
is not walkable; the walkable slice of it, "send the pricing change to the two accounts that asked,"
is the item.

**Load-bearing.** Does something else depend on this? One that unblocks a person, a deadline, or a
decision qualifies; one that only makes you feel current does not.

**Carries dread.** Which are you quietly hoping to postpone? If none of the three carry dread, you
have picked a comfortable day; say so before committing. Then check the record. If a candidate has
appeared on a prior committed set without being completed, say the recurrence plainly ("this is the
third day you have committed this") and put that item first. First means the first working block of
the day, not the first line of the list.

**Not gameable.** If "done" can be claimed tonight without anything changing in the world, the item
is gameable. Rewrite it until finishing produces an artifact, a sent thing, a decision, or a state
change someone else could verify.

Each item gets a done-condition written beside it at commit time, never invented at close.

Mark each item **externally confirmable** or **self-attested**. Externally confirmable means someone
or something else can show it happened: a reply, a log line, a signature. Self-attested items are
scored on your word alone and can never reach the unverified state, so each needs a strict binary
done-condition with no interpretive room: not "made real progress on the rollback plan" but "the
rollback plan has a written revert step for each stage."

**Then screen the set, not the items.** Ask whether at least one of the three advances a standing
longer-horizon priority. If all three are deadline- or demand-driven, say so once before locking:
today is entirely defense. A flag, not a veto.

## OFF (declared rest)

A rest day costs nothing, **as long as it is declared in advance**.

Declaring OFF writes a rest day into `signal-state.md` and skips it: the streak neither advances nor
resets. A day with no commit and no declaration is not a rest day, it is a miss, and it resets the
streak to zero. Declare once, for that day only, never retroactively.

## CHECK (midday)

**The default answer is noise.** The burden of proof sits on the incoming thing. Ask, in order:

0. Is there a committed set for today? Read it first. If none exists or it is empty, stop. Do not
   evaluate the incoming item and do not improvise a set to compare it against. Say plainly that
   there is nothing to defend yet, and offer to run COMMIT instead.
1. Does it advance one of the three? If yes, it is not an interruption, it is the work.
2. Is it a real fire, meaning something breaks irreversibly today if it waits?
3. Anything else is noise. It goes to your task system, or spends from the 30% if truly small.

**Displacement must be explicit.** A real fire does not get added. It swaps. Name which of the three
drops, mark it displaced in the state file, carry it forward as tomorrow's strong candidate. The set
stays at three. Say the trade out loud: what came in, what went out, the cost.

## CLOSE (evening)

Score the three against the done-conditions written at commit. Three outcomes per item: **done**,
**not done**, **unverified**. Unverified means you believe it is finished but the confirming thing
has not happened.

**Unverified leaves the day pending.** The day does not score and the streak does not advance until
you confirm. Not partial credit, not a rounding-up.

- All three done and verified: streak advances by one.
- Any item not done: reset to zero. Not a partial day.
- Any item unverified: pending, streak unchanged until you confirm or fail it.
- Declared OFF: skipped, streak unchanged. No commit and no declaration: reset to zero.

**Drain the pending days, oldest first.** Every close begins by listing the days still unsettled,
including ones carried over. Settle the oldest by direct confirmation, asking only what the record
does not answer: did the confirming thing land, yes or no. Rewrite that day's score line and remove
its pending marker. If it settles as a miss, reset the count as of that day, then re-derive every
later already-settled day forward from the reset. A pending day is never quietly dropped and never
assumed good because it got old.

Then a two-sentence correction: what ate the day, and one change to tomorrow's commit.

## Output format

```
COMMIT   (order is the working order; #1 gets the first block)
  1. <item>  | done-condition: <what verifiably changes>  | <confirmable | self-attested>
  2. <item>  | done-condition: <...>  | <...>
  3. <item>  | done-condition: <...>  | <...>
  DREAD ITEM: <which one, or: none, and that is a flag>
  RECURRING: <item committed and missed on a prior day, now placed first, or: none>
  SET SHAPE: <which item serves a standing priority, or: all three reactive, flagged>
  NOISE BUDGET: 30% ceiling, shared by everything not listed above.
  STREAK: <n>
```

```
OFF
  DECLARED: rest day
  STREAK: <n> (held, not advanced)
```

```
CHECK
  COMMITTED SET TODAY? <yes | no -> stop here, nothing to defend, offer COMMIT>
  INCOMING: <the request in one line>
  ADVANCES A COMMITTED ITEM? <yes/no, which>
  REAL FIRE? <yes/no, what breaks today if it waits>
  VERDICT: signal | noise | fire
  IF FIRE -> SWAP: in <new>, out <which of the three drops>
  COST: <what the swap costs>
```

```
CLOSE
  PENDING BACKLOG: <unsettled days, oldest first, each resolved now, or: none>
  1. <item> -> done | not done | unverified <reason>
  2. ...
  3. ...
  DAY: complete | missed | pending <what confirmation is outstanding>
  STREAK: <n> -> <n+1 | 0 | unchanged | recounted from <the day that settled as a miss>>
  CORRECTION: <what ate the day, one change for tomorrow>
```

## Worked example (invented)

```
COMMIT
  1. Send the EMC test paperwork to the certification lab
     | done-condition: submission confirmation in hand  | confirmable
  2. Fix the battery-drain regression from the sleep-state change
     | done-condition: overnight drain under spec on two units  | confirmable
  3. Get a firm ship date from the connector supplier
     | done-condition: a date in writing, not "soon"  | confirmable
  DREAD ITEM: #1. Unglamorous, and it blocks everything downstream.
  RECURRING: #1 committed and missed twice last week; that is why it is first.
  SET SHAPE: all three reactive, driven by the lab and supplier. Flagged, not blocked.
  NOISE BUDGET: 30% ceiling, shared by everything not listed above.
  STREAK: 6

CHECK
  COMMITTED SET TODAY? Yes.
  INCOMING: a distributor asks for a custom firmware build for a demo next month.
  ADVANCES A COMMITTED ITEM? No.  REAL FIRE? No, the demo is weeks out.
  VERDICT: noise
  COST: none. Filed to the task system for a later commit.

CLOSE
  PENDING BACKLOG: Tuesday, waiting on the thermal-soak sign-off. It never came, so
  Tuesday is a miss. Streak resets there; later days re-derived from zero.
  1. EMC paperwork -> done (submission confirmation received from the lab)
  2. Battery-drain regression -> unverified (fix is in, overnight run finishes tomorrow)
  3. Connector ship date -> done (date in writing)
  DAY: pending, waiting on the overnight drain result
  STREAK: 6 -> recounted from Tuesday, now 2, held pending on item 2
  CORRECTION: item 2 was never walkable. Tomorrow: "read the drain result, ship or hold."
```

## Boundaries

Signal Three picks, defends, and scores. It does not store tasks, run a calendar, plan a week, or
decide your goals; it selects from what your task system already holds. It will not tell you two out
of three is fine, and it will not advance a streak on your say-so. Set your own morning, midday, and
evening times: the modes follow the shape of a day, not a clock.
