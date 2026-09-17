#!/usr/bin/env python3
"""Crossed equivalence comparison (codebook v0.2 sec.13.1).
Usage: python3 compare_crossed.py <incumbent_dir> <candidate_dir>   e.g. scores_fable scores_opus"""
import json, csv, sys, glob, pathlib, collections, itertools
here = pathlib.Path(__file__).parent
dA, dB = sys.argv[1], sys.argv[2]   # A = incumbent
fc_ids = {p: [c["id"] for c in json.load(open(here/f"claims_{p.lower()}.json")) if c.get("forecast")]
          for p in ("LS11","FR11")}

def load(d):
    out = collections.defaultdict(list)
    for f in sorted(glob.glob(str(here/d/"*_r*.json"))):
        s = json.load(open(f)); out[s["paper"]].append(s)
    return out
A, B = load(dA), load(dB)
def itemvec(run):
    v = {c["id"]: c["O"] for c in run["claims"]}
    v.update(run["items"]); return v
def pairwise(runs1, runs2, same=False):
    pairs = itertools.combinations(runs1, 2) if same else itertools.product(runs1, runs2)
    aggs = []
    for r1, r2 in pairs:
        v1, v2 = itemvec(r1), itemvec(r2); keys = set(v1) & set(v2)
        aggs.append(sum(v1[k]==v2[k] for k in keys)/len(keys))
    return sum(aggs)/len(aggs)
def majority(runs):
    keys = itemvec(runs[0]).keys()
    return {k: collections.Counter(itemvec(r)[k] for r in runs).most_common(1)[0][0] for k in keys}
def composites(m, paper):
    Cids = [k for k in m if k[0] in "ACF" and k not in ("E1","E1b")]
    nonfc = [k for k in Cids if k not in fc_ids[paper]]
    cal = sum(1 for k in nonfc if m[k]>=1)/len(nonfc)
    calfi = sum(1 for k in Cids if m[k]>=1)/len(Cids)
    prac = sum(v for k,v in m.items() if k.startswith("P"))/8
    return cal, calfi, prac

md, rows = ["# Crossed equivalence results (codebook v0.2 sec.13.1)",
            f"Incumbent: {dA}   Candidate: {dB}\n"], []
S = {}
for paper in sorted(set(A) & set(B)):
    wA, wB = pairwise(A[paper], A[paper], True), pairwise(B[paper], B[paper], True)
    x = pairwise(A[paper], B[paper])
    mA, mB = majority(A[paper]), majority(B[paper])
    keys = set(mA) & set(mB)
    mm = sum(mA[k]==mB[k] for k in keys)/len(keys)
    cA, cfA, pA = composites(mA, paper); cB, cfB, pB = composites(mB, paper)
    S[paper] = dict(wA=wA, wB=wB, x=x, mm=mm, cA=cA, cB=cB, cfA=cfA, cfB=cfB, pA=pA, pB=pB)
    md += [f"## {paper}",
           f"- Within-model mean pairwise agreement: {dA} {wA:.0%}, {dB} {wB:.0%}",
           f"- Cross-model mean pairwise agreement: {x:.0%}   (majority-vs-majority: {mm:.0%})",
           f"- CAL primary: {dA} {cA:.3f} vs {dB} {cB:.3f}  (|delta| = {abs(cA-cB):.3f})",
           f"- CAL-FI sensitivity: {cfA:.3f} vs {cfB:.3f}   PRAC: {pA:.3f} vs {pB:.3f}\n"]
    for k in sorted(keys):
        vals = lambda runs: [itemvec(r).get(k,"") for r in runs]
        rows.append([paper, k, *vals(A[paper]), mA[k], *vals(B[paper]), mB[k],
                     "match" if mA[k]==mB[k] else "DIFFER"])
if {"LS11","FR11"} <= S.keys():
    s1, s2 = S["LS11"], S["FR11"]
    c1 = all(S[p]["x"] >= S[p]["wA"] - 0.05 for p in S)
    dirs = (s1["cA"]>s2["cA"] and s1["cB"]>s2["cB"] and s2["pA"]>s1["pA"] and s2["pB"]>s1["pB"])
    c2 = all(abs(S[p]["cA"]-S[p]["cB"]) <= 0.10 for p in S) and dirs
    gap = abs(s1["x"]-s2["x"]); c3 = gap <= 0.10
    md += ["## Verdict (sec.13.1)",
           f"1. Ceiling-relative: cross >= within({dA})-5pts per paper -> " + ("PASS" if c1 else "FAIL")
           + f"  [LS11 {s1['x']:.0%} vs floor {s1['wA']-0.05:.0%}; FR11 {s2['x']:.0%} vs {s2['wA']-0.05:.0%}]",
           f"2. Composite equivalence (|dCAL|<=0.10, directions preserved) -> " + ("PASS" if c2 else "FAIL")
           + f"  [dCAL LS11 {abs(s1['cA']-s1['cB']):.3f}, FR11 {abs(s2['cA']-s2['cB']):.3f}; directions {'ok' if dirs else 'VIOLATED'}]",
           f"3. Symmetry: cross-agreement gap {gap*100:.0f} pts -> " + ("PASS" if c3 else "FAIL"),
           "\nOverall: " + ("PASS - re-anchor per r15" if (c1 and c2 and c3) else "FAIL - see item table")]
open(here/"results_crossed.md","w").write("\n".join(md)+"\n")
with open(here/"per_item_crossed.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["paper","item",f"{dA}_r1",f"{dA}_r2",f"{dA}_r3",f"{dA}_maj",
                f"{dB}_r1",f"{dB}_r2",f"{dB}_r3",f"{dB}_maj","status"])
    w.writerows(rows)
print("\n".join(md))
