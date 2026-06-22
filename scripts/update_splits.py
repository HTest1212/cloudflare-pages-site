import json, datetime, statistics as st
OUT="/sessions/happy-serene-gates/mnt/outputs"
NOW=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
LG_OPS=0.715
SPOT_W=[1.00,0.97,0.94,0.91,0.88,0.85,0.82,0.79,0.76]
K_REG=50  # regression constant (PA)

def load(f): return json.load(open(f"{OUT}/{f}"))
phi=load("splits_phillies.json"); nym=load("splits_mets.json")

def overall_ops(p):
    l,r=p["vsL"],p["vsR"]
    pa=l["PA"]+r["PA"]
    if pa==0: return LG_OPS,0
    # PA-weighted blend of the two hand OPS as overall
    return round((l["OPS"]*l["PA"]+r["OPS"]*r["PA"])/pa,3),pa

def team_block(data):
    hand=data["faces_hand_today"]  # L or R
    key="vsL" if hand=="L" else "vsR"
    hitters=[]; wsum=0; wops=0
    for i,p in enumerate(data["players"]):
        sp=p[key]; faced_pa=sp["PA"]; faced_ops=sp["OPS"]
        ov,ovpa=overall_ops(p)
        # sample guard: regress faced OPS toward overall by PA
        rel=round((faced_ops*faced_pa + ov*K_REG)/(faced_pa+K_REG),3) if (faced_pa+K_REG)>0 else ov
        low = faced_pa<40
        edge=round(rel-ov,3)  # platoon edge vs own overall
        flag=None
        if faced_pa>=40 and ov<0.720 and faced_ops>0.800: flag="reverse split plus: weak overall bat crushes this hand"
        elif faced_pa>=40 and ov>0.800 and faced_ops<0.680: flag="platoon downgrade: strong bat in a bad split"
        elif faced_pa>=40 and faced_ops>0.850: flag="strong in this matchup"
        elif faced_pa>=40 and faced_ops<0.600: flag="weak in this matchup"
        w=SPOT_W[i] if i<9 else 0.76
        # weight reliability down for low sample
        wq=w*(0.5 if low else 1.0)
        wsum+=wq; wops+=rel*wq
        hitters.append({"name":p["name"],"bat":p["bat"],"spot":i+1,
            "faced_OPS":faced_ops,"faced_PA":faced_pa,"reliable_OPS":rel,
            "overall_OPS":ov,"xwOBA":sp.get("xwOBA"),"platoon_edge":edge,
            "low_sample":low,"flag":flag})
    lineup_ops=round(wops/wsum,3) if wsum else LG_OPS
    # baseline = weighted overall OPS of same lineup (so edge isolates the platoon effect)
    bw=0; bo=0
    for i,p in enumerate(data["players"]):
        ov,_=overall_ops(p); w=SPOT_W[i] if i<9 else 0.76
        bw+=w; bo+=ov*w
    base_ops=round(bo/bw,3) if bw else LG_OPS
    platoon_edge=round(lineup_ops-base_ops,3)
    nudge=round(max(-4,min(4, platoon_edge*40)),1)  # ~0.010 OPS = 0.4 pts, cap +-4
    tier=("favorable" if platoon_edge>=0.015 else "unfavorable" if platoon_edge<=-0.015 else "neutral")
    standouts=[h for h in hitters if h["flag"]]
    return {"faces_hand":hand,"starter_faced":data["starter_faced"],
            "lineup_platoon_ops":lineup_ops,"lineup_baseline_ops":base_ops,
            "platoon_edge":platoon_edge,"conf_nudge":nudge,"tier":tier,
            "standouts":[{"name":h["name"],"flag":h["flag"],"faced_OPS":h["faced_OPS"],"faced_PA":h["faced_PA"]} for h in standouts],
            "hitters":hitters}

overlay={"asof":NOW,"asOf":NOW,"slate_date":"2026-06-21",
  "generated_by":"platoon splits engine v1: season statcast vs LHP and vs RHP per projected hitter, lineup spot weighted, sample guard regresses splits under 40 PA toward the hitter overall. xwOBA from estimated_woba_using_speedangle.",
  "games":{"823449":{"away":"New York Mets","home":"Philadelphia Phillies",
     "teams":{"Philadelphia Phillies":team_block(phi),"New York Mets":team_block(nym)}}}}
json.dump(overlay,open(f"{OUT}/splits_overlay.json","w"),indent=2)

for tm in ["Philadelphia Phillies","New York Mets"]:
    b=overlay["games"]["823449"]["teams"][tm]
    print(f"\n=== {tm} vs {b['starter_faced']} ({b['faces_hand']}) ===")
    print(f"lineup platoon OPS {b['lineup_platoon_ops']} vs baseline {b['lineup_baseline_ops']} | edge {b['platoon_edge']:+} | nudge {b['conf_nudge']:+} | {b['tier']}")
    for h in b["hitters"]:
        fl=f"  << {h['flag']}" if h['flag'] else ""
        ls=" [low samp]" if h['low_sample'] else ""
        print(f"  {h['spot']} {h['name'][:20]:20} {h['bat']} faced OPS {h['faced_OPS']:.3f} ({h['faced_PA']} PA){ls} ovr {h['overall_OPS']:.3f} edge {h['platoon_edge']:+.3f}{fl}")
