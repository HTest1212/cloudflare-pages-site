# Statcast Refresh Report -- 2026-05-21

**Run type:** Scheduled (mlb-statcast-refresh-6am)
**Generated:** 2026-05-21T10:45:00Z
**Commit:** 6df389e
**Deploy:** Cloudflare Pages via GitHub Actions (push to main)
**Live URL:** https://mlb-betting-dashboard-v2.pages.dev

## Slate Summary

Date: 2026-05-21 | Games: 7

| gamePk | Matchup | First Pitch UTC | Venue |
|--------|---------|-----------------|-------|
| 824274 | CLE @ DET | 17:10 | Comerica Park |
| 823056 | PIT @ STL | 17:15 | Busch Stadium |
| 822733 | NYM @ WSH | 20:05 | Nationals Park |
| 823864 | ATL @ MIA | 22:40 | loanDepot park |
| 823545 | TOR @ NYY | 23:05 | Yankee Stadium |
| 824031 | ATH @ LAA | 01:38+1 | Angel Stadium |
| 825083 | COL @ ARI | 01:40+1 | Chase Field |

## Pitcher Statcast Coverage: 14 of 14

| Pitcher | Team | Pitches 15d | Avg Velo | xwOBA | SwStr% |
|---------|------|-------------|----------|-------|--------|
| Tanner Bibee | CLE | 185 | 87.5 | .235 | 45.4% |
| Brant Hurter | DET | 95 | 88.5 | .272 | 43.2% |
| Paul Skenes | PIT | 251 | 92.4 | .163 | 54.6% |
| Dustin May | STL | 175 | 93.9 | .273 | 48.6% |
| Tobias Myers | NYM | 100 | 90.3 | .273 | 48.0% |
| Cade Cavalli | WSH | 183 | 91.8 | .292 | 50.8% |
| Chris Sale | ATL | 182 | 87.5 | .251 | 56.6% |
| Sandy Alcantara | MIA | 261 | 92.5 | .219 | 34.9% |
| Yariel Rodriguez | TOR | 44 | 90.5 | .465 | 47.7% (SMALL SAMPLE) |
| Will Warren | NYY | 176 | 91.1 | .197 | 65.3% |
| Aaron Civale | ATH | 162 | 85.9 | .288 | 50.6% |
| Grayson Rodriguez | LAA | 75 | 89.8 | .379 | 49.3% |
| Antonio Senzatela | COL | 30 | 92.8 | .232 | 48.3% (SMALL SAMPLE) |
| Zac Gallen | ARI | 251 | 86.8 | .257 | 46.6% |

## Batter Coverage: 41 of 46

statcast_fetched=false (5): Chase DeLauter (CLE), Bo Bichette (NYM), Andres Gimenez (TOR), Trent Grisham (NYY), Luis Garcia (ARI)

## Pipeline Notes

- Statcast window: 2026-05-06 to 2026-05-21 (15-day rolling)
- FUSE workspace deadlock workaround: cloned repo to /tmp, committed and pushed from native Linux fs
- index.lock stale artifact from prior context session; unresolvable from sandbox
- Deploy: git push main triggered GitHub Actions (cloudflare/wrangler-action@v3)

## Verification

curl https://mlb-betting-dashboard-v2.pages.dev/statcast_overlay.json
Result: asof=2026-05-21T10:45:00Z, games=7 CONFIRMED LIVE
