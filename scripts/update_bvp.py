#!/usr/bin/env python3
# Batter vs Pitcher career overlay from statsapi (vsPlayerTotal). Standalone.
# Output: bvp_overlay.json keyed batterId_pitcherId (matches dashboard STATE.bvp).
import json, datetime, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor
BASE="https://statsapi.mlb.com/api/v1"
TODAY=(sys.argv[1] if len(sys.argv)>1 else datetime.date.today().isoformat())
YEAR=TODAY[:4]; YDAY=(datetime.date.fromisoformat(TODAY)-datetime.timedelta(days=1)).isoformat()
WSTART=(datetime.date.fromisoformat(TODAY)-datetime.timedelta(days=10)).isoformat()
NOW=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
def get(url):
    try:
        with urllib.request.urlopen(url,timeout=12) as r: return json.load(r)
    except Exception: return {}
sched=get(f"{BASE}/schedule?sportId=1&date={TODAY}&hydrate=probablePitcher")
games=[]
for d in sched.get("dates",[]):
    for g in d.get("games",[]):
        h=g["teams"]["home"]; a=g["teams"]["away"]
        games.append({"gamePk":g["gamePk"],
            "home":{"id":h["team"]["id"],"name":h["team"]["name"],"sp":h.get("probablePitcher",{}).get("id"),"spName":h.get("probablePitcher",{}).get("fullName")},
            "away":{"id":a["team"]["id"],"name":a["team"]["name"],"sp":a.get("probablePitcher",{}).get("id"),"spName":a.get("probablePitcher",{}).get("fullName")}})
def phand(pid):
    if not pid: return None
    p=get(f"{BASE}/people/{pid}")
    pe=p.get("people",[{}])
    return pe[0].get("pitchHand",{}).get("code") if pe else None
def last_lineup(tid):
    s=get(f"{BASE}/schedule?sportId=1&teamId={tid}&startDate={WSTART}&endDate={YDAY}")
    gps=[]
    for d in s.get("dates",[]):
        for g in d.get("games",[]):
            if g.get("status",{}).get("abstractGameState")=="Final": gps.append((d["date"],g["gamePk"]))
    if not gps: return []
    gp=sorted(gps)[-1][1]
    bx=get(f"{BASE}/game/{gp}/boxscore")
    for side in ("home","away"):
        tinfo=bx.get("teams",{}).get(side,{})
        if tinfo.get("team",{}).get("id")==tid:
            order=tinfo.get("battingOrder",[])[:9]
            players=tinfo.get("players",{})
            out=[]
            for pid in order:
                pl=players.get(f"ID{pid}",{})
                out.append({"id":pid,"name":pl.get("person",{}).get("fullName"),"bat":pl.get("person",{}).get("batSide",{}).get("code")})
            return out
    return []
def bvp(bid,pid):
    d=get(f"{BASE}/people/{bid}/stats?stats=vsPlayerTotal&group=hitting&opposingPlayerId={pid}")
    for s in d.get("stats",[]):
        sp=s.get("splits",[])
        if sp:
            st=sp[-1]["stat"]
            return {"atBats":st.get("atBats",0),"plateAppearances":st.get("plateAppearances",0),
                    "hits":st.get("hits",0),"homeRuns":st.get("homeRuns",0),"doubles":st.get("doubles",0),
                    "baseOnBalls":st.get("baseOnBalls",0),"strikeOuts":st.get("strikeOuts",0),
                    "avg":st.get("avg"),"ops":st.get("ops")}
    return {"atBats":0,"plateAppearances":0,"hits":0,"homeRuns":0,"doubles":0,"baseOnBalls":0,"strikeOuts":0,"avg":None,"ops":None}
# gather starter hands + lineups
for g in games:
    g["home"]["spHand"]=phand(g["home"]["sp"]); g["away"]["spHand"]=phand(g["away"]["sp"])
    g["home"]["lineup"]=last_lineup(g["home"]["id"]); g["away"]["lineup"]=last_lineup(g["away"]["id"])
matchups={}; games_out={}
tasks=[]
for g in games:
    # home hitters vs away SP; away hitters vs home SP
    for bat_side,opp_side in (("home","away"),("away","home")):
        sp=g[opp_side]["sp"]
        if not sp: continue
        for h in g[bat_side]["lineup"]:
            if h["id"]: tasks.append((g["gamePk"],g[bat_side]["name"],g[opp_side]["spName"],h,sp))
def run(t):
    gp,team,spName,h,sp=t
    line=bvp(h["id"],sp); key=f"{h['id']}_{sp}"
    return gp,team,spName,h,key,line
results={}
with ThreadPoolExecutor(max_workers=16) as ex:
    for gp,team,spName,h,key,line in ex.map(run,tasks):
        matchups[key]=line
        gobj=games_out.setdefault(str(gp),{})
        tobj=gobj.setdefault(team,{"starter_faced":spName,"hitters":[]})
        ab=line["atBats"]; ops=line["ops"]
        sample=("strong" if ab>=25 else "usable" if ab>=15 else "thin" if ab>=5 else "none")
        flag=None
        try: opsf=float(ops) if ops not in (None,"") else None
        except: opsf=None
        if ab>=15 and opsf is not None:
            if opsf>=0.900: flag="owns this pitcher"
            elif opsf<=0.550: flag="dominated by this pitcher"
        tobj["hitters"].append({"name":h["name"],"bat":h["bat"],"AB":ab,"PA":line["plateAppearances"],
            "H":line["hits"],"HR":line["homeRuns"],"ops":ops,"sample":sample,"flag":flag})
# game level summary
for gp,gobj in games_out.items():
    for team,t in gobj.items():
        strong=[h for h in t["hitters"] if h["sample"] in ("strong","usable")]
        t["meaningful_samples"]=len(strong)
        t["standouts"]=[{"name":h["name"],"ops":h["ops"],"AB":h["AB"],"flag":h["flag"]} for h in t["hitters"] if h["flag"]]
overlay={"asof":NOW,"asOf":NOW,"slate_date":TODAY,
  "generated_by":"batter vs pitcher engine v1: statsapi vsPlayerTotal career line per projected hitter against today opposing starter. Sample tiers strong>=25 AB, usable>=15, thin>=5. Keyed batterId_pitcherId.",
  "matchups":matchups,"games":games_out}
json.dump(overlay,open("bvp_overlay.json","w"),indent=2)
print(f"games {len(games_out)} matchups {len(matchups)}")
# show one game detail
if games_out:
    gp=next(iter(games_out)); 
    for team,t in games_out[gp].items():
        print(f"\n{team} vs {t['starter_faced']} (meaningful {t['meaningful_samples']})")
        for h in sorted(t["hitters"],key=lambda x:-x["AB"])[:6]:
            print(f"  {h['name'][:20]:20} {h['AB']:3} AB OPS {h['ops']} {h['sample']}"+(f"  << {h['flag']}" if h['flag'] else ""))
