#!/usr/bin/env python3
"""Compare model re-run scores against the Fable baseline. Writes results.md + per_item.csv."""
import json, csv, pathlib, collections
here = pathlib.Path(__file__).parent
base = json.load(open(here / "fable_baseline.json"))
leaks = json.load(open(here / "leak_sets.json"))
runs = collections.defaultdict(list)
for f in sorted((here / "scores").glob("*_r*.json")):
    s = json.load(open(f)); runs[s["paper"]].append(s)

def majority(vals):
    return collections.Counter(vals).most_common(1)[0][0]

rows, md = [], ["# Model-equivalence probe: results\n"]
summary = {}
for paper, rs in runs.items():
    md.append(f"\n## {paper}  ({len(rs)} runs)\n")
    cbase, pbase = base[paper]["C"], base[paper]["PE"]
    # per-item majorities and instability
    agree_O = agree_L = agree_T = unstable = 0
    leak_c = set(leaks[paper].get("C", [])) | set(leaks[paper].get("C_partial", []))
    agree_O_x = n_x = 0
    maj_O = {}
    for cid, bv in cbase.items():
        Os = [next(c for c in r["claims"] if c["id"] == cid)["O"] for r in rs]
        Ls = [next(c for c in r["claims"] if c["id"] == cid)["level"] for r in rs]
        Ts = [next(c for c in r["claims"] if c["id"] == cid)["tier"] for r in rs]
        mO, mL, mT = majority(Os), majority(Ls), majority(Ts)
        maj_O[cid] = mO
        if len(set(Os)) > 1: unstable += 1
        agree_O += (mO == bv["O"]); agree_L += (mL == bv["level"]); agree_T += (mT == bv["tier"])
        if cid not in leak_c: n_x += 1; agree_O_x += (mO == bv["O"])
        rows.append([paper, cid, bv["level"], mL, bv["tier"], mT, bv["O"], mO,
                     "unstable" if len(set(Os)) > 1 else "", "leak" if cid in leak_c else ""])
    nC = len(cbase)
    leak_p = set(leaks[paper].get("PE", []))
    agree_P = agree_P_x = nP_x = unstable_P = 0
    for k, bv in pbase.items():
        vs = [r["items"][k] for r in rs]; mv = majority(vs)
        if len(set(vs)) > 1: unstable_P += 1
        agree_P += (mv == bv)
        if k not in leak_p: nP_x += 1; agree_P_x += (mv == bv)
        rows.append([paper, k, "", "", "", "", bv, mv,
                     "unstable" if len(set(vs)) > 1 else "", "leak" if k in leak_p else ""])
    CAL = sum(1 for v in maj_O.values() if v >= 1) / nC
    Pmaj = {k: majority([r["items"][k] for r in rs]) for k in pbase}
    PRAC = sum(Pmaj.values() ) / len(Pmaj) if all(k.startswith("P") for k in Pmaj) else \
           sum(v for k, v in Pmaj.items() if k.startswith("P")) / 8
    summary[paper] = dict(nC=nC, aO=agree_O, aL=agree_L, aT=agree_T, aOx=agree_O_x, nx=n_x,
                          nP=len(pbase), aP=agree_P, aPx=agree_P_x, nPx=nP_x,
                          inst=(unstable + unstable_P) / (nC + len(pbase)), CAL=CAL, PRAC=PRAC)
    s = summary[paper]
    md += [f"- O-agreement (majority vs Fable): {s['aO']}/{nC} = {s['aO']/nC:.0%}"
           f"  |  leak-excluded: {s['aOx']}/{s['nx']} = {s['aOx']/s['nx']:.0%}",
           f"- Level agreement: {s['aL']}/{nC} = {s['aL']/nC:.0%}   Tier agreement: {s['aT']}/{nC} = {s['aT']/nC:.0%}",
           f"- E/P item agreement: {s['aP']}/{s['nP']} = {s['aP']/s['nP']:.0%}"
           f"  |  leak-excluded: {s['aPx']}/{s['nPx']} = {s['aPx']/s['nPx']:.0%}",
           f"- Within-model instability (non-unanimous items): {s['inst']:.0%}",
           f"- Composites under this model: CAL = {s['CAL']:.3f}   PRAC = {s['PRAC']:.3f}"
           f"   (Fable: CAL = {sum(1 for v in cbase.values() if v['O']>=1)/nC:.3f}, "
           f"PRAC = {sum(v for k,v in pbase.items() if k.startswith('P'))/8:.3f})"]
if {"LS11", "FR11"} <= summary.keys():
    s1, s2 = summary["LS11"], summary["FR11"]
    allO1, allO2 = s1["aO"] / s1["nC"], s2["aO"] / s2["nC"]
    tot1 = (s1["aO"] + s1["aP"]) / (s1["nC"] + s1["nP"])
    tot2 = (s2["aO"] + s2["aP"]) / (s2["nC"] + s2["nP"])
    md += ["\n## Verdict against pre-set criteria",
           f"1. Agreement floor >=90% (all judgment items): LS11 {tot1:.0%}, FR11 {tot2:.0%} -> "
           + ("PASS" if min(tot1, tot2) >= .9 else "FAIL"),
           f"2. Composite direction preserved: CAL {s1['CAL']:.3f} > {s2['CAL']:.3f}: "
           + ("yes" if s1["CAL"] > s2["CAL"] else "NO")
           + f"; PRAC {s2['PRAC']:.3f} > {s1['PRAC']:.3f}: "
           + ("yes" if s2["PRAC"] > s1["PRAC"] else "NO"),
           f"3. Symmetry: per-paper agreement gap = {abs(tot1-tot2)*100:.0f} pts "
           + ("(<=10: PASS)" if abs(tot1 - tot2) <= .10 else "(>10: FAIL)")
           + f"  [binomial caveat: n = {s1['nC']+s1['nP']} vs {s2['nC']+s2['nP']} items]"]
open(here / "results.md", "w").write("\n".join(md) + "\n")
with open(here / "per_item.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["paper","item","fable_level","model_level","fable_tier",
                                   "model_tier","fable_O_or_score","model_O_or_score","stability","leak"])
    w.writerows(rows)
print("\n".join(md))
