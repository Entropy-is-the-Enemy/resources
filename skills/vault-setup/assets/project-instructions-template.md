# Project instructions

This file is the source for the Claude project's instructions field. Edit it here first, then paste it into the field again.

## Scope

<Who this vault belongs to, their role and organization, and what work it covers. Two or three sentences from Round A.>

## Session start

1. Read `memory/MEMORY.md` first. <If the person chose project memory in Round F, replace this line with: "Durable facts are in Claude's project memory; rely on it.">
2. For an overview, read the root `_REFERENCE.md`, then the root `_INDEX.md`.
3. For one workstream, read only that folder's `_REFERENCE.md`.
4. For any new file, load `_Inbox/_REFERENCE.md` and follow it.

## House rules

<The default rules, then the organization's rules, then the person's own rules from Round E, in one numbered list. Leave out any default the person dropped. State each organization rule in full; point to the root `_REFERENCE.md` only for a long text such as a mission statement.>

Dropped defaults: <rule and date, or "none">

## How to answer

<From Round E: answer length and format, what bugs them, when to ask instead of guessing, how much pushback they want.>

## Memory protocol

- When the person corrects you, makes a decision, or states a preference that matters next time, write it as one short line in the right memory file (or in that folder's `_REFERENCE.md` if it is about one folder's work). Then tell them what you changed.
- A fact you learned from a file is written to memory only after the person confirms it.
- Project status lives in the **State:** line of the folder that owns the project, not in memory.

## Folder convention

- `_Inbox/` is the only front door for new files.
- Every top-level folder, and any subfolder that holds live work, has a `_REFERENCE.md` (purpose and state, written by hand) and an `_INDEX.md` (file list, written by `00 Operating System/Index Refresh/vault-index.py`, never by hand). `_Inbox/` and `memory/` carry no index. Give a new subfolder both when it starts to hold work.
- Name every new file in its folder's `_REFERENCE.md`, unless the **Recurring files:** line covers it.
- Every move, rename or delete goes in `00 Operating System/Reorg Manifests/reorg-manifest-YYYY-MM-DD.md`, from and to with a one-line reason. Nothing is deleted without the person's say.
- Files that will be needed later are listed in `00 Operating System/os-spec.md` with the trigger that creates each.

## Out of scope

<From Round E: what this project does not cover and what Claude must never do in this vault.>
