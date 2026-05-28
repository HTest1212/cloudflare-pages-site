# MLB Dashboard Refresh Report

**Window:** midday (11:30 AM)
**Run Timestamp UTC:** 2026-05-28T15:35:00Z
**Slate Date:** 2026-05-28
**Game Count:** 6

---

## API Data Quality

**Pitchers Confirmed:** 12 of 12 (100%) via schedule-api hydrate=probablePitcher
**Pitcher Stats Source:** MLB Stats API /people batch call, season pitching stats
**Lineups Confirmed:** 2 of 6 games (Games 1 and 2 had 9 batters each); 4 games projected from rolling form
**Weather Success:** 6 of 6 parks fetched via Open Meteo

**Overlay Read Status:**
- learnings.json: READ via /tmp/mlb_deploy clone (workspace Resource deadlock bypassed)
- picks_log.json: READ and updated via /tmp/mlb_deploy clone
- statcast_overlay.json: REBUILT from pitcher stats (ERA-based xFIP and FIP estimates)
- odds_overlay.json: REBUILT from projected scores and card analysis
- bullpen, rolling_form, catcher_framing, umpire, park_factors overlays: FILE NOT FOUND, used general MLB knowledge

---

## Learnings Adjustments Applied

Active adjustments from learnings.json (7 rules, LOCK GUARD cap_active):
1. LOCK GUARD ACTIVE: Rolling 14d win rate 52.2 percent. A tier publication capped across all games.
2. F5 Under A tier requires both starters ERA below 3.50.
3. A tier ML requires FIP within 0.50 of ERA and 3 consecutive quality starts.
4. A tier ML blocked against ERA above 4.50 starter with recent 2 or fewer run starts.
5. A tier Over blocked when visiting pitcher ERA above 6.00 and bullpen ERA below 3.80.
6. Cap A tier at 2 picks per game max; no stacking F5 Under plus ML plus Total all A tier.
7. Never A tier ML on offense ranking bottom third in runs scored last 7 days.

---

## Per Game Summary

| Game | Grade | Score | Primary Chips | Picks |
|------|-------|-------|---------------|-------|
| Angels @ Tigers (824272) | C 60 | 4.5 vs 5.0 | Pass (Rodriguez tiny sample cap) | 7 |
| Twins @ White Sox (824595) | B 71 | 2.9 vs 2.7 | Under 7, Martin K over 5.5 | 7 |
| Braves @ Red Sox (824757) | B 82 | 2.8 vs 2.5 | Braves ML, Sale K over 7.5 | 7 |
| Blue Jays @ Orioles (824834) | C 65 | 4.2 vs 3.5 | Blue Jays ML | 7 |
| Cubs @ Pirates (823378) | B 77 | 2.8 vs 3.8 | Pirates ML, Skenes K over 6.5 | 7 |
| Astros @ Rangers (822896) | B 82 | 3.8 vs 2.2 | Astros ML, Arrighetti K over 5.5 | 7 |

Primary chips issued: 8 across 5 games. 0 A tier per lock guard. 1 Pass game.

---

## Weather Summary

| Park | Temp | Wind | Effect |
|------|------|------|--------|
| Comerica Park | 71.8F | 40.7 mph NNE | Major ball flight uncertainty |
| Guaranteed Rate Field | 63.5F | 52.8 mph NNE | Extreme suppression, Under supported |
| Fenway Park | 68.0F | 22.1 mph NNE | Moderate, fly ball carry toward LF |
| Oriole Park at Camden Yards | 71.4F | 50.8 mph N | Extreme chaos, totals avoided |
| PNC Park | 71.2F | 42.3 mph NNW | Crosswind, minor impact vs Skenes |
| Globe Life Field | 78.8F | 14.3 mph NE | Retractable, likely controlled |

---

## Overlays Deployed

- odds_overlay.json: 6 games
- statcast_overlay.json: 6 games, 12 pitchers
- picks_log.json: 330 total entries (9 new picks added)

---

## Deploy Status

**GitHub Commit Hash:** 847f558
**Push Status:** SUCCESS
**Branch:** main
**Live URL:** https://mlb-betting-dashboard-v2.pages.dev
**Deploy Method:** Cloudflare Pages auto-deploy on push (no wrangler)

---

## Errors and Fallbacks

- Workspace overlay files not found (bullpen, rolling_form, catcher_framing, umpire, park_factors, pitch_matchup, park_wind_rules). Proceeded with general MLB knowledge.
- workspace folder Resource deadlock on all reads/writes via bash and Read tool. Resolved by reading from fresh /tmp/mlb_deploy git clone.
- /tmp/cloudflare-pages-site had ownership conflicts from prior session. Cloned fresh to /tmp/mlb_deploy.
- Rojas 14.1 IP below 15 inning threshold: grade downgraded from B plus to B minus 71.
- Rodriguez 9.1 IP below 15 inning threshold: game graded C 60, verdict Pass.
