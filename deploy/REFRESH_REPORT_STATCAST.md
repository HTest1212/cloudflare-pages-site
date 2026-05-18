# Statcast Overlay Refresh Report

Run timestamp UTC: 2026-05-18T23:45:00Z
Slate date: 2026-05-18
Run window: 6 AM ET scheduled (executed with games already in progress)

## Yesterday's Slate (2026-05-17)

15 Final games processed. 12 boxscores were pre-fetched; 3 additional (825006 SF@ATH, 824034 LAD@LAA, 823138 SD@SEA) fetched during this run. All boxscore JSON files saved to host Mac filesystem.

Player IDs extracted via MLB Roster API:
- Pitchers refreshed: 54 unique IDs
- Batters refreshed: 37 unique IDs
- Total unique player IDs: 91

Sabermetrics inline for 5 pitchers: Paul Skenes fip 2.64/war 1.64, Chase Burns fip 3.51/war 1.28, Chris Sale fip 3.22/war 1.15, Tanner Bibee fip 4.25/war 0.66, Sandy Alcantara fip 3.49/war 1.31.

## Today's Slate (2026-05-18)

14 games. Lineup endpoint returned empty arrays at query time. Probable starters inferred from roster rotation data.

Matchups:
- 824277 CLE@DET: Bibee vs Mize
- 822980 BAL@TB: Wells vs McClanahan
- 823465 CIN@PHI: Burns vs Nola
- 823867 ATL@MIA: Sale vs Alcantara
- 822734 NYM@WSH: TBD vs Cavalli
- 823549 TOR@NYY: Rodriguez vs TBD
- 824114 BOS@KC: Bello vs Singer
- 823705 HOU@MIN: TBD vs TBD
- 824680 MIL@CHC: TBD vs TBD
- 824357 TEX@COL: TBD vs TBD
- 824035 ATH@LAA: TBD vs TBD
- 823301 LAD@SD: TBD vs TBD
- 825087 SF@ARI: TBD vs TBD
- 823137 CWS@SEA: TBD vs TBD

Pitchers with confirmed IDs: 12/28. Batters in overlay: 33.

## GitHub Push

Branch: main
Commit: 6a23288f40594271a9eb6c0171b9a6a3e3f94c28
Message: Auto refresh statcast 2026-05-18 06:00
Status: Pushed successfully (clean, no rebase needed)
Note: Git run from /tmp clone due to FUSE mount bus errors on Linux.

## Cloudflare Deploy

Project: mlb-betting-dashboard-v2
Method: GitHub Actions auto-deploy on push to main
Status: Triggered by commit 6a23288
Live URL: https://mlb-betting-dashboard-v2.pages.dev

## Data Gaps

1. Statcast pitch files saved to Mac /var/folders, not accessible from Linux container.
2. 16 of 28 pitcher slots TBD (rosters not retrieved for NYM, NYY, KC, HOU, MIN, MIL, CHC, TEX, COL, ATH, LAA, LAD, SD, SF, ARI, CWS, SEA).
3. Sabermetrics returned inline data for only 5 pitchers and 2 batters.
4. player_stats calls saved to host filesystem as large files.

Source: MLB Stats API via mlb-api-mcp. Season window 2026-04-18 to 2026-05-18.
