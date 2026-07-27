---
name: handoff
description: Create or update a session handoff document that captures full conversation context so a new chat can continue without loss. Use this skill whenever you say "handoff", "create a handoff", "update the handoff", "save context", "session summary", "continuation doc", "wrap up this session", "prep for next chat", "pick up where we left off", or any variation of wanting to preserve the current session's state so a new chat can resume seamlessly. Also trigger when you say you're running out of context, are about to start a new session, or want to carry work forward. This is a project continuity system - any signal that you want to preserve session state for later should trigger this skill. If in doubt, trigger.
---

# Handoff Skill

Create or update a handoff document (`.md`) that captures everything from the current session so a new chat can continue without loss of context.

## Why This Matters

Paste the prompt, attach the doc, and the new session is already up to speed; without it the next session starts cold.

## Step 1: Detect Existing Handoff

Before writing anything, look for an existing handoff doc so you update it rather than starting a new one from scratch. Check three distinct places, in this order:

1. **Where attached or handed-in files land** - the location this session exposes files you attached or uploaded. Check this first: a prior handoff is most often carried forward as an attachment rather than found on disk, which makes this the highest-yield place and the easiest one to skip.
2. **Where this skill writes its outputs** - the folder handoff docs get saved to.
3. **Where durable project reference is kept** - the folder holding long-lived project notes.

A search for filenames containing "handoff" across all three is usually enough. Do not conclude that no prior handoff exists until all three have been checked.

- **If one exists:** Read it. You're updating, not creating from scratch. Preserve stable sections and layer in new work.
- **If none exists:** Create a new one by auditing the full conversation.

## Step 2: Audit the Conversation

Before writing, systematically extract from the conversation:

1. **Decisions made** - What was decided, what was rejected, and why
2. **Work completed** - Specific outputs, record counts, files created, commands run
3. **System state** - IDs, configurations, mappings, API patterns, credential references (never actual secrets)
4. **Open threads** - Unfinished work, unresolved questions, known issues
5. **Files** - Everything created or modified, with locations and purposes

This audit is the source of truth. Every claim in the handoff must trace back to something actually discussed. Invent nothing.

## Step 3: Write the Handoff

Use the template below. Not every section applies to every project - include only sections that have real content from the conversation. An empty section is worse than no section.

### Template

```markdown
# [Project Name] - Session Handoff

**Last updated:** [Date]
**Session summary:** [One line - where things stand right now]

---

## Background

[What is this project? Who's involved? What's the goal? What tools/systems are in play?]

[Keep this stable across updates. Only revise if the project scope or team actually changed.]

---

## Work Completed This Session

[What actually happened. Be specific - include record counts, file names, command outputs,
IDs created, decisions made and their reasoning.]

[Use sub-sections if multiple workstreams were touched.]

---

## Current State

[The single most important section. A reader should understand exactly where things stand
from this section alone.]

[For data projects: row counts, pipeline status, quality metrics]
[For code projects: what builds, what doesn't, branch state, test status]
[For research/analysis: findings so far, confidence levels, gaps remaining]
[For multi-phase projects: phase completion status table]

---

## Configuration & Technical Context

[System config the next session needs: account IDs, field mappings, API endpoints,
environment details, tool versions, schema definitions.]

[Reference credentials by name or location only, never paste actual secrets.]

[Stays stable unless config changed. Use tables or code blocks for structured data.]

---

## Key Decisions & Rationale

[Decisions that constrain future work. Include the reasoning - the next session needs to
know not just WHAT was decided but WHY, so it doesn't relitigate settled questions.]

| Decision | Rationale | Date |
|----------|-----------|------|
| [What] | [Why] | [When] |

---

## Open Items

[What's unfinished, blocked, or needs follow-up. Be specific - name the entities,
describe what's unresolved, note what decision or input is needed.]

- [ ] [Item - what needs to happen, any blockers, who owns it]

---

## Files

| File | Location | Description |
|------|----------|-------------|
| [name] | [path] | [what it is, what it's for] |

---

## Next Session Prompt

[A ready-to-paste block that gives the next chat enough context to start immediately.
Reference the handoff doc path. Be specific about what to do next.]
```

---

## Section Selection Guide

Not every project needs every section. Choose based on what the conversation actually covered:

| If the session involved... | Include these sections |
|---|---|
| Any project | Background, Work Completed, Current State, Open Items, Next Session Prompt |
| Data pipelines, CRM, ETL | + Configuration & Technical Context, + Files |
| Code / engineering | + Configuration & Technical Context, + Files |
| Research or analysis | + Key Decisions & Rationale |
| Multi-session project (updating) | All that apply - preserve stable sections, update dynamic ones |
| Quick one-off task | Background, Work Completed, Open Items, Next Session Prompt (lighter weight) |

## Updating an Existing Handoff

When updating rather than creating:

1. **Preserve stable sections** - Background, Configuration, and Key Decisions only change if something actually changed this session
2. **Append to Work Completed** - Add a new dated sub-section for this session's work; don't overwrite prior sessions
3. **Refresh Current State** - Always reflects the latest status, not historical
4. **Close resolved Open Items** - Mark done or remove; add new ones
5. **Update Files table** - Add new files, remove deleted ones
6. **Rewrite the Next Session Prompt** - Must reflect the new starting point
7. **Bump the date**

## Quality Checklist

Before saving, verify:

- Every claim traces to something actually discussed in this conversation
- No invented details, no speculation, no assumptions about undiscussed topics
- IDs, file names, record counts, and paths are accurate
- The Current State section is a complete standalone picture
- The Next Session Prompt would actually work if pasted cold into a new chat
- Stable sections from a prior handoff are preserved (if updating)

## Where to Save

Save as `[project-name]-handoff.md`. Put it in the folder you keep persistent project reference in, or failing that, your usual outputs folder, so the next session can find it and attach it.

- If updating an existing handoff, overwrite the same file path
- If the project name is ambiguous, ask what to call it
- If the conversation covered multiple distinct projects, create separate handoffs

## Tone and Format

- Direct and operational - every sentence earns its place
- Tables for structured data (status lists, file inventories, field mappings)
- Code blocks for commands, configs, and the next-session prompt
- Bracketed status tags where useful (e.g., `[DONE]`, `[BLOCKED]`, `[NEXT]`)
- Match the register of the conversation - technical users get technical handoffs, casual conversations get clear but lighter docs
