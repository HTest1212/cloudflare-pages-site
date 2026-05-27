# MLB Betting Retrospective — 2026-05-26

**Generated:** 2026-05-27T04:00:00Z
**Yesterday's Date:** 2026-05-26

---

## SECTION 1 — LOCK BREACH BANNER

No Lock losses on 2026-05-26.
Zero picks were logged for this date. Lock guard remains cap_active from prior deficit.

---

## SECTION 2 — SLATE SUMMARY

**Yesterday's slate:** 2026-05-26 — 15 games, all Final.

**Pick count:** 0 picks logged for 2026-05-26 across all schemas (v2, v1, midday).

> **HARD ERROR NOTE:** The 2026-05-26 schedule contained 15 finalized games but picks_log.json recorded zero picks for this date. No midday run data was found. The 11:30 AM run may not have executed or failed to write picks. This is a data gap — no bets to settle.

**Overall record for 2026-05-26:** 0W-0L-0P

**Record by market:** N/A  
**Record by tier:** N/A

**Game results for reference:**
- WSH 6 @ CLE 3 — Washington wins
- TBR 1 @ BAL 6 — Baltimore wins
- LAA 10 @ DET 6 — LA Angels win
- CHC 1 @ PIT 12 — Pittsburgh wins
- ATL 7 @ BOS 6 — Atlanta wins
- MIA 1 @ TOR 8 — Toronto wins
- CIN 7 @ NYM 2 — Cincinnati wins
- MIN 5 @ CWS 3 — Minnesota wins
- NYY 15 @ KC 1 — New York Yankees win
- STL 0 @ MIL 6 — Milwaukee wins
- HOU 7 @ TEX 10 — Texas wins
- SEA 4 @ OAK 1 — Seattle wins
- PHI 4 @ SD 3 — Philadelphia wins
- ARI 7 @ SF 5 — Arizona wins
- COL 6 @ LAD 15 — LA Dodgers win

---

## SECTION 3 — LOCK TRACK RECORD

**Guard Status:** CAP ACTIVE
**Rolling 14 day Lock win rate:** 54.17% (0.5417) — BELOW 80% threshold

The 11:30 AM run is operating under the Lock Guard Cap. No A tier picks may be published until the rolling 14 day Lock win rate recovers to 85%.

**Lifetime Lock KPIs:**
- Record: 18W-12L-2P (37 total entries including pending)
- Units: -1.2528 (net loss)
- Win rate: 60.00% (0.6000)
- ROI: -3.91%
- Current streak: See entries
- Rolling 14d win rate: 54.17%
- Rolling 30d win rate: 60.00%

**Locks by Market:**
- F5 Total: see entries (normalized from F5)
- ML: tracked
- Total: tracked
- K: tracked
- RL: tracked
- Other: Hits, TotalBases, F5_ML

**Guard Enforcement:** The 11:30 AM model must enforce the full A tier checklist. Any candidate missing 4 or more of the following is automatically demoted to B tier: model confidence above 80, recent form positive, lineup confirmed, weather neutral or favorable, bullpen rested, no key injury, no umpire risk flag.

---

## SECTION 4 — TOP THREE LOSSES WITH DIAGNOSES

No picks were logged for 2026-05-26. No losses to diagnose.

Prior A tier losses are documented in locks_log.json loss_diagnoses (12 total historical losses).

---

## SECTION 5 — RULE MEMORY STATUS

**Permanent rules (never expire):** 4

1. ★ Never issue A tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ERA and top 5 K rate. The park cannot overcome elite SP offense suppression that also kills the under edge.
   - times_validated: 3 | first learned: 2026-05-20

2. ★ Never issue Giants ML as A tier unless SF starting pitcher has sub 3.20 ERA AND Giants offense ranks top 10 NL in runs last 14 days. Suppress juice requirement to no worse than minus 125 when both conditions are not met.
   - times_validated: 3 | first learned: 2026-05-20

3. ★ Cap A tier exposure at 2 picks per game maximum. F5 Under 4 requires both starters sub 3.50 ERA with sub 7.0 BB9. Never stack F5 Under + ML + Total all A tier on same game.
   - times_validated: 3 | first learned: 2026-05-20

4. ★ Never issue A tier ML on any team when their offense ranks bottom third in runs scored last 7 days regardless of park advantage. Minimum requirement: top half run production last 7 days for A tier ML designation.
   - times_validated: 3 | first learned: 2026-05-20

**Rules promoted to permanent today:** 0

**Trial rules still accumulating evidence:** 5

1. Do not publish A tier F5 Under when the run suppressor is park and weather only — require starter ERA below 3.50 and opposing lineup ranked bottom 5 NL in runs scored.
   - times_validated: 1/3 | expires: 2026-06-08 (12 days remaining)

2. Do not publish A tier ML relying on ERA differential alone; require FIP within 0.50 of ERA and at least 3 consecutive quality starts before classifying as starter edge.
   - times_validated: 1/3 | expires: 2026-06-08 (12 days remaining)

3. Do not publish A tier Under at Oracle Park when the visiting pitcher has a WHIP above 1.30 in last 5 starts regardless of wind magnitude.
   - times_validated: 1/3 | expires: 2026-06-08 (12 days remaining)

4. Do not publish A tier ML against a starter with ERA above 4.50 when that starter has allowed 2 or fewer runs in 2 of his last 3 starts regardless of season ERA.
   - times_validated: 1/3 | expires: 2026-06-08 (12 days remaining)

5. Do not publish A tier Over when the visiting team's rotation is starting a pitcher with an ERA above 6.00 but the bullpen ERA is below 3.80; the pen can neutralize the starter damage and suppress the run total.
   - times_validated: 1/3 | expires: 2026-06-08 (12 days remaining)

**Rules that aged out today:** 0

**New rules created today:** 0 (no losses to generate rules from)

**Total rules in active memory:** 4 permanent + 5 trial = 9 total

---

## SECTION 6 — ADJUSTMENTS FOR TODAY (Priority Order)

1. ★ LOCK GUARD ACTIVE: Cap A tier publication until rolling 14d Lock win rate recovers to 0.85. Demote any A tier candidate missing 4 or more of: model confidence above 80, recent form positive, lineup confirmed, weather neutral or favorable, bullpen rested, no key injury, no umpire risk flag. [GUARD RULE — FIRST PRIORITY]

2. Do not publish A tier F5 Under when the run suppressor is park and weather only — require starter ERA below 3.50 and opposing lineup ranked bottom 5 NL in runs scored. [trial lock_breach — expires 2026-06-08]

3. Do not publish A tier ML relying on ERA differential alone; require FIP within 0.50 of ERA and at least 3 consecutive quality starts before classifying as starter edge. [trial lock_breach — expires 2026-06-08]

4. Do not publish A tier Under at Oracle Park when the visiting pitcher has a WHIP above 1.30 in last 5 starts regardless of wind magnitude. [trial lock_breach — expires 2026-06-08]

5. Do not publish A tier ML against a starter with ERA above 4.50 when that starter has allowed 2 or fewer runs in 2 of his last 3 starts regardless of season ERA. [trial lock_breach — expires 2026-06-08]

6. ★ Never issue A tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ERA and top 5 K rate. The park cannot overcome elite SP offense suppression that also kills the under edge. [PERMANENT — manual]

7. ★ Never issue Giants ML as A tier unless SF starting pitcher has sub 3.20 ERA AND Giants offense ranks top 10 NL in runs last 14 days. [PERMANENT — manual]

8. ★ Cap A tier exposure at 2 picks per game maximum. F5 Under 4 requires both starters sub 3.50 ERA with sub 7.0 BB9. Never stack F5 Under + ML + Total all A tier on same game. [PERMANENT — manual]

9. ★ Never issue A tier ML on any team when their offense ranks bottom third in runs scored last 7 days regardless of park advantage. [PERMANENT — manual]

---

## SECTION 7 — LIFETIME AND RECENT 14 DAY KPIs

**Lifetime:**
- Record: 472W-367L-29P
- Units: +4.4484
- Win rate: 56.26%
- ROI: +0.51%
- Total picks settled: 868

**Recent 14 days (2026-05-14 through 2026-05-27):**
- Record: 166W-136L-12P
- Units: +4.4484 (recent 14d share of lifetime)
- Win rate: 54.97%
- ROI: +1.42%

**Recent 7 days:**
- Record: 112W-84L-7P
- Win rate: 57.14%
- ROI: +2.19%

**Recent 30 days:**
- Record: 472W-367L-29P
- Win rate: 56.26%
- ROI: +0.51%

**Lock Track Record:**
- Lifetime: 18W-12L-2P | WR 60.00% | -1.2528u
- Rolling 14d: 54.17% WIN RATE — BELOW THRESHOLD
- Guard status: CAP ACTIVE

---

## SECTION 8 — DATA NOTES

- **Git sync:** Clone succeeded without PAT (public repo). picks_log.json refreshed from origin.
- **Missing picks (HARD ERROR):** 0 picks found for 2026-05-26 across all three schemas. The 2026-05-26 schedule had 15 Final games. This is a pick logging gap — the 11:30 AM run may have failed or not run on May 26.
- **Schema warnings:** Prior carryover_rules in learnings.json were plain strings (old format). Migrated to object format with source="manual", permanent=true, times_validated=3.
- **Outcomes settled:** 0 new outcomes (no picks to settle). outcomes_log.json unchanged.
- **Lock guard:** Inherited cap_active status from 2026-05-26 run (rolling 14d WR 54.17% < 80%).
- **No missing boxscores:** All 15 games returned Final status from MLB API.
