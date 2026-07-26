---
name: content-harvest
description: >
  Scan work you have already done for moments worth posting about, and file each one as a structured
  idea card you can draft from later. Runs on two surfaces: content you submit (a document,
  transcript, thread, or set of notes you paste or point at) and the live session itself when you
  explicitly ask for it. For each candidate it names the angle, the hook, the audience, and whether it
  is one post or several, then stops. Trigger on "harvest this," "any posts in this," "harvest the
  session," "is this postable," "content harvest," or "find the ideas in this thread."
  It does NOT draft, does not pick a platform or a format, and never runs on its own: it fires only
  on explicit invocation. "Nothing here is postable" is a valid and expected result.
---

# Content Harvest

## What this skill does

The reason people with genuinely interesting work post so little is rarely that writing a post is
hard. It is that the moment goes by unnoticed. You solve something at 4pm, close the tab, and by
morning the fact that it was worth saying out loud is gone. The bottleneck is **noticing**.

This skill is the noticing step, run on demand. It reads work you have already done, finds the moments
a specific audience would want, files each as a structured card, and then stops, on purpose, before a
sentence of the post exists.

Separating noticing from drafting is the whole design. A harvest that drifts into drafting produces
four half-written posts and no queue. One that stays in its lane produces a queue you can draft from
on a day when you have no ideas, which is the day you need one.

## The two invocation surfaces

**Submitted content.** You paste something or point at it: a working document, a long thread, a
transcript, rough notes, a summary of something you shipped. The material is bounded, and the harvest
covers exactly that.

**The live session.** You have been working for an hour and say "harvest this." The material is now
the session itself: what you were stuck on, what you tried, what was wrong, what finally worked. This
surface tends to be richer, because sessions contain the reasoning documents edit out, and the
reasoning is usually the postable part.

Both surfaces are **explicit**. This skill does not fire on its own, does not watch for postable
moments in the background, and does not append cards to unrelated work. An unrequested harvest is an
interruption, and interruptions get the habit turned off.

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
  Yours should match the audiences you write for and stay few enough to hold in your head.
- **One or several.** A single post, or a cluster of two or three distinct angles, one line each. Do
  not split by section; split by claim.
- **Source pointer.** Where the raw material is, specific enough to find the details again.
- **Status.** Where it sits in the lifecycle.

The load-bearing rule: **the card records the angle, never a draft.** No opening paragraphs, no
polished sentences, no "here is a version to start from." The moment a card contains prose, your
drafting and voice step is anchored to whatever got typed in a capture pass, which is exactly the
wrong input for it.

## Lifecycle and the queue

Every card carries a status: **captured -> drafted -> shipped or killed.**

- **captured.** Filed, not yet worked. The default on creation.
- **drafted.** Handed to your drafting and voice step and turned into copy. Now a record, not a
  source of work.
- **shipped.** Posted. Note where, in one line.
- **killed.** Deliberately dropped, with one line on why. A normal outcome, and it belongs on the
  record: without it you re-surface the same dead idea every quarter.

Split the store in two. The **open queue** holds only `captured` cards. The **archive** holds
everything `drafted`, `shipped`, or `killed`. Move cards on status change, do not relabel in place.
That split keeps a backlog a working queue instead of a junk drawer: the open queue stays short enough
to read top to bottom on a drafting day, and a file where live and dead ideas interleave is a file
nobody opens twice.

## Output format

Write cards to a capture file such as `captures/harvest.md`, one block per card.

```
CARD: <short slug>
STATUS: captured
ANGLE: <the claim, one sentence with a verb>
HOOK: <where it opens, one line, a pointer not a sentence>
LANE: <your audience lane>
SHAPE: one post | cluster of <n>
  - <angle 1 if cluster>
  - <angle 2 if cluster>
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
SHAPE: cluster of 2
  - A metric that counts attempts instead of outcomes will always look healthy.
  - The floor team knew for months. Nobody had a channel that made their knowing count.
SOURCE: live session
NOTE: The second angle is stronger and is not technical at all.

CARD: forty-to-one
STATUS: captured
ANGLE: One dropped scan in forty sounds like a rounding error until you multiply it by a
  shift, at which point it is two hours of recounting a day.
HOOK: Open on the arithmetic, before the bug.
LANE: team leadership
SHAPE: one post
SOURCE: live session
NOTE: Carries a real number. Check the shift figure before drafting.
```

What did not get captured: the fix, a config change any reader could look up, and the tooling
walkthrough, which was competent and unremarkable. Two cards from two hours is a good harvest.

## Boundaries

This skill notices and files. It does not draft, rewrite, tighten, or apply voice: that is your
drafting and voice step, working from a card. It does not choose between a thread, a short post, or a
carousel, and does not know character limits: that is a platform-format step, applied after a draft
exists. It does not schedule or batch across many sources on its own: that is an orchestration step
you invoke deliberately. It is not general knowledge capture, so a useful fact with no audience and no
angle does not belong on a card. It never fires unasked.
