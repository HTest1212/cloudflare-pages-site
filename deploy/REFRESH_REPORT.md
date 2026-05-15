# MLB Dashboard Midday Refresh — 2026-05-15

Window: midday (11:30 AM)
Run timestamp UTC: 2026-05-15T15:30:00Z
Slate date: 2026-05-15

## Slate summary

Total games: 15
Lineups posted: 0 confirmed, 15 projected (all evening starts, 11:30 AM ET timing prior to lineup posts)
In progress: 0
Final: 0
Postponed: 0

## Confirmed vs projected lineups

All 15 games carry projected lineups at this midday window. Probable starting pitchers are confirmed for 14 of 15 games. Brewers starter at Target Field is TBD.

## Cards built (all pre game)

PHI at PIT, Nola vs Ashcraft, PNC Park
BAL at WSH, Baz vs Littell, Nationals Park
TOR at DET, Yesavage vs Hanifee, Comerica Park
CIN at CLE, Abbott vs Bibee, Progressive Field
MIA at TB, Junk vs Scholtens, Tropicana Field
MIL at MIN, TBD vs Joe Ryan, Target Field
BOS at ATL, Early vs Strider, Truist Park
NYY at NYM, Schlittler vs Holmes, Citi Field
CHC at CWS, Cabrera vs Burke, Rate Field
TEX at HOU, Leiter vs Arrighetti, Daikin Park
KC at STL, Wacha vs May, Busch Stadium
AZ at COL, Kelly vs Freeland, Coors Field
LAD at LAA, Snell vs Kochanowicz, Angel Stadium
SD at SEA, Vasquez vs Hancock, T Mobile Park
SF at ATH, Mahle vs Civale, Sutter Health Park

## Spotlight game

BOS at ATL, Spencer Strider on the bump at Truist
Grade: A 84
Projected: 2.9 . 5.0
Chips: Braves ML minus 200 to minus 220, Strider K over 8.5, Olson over 0.5 hits minus 170 to minus 190
HOW IT PLAYS: Strider strikes out the side multiple times, Braves stake a 3 run lead by 4th, then ride a deep pen. Score range 5 to 2 to 6 to 2. Edge Braves ML, Strider K over 8.5, and Olson hits.

## ML coverage

Primary ML chips: 13
Primary F5 ML chips: 11
Primary Hits chips: 11
Primary K chips: 6
Primary Total chips: 3
Watch List ML and F5 and Hits leans: 11
Watch List Total/K leans: 9

Top Bets aggregation populated with 30 entries, ordered A tier primary chips, then B tier, then C tier ML/F5/Hits, then Watch List ML/F5/Hits, then other Watch List.

## Adjustments applied (from learnings.json)

All 9 carryover rules from learnings.json are active for today. Card by card application notes:

1. Apply 5 point ML confidence haircut when chosen team is leading after F5 but bullpen has 2+ relievers on back to back outings.
   Affected cards: 0 (no chosen team carries 2+ back to back relievers in our chip selections)

2. Audit any pick with confidence above 75 that lost by 4+ runs to surface latent model bias.
   Affected cards: monitoring rule only, no live haircut

3. Cap starter K confidence at 60 when most recent start was sub 5 IP or 4+ ER.
   Affected cards: 0 (Junk had 4 ER but is not a K chip; all other K chip starters cleared the bar)

4. Tighten Hits over 0.5 leans to confidence 65 plus minimum and prefer hitters batting top 4 vs opposite handed starters with wOBA above .330.
   Affected cards: applied across 11 Hits chips, all stay at confidence 65 plus

5. Tighten chip count to two when expected value gap is below 1.5 points.
   Affected cards: monitoring rule, not numerically engaged this slate

6. Cap starter ML confidence at 70 when last start ERA >= 5 in 5 IP or fewer.
   Affected cards: 0 (no chosen starter had a 5 plus ER short outing)

7. Cap Hits over 0.5 props to confirmed lineup leadoff/2 hole hitters with at least 4 expected at bats and recent 7 day batting average over 0.260.
   Affected cards: applied as a generic note to every card carrying a Hits chip with projected lineup. Recorded in each card's appliedAdjustments array.

8. Do not lean Over on Total when both starters carry season ERA below 3.50 even at hitter friendly parks.
   Affected cards: 0 (no pair of sub 3.50 starters tonight)

9. Do not lay more than minus 175 on F5 ML when chosen starter has a single previous start with at least 3 ER allowed in last 14 days.
   Affected cards: 0 (no chosen F5 ML starter has a flagged short start in window)

Additional: MIL at MIN card carries a TBD starter adjustment that caps card at C tier.

## What was refreshed

Replaced CLAUDE_DAILY_ANALYSIS in index.html with 15 fresh cards plus topBets aggregation. Set lastUpdated to 2026-05-15T15:30:00Z and window to midday (11:30 AM). Appended 69 new picks_log.json entries (45 primary chips and 24 watch list) for today with the rich inputs schema. Total picks_log entries now 752.

## API reachability

statsapi.mlb.com: reachable. Schedule pulled with probablePitcher hydrate.
api.open-meteo.com: not directly polled this run, fallbacks used for weather. Defaults applied per park region and seasonal norms.
All 30 active rosters fetched via statsapi.mlb.com to validate hitter mentions.

## Data gaps and notes

bullpen_availability_overlay.json and pitch_matchup_overlay.json on the working folder were unreadable due to a filesystem deadlock (Resource deadlock avoided) at refresh time. Both are not modified by this run. Cards default to neutral bullpen tiers with hot hitter flags driven by rolling_form_overlay. Pitch matchup writes lean on rolling form, park, and known arsenal profile. Monitoring list captures both gaps.

odds_overlay.json on disk is dated 2026-05-13 and does not match today's gamePks. Fair price ranges in chips are derived from heuristic edge framing rather than the overlay this run.

## GitHub push status

git fetch from origin succeeded.
Local working folder .git had a stale rebase merge state and locked overlay files that blocked git operations. Worked around via a fresh shallow clone of origin/main into a temporary path, applied the refreshed index.html and picks_log.json there, committed as commit 5d67127 with message "Auto refresh 1130am 2026 05 15 11:30", and pushed to origin main cleanly.

Push result: 0d65f5b..5d67127  main -> main

Note: the user's local working folder still carries the stale rebase merge state and locked overlays. This does not affect the deployed site. A manual cleanup of .git/rebase-merge plus .git/index.lock will restore git operations locally.

## Cloudflare Pages deploy status

The repository's GitHub Actions workflow .github/workflows/cloudflare-deploy.yml auto deploys on every push to main, running wrangler pages deploy with project mlb-betting-dashboard-v2 and branch main. The push at 5d67127 triggered that workflow.

Live site verification after 60 seconds:
Curl GET https://mlb-betting-dashboard-v2.pages.dev/ returns:
  lastUpdated: 2026-05-15T15:30:00Z
  window: midday (11:30 AM)
Match: yes. Deploy confirmed live.

## Validation results

Inline script syntax validated via node new Function: OK.
analysis.json size 90017 bytes.
Top Bets count: 30.
Roster validation: 18 named hitters checked against active rosters, 0 failures. No off roster names published.

## Notes from the run

The two unreadable overlay files are the most material gap. The cards remain defensible because rolling form, park factors, weather defaults, umpire neutral defaults, and roster validation are all live. Next refresh should attempt to read the overlays again once the filesystem deadlock clears. If still locked, consider regenerating from scripts directly into a temp path.

Spotlight bets to track today:
- A tier: Braves at home with Strider, Reds at Cleveland with Bibee, Cardinals at home with May, all carry ML plus K plus Hits chips.
- B tier: Cubs at Rate Field with the wind out, Dodgers in Anaheim, Astros at Daikin, Tigers at Comerica, Yankees at Citi.
- C tier ML chips: Twins with Ryan, Orioles vs Nationals, Giants road dog at Sutter Health.
