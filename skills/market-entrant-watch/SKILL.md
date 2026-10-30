---
name: market-entrant-watch
description: >
  Scheduled watch on a team's competitive market. Each run posts a short digest of new, verified
  competitor and ecosystem news to one team channel, and appends to an owner-only log every new
  market entrant found and every place the team's reference files look out of date. Trigger on
  "run the market watch", "what's new with our competitors", "any new entrants", or a scheduled
  weekday run. Does NOT edit reference files, track pricing or feature tables, or rule on the gaps
  it logs (a separate periodic reverification run does that).
---

# Market Entrant Watch

## What this skill does
Teams keep reference files on their competitors and partners, and those files drift. New players appear, owners change, products launch. This skill runs on a schedule (weekdays is typical) and keeps the team's view complete and current with two outputs:

1. **A digest** of NEW, verified news, posted to one team channel.
2. **An append-only log** for the owner, listing every new entrant found and every knowledge gap in the reference files.

The owner makes every reference edit. The run never touches the reference files. The log is the only file it may write.

## What to configure
- **Reference folder:** one file per competitor or partner. Name the archive, build and draft subfolders to skip.
- **Log file:** the append-only log.
- **Team channel and owner:** where the digest goes, and who gets the thread reply.
- **Competitor priority order:** top competitor first.
- **Partners and ecosystem players**, the industry body or regulator relevant to your customer, and 3 to 5 **product lanes** for discovery.
- **Pinned canonical facts** (for example, who owns whom). These override the reference files.
- **Fallback known list:** a short list of known entities, used only if the reference folder is unreachable.

## How it works
1. **Build the known set before searching.** Read the current reference files, skipping archive, build and draft folders (they hold superseded copies). Every entity with its own file, or named as a competitor in one, is known. For each, note its recorded key facts (owner or parent, products, AI features, partnerships, leadership) and the file's last-updated date.
2. **Read the log.** Every candidate already logged, and every name on a "Screened and excluded" line, is known too.
3. **Read the channel.** Read the last ~100 messages and prior digest threads. Never report a story again unless there is a material new development; then label it "Update:".
4. **If the reference folder is unreachable:** use the fallback known list, still do the digest, skip the log, and say so in one line in the owner's thread.
5. **Search the news lanes, in order.** Direct competitors in priority order. Then partners and ecosystem players (watch ownership changes and bundle deals). Then the industry body or regulator news relevant to your customer. Then broader trends, only if substantive. Window: since the last run (Monday covers the weekend), plus anything from the past 7 days not yet reported.
6. **Run the discovery scan for unknown entities.** This is not limited to the news window. Cover each product lane using trade news and press releases, funding and acquisition announcements, partnership announcements, "best X" and "alternatives to <known vendor>" pages per lane, app-store categories, and names mentioned in stories you read. Vary queries day to day. Keep going until new searches stop turning up unlogged entities.
7. **Qualify each candidate** against the bar below.
8. **Check each known entity for gaps.** A knowledge gap is a verified fact that contradicts or is missing from an entity's reference file: ownership change, acquisition, new product line, AI feature, partnership, leadership change, discontinued product.
9. **Verify everything** (see Rules), then append to the log, post the digest, and reply in the owner's thread.

## Qualification bar (all must hold)
- Sells specifically to your customer type, not a generic tool.
- Fits one of your product lanes.
- Has a live product website that you actually opened.
- Shows at least one traction signal: funding, an acquisition, a named partnership, named customers, press coverage, or appearing on several independent comparison lists.

Review aggregators, listicle publishers and consultancies are not competitors. If unsure, log the candidate as "Watch, unverified traction" rather than qualifying it.

## Log format
Append at the end of the log file. Never rewrite earlier entries.

```
## YYYY-MM-DD
### New entrants
| Name | Lane | Owner/parent | Traction signal | Website | Source | Most similar known entity | Status |
(Status is Qualified or Watch)

Screened and excluded today: Name (reason), Name (reason)

### Knowledge gaps
| Reference file | Entity | What is out of date or missing | Verified fact | Source |

### Posted today
- <link to each digest item or thread>
```

Write "None today." under any empty subsection. Omit the "Screened and excluded" line if nobody was rejected. If nothing at all was found, still append the date heading and "No new entrants, gaps, or stories." so the owner can see the run happened.

## Digest format
Title with the date. Up to five sections, omitting empty ones: **Competitors**, **Partner watch**, **Industry and us**, **Trends**, **New on the radar**.

Each news item:
- **Bold headline** (source link, date)
- What happened: one sentence.
- Talk track: one line on how a frontline person answers "do we do this?" or uses the news. Factual. Never claim a feature of your own product that you have not verified on your own public site.

"New on the radar" lists the top 3 Qualified entrants in lane priority order, each with site link, source link, what it is, and why it matters (where the team may run into it). If more qualified, end with "+N more in the log."

Cap the digest at 10 items. News first, most important first. No padding.

**Owner thread reply** under the digest, starting "For <owner>:": a log summary ("Logged N new entrants (Q qualified) and G gaps"), the top gaps one line each (max 5), and at most ONE content angle grounded in today's news. Skip the reply if it would be empty.

**Nothing new for the team** (no verified news item and no Qualified entrant): post nothing to the channel, even if the log has gaps or Watch rows.

## Rules
- **Verify or leave it out.** Every news item needs a working source link dated inside the window. Every new entity needs its own website link plus one third-party source. Every gap needs a source. Never invent a story, figure, quote, date, customer or source.
- **Never edit reference files.** Only the log is written.
- **Pinned facts win.** Canonical facts in your run prompt override the reference files. If the files disagree with a pinned fact, log it as a gap; do not repeat the file.
- **Absence is dated.** Write "no public evidence of X as of DATE", never "they don't have X".
- **Stay inside the source.** Never state an entrant's pricing, customer counts or features beyond what its own site or the cited source says.
- **Pricing is out of scope.** Do not track prices or detailed feature tables. Only note that a pricing change was announced, with the source.
- **Internal content never goes to the channel.** Contracts, partner terms, internal plans and internal politics stay out. The channel gets entity names and public facts with public sources only.
- **No repeats.** A story already posted returns only as "Update:" with a material new development.

## Pairs with
A separate periodic reverification run (monthly, for example) reads the open gaps in the log and asks the owner to rule on each. This daily watch only logs.

## Example
**Setup:** A regional distributor of e-bike components. Reference folder holds files on motor, battery and drivetrain makers it competes with or resells. Priority order: the motor maker it competes with most, then two battery makers. Lanes: mid-drive motors, battery packs, drivetrains and shifting, controllers and displays. Pinned fact: the drivetrain partner is owned by a larger cycling parts group.

**Run (a Tuesday):**
- Known set built from 14 reference files and 22 logged names. The channel shows last week's story on a battery recall already posted.
- News: the top motor competitor announced a lighter mid-drive with app-based tuning (press release, dated yesterday). The battery recall story has a new development: the recall was extended to a second pack size, so it runs as "Update:".
- Discovery: an "alternatives to <known controller maker>" page and a trade-news funding story surface a controller startup selling to e-bike assemblers. Its site is live, it raised a seed round reported by a trade outlet. Qualified. A second name, a generic electronics parts marketplace, fails the customer-type test. A third, a small motor brand with a live site but no traction signal, goes in as Watch.
- Gaps: the drivetrain partner's file still lists the founder as CEO; a trade story names a new CEO. Logged with source.

**Log entry appended:**
```
## 2026-03-10
### New entrants
| <Controller startup> | Controllers and displays | Independent | Seed round (trade press) | <site> | <source> | <known controller maker> | Qualified |
| <Small motor brand> | Mid-drive motors | Independent | None found | <site> | <site> | <top motor competitor> | Watch |

Screened and excluded today: <Parts marketplace> (generic electronics marketplace)

### Knowledge gaps
| drivetrain-partner.md | <drivetrain partner> | CEO listed as founder | New CEO named | <source> |

### Posted today
- <link to digest>
```

**Digest posted:**
> **Market watch, 2026-03-10**
> **Competitors**
> **<Motor competitor> launches lighter mid-drive with app tuning** (<link>, 2026-03-09)
> What happened: a new mid-drive model with app-based assist tuning.
> Talk track: if a shop asks whether we carry app-tunable motors, point to the models we stock today and say we are watching this launch; do not promise a date.
> **Update: battery recall widened** (<link>, 2026-03-09) ...
> **New on the radar**
> <Controller startup> (<site>, <source>): controller maker selling to assemblers; shops building custom kits may mention it.

**Owner thread:** "For <owner>: Logged 2 new entrants (1 qualified) and 1 gap. Gap: drivetrain partner file lists an outdated CEO. Angle: a short note to shops on what app-tunable motors mean for service."
