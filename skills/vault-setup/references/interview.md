# Phase 2: Interview

The interview is where the vault gets its shape. Thin answers produce a generic vault, so the aim is to get the person talking in their own words.

## How to run it

- Rounds A to D are open questions in chat, one at a time. Wait for each answer before asking the next. Tell the person once, at the start, that they can dictate.
- Round E is part cards and part chat; the round says which. Round F is one card.
- When a question the round needs gets no answer, record "not stated" and move on. Do not fill the gap yourself.
- Use what the person has already said to shape later questions and card options. Do not ask what you can already infer; say what you inferred and let them correct it.
- After each round, write a short recap in chat (3 to 6 lines for most rounds; Rounds C and E may need more, and nothing the person said should be dropped to fit) of what you heard, in their words where you can and adding nothing they did not say, so they can correct it. Put the corrected lines in the progress file under that round. Those lines are what a resumed chat works from.
- The bullets under each round are what the round must cover, not a script. Turn them into natural questions.

## Round A: Role and responsibilities

- Title and department.
- Who they report to.
- What they own.
- What they are measured on.
- What a good quarter looks like.

## Round B: Recurring work and cadence

- Reports, meetings, deadlines and reviews: daily, weekly, monthly, quarterly, yearly.
- Who receives each.
- Which ones eat the most time.
- Which ones they would gladly stop doing by hand.

These answers feed the skill suggestions in Phase 8 and the State lines of folders that hold recurring work, so note the exact tasks they name.

## Round C: Current projects

First ask for a list of what they are working on right now. Then go one project at a time:

- The goal.
- The deadline.
- Who else is involved.
- Where it stands.
- What done looks like.
- The files or links that matter.

These answers shape the folder tree and fill the **State:** line of each folder's `_REFERENCE.md`.

## Round D: People and systems

- Their team and the people they work with most (names and roles only).
- The systems they use (for example their order or finance system, a reporting tool, a CRM, Outlook or Gmail, Teams or Slack, SharePoint or Drive, Excel).
- Where files live today (desktop, network drive, SharePoint, email).
- Which of those systems Claude has a connector for in this session. You found this in Phase 0, so tell them rather than ask.

## Round E: Style and rules (one card, then chat)

On one card, because these have sensible options:

- How long and in what format they want answers (for example: a few bullets; short paragraphs; full detail with a summary on top).
- When Claude should ask instead of guessing (for example: always when a number, a date or a person is involved; only when the stakes are high; rarely, state the assumption and go).
- How much pushback they want before Claude agrees with a conclusion (for example: firm; some, then go with my call; little).

Shape the options from what you have already heard; these are starting points.

Then in chat, as open questions, because only the person knows the answer:

- Whether their organization has a mission or values statement, naming rules, or standards all work must meet. Skip this if `references/baseline-rules.md` already holds organization rules.
- Their own house rules on top of the baseline, and any default rule they want dropped.
- What bugs them in AI answers.
- Anything Claude must never do in this vault.
- Anything out of scope for this project.

Last, in chat, the writing sample:

1. Ask which kind of message they write most and most want Claude to get right: email, Slack or Teams messages, reports, or something else. Their choice; do not pick for them.
2. Ask them to paste one or two short samples of that kind, written by them.
3. Describe their style from the samples in plain words and ask them to confirm or correct the description. Keep the description, not the samples: it goes in the progress file now and in memory when the build creates it. If they do not confirm it, it is kept as unverified.
4. Tell them this is a first sketch, not a finished voice. It gets sharper each time they show Claude more of their real messages, and they can do that whenever they like. If a connector for the kind they chose is on in this session (from Phase 0), say that Claude could read a handful of their sent messages to refine it, and ask before reading any.
5. Mention the `sounds-like-you` skill in one line: it edits a draft so it reads like them, and it works from these samples. The link is in the skill's "Companion skills" table. Offer it; do not install anything.

## Round F: Memory location (one card)

Offer the project-memory option only if Phase 0 found a Claude project memory you can write to. If there is none, say in one line that memory will be kept as files in their folder, and why, and skip the card.

Otherwise explain the two options in the card descriptions, then let them pick:

- **Vault `memory/` folder:** durable facts are plain files in the vault (`memory/MEMORY.md` as an index plus one file per topic). The person can open, read and edit them. Claude's project memory holds only a pointer to the vault index.
- **Claude project memory:** the built-in store. Simpler, but the person cannot see it as files in their folder.
