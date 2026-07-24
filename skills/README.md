# Skills

Each subfolder here is a self-contained Claude skill: a `SKILL.md` file (and any supporting files) that teaches Claude how to do one kind of task well.

## Anatomy of a skill

```
skill-name/
└── SKILL.md      # name, description, and the instructions themselves
```

The `SKILL.md` opens with a short frontmatter block — a `name` and a `description` that tells Claude *when* to use the skill — followed by the instructions.

## Using a skill

**Claude Code / Cowork:** copy the skill folder into your skills directory so Claude can discover it. Claude reads the `description` to decide when the skill applies, then follows the `SKILL.md` when the task matches.

**Any Claude chat:** you can also just open a `SKILL.md`, copy its contents, and paste it in as instructions for a one-off task. Skills are plain Markdown — nothing is hidden.

## Writing your own

Start from [`_template/SKILL.md`](./_template/SKILL.md). The two things that make a skill work:

- A **description** that names the concrete triggers ("use when the user asks to X, mentions Y…"). This is what decides whether the skill fires.
- **Instructions** that are specific enough to change behavior — steps, rules, and examples, not vague advice.

Keep skills scoped to one job. A skill that tries to do everything fires for nothing.
