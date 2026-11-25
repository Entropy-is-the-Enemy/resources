# _Inbox: Reference

**Last updated:** YYYY-MM-DD (created during vault setup).
**Recurring files:** none. Files here are in transit and are not named in this reference.
**Purpose:** The only front door to the vault. New files land here; Claude files them out with <person's name>, group by group.
**State:** <"empty" or what is waiting>

## The inbox pass

Run these steps in order every time files are waiting. Nothing moves before <person's name> rules on it.

1. **Orient.** Read `00 Operating System/project-instructions.md`, the memory index, this file and `_Inbox/_LOG.md`.
2. **Inventory, read only.** List every file except `_REFERENCE.md` and `_LOG.md`. For each one:
   - Look at the name first. If the name suggests anything sensitive (see the flag step below), stop there: read nothing but the name and, for a spreadsheet, its header row, and do not hash it, until <person's name> rules in step 4.
   - Otherwise read enough to know what it is: email headers and body, spreadsheet sheets and headers, PDF text, media by metadata only. For any spreadsheet, read the header row first; if it shows personal details, treat the file as flagged. Read files one at a time, not in one bulk command.
   - Compute a file hash (`shasum -a 256` or `sha256sum`; `Get-FileHash` in PowerShell) and compare it with same-size files already in the vault (ignore `Archive/pre-setup-copy-*` and any file the root `_REFERENCE.md` marks as set aside, which is never opened or hashed). Only a matching hash proves a duplicate.
   - Propose a destination folder that already exists. A file with no clear home is held in `_Inbox` and raised in step 4 as a question: is a folder missing, or does it not belong in the vault?
   - Flag anything sensitive: pay, personnel, health, personal data of customers, donors or clients, and anything a house rule protects. A flagged file gets its own question in step 4 with three choices: file it like the rest, hold it in `_Inbox` (logged), or <person's name> removes it from the vault. Claude never deletes it. Until they remove it, it stays in `_Inbox` as held, logged with the reason, and nothing from it is written anywhere.
   - List your questions.
   Move nothing in this step.
3. **Group and order.** Group by type and subject. Simple and time-sensitive groups go first.
4. **Review each group** with question cards, or with numbered plain-text questions and lettered options when there is no card tool. For each group show: what the files are (facts), what you infer (marked as inference), the proposed destination, the reference update it would make, and any fact from the files worth keeping in memory or in a folder's **State:** line, for a yes or no. "Not sure" counts as no: the fact is not confirmed.
5. **Act.** Move with a command that refuses to overwrite (`mv -n`; `Move-Item` without `-Force` in PowerShell). Take a hash before and after each move, with the same hash command every time. Write every move in today's reorg manifest. Create a subfolder only when three or more files of one kind land together or the folder's reference already plans it, and give it its own `_REFERENCE.md` and an index (`vault-index.py --create "<folder>"`).
6. **Record.**
   - Name each filed file in its folder's `_REFERENCE.md` (unless the **Recurring files:** line covers it) and update that reference's **Last updated:** line. Update the folder's **State:** line only with what was confirmed in step 4.
   - Create any staged file whose trigger fired, per `00 Operating System/os-spec.md`.
   - Write durable facts the files revealed to memory, only after they are confirmed. An unconfirmed fact is marked "unverified" on the file's line in the folder reference and stays out of memory.
   - Add one entry to `_Inbox/_LOG.md`: the date, how many files, where they went, what was held and why.
   - Set this file's own **State:** line to what is still waiting, or "empty".
7. **Close.** Run `python3 "00 Operating System/Index Refresh/vault-index.py"`, then run it again with `--check`. The pass is done when `_Inbox` holds only `_REFERENCE.md`, `_LOG.md` and anything held on purpose (logged with the reason). Report open items in short lines.
