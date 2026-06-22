import json, datetime, statistics as st
OUT="/sessions/happy-serene-gates/mnt/outputs"
NOW=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
d=json.load(open(f"{OUT}/form_data.json"))
teams=d["teams"]
LG_RG=st.mean(t["season_RG"] for t in teams.values())
LG_RAG=st.mean(t["season_RAG"] for t in teams.values())

def weights(n):
    # most recent 4 -> 1.5, next 3 -> 1.0, rest -> 0.6 ; list aligned oldest..newest
    w=[]
    for i in range(n):
        from_end=n-i  # 1 = newest
        w.append(1.5 if from_end<=4 else (1.0 if from_end<=7 else 0.6))
    return w

def wmean(vals,w):
    s=sum(w)
    return sum(v*wi for v,wi in zip(vals,w))/s if s else 0

def pctile(vals,p):
    if not vals: return 0
    s=sorted(vals); k=(len(s)-1)*p; f=int(k); c=min(f+1,len(s)-1)
    return s[f]+(s[c]-s[f])*(k-f)

out_teams={}
for name,t in teams.items():
    log=t["log"][-10:]
    n=len(log)
    if n<5:
        out_teams[name]={"games15":n,"ops15":0,"opsBaseline":0.715,"deltaOps":0,
            "runsPg15":0,"runsPgBaseline":t["season_RG"],"tier":"neutral",
            "formScore":50,"components":{},"note":"Insufficient recent sample.","insufficient":True}
        continue
    w=weights(n)
    RF=[g["RF"] for g in log]; RA=[g["RA"] for g in log]; wins=[1 if g["win"] else 0 for g in log]
    # opponent run-prevention factor: scoring on a stingy staff counts more
    opp_off=[]; opp_def=[]
    for g in log:
        o=teams.get(g["opp"])
        opp_def.append(o["season_RAG"] if o else LG_RAG)  # opp pitching/defense
        opp_off.append(o["season_RG"] if o else LG_RG)     # opp offense
    # OFFENSE: opponent-adjusted, winsorized, recency-weighted, consistency-penalized
    adjRF=[rf*(LG_RAG/od if od>0 else 1) for rf,od in zip(RF,opp_def)]
    cap=pctile(adjRF,0.85)
    winRF=[min(v,cap) for v in adjRF]
    off_metric=wmean(winRF,w)
    # consistency penalty: share of raw runs from single biggest game
    tot=sum(RF) or 1
    top_share=max(RF)/tot
    penalized=top_share>0.40 and n>=6
    if penalized:
        off_metric=0.6*off_metric+0.4*t["season_RG"]   # shrink toward own baseline
    runsPg15_disp=wmean([min(v,pctile(RF,0.85)) for v in RF],w)
    off_delta=off_metric-t["season_RG"]
    # RUN PREVENTION (pitching + bullpen proxy): fewer runs allowed than usual, opp-offense adjusted
    adjRA=[ra*(LG_RG/oo if oo>0 else 1) for ra,oo in zip(RA,opp_off)]
    capA=pctile(adjRA,0.85); winRA=[min(v,capA) for v in adjRA]
    prev_metric=wmean(winRA,w)
    prev_delta=t["season_RAG"]-prev_metric   # positive = allowing fewer = good
    # RECORD
    wr=wmean(wins,w); rec_delta=wr-0.5
    # MORALE
    morale = (4 if t["walkoff_win"] else 0) + (-4 if t["walkoff_loss"] else 0)
    # COMPOSITE
    off_pts=max(-18,min(18, off_delta*9))
    prev_pts=max(-12,min(12, prev_delta*6))
    rec_pts=max(-12,min(12, rec_delta*40))
    score=50+off_pts+prev_pts+rec_pts+morale
    score=max(0,min(100,round(score,1)))
    tier=("hot" if score>=64 else "warm" if score>=56 else "neutral" if score>=45 else "cool" if score>=37 else "cold")
    conf=min(1,n/12)
    deltaOps=round(max(-0.45,min(0.45,off_delta))/11,5)
    note_bits=[]
    if penalized: note_bits.append(f"offense shrunk toward baseline (one game = {round(top_share*100)} percent of recent runs)")
    if t["walkoff_win"]: note_bits.append("walk off win morale boost")
    if t["walkoff_loss"]: note_bits.append("walk off loss morale hit")
    note=f"Last {n} games. " + (("; ".join(note_bits)+". ") if note_bits else "") + \
         f"Off {round(off_metric,2)} vs base {t['season_RG']}, prevention {round(prev_metric,2)} vs base {t['season_RAG']}, wtd win {round(wr,2)}."
    out_teams[name]={
        "games15":n,
        "ops15":round(0.715+deltaOps,3),"opsBaseline":0.715,"deltaOps":deltaOps,
        "runsPg15":round(runsPg15_disp,2),"runsPgBaseline":round(t["season_RG"],2),
        "tier":tier,
        "formScore":score,
        "components":{"offense_pts":round(off_pts,1),"prevention_pts":round(prev_pts,1),
                      "record_pts":round(rec_pts,1),"morale_pts":morale,
                      "off_delta_runs":round(off_delta,2),"prevention_delta_runs":round(prev_delta,2),
                      "wtd_win_pct":round(wr,3),"top_game_share":round(top_share,2),
                      "consistency_penalized":penalized,"opponent_adjusted":True},
        "walkoff_win":t["walkoff_win"],"walkoff_loss":t["walkoff_loss"],
        "note":note
    }

overlay={"asof":NOW,"asOf":NOW,"slate_date":"2026-06-21",
  "generated_by":"recent form engine v2: recency weighted last 10 (last 4 heaviest), opponent adjusted and consistency penalized runs, run prevention proxy, weighted record, walk off morale. ops fields derived from runs.",
  "league_avg_RG":round(LG_RG,3),"league_avg_RAG":round(LG_RAG,3),
  "teams":out_teams}
json.dump(overlay,open(f"{OUT}/rolling_form_overlay.json","w"),indent=2)

# validation view
print("league R/G",round(LG_RG,3),"RA/G",round(LG_RAG,3))
from collections import Counter
print("tier dist:",Counter(v["tier"] for v in out_teams.values()))
slate_names=set()
for g in d["slate"]: slate_names.add(g["away"]); slate_names.add(g["home"])
print("\n=== SLATE TEAM FORM (sorted by score) ===")
for nm,v in sorted(((n,out_teams[n]) for n in slate_names),key=lambda x:-x[1]["formScore"]):
    c=v["components"]
    print(f"{v['formScore']:5} {v['tier']:7} {nm:24} off{c['off_delta_runs']:+.2f} prev{c['prevention_delta_runs']:+.2f} win{c['wtd_win_pct']:.2f} topShr{c['top_game_share']:.2f}{' PEN' if c['consistency_penalized'] else ''}")
print("\n=== PHILLIES detail ===")
import pprint; pprint.pprint(out_teams["Philadelphia Phillies"])
print("\n=== METS detail ===")
pprint.pprint(out_teams["New York Mets"])
