---
name: airtight
description: >
  Run a deep verification and confidence-calibration pass on a document before it goes out, when a
  single wrong fact is expensive. Every load-bearing claim is forced into exactly one of three states:
  verified, confidently stated, or flagged. Use this on board and committee memos, funding
  applications, client-facing recommendations, published research, regulatory filings, safety and
  clinical guidance, and anything containing a number, a calculation, a named source, a quote, a
  statute, or a claim about the current state of the world that a reader will act on. Trigger on "make this airtight," "verify this," "ground-truth this," "fact-check this,"
  "before this goes out," or "lock this down." This is the DEEP single-fact, number, and citation
  lane. For a broad multi-dimension quality pass over an AI draft (relevance, tone, completeness,
  ethics, as well as facts), run that broader review first and escalate its load-bearing items here.
---

# Airtight

## What this skill does

Airtight is a verification gate. It runs over a finished or near-finished document and does one job:
make sure nothing in it is a guess wearing the costume of a fact.

It is not an editor. It does not improve your prose, restructure your argument, or adjust your voice.
It finds the claims a reader will act on and settles each one.

## The standard: three states, no fourth

Before the document goes out, every load-bearing claim must resolve to exactly one of these:

- **Verified.** Checked against a source you can name. You know where the number came from and you
  could produce it if challenged.
- **Confidently stated.** Not externally checked, but you would stake the deliverable on it. Domain
  knowledge you own, from a position where being wrong would be embarrassing rather than surprising.
- **Flagged.** Uncertain, and the uncertainty is marked and made actionable in the document itself
  or in the note that accompanies it.

There is no fourth state. A claim that is none of these is a guess in a suit, and it is the entire
reason this gate exists.

**Hedging is a failure mode, not a safety net.** Marking everything "approximately" or "roughly" or
"I believe" is not caution. It is laziness with a disclaimer stapled on, and it transfers the
verification work to your reader, who has less context than you and no way to do it. A document where
every claim is hedged fails this gate exactly as hard as one stated with false confidence. Reflexive
hedging and reflexive confidence are the same error pointed in opposite directions.

## Scale the effort to the stakes

Verification effort tracks consequence, not convenience.

- **Routine.** Internal, reversible, low cost if wrong. Spot-check the numbers and the current-state
  claims. Do not build a full log.
- **Consequential.** Someone outside your team acts on this, or it informs a decision that is
  annoying to reverse. Walk every vector below. Recompute every derived figure. Flag what you cannot
  settle.
- **Irreversible.** Money moves, a filing is made, a reputation is on the line, or a person's health
  or legal position depends on it. Nothing ships until every load-bearing claim is verified against a
  primary source with the source named, and a human is on record as having checked it.

If the stakes were not stated, infer them, say which tier you are applying, and let it be overridden.

## The seven fabrication vectors

These are the specific places a capable model, or a fast human, most often ships an error. Walk them
in order. For each, the tell is what to look for on a scan.

**1. Current-state claims.** The highest-yield trap. Any claim about what is true *right now*: a
price, a rate, a rule, a version, who holds a role, whether a program still exists. Training data has
a cutoff and the world does not. *Tell:* the words "currently," "as of," "the latest," or a present-tense
verb attached to an external fact. Every one of these needs a dated source or a flag.

**2. Numbers and derivations.** Any figure, and especially any figure computed from other figures.
See the recomputation rule below. *Tell:* a number with more than two significant digits, or a
percentage that no one shows the arithmetic for.

**3. Sources and citations.** Titles, authors, dates, page numbers, URLs, case names, statute numbers.
These are cheap to invent and expensive to be caught inventing. *Tell:* a citation that is perfectly
formatted and perfectly convenient.

**4. Negative and absence claims.** "There is no requirement that," "no competitor offers,"
"nothing in the record shows." Proving absence is much harder than proving presence, and this class of
claim is almost never actually checked. *Tell:* the words no, none, never, nothing, only.

**5. Causal and mechanism claims.** "X happened because Y." Correlation dressed as mechanism.
*Tell:* because, drives, causes, leads to, results in, attached to two things you have only observed
together.

**6. Implied completeness and closed sets.** "The three options are," "all of the requirements are,"
"the factors that matter are." A list presented as exhaustive when it is a list of what came to mind.
*Tell:* a numbered list with a definite article in front of it.

**7. Quotes and motives.** What someone said, and why they did something. Paraphrase drifts toward
what would be convenient, and attributed motive is usually the writer's inference. *Tell:* quotation
marks around anything you did not read off a transcript, and any sentence describing what a named
person wanted, feared, or intended.

## The recomputation rule

Any figure derived from other figures must be recomputed from its inputs, in the document's own
context, before it ships. Not eyeballed. Not trusted because it looked right last time.

The reason this matters more than it sounds: a fabricated number is often obviously wrong, and someone
catches it. A derived number with correct inputs and wrong arithmetic looks completely reasonable.
The inputs check out, so nobody rechecks the math, and the error travels all the way to the decision.
It is the more insidious of the two failures by a wide margin.

Show the arithmetic in your working notes even when it does not appear in the document. If you cannot
reproduce a figure from named inputs, the figure is not verified, whatever its provenance.

## A flag is a work order

A useful flag is not "verify this." It names three things:

1. **The claim**, quoted exactly as it appears in the document.
2. **The source to check**, specifically enough that someone else could go check it. Not "a market
   report." The report, the filing, the person, the page.
3. **The location**, so the fix is a two-minute job and not a re-read.

Add a fourth element when it applies: what changes if the claim is wrong. A flag on a number that
moves a recommendation is not the same as a flag on a number in a background paragraph, and the person
triaging your flags needs to know which is which.

## Output format

Lead with the verdict. Then the detail.

**Verdict**, one of:

- **AIRTIGHT.** Every load-bearing claim is verified or confidently stated. Ship it.
- **FLAGS OPEN.** Specific claims need checking before this goes out. Listed below.
- **DO NOT SEND.** A load-bearing claim is wrong, unsupportable, or a derived figure does not
  recompute.

Then:

1. **Why**, one line.
2. **Verified**, with the source named for each.
3. **Confidently stated**, so the sender can see what they are standing behind.
4. **Flags open**, each as a work order per the four elements above, ordered by what it would cost to
   be wrong.
5. **Recomputation log**, for consequential and irreversible tiers: every derived figure, its inputs,
   and the result you got.

For irreversible-tier documents, append the log to the working file so the check is auditable later.
For routine work, the verdict and the flags are enough.

## Worked example (invented)

**Input:** a two-page memo recommending a software purchase, going to a nonprofit's board.

> **Verdict: FLAGS OPEN.** Three claims are load-bearing and unsettled, and one derived figure does
> not recompute.
>
> **Verified**
> - Annual license cost of $84,000 (vendor quote dated last week, attached as Appendix B).
>
> **Confidently stated**
> - "Migration typically takes two to three weeks." Your own experience with the last two systems you
>   moved. You would stand behind it; leave it unhedged.
>
> **Flags open**
> - Claim: "The platform is the only one in this category with native audit logging." Vector: negative
>   or closed-set claim. Check: name the three or four products actually surveyed, and when, or soften
>   to "of the products we reviewed in March." Location: page 1, paragraph 3. Cost if wrong: one board
>   member who knows of a second product reads the entire memo as unresearched.
> - Claim: "Their enterprise tier currently includes unlimited seats." Vector: current-state. Check:
>   the vendor's live pricing page today, not the deck they sent in the spring. Location: page 1, the
>   comparison table. Cost if wrong: seat pricing is the whole basis of the cost comparison.
> - Claim: "Payback in 14 months." Vector: derived figure. Recompute: $84,000 divided by the stated
>   monthly savings of $5,400 is 15.6 months, not 14. Location: page 2, the summary box. Cost if
>   wrong: it is the headline number of the recommendation.
>
> **Recomputation log**
> - Payback: 84,000 / 5,400 = 15.56 months. Document says 14. Does not reconcile; either the savings
>   figure is stale or the payback was computed from a different input. Settle before sending.

Note what the example does not do. It does not rewrite the sentences, and it does not soften the
recomputation miss. The gate reports; the author decides.

## Boundaries

Airtight verifies. It does not draft, restructure, or apply a voice, and it does not judge whether the
argument is persuasive or the tone fits the reader. Those are separate jobs, and running them at the
same time as this one reliably produces a document that reads better and is no more true.

Run a broad quality review first if the draft is unproven across relevance, tone, and completeness.
Bring its load-bearing factual items here.
