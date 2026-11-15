import subprocess, json, time, re, urllib.parse
UA = "codebook-cite-verify/0.1 (paper-behavior study)"
def get(url):
    r = subprocess.run(["curl","-s","--max-time","20","-H",f"User-Agent: {UA}",url],capture_output=True,text=True)
    try: return json.loads(r.stdout)
    except: return None
def norm(s): return set(re.findall(r"[a-z0-9]+", s.lower())) - {"the","a","an","of","in","and","for","to"}
def validate(msg, title, surname, year):
    t = msg.get("title",[""])[0]
    ov = len(norm(title)&norm(t))/max(1,len(norm(title)))
    auths = " ".join(a.get("family","") for a in msg.get("author",[])).lower()
    y = (msg.get("published-print") or msg.get("published-online") or msg.get("published") or msg.get("issued") or {}).get("date-parts",[[0]])[0][0]
    ok = ov>=0.6 and surname.lower() in auths and abs((y or 0)-year)<=1
    return ok, t, y, ov
def fmt(msg):
    c = (msg.get("container-title") or [msg.get("publisher","")])
    c = c[0] if c else msg.get("publisher","")
    return dict(doi=msg["DOI"], cont=c, vol=msg.get("volume",""), iss=msg.get("issue",""), pg=msg.get("page",""), yr=(msg.get("published-print") or msg.get("published-online") or msg.get("issued") or {}).get("date-parts",[[""]])[0][0], typ=msg.get("type",""))
entries = [
 (3,"Hedging in Scientific Research Articles","Hyland",1998,"10.1075/pbns.54"),
 (4,"Metadiscourse Exploring Interaction in Writing","Hyland",2005,None),
 (5,"Reporting and interpretation of randomized controlled trials with statistically nonsignificant results for primary outcomes","Boutron",2010,"10.1001/jama.2010.651"),
 (8,"Use of positive and negative words in scientific PubMed abstracts between 1974 and 2014","Vinkers",2015,"10.1136/bmj.h6467"),
 (9,"Climate change prediction erring on the side of least drama","Brysse",2013,"10.1016/j.gloenvcha.2012.10.008"),
 (10,"Some results on the function and quality of citations","Moravcsik",1975,None),
 (11,"Automatic classification of citation function","Teufel",2006,None),
 (12,"How citation distortions create unfounded authority analysis of a citation network","Greenberg",2009,"10.1136/bmj.b2680"),
 (17,"Assessment of transparency indicators across the biomedical literature How open is open","Serghiou",2021,"10.1371/journal.pbio.3001107"),
 (18,"The prevalence of statistical reporting errors in psychology","Nuijten",2016,"10.3758/s13428-015-0664-2"),
 (19,"The nonsense math effect","Eriksson",2012,None),
 (21,"The readability of scientific texts is decreasing over time","Plaven-Sigray",2017,"10.7554/eLife.27725"),
]
for n,title,surname,year,doi in entries:
    res=None; how=""
    if doi:
        j=get(f"https://api.crossref.org/works/{doi}")
        if j and j.get("status")=="ok":
            ok,t,y,ov = validate(j["message"],title,surname,year)
            if ok: res=fmt(j["message"]); how="direct"
    if not res:
        q=urllib.parse.quote(f"{title} {surname}")
        j=get(f"https://api.crossref.org/works?query.bibliographic={q}&rows=5")
        if j and j.get("status")=="ok":
            for item in j["message"]["items"]:
                ok,t,y,ov = validate(item,title,surname,year)
                if ok: res=fmt(item); how=f"query(ov={ov:.2f})"; break
    if res:
        print(f"[{n}] VERIFIED-{how}: doi:{res['doi']} | {res['cont']} {res['vol']}({res['iss']}):{res['pg']} {res['yr']} [{res['typ']}]")
    else:
        print(f"[{n}] FAIL — no validated match ({surname} {year})")
    time.sleep(0.4)
