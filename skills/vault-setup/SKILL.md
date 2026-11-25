---
name: vault-setup
description: Sets up a working vault for one person in the local folder connected to their Claude project, so every later session can pick up their work without a re-brief. Looks at the folder, interviews the person about their job, proposes a numbered folder tree, builds the operating files (references, indexes, memory, rules), files their first batch of documents through an inbox, and finishes with one real task from their week. Use when someone says "set up my vault", "set up my folder", "set up my Claude project", "organize my work folder for Claude", "get me started with Claude", "onboard me", or asks to continue, resume or finish a vault setup started in an earlier chat. Also use when a connected work folder has no `00 Operating System` folder and the person asks Claude to get it ready for ongoing work. Not for routine inbox filing in a vault that is already set up; that vault's own `_Inbox/_REFERENCE.md` covers it. Not for code repositories.
---

# Vault setup

Set up a working vault for one person, in the local folder connected to their Claude project. A vault is a folder system plus an operating system (rules, orientation files, memory, logs) that lets every later Claude session pick up the person's work without them explaining it again.

Assume the person has set up nothing and is new to this. Before each step, say in one or two plain sentences what you are about to do and why.

## What it produces

    <work folder>/
    ├── 00 Operating System/   rules, handoffs, manifests, index script, setup progress
    ├── 01 ... NN ...          numbered folders named for this person's job
    ├── _Inbox/                the only front door for new files, with its own playbook
    ├── memory/                durable facts about the person and their work
    ├── Archive/               untouched copy of whatever was there before
    ├── CLAUDE.md              pointer to the rules every session reads first
    ├── _REFERENCE.md          what the vault is for (one per folder, written by hand)
    └── _INDEX.md              full file list (one per folder, written by a script)

## Three promises (they hold for the whole setup)

These are the person's real work files and the folder has no version history, so a wrong move cannot be undone by anyone but you.

1. **Nothing is deleted.** Not during any phase, not to tidy up.
2. **Nothing moves and nothing is built without the person's approval.** The folder tree is approved in Phase 4; every file move is approved before it happens and written in a reorg manifest after.
3. **Nothing is invented.** No number, name, source or date that the person or a file did not give you. If you are guessing about their job or situation, say it is a guess and ask.

## Start here: new setup or resuming

Look for a progress file in the connected folder: `00 Operating System/setup-progress.md`, or `_setup-progress.md` at the folder root (where it lives before Phase 5 builds the folders).

- **Found:** read it, then the newest handoff if there is one (in `00 Operating System/Handoffs/`, or `_setup-handoff-*.md` at the folder root if the build has not happened yet), then the memory index if it exists. Tell the person in two lines where they stopped. Then, before continuing at the first phase not ticked:
  - Redo the Phase 0 tool checks (steps 3 to 5). They describe a session, not the folder, so the earlier answers may no longer hold.
  - Settle the progress file's Open items that the next phase depends on. To know which, read that phase's "Read first" file now (for the build, `references/build.md`).
  - Do not ask again about a sensitive-looking file the progress file already records a ruling for.
  - If the progress file and the handoff disagree, say so and ask; until the person answers, the more careful of the two holds.
  - If the next phase is the build, show the approved tree from the progress file and get a one-word confirmation. The approval was given in a chat you cannot see.
  - Do not repeat interview questions the progress file already answers. If a ticked phase records "not stated" for something that was only an offer (such as explaining a part again), make the offer once and move on.
- **Not found:** this is a new setup. Open with a short message that covers these points, then begin Phase 0:
  - What happens: you look at their folder, interview them about their job, show a folder plan, build it once they approve, file their first batch of documents with them, then do one real task from their week.
  - They can stop at any point; progress is saved so a new chat picks up where they stopped.
  - Good to have ready: a short sample of their own writing (an email or a report) and a rough list of what they are working on now.
  - They can type or dictate. Longer answers in their own words give you more to work with.
  - The three promises above, in plain words.

Do not quote how long setup takes; no one has timed it.

## How to talk to the person

There are three ways of asking. Pick by what the step needs.

- **A step that shows a visual** (folder tree, diagram, summary): put the visual and its question in chat, then stop and wait for a typed reply. Do not open a question card in the same turn. The card covers the chat, so the person cannot see the visual while answering.
- **A question about their job with no sensible set of options** (most of the interview): ask it in chat as an open question, one at a time, and wait for the answer before the next. Keep it short and give an example answer if it helps. If the answer is vague, ask one follow-up.
- **A choice with no visual:** use the question card tool (AskUserQuestion): up to 4 questions per card, 2 to 4 options each, your recommended option first and marked "(Recommended)". Each question must make sense on its own, without the chat above it. If the card tool is not available, ask in plain text with numbered questions and lettered options, so they can reply like "1A 2C".

For visuals, use an inline visual or diagram tool if you have one; otherwise a Mermaid diagram or a plain-text tree in a code block. Write short lines, with no preamble and no filler.

## House rules

Read `references/baseline-rules.md` before you write any file, and apply it to every file you write. It holds five default rules (no em dashes, absolute dates, exact names, verify AI output, plain Markdown only) and a section for the organization's own rules. The person adds their rules in the interview. Rules stack in that order: defaults, organization, person. Where two conflict, the later one wins, and the project instructions say so next to the rule (for example a person's "donors by ID, not name" over the default on exact names).

## Progress file and handoffs

Setup is long, and long chats lose early detail. Two things protect against that.

- **Progress file.** At the end of Phase 0, tell the person you are adding one file to track setup, and create `_setup-progress.md` at the folder root from `assets/setup-progress-template.md`. Tick each phase as it closes, add the recap lines it asks for, and add a line under Phase notes for anything a later chat would need. Phase 5 moves it to `00 Operating System/setup-progress.md`.
- **Handoffs.** Run the `handoff` skill whenever the person stops for the day, any time the chat is getting long or your memory of earlier answers is slipping (say so plainly), and at the end of Phase 9. The ends of Phase 4, Phase 6 and Phase 8 are good places to offer a stop. A small vault can finish in one chat; do not force a restart that is not needed. Save handoffs in `00 Operating System/Handoffs/`. Before Phase 5 that folder does not exist yet, so save the handoff at the folder root as `_setup-handoff-YYYY-MM-DD.md`, next to the progress file; Phase 5 moves it, keeping its name. A second handoff on the same day adds a letter (`-b`). After a handoff, tell the person what state the folder is in (for example "nothing is built yet; two new files hold your progress") and to start the next phase in a fresh chat with the handoff prompt. After Phase 9 there is no next phase: the prompt is a general one for continuing work in the vault.
- **No handoff skill.** Write the handoff by hand in the same place and under the same name rule: `_setup-handoff-YYYY-MM-DD.md` at the folder root before Phase 5, `handoff-YYYY-MM-DD-phase-N.md` in `00 Operating System/Handoffs/` after it. It holds: where setup stands, what was decided in this chat, the open items, and a short prompt the person can paste into a new chat that says to continue the vault setup and read the progress file first.

## The phases

Work through the phases in order. Do not skip ahead.

| Phase | What happens | Read first |
|---|---|---|
| 0 | Look before touching | (below) |
| 1 | Get the handoff skill | (below) |
| 2 | Interview | `references/interview.md` |
| 3 | Explain how the vault works | (below) |
| 4 | Propose the folder tree | (below) |
| 5 | Build | `references/build.md` |
| 6 | Paste the project instructions | (below) |
| 7 | Summary and the inbox drop | (below) |
| 8 | First inbox pass | the vault's `_Inbox/_REFERENCE.md` |
| 9 | First real task | (below) |

### Phase 0: Look before touching (one question at most)

1. Find the connected folder and list its top two levels. Tell the person in short lines what is already there. List only: do not open the files yet, and do not create test files to probe the folder. If a file name suggests pay, personnel, health or personal details of customers, donors or clients, name it and say you will ask about it at the end of this phase, before anything is copied or moved. Do not open, read or hash such a file.
2. Say in one line where the folder sits: on the computer's own drive, on a network drive, or in a synced folder (OneDrive, SharePoint, Google Drive, Dropbox). If you cannot tell from the path, ask. If it is a network drive, say so plainly and ask before going on. Claude may not work reliably there; a folder on the computer's own drive, with the network copy kept as the backup, may be the better setup.
3. Check your tools, one line each: can you run commands in that folder, or only read and write files? Is Python 3 available (try `python3 --version`, `python --version`, then `py --version`; work computers often do not have it)? Which shell do commands run in? Record the Python command that worked, the shell and its file-hash command in the progress file; every later command, including the ones you write into the vault's own files, uses those and not the examples printed in this skill.
4. Check whether the `handoff` skill is available in this session, whether the person is working in a Claude project (Phase 6 depends on it; ask in Phase 2 if you cannot tell), and whether the session has a Claude project memory you can write to (Round F depends on it).
5. List the connectors this session has (email, chat, calendar, file storage, CRM and so on), in one line.
6. If the folder already holds files, do not move them. Phase 5 handles them.
7. Create the progress file (see above) and record what you found.
8. If step 1 named any sensitive-looking file, ask about each one now, the only question of this phase: leave it where it is and out of everything (a **set-aside file**: never opened, copied or moved), or treat it like the rest. Say that a set-aside file's name will still show in the vault's root file list for as long as it sits in the folder; only its name, never its contents. If the person is not sure about a file, or you are not sure whether a name counts as sensitive, the file is held as set aside until they rule. Record each ruling in the progress file.

### Phase 1: Get the handoff skill

Explain why in two sentences: setup is long, and the `handoff` skill writes a handoff document and a ready-to-paste prompt so a fresh chat continues exactly where this one stopped.

If `handoff` is not available, walk the person through turning it on from the skills list in their Claude settings. It is not something to build. If you are not certain of the exact menu path in their app, say so and describe what to look for. Wait until they confirm it is on. If they are not sure how, or would rather not do it now, do not press: continue, write handoffs by hand, and say in one plain line at the first stop that the skill can still be turned on later.

If it is not in their organization's list, give them the public copy: https://github.com/Entropy-is-the-Enemy/resources/tree/main/skills/handoff. They download the `handoff` folder, zip it, and add it under Skills in their Claude settings. Tell them to read the `SKILL.md` first; a skill is instructions Claude will follow, so it deserves the same care as installing software. If their organization does not allow adding skills, or it still does not appear, continue, and write handoffs by hand at the checkpoints (see "Progress file and handoffs").

### Phase 2: Interview

Follow `references/interview.md`. Most of it is open questions in chat; the few real choices go on question cards. After each round, recap in chat and in the progress file.

### Phase 3: How the vault works (visual, in chat)

Show one diagram of the operating system with a caption of one or two short lines per part:

- `_Inbox/`: the only front door. New files go here; Claude files them out with the person.
- `_REFERENCE.md` in every working folder: what the folder is for and its current state, written by hand.
- `_INDEX.md` in every working folder: the full file list, written by a script, never by hand.
- `memory/` (or project memory, per the Round F answer): durable facts about the person and their work.
- `00 Operating System/`: rules, handoffs, templates, manifests, logs.
- Reorg manifests: the undo record for every move, rename or delete, because the vault has no version history.
- `CLAUDE.md` plus the project instructions: the rules every session reads first. (If the person is not in a Claude project, say `CLAUDE.md` and the rules file it points to.)

Ask: "Does this make sense, or should I explain a part?" Wait for the reply.

### Phase 4: Propose the folder tree (visual, in chat)

From the interview answers, propose the top-level folders:

- `00 Operating System` always comes first.
- Then the numbered subject folders, `01` to `NN`: two-digit number, a space, then a name drawn from this person's job (the work they own, the people they serve, the reports they produce). Most jobs need 6 to 11; a narrow role may need fewer, and a folder with nothing to hold should not be added to reach a count. Order them by how much of the person's working time each holds, judged from Round B (what recurs and what eats the most time), and say the order is a first guess they can change.
- Plus `_Inbox`, `memory` (only if they chose the vault option in Round F), and `Archive`.
- Under each subject folder, at most 2 to 4 likely subfolders, marked "create when needed".
- Folders that were already there in Phase 0 are not part of the tree. Say in one line that Phase 5 will copy them first (leaving out any set-aside file from Phase 0) and then ask where each goes.

Example names, for shape only and not to copy: `01 Leadership & Planning`, `02 Campaigns`, `03 Monthly Reporting`, `04 Customers`, `05 Vendors & Partners`.

Show it as a tree with one line of purpose per folder. The tree shows folders only; the files setup adds at the root (`CLAUDE.md`, `_REFERENCE.md`, `_INDEX.md`) were covered in Phase 3. Ask the person to reply "approved" or say what to rename, merge, split or reorder. Iterate until they approve. Build nothing before that.

### Phase 5: Build

Follow `references/build.md`. Say what you are doing as you go. The phase closes only when the index check and the vault check both pass. Go straight on to Phase 6; it is short and is a better place to stop.

### Phase 6: Paste the project instructions

You cannot edit a Claude project's settings. Paste the full text of `00 Operating System/project-instructions.md` in chat in one code block, tell the person where to paste it (this Claude project's instructions field), and ask them to reply "pasted". Explain in one line that later edits happen in the file first and are then pasted again, so there is one source.

If the person is not working in a Claude project (Phase 0 recorded this; for example Claude Code, where there is no instructions field), skip the paste: the root `CLAUDE.md` already points every session at the file. Say so in one line. Tick the progress file.

From here on, any change to `project-instructions.md` (a new house rule in Phase 8, for example) ends with asking the person to paste it again.

### Phase 7: Summary and the inbox drop (visual, in chat)

Show a final summary visual: the tree as built, the core files created, the staged files waiting for their trigger, and where memory lives. Then tell the person, plainly:

> Your vault is ready. Now drag the files you work with most into `_Inbox`: recent reports, trackers, key emails saved as files, planning documents, anything you open every week. Start with 10 to 30 files, not everything. For now, leave out anything with pay, personnel, health or customer personal details; we will decide together where those belong. Reply "done" when they are in.

If Phase 5 already moved files into `_Inbox`, say so: those are waiting and count toward the first batch, and adding more is optional. Wait for "done".

### Phase 8: First inbox pass (with the person, group by group)

Follow the playbook you built in Phase 5, `_Inbox/_REFERENCE.md`, step by step. Using the vault's own copy on its first real run is the test that the playbook works without this skill.

One addition for this first pass. When the pass closes, suggest in one line each up to 3 recurring tasks from the Round B answers that could become skills later. Suggest only tasks that pass all three tests: the task repeats, it takes several steps or several files, and the person said they would gladly stop doing it by hand. Do not build them now. A task becomes a skill only after it has worked twice by hand, because a skill written before the task is understood locks in the wrong steps. Then run the vault check from this skill's folder (`scripts/check-vault.py`, with the vault path), fix or explain what it reports, and tick the progress file.

### Phase 9: First real task (the payoff)

1. **Pick:** with a question card, ask the person to pick one task from their week that the filed files can support. Offer 2 to 4 small ones you can see in the files, each doable in one sitting; a slice of a Phase 8 suggestion can be one of them. They can also name their own.
2. **Goal:** ask in chat for the task as one goal: what done looks like and which files it needs.
3. **Do it:** read memory and the relevant folder's `_REFERENCE.md` first, then do the task. Put the source (a backticked file path) next to every claim. If no file supports something, say so. If a file seems to contradict how the person framed the task, do what they asked and flag the mismatch. Save the result in the folder that owns the work, in one of the tree's "create when needed" subfolders if it fits one; a new subfolder gets its `_REFERENCE.md` and its index (`--create`). When the result is something the person will send or print, keep its text clean and list the sources under a divider below it. Where a sentence needs a fact no file gives, leave a marked gap like `[needs: who signs for the parish]` and list the gaps; a gap the person fills in a minute is better than a smooth line that hides what is missing.
4. **Check one claim:** ask the person to open one source file and confirm it says what you said. Name a claim worth checking if they ask. This is how they learn the habit behind the "verify AI output" rule.
5. **Record:** write any correction they give per the memory protocol (a confirmed number or status is project state and goes in the folder's `_REFERENCE.md`, not memory); name any new file in its folder's `_REFERENCE.md`; run the index script and `--check`, then the vault check.
6. Tick the progress file and run the handoff skill so their next session starts warm.

## Companion skills

Three public skills pair with the vault. None is required; setup works without them.

| Skill | What it adds | Where it comes up | Link |
|---|---|---|---|
| `handoff` | Writes a handoff document and a paste-ready prompt so a new chat continues where this one stopped | Phase 1 and every checkpoint | https://github.com/Entropy-is-the-Enemy/resources/tree/main/skills/handoff |
| `sounds-like-you` | Edits a draft so it reads like the person wrote it, working from samples of their real writing | Round E of the interview, and any later draft that goes out under their name | https://github.com/Entropy-is-the-Enemy/resources/tree/main/skills/sounds-like-you |
| `intake-filing` | Empties a drop folder and inbox into the right records, one group at a time, for routine filing after setup | Any time after Phase 8, alongside the vault's own inbox playbook | https://github.com/Entropy-is-the-Enemy/resources/tree/main/skills/intake-filing |

## Bundled files

- `references/baseline-rules.md`: the default rules and the slot for an organization's own rules. Read before writing any file.
- `references/interview.md`: the six interview rounds. Read at Phase 2.
- `references/build.md`: what to create, in what order, and how to close the build. Read at Phase 5.
- `assets/`: templates to copy and fill in (references, project instructions, `CLAUDE.md`, inbox playbook, staged-file spec, reorg manifest, progress file). `references/build.md` says which goes where.
- `scripts/vault-index.py`: writes every `_INDEX.md`. Copy it into the vault in Phase 5 and run it there; do not rewrite it.
- `scripts/check-vault.py`: checks a vault against this setup's rules, including subfolders and whether each file is named in its folder's reference. Run it from this skill's folder with the vault path, at the end of Phases 5, 8 and 9.
