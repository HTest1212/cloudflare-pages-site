# MLB Retrospective Report — 2026-05-27

Generated: 2026-05-28T04:00:00Z

---

## SECTION 1 — LOCK BREACH BANNER

No Lock losses on 2026-05-27. No breach to report.

---

## SECTION 2 — SLATE SUMMARY

**Date:** 2026-05-27  
**Total games:** 15 (all Final)

**HARD ERROR: Zero picks found for 2026-05-27.**

The picks_log.json available at run time (last synced 2026-05-27 09:15 UTC) contains no entries dated 2026-05-27. The 11:30 AM midday pick run either did not execute, did not commit picks, or committed them after the snapshot used by this retrospective. No picks were settled because no picks exist for this date.

**Schemas checked:**
- Schema A (v2 algorithm, id ending in -v2): 0 picks
- Schema B (v1 algorithm): 0 picks
- Schema C (midday runWindow field): 0 picks

**Yesterday's record:** 0W-0L-0P | 0.00 units

**Record by market:** N/A (no picks)  
**Record by tier:** N/A (no picks)

---

## SECTION 3 — LOCK TRACK RECORD

**Lifetime Locks (A-tier):** 33 settled picks | 18W-12L-2P-1V  
**Win rate:** 60.0% | **Units:** +1.83u | **ROI:** +5.7%  
**Current streak:** Loss x3  
**Longest win streak:** 8 | **Longest loss streak:** 6  
**Rolling 14d win rate:** 52.2% (12W-11L)  
**Rolling 30d win rate:** 60.0% (18W-12L)  

**Guard status: CAP ACTIVE**

Rolling 14d Lock win rate (52.2%) is below the 80% floor. The 11:30 AM run must enforce: no new A tier picks until rolling 14d rate recovers to 85%. Any A tier candidate missing 4 or more qualifying signals is automatically demoted to B tier.

---

## SECTION 4 — TOP THREE LOSSES WITH DIAGNOSES

No new losses on 2026-05-27 (zero picks settled).

**Most recent Lock losses (prior sessions):**

1. **2026-05-25 Giants ML (A-tier)** — Category: MODEL_ERROR  
   Model overweighted home field and opposing starter ERA without confirming Giants offense ranked bottom third in runs scored last 7 days. A permanent exclusion rule violation.

2. **2026-05-25 Under 7 or 7.5 at Oracle (A-tier)** — Category: BAD_PARK_READ  
   Oracle Park suppressor overweighted. Visiting pitcher WHIP above 1.30 in last 5 starts was a known disqualifier per carryover rule.

3. **2026-05-25 Padres ML (A-tier)** — Category: STARTER_OVERRATED  
   Padres starter ERA differential was primary justification without FIP cross-check. FIP was outside the 0.50 tolerance window.

---

## SECTION 5 — RULE MEMORY STATUS

**Permanent rules (never expire): 4**

★ Never issue A-tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ERA and top 5 K rate. | validated=3
★ Never issue Giants ML as A-tier unless SF starting pitcher has sub 3.20 ERA AND Giants offense ranks top half R/G last 14 days. | validated=3
★ Cap A-tier exposure at 2 picks per game maximum. F5 Under 4 requires both starters sub 3.50 ERA with confirmed lineups. | validated=3
★ Never issue A-tier ML on any team when their offense ranks bottom third in runs scored last 7 days. | validated=3

**Rules promoted to permanent today:** 0

**Trial rules (all expire 2026-06-08, 11 days remaining): 5**

1. (1/3) Do not publish A tier F5 Under when the run suppressor is park and weather only — require starter ERA sub 3.50 and WHIP sub 1.20 in last 5.
2. (1/3) Do not publish A tier ML relying on ERA differential alone; require FIP within 0.50 of ERA and at least 3 quality starts in last 5.
3. (1/3) Do not publish A tier Under at Oracle Park when the visiting pitcher has a WHIP above 1.30 in last 5 starts.
4. (1/3) Do not publish A tier ML against a starter with ERA above 4.50 when that starter has allowed 2 or fewer runs in their last start.
5. (1/3) Do not publish A tier Over when the visiting team's rotation is starting a pitcher with an ERA above 5.00 in last 3 starts.

**Rules that aged out today:** 0  
**New rules created today:** 0 (no losses on slate)  
**Total rules in active memory:** 4 permanent + 5 trial = 9 total

---

## SECTION 6 — ADJUSTMENTS FOR TODAY (priority order)

1. ★ LOCK GUARD ACTIVE: Cap A tier publication until rolling 14d Lock win rate recovers to 0.85. Demote any A tier candidate missing 4 or more of: model confidence above 80, recent form positive, lineup confirmed, weather neutral or favorable, bullpen rested, no key injury, no umpire risk flag.
2. Do not publish A tier F5 Under when the run suppressor is park and weather only — require starter ERA sub 3.50 and WHIP sub 1.20 in last 5.
3. Do not publish A tier ML relying on ERA differential alone; require FIP within 0.50 of ERA and at least 3 quality starts in last 5.
4. Do not publish A tier Under at Oracle Park when the visiting pitcher has a WHIP above 1.30 in last 5 starts.
5. Do not publish A tier ML against a starter with ERA above 4.50 when that starter has allowed 2 or fewer runs in their last start.
6. Do not publish A tier Over when the visiting team's rotation is starting a pitcher with an ERA above 5.00 in last 3 starts.

*(4 permanent rules always active — not repeated here.)*

---

## SECTION 7 — LIFETIME AND RECENT 14-DAY KPIS

**Lifetime (926 settled picks)**
- Record: 472W-367L-29P
- Win rate: 56.3% | Units: +43.11u | ROI: +5.0%

**Recent 14 days (264 settled picks)**
- Record: 142W-109L-7P
- Win rate: 56.6% | Units: +10.25u | ROI: +4.0%

**Recent 7 days (142 settled picks)**
- Record: 79W-57L-5P
- Win rate: 58.1% | Units: +8.90u | ROI: +6.3%

**Yesterday (2026-05-27):** 0 picks settled (no picks in log for this date)

---

## SECTION 8 — DATA NOTES

**Git sync:** PAT unavailable in shell environment. Using existing /tmp/repo_retro (cloned 2026-05-27 09:15 UTC). Fresh clone was blocked by Permission denied on directory removal.

**HARD ERROR:** Zero picks for 2026-05-27 despite 15 Final games. Root cause likely: picks committed after 09:15 AM or /sessions disk exhaustion (100% full at 9.3G/9.8G) preventing the 11:30 AM run from writing to the working folder.

**Disk status:** /sessions partition 100% full. All I/O routed through /tmp. Output files staged at /tmp for git push.

**Profit normalization:** 77 outcomes (May 23, stake=100) and 65 outcomes (May 25, stake missing, 100-unit scale) normalized to stake=1 by dividing profit by 100. Corrects lifetime Lock units from previously reported figure to +1.83u.
