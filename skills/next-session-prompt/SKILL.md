---
name: next-session-prompt
description: "Produce a ready-to-paste prompt that starts the next chat session where this one left off. Use when the user says /next-session-prompt, \"give me the prompt\", \"prompt for the next session\", \"what do I paste into a new chat\", or asks for a handoff prompt to copy into a new chat."
---

# Next Session Prompt

Put a next-session prompt in chat, in one fenced code block, ready to copy and paste. Nothing above it but one short line of context.

## Two modes. Pick by what exists.

**Mode A, lift it.** A handoff document was written or updated this session, or the user names one. Read its `## Next Session Prompt` block and print it verbatim in a fenced block.

Before printing, check three things against the session. Fix them in the file first, then print:
- Every path it names still exists on disk
- Nothing it calls open was closed later in the session
- The dates are absolute and current

If the handoff has no prompt block, or the block is a placeholder, write one with Mode B and save it back into the handoff under that heading.

**Mode B, build it.** No handoff, or the user wants a prompt for something narrower than the handoff covers. Build it from the conversation. Invent nothing: every claim traces to something actually done or said this session.

## What a prompt has to carry

The test is whether it works pasted cold into a new chat with no memory of this one.

1. **The job in one or two sentences,** and what is already DONE so the next session does not redo it. Name the done work explicitly. "Do not reopen X" is worth a line.
2. **Read first,** two to four files in priority order, each with one clause on why. Full paths.
3. **The work,** in priority order. Findings from this session go in as a starting point, with "verify before acting; this is not an inventory" attached, because a stale finding acted on blind does damage.
4. **What not to touch.**
5. **Method,** only where this session learned one that worked.
6. **Open decisions for the user,** each with the default to take if they do not answer.
7. **Standing rules,** only the ones that bear on this job. Absolute dates always apply. Point to where the rest live rather than restating the whole house style.

## Format

- One fenced code block. Hard-wrap around 72 characters so it survives paste.
- Plain prose and simple lists. No tables, no markdown headings inside the block.
- No internal IDs unless the next session needs them to find something.
- Absolute dates. Never "yesterday" or "last session".
- If a number comes up, carry what it was agreed to mean, not the number alone.

## Before printing

Read it once as if you have never seen this conversation. If any sentence only makes sense to someone who was here, rewrite it.

## Boundaries

- **NOT handoff.** Handoff writes the full continuation document. This skill prints the short prompt that opens the next chat, lifted from that document when one exists.
- **Prints, does not run.** The prompt is for the user to paste. Never start the next session's work here.
