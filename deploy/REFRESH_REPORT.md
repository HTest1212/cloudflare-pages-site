# MLB Dashboard Refresh Report — 2026-05-21

**Run:** 11:30 AM ET automated refresh
**Window:** midday (11:30 AM)
**Timestamp UTC:** 2026-05-21T17:35:00Z
**Commit:** 4669a8f56d85d006c908ebf2b76cad00bac74556
**Deploy:** Cloudflare Pages CI triggered on push to main (auto-deploy)

---

## Slate: 2026-05-21 | Games: 7

### API Data Quality

| Field | Result |
|-------|--------|
| Pitchers confirmed via schedule-api | 14 of 14 |
| TBD pitchers | 0 |
| Weather fetched | 7 parks (all outdoor / retractable) |
| Lineups confirmed | CLE@DET, PIT@STL, NYM@WSH (3 games) |
| Lineups projected | ATL@MIA, TOR@NYY, OAK@LAA, COL@ARI (4 games) |

### Per Game Summary

| gamePk | Matchup | Status | Grade | Score | Proj Score | Picks | Primary Chips |
|--------|---------|--------|-------|-------|------------|-------|---------------|
| 824274 | CLE @ DET | Live | B | 78 | 3.2 – 3.8 | 6 | Tigers RL -1.5 +130 to +145 · Under 7 or 7.5 |
| 823056 | PIT @ STL | Live | B | 75 | 3.9 – 3.3 | 6 | Pirates RL +1.5 -165 to -175 · Ashcraft K Over 6.5 |
| 822733 | NYM @ WSH | Preview | C | 62 | 4.2 – 4.5 | 5 | Nationals ML -115 to -125 |
| 823864 | ATL @ MIA | Preview | B | 72 | 3.5 – 3.1 | 6 | Braves ML -130 to -145 · Strider K Over 7.5 |
| 823545 | TOR @ NYY | Preview | B | 74 | 4.8 – 4.3 | 6 | Blue Jays ML +115 to +130 · Over 9 or 9.5 |
| 824031 | OAK @ LAA | Preview | A | 87 | 3.1 – 4.4 | 7 | Angels ML -155 to -170 · Soriano K Over 7.5 · Under 8 or 8.5 |
| 825083 | COL @ ARI | Preview | B | 76 | 3.6 – 4.8 | 7 | Diamondbacks RL -1.5 -130 to -145 · E Rodriguez K Over 5.5 |

### Slate Best Edge
OAK @ LAA (824031) is the A grade slate leader. Jose Soriano posts a 2.41 ERA and 10.1 K9 in 59.2 innings against Luis Severino's 5.1 BB9 and 4.45 ERA — the largest quality gap on the full slate. Angels ML, Soriano K Over 7.5, and Angels F5 ML are the top three plays.

### Weather Summary

| Park | Temp | Wind | Precip |
|------|------|------|--------|
| Comerica Park (CLE@DET) | 59F | 11 mph ENE | 0% |
| Busch Stadium (PIT@STL) | 64F | 7 mph NE | 0% |
| Nationals Park (NYM@WSH) | 60F | 6 mph NNE | 32% rain watch |
| loanDepot park (ATL@MIA) | 84F | 12 mph E | 3% |
| Yankee Stadium (TOR@NYY) | 62F | 1 mph SSE | 18% |
| Angel Stadium (OAK@LAA) | 72F | 8 mph SW | 0% |
| Chase Field (COL@ARI) | 94F | 10 mph WNW | 0% roof likely open |

Weather flag: NYM@WSH has 32% precip at 8:05 PM ET. Monitor for rain delay before wagering.

---

## Overlays Deployed

| File | Games |
|------|-------|
| odds_overlay.json | 7 |
| statcast_overlay.json | 7 |
| picks_log.json | 56 new entries (93 total) |

---

## Learnings Adjustments Applied

Active rule: Two or more MODEL_ERROR total losses yesterday — require second-pass validation on all over/total picks before publishing; cross-check run environment metrics and bullpen usage.

Carryover rule: When stacking K over and Under total on the same starter, require ERA below 3.50 in last 5 starts before publishing both as separate picks.

Applied per game:
- CLE@DET: Under cross-checked against ENE wind and pitcher park factor — thesis holds
- PIT@STL: Ashcraft K pick validated against 9.1 K9 and Cardinals contact tendencies — thesis holds
- NYM@WSH: Over total moved to long shot due to rain risk and walk rate volatility; card capped at C with one chip
- ATL@MIA: Strider small sample (14.2 IP) flagged — grade held at B; K prop validated
- TOR@NYY: Rodon 8 IP sample flagged — over retained given extreme 9.0 BB9 at Yankee Stadium
- OAK@LAA: Under total cross-checked — Soriano quality suppresses Athletics; thesis holds at A
- COL@ARI: Total chip removed; run line and K chip retained with roof status unknown

---

## GitHub Commit

Hash: 4669a8f56d85d006c908ebf2b76cad00bac74556
Branch: main
Push status: SUCCESS
Files committed: index.html, odds_overlay.json, statcast_overlay.json, picks_log.json
Deploy: Cloudflare Pages auto-deploys on push — no wrangler used
Live URL: https://mlb-betting-dashboard-v2.pages.dev

---

## Errors / Fallbacks

- Overlay files (bullpen_availability_overlay.json, rolling_form_overlay.json, catcher_framing_overlay.json, etc.) not accessible — resource deadlock on workspace mount prevented all read methods. Fallback: built-in park factor estimates and general bullpen form assessments used.
- Pitcher stats collected successfully via MLB Stats API batch call for all 14 confirmed starters.
- Weather collected via Open-Meteo for all 7 parks — wind unit confirmed as km/h and converted correctly to mph.
- Two Live games (CLE@DET, PIT@STL): morning verdict locked; picks and paragraphs generated from confirmed pre-game data.
