#!/usr/bin/env python3
# Platoon splits overlay builder (slate general).
# Reads per-team input files from splits_inputs/*.json, each shaped:
#   {"gamePk":int,"away":bool,"team":"..","faces_hand_today":"L|R","starter_faced":"..",
#    "players":[{"name","playerId","bat","vsL":{...},"vsR":{...}}]}
# Writes splits_overlay.json grouped by gamePk.
import json, datetime, glob, os, sys
INDIR=sys.argv[1] if len(sys.argv)>1 else "splits_inputs"
OUTFILE=sys.argv[2] if len(sys.argv)>2 else "splits_overlay.json"
SLATE_DATE=sys.argv[3] if len(sys.argv)>3 else datetime.date.today().isoformat()
NOW=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
LG_OPS=0.715; SPOT_W=[1.00,0.97,0.94,0.91,0.88,0.85,0.82,0.79,0.76]; K_REG=50

def overall_ops(p):
    l,r=p["vsL"],p["vsR"]; pa=l["PA"]+r["PA"]
    if pa==0: return LG_OPS
    return round((l["OPS"]*l["PA"]+r["OPS"]*r["PA"])/pa,3)

def team_block(team,hand,starter,players):
    key="vsL" if hand=="L" else "vsR"
    hitters=[]; wsum=0; wops=0; bw=0; bo=0
    for i,p in enumerate(players):
        sp=p[key]; pa=sp["PA"]; ops=sp["OPS"]; ov=overall_ops(p)
        rel=round((ops*pa+ov*K_REG)/(pa+K_REG),3) if (pa+K_REG)>0 else ov
        low=pa<40; edge=round(rel-ov,3); flag=None
        if pa>=40 and ov<0.720 and ops>0.800: flag="reverse split plus: weak overall bat crushes this hand"
        elif pa>=40 and ov>0.800 and ops<0.680: flag="platoon downgrade: strong bat in a bad split"
        elif pa>=40 and ops>0.850: flag="strong in this matchup"
        elif pa>=40 and ops<0.600: flag="weak in this matchup"
        w=SPOT_W[i] if i<9 else 0.76; wq=w*(0.5 if low else 1.0)
        wsum+=wq; wops+=rel*wq; bw+=w; bo+=ov*w
        hitters.append({"name":p["name"],"bat":p.get("bat"),"spot":i+1,"faced_OPS":ops,
            "faced_PA":pa,"reliable_OPS":rel,"overall_OPS":ov,"xwOBA":sp.get("xwOBA"),
            "platoon_edge":edge,"low_sample":low,"flag":flag})
    lineup=round(wops/wsum,3) if wsum else LG_OPS
    base=round(bo/bw,3) if bw else LG_OPS
    edge=round(lineup-base,3); nudge=round(max(-4,min(4,edge*40)),1)
    tier=("favorable" if edge>=0.015 else "unfavorable" if edge<=-0.015 else "neutral")
    return {"faces_hand":hand,"starter_faced":starter,"lineup_platoon_ops":lineup,
        "lineup_baseline_ops":base,"platoon_edge":edge,"conf_nudge":nudge,"tier":tier,
        "standouts":[{"name":h["name"],"flag":h["flag"],"faced_OPS":h["faced_OPS"],"faced_PA":h["faced_PA"]} for h in hitters if h["flag"]],
        "hitters":hitters}

games={}
for f in sorted(glob.glob(os.path.join(INDIR,"*.json"))):
    d=json.load(open(f)); gp=str(d["gamePk"])
    g=games.setdefault(gp,{"away":None,"home":None,"teams":{}})
    g["teams"][d["team"]]=team_block(d["team"],d["faces_hand_today"],d.get("starter_faced",""),d["players"])
    if d.get("away"): g["away"]=d["team"]
    else: g["home"]=d["team"]
overlay={"asof":NOW,"asOf":NOW,"slate_date":SLATE_DATE,
  "generated_by":"platoon splits engine v1: season statcast vs LHP and vs RHP per projected hitter, lineup spot weighted, sample guard regresses splits under 40 PA toward the hitter overall.",
  "games":games}
json.dump(overlay,open(OUTFILE,"w"),indent=2)
print(f"wrote {OUTFILE}: {len(games)} games, teams={sum(len(g['teams']) for g in games.values())}")
