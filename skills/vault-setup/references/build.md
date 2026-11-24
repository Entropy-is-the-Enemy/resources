# Phase 5: Build

Build only the tree the person approved in Phase 4. Say what you are doing as you go, in short lines. Templates are in this skill's `assets/` folder: copy each one, then fill in every `<placeholder>`. Leave no placeholder behind.

## Contents

1. Make the fixed folders
2. Protect and place what was already there
3. Create the core files
4. Stage the files that come later
5. Indexes last
6. Close the phase

## 1. Make the fixed folders

Create the approved subject folders, plus `_Inbox/`, `Archive/`, `memory/` (only if the person chose the vault option in Round F) and `00 Operating System/` with these inside it: `Handoffs/`, `Templates/`, `Reorg Manifests/`, `Index Refresh/`. `Templates/` stays empty; it is for the person's own document templates later.

Start today's reorg manifest now, from `assets/reorg-manifest-template.md`, at `00 Operating System/Reorg Manifests/reorg-manifest-YYYY-MM-DD.md`. Every move in this phase gets a row.

## 2. Protect and place what was already there

Skip this section if Phase 0 found the folder empty. "What was already there" means every file and folder Phase 0 listed. It does not include the progress file or anything you created.

1. **Ask about sensitive files first.** If Phase 0 named any file that looks sensitive, ask about each before anything is copied: leave it where it is and out of the copy, or treat it like the rest. A file the person says they will remove is left alone, noted under Open items, and never opened.
2. **Copy, with a yes.** Tell the person you will copy everything else that was already there, as it is, into `Archive/pre-setup-copy-YYYY-MM-DD/`, and do it on their yes, keeping file dates (`cp -Rp` on Mac and Linux; `Copy-Item -Recurse` or `robocopy /E /COPY:DAT` on Windows). Tell them the copy is on purpose: for a while some files exist twice, once in the copy and once where they are filed. They can remove the copy later. If it is too large to copy sensibly, tell them the size and ask what to do.
3. **Files at the folder root:** propose moving each into `_Inbox/`, so it is filed properly in Phase 8.
4. **Folders that were already there:** for each one, offer two choices: move the whole folder into `Archive/` as it is, or move its files into `_Inbox/` to be filed in Phase 8. If its files go to `_Inbox/`, the emptied folder moves into `Archive/` too; it is not deleted.
5. Ask about steps 3 and 4 with a question card, or more than one if there are many folders. Move only what the person approves, with a move that refuses to overwrite (`mv -n` on Mac and Linux; `Move-Item` without `-Force` in PowerShell), and give every move a row in the manifest. After each move, confirm the file is at the new path and gone from the old one; some systems skip a refused move without an error.

Anything the person chooses to leave where it is stays there. Note it under Open items in the progress file.

## 3. Create the core files

1. **A `_REFERENCE.md` in every top-level folder except `memory/`** (its `MEMORY.md` does that job), from `assets/reference-template.md`. Fill each **State:** line from the Round C answers, in the person's words; for a folder that holds recurring work, the Round B cadence is a fair state ("weekly, built by hand every Friday"). Where they said nothing, write "not stated yet"; a guessed state is worse than an empty one because later sessions will trust it. In `00 Operating System/_REFERENCE.md`, set **Recurring files:** to cover `Handoffs/*`, `Reorg Manifests/reorg-manifest-*.md` and `Index Refresh/*`, so those need no line each.
2. **Root `_REFERENCE.md`:** owner (the person), the **Last updated:** line, a **Purpose:** line saying what the vault is for, the organization's mission or standards word for word (from `references/baseline-rules.md` or the Round E answer; "not stated" if neither gave any), and a table of top folders with one-line purposes. The root needs no **State:** line; each folder carries its own. Its Files section lists the files that sit at the root, including any the person chose to leave there.
3. **`00 Operating System/project-instructions.md`**, from `assets/project-instructions-template.md`. This is the canonical text for the Claude project's instructions field. House rules are the default rules, then the organization's, then the person's Round E rules, numbered in one list, with dropped defaults handled as `references/baseline-rules.md` says.
4. **Root `CLAUDE.md`**, from `assets/claude-md-template.md`. Its house style line is the short form of the rules as they ended up: no dropped default, and the organization's and the person's rules included.
5. **`_Inbox/_REFERENCE.md`**, from `assets/inbox-playbook.md` (swap in the Python, move and hash commands that work on this computer, from Phase 0), and **`_Inbox/_LOG.md`** with a title line and nothing else yet.
6. **Memory, per the Round F answer.** Do one of the two options, not both.
   - **Vault option.** Write one file per topic the interview covered: role, team, systems, cadence, writing style. Use short lowercase names like `role.md`. Each file starts with frontmatter: `name`, `description`, `type`: `user` for facts about the person (role, team), `feedback` for how they want work done (writing style), `reference` for where things are (systems, cadence), `project` for anything else tied to their work. Then write `memory/MEMORY.md` as the index: one line per memory file, with its backticked path and what it holds. Last, and only under this option: if this session has a Claude project memory you can write to, write its `MEMORY.md` as a pointer only: "Not canonical. Read the vault's `memory/MEMORY.md` first; write all memory there." If it has none, skip the pointer and note it under Open items.
   - **Project-memory option.** Write the same facts to Claude's project memory and do not create `memory/`. Write no pointer. If this session turns out to have no project memory you can write to, tell the person, and ask whether to use the vault option instead; do not drop the facts.
   - Under either option, each fact has one home. The person's rules and how they like answers live in `project-instructions.md`, not in memory. Project status lives in the **State:** line of the folder that owns the project.
   - The writing-style entry records which kind of message the samples came from and the date, and ends with one line: "Refine this whenever <person's name> shares more of their own messages."
   - A description the person has not confirmed (for example the writing-style description) is written with "unverified" in its first line and listed under Open items.
7. **The index script.** Copy `scripts/vault-index.py` from this skill to `00 Operating System/Index Refresh/vault-index.py`. Copy it; do not rewrite or retype it, because the bundled copy is the tested one. It finds the vault root from its own location, so it must sit exactly there.
8. **The progress file and early handoffs.** Move `_setup-progress.md` from the root to `00 Operating System/setup-progress.md`, and any `_setup-handoff-*.md` at the root into `00 Operating System/Handoffs/`, with a move that refuses to overwrite. Give each move a row in the manifest. The handoff keeps its name.

## 4. Stage the files that come later

Copy `assets/os-spec.md` to `00 Operating System/os-spec.md`. It lists files the vault will need later, each with the trigger that creates it. Do not create the staged files themselves. An empty register or ledger teaches the person nothing and clutters the first look at their vault.

## 5. Indexes last

Create the indexes after every other file exists, so they are correct the moment they are written.

Give an `_INDEX.md` to the root and to every top-level folder except `_Inbox/` and `memory/`, which carry no index:

    python3 "00 Operating System/Index Refresh/vault-index.py" --create "<folder>"

Use `--create .` for the root. Subfolders get a `_REFERENCE.md` and an `_INDEX.md` when they start to hold live work, not before.

**If Python is not available on the computer:** say so, write each `_INDEX.md` by hand in the same format (a title line, then the file list between `<!-- files:start -->` and `<!-- files:end -->`, subfolders first with a trailing slash, each name in backticks), and note in `00 Operating System/_REFERENCE.md` that indexes are kept by hand for now. The script stays in place for when Python arrives.

## 6. Close the phase

1. Run the index script, then run it again with `--check`. It must report nothing stale.
2. Run the vault check from this skill's folder: `python3 scripts/check-vault.py "<path to the vault>"`. Fix every ERROR line and run it again until it passes. Read each WARNING and fix it or tell the person why it stands.
3. Tell the person both checks passed, or exactly what failed. Do not report the build as done while either check fails.
4. Tick Phase 5 in the progress file.

Without Python, do step 2 by hand: walk the checklist at the top of `scripts/check-vault.py` and tell the person it was a manual check.
