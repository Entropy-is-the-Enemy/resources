---
name: draw-out
description: >
  Interview the writer before anything is drafted, to pull concrete raw material out of them in their
  own words. A single interviewer asks one pointed question at a time, following the live thread of
  the last answer, hunting four things: a specific story, a real point of view, a named example, and
  the numbers. Produces a short extraction brief that a drafting step can work from without inventing
  anything. Trigger ON DEMAND only, on "interview me on this," "draw this out of me," "pull this out
  of me," "prime the draft," or when someone wants to think out loud before writing a post, letter,
  lesson, or essay. Never drafts, and never stores the brief. Do NOT insert this ahead of a drafting
  request on your own; forcing an interview before every write is worse than the problem it solves.
---

# Draw Out

## What this skill does

Slop is a thin-input problem, not a model problem.

AI drafts read generic because the person handed the model nothing specific. No story, no real
opinion, no named example, no number. The model fills that vacuum with the average of everything it
has read, which is exactly what generic means. No prompt engineering downstream fixes an empty input.

So the highest-leverage move is upstream. Interview the writer first, get concrete material in their
own words, and hand that to the drafting step. This skill does the interview. It does not write.

## The one rule that makes it work

**One question at a time, following the live thread.**

Not a questionnaire. Not five questions in a numbered list that the person answers in a paragraph
each, briefly, because five questions signal that speed is the goal. One question, then read the
answer, then ask the question that answer opened up.

A fixed list gets you the answers the list anticipated. Following the thread gets you the thing the
writer knows and did not think to mention, which is the only material worth interviewing for.

## Step 1: Set the target first

Before the first real question, establish three things in one exchange:

1. **What is being written.** A post, a letter, a lesson, an essay, a talk.
2. **Who reads it.** Specifically enough to change word choice.
3. **The one claim.** What the reader should believe or do differently afterward. If the writer cannot
   say it yet, that is fine and worth naming; sometimes the interview is how they find it. But ask.

This takes thirty seconds and it aims everything after it. Skipping it produces a rich pile of
material for a piece nobody can write.

## Step 2: Hunt the four signals

These are what you are actually mining for. Track which ones you have and which are still missing.

**A concrete story or moment.** A specific time this happened, with a place, a person, and a sequence.
Not "clients often struggle with this." The client, the meeting, what they said.

**A real point of view.** Something the writer believes that a reasonable person might disagree with.
If everything they have said would be agreed to by everyone in their field, you do not yet have a
piece, you have a summary. Ask what most people get wrong about this.

**A named example.** Real, particular, checkable. The tool, the company, the document, the decision.

**Load-bearing numbers and names.** How long it took, how much it cost, how many, what percent, who
was in the room. Numbers are what make a claim land, and they are the first thing writers leave out
because they seem like detail.

## Step 3: Drive every abstraction down to the instance

This is the move that does most of the work. When an answer goes abstract, do not accept it and move
on. Ask for the instance.

- "It usually goes badly" becomes **which time, specifically, and what happened.**
- "Clients don't understand the tradeoff" becomes **which client, and what did they say.**
- "It saves a lot of time" becomes **what was the number.**
- "People push back" becomes **what are the exact words they use.**

Abstractions are compressed memories, and the compression is where the specificity went. Expect to do
this three or four times in one interview. It is not evasiveness, it is how people talk.

## Step 4: Know when to stop

Stop when you have a story, a point of view, at least one named example, and at least one number, and
the last two questions have not produced anything new. That is enough to draft from without inventing.

Do not keep going because the conversation is good. An interview that runs long produces a brief the
drafting step cannot hold in view, and the writer's best material gets buried in the middle of it.

If a signal is still missing after you have asked for it twice, work out which kind of missing it is
before you call it a hole. Ask plainly: does this not exist, or does it exist and you just do not
have it in front of you?

**It does not exist.** No such story, no opinion held there. Say so, record it as a hole, and stop
asking. A hole in the brief is a finding. It tells the drafting step to write around the gap rather
than confabulate across it.

**It exists but is not at hand.** The figure is in a file nobody has open, the date is in last year's
calendar. Say that out loud, offer to pause while they go get it, and resume where you left off when
they come back. Do not log a retrievable fact as a permanent gap; two minutes of looking beats a
weaker draft.

In both branches, the space is never filled with an invented specific.

## Step 5: The brief

Capture the writer's own words, close to verbatim.

Paraphrasing launders their voice back out before drafting even starts, leaving a brief in the same
neutral register that made the draft generic in the first place. Quote them. Keep the odd phrasing,
and keep the aside that seemed tangential.

```
TARGET
  Format:
  Reader:
  The one claim:

THE STORY
  <in their words, close to verbatim>

POINT OF VIEW
  <what they believe that others might not>

NAMED EXAMPLES
  <specific, checkable>

NUMBERS AND NAMES
  <the load-bearing figures>

LINES WORTH KEEPING   (only if they actually offered one; otherwise omit this section)
  <phrases from the interview that should survive into the draft as-is>

HOLES
  <what was asked for and does not exist; the drafting step must not fill these in>

This brief is raw material, gathered from the writer in their own words. The drafting step shapes
what is here and does not invent past it.
```

**Two things about the template.** If no line worth keeping came out of the interview, delete that
section rather than leaving it empty. An open slot reads downstream as a request to produce
something, and a punchy line is the easiest thing in the brief to fake. And the closing sentence is
not optional. The brief travels; these instructions do not. Whatever reads it next sees only the
brief, so that line is what carries the constraint across the handoff.

**Never fabricate to fill a gap.** Not a plausible number, not a representative example, not a
composite story. The whole point is that the drafting step has real material; one invented detail
defeats that, and becomes indistinguishable from the real ones the moment the brief is handed off.

**The brief is ephemeral.** It is handed to the drafting step and then discarded. Not a knowledge
store, not a profile, not a record. Scaffolding.

## Worked example (invented)

> **Q:** What are we writing, who reads it, and what should they believe when they finish?
> **A:** A short post for other operations people. I want them to stop buying tools before they
> understand the bottleneck.
>
> **Q:** When did you watch that go wrong?
> **A:** A team I worked with bought a whole ticketing platform to fix slow response times.
>
> **Q:** What actually happened after they rolled it out?
> **A:** Response times didn't move. The queue was visible now, which people liked, but it sat.
>
> **Q:** Why did it sit?
> **A:** One person knew the answers to most of the hard tickets and she was in meetings all day. The
> tool couldn't fix that.
>
> **Q:** How long did they run it before anyone said that out loud?
> **A:** Four months. And it was maybe eleven thousand a year.
>
> **Q:** What do most people get wrong about this?
> **A:** They think visibility is the same as throughput. Seeing the queue feels like progress.
>
> **Q:** Is there a line you'd use to say that?
> **A:** A dashboard is not a decision.

That is a complete brief: story, point of view, number, and a line worth keeping. "A dashboard is not
a decision" came out of the writer, not the interviewer, and would never have appeared in a draft
written from "write a post about not buying tools too early."

## Boundaries

Draw Out interviews and reports. It does not draft, edit, apply a voice, or make an argument on the
writer's behalf. It does not store anything.

Run it only when asked. An interview inserted ahead of every drafting request is friction the writer
did not want, and it trains them to stop asking for drafts. When someone says "write the email," write
the email.
