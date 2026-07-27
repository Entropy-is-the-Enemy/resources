---
name: scales
description: >
  Pressure-test or shape a strategy, plan, or deliverable by routing it through a fixed set of
  commodity mental-model laws, firing only the two to four whose signature actually appears in the
  input, naming the ones it withheld, and certifying each against what the original claim covered.
  Trigger on "run the scales on this," "pressure-test this plan," "what am I missing," "stress this
  strategy," "which mental models apply," or "poke holes in this before I send it." Returns
  fired laws with one move each, withheld laws with the missing feature, active guardrails, the
  residual no law covers, and one verdict on what changes, which is allowed to be nothing. Does
  NOT verify facts, check arithmetic, edit prose, or decide, and never takes a person as its
  object.
---

# Scales

## What this skill does

Scales holds eleven public-domain laws, each a detector with a trigger condition. A law fires only
when the input contains the concrete feature its mechanism is about. No feature, no fire, and the
output names what it withheld.

**Cap at four fired laws. Floor at two.** Below two, say the input is too thin and stop.

## Two uses, one selection rule

**Review.** The thing exists and you are reading it back to whoever built it.

**Design.** The approach is undecided, and the detectors run as constraints on what gets built.
Quote features of the approach as stated so far; a law fires against a choice being considered
rather than one already made. Goodhart, Chesterton's fence, and Brooks's law are cheaper here
than after the fact.

Declare the use on the first line of the output. It never changes which laws fire: selection stays
on quoted features alone. A design run with nothing quotable is the too-thin stop.

## Routing by signature

1. **Extract the signature set.** Concrete features only: dates, numbers with targets attached, rules
   proposed for removal, single dependencies, claims about why someone acted. Quote each. A feature
   you cannot quote is one you inferred.
2. **Match features to laws.** One feature may fire several. No matching feature, no fire.
3. **Rank by consequence, cut to four.** Keep readings that change what someone does next, drop the
   true but inert. Anything cut enters the withheld list, marked capped.
4. **Bound-check each survivor** before writing its reading.

## The eleven laws

Each gives the **signature** that fires it, the **mechanism**, and the **bound**: what the original
claim covered.

**Planning fallacy.** Signature: a date the doers estimated. Mechanism: inside-view estimates omit
known failure paths. Bound: your own future work, not estimates anchored on past comparables.

**Goodhart's law.** Signature: a target-bearing metric the measured party controls. Mechanism: the
proxy stops tracking what it proxied for. Bound: needs proxy, control, and slack together. A measure
that is the outcome cannot corrupt. Note this is the generalized form in common use; the 1975 original
was narrower, about a statistical regularity collapsing once it is used for control.

**Hick-Hyman law.** Signature: many simple options shown at once to someone choosing fast. Mechanism:
decision time rises with the log of the count. Bound: equal-weight, mutually exclusive, hurried
choices, not deliberate high-stakes ones, not sorted or defaulted lists.

**Chesterton's fence.** Signature: a rule proposed for removal with no account of why it exists.
Mechanism: the cost a rule prevents is invisible because the rule prevents it. Bound: find the reason;
once found and obsolete, the fence says remove it. Not a status-quo presumption.

**Hanlon's razor.** Signature: an explanation of behavior that assumes intent. Mechanism: constraint
and missing information explain more than malice. Bound: a prior where nobody gains from the outcome,
never evidence, and suspended by the guardrail below.

**Second-order effects.** Signature: an intervention aimed at an actor who can respond. Mechanism:
responses often swamp the change. Bound: name the actor and the channel, or you are writing
speculative cascades. An irreversible step in the input holds a slot for this law against a
higher-consequence one.

**Base rates.** Signature: a forecast about a case in a class with a track record. Mechanism:
frequency beats narrative detail. Bound: the class must match on outcome-relevant features; a
mismatched class is worse than none.

**Concentration risk.** Signature: one dependency holding an outsized share of an exposure.
Mechanism: independent-looking exposures fail together. Bound: substitutable exposures only, and it
flags fragility, not error. Never people.

**Brooks's law.** Signature: capacity added to an effort already behind. Mechanism: ramp-up and
coordination cost land before the added throughput does, so the near date slips further. Bound:
partitionable work with little handoff between the parts is exempt, and this is a claim about
timing, not an argument against adding capacity.

**Dunning-Kruger effect.** Signature: an actor rating their own readiness for territory they have
not worked in. Mechanism: judging the competence takes the same skill as having it. Bound:
calibration, never intelligence, and it needs genuine unfamiliarity rather than mere confidence. It
fires on the readiness claim, not on whoever made it, and the move is always an external check.

**Occam's razor.** Signature: two or more explanations offered for the same evidence. Mechanism:
each unsupported assumption is one more way to be wrong. Bound: a tie-breaker between explanations
that fit equally well, not a test of truth, and it goes quiet once evidence separates them.

## The bound check

Every fired law carries one line in the output:

> Stays inside the original claim because [the condition it requires] is present as [quoted feature].

If you cannot write it without hedging, the law does not fire. Move it to withheld, reason "bound
not satisfied."

Where a reading leans on anything you did not quote from the input,
mark that inline as "(assumes X; check: Y)" rather than asserting it. If the input says the
assumption no longer holds, re-derive the reading instead of running on the stale premise.

## Guardrails

- **Adversarial-interest suspension.** If any party gains from the confusion, delay, or failure in
  the input, Hanlon's razor is suspended for the run and marked suspended.
- **Persons clause.** Concentration risk and Goodhart never take a person or a relationship as their
  object, and a readiness reading addresses the claim, not the claimant.
- **Absent-feature suppression.** A law never fires because the input resembles a domain where it
  is usually relevant; it fires on the quoted feature or not at all.

## Output format

```
MODE: review | design

SIGNATURE SET
  "<quoted feature>"  ->  <law(s) matched>

FIRED (2 to 4)
  LAW
    Reading: <what it says about this specific input> (assumes <unquoted premise>;
      check: <what would settle it>)
    Bound check: stays inside the original claim because <condition> is present as <feature>
    Move: <the one concrete change this implies>

WITHHELD
  LAW: <the feature that would have fired it, and that it is absent>
  LAW: capped or bound not satisfied, <which condition fails, what displaced it>

GUARDRAILS ACTIVE
  <rule>: <the input feature that switched it on>

RESIDUAL
  <the risk none of the laws addresses>

VERDICT
  <one consolidated statement of what to do differently, as concrete changes, or
   "no change" plus the one thing to watch>
```

The residual line is mandatory. The verdict is one statement of what the reader now does
differently, written as changes, not a summary of which laws matched. If the fired readings
change no decision, say exactly that: no change, the plan holds as written, and the one thing to
watch. Manufacturing a move to fill the slot is the failure. Too thin means you could not analyze
the input; no change means you did and it held.

## Worked example (invented)

**Input:** an evening on-demand shuttle on one dispatch vendor, with driver bonuses tied to on-time
percentage.

```
MODE: review

SIGNATURE SET
  "bonus tied to on-time percentage"      ->  Goodhart
  "single dispatch vendor"                ->  concentration risk

FIRED (2)
  GOODHART'S LAW
    Reading: drivers control acceptance, so the number rises fastest by declining the long
      pickups the shuttle exists to run. (Assumes drivers see trip length before accepting;
      check the dispatch screen.)
    Bound check: proxy, control, and slack are all present in the bonus design.
    Move: add a completion-rate floor on requested trips, or bonus the crew, not drivers.

  CONCENTRATION RISK
    Reading: a vendor outage is a total outage during the only hours this runs.
    Bound check: dispatch software is a substitutable exposure, not a person.
    Move: write the two-hour-outage procedure: manual dispatch or suspend, decided now.

WITHHELD
  Planning fallacy: no date estimated. Base rates: no forecast. Hanlon's razor: no
  attribution of intent. Hick-Hyman: riders face two service types. Brooks's law: no
  capacity added. Chesterton's fence: no rule proposed for removal. Dunning-Kruger: no
  readiness claim. Occam's razor: one explanation offered, not two. Second-order effects:
  driver response sits inside the Goodhart reading.

GUARDRAILS ACTIVE
  Persons clause: concentration applied to the vendor, not to the dispatchers.

RESIDUAL
  Nothing above asks whether evening demand exists.

VERDICT
  Two changes before launch: a completion floor on the bonus and a written two-hour-outage
  procedure. The schedule is unaffected.
```

## Boundaries

Scales routes and reads. It does not check arithmetic, verify claims, edit voice, or decide. It will
not invent a second signature to clear the floor, exceed four to look thorough, or invent a change
to fill a verdict that should read "no change." If the input is a person or a relationship rather
than a plan, the correct output is that this is the wrong instrument.
