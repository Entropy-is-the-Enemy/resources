# Operating system spec: staged files

These files are defined now and created on first use. When a trigger fires, create the file in `00 Operating System/`, name it in `00 Operating System/_REFERENCE.md`, and remove its row from this table.

| File | What it is for | Created when |
|---|---|---|
| `action-register.md` | One list of open action items, each with an ID like ACT-01, an owner and a due date | The first time a file or a meeting gives a task with a named owner and a due date. A task missing either one is asked about, not added; do not fill it in |
| `rulings-ledger.md` | Standing decisions about how the vault works, each with an ID like R-01 and a date, so they are not argued twice | The first time the person decides where a kind of file goes, or how something here is named or kept, in a way that will apply again (for example "vendor files go with appeals") |
| `Email Digests/` | Short summaries of filed emails, so the thread can be found without opening each message. One file per month, `email-digest-YYYY-MM.md`, holding a table: date, from, to, subject, one-line summary, where the email is filed. The folder has no reference or index of its own; add `Email Digests/*` to the **Recurring files:** line of `00 Operating System/_REFERENCE.md` | The first email is filed through the inbox |
| `vault-health.md` | The result of each tidy pass: what was checked, what was fixed | The first vault tidy pass |
| `vault-tidy-queue.md` | Items a tidy pass saw but put off, with the reason | The first item a tidy pass defers |
