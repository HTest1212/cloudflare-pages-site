#!/usr/bin/env python3
# Recent form overlay builder. Reads form_data.json (argv[1] or cwd), writes rolling_form_overlay.json (argv[2] or cwd).
# form_data.json shape: {"teams":{"Team":{"log":[{date,RF,RA,win,home,opp}],"season_RG","season_RAG","walkoff_win","walkoff_loss"}}, "slate":[...]}
import json, datetime, statistics as st, sys
INFILE=sys.argv[1] if len(sys.argv)>1 else "form_data.json"
OUTFILE=sys.argv[2] if len(sys.argv)>2 else "rolling_form_overlay.json"
NOW=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
d=json.load(open(INFILE)); teams=d["teams"]
LG_RG=st.mean(t["season_RG"] for t in teams.values()); LG_RAG=st.mean(t["season_RAG"] for t in teams.values())
def weights(n):
    w=[]
    for i in range(n):
        fe=n-i; w.append(1.5 if fe<=4 else (1.0 if fe<=7 else 0.6))
    return w
def wmean(v,w): s=sum(w); return sum(a*b for a,b in zip(v,w))/s if s else 0
def pctile(v,p):
    if not v: return 0
    s=sorted(v); k=(len(s)-1)*p; f=int(k); c=min(f+1,len(s)-1); return s[f]+(s[c]-s[f])*(k-f)
out={}
for name,t in teams.items():
    log=t["log"][-10:]; n=len(log)
    if n<5:
        out[name]={"games15":n,"ops15":0,"opsBaseline":0.715,"deltaOps":0,"runsPg15":0,
            "runsPgBaseline":t["season_RG"],"tier":"neutral","formScore":50,"components":{},
            "note":"Insufficient recent sample.","insufficient":True}; continue
    w=weights(n); RF=[g["RF"] for g in log]; RA=[g["RA"] for g in log]; wins=[1 if g["win"] else 0 for g in log]
    opp_def=[teams.get(g["opp"],{}).get("season_RAG",LG_RAG) for g in log]
    opp_off=[teams.get(g["opp"],{}).get("season_RG",LG_RG) for g in log]
    adjRF=[rf*(LG_RAG/od if od>0 else 1) for rf,od in zip(RF,opp_def)]
    cap=pctile(adjRF,0.85); winRF=[min(v,cap) for v in adjRF]; off=wmean(winRF,w)
    tot=sum(RF) or 1; top_share=max(RF)/tot; pen=top_share>0.40 and n>=6
    if pen: off=0.6*off+0.4*t["season_RG"]
    runsPg=wmean([min(v,pctile(RF,0.85)) for v in RF],w); off_delta=off-t["season_RG"]
    adjRA=[ra*(LG_RG/oo if oo>0 else 1) for ra,oo in zip(RA,opp_off)]
    capA=pctile(adjRA,0.85); winRA=[min(v,capA) for v in adjRA]; prev=wmean(winRA,w); prev_delta=t["season_RAG"]-prev
    wr=wmean(wins,w); rec_delta=wr-0.5; morale=(4 if t["walkoff_win"] else 0)+(-4 if t["walkoff_loss"] else 0)
    op=max(-18,min(18,off_delta*9)); pp=max(-12,min(12,prev_delta*6)); rp=max(-12,min(12,rec_delta*40))
    score=max(0,min(100,round(50+op+pp+rp+morale,1)))
    tier=("hot" if score>=64 else "warm" if score>=56 else "neutral" if score>=45 else "cool" if score>=37 else "cold")
    deltaOps=round(max(-0.45,min(0.45,off_delta))/11,5)
    nb=[]
    if pen: nb.append(f"offense shrunk toward baseline (one game = {round(top_share*100)} percent of recent runs)")
    if t["walkoff_win"]: nb.append("walk off win morale boost")
    if t["walkoff_loss"]: nb.append("walk off loss morale hit")
    note=f"Last {n} games. "+(("; ".join(nb)+". ") if nb else "")+f"Off {round(off,2)} vs base {t['season_RG']}, prevention {round(prev,2)} vs base {t['season_RAG']}, wtd win {round(wr,2)}."
    out[name]={"games15":n,"ops15":round(0.715+deltaOps,3),"opsBaseline":0.715,"deltaOps":deltaOps,
        "runsPg15":round(runsPg,2),"runsPgBaseline":round(t["season_RG"],2),"tier":tier,"formScore":score,
        "components":{"offense_pts":round(op,1),"prevention_pts":round(pp,1),"record_pts":round(rp,1),"morale_pts":morale,
            "off_delta_runs":round(off_delta,2),"prevention_delta_runs":round(prev_delta,2),"wtd_win_pct":round(wr,3),
            "top_game_share":round(top_share,2),"consistency_penalized":pen,"opponent_adjusted":True},
        "walkoff_win":t["walkoff_win"],"walkoff_loss":t["walkoff_loss"],"note":note}
overlay={"asof":NOW,"asOf":NOW,"slate_date":d.get("slate_date",datetime.date.today().isoformat()),
    "generated_by":"recent form engine v2: recency weighted last 10 (last 4 heaviest), opponent adjusted and consistency penalized runs, run prevention proxy, weighted record, walk off morale.",
    "league_avg_RG":round(LG_RG,3),"league_avg_RAG":round(LG_RAG,3),"teams":out}
json.dump(overlay,open(OUTFILE,"w"),indent=2)
print(f"wrote {OUTFILE}: {len(out)} teams")
