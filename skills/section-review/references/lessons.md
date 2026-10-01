# Lessons that recur

Read before the diagnosis is briefed; hand the relevant ones to the diagnosis agent as
constraints when the document family matches. Heuristics, not rules: the constraints file wins.

**Structure**

- A section that answers six questions reads worse than one that answers one. Put restatements
  and arithmetic under the table or figure they explain, not in the running prose.
- Describe the thing before the argument that depends on it. Working-note headings ("Findings",
  "Update") are not document headings.
- A bullet over about 60 words is carrying two ideas or an argument. Split it or make it prose.
- A restructure is where new errors come from. On deadline day, cut the two dead bullets and settle
  the contradictions before re-cutting thirty.

**Facts**

- Two figures on different bases are not a contradiction. Name the basis for each and let the
  author decide whether both belong.
- An unsourced figure usually has a source in the build logs, briefs, or audits. Grep the pack and
  the project before proposing to change it.
- Recompute from the printed figures, not from the source. The reader only has the printed ones.

**Mechanics and tooling**

- Inspect the file, not just the text dump, before calling a table column empty or a format wrong.
  Dumps drop images, shading, and merged cells.
- Match paragraphs by full visible text and rebuild them with their own properties. Never
  string-replace a number in raw XML: the same figure appears in other paragraphs and in tables.
- Clone the sibling's list style for new bullets; a new bullet with default properties renders as
  a different list.

**Process**

- Internal contradictions are the author's rulings, never the agent's guess. List them numbered.
- One diagnosis per section keeps the verdict honest; batching sections into one agent blurs it.
- Back up before the first edit, not before the second.
