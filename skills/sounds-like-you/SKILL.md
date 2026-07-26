---
name: sounds-like-you
description: >
  Edit a draft so it reads like a specific person wrote it, using four tests instead of a banned-word
  list: does the sentence change anything for the reader, is each suspect word earned or decorative,
  how many times does each rhythmic move repeat, and does the register match the situation. Counts the
  failures to decide whether to edit, rewrite, or stop and ask the writer. Also sets up voice transfer
  at the front of a task by pulling sample paragraphs and naming the reader, which works far better
  than describing a style in adjectives. Trigger on "make this sound like me," "this reads like AI,"
  "de-robot this," "tighten this," "rewrite this in my voice," "why does this feel off," or before any
  draft goes out under a human name. Returns a marked list of instance-level calls with reasons, not a global find and
  replace. This applies the writer's OWN voice; to apply a borrowed one deliberately, see
  narrative-register. Does NOT check facts, evaluate the argument, or help anything pass an AI
  detector.
---

# Sounds Like You

## What this skill does

The words are not the tell. **The tell is a word used where a plainer one would have done, a move
repeated until it becomes a mannerism, and a sentence that is there for no reason at all.** Those are
properties of an instance, not of a vocabulary. This pass never operates globally. It quotes each
occurrence and rules on it individually.

## Test 0: should this sentence exist

Before ruling on any word, ask one question of every sentence:

> What does the reader know well enough to act on, or do differently, because this sentence is here?

No answer, cut the sentence. This outranks the other three tests: no earned word, budgeted move, or
right register saves a sentence that changes nothing.

Second-order case: a sentence passes Test 1 word by word, then collapses into nothing once the
decorative words are gone. Delete or rewrite it rather than substituting again.

## Test 1: earned or decorative

For each suspect word or phrase, quote the sentence and ask one question:

> Would a plainer word lose real meaning here, or could it swap for a common verb with no loss?

If a plain substitute carries the same meaning, the original was decorative. Cut it. If the substitute
loses precision, the word was earned. Keep it, even if it appears on every banned-word list.

Two rules keep this honest:

- **Rule on instances, never on counts.** Four occurrences can be four rulings: one earned, three
  decorative. Quote all four.
- **Name the substitute you tested against.** A ruling of "decorative" is only checkable if you say
  what the plainer version was.

The same test applies to phrases. Constructions like "it is worth noting that" and "in today's
landscape" are almost always decorative, but run the test anyway.

## Test 2: frequency, not existence

The second tell is rhythm. The devices people warn about are not errors; they are moves.

**Used once, it is a move. Used twice in the same piece, it is a tic. Used three times, it is a
signature the writer did not choose.**

So count, do not ban. Devices worth counting:

| Move | What it looks like | Budget per piece |
|---|---|---|
| Rule-of-three closer | a list of three landing a paragraph or section | 1 |
| Balanced antithesis | "not X, but Y" as a sentence shape | 1 |
| Fragment sequence | two or more deliberate sentence fragments in a row | 1 |
| One-word punch | a single-word sentence for emphasis | 1 |
| Long dash aside | the em dash used to interrupt a sentence with an aside | 2 |
| Rhetorical question into answer | asking, then immediately answering | 1 |
| Colon reveal | a sentence that sets up and then delivers after a colon | 2 |

Count each move across the draft and report it against the budget. Over budget, keep the
strongest instance and rewrite the rest flat. Under budget, leave everything alone, including devices
a list would delete.

## Test 3: register match

Set the register before editing; half of what reads as wrong voice is right voice in the wrong room.
Define your own modes, five is usually enough, and fix three things for each: target length, opener,
closer.

| Mode | Length | Opener | Closer |
|---|---|---|---|
| Cold outreach to a stranger | Shortest. Under 150 words. | The reason you are writing, in the first sentence. No warm-up. | One specific ask with a date. |
| Status update to a group | Medium, scannable. | The headline outcome, before any narrative. | What each reader needs to do, if anything. |
| Public explainer | Longest. Room to build. | A concrete situation, not a definition. | The reader can now do or decide something. |
| Delivering bad news | Short. Shorter than feels right. | The news, in sentence one. No preamble, no cushion. | What happens next and who owns it. |
| Recommendation to a decision-maker | Medium. One page maximum. | The recommendation itself. | The consequence of not deciding. |

Every opener row also faces the clever-or-clear question in Write order below: a first line that
satisfies its row and still leaves a stranger guessing at the stakes fails.

**Replying, not initiating.** Every row assumes you set the temperature; in correspondence the other
person often set it first. If their message arrived warm or formal, match that level in your first
line, then start the substance on the next one. Matching outranks the opener rules for one line, and
one line only. The test for whether that line is real: it answers something they actually said or did.
"Thanks for turning the room list around so fast" is reciprocation. "Hope this finds you well" is a
template.

## Setting up voice transfer before drafting

**Voice does not transfer through description. It transfers through examples and through the reader.**

Describing a style in adjectives produces the average of every document described that way. Instead:

1. **Paste two or three paragraphs of the person's actual prior writing, in the target register.**
   Not their best writing. Their most typical writing in this mode; samples from the wrong mode
   mislead.
2. **Name the reader, specifically.** Not "a professional audience." A named role in a named
   situation: the subscriber who has attended for nine years.
3. **State what the reader should do or feel at the end.** One sentence; this sets the closer.
4. **Do not paraphrase the style rules.** If you have a register table, hand over the row. Do not
   translate it into adjectives.

## Write order

When producing a draft rather than repairing one, write in this order:

1. The substance: what happened, what you are asking for, what the reader has to decide.
2. The opening line, now that you know what it is opening.
3. Any summary line, if the piece still needs one once the body exists.
4. The closing move, taken from the register row.

The opening comes last because one written first promises something the body was never built to
deliver.

The opener has two jobs: give the reader a reason to feel something, and earn the next line. Can a
stranger tell what is at stake by the end of it, or is the line clever at the expense of clear?
Clever loses.

## Counting the findings into the call

One failure is any one of these: a move over budget (count the move, not each instance), a decorative
ruling, a register row that does not match (length, opener, and closer count separately), a sentence
cut for changing nothing. The total makes the call, not your patience.

- **Two or fewer.** Edit in place and ship as edited.
- **Exactly three.** The piece needs a rewrite, not an edit. Do not patch it.
- **Four or more.** Stop. Produce no draft at all. Ask the writer one question about what this piece
  is for, and wait.

## Output format

```
CUT FOR CHANGING NOTHING
  "<quoted sentence>"  ->  CUT. Reader knows nothing new, does nothing differently.
  "<quoted sentence>"  ->  CUT. Passed the word test, then said nothing.
  (kept separate from the decorative rulings below)

EARNED OR DECORATIVE
  "<quoted sentence>"
    Word: <the suspect>  Substitute tested: <the plain version>
    Ruling: EARNED because <what the substitute loses>
            or DECORATIVE, replace with <the substitute>
  (one block per instance, never per word type)

FREQUENCY
  <move>: <count> vs budget <n>  ->  keep <which instance>, flatten <which>
  <move>: <count> vs budget <n>  ->  within budget, no change
  Moves over budget: <n>  (<n> instances to flatten)

REGISTER
  Mode: <which one>
  Length: <actual> vs <target>
  Opener: <matches / does not, and what it does instead>
  Closer: <matches / does not>

CALL
  Failures: <n>  (<over-budget moves> + <decorative> + <register rows> + <cut for nothing>)
  Verdict: <ship as edited, 2 or fewer | rewrite section X, exactly 3 | stop, 4 or more>
  Question for the writer: <only when stopping, and then no draft>
```

## Worked example (invented)

**Input:** a model-drafted email telling season subscribers that next season moves to a different
building while the usual hall is repaired.

```
CUT FOR CHANGING NOTHING
  "Every organization faces moments like this one."  ->  CUT. No suspect word in it, so the
    word test passes it clean. Reader learns nothing, does nothing.
  "We are excited to leverage this transition to enhance the subscriber experience."  ->  CUT.
    With both swaps below made it says nothing; the vocabulary carried the claim.
    Delete, do not substitute again.

EARNED OR DECORATIVE
  "We are excited to leverage this transition to enhance the subscriber experience."
    Word: leverage   Substitute tested: use       Ruling: DECORATIVE, says the same thing.
    Word: enhance    Substitute tested: improve   Ruling: DECORATIVE, nothing is lost.
    Cut above, so it counts once there and not again here.

  "The Ardmore has better sightlines and will enhance every seat in the house."
    Word: enhance         Substitute tested: improve
    Ruling: EARNED, narrowly. "Improve every seat" is odd; the sentence is about the view
      from each seat. Better fix is rewriting it: "Every seat at the Ardmore has a clear
      view of the stage."
    Note: two rulings on "enhance," opposite directions, same draft.

  "It is worth noting that parking is available on Fourth Street."
    Phrase: it is worth noting that   Substitute tested: deleting it
    Ruling: DECORATIVE. "Parking is on Fourth Street."

FREQUENCY
  Rule-of-three closer: 3 vs budget 1  ->  keep the one closing the parking paragraph,
    genuinely three things. Flatten two that were padded to three for rhythm.
  Balanced antithesis: 2 vs budget 1  ->  keep "not a smaller season, a different room."
    Flatten "not an ending, but a beginning."
  Long dash aside 1 vs 2, one-word punch 0  ->  within budget, leave alone.
  Moves over budget: 2  (3 instances to flatten)

REGISTER
  Mode: delivering bad news, not status update.
  Length: 410 words vs target short. Over.
  Opener: no. Three sentences of gratitude first; the news lands in paragraph three.
  Closer: no. Ends on "we can't wait to see you there," which is uplift, not next steps.

CALL
  Failures: 8  (2 over-budget moves + 1 decorative + 3 register rows + 2 cut for nothing)
  Verdict: stop. No second draft yet.
  Question for the writer: is this an announcement subscribers have to act on, or a
    reassurance letter? It is trying to be both. Only then rewrite, from the substance
    out: venue change in sentence one, half the length, close on seat assignments and the
    response date.
```

## The standard covers your replies too

Everything above governs what you say about the draft, not only the draft. Two branches:

- **The writer gave a directive, or asked something answerable yes or no.** Answer in one line and
  stop. Agreement with reasoning bolted on is padding, and Test 0 applies to it.
- **The writer left the question open, or is visibly mid-decision.** Do not summarize the options in
  prose. Put two to four concrete alternatives in front of them, one line each, and ask which. Never
  more than four.

## Boundaries

This pass edits for voice. It does not check whether anything in the draft is true, evaluate whether
the argument holds, or decide whether the piece should be sent. Those are separate reviews.

It will not help a draft evade an AI-detection tool. The goal is prose a specific person would
actually have written, not prose that scores below a threshold on a classifier.

It also does not invent a person's voice from nothing. With no samples in the target register, the
honest output is a request for two or three paragraphs of their actual prior writing, not a guess
dressed up as a profile.
