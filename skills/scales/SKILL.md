---
name: scales
description: >
  Pressure-test or shape a strategy, plan, or deliverable by routing it through a fixed set of
  commodity mental-model laws, firing only the two to four whose signature actually appears in the
  input, naming the ones it withheld, and certifying each against what the original claim covered.
  Trigger on "run the scales on this," "pressure-test this plan," "what am I missing," "stress this
  strategy," "which mental models apply," or "poke holes in this before I send it." Returns
  fired laws with one move each, withheld laws with the missing feature, active guardrails, and the
  residual no law covers. Does NOT verify facts, check arithmetic, edit prose, or decide, and never
  takes a person as its object.
---

# Scales

## What this skill does

Run the same ten mental models across two unrelated plans and you get the same ten paragraphs. That
sameness is the tell: nothing was selected, so nothing was thought.

Scales holds eight public-domain laws and treats each as a detector with a trigger condition. A law
fires only when the input contains the concrete feature its mechanism is about. A deadline fires the
planning-fallacy law. A number someone is paid on fires the proxy-corruption law. No deadline, no
planning fallacy, and the output says so, because a report of what did not fire is falsifiable and a
report of hits alone is not. The models are commodity. The routing is the product.

**Cap at four fired laws. Floor at two.** Below two, say the input is too thin and stop. Above four
you are pattern-matching: eight readings at once is not eight times the insight, it is a reader who
acts on none.

## Routing by signature

The question is never "does this feel relevant," but "is the feature present, and can you quote it."

1. **Extract the signature set.** Concrete features only: dates, numbers with targets attached, rules
   proposed for removal, single dependencies, claims about why someone acted. Quote each. A feature
   you cannot quote is one you inferred, and inference is how a checklist pass returns.
2. **Match features to laws.** One feature may fire several. No matching feature, no fire.
3. **Rank by consequence, cut to four.** Keep readings that change what someone does next, drop the
   true but inert. Anything cut enters the withheld list, marked capped.
4. **Bound-check each survivor** before writing its reading.

## The eight laws

Each gives the **signature** that fires it, the **mechanism**, and the **bound**: what the original
claim actually covered. The bound is the load-bearing part.

**Planning fallacy.** Signature: a date the doers estimated. Mechanism: inside-view estimates omit
known failure paths. Bound: your own future work, not estimates anchored on past comparables.

**Goodhart's law.** Signature: a target-bearing metric the measured party controls. Mechanism: the
proxy stops tracking what it proxied for. Bound: needs proxy, control, and slack together. A measure
that is the outcome cannot corrupt.

**Hick's law.** Signature: many simple options shown at once to someone choosing fast. Mechanism:
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
speculative cascades, which read as sophistication and predict nothing. An irreversible step in the
input holds a slot for this law against a higher-consequence one.

**Base rates.** Signature: a forecast about a case in a class with a track record. Mechanism:
frequency beats narrative detail. Bound: the class must match on outcome-relevant features, since a
mismatched class carries false precision and is worse than none.

**Concentration risk.** Signature: one dependency holding an outsized share of an exposure.
Mechanism: independent-looking exposures fail together. Bound: substitutable exposures only, and
concentration is often the strategy, so this flags fragility, not error. Never people.

## The bound check

Overextension is the most common failure in mental-model work, and invisible without a forcing
function. So every fired law carries one line in the output:

> Stays inside the original claim because [the condition it requires] is present as [quoted feature].

If you cannot write it without hedging, the law does not fire. Move it to withheld, reason "bound
not satisfied." This is what stops Hick's law from becoming "simplify everything."

## Guardrails that key off the input

Guardrails trigger on features, never on domain labels, which is what protects an input whose
subject you have never seen.

- **Adversarial-interest suspension.** If any party gains from the confusion, delay, or failure in
  the input, Hanlon's razor is suspended for the run and marked suspended. The charitable prior is a
  cooperative assumption that stops holding once someone plays a different game.
- **Persons clause.** Concentration risk and Goodhart never take a person or a relationship as their
  object. Pointed at people, exposure tools give fluent, corrosive advice.
- **Absent-feature suppression.** A law never fires because the input resembles a domain where it is
  usually relevant. It fires on the quoted feature or not at all.

## Output format

```
SIGNATURE SET
  "<quoted feature>"  ->  <law(s) matched>

FIRED (2 to 4)
  LAW
    Reading: <what it says about this specific input>
    Bound check: stays inside the original claim because <condition> is present as <feature>
    Move: <the one concrete change this implies>

WITHHELD
  LAW: <the feature that would have fired it, and that it is absent>
  LAW: capped or bound not satisfied, <which condition fails, what displaced it>

GUARDRAILS ACTIVE
  <rule>: <the input feature that switched it on>

RESIDUAL
  <the risk none of the eight laws addresses>
```

The residual line is mandatory: a report with nothing left over is claiming eight laws exhaust the
problem.

## Worked example (invented)

**Input:** a transit agency's plan for an evening on-demand shuttle on one dispatch vendor, with
driver bonuses tied to on-time percentage, and a proposal to delete the rule requiring two
dispatchers after 9pm.

```
SIGNATURE SET
  "bonus tied to on-time percentage"      ->  Goodhart
  "delete the two-dispatcher rule"        ->  Chesterton's fence
  "single dispatch vendor"                ->  concentration risk

FIRED (3)
  GOODHART'S LAW
    Reading: drivers control acceptance, so the number rises fastest by declining the long
      pickups the shuttle exists to run.
    Bound check: proxy, control, and slack are all present in the bonus design.
    Move: add a completion-rate floor on requested trips, or bonus the crew, not drivers.

  CHESTERTON'S FENCE
    Reading: no origin given. If it followed a night when one dispatcher could not work a
      radio and call for help at once, evening service recreates that.
    Bound check: the origin is genuinely unstated, the only case the fence covers.
    Move: one call to whoever wrote it. If the reason is obsolete, delete it, and say why.

  CONCENTRATION RISK
    Reading: a vendor outage is a total outage during the only hours this runs, and no loss
      case is written anywhere.
    Bound check: dispatch software is a substitutable exposure, not a person.
    Move: write the two-hour-outage procedure: manual dispatch or suspend, decided now.

WITHHELD
  Planning fallacy: no date or duration estimated. Base rates: no forecast.
  Hanlon's razor: no attribution of intent. Hick's law: riders face two service types.
  Second-order effects: driver response already sits inside the Goodhart reading.

GUARDRAILS ACTIVE
  Persons clause: concentration applied to the vendor, not to the dispatchers themselves.

RESIDUAL
  Nothing above asks whether evening demand exists. Every fired law assumes the service is
  worth running.
```

The withheld list is the honest part: it shows which detectors ran and found nothing.

## Boundaries

Scales routes and reads. It does not check arithmetic, verify claims, edit voice, or decide. It will
not invent a second signature to clear the floor, or exceed four to look thorough. If the input is a
person or a relationship rather than a plan, the correct output is that this is the wrong
instrument.
