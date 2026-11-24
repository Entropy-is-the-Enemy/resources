# _Inbox: Reference

**Last updated:** YYYY-MM-DD (created during vault setup).
**Recurring files:** none. Files here are in transit and are not named in this reference.
**Purpose:** The only front door to the vault. New files land here; Claude files them out with <person's name>, group by group.
**State:** <"empty" or what is waiting>

## The inbox pass

Run these steps in order every time files are waiting. Nothing moves before <person's name> rules on it.

1. **Orient.** Read `00 Operating System/project-instructions.md`, the memory index, this file and `_Inbox/_LOG.md`.
2. **Inventory, read only.** List every file except `_REFERENCE.md` and `_LOG.md`. For each one:
   - Read enough to know what it is: email headers and body, spreadsheet sheets and headers, PDF text, media by metadata only.
   - Compute a file hash (`md5` or `md5sum`; `Get-FileHash` in PowerShell) and compare it with same-size files already in the vault (ignore `Archive/pre-setup-copy-*`). Only a matching hash proves a duplicate.
   - Propose a destination folder that already exists.
   - Flag anything sensitive: pay, personnel, health, customer personal data. A flagged file gets its own question in step 4 with three choices: file it like the rest, hold it in `_Inbox` (logged), or <person's name> takes it out of the vault themselves. Claude never deletes it.
   - List your questions.
   Move nothing in this step.
3. **Group and order.** Group by type and subject. Simple and time-sensitive groups go first.
4. **Review each group** with question cards. For each group show: what the files are (facts), what you infer (marked as inference), the proposed destination, the reference update it would make, and any fact from the files worth keeping in memory or in a folder's **State:** line, for a yes or no.
5. **Act.** Move with a command that refuses to overwrite (`mv -n`; `Move-Item` without `-Force` in PowerShell). Take a hash before and after each move, with the same hash command every time. Write every move in today's reorg manifest. Create a subfolder only when the group needs one, and give it its own `_REFERENCE.md`.
6. **Record.**
   - Name each filed file in its folder's `_REFERENCE.md` (unless the **Recurring files:** line covers it) and update that reference's **Last updated:** line. Update the folder's **State:** line only with what was confirmed in step 4.
   - Create any staged file whose trigger fired, per `00 Operating System/os-spec.md`.
   - Write durable facts the files revealed to memory, only after they are confirmed.
   - Add one entry to `_Inbox/_LOG.md`: the date, how many files, where they went, what was held and why.
   - Set this file's own **State:** line to what is still waiting, or "empty".
7. **Close.** Run `python3 "00 Operating System/Index Refresh/vault-index.py"`, then run it again with `--check`. The pass is done when `_Inbox` holds only `_REFERENCE.md`, `_LOG.md` and anything held on purpose (logged with the reason). Report open items in short lines.
