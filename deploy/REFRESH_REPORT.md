# MLB Dashboard Refresh Report

Window: early afternoon (2:08 PM)
Run timestamp (UTC): 2026-07-01T18:55Z
Slate date: 2026-07-01
Game count: 14 (5 Live, 9 Preview)

## API data quality
Schedule and probable pitchers pulled from MLB Stats API (schedule hydrate). Pitcher season stats batch fetched in one people endpoint call for 27 confirmed starters.
Pitchers confirmed: 27 of 28 starter slots. TBD: 1 (Los Angeles Dodgers at Athletics, away starter not posted, league average applied, grade capped at C).
Weather (Open Meteo) success per outdoor park: Citizens Bank 98.6F wind 5 out to left; Truist 92.6F wind 7; Kauffman 94.2F wind 16; Coors 91.2F wind 12; Sutter Health 84.5F wind 11. Retractable roofs (Rogers Centre, Daikin, American Family, Chase) treated as controlled or closed.

## Per game (grade, projected score, picks, primary chips)
822791 NYM at TOR  B- 71  3.6-3.7  6 picks  Under 8.5, Peralta K over 5.5
823446 PIT at PHI  B 82   3.9-4.2  6 picks  NRFI, Skenes K over 7.5
824905 STL at ATL  B- 73  3.4-3.6  6 picks  Under 8, F5 Under 4.5
824094 TB at KC    B- 73  4.6-4.0  6 picks  Rays ML, McClanahan K over 5.5
824174 MIN at HOU  C+ 67  4.4-4.6  6 picks  Bradley K over 5.5, Imai K over 5.5
823767 CIN at MIL  C 62   4.0-4.0  6 picks  Under 8.5
824337 MIA at COL  B- 72  5.2-4.6  6 picks  Marlins ML, Meyer K over 5.5
824985 LAD at ATH  C 60   5.4-4.6  6 picks  Over 9.5 (TBD cap)
825064 SF at ARI   C 61   4.4-4.6  6 picks  Over 8.5
824818 CWS at BAL  Live B- 72  Top 8 BAL 5-1 (morning verdict locked)
824419 TEX at CLE  Live B 74   Top 6 CLE 5-1 (morning verdict locked)
824740 WSH at BOS  Live B 75   Mid 4 WSH 7-0 (morning verdict locked)
823530 DET at NYY  Live C+ 69  Top 6 DET 1-0 (morning verdict locked)
824660 SD at CHC   Live B+ 80  End 2 CHC 4-0 (morning verdict locked)

No new A tier published. Lock guard healthy, honored.

## Overlay game counts
odds_overlay.json: 14 games. statcast_overlay.json: 14 games (ERA based xFIP/FIP estimates). picks_log.json: 15 new pending entries appended (Preview primary chips), 1157 total, sorted date desc then confidence desc.
Read overlays: rolling_form (fresh), bullpen_availability (dated Jun 21, used directionally), splits/bvp/hitter_advanced consulted as carryover rules.

## Learnings adjustments applied
Loaded 12 adjustments_for_today. Applied across cards: VARIANCE downweight on every card; under totals tightened where both lineups top 12 L14 (PIT/PHI full game under suppressed, played NRFI and F5 instead); Coors road ML and Coors Over capped at B/C (MIA at COL); K over lines held at 5.5 for short workload starters and floor check; cold team ML never graded above C (Athletics, Giants not backed as favorites); Giants ML A tier suppressed.

## Deploy
Commit: 0441f92 "Auto refresh 208pm 2026-07-01". Push status: success. Remote HEAD 0441f926 confirmed.
Cloudflare Pages auto deploy verified: live URL returns HTTP 200, date 2026-07-01, window "early afternoon (2:08 PM)", all 14 cards resolve non zero grade and projected score.

## Errors and fallbacks
Workspace mount deadlock (errno 35) blocked reading .env and learnings.json from the working folder; recovered PAT from the fresh clone .git/config and read learnings from the clone. Bullpen overlay is 10 days stale; used directionally only. Statcast velocity feed not queried this run (ERA based estimates used per spec).
