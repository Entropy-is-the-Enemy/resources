---
name: content-harvest
description: >
  Scan work you have already done for moments worth posting about, and file each one as a structured
  idea card you can draft from later. Runs on two harvest surfaces: content you submit (a document,
  transcript, thread, or set of notes you paste or point at) and the live session itself when you
  explicitly ask for it. For each candidate it names the angle, the hook, the audience, a confidence
  grade, and whether it is one post or several, then stops. A third, lighter surface updates a card
  you already filed when you report what became of it. Trigger on "harvest this," "any posts in
  this," "harvest the session," "is this postable," "content harvest," "find the ideas in this
  thread," or "that one shipped."
  It does NOT draft, does not pick a platform or a format, and never runs on its own: it fires only
  on explicit invocation. "Nothing here is postable" is a valid and expected result.
---

# Content Harvest

## What this skill does

People with genuinely interesting work post so little not because writing a post is hard, but
because the moment goes by unnoticed. You solve something at 4pm, close the tab, and by morning the
fact that it was worth saying out loud is gone. The bottleneck is **noticing**.

This skill is the noticing step, run on demand: it reads work you have already done, finds the
moments a specific audience would want, files each as a structured card, and stops before a sentence
of the post exists.

Separating noticing from drafting is the whole design. A harvest that drifts into drafting produces
four half-written posts and no queue. One that stays in its lane produces a queue you can draft from
on a day when you have no ideas, which is the day you need one.

## The invocation surfaces

**Submitted content.** You paste something or point at it: a working document, a long thread, a
transcript, rough notes, a summary of something you shipped. The material is bounded, and the harvest
covers exactly that.

**The live session.** You have been working for an hour and say "harvest this." The material is now
the session itself: what you were stuck on, what you tried, what was wrong, what finally worked. This
surface tends to be richer, because sessions contain the reasoning documents edit out, and the
reasoning is usually the postable part.

**A status report on a card you already filed.** "I posted the one about the recount," or "drop the
scanner card, it went nowhere." A bare progress report is a valid invocation: update that card's
status, move it between the open queue and the archive, and stop. No scan, no new candidates.

All three surfaces are **explicit**. This skill does not fire on its own, does not watch for postable
moments in the background, and does not infer a status change from something you happened to mention
while working on something else. An unrequested harvest is an interruption, and interruptions get the
habit turned off.

## Detection: what counts as a moment

A postable moment is not a topic you know about. It is something that happened in the work, with a
shape someone else can use. Look for these:

- **The surprise.** You expected one thing and got another. A corrected expectation is the most
  reliably useful thing you can hand someone; it is what experience is made of.
- **The wrong turn.** An approach you tried that did not work, and the specific reason.
- **The rule you can now state.** You did this three times and can finally say the general thing.
- **The distinction.** Two things that look identical and are not, where confusing them costs you.
- **The number.** A measured before and after, or a real cost, that makes an abstract claim land.

Against that, apply the **honest no**. If the work was competent and unremarkable, the correct output
is "nothing here is postable," with one line on why. That is not a failed run. Two strong ideas beat
eight thin ones manufactured to fill the page: a queue you trust gets drafted from, a padded one gets
skimmed once and abandoned. Three to five candidates from a substantial source is generous. If you
find nine, you are counting topics instead of moments.

## The card: angle, never draft

Each candidate becomes one card with these fields.

- **Angle.** The claim in one sentence, not the subject. "Retry logic" is a subject; "retries hid the
  failure instead of fixing it" is an angle. If you cannot write it as a sentence with a verb and a
  point, you do not have a moment yet.
- **Hook.** Where the post starts, in one line, as a note to yourself. A pointer, not a sentence.
  "Open on the alert that fired for six weeks and meant nothing" is a hook. Writing the actual
  opening line is drafting.
- **Audience lane.** Who this is for. Define your own lanes once and reuse them so the queue sorts.
  As an example set to replace with your own: technical craft, team leadership, industry commentary.
  A candidate may sit in two lanes honestly; the failure case is fitting none. A candidate that lands
  in no lane cleanly is thin, not badly filed, so downgrade it or drop it rather than inventing a
  lane to hold it.
- **One or several, and how strong.** A single post, or a cluster of two or three distinct angles,
  one line each. Split by claim, not by section. On the same line, grade it: **strong**, **worth a
  look**, or **marginal**. Grade at capture, while the material is in front of you and the judgment
  is cheap, so the queue can be read in priority order instead of date order.
- **The material.** The thing the card came from, carried on the card. Short enough to quote, quote
  it exactly. Too long, point at it precisely: the section, the step, the exchange. Separate from
  the source pointer, and the field that decays if you skip it.
- **Source pointer.** Where the raw material lives, specific enough to go back to it.
- **Status.** Where it sits in the lifecycle.

A finished card is the **entire brief** the drafting step needs: claim, opening pointer, audience,
material. Nothing should have to be reconstructed weeks later from a session that is gone and a
document that has since been edited.

The load-bearing rule: **the card records the angle, never a draft.** No opening paragraphs, no
polished sentences, no "here is a version to start from." Quoted source material is not a draft, it
is evidence, and it belongs in the material field verbatim. The moment a card contains prose you
wrote, your drafting and voice step is anchored to whatever got typed in a capture pass, which is
exactly the wrong input for it.

## Lifecycle and the queue

Every card carries a status: **captured -> drafted -> shipped or killed.**

- **captured.** Filed, not yet worked. The default on creation.
- **drafted.** Handed to your drafting and voice step. Now a record, not a source of work.
- **shipped.** Posted. Note where, in one line.
- **killed.** Deliberately dropped, with one line on why. A normal outcome, and it belongs on the
  record: without it you re-surface the same dead idea every quarter.

Split the store in two. The **open queue** holds only `captured` cards. The **archive** holds
everything `drafted`, `shipped`, or `killed`. Move cards on status change, do not relabel in place.
That split keeps a backlog a working queue instead of a junk drawer: the open queue stays short
enough to read strongest first on a drafting day, and a file where live and dead ideas interleave is
a file nobody opens twice.

## Output format

Write cards to a capture file such as `captures/harvest.md`, one block per card.

```
CARD: <short slug>
STATUS: captured
ANGLE: <the claim, one sentence with a verb>
HOOK: <where it opens, one line, a pointer not a sentence>
LANE: <your audience lane>
SHAPE: one post | cluster of <n>   GRADE: strong | worth a look | marginal
  - <angle 1 if cluster>
  - <angle 2 if cluster>
MATERIAL: <the exact quote, or a precise pointer to the passage or moment>
SOURCE: <file, thread, date, or "live session">
NOTE: <optional: what makes it land, or what is missing>
```

And when nothing qualifies:

```
HARVEST: no candidates
SCANNED: <what was read>
WHY: <one line: competent but unremarkable, no surprise, no stated rule yet>
```

## Worked example (invented)

Source: a two-hour session debugging why a warehouse barcode scanner silently dropped about one scan
in forty.

```
CARD: retries-hid-the-drop
STATUS: captured
ANGLE: The retry logic was not fixing the dropped scans, it was hiding them, and the success
  rate metric was measuring the retries.
HOOK: Open on the dashboard reading 99.97% while the floor team recounted pallets.
LANE: technical craft
SHAPE: cluster of 2   GRADE: strong
  - A metric that counts attempts instead of outcomes will always look healthy.
  - The floor team knew for months. Nobody had a channel that made their knowing count.
MATERIAL: Same day, same dashboard: 99.97% success, 56,300 scans, 1,412 retries. The retries
  were counted as successes.
SOURCE: live session
NOTE: The second angle is stronger and is not technical at all.

CARD: forty-to-one
STATUS: captured
ANGLE: One dropped scan in forty sounds like a rounding error until you multiply it by a
  shift, at which point it is two hours of recounting a day.
HOOK: Open on the arithmetic, before the bug.
LANE: team leadership
SHAPE: one post   GRADE: worth a look
MATERIAL: The arithmetic as it was worked in the session: 2,200 scans a shift, 1 in 40 dropped,
  55 recounts, about two hours.
SOURCE: live session
NOTE: Carries a real number. Check the shift figure before drafting.
```

What did not get captured: the fix, a config change any reader could look up, and the tooling
walkthrough, which was competent and unremarkable. Two cards from two hours is a good harvest.

## Boundaries

This skill notices and files. It does not draft, rewrite, tighten, or apply voice: that is your
drafting and voice step, working from a card. When one request asks for both ("find the ideas in
here and write the best one up"), do the noticing, say plainly that drafting is a separate step, and
hand the finished card over as the brief for it. A combined request is not permission to skip the
boundary; it is the case the boundary exists for. It does not choose between a thread, a short post,
or a carousel, and does not know character limits: that is a platform-format step, applied after a
draft exists. It does not schedule or batch across many sources on its own: that is an orchestration
step you invoke deliberately. It is not general knowledge capture, so a useful fact with no audience
and no angle does not belong on a card. It never fires unasked.
