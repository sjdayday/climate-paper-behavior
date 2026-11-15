import subprocess, json, time, re, urllib.parse
UA = "codebook-cite-verify/0.1 (paper-behavior study)"
def get(url):
    r = subprocess.run(["curl","-s","--max-time","20","-H",f"User-Agent: {UA}",url],capture_output=True,text=True)
    try: return json.loads(r.stdout)
    except: return None
def norm(s): return set(re.findall(r"[a-z0-9]+", s.lower())) - {"the","a","an","of","in","and","for","to","on"}
def validate(msg, title, surname, year):
    t = (msg.get("title") or [""])[0]
    ov = len(norm(title)&norm(t))/max(1,len(norm(title)))
    auths = " ".join(a.get("family","") for a in msg.get("author",[])).lower()
    y = (msg.get("published-print") or msg.get("published-online") or msg.get("issued") or {}).get("date-parts",[[0]])[0][0]
    return (ov>=0.55 and surname.lower() in auths and abs((y or 0)-year)<=1), t, y, ov
def fmt(m):
    c=(m.get("container-title") or [m.get("publisher","")]); c=c[0] if c else ""
    yr=(m.get("published-print") or m.get("published-online") or m.get("issued") or {}).get("date-parts",[[""]])[0][0]
    return f"{c} {m.get('volume','')}({m.get('issue','')}):{m.get('page','') or m.get('article-number','')} {yr} doi:{m['DOI']}"
works = [
 ("HylandTse04","Metadiscourse in academic writing a reappraisal","Hyland",2004,"10.1093/applin/25.2.156"),
 ("Hyland05DS","Stance and engagement a model of interaction in academic discourse","Hyland",2005,"10.1177/1461445605050365"),
 ("HylandJiang16","Change of attitude A diachronic study of stance","Hyland",2016,"10.1177/0741088316650399"),
 ("BiberFinegan89","Styles of stance in English lexical and grammatical marking of evidentiality and affect","Biber",1989,"10.1515/text.1.1989.9.1.93"),
 ("SalagerMeyer94","Hedges and textual communicative function in medical English written discourse","Salager-Meyer",1994,"10.1016/0889-4906(94)90013-2"),
 ("Crompton97","Hedging in academic writing some theoretical problems","Crompton",1997,None),
 ("Vincze08","The BioScope corpus biomedical texts annotated for uncertainty negation and their scopes","Vincze",2008,"10.1186/1471-2105-9-s11-s9"),
 ("Farkas10","The CoNLL-2010 shared task learning to detect hedges and their scope in natural language text","Farkas",2010,None),
 ("PeiJurgens21","Measuring sentence-level and aspect-level uncertainty in science communications","Pei",2021,None),
 ("TanLee14","A corpus of sentence-level revisions in academic writing a step towards understanding statement strength in communication","Tan",2014,None),
 ("LoughranMcDonald11","When is a liability not a liability Textual analysis dictionaries and 10-Ks","Loughran",2011,"10.1111/j.1540-6261.2010.01625.x"),
 ("Budescu14","The interpretation of IPCC probabilistic statements around the world","Budescu",2014,"10.1038/nclimate2194"),
 ("Mastrandrea11","The IPCC AR5 guidance note on consistent treatment of uncertainties","Mastrandrea",2011,"10.1007/s10584-011-0178-6"),
 ("MartinWhite05","The Language of Evaluation Appraisal in English","Martin",2005,"10.1057/9780230511910"),
]
for key,title,surname,year,doi in works:
    res=None; how=""
    if doi:
        j=get(f"https://api.crossref.org/works/{doi}")
        if j and j.get("status")=="ok":
            ok,t,y,ov=validate(j["message"],title,surname,year)
            if ok: res=fmt(j["message"]); how="direct"
    if not res:
        q=urllib.parse.quote(f"{title} {surname}")
        j=get(f"https://api.crossref.org/works?query.bibliographic={q}&rows=5")
        if j and j.get("status")=="ok":
            for item in j["message"]["items"]:
                ok,t,y,ov=validate(item,title,surname,year)
                if ok: res=fmt(item); how=f"query(ov={ov:.2f})"; break
    print(f"{key}: {'VERIFIED-'+how+' | '+res if res else 'FAIL'}")
    time.sleep(0.35)
