---
name: send-imessage
description: >
  Send an iMessage from your own Mac to a chosen contact or handle by driving the Messages app through
  a computer-use bridge, then verify by screenshot that the exact text landed in the right thread. Use
  on "text Alex," "send an iMessage to," "message the contractor on my Mac," "shoot a quick text to
  that number," or "reply in that thread." The safety spine is a confirm gate on the resolved handle
  plus a refusal to send unattended. NOT for SMS through a third-party messaging API, NOT for Slack,
  Teams, or email, and NOT usable when the Mac is offline, asleep, or locked. The pattern generalizes:
  resolve, confirm, act, verify for any irreversible outbound action.
---

# Send iMessage

## What this skill does

Sending a text is irreversible. No unsend, no draft state on the recipient's side, no second look once
the bubble is up. A workflow ending in one of those needs a shape, not just a tool call.

The shape is **resolve, confirm, act, verify**. Resolve the friendly name into a real target. Confirm
that target and the exact wording with the human. Act through the narrowest path that works. Verify
what happened before reporting or retrying. iMessage is the concrete instance. The same four steps
carry to any publish, any payment, any outbound send.

The transport is your own Mac, reached over a computer-use bridge as `<your-mac-device-id>`. The
Messages UI is the primary path. A one-line `osascript` call is a narrow fallback.

## Resolve the name to a handle

**"Text Alex" is not a recipient. A handle is.** A handle is a phone number or an Apple ID email.
Anything short of one is guesswork wearing a friendly label.

Search in Messages or Contacts and enumerate what comes back. Three outcomes:

- **One match, one handle.** Proceed to the gate with it.
- **One match, several handles.** A mobile number, a work number, and an Apple ID email are three
  different destinations. Ask which. Do not default to the first row or the app's highlighted one.
- **Several matches, or a partial-name match.** Ask the human to pick, showing full name as stored
  plus the last four digits of each candidate. Same-name collisions are the most common
  wrong-recipient failure, and they stay invisible until the message is delivered.

A raw number or email from the human is already resolved. Skip lookup, still run the gate.

## Confirm before anything sends

**The gate is mandatory and it echoes the resolved target, never the friendly name.** "Send to Alex?"
confirms nothing, because the failure mode is the name mapping to the wrong person. Echo the handle,
or at minimum the last four digits, alongside the name.

The gate shows four things: the resolved handle, the display name it maps to, the exact message text
character for character, and the send path. Then it waits. No timeout, no "proceeding unless you
object," no assent inferred from an earlier turn.

**Refuse unattended sends.** Autonomous or scheduled execution is allowed only when **both** the
recipient and the exact wording came from the human verbatim. If any part was generated, paraphrased,
inferred, or self-resolved from an ambiguous name, queue it as a draft for approval and say so. A
model-authored text going out under someone else's name with no human read is the worst outcome here,
and it costs nothing to prevent.

Any edit at the gate restarts the gate.

## Check state, then act

Run a **pre-send state check** before the first keystroke. Screenshot and confirm:

1. Awake and unlocked. A locked screen swallows keystrokes silently.
2. Messages running and frontmost. Keystrokes go to whatever has focus, not what you meant.
3. Correct thread open, recipient name or handle visible in the header.
4. Compose field empty. Leftover draft text concatenates into your message.

**Path A: the Messages UI.** The default. Select the thread or start a new message, type the recipient
into the To field, wait for the app to tokenize it, screenshot to confirm the token shows the handle
you expect, click into the compose field, type the body, screenshot again, then press Return. The UI
is preferred because it shows the recipient chip, the thread history, and the blue-versus-green
indicator telling you whether this sent as iMessage or fell back to SMS.

**Path B: `osascript`.** A one-line AppleScript handing the text to Messages directly. Use only when
Path A is blocked, and only with a **literal handle**. Path B does no name resolution: give it a
friendly name and it will fail or, worse, guess. It also gives no blue-versus-green signal and no
visual thread confirmation, which is why it is the fallback. Verify Path B sends in the UI.

On either path, type the body in one action where the bridge allows it, and never press Return
mid-body. A stray Return sends a half-written text, which cannot be recalled either.

## Verify before you report, and before you retry

**Verify before retry is the rule that prevents double-sends.** A send call can return an error, a
timeout, or nothing at all after the message already went out. Retrying on a bare error is how one text
becomes two.

After every attempt, screenshot the thread and check three things on the newest bubble: the header
shows the resolved handle or expected contact, the text matches character for character, and the
bubble is outbound and delivered rather than stuck sending or marked "Not Delivered."

Bubble present: it succeeded, so report it and do not retry, whatever the tool returned. Bubble
absent: it failed cleanly and one retry is safe. No readable screenshot: report uncertainty and stop.
Never retry blind. Only a screenshot supports a "sent" claim.

## Output format

The confirm gate, before anything sends:

```
CONFIRM SEND
  To:      Jordan Lee
  Handle:  +1 (555) 010-1234   [...1234]
  Path:    A (Messages UI)
  Message: "Moving our 2pm to 3pm today, same link. Works?"

  Sends immediately and cannot be recalled.
  Reply "send" to proceed, or edit the text or the recipient.
```

The sent confirmation, after screenshot verification:

```
SENT
  To:       Jordan Lee  [...1234]
  Thread:   header confirmed, handle matches
  Bubble:   text matches exactly, delivered, blue (iMessage)
  Path:     A (Messages UI)
  Verified: screenshot of thread after send
```

If verification is partial, say which checks passed. Never write SENT above an unread screenshot.

## Worked example (invented)

```
Human: text Alex that the code review is done

Resolve:
  Two contacts match "Alex."
    1. Alex Rivera   mobile  ...1234
    2. Alex Rivera   work    ...8890   (separate card, same name)
  Ambiguous. Asking rather than guessing.

Human: the first one, mobile

Gate:
  To ...1234 (Alex Rivera), Path A:
    "Code review is done, comments are in the PR."
  Wording drafted, not verbatim. Approval required.

Human: send

State check:
  awake, Messages frontmost, thread ...1234 open with header
  reading Alex Rivera, compose empty. All four ok.

Act (Path A):
  typed body, screenshotted compose field, pressed Return.
  Bridge returned a timeout with no status.

Verify (NOT retry):
  screenshot shows one new outbound blue bubble, text matching
  character for character, marked Delivered. The timeout was a
  reporting failure, not a send failure. A retry would have sent
  the message twice.

Report:
  SENT to Alex Rivera [...1234], header and text confirmed, delivered, blue.
```

The refusal, invented: a scheduled job wants to text "your package was delivered to the front desk"
to a handle it resolved itself. Generated wording, self-resolved recipient, so nothing sends. It
queues as a draft with the handle shown, for approval.

## Boundaries

This skill sends and verifies. It does not compose without showing you the text at the gate, read your
history, manage contacts, or send to groups, where a wrong recipient multiplies by thread size.

It requires a Mac powered on, unlocked, signed in to Messages, and reachable over the bridge. Offline,
asleep, or locked means it stops and says so rather than queuing something to fire later.

It does not send SMS through a third-party messaging API, and does not touch Slack, Teams, or email.
Those transports have their own failure modes and confirmation requirements.

iMessage and AppleScript are trademarks of Apple Inc. This skill is not affiliated with, endorsed by,
or sponsored by Apple.

The four steps generalize. Any irreversible outbound action deserves a resolved target echoed back, an
explicit human yes on the exact payload, the narrowest path that works, and verified state before you
claim success or retry.
