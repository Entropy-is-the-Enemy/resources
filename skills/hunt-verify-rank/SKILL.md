---
name: hunt-verify-rank
description: >
  Whole-codebase bug and security audit for apps written mostly by AI ("vibe-coded"). Maps the
  attack surface, hunts with parallel agents by lens, has a separate agent verify every finding
  against the code, ranks what survives Critical, High, Medium or Low by who can trigger it and
  what it costs, keeps a findings ledger between runs, and fixes worst-first only when asked.
  Trigger on "audit my app", "security audit", "code diagnostic", "is this safe to launch",
  "check the whole codebase for bugs". Does NOT replace per-change review: for the current diff
  or a pull request, use Claude Code's built-in /code-review and /security-review. Not a
  penetration test, and never sends traffic to production.
argument-hint: "[path] [--fix] [--since <git-ref>] [--quick]"
---

# Hunt, Verify, Rank

A periodic, whole-repo audit. It finds bugs and security holes, proves each one is real, ranks them by how bad they are, and fixes the worst first when asked.

**Where it fits (tell the user this when no prior ledger exists in `.claude/audits/`):**

| When | Run | Why |
|---|---|---|
| Every change, before commit or merge | built-in `/code-review` and `/security-review` | Fast, diff-scoped, already verify and rank |
| Weekly, before a launch, after a long build session, before adding payments or user data | this skill | Looks at the WHOLE app, including code no diff touched |

A clean report does not mean the app is secure. It means this pass found nothing it could prove.

**Arguments:** `$ARGUMENTS`
- none: full audit of the repo
- a path (`src/api`): audit only that area
- `--since <ref>`: weight the hunt toward files changed since that ref, still map the whole surface
- `--quick`: phases 1 to 3 on the top 5 risk areas only, single hunter, still verified
- `--fix`: after the report, fix Critical and High findings (phase 7). Without it, report only.

---

## Phase 0: Set up (no edits)

1. Confirm this is a git repo and record `git rev-parse HEAD` and `git status --short`. The report is pinned to that commit.
2. If `--fix` was passed and the tree is dirty (ignoring this skill's own `.claude/audits/` files), stop and ask the user to commit or stash first. Fixes must be revertable.
3. Read `CLAUDE.md`, `README`, and the package manifests (`package.json`, `requirements.txt`, `pyproject.toml`, `go.mod`, etc.). Identify: framework, hosting, database and auth provider (Supabase, Firebase, Clerk, NextAuth, custom), payment provider, AI/LLM API use. Write "unknown" for anything the repo does not reveal and move on; do not guess.
4. Check whether you can spawn subagents (the Agent/Task tool). If not, use the single-agent fallback in Phases 3 and 4 and label the report "single-agent verification".
5. Look for a prior ledger at `.claude/audits/`. If one exists, load its open findings. This run must report each as STILL OPEN, FIXED, or REGRESSED, not rediscover them as new.

## Phase 1: Map the attack surface

Spend effort where an attacker would. Build a short inventory before hunting.

1. List every **entry point**: HTTP routes and API handlers, server actions, webhooks, cron jobs, edge functions, form handlers, file uploads, anything that reads a URL param, header, cookie, or request body, and any client code that talks to the database directly.
2. List every **trust boundary**: where auth is checked, where user input reaches a database, shell, file path, HTML, redirect, or LLM prompt, and where secrets are read.
3. Score each area on two 1 to 10 scales and write one line of reason for each score:
   - **Likelihood**: how likely this code holds a bug (complex logic, hand-rolled auth, string-built queries, money, permissions)
   - **Reachability**: how easily an outsider can reach it (public and anonymous = 10, any logged-in user = 7, admin only = 3, internal and unreachable = 1)
4. Sort by Likelihood x Reachability. The hunt works top-down. With `--quick`, take the top 5.

Under about 20 source files, skip the scoring: list the entry points and trust boundaries and hunt everything.

## Phase 2: Cheap, deterministic checks

Run what already exists. Do not install tools without asking.

- Dependency advisories: `npm audit --omit=dev` / `pnpm audit` / `pip-audit` / `go list -m -u` if available
- Type check and lint: `tsc --noEmit`, the project's lint script; for plain JavaScript with neither, `node --check` on each file; for Python, `python -m py_compile`
- The test suite, if one exists. Record pass/fail counts.
- If a step cannot run (no lockfile, no installed deps, no network), say "not run" and why. Do not count it as passing.
- Secret scan, by search, across tracked files AND history:
  - patterns: `sk_live_`, `sk-[A-Za-z0-9_-]{20,}`, `AKIA[0-9A-Z]{16}`, `-----BEGIN`, `service_role`, `SUPABASE_SERVICE`, `api_key\s*=\s*['"]`, `secret\s*=\s*['"]`, `password\s*=\s*['"]`, long base64 or hex strings assigned to key-like names
  - `git log -p --all -S '<pattern>'` for the high-risk patterns (`sk_live_`, `AKIA`, `-----BEGIN`, `service_role`), so keys deleted later still show up
  - confirm `.env*` is in `.gitignore` and that `git ls-files | grep -i env` returns nothing secret
  - any secret in a variable prefixed `NEXT_PUBLIC_`, `VITE_`, `REACT_APP_`, `EXPO_PUBLIC_` ships to every browser

Tool output is a candidate list, not a finding list. It goes through Phase 4 like everything else.

## Phase 3: Hunt (parallel agents)

Spawn one subagent per lens below, in a single message so they run in parallel. Give each: the stack summary, the ranked surface map, its lens, and the candidate schema. Tell each: "Assume at least one real issue exists in your lens. Find it, and trace it to an entry point." This raises recall; Phase 4 removes the false positives it creates.

Skip a lens that does not apply (no payments, no LLM). With `--quick`, run one hunter covering lenses A, B and C.

**Single-agent fallback:** if you cannot spawn subagents, run the lenses one at a time yourself and write every candidate in the schema below before starting Phase 4.

**A. Secrets and configuration**: keys in code, client bundles, logs or history; debug mode or verbose errors in production; permissive CORS; missing security headers; public storage buckets; default credentials.

**B. Authentication and authorization (highest yield in AI-written apps)**: routes or server actions with no auth check; auth checked in the UI but not on the server; one user able to read or change another user's records by changing an ID (IDOR); role checks trusted from the client; Supabase tables without row-level security or with `using (true)`; Firebase rules open to all; service-role or admin keys used from client code; password reset, magic link, or session flaws; missing rate limits on login and signup.

**C. Injection and input handling**: SQL or NoSQL built from strings; shell commands with user input; path traversal in file reads or uploads; XSS via `dangerouslySetInnerHTML`, `v-html`, `innerHTML`, or unescaped templates; open redirects; SSRF from user-supplied URLs; unvalidated request bodies; prompt injection where user text flows into an LLM that can call tools or see other users' data.

**D. Correctness and reliability**: unhandled promise rejections and missing error handling on network and DB calls; race conditions (double submit, double charge, check-then-act); wrong logic at edges (empty lists, null user, timezone, pagination, off-by-one); data written without a transaction where partial writes corrupt state; infinite loops or unbounded queries; failures the UI hides.

**E. Money, webhooks, and third parties** (only if present): webhook handlers that do not verify signatures; prices or amounts trusted from the client; fulfillment that runs before payment is confirmed; no idempotency on payment or email sends; unbounded paid-API calls a user can trigger (cost attack).

**Candidate schema** (each hunter returns a list in this shape, nothing else):

```
- id: <lens letter + number, e.g. B3>
  title: <one line>
  location: <file:line, plus the entry point it is reached from>
  evidence: <the exact code, quoted, max 15 lines>
  trace: <entry point -> ... -> the vulnerable line, one step per hop>
  claimed_impact: <what an attacker or bad input achieves>
  how_to_confirm: <a safe check: a request to send to localhost, a test to write, a query to run>
```

## Phase 4: Verify (separate agent, never the hunter)

The hunter does not grade its own work. Spawn one or more verifier subagents. Give each verifier ONLY the candidate entry and repo access, not the hunter's reasoning. Instruct:

> You are a skeptical reviewer. For this candidate, independently trace the code from the entry point to the cited line. Decide CONFIRMED, PLAUSIBLE, or REJECTED, and give the evidence for your verdict. Reject it if: the line is unreachable; an auth check, validation, ORM parameterization, framework escaping, or RLS policy upstream already blocks it; it only happens in dev or test config; or the evidence was misquoted. If confirming it safely is possible (a unit test, a request to a local dev server, a read-only query), do it and report the result. Never run anything against production, never send real payments or emails, never modify data you did not create.

**Single-agent fallback:** verify in a fresh pass that re-reads only each candidate block and the code, re-tracing from the entry point without relying on what you concluded while hunting.

Verdicts:
- **CONFIRMED**: full path traced with quoted code at each hop, or reproduced safely. A reproduction on a stand-in (for example the same SQL run against an in-memory SQLite instead of the app's driver) counts if the trace is also quoted; say it was a stand-in.
- **PLAUSIBLE**: path mostly traced, one hop unproven; say which hop
- **REJECTED (guarded)**: an upstream check blocks it; name the check in one line
- **NOT APPLICABLE**: the code the concern needs does not exist (no login route, so no login rate limit). List these separately; they are not false positives.

Rejected and not-applicable entries go in the ledger so the next run does not re-raise them.

A secret found in tracked files or git history is CONFIRMED by existence and rated Critical, even if it looks like a placeholder or test key; add "confirm at provider whether this key is live" to the finding. A test-mode key (`sk_test_`, `pk_test_`) is Medium. A dependency advisory is CONFIRMED only if the vulnerable function is actually imported or reachable; otherwise Low.

## Phase 5: Triage by severity

Score each surviving finding on **who can trigger it** and **what it costs**. Use the highest row that fits.

| Severity | Who can trigger it | What it costs | Typical examples |
|---|---|---|---|
| **Critical** | Anyone on the internet, no login | Data breach, account takeover, money loss, full outage, or irreversible data loss | Live secret key exposed; unauthenticated admin or data route; RLS off on a user-data table; SQL injection on a public input; unsigned payment webhook that fulfills orders |
| **High** | Any logged-in user, or anyone under a common condition | One user reaches or changes another user's data; core flow breaks or corrupts data for many users | IDOR on `/api/orders/:id`; stored XSS; server action missing its auth check; double-charge race |
| **Medium** | Needs an unusual condition, or impact is contained | Limited exposure, degraded service, cost abuse | No rate limit on login; stack traces shown to users; reachable dependency advisory with no known exploit path; unhandled error that crashes one page |
| **Low** | Hard to reach, or defense-in-depth only | Hygiene; raises the cost of a future bug | Missing security headers; unreachable vulnerable dependency; dead code with a risky pattern |

Rules:
- PLAUSIBLE findings drop one level, and never sit at Critical.
- Then group findings that share a root cause (for example "no auth middleware on /api/*" instead of nine separate route findings). Fix the cause, not each symptom.
- Effort for each fix: **S** (under 15 lines, one file), **M** (several files), **L** (design change, migration, or new dependency).

## Phase 6: Report

**In chat**, lead with the verdict in one line: `Launch-blocking: N Critical, N High.` Then:

| # | Sev | Finding | Where | What could happen (plain English) | Fix effort | Verdict |
|---|---|---|---|---|---|---|

"What could happen" is one sentence a non-engineer understands: "Anyone could download every customer's email address by visiting this URL," not "IDOR in GET handler."

Then: counts by severity, the rejected count with one line on why most were rejected, the Phase 2 tool results (tests, audit, type check), and the recommended fix order.

**On disk**, write `.claude/audits/AUDIT-<YYYY-MM-DD>.md` with: the commit hash, the surface map with scores, every finding (full candidate schema plus verdict, evidence, severity, fix plan, status OPEN), the rejected list with reasons, and the carry-forward status of prior findings. Then check `git check-ignore .claude/audits/`. If the folder is NOT ignored, tell the user plainly: a committed audit file is a map of the app's weak points, so it should not go into a public repo, and offer to add it to `.gitignore`. Do not edit `.gitignore` without a yes.

## Phase 7: Fix (only with --fix, or when the user picks findings)

Work Critical first, then High. Medium and Low only when the user asks.

For each finding or root-cause group:
1. State the fix in one line before editing.
2. Make the **smallest** change that closes the hole. No drive-by refactors.
3. Where the project has tests, add a regression test that fails before the fix and passes after it. If there is no test setup, say so and describe the manual check instead.
4. Re-run the Phase 4 verifier against the patched code: does the original trace still work? Does an adjacent variant (the same bug on a sibling route) still work? If yes, the fix is incomplete.
5. Run the test suite and type check. Mark the ledger entry FIXED with the evidence, or BLOCKED with the reason.

**Stop and ask before:** database schema or RLS policy migrations, changes to the auth model, deleting data, adding dependencies, rewriting git history, or anything touching production config or deploy settings.

**Secrets are never fixed by deleting them from code.** Git history keeps them. The fix is: (1) tell the user to rotate the key at the provider NOW, with the provider's name; (2) move the value to an environment variable; (3) only if the user asks, help scrub history, and warn that this rewrites history for every collaborator.

After fixing, give a short before/after: findings closed, findings left open with their severity, tests passing.

## Phase 8: Close

- Update the ledger statuses.
- Recommend the next run: before the next deploy if any Critical or High is still open, otherwise weekly or after the next large build session.
- For a recurring check inside a long-running session: `/loop 7d` followed by this skill with `--quick`. That stops when the session closes; for a standing weekly run, use a scheduled task.

## Rules that hold across every phase

- Read-only until Phase 7. Phases 0 to 6 change nothing except writing the report file.
- Never send traffic to a production URL, real payment provider, or real email/SMS endpoint. Local dev server and test mode only.
- Never print a full secret value in chat or the report. Show the first 4 and last 4 characters.
- Never report a finding without quoted code. If you cannot quote it, you have not found it.
- Do not inflate. Ten honest Mediums beat one invented Critical. If the audit found nothing Critical or High, say so plainly and stop.

## Prior art and attribution

This is a synthesis of workflows described on episodes of the How I AI podcast, hosted by Claire Vo, plus gaps those workflows leave open.

- The two-tier shape (a wide scan produces candidate issues, a stronger model checks each against the code and ranks the real ones from most to least critical) follows the hybrid security scan Alex Finn described on his How I AI episode.
- Ranking files by likelihood and reachability before hunting, telling the hunter a bug exists, requiring a separate verifier to reproduce each finding, and re-running the exploit against the patch follow the workflow described in "How Mozilla Fixed 500 Security Bugs with Claude Mythos."
- Grouping findings by shared root cause before fixing follows Claire Vo's GPT-5.5 review episode.

Added here: a defined severity rubric, a threat list aimed at AI-written apps, a findings ledger that tracks fixes and regressions across runs, the rule for leaked secrets, and the hand-off to Claude Code's built-in diff-scoped review commands. This skill is not affiliated with or endorsed by How I AI, its host, its guests, or Mozilla.
