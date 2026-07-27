# Entropy is the Enemy — Resources

Open resources for building **agentic operating systems**: reusable Claude *skills*, teaching guides, templates, and reference material.

If you follow [Entropy is the Enemy](https://entropyistheenemy.com), this is the companion library. Everything here is meant to be read, forked, and adapted to your own work.

## What's inside

| Folder | What it holds |
|---|---|
| [`skills/`](./skills) | Portable Claude skills, self-contained `SKILL.md` folders you can drop into Claude Cowork or Claude Code. |
| [`resources/`](./resources) | Guides, templates, handouts, and reference docs that stand alone (no skill runtime required). |

## What a "skill" is

A skill is a folder with a `SKILL.md` at its root: a named set of instructions that teaches Claude how to do one kind of task well. When the task matches, the skill loads and Claude follows it. Skills are just Markdown, so you can read every one before you use it.

See [`skills/README.md`](./skills/README.md) for how to install and use them.

## The skills

Twenty-four skills, grouped by what you are trying to get done. Every one is a single `SKILL.md` you can read start to finish in a few minutes.

### Writing and voice

| Skill | What it does |
|---|---|
| [`sounds-like-you`](./skills/sounds-like-you) | Edits a draft so it reads like a specific person wrote it, using four diagnostic tests instead of a banned-word list. |
| [`narrative-register`](./skills/narrative-register) | Rewrites named passages in a plain narrative-nonfiction register: concrete nouns, hard verbs, short propulsive rhythm. |
| [`draw-out`](./skills/draw-out) | Interviews the writer before drafting, one pointed question at a time, until there is real material to write from. |
| [`bones`](./skills/bones) | Strips a piece down to its load-bearing structure so it can be reused in another format without a rewrite. |
| [`edit-harvest`](./skills/edit-harvest) | Turns the diff between the draft and what you shipped into reusable corrections future drafts consult. |
| [`content-harvest`](./skills/content-harvest) | Scans work you have already done for moments worth posting about and files each as a structured idea card. |

### Review and verification

| Skill | What it does |
|---|---|
| [`airtight`](./skills/airtight) | Forces every load-bearing claim into one of three states (verified, confidently stated, flagged) before a document goes out. |
| [`trace-review`](./skills/trace-review) | A five-point quality-control pass on AI output: Truth, Relevance, Accuracy of tone, Completeness, Ethics and risk. |
| [`red-team-reflex`](./skills/red-team-reflex) | Attacks a persuasive document as its harshest credible reader, then triages down to the one objection that flips the decision. |
| [`hard-look`](./skills/hard-look) | States the strongest objection to a call you are about to make, before agreeing with any of it. The counter to sycophancy. |

### Building and testing AI tools

| Skill | What it does |
|---|---|
| [`deploy-method`](./skills/deploy-method) | Four sequential gates before an AI tool reaches real users: intake, pilot design, measurement spec, governance. |
| [`eval-author`](./skills/eval-author) | Generates an edge-weighted regression suite for a skill or prompt kit, with falsifiable criteria rather than expected outputs. |
| [`eval-scorer`](./skills/eval-scorer) | Runs an existing suite against a live skill and returns a scorecard, variance across runs, and clustered failure patterns. |
| [`sub-agent-ops`](./skills/sub-agent-ops) | Picks the architecture for an orchestrated agent run, seals the worker packets, and spawns on your confirmation. |

### Thinking and decisions

| Skill | What it does |
|---|---|
| [`scales`](./skills/scales) | Routes a plan through a fixed set of mental-model laws, firing only the two to four whose signature is actually present. |
| [`line-by-line`](./skills/line-by-line) | Builds a high-stakes deliverable end-first, one walkable unit at a time, when a wrong structure is expensive to unwind. |

### Work systems

| Skill | What it does |
|---|---|
| [`tasks-of-record`](./skills/tasks-of-record) | A task system where one plain-text file is the source of truth and every app is a read-only mirror of it. |
| [`signal-three`](./skills/signal-three) | Exactly three must-finish items a day, at least 70% of effort on them, nothing displacing them until they are done. |
| [`handoff`](./skills/handoff) | Captures full session context into a continuation document so a new chat picks up without loss. |
| [`kb-integrate`](./skills/kb-integrate) | Merges new material into a reference knowledge base the way you would merge code: collisions first, one concept per file. |
| [`send-imessage`](./skills/send-imessage) | Sends an iMessage from your own Mac through a computer-use bridge, with a confirm gate and screenshot verification. |

### Acquiring and running a business

| Skill | What it does |
|---|---|
| [`buying-a-business`](./skills/buying-a-business) | The non-financial half of a small acquisition: sourcing, opening the price conversation, and the first hundred days. |
| [`acquisition-screen`](./skills/acquisition-screen) | Screens a target's financials against a size-banded rubric and returns a verdict a lender or partner could follow. |
| [`post-session-qualify`](./skills/post-session-qualify) | Grades a lead on what they did after a free session, not what they claimed on an intake form, and routes them explicitly. |

## How to use these

1. Browse the folders and open any `SKILL.md` or guide directly. They're plain Markdown.
2. To use a skill in Claude, copy its folder into your skills directory (see the skills README).
3. Adapt freely. These are starting points, not gospel. The whole point is that you make them yours.

## Contributing

Issues and pull requests are welcome. If you've adapted a skill and it works better for you, open a PR so others benefit.

## License

Released under the [MIT License](./LICENSE) unless a specific file says otherwise. Use it, change it, ship it.
