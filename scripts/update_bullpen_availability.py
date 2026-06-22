#!/usr/bin/env python3
# Bullpen + closer availability overlay from statsapi (no auth). Standalone.
# Output: bullpen_availability_overlay.json
import json, datetime, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor
BASE="https://statsapi.mlb.com/api/v1"
TODAY=(sys.argv[1] if len(sys.argv)>1 else datetime.date.today().isoformat())
YEAR=TODAY[:4]; YDAY=(datetime.date.fromisoformat(TODAY)-datetime.timedelta(days=1)).isoformat()
D2=(datetime.date.fromisoformat(TODAY)-datetime.timedelta(days=2)).isoformat()
D3=(datetime.date.fromisoformat(TODAY)-datetime.timedelta(days=3)).isoformat()
NOW=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
def get(url):
    try:
        with urllib.request.urlopen(url,timeout=12) as r: return json.load(r)
    except Exception: return {}
def ipf(ip):
    if ip in (None,""): return 0.0
    s=str(ip); w,_,f=s.partition("."); return int(w)+(int(f)/3 if f else 0)
sched=get(f"{BASE}/schedule?sportId=1&date={TODAY}&hydrate=probablePitcher,team")
teams={}
for d in sched.get("dates",[]):
    for g in d.get("games",[]):
        for side in ("home","away"):
            t=g["teams"][side]["team"]; teams[t["id"]]=t["name"]
def reliever_stats(pid):
    s=get(f"{BASE}/people/{pid}/stats?stats=season&group=pitching&season={YEAR}")
    sp=s.get("stats",[{}])[0].get("splits",[]) if s.get("stats") else []
    st=sp[0]["stat"] if sp else {}
    gl=get(f"{BASE}/people/{pid}/stats?stats=gameLog&group=pitching&season={YEAR}")
    glsp=gl.get("stats",[{}])[0].get("splits",[]) if gl.get("stats") else []
    appts=[{"date":x.get("date"),"pitches":x.get("stat",{}).get("numberOfPitches",0)} for x in glsp]
    return st,appts
def classify(appts):
    rec={a["date"]:a["pitches"] for a in appts if a.get("date")}
    y=rec.get(YDAY,0); d2=rec.get(D2,0); d3=rec.get(D3,0)
    days=[d for d in (YDAY,D2,D3) if rec.get(d,0)>0 or d in rec]
    appeared=[d for d in (YDAY,D2,D3) if d in rec]
    status="available"; reason=""
    if y>=30: status,reason="out",f"{y} pitches yesterday"
    elif rec.get(YDAY) is not None and rec.get(D2) is not None and YDAY in rec and D2 in rec: status,reason="limited","back to back"
    if len(appeared)>=3: status,reason="out","3 appearances in 3 days"
    if (y+d2)>=40 and y>0 and d2>0: status,reason="out",f"{y+d2} pitches in 2 days"
    if status=="available" and 20<=y<=29: status,reason="limited",f"{y} pitches yesterday"
    return status,reason,rec.get(YDAY),rec.get(D2)
def build_team(tid,tname):
    roster=get(f"{BASE}/teams/{tid}/roster?rosterType=active").get("roster",[])
    pitchers=[p for p in roster if p.get("position",{}).get("abbreviation")=="P"]
    rel=[]
    def work(p):
        pid=p["person"]["id"]; st,appts=reliever_stats(pid)
        gp=st.get("gamesPlayed",0) or 0; gs=st.get("gamesStarted",0) or 0
        ip=ipf(st.get("inningsPitched",0)); sv=st.get("saves",0) or 0
        # relievers: mostly relief appearances
        if gs and gp and gs/gp>0.5: return None
        era=st.get("era"); whip=st.get("whip"); h=st.get("hits",0) or 0; k=st.get("strikeOuts",0) or 0
        try: eraf=float(era) if era not in (None,"-.--","") else None
        except: eraf=None
        status,reason,yp,d2p=classify(appts)
        low=ip<12
        # reliability: regress ERA toward 4.00 by IP; trust grows with IP
        if eraf is not None and ip>0:
            reg=(eraf*ip + 4.00*15)/(ip+15)
        else: reg=4.00
        reliability=round(max(0,min(100, 100-(reg-2.0)*16)),1)  # ~2.0 ERA->97, 4.0->65, 6.0->33
        return {"name":p["person"]["fullName"],"playerId":pid,"era":eraf,"whip":(float(whip) if whip not in (None,"") else None),
                "ip":round(ip,1),"saves":sv,"k":k,"hits":h,"games":gp,"status":status,
                "available":status=="available","reason":reason,"reliability":reliability,
                "low_sample":low,"pitches_yest":yp,"pitches_d2":d2p}
    with ThreadPoolExecutor(max_workers=10) as ex:
        for r in ex.map(work,pitchers):
            if r: rel.append(r)
    if not rel: return {"unavailable":[],"relievers":[],"closer":None,"saves_leader":None,"bullpen_health":"unknown","elite_down":[]}
    rel.sort(key=lambda r:(-r["saves"],-(r["reliability"])))
    closer=rel[0]
    # roles: closer=most saves; setup=next best available reliability
    for i,r in enumerate(rel):
        r["role"]="closer" if r is closer else ("setup" if i==1 else ("high_leverage" if i==2 else "middle"))
    saves_leader={"name":closer["name"],"saves":closer["saves"]}
    unavailable=[{"name":r["name"],"role":r["role"],"status":r["status"],"reason":r["reason"]} for r in rel if r["status"]!="available"]
    elite_down=[{"name":r["name"],"era":r["era"],"status":r["status"]} for r in rel if (r["era"] is not None and r["era"]<3.00 and r["ip"]>=10 and r["status"]!="available")]
    n_out=sum(1 for r in rel if r["status"]=="out")
    health="depleted" if n_out>=3 else ("mixed" if n_out>=1 else "rested")
    return {"closer":{"name":closer["name"],"saves":closer["saves"],"era":closer["era"],"ip":closer["ip"],"status":closer["status"],"available":closer["available"]},
            "saves_leader":saves_leader,"bullpen_health":health,"elite_down":elite_down,
            "relievers":sorted(rel,key=lambda r:(-r["reliability"])),
            "unavailable":unavailable}
out={}
with ThreadPoolExecutor(max_workers=8) as ex:
    res=list(ex.map(lambda kv:(kv[1],build_team(kv[0],kv[1])),teams.items()))
for tname,blk in res: out[tname]=blk
overlay={"date":TODAY,"updated_at_iso":NOW,"source":"mlb_statsapi",
  "generated_by":"bullpen engine v1: season ERA/WHIP/saves with IP weighted reliability, recent usage availability (pitches yesterday, back to back, 3 in 3, 40 in 2), closer and saves leader, low ERA but unavailable cross flag.",
  "teams":out}
json.dump(overlay,open("bullpen_availability_overlay.json","w"),indent=2)
print(f"teams {len(out)}")
for t,b in list(out.items())[:6]:
    c=b.get("closer"); ed=b.get("elite_down",[])
    print(f"{t:24} closer {c['name'] if c else '-'} ({c['saves'] if c else 0} SV, {c['status'] if c else '-'}) health {b['bullpen_health']} eliteDown {len(ed)} unavail {len(b['unavailable'])}")
