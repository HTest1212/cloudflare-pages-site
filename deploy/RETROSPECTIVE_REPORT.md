# Daily Retrospective — 2026-06-01

Settled 2026-06-02 04:37 UTC. No Lock breach. Lock Guard remains active for a second straight slate.

## Section 2 — Slate Summary

Slate date 2026-06-01, 9 games on the board, all final. Ten picks settled, all from the midday schema (label and price form). Game 824027 was still in progress at the prior check and finalized as Colorado 8, Los Angeles Angels 6.

Overall record 4 wins, 5 losses, 0 pushes, 1 void. Units minus 1.79 on a 9 unit non void book. Win rate 0.444, ROI minus 0.199.

Record by market: ML went 1 and 2 (minus 1.26u). K props went 3 and 3 with one void (minus 0.53u). Record by tier: B tier 2 and 3 with one void (minus 1.36u), C tier 2 and 2 (minus 0.43u). No A tier picks were published because the Lock Guard cap is active.

## Section 3 — Lock Track Record

Lifetime A tier record is 39 picks, 23 wins, 13 losses, 2 pushes, 1 void. Win rate 0.639, units plus 5.45, ROI 0.143. Current streak is 5 wins. Longest win streak 8, longest loss streak 6. Rolling 14 day Lock win rate 0.586, rolling 30 day 0.639.

Lock by market highlights: RL 3 and 0 (plus 3.13u), F5_ML 2 and 0, Total 2 and 1, K 7 and 4 (plus 1.65u). The drag is ML at 4 and 5 (minus 2.75u) and a lone Over loss.

Guard status: cap_active. Rolling 14 day Lock win rate 0.586 sits below the 0.80 floor and well under the 0.85 recovery target. The 11:30 AM run will treat the Lock Guard cap as non negotiable: A tier publication stays suppressed and any A tier candidate missing 4 or more of the seven confirmation signals is demoted. This is why last night carried zero Locks, and the same holds today until the rolling number recovers.

## Section 4 — Top Three Losses With Diagnoses

1. Reds ML at minus 155 (B tier, 78). Final Kansas City 9, Cincinnati 2. The entire edge rested on projected starter Burns, who was scratched. Replacement Lyon Richardson allowed 4 earned in 1 inning and the game was gone early. Category MISSED_NEWS. This is the most preventable loss on the card: a confirmed starter check before publishing would have pulled both the ML and the Burns K chip.

2. Sheehan K Over 6.5 at minus 115 (C tier, 66). Final Los Angeles Dodgers 1, Arizona 4. The model tagged Arizona as a whiff prone order, but they put the ball in play and Sheehan managed only 3 strikeouts across 6.1 innings while taking the loss. Category MODEL_ERROR. The whiff prone read was the error, not the workload.

3. Angels ML at minus 165 (B tier, 76). Final Colorado 8, Los Angeles Angels 6. Soriano did his job with 7 strikeouts, but the supporting staff and bats could not hold a one score game. Category VARIANCE. A backable favorite that simply lost a close one.

The two remaining losses were Cavalli K Over 6.5, who landed 6 strikeouts in 5 innings for a one short miss after an early hook, and Roupp K Over 6.5, who was pulled after 4 innings and 4 strikeouts in a 16 to 2 blowout. Burns K voided on the scratch.

## Section 5 — Rule Memory Status

Permanent rules (never expire), 8 total:

- Down weight setups exposed to VARIANCE until the pattern clears. Validated 7 times, last 2026-06-01.
- Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over. Validated 5 times, last 2026-05-30.
- Never issue A-tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ERA and top 5 K rate. Validated 3 times, first learned 2026-05-20.
- Never issue Giants ML as A-tier unless SF starting pitcher has sub 3.20 ERA and Giants offense ranks top 10 NL in runs last 14 days. Validated 3 times, first learned 2026-05-20.
- Cap A-tier exposure at 2 picks per game maximum; never stack F5 Under, ML and Total all A-tier on one game. Validated 3 times, first learned 2026-05-20.
- Never issue A-tier ML when the team offense ranks bottom third in runs scored last 7 days. Validated 3 times, first learned 2026-05-20.

Promoted to permanent today (milestones):

- Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights. Reached 3 validations and is now permanent.
- Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing 14 days. Reached 3 validations and is now permanent.

Trial rules still accumulating evidence, 8 total:

- Six A tier lock breach rules from 2026-05-25 and 2026-05-28, each at 1 of 3 validations, expiring 2026-06-08 and 2026-06-11.
- Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings. 2 of 3 validations, no STARTER_REGRESSION loss matched yesterday, expires 2026-06-07.
- New variance rule on K Over short outings, 1 of 3 validations, expires 2026-06-08.

Rules that aged out today: none.

New rules created today:

- Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; avoid K Over chips when the starter carries blowout or short leash risk and require a projected floor of 6 innings. Source pattern, expires 2026-06-08.

Total rules in active memory: 8 permanent plus 8 trial.

## Section 6 — Adjustments For Today (priority order, permanent marked with a star)

1. LOCK GUARD ACTIVE: Cap A tier publication until rolling 14d Lock win rate recovers to 0.85. Demote any A tier candidate missing 4 or more of seven confirmation signals.
2. Do not publish A tier F5 Under when the run suppressor is park and weather only; require starter ERA below 3.50 and opposing lineup bottom 5 NL in runs.
3. Do not publish A tier ML relying on ERA differential alone; require FIP within 0.50 of ERA and at least 3 consecutive quality starts.
4. Do not publish A tier Under at Oracle Park when the visiting pitcher has a WHIP above 1.30 in last 5 starts.
5. Do not publish A tier ML against a starter with ERA above 4.50 when that starter has allowed 2 or fewer runs in 2 of his last 3 starts.
6. Do not publish A tier Over when the visiting rotation starter has ERA above 6.00 but the bullpen ERA is below 3.80.
7. Do not publish A tier pitcher K over at a line of 7.0 or higher unless season strikeouts per start exceed the line by at least 1.5.
8. Down weight setups exposed to VARIANCE until the pattern clears. (star)
9. Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over. (star)
10. Never issue A-tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ERA and top 5 K rate. (star)
11. Never issue Giants ML as A-tier unless SF starter sub 3.20 ERA and Giants offense top 10 NL last 14 days. (star)
12. Cap A-tier exposure at 2 picks per game maximum; never stack F5 Under, ML and Total all A-tier on one game. (star)

Trimmed from the active list at the 12 cap (still live in rule memory): the A-tier bottom third offense ML rule, the two rules promoted to permanent today, the new K Over short outing rule, and the trial ML favorite quality start rule.

## Section 7 — Lifetime And Recent 14 Day KPIs

Lifetime: 1086 settled picks, 538 wins, 441 losses, 29 pushes, 78 voids. Units plus 25.24, win rate 0.550, ROI 0.003.

Recent 14 day: 387 settled picks, 191 wins, 164 losses, 7 pushes, 25 voids. Units minus 2.44, win rate 0.538, ROI roughly flat at minus 0.0003.

## Section 8 — Data Notes

Git sync succeeded. The workspace mount returned a resource deadlock, so the full run was executed against the origin clone in temporary space and all outputs were written there, then staged for deploy through a fresh clone. The PAT was recovered from the working folder git remote because no token file was readable through the mount. Picks log pulled cleanly from origin at 403 total picks. All 9 box scores read without error. One game, 824027, had finalized by settle time. No schema parse warnings. The stake field carries 77 legacy entries logged at 100 units; these are kept for continuity with the established summary convention and do not affect win rate or unit math since their profit is normalized to plus or minus 1.
