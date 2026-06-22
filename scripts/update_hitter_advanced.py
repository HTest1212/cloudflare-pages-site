#!/usr/bin/env python3
# Lineup advanced metrics overlay from statsapi. Standalone. Output: hitter_advanced_overlay.json
import json, datetime, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor
BASE="https://statsapi.mlb.com/api/v1"
TODAY=(sys.argv[1] if len(sys.argv)>1 else datetime.date.today().isoformat())
YEAR=TODAY[:4]; YDAY=(datetime.date.fromisoformat(TODAY)-datetime.timedelta(days=1)).isoformat()
WSTART=(datetime.date.fromisoformat(TODAY)-datetime.timedelta(days=10)).isoformat()
NOW=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
SPOT_W=[1.00,0.97,0.94,0.91,0.88,0.85,0.82,0.79,0.76]
def get(url):
    try:
        with urllib.request.urlopen(url,timeout=12) as r: return json.load(r)
    except Exception: return {}
def woba(st):
    ab=st.get("atBats",0) or 0; bb=st.get("baseOnBalls",0) or 0; ibb=st.get("intentionalWalks",0) or 0
    hbp=st.get("hitByPitch",0) or 0; h=st.get("hits",0) or 0; d=st.get("doubles",0) or 0
    t=st.get("triples",0) or 0; hr=st.get("homeRuns",0) or 0; sf=st.get("sacFlies",0) or 0
    s1=h-d-t-hr; ubb=bb-ibb
    denom=ab+bb-ibb+sf+hbp
    if denom<=0: return None
    num=0.69*ubb+0.72*hbp+0.89*s1+1.27*d+1.62*t+2.10*hr
    return round(num/denom,3)
sched=get(f"{BASE}/schedule?sportId=1&date={TODAY}&hydrate=probablePitcher")
games=[]
for d in sched.get("dates",[]):
    for g in d.get("games",[]):
        h=g["teams"]["home"]; a=g["teams"]["away"]
        games.append({"gamePk":g["gamePk"],
          "home":{"id":h["team"]["id"],"name":h["team"]["name"],"sp":h.get("probablePitcher",{}).get("id"),"spName":h.get("probablePitcher",{}).get("fullName")},
          "away":{"id":a["team"]["id"],"name":a["team"]["name"],"sp":a.get("probablePitcher",{}).get("id"),"spName":a.get("probablePitcher",{}).get("fullName")}})
def last_lineup(tid):
    s=get(f"{BASE}/schedule?sportId=1&teamId={tid}&startDate={WSTART}&endDate={YDAY}")
    gps=[]
    for d in s.get("dates",[]):
        for g in d.get("games",[]):
            if g.get("status",{}).get("abstractGameState")=="Final": gps.append((d["date"],g["gamePk"]))
    if not gps: return []
    gp=sorted(gps)[-1][1]; bx=get(f"{BASE}/game/{gp}/boxscore")
    for side in ("home","away"):
        ti=bx.get("teams",{}).get(side,{})
        if ti.get("team",{}).get("id")==tid:
            order=ti.get("battingOrder",[])[:9]; players=ti.get("players",{})
            return [{"id":pid,"name":players.get(f"ID{pid}",{}).get("person",{}).get("fullName"),
                     "bat":players.get(f"ID{pid}",{}).get("person",{}).get("batSide",{}).get("code")} for pid in order]
    return []
def hit_stats(pid):
    d=get(f"{BASE}/people/{pid}/stats?stats=season&group=hitting&season={YEAR}")
    sp=d.get("stats",[{}])[0].get("splits",[]) if d.get("stats") else []
    if not sp: return None
    st=sp[0]["stat"]; pa=st.get("plateAppearances",0) or 0
    if pa<1: return None
    avg=st.get("avg"); slg=st.get("slg"); obp=st.get("obp"); ops=st.get("ops")
    try: iso=round(float(slg)-float(avg),3) if slg and avg else None
    except: iso=None
    bbpct=round((st.get("baseOnBalls",0) or 0)/pa,3); kpct=round((st.get("strikeOuts",0) or 0)/pa,3)
    w=woba(st)
    return {"PA":pa,"AVG":avg,"OBP":obp,"SLG":slg,"OPS":ops,"ISO":iso,"BBpct":bbpct,"Kpct":kpct,"wOBA":w,"HR":st.get("homeRuns",0)}
for g in games:
    g["home"]["lineup"]=last_lineup(g["home"]["id"]); g["away"]["lineup"]=last_lineup(g["away"]["id"])
# gather hitter stats
ids=set()
for g in games:
    for side in ("home","away"):
        for h in g[side]["lineup"]:
            if h["id"]: ids.add(h["id"])
statmap={}
with ThreadPoolExecutor(max_workers=16) as ex:
    for pid,s in ex.map(lambda i:(i,hit_stats(i)),ids):
        if s: statmap[pid]=s
def tier(w):
    if w is None: return "unknown"
    return "elite" if w>=0.370 else "strong" if w>=0.340 else "average" if w>=0.310 else "weak"
games_out={}
for g in games:
    gobj=games_out.setdefault(str(g["gamePk"]),{"away":g["away"]["name"],"home":g["home"]["name"],"teams":{}})
    for side in ("home","away"):
        hitters=[]; wsum=0; ww=0
        for i,h in enumerate(g[side]["lineup"]):
            s=statmap.get(h["id"])
            if not s: continue
            wv=s["wOBA"]; spw=SPOT_W[i] if i<9 else 0.76
            if wv is not None: ww+=spw; wsum+=wv*spw
            hitters.append({"spot":i+1,"name":h["name"],"bat":h["bat"],**s,"tier":tier(wv)})
        lw=round(wsum/ww,3) if ww else None
        threats=[{"name":x["name"],"wOBA":x["wOBA"],"ISO":x["ISO"]} for x in hitters if x["tier"]=="elite"]
        weak=[{"name":x["name"],"wOBA":x["wOBA"]} for x in hitters if x["tier"]=="weak"]
        gobj["teams"][g[side]["name"]]={"lineup_wOBA":lw,
            "lineup_tier":("elite" if lw and lw>=0.345 else "strong" if lw and lw>=0.325 else "average" if lw and lw>=0.305 else "weak"),
            "threats":threats,"soft_spots":weak,"opp_starter":g["home" if side=="away" else "away"]["spName"],"hitters":hitters}
overlay={"asof":NOW,"asOf":NOW,"slate_date":TODAY,
  "generated_by":"lineup advanced metrics engine v1: statsapi season wOBA (linear weights), ISO, BB rate, K rate, OPS per projected hitter; lineup spot weighted lineup wOBA. Savant barrel and xwOBA unavailable, sourced from Statcast splits run where present.",
  "games":games_out}
json.dump(overlay,open("hitter_advanced_overlay.json","w"),indent=2)
print(f"games {len(games_out)} hitters {len(statmap)}")
gp=next(iter(games_out))
for tm,t in games_out[gp]["teams"].items():
    print(f"\n{tm} lineup wOBA {t['lineup_wOBA']} ({t['lineup_tier']}) vs {t['opp_starter']}")
    for h in t["hitters"][:5]:
        print(f"  {h['spot']} {h['name'][:18]:18} {h['bat']} wOBA {h['wOBA']} ISO {h['ISO']} K% {h['Kpct']} ({h['tier']})")
