---
name: post-session-qualify
description: >
  Grade a lead after a free session, workshop, audit, or intro call using what the person actually did
  rather than what they told an intake form, then route them with an explicit scoring formula that is
  held as an unvalidated hypothesis until enough real outcomes exist to calibrate it. Also specifies
  the single-property firewall that keeps two unrelated funnels from leaking into each other inside one
  shared CRM. Trigger on "grade this lead," "was that a real buyer," "who should I follow up with,"
  "score the people from the workshop," "set up my qualification fields," or "how do I keep these two
  pipelines apart." Writes structured field values and a routing decision with its reasoning. Does NOT
  write the follow-up message, run the outreach, forecast revenue, or decide your pricing.
---

# Post-Session Qualify

## What this skill does

The intake question "are you interested in working together?" is the least informative one on the
form. Asking a respondent with no well-formed intention constructs one on the spot, and the
answer then predicts behavior partly because it was elicited: the self-generated validity effect
(Feldman and Lynch, 1988). Measuring intent also changes behavior, usually upward and for people
already well disposed (Morwitz, Johnson and Schmittlein, 1993; Morwitz and Fitzsimons, 2004). A
conversion rate computed against stated intent reads the instrument.

**So grade nothing before the session, and after it grade only what the person did.**

## Lineage

The four observables below overlap deliberately with established B2B qualification frameworks, most
directly MEDDIC (Dick Dunkel and Jack Napoli at PTC, 1996) and its MEDDPICC extension, which
contributed the vocabulary of the economic buyer, the champion, and the compelling event. This is not
MEDDIC. MEDDIC qualifies an active enterprise deal in flight; this qualifies a lead immediately after a
free session, from post-session observed behavior only. The departures are the multiplicative gate, the
cost threshold on champion action, and the calibration protocol. MEDDIC is a registered trademark of
John F. Napoli, US Reg. No. 3,333,508, named here for identification and attribution only.

## The four observables

Grade each on a zero to three scale: zero for observed absence, one to three for observed degree.
Five levels invite false precision. Each observable names where its evidence may come from.

**1. Economic authority.** Can this person cause money to be spent, or do they have to convince
someone who can?

- Evidence channel: operator judgment, plus factual role and organizational context. Those are
  admissible facts here; refusing to look them up leaves the heaviest factor blank forever.
- Watch for: who they said they would need to talk to, whether they described a budget as theirs,
  whether they used "I" or "we" when describing a decision, whether they know their own procurement
  process.
- A title alone does not establish spending power, and a senior person's inability to buy outside
  services is structural rather than personal. Record it as context, weigh it in routing, and never
  convert it into reduced service.
- Before committing this one, read the value back to the operator and accept a one-word override.

**2. Compelling event.** Is there something dated forcing a change?

- Evidence channel: observed in-session behavior, and the dated artifact behind it.
- Watch for: a deadline, a departure, a renewal, an audit, a launch, a season.
- Absent a compelling event, even a genuinely interested buyer is a next-year buyer.

**3. Champion action.** Did they do something that cost them anything?

- Evidence channel: observed behavior during and after the session.
- Watch for: rescheduling something to attend, bringing a colleague, sending a follow-up question
  unprompted, sharing an internal document, asking what it would cost.
- The threshold is cost, not enthusiasm.

**4. Task clarity.** Can they describe one specific, recurring, expensive task?

- Evidence channel: observed in-session behavior.
- Watch for: frequency, who does it now, and roughly how long it takes. All three, or the task is
  aspiration.

The outcome field is not an observable; it is logged after the fact, once it resolves.

Every grade must cite the evidence that produced it, drawn from that factor's own channel.

**Any factor you cannot tie to a specific piece of evidence is left blank.** Write it as UNKNOWN and
raise it to the operator as a question. Never score it, never default it to the low end of the scale,
never infer it from the other three. A defaulted zero silently collapses the multiplicative signal and
drops a row into the calibration set that is not a measurement. This rule is not waivable by a
session-level "skip confirmations" or "stop asking me to confirm" setting.

## The routing signal

Combine the observables into one explicit value. A workable form:

```
signal = authority x compelling_event x task_clarity
```

Multiplicative, not additive: a conjunctive, non-compensatory rule, so a zero anywhere collapses the
whole thing and strength on one factor cannot buy its way past absent authority, absent urgency, or an
unnamed task. Carry champion action as a separate flag rather than a factor, since it is evidence of
momentum rather than of fit.

If any factor is UNKNOWN, the signal is NOT COMPUTABLE. It is not zero. A zero is a finding; a blank is
a gap.

**Then treat the formula as a hypothesis, and say so in the field description.**

It is not validated; the weights are guesses. It becomes an instrument only after calibration:

1. **Log the score at the time of grading**, before you know the outcome. A score recorded after the
   fact is contaminated.
2. **Log the actual outcome** when it lands: bought, did not buy, went quiet, not yet resolved.
3. **Keep the non-buyers in the set.** A model with no negative class can only tell you what buyers
   look like.
4. **Treat your first review as a checkpoint, not a validation.** After the first two dozen or so
   resolved outcomes you can sanity-check whether the zeros are landing where you expected. You cannot
   validate it, and tuning weights at that N fits noise.
5. **Recalibrate against the log, not against memory.** Memory oversamples the deals that closed and
   the ones that hurt.

Until calibration, use the signal to order a follow-up list. Do not use it to decline to follow up,
and never to decline service.

## The two-funnel firewall

Separate boards do not keep two funnels apart inside one CRM, and neither does discipline; both depend
on remembering. **Use a single routing property and filter bilaterally on it.**

1. **One property, on every record.** A short enum: one value per funnel, plus one overlap value for
   records that legitimately belong to both, which is what your own conversion path produces. Not a
   checkbox, not a tag, not a list membership. A required field with a small closed set of values.
2. **Set membership on both sides, never equality.** Each side selects the set of values it owns.
   Each side's exclusion filter names the full set the other side owns, overlap value included.
   Equality filters break silently the moment a third value exists.
3. **Write down which side owns the overlap value, and why.** Exactly one side claims it positively;
   the other excludes it by name. Record the decision next to the property definition.
4. **Legacy and empty values land on the exclusion side.** Every record that predates the property,
   and every one where the field was skipped, defaults to the side where a mistake is harmless.
   Decide which side that is before you build it, and write down why.
5. **Never use the routing filter to find unprocessed records.** The property is unset on brand-new
   records, so the positively filtering side is structurally blind to its own inbound queue. Discover
   work with a query keyed on something present from creation instead, such as records created in the
   last N days, or the source form. A record without the property set is exposed to the other
   funnel's views and sequences, so processing it is the act that closes the exposure. Name a maximum
   acceptable lag between a record appearing and being processed, and treat a breach as a fault.
6. **Creation metadata is not event metadata.** Never infer that the session happened, lapsed, or was
   missed from when the record was created. Read the scheduling artifact itself.
7. **Test all three values with real records.** Create one in each funnel and one carrying the
   overlap value, then confirm each is visible to exactly the views and automations it should be, in
   both directions.

The rule that makes it hold: automations key off the property, never off a list, a board position, or
a lifecycle stage, all of which drift.

## Output format

```
GRADE
  Authority        <n>/3 | UNKNOWN   because <cited evidence> / <question for the operator>
  Compelling event <n>/3 | UNKNOWN   because <cited observation, with the date>
  Task clarity     <n>/3 | UNKNOWN   because <the task, its frequency, and who does it now>
  Champion action  YES/NO/UNKNOWN    <what it was, and what it cost them>
  Authority read-back: <the authority value about to be written>. Confirm or override in one word.

SIGNAL
  Value: <n>   (authority x event x clarity), or NOT COMPUTABLE if any factor is UNKNOWN
  Status: UNVALIDATED. Calibration set: <n> resolved outcomes logged (checkpoint at ~24, not a validation).
  Routing: <which follow-up track; service is unchanged either way>
  Zero factor, if any: <which one, and what would change it>

FIREWALL
  Routing property value written: <value>
  Cross-funnel check: <set this side owns / set the other side excludes / visible only
    where intended: yes/no>

FIELDS WRITTEN
  <field>: <value>
  <field>: <value>

WHAT IS NOT KNOWN
  <the observation this grade needed and did not have>
  <every UNKNOWN factor, restated as a question the operator can answer>
```

## Worked example (invented)

**Input:** a kitchen designer runs free walkthroughs for restaurant owners; two attendees from last
week. The same CRM also holds an unrelated used equipment brokerage funnel.

```
Attendee 1

GRADE
  Authority        3/3   because she owns both locations and called the remodel budget
                          "mine to spend, and I've already moved it."
  Compelling event 3/3   because the hood system failed inspection on July 14 and the
                          re-inspection is September 2. Dated and external.
  Task clarity     2/3   because she named the task (line staff re-plating during the
                          dinner rush) and who does it, but not the minutes per service.
  Champion action  YES   she sent the original 2016 kitchen drawings that evening,
                          unprompted.
  Authority read-back: 3/3, owner with the budget already moved. Operator: confirmed.

SIGNAL
  Value: 18  (3 x 3 x 2)
  Status: UNVALIDATED. Calibration set: 9 resolved outcomes logged (checkpoint at ~24, not a validation).
  Routing: priority follow-up track, this week
  Zero factor, if any: none

FIREWALL
  Routing property value written: design_intake
  Cross-funnel check: yes. Brokerage views select [brokerage, both] and exclude
    [design_intake]; she is invisible to them. If she buys used equipment while the
    design job is still live, this flips to both, which the brokerage side owns.

FIELDS WRITTEN
  qualification_authority: 3
  qualification_event: 3
  qualification_clarity: 2
  champion_action: true
  routing_signal: 18
  signal_status: unvalidated_hypothesis
  funnel_track: design_intake

WHAT IS NOT KNOWN
  Minutes lost per service on the re-plating, so there is no number to quote against.

Attendee 2

GRADE
  Authority        0/3   because he is a hospital kitchen manager and outside design work
                          runs through a procurement office he does not sit in. Structural,
                          not personal.
  Compelling event 2/3   because an equipment replacement cycle is budgeted for next
                          fiscal year: real but not dated.
  Task clarity     3/3   because three staff spend the first hour of every shift
                          hand-counting a walk-in that has no inventory system.
  Champion action  NO    engaged well during the session, nothing since.
  Authority read-back: 0/3, structural rather than personal. Operator: confirmed.

SIGNAL
  Value: 0  (0 x 2 x 3)
  Status: UNVALIDATED, as above.
  Routing: nurture track rather than the priority sequence. Service is unchanged and he
    stays in the calibration set until his outcome resolves.
  Zero factor: authority. The clearest task at the session, and no path from him to a
    signature.
  What would change it: an introduction to whoever owns the procurement decision.

FIREWALL, FIELDS WRITTEN: as above, with routing_signal 0 and champion_action false.

WHAT IS NOT KNOWN
  Whether he has ever routed an outside vendor through that office. If he has, he is a
  channel rather than a buyer, which the formula does not model. Logged as a note.
```

## Boundaries

This grades and routes. It does not write the follow-up, run a sequence, negotiate, quote a price, or
forecast anything. A signal value is a sort order, not a probability, until the calibration set is
full.

It grades from evidence, never from stated intent. If nobody watched the session or nothing was
logged, the honest output is that the lead cannot be graded yet, not a guess assembled from the
intake form.

It does not grade people on anything other than fit and readiness to buy. Personal
characteristics, employer prestige, and how much you liked them are not observables and have no field.

### The grade governs follow-up order only

The grade is a backend artifact. It may order who you contact first. It may never decide who is
admitted to the free offering. Three prohibitions:

- **No buyer-capacity question of any kind on the pre-event form.** Not budget, not authority, not
  "what are you hoping to spend," not a dropdown that quietly sorts. The form collects what you need
  to run the session and nothing else.
- **No recommendation that withholds, deprioritizes, delays, or cancels the free offering** on the
  basis of a grade or a predicted grade. That includes the soft versions: the later date, the smaller
  room, the invitation that goes out last.
- **No "skip this one" output.** There is no field for it and no sentence for it.

What is permitted instead: enrich the record after the session, keep the low scorers in the
calibration set and log their resolved outcome, and extract reusable material from every session
regardless of grade. A structural inability to buy is a fact about the record and the negative class
calibration requires, never a reason to serve someone less.
