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

## What this skill does

Most days do not fail at the list. They fail at the commit and at the refusal. You already know
roughly what matters; what breaks the day is that the list stays soft, so a request arriving at
midday looks as important as the thing you chose that morning and wins because it is louder and
newer. Signal Three replaces the soft list with a hard set of three, a budget that protects them,
and a scoring pass that will not let you pretend.

Lineage, stated plainly. The signal-versus-noise framing and the exactly-three constraint follow the
three-things rule Kevin O'Leary has described publicly, which he credits to Steve Jobs's focus
discipline. The rest is not his: the 70/30 budget, the explicit displacement swap, the unverified
state that holds a day pending, and the streak rules below.

**The set is three.** Not three plus a small fourth. The moment there is a fourth, there is no
signal, only a ranked list, and a ranked list is what you had before.

**The budget is 70/30.** At least 70% of the day's real working effort goes to the three. Everything
else shares the remaining 30%, which is a ceiling and not an allowance to spend.

State lives in one small file you keep, `signal-state.md`: today's three, today's status, the streak.

## COMMIT (morning)

Pick exactly three. Pressure test each one before it enters the set.

**Walkable today.** Can this be finished today, by you, with what you have? "Ship the new pricing" is
not walkable. "Send the pricing change to the two accounts that asked" is. If an item is not walkable,
the walkable slice of it is the item.

**Load-bearing.** Does something else depend on this, or does it only feel productive? An item that
unblocks a person, a deadline, or a decision is load-bearing. One that only makes you feel current is
not.

**Carries dread.** Which are you quietly hoping to postpone? The dread item is usually the real one.
If none of the three carry dread, you have picked a comfortable day; say so before committing.

**Not gameable.** If "done" can be claimed tonight without anything changing in the world, the item
is gameable. Rewrite it until finishing produces an artifact, a sent thing, a decision, or a state
change someone else could verify.

Each item gets a done-condition written beside it at commit time, never invented at close. Rewriting
the condition in the evening is how an honest streak becomes a decorative one.

## OFF (declared rest)

A rest day is legitimate and costs nothing, **as long as it is declared in advance**.

Declaring OFF writes a rest day into `signal-state.md` and skips it: the streak neither advances nor
resets. A day with no commit and no declaration is not a rest day, it is a miss, and it resets the
streak to zero. Deciding in the morning that you are not working is a decision. Discovering at night
that you did not is a result. Declare once, for that day only, never retroactively.

## CHECK (midday)

Something arrived. Run it against the three.

**The default answer is noise.** The burden of proof sits on the incoming thing, not on your
commitment. Ask, in order:

1. Does it advance one of the three? If yes, it is not an interruption, it is the work.
2. Is it a real fire, meaning something breaks irreversibly today if it waits? Fires are rare and
   usually involve a hard external deadline, a customer already harmed, or money leaving.
3. Anything else is noise. It goes to your task system, or spends from the 30% if it is truly small.

**Displacement must be explicit.** A real fire does not get added. It swaps. Name which of the three
drops, mark it displaced in the state file, carry it forward as tomorrow's strong candidate. The set
stays at three. This prevents the quiet growth from three to five to a list, which is how every
version of this practice dies. Say the trade out loud: what came in, what went out, the cost.

## CLOSE (evening)

Score the three against the done-conditions written at commit. Three outcomes per item: **done**,
**not done**, **unverified**. Unverified means you believe it is finished but the confirming thing
has not happened: the reply has not landed, the run has not completed, nobody signed off.

**Unverified leaves the day pending.** The day does not score and the streak does not advance until
you confirm. Not partial credit, not a rounding-up. This is what makes the metric un-gameable, since
the easiest way to fake a streak is to declare soft wins at night when nobody will check.

- All three done and verified: streak advances by one.
- Any item not done: reset to zero. Not a partial day.
- Any item unverified: pending, streak unchanged until you confirm or fail it.
- Declared OFF: skipped, streak unchanged. No commit and no declaration: reset to zero.

Then a two-sentence correction: what ate the day, and one change to tomorrow's commit.

## Output format

```
COMMIT
  1. <item>  | done-condition: <what verifiably changes>
  2. <item>  | done-condition: <...>
  3. <item>  | done-condition: <...>
  DREAD ITEM: <which one, or: none, and that is a flag>
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
  INCOMING: <the request in one line>
  ADVANCES A COMMITTED ITEM? <yes/no, which>
  REAL FIRE? <yes/no, what breaks today if it waits>
  VERDICT: signal | noise | fire
  IF FIRE -> SWAP: in <new>, out <which of the three drops>
  COST: <what the swap costs>
```

```
CLOSE
  1. <item> -> done | not done | unverified <reason>
  2. ...
  3. ...
  DAY: complete | missed | pending <what confirmation is outstanding>
  STREAK: <n> -> <n+1 | 0 | unchanged>
  CORRECTION: <what ate the day, one change for tomorrow>
```

## Worked example (invented)

A small hardware team preparing a firmware release for outside certification.

```
COMMIT
  1. Send the EMC test paperwork to the certification lab
     | done-condition: submission confirmation in hand
  2. Fix the battery-drain regression from the sleep-state change
     | done-condition: overnight drain under spec on two units
  3. Get a firm ship date from the connector supplier
     | done-condition: a date in writing, not "soon"
  DREAD ITEM: #1. Unglamorous, and it blocks everything downstream.
  STREAK: 6

CHECK
  INCOMING: a distributor asks for a custom firmware build for a demo next month.
  ADVANCES A COMMITTED ITEM? No.  REAL FIRE? No, the demo is weeks out.
  VERDICT: noise
  COST: none today. Filed to the task system as a candidate for a later commit.

CHECK
  INCOMING: the lab will not accept the submission without a revised test plan.
  ADVANCES A COMMITTED ITEM? Yes, item 1. Not an interruption, the work.
  VERDICT: signal

CLOSE
  1. EMC paperwork -> done (confirmed after the revised plan went back)
  2. Battery-drain regression -> unverified (fix is in, overnight run finishes tomorrow)
  3. Connector ship date -> done (date in writing)
  DAY: pending, waiting on the overnight drain result
  STREAK: 6 -> unchanged until item 2 is confirmed
  CORRECTION: item 2 was never walkable; an overnight test cannot finish inside a day.
  Tomorrow it becomes "read the drain result and decide ship or hold."
```

Notice what CLOSE does not do. It does not call item 2 done because the fix looked right, and it does
not round two out of three up to a win.

## Boundaries

Signal Three picks, defends, and scores. It does not store tasks, run a calendar, plan a week, or
decide your goals; it selects from what your task system holds and your daily brief surfaced. It will
not tell you two out of three is fine, and it will not advance a streak on your say-so. Set your own
morning, midday, and evening times: the modes are anchored to the shape of a day, not to a clock.
