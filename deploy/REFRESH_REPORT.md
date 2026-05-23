# MLB Betting Dashboard Refresh Report

**Window:** midday (11:30 AM ET)
**Run Timestamp (UTC):** 2026-05-23T19:15:00Z
**Slate Date:** 2026-05-23

## Data Quality

- Games on slate: 16 total (11 Preview, 3 Live, 2 Final)
- Probable pitchers confirmed via schedule-api: 32/32 (100%)
- Weather data: 13/13 outdoor/retractable parks fetched (Open-Meteo)
- Short sample flags: Chase Petty opener role (5.2 IP), Robert Gasser IL return (4 IP), Lucas Giolito IP limit (5 IP), Jovani Moran reliever-to-SP (25.2 IP)

## Weather Highlights

- Oracle Park: 61F, 49mph WSW — extreme suppression, most impactful weather on slate
- Citizens Bank Park: 51F, 38mph NE blowing in — flips park to pitcher-friendly
- Truist Park: 72F, 35mph E — strong RF headwind
- Fenway Park: 56F, 24mph E — cold, E wind suppresses Green Monster
- Great American Ball Park: 70F, 25mph W — wind OUT to right-center, offense-boosting
- Kauffman Stadium: 77F, 24mph NW — crosswind, neutral
- Rogers Centre: roof closed confirmed (97% precip, 70mph wind outside)
- Chase Field: roof closed (92.7F outside)
- loanDepot park: roof likely closed (81.7F, 31mph wind outside)
- American Family Field: roof likely closed (59F, 24mph outside)

## Per Game Summary

| gamePk | Matchup | Grade | Verdict Chips | Picks |
|---|---|---|---|---|
| 823458 | CLE @ PHI | A 87 | Phillies ML, Under 7.5, Wheeler K over 6.5 | 7 |
| 823222 | CWS @ SF | B 80 | Under 7, Giants ML | 7 |
| 824109 | SEA @ KC | B 78 | Mariners ML, Kirby K over 5.5 | 7 |
| 824760 | MIN @ BOS | B 75 | Twins ML, Bradley K over 6.5 | 7 |
| 824920 | WSH @ ATL | B 78 | Braves ML, Under 8 | 7 |
| 823862 | NYM @ MIA | B 82 | Mets ML, Meyer K over 6.5 | 7 |
| 824516 | STL @ CIN G2 | C 68 | Over 9 | 7 |
| 823787 | LAD @ MIL | C 66 | Pass (no primary chips) | 7 |
| 823300 | OAK @ SD | B 74 | Padres ML, Under 7 | 7 |
| 824030 | TEX @ LAA | B 72 | Rangers ML, Eovaldi K over 6.5 | 7 |
| 825080 | COL @ ARI | B 75 | Diamondbacks ML, Under 9 | 7 |
| 824518 | STL @ CIN G1 | LIVE | locked | 0 |
| 824674 | HOU @ CHC | LIVE | locked | 0 |
| 822814 | PIT @ TOR | LIVE | locked | 0 |
| 823543 | TB @ NYY | FINAL | closed | 0 |
| 824840 | DET @ BAL | FINAL | closed | 0 |

## Overlays Deployed

- odds_overlay.json: 16 games (ML, total, run line)
- statcast_overlay.json: 16 games (32 pitchers, ERA-based xFIP/FIP)
- picks_log.json: 170 total entries, 77 new today

## Learnings Adjustments Applied

Active rule: Two or more MODEL_ERROR losses yesterday. Second-pass validation on all over/total picks applied to all 11 Preview cards. Each card carries appliedAdjustments array noting validation.

Carryover rule: K over + Under total stacks only for ERA below 3.50 starters. Applied to Wheeler 1.99, Ginn 2.98, Bradley 2.87, Kirby 3.45.

## Deploy Status

- Git commit: 6116935
- Branch: main
- Push: SUCCESS
- Cloudflare Pages auto-deploy triggered (no wrangler used)
- Live URL: https://mlb-betting-dashboard-v2.pages.dev

## Notable Edges This Slate

1. Oracle Park 49mph WSW wind: Under 7 in CWS vs SF is the highest-conviction weather play on the slate
2. Citizens Bank Park 38mph NE: Wheeler ERA 1.99 plus wind-in earns A 87 grade, three-chip card
3. Petty/Gasser/Giolito all short-sample: three games capped at C/B grade per short-sample rules
4. Dodgers Pass card: C 66 grade, no primary Verdict chips despite LAD lineup quality (Gasser unknown too large)
5. Great American W wind: C 68 over lean with opener Chase Petty driving the thesis
