# MLB Dashboard Refresh Report

Window: early afternoon (2:08 PM)
Run timestamp UTC: 2026-06-24T18:14:00Z
Slate date: 2026-06-24  Game count: 16
Commit: 6d18e69  Push status: success (remote HEAD matches local)
Live verify: window and 16 grades and projected scores all resolve non zero

## API data quality
Pitchers: 32 probables confirmed via schedule-api. Two returned no season stats and used a league average fallback: Mitch Bratt (STL debut) and JP Sears (SD). Both capped conviction on their cards.
Weather: 13 outdoor or retractable parks fetched successfully from Open Meteo. Domes skipped: Tropicana Field. Two Live games used prior weather context.
Lineups: confirmed both for TEX@MIA, CHC@NYM g1, CLE@CWS, BOS@COL; home confirmed for BAL@LAA; all other Preview games projected and capped at B.

## Active learnings adjustments applied
- LOCK GUARD ACTIVE: A tier publication suspended until rolling 14d Lock win rate recovers to 0.85, slate capped at B
- Recent form two way modifier from rolling_form_overlay; cold teams never graded ML above C
- Projected lineup cards capped at B plus 84, TBD or debut starter capped at C with one chip
- K over chips require a six inning floor and trailing form clearing the line; short leash arms blocked
- Coors over not Locked on wind alone, altitude variance caps at B
- Under blocked when both lineups rank top 12 in trailing runs per game
- Factor overlays for park, umpire, and framing absent so top tier held to B

## Per game summary
- TEX @ MIA (823850) Live: B 76, proj 3.4 to 3.6, picks 6. Chips: Under 8 or 8.5 | deGrom K over 6.5
- CHC @ NYM (823613) Live: B 74, proj 3.8 to 3.6, picks 6. Chips: Under 8 | NRFI
- CHC @ NYM (823611) Preview: C 66, proj 4.4 to 3.9, picks 6. Chips: Cubs F5 ML +105 to +120
- CLE @ CWS (824583) Preview: B 77, proj 3.5 to 3.7, picks 6. Chips: Under 8 or 8.5 | NRFI
- BOS @ COL (824341) Preview: B 75, proj 5.6 to 6.1, picks 6. Chips: Over 11 or 11.5 | Boston Red Sox ML +100 to +115
- BAL @ LAA (824018) Preview: B 74, proj 3.6 to 4.8, picks 6. Chips: Los Angeles Angels ML -120 to -135 | Soriano K over 5.5
- SEA @ PIT (823367) Preview: B 78, proj 2.9 to 3.2, picks 6. Chips: Under 7 or 7.5 | NRFI
- KC @ TB (822965) Preview: B 76, proj 5.1 to 3.5, picks 6. Chips: Kansas City Royals ML -115 to +105 | Royals over 4.5 team runs
- NYY @ DET (824259) Preview: B 78, proj 3.4 to 3.7, picks 6. Chips: Under 8 | Skubal K over 6.5 | Detroit Tigers ML -110 to +110
- PHI @ WSH (822719) Preview: B 79, proj 5.7 to 4.6, picks 6. Chips: Over 9 or 9.5 | Philadelphia Phillies ML -130 to -145
- HOU @ TOR (822798) Preview: B 74, proj 4.1 to 5.0, picks 6. Chips: Toronto Blue Jays ML -125 to -140 | Blue Jays over 4.5 team runs
- MIL @ CIN (824500) Preview: C 65, proj 4.5 to 4.0, picks 6. Chips: Milwaukee Brewers ML -105 to +110
- LAD @ MIN (823691) Preview: B 76, proj 3.4 to 3.6, picks 6. Chips: Under 8 | Joe Ryan K over 6.5
- ARI @ STL (823041) Preview: C 60, proj 4.4 to 4.2, picks 6. Chips: Arizona over 4.5 team runs
- ATL @ SD (823284) Preview: B 72, proj 3.1 to 3.9, picks 6. Chips: Under 8 | San Diego Padres ML -120 to -135
- ATH @ SF (823208) Preview: B 75, proj 3.3 to 3.4, picks 6. Chips: Under 8 or 7.5 | NRFI

## Overlay counts
odds_overlay.json: 16 games. statcast_overlay.json: 16 games. picks_log.json: 41 new pending entries for Preview games, total 976.
Factor overlays absent (park_factors, park_wind_rules, umpire_factors, catcher_framing, pitch_matchup); analyst defaults used and top tier held to B.

## Notes and fallbacks
Lock guard cap_active (rolling 14d Lock win rate 0.3333), so no A tier published; slate ceiling B 84.
Bratt and Sears stat fallback noted above. .env unreadable due to mount deadlock; PAT recovered from clone .git/config.