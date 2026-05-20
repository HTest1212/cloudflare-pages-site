# MLB Retrospective Report — 2026-05-19

---

## SECTION 2 — SLATE SUMMARY

**Date:** 2026-05-19 | **Total games on slate:** 15 | **All games Final**

**Picks settled:** 8 (all Schema A / v2 algorithm)

| Metric | Value |
|--------|-------|
| Record | 3W 5L 0P |
| Units | -2.6017 |
| Win Rate | 37.5% |
| ROI | -32.5% |

**By market (yesterday):**

| Market | W | L | Win Rate | Units |
|--------|---|---|----------|-------|
| K | 1 | 2 | 33.3% | -1.1525 |
| Total | 1 | 2 | 33.3% | -1.1071 |
| ML | 1 | 1 | 50.0% | -0.3421 |

**By tier (yesterday):**

| Tier | W | L | Win Rate | Units |
|------|---|---|----------|-------|
| B | 3 | 4 | 42.9% | -1.7493 |
| C | 0 | 1 | 0.0% | -1.0000 (K win offset by Total loss in same game) |

*Note: C tier Detmers K won but C tier Under 8 ATH@LAA lost in the same game.*

---

## SECTION 3 — LOCK TRACK RECORD

**No Lock (A tier) picks were published on 2026-05-19.**

**Lifetime Lock KPIs (all A tier settled picks):**

| Metric | Value |
|--------|-------|
| Record | 6W 1L |
| Win Rate | 85.7% |
| Units | +3.8778 |
| ROI | 48.5% |
| Current Streak | 6 win(s) |
| Rolling 14d Win Rate | 85.7% |
| Rolling 30d Win Rate | 85.7% |

**Guard Status: WARNING** — Rolling 14d Lock win rate is 85.7%, between 80% and 90% threshold. No cap is active but the 11:30 AM run should apply extra scrutiny before publishing any A tier pick. Require at minimum 4 of the 7 qualifier signals before elevating to A tier.

---

## SECTION 4 — TOP THREE LOSSES WITH DIAGNOSES

**1. Mariners ML (823136, B tier, conf 76)**
Bryce Miller was dominant (5.2 IP, 7 K, 0 ER) but the SEA offense was completely shut down by Anthony Kay who outperformed his right handed batter wOBA split. The model correctly identified the pitching edge but failed to protect against the scenario where the favored team's offense goes cold. Final: CWS 2, SEA 1.
Category: VARIANCE

**2. Sheehan K Over 6.5 (823302, B tier, conf 80)**
Sheehan lasted only 4 innings with just 2 strikeouts before being removed with 4 ER on the board. His 10.6 K per 9 rate was built on longer outings; a short early exit eliminated the counting path to 6.5 Ks. The model stacked this with an Under on the same game, creating correlated loss exposure.
Category: STARTER_REGRESSION

**3. Under 8 ATH@LAA (824033, C tier, conf 60)**
Detmers struck out 8 batters but allowed 8 ER as the Athletics punished mistake pitches. The LAA bullpen added 5 more runs. The game finished 14 to 6 and the total of 20 crushed the Under by 12. This was the same game as the Detmers K win, showing how K upside and run prevention can decouple completely.
Category: STARTER_REGRESSION

---

## SECTION 5 — PATTERNS AND RULES GENERATED

**Pattern: STARTER_REGRESSION (3 occurrences)**

Three losses were tied to starters who either got shelled before accumulating Ks (Sheehan), or who struck out batters while leaking runs (Detmers), causing combined K plus Under bets to split results or both lose. The core issue is that stacking a K over and an Under on the same starter creates correlated exposure: if the starter struggles with run prevention, the Under fails even if Ks accumulate; if the starter gets pulled early, both props fail simultaneously.

**Rule generated:** When stacking K over and Under total on the same starter, require ERA below 3.50 in last 5 starts AND minimum 5 innings pitched average in last 3 starts before publishing both as separate picks. If ERA is above 3.50 in recent starts, publish only the K prop OR the Under, not both.

---

## SECTION 6 — ADJUSTMENTS FOR TODAY

**(Guard status: WARNING — no cap active, but extra scrutiny required before any A tier publish)**

1. When stacking K over and Under total on the same starter, require ERA below 3.50 in last 5 starts AND minimum 5 innings pitched average in last 3 starts before publishing both. Publish only one if ERA is above 3.50.

2. (LOCK GUARD WARNING) Rolling 14d Lock win rate is 85.7%. Before publishing any A tier pick today, confirm at least 4 of: model confidence above 80, recent form positive, lineup confirmed, weather neutral or favorable, bullpen rested, no key injury, no umpire risk flag.

---

## SECTION 7 — LIFETIME AND RECENT 14-DAY KPIs

| Window | W | L | Win Rate | Units | ROI |
|--------|---|---|----------|-------|-----|
| Yesterday | 3 | 5 | 37.5% | -2.6017 | -32.5% |
| Recent 14d | 347 | 277 | 55.6% | +27.6858 | 4.3% |
| Lifetime | 347 | 277 | 55.6% | +27.6858 | 4.3% |

---

## SECTION 8 — DATA NOTES

- **Git sync:** Existing repo at /tmp/repo_retro reused (permissions prevented rm, re-clone not needed). Local picks_log.json used (7692 bytes, last modified 2026-05-20 01:47).
- **PAT:** Read from .env file at working folder path.
- **Boxscores:** All 4 game boxscores retrieved successfully for gamePks 824033, 825086, 823136, 823302.
- **Schema:** All 8 picks are Schema A (v2, id ending format YYYYMMDD-gamePk-market-key).
- **No Schema C (midday) picks found for 2026-05-19.**
- **Lock breaches:** None. No A tier picks were published on 2026-05-19.
