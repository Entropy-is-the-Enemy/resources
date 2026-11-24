# Baseline rules

Apply these to every file you write during setup, starting with the first one. They also go, numbered, into the House rules section of `00 Operating System/project-instructions.md`, followed by the organization rules below and then the person's own rules from Round E.

## Default rules

1. **Plain punctuation, no em dashes.** Use commas, periods, colons, semicolons or parentheses. Files written this way read as the person's own and are easy to search.
2. **Absolute dates** (2026-11-23), never "yesterday" or "next week". A file is read months later, when relative dates no longer mean anything.
3. **Exact names.** Products, systems, teams and people are written the way the organization writes them, including capitals and symbols. Take the spellings from the person's answers and files; do not tidy them.
4. **Verify AI output.** Anything the person will rely on (a number, a recommendation, a message they send) is checked against its source first. Mark unverified claims as unverified.
5. **Plain Markdown only.** No `[[wikilinks]]` and no app-specific files or plugins, so the vault opens the same in any editor. (The short frontmatter block at the top of a memory file is plain text and is fine.) Point to other files with backticked paths relative to the vault root, like `00 Operating System/project-instructions.md`.

**Scope.** These rules govern the files in the vault. A message the person will send to someone else follows the person's own voice first: if they write "tomorrow" to their team, a draft for them can too.

**Dropping a default.** The person can drop or change a default in Round E. Leave a dropped rule out of the numbered list, stop applying it, and record it on one line under the list in the project instructions: "Dropped defaults: <rule> (YYYY-MM-DD)." The vault check reads that line.

## Organization rules

None set. In Round E, ask the person whether their organization has a mission or values statement, naming rules, or standards that all work must meet (brand, legal, compliance, faith, safety). Use what they give word for word. If they give none, write "not stated" and move on.

Each organization rule becomes its own numbered house rule, stated in full. A longer text (a mission statement, a values list) is quoted once in the root `_REFERENCE.md`, and the house rule points to it. If a rule depends on a document ("attach the safety checklist"), ask the person to put that document in `_Inbox` so it can be filed.

**For an organization rolling this skill out to its people:** replace the paragraph above with your own rules and any text that must be quoted exactly (a mission statement, product names, required standards). When this section holds rules, Claude applies them from the first file and does not ask the person for them.
