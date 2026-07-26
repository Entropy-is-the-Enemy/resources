---
name: acquisition-screen
description: >
  Screen an acquisition target's financials against a size-banded rubric and return a go, conditional,
  counter, or pass verdict that a lender or a partner could follow. Reads uploaded statements, teasers,
  tax returns, and summaries; picks the size band from what is actually in the documents; applies the
  band's own thresholds for margin, debt service coverage at three points in the deal's life, and
  customer concentration; re-underwrites earnings against what a new owner must fund; declines when the
  buyer cannot name the weakness they are equipped to fix; and refuses to state a verdict until every
  derived number has been recomputed and the verdict checked against it. Trigger on "screen this deal,"
  "does this pencil," "go or pass," "review these financials," "run the numbers on this target," or when
  financial documents for a target arrive with no question attached. Does NOT negotiate, write the
  offer, plan the takeover, or verify anything outside the arithmetic.
---

# Acquisition Screen

## What this skill does

Band the thresholds by deal size, re-underwrite earnings to what a new owner takes home, score the
weakness you are equipped to fix, and print no verdict until a separate gate has recomputed the
arithmetic and checked the verdict against it.

## Step 1: pick the band before the thresholds

Define your bands once, in advance, and let the documents select which one applies. Two is usually
enough. **Diligence gates scale with deal size, and they trade against each other rather than all
tightening at once:** pair a loosened concentration ceiling with a tightened floor somewhere
structurally related, most usefully customer tenure.

Set, per band:

- **Margin floor.** What gross and operating margin must clear to survive a bad year.
- **A coverage floor set, not a coverage floor.** Three ratios, each on the actual proposed structure
  rather than a placeholder:
  - **Base.** At close, on flat no-growth historical earnings. Clears the band's base floor.
  - **Stress.** Under a named first-year earnings decline, percentage stated. Clears a lower, explicitly
    written stress floor.
  - **Step-up.** Recomputed at the period when any deferred, standby, or interest-only portion of the
    consideration begins amortizing. Clears the **base** floor, not the stress floor.
- **The absolute cushion, in currency, quoted beside every ratio.** Earnings available for debt service
  minus annual debt service, stated as money. On the smaller band it is the binding test.
- **Concentration ceiling, paired with a tenure floor.** State both, always together.
- **Owner dependence test.** How much of the revenue walks out with the seller.
- **Hard exclusions.** The findings that end the review regardless of the numbers. Write them in
  advance so they cannot be argued away in the moment.
- **What you are not the right owner of.** Categories where you bring nothing a cheaper or
  better-matched buyer does not. Written beside the exclusions.

Expect your values near the conventions: base coverage floor 1.25x to 1.50x, stress floor near 1.10x
under a fifteen to twenty percent first-year decline, concentration ceiling in the twenties. Say when
you are using a convention.

If the documents do not settle the band, say so and ask rather than defaulting to the more permissive
one.

### Conditional admission, instead of a blanket exclusion

For a category you would otherwise exclude outright because its average member is bad, keep it
admissible and make it expensive. Write two lists: a conjunctive qualifying set where **every** item
must hold, and a disjunctive veto set where **any one** item ends the review. Adapt the items; for a
category that usually fails on volatility, all of: repeat demand across cycles, pricing that passes
input cost through, committed forward workload, few qualified competitors. Any one of, and the review
stops: the founder is the pricing authority, know-how leaves undocumented with the seller, the
counterparty owns the specifications, one work type dominates revenue.

Run it as early as the hard exclusions, re-confirm once customer-level detail arrives, and let failure
stop the review the way an exclusion does.

## Step 2: underwrite your own free cash flow, not the seller's

You are buying the business the seller ran plus whatever you must add to run it without being the
seller. Before any coverage ratio gets computed, subtract the cost of the gaps:

- **The role the seller was filling for free.** If the owner was also the general manager, plant lead,
  or top salesperson, price the hire at a market salary. Treat any claim that the business runs without
  the owner, or that the owner is in two days a week, as an unverified assertion from the party most
  motivated to understate it. Test it against proxies: who signs the agreements, who holds the customer
  relationships, whether the headcount contains anyone who could hold the role, where the owner spends
  the week. The tested answer sizes the backfill; the stated one does not.
- **The systems that were never bought.** Software and tooling the business ran without is a bill in
  your first year.
- **The deferred maintenance.** Equipment at the end of its life is a capital call with a date on it.
- **The customer-facing capacity you will need.** If growth is in the thesis, someone has to sell, and
  that someone is leaving.

Finance against seller's normalized earnings minus those costs.

**Frame value before you quote a price.** Once the seller has been walked through what a new owner must
fund, the counter is a shared arithmetic problem rather than an insult.

## Step 3: name your edge, or decline

Financial gates alone approve sound businesses you bring nothing to and win only by paying the most.
Score the gap you close like a gate.

Name the specific improvable weakness in this target that **you** are equipped to fix: not a category of
skill you have, but the underdeveloped system in this business and the change you would make to it.
Record one of five scores.

- **Clear.** Named weakness, you have fixed this exact thing before, and the fix needs no capability the
  business lacks.
- **Partial.** Plausible, but name the specific system or function that is underdeveloped. Unnamed is
  absent.
- **Absent.** You cannot name one. **This is a PASS, regardless of every financial gate clearing.**
- **Outside your competence.** Real weakness, someone else's to fix. Also a PASS.
- **Not yet knowable.** The documents will not carry the question. Not a verdict, a request for what is
  missing.

Then the subordinate question: **is there headroom for the improvement to land in?** Physical,
contractual, or operational. An edge that doubles throughput against a facility, licence, or supply
ceiling that will not move scores partial at best.

Check the answer against your written list of what you are not the right owner of. An edge that survives
only as a general claim that things could be run better is absent.

## Step 4: the numbers pass, as its own gate

**Gate one, the numbers pass.** Runs before the verdict. Its only question is whether the arithmetic
is right.

1. **Recompute, do not re-read.** Every derived figure gets calculated again from the source numbers.
2. **Trace every number to a location.** Document, page or tab, line.
3. **Cross-foot, then reconcile the two versions.** Statement totals against their components, period
   against period, income against cash. Then, where the same period exists in both a sale-prepared and
   an authority-filed document, reconcile them line by line. Every delta is a finding, and the
   authority-filed version governs.
4. **Reconcile the adjustments.** Every add-back listed, sourced, and separately defensible.
5. **Test the verdict against the recomputed gates.** Read the draft verdict back against every gate
   result as recomputed, not as first written. Resolve any contradiction by the rules already in this
   file: a clean gate failure resolves to PASS, and a failure the structure check calls renegotiable
   resolves to COUNTER.
6. **Disclose any correction that moved the verdict.** If recomputation changed the call, put the prior
   figure, the corrected figure, and the input that drove the change at the top of the recommendation.

Exactly one condition stops you and sends you to a human: two sources give irreconcilable values for the
same input. Do not silently pick one and do not split the difference. Name both values, name their
sources, and ask.

Not every check is owed on every review: a decline on an obvious kill reason may skip tracing and
cross-footing. It may never skip recomputation, and a shortcut estimate still gets its arithmetic
recomputed before it is quoted.

The gate closes or no final verdict prints. A verdict issued while the gate is still open is marked
provisional, lists the open items, and does not leave your hands until they close. State explicitly
which figures could not be traced.

**Gate two, everything else.** Runs later, only when the artifact leaves your hands: claims about the
market, the regulatory posture, the named sources, the industry statistics. Do not fold it into gate
one.

## Step 5: the verdict, and the structure check before a pass

Four outcomes only:

- **GO.** Clears the band's thresholds on the re-underwritten number. Proceed.
- **CONDITIONAL.** Clears subject to named, checkable items. Each condition gets a verification method
  and a fail consequence, or it is not a condition, it is a hope.
- **COUNTER.** Fails as presented but the flaw is in the wrapper rather than the business.
- **PASS.** Fails on its own merits, hits a hard exclusion, fails conditional admission, or the edge
  scores absent or outside your competence.

**Before any PASS prints, force the distinction between "no" and "no at this structure."** Check
whether the failure moves under a change to how the consideration is formed, when it pays, what the
headline is, or who else is at the table. If any of those fixes it, the verdict is COUNTER and the
output owes a specific one. Reserve a pass for a business you would not want on generous terms, and for
one you have no business owning.

## Output format

```
BAND
  Selected: <band> because <the figure in the documents that placed it>
  Thresholds in force: margin <x>, base coverage <y> and stress coverage <y2> at a <p>%
    first-year decline, concentration <z> paired with tenure <t>

RE-UNDERWRITTEN EARNINGS
  Seller normalized:        <figure>  [source: doc, page, line]
  Less role to backfill:    <figure>  <role, basis for the number>
  Less systems and tooling: <figure>
  Less deferred capital:    <figure>
  Underwriting basis:       <figure>

GATES
  Margin:           <pass/fail> <computed> vs <floor>
  Coverage base:    <pass/fail> <at close, flat historical> vs <base floor>
  Coverage stress:  <pass/fail> <at a <p>% first-year decline> vs <stress floor>
  Coverage step-up: <pass/fail> <at <period> when deferred consideration amortizes> vs
                    <base floor>, or n/a if nothing is deferred
  Annual cushion:   <currency> earnings available less annual debt service
  Concentration:    <pass/fail> <top customer %> at <tenure>
  Owner dependence: <finding, and the proxies it was tested against>
  Conditional admission: <n/a, or all-of met and no veto triggered, or which item failed>
  Hard exclusions:  <none, or which one>

EDGE
  Score: clear | partial | absent | outside competence | not yet knowable
  The weakness you fix: <the specific underdeveloped system or function>
  Headroom: <where the improvement lands, or the ceiling that blocks it>

NUMBERS PASS
  Recomputed: <n of n derived figures>
  Untraceable: <list, or none>
  Cross-foot discrepancies: <list, or none>
  Sale-prepared vs filed deltas: <list, or none, or not testable and what to request>
  Add-backs reconciled: <n of n>
  Verdict consistent with recomputed gates: <yes, or the contradiction and how it resolved>
  Gate: CLOSED / OPEN

VERDICT: GO | CONDITIONAL | COUNTER | PASS
  Correction that moved the call: <was <figure>, now <figure>, driven by <input>, or none>
  Because: <one sentence>
  If COUNTER, the counter: <the specific change>
  If CONDITIONAL, each condition: <item> verified by <method>, fails to <consequence>
```

## Worked example (invented)

**Input:** a single-yard lighting and grip rental house, two years of statements plus a broker summary,
asking four times reported earnings.

```
BAND
  Lower band: operating earnings $310K, below the $750K break. In force: margin 12%, base
  1.50x, stress 1.15x at a 20% decline, concentration 45% with 5-year tenure above 30%.

RE-UNDERWRITTEN EARNINGS
  Seller normalized:        $310,000  [P&L 2025, summary tab, line 44]
  Less role to backfill:    $95,000   owner books and quotes every job; yard manager
  Less systems and tooling: $18,000   inventory software; currently a whiteboard
  Less deferred capital:    $40,000   a third of the lighting past service life
  Underwriting basis:       $157,000

GATES
  Margin:           fail on the basis. 17.2% reported, 8.7% vs the 12% floor. Driven by
                    the $95K backfill, not by the trade: see the verdict.
  Coverage base:    fail. 1.12x on the basis; 2.21x on the seller's number, the trap.
  Coverage stress:  fail. 0.90x at a 20% decline ($125,600 vs $140,200 of service).
  Coverage step-up: n/a, nothing deferred. Recomputed under the counter.
  Annual cushion:   $16,800. One slow quarter erases it; 1.12x reads as a near miss.
  Concentration:    fail on the pair. Top customer 38% at 2 years: under the ceiling,
                    under the tenure floor.
  Owner dependence: high, tested not taken. Summary says "two days a week"; he signs
                    every agreement, every booking arrives by text. Sized the $95K.
  Conditional admission: n/a.  Hard exclusions: none.

EDGE
  Partial. Booking and utilization run on text and a whiteboard; this buyer has installed
  utilization reporting before. Headroom: the yard runs at sixty percent utilization.

NUMBERS PASS
  Recomputed 14 of 14. Add-backs 3 of 4. Untraceable: broker "normalized" figure $28K
  above the statements. Cross-foot: balance sheet equipment over the itemized list by
  $61K. Filed deltas: not testable, no returns provided, request both. Verdict consistent
  with recomputed gates: yes, all three failures move under a lever. Gate: OPEN.

VERDICT: COUNTER (provisional, numbers pass has not closed)
  Correction that moved the call: none.
  Because: all three failures are in the wrapper, not the trade. Margin is the one worth
  reading twice. It fails only on the basis, and the whole gap is the $95K backfill, so it
  moves on Partners: the seller staying twelve months in a defined paid role at less than
  a full manager's cost lifts the basis above the floor while the reporting gets built.
  A margin shortfall driven by a cost you are choosing to add is renegotiable. One driven
  by what the business earns is a hard PASS, and this is not that.
  Counter: hold the headline, move a third of consideration into
  seller paper behind the lender, interest-only, release tied to the top customer still
  booking at month eighteen. Clears 1.55x at close. The step-up set the term: at
  twenty-four months the note amortizes into 1.31x, under the 1.50x floor, so ask
  thirty-six, recomputing to 1.52x with cushion above $40K. Close the numbers pass before
  it goes out; all three open items change the counter if they resolve badly.
```

## Boundaries

This screen reads financials and returns a verdict. It does not negotiate, draft the offer or the
letter of intent, plan the first hundred days, or run the operating business afterward. It is not
investment advice, it is not an appraisal, and it does not replace a quality-of-earnings engagement or
your own accountant and counsel.

It will not produce a verdict from a teaser alone. If the documents cannot support the band selection
or the numbers pass, the correct output is the list of what is missing.

It will not print an approval where the edge scores absent. No financial result overrides that.

It does not verify anything that is not arithmetic. Market, regulatory, and industry claims are gate
two, a different pass.

## Prior art

None of the underlying mechanics are new. The buyer-side re-underwrite is covered in Ruback and
Yudkoff's *HBR Guide to Buying a Small Business* and across the standard owner-buyer acquisition
literature. Cross-footing, tie-outs, and add-back reconciliation are ordinary quality-of-earnings
procedure that any accounting firm will sell you.

What this file adds is arrangement: gates banded by deal size, a concentration ceiling quoted only with
a tenure floor, a coverage floor set tested at three moments with a cushion in money beside it, a buyer
edge that is scored and can decline on its own, and a numbers pass that holds the verdict hostage until
the arithmetic and the verdict agree.
