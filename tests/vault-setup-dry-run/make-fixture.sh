#!/bin/sh
# Builds a throwaway work folder for a dry run of the vault-setup skill.
# Usage: sh make-fixture.sh "<empty target folder>"
# Everything it writes is fictional. See README.md in this folder.
set -eu
S="${1:?give a target folder}"
[ -e "$S" ] && [ -n "$(ls -A "$S" 2>/dev/null)" ] && { echo "target is not empty: $S" >&2; exit 1; }
HERE="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$S/Dana Work/Old Reports" "$S/Dana Work/misc" "$S/to-drop" "$S/run"
cp -R "$HERE/../../skills/vault-setup" "$S/skill"
cp "$HERE/persona.md" "$S/persona.md"

cd "$S/Dana Work"
printf 'month,gifts,total_usd,new_donors\n2026-07,212,48150,19\n2026-08,198,44720,14\n2026-09,240,61390,27\n' > "Old Reports/giving-summary-Q3-2026.csv"
printf '# Board report, September 2026\n\nGiving in September was $61,390 from 240 gifts. 27 new donors.\nFall appeal mailed 2026-09-14 to 3,100 households.\n' > "Old Reports/board-report-2026-09.md"
printf '# Board report, August 2026\n\nGiving in August was $44,720 from 198 gifts. 14 new donors.\n' > "Old Reports/board-report-2026-08.md"
printf 'name,title,salary_usd,review_date\nP. Lindqvist,Gift Processor,51200,2026-12-04\nR. Abara,Data Coordinator,56800,2026-12-11\n' > "Staff salary review 2026.csv"
printf 'Notes from call w/ Harlow Print 10/29: year-end mailer proof due Nov 20, drop date Dec 1. Qty 3,400. Quote pending.\n' > "misc/harlow call notes.txt"
printf 'todo\n- reconcile Oct gifts\n- board report\n- CRM dedupe??\n' > "todo.txt"

cd "$S/to-drop"
printf 'gift_id,date,donor_id,amount_usd,fund,channel\n' > gifts-2026-10.csv
i=1
for a in 50 100 25 250 75 1000 40 60 500 35 120 80 200 45 150 30 90 2500 55 65; do
  if [ $((i % 3)) = 0 ]; then fund=Scholarship; else fund=General; fi
  if [ $((i % 2)) = 0 ]; then ch=online; else ch=mail; fi
  printf 'G10-%03d,2026-10-%02d,D%04d,%s,%s,%s\n' "$i" $((i % 28 + 1)) $((1000 + i * 7)) "$a" "$fund" "$ch" >> gifts-2026-10.csv
  i=$((i + 1))
done
printf 'month,gifts,total_usd,new_donors\n2026-10,20,5470,4\n' > giving-summary-2026-10-DRAFT.csv
printf '# Board report, October 2026 (DRAFT)\n\nGiving in October was $5,740 from 20 gifts.\n\nTODO new donors, appeal results.\n' > board-report-2026-10-draft.md
printf '# Year-end appeal plan 2026\n\nGoal: $180,000 by 2026-12-31. Mailer drops 2026-12-01 via Harlow Print, 3,400 households. Email series: Dec 3, Dec 17, Dec 30.\nOwner: Dana. Copy: Mireille Stroud. Approval: Tobias Wenck.\n' > year-end-appeal-plan.md
printf 'From: Tobias Wenck\nTo: Dana Okafor\nDate: 2026-11-18\nSubject: Board packet\n\nDana, board meets Dec 9. Need the October and November numbers in the packet by Dec 2. Keep it to one page.\n' > email-wenck-board-packet-2026-11-18.txt
printf 'From: Dana Okafor\nTo: Mireille Stroud\nDate: 2026-11-12\nSubject: appeal letter draft\n\nMireille, read it twice. Second paragraph is the strongest thing in it, so move it up. Cut the stats block, nobody gives because of a pie chart. Need the next pass Friday. Thanks. D\n' > email-dana-to-stroud-2026-11-12.txt
printf 'CRM dedupe project\n\nBrightledger has about 1,900 suspected duplicate donor records. Plan: R. Abara exports pairs, Dana reviews top 200 by giving, merge by Jan 31 2027.\nStatus 2026-11-10: export done, review not started.\n' > crm-dedupe-notes.txt
printf 'vendor,contact,service,contract_end\nHarlow Print,Jo Petrakis,mail house,2027-06-30\nBrightledger,support desk,donor CRM,2027-03-31\n' > vendors.csv
printf 'Quote Q-4471 Harlow Print 2026-11-05\nYear-end mailer, qty 3,400, 2 inserts: $4,862.00. Postage est: $1,530.00.\n' > harlow-quote-Q-4471.txt
printf 'Monthly gift reconciliation checklist\n1. Export gifts from Brightledger\n2. Match to bank deposit report from finance (Corinne Vale)\n3. Fix mismatches\n4. Send summary to Tobias by the 5th business day\n' > reconciliation-checklist.txt
printf 'donor_id,name,street,phone,lifetime_giving_usd\nD1042,Example Donor A,12 Test Ln,555-0101,18250\nD1077,Example Donor B,9 Sample Rd,555-0102,9400\n' > "top donors with addresses.csv"
printf 'Scholarship fund report FY26 notes: 14 awards, $42,000 total. Report to donors due Jan 15 2027.\n' > scholarship-fund-notes.txt
printf 'Board mtg prep notes, Sept. Tobias wants fewer tables, more one-line takeaways. Scholarship numbers go last.\n' > "FINAL final v3 board notes (2).txt"
echo "fixture ready: $S"
