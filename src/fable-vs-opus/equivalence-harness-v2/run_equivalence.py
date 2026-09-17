#!/usr/bin/env python3
"""v2 — Crossed model-equivalence runs under codebook v0.2.
Clean-context per run: codebook + paper text + fixed claim list (forecast-tagged).
Usage: ANTHROPIC_API_KEY=... python3 run_equivalence.py --model claude-fable-5 --rate-in 10 --rate-out 50 --outdir scores_fable
       ANTHROPIC_API_KEY=... python3 run_equivalence.py --model claude-opus-5 --outdir scores_opus
       python3 run_equivalence.py --mock --outdir scores_mock   (pipeline self-test)"""
import argparse, json, os, sys, time, urllib.request, pathlib, re

SCHEMA = """Output ONLY valid JSON, no prose, no markdown fences, exactly this shape:
{"paper":"<ID>",
 "part0_abstract_claims":["<verbatim sentence trimmed <=25 words>", ...],
 "claims":[{"id":"A1","level":"L1|L2|L3|L4|Conditional","marker":"<governing word(s)>",
            "tier":"T0|T1|T2|T3|link","basis":"<=10 words","O":0},
           {"id":"<forecast-tagged id>","level":"...","marker":"...","tier":"...","basis":"...","O":0,
            "forecast_confirmed":1,"horizon":"<e.g. 2100 / next decades>","interval_present":0}, ...],
 "items":{"E1":0,"E1b":0,"P1a":0,"P1b":0,"P2a":0,"P2b":0,"P3":0,"P4":0,"P6":0,"P7":0},
 "item_basis":{"E1":"<=15 words + anchor", ... one entry per item ...}}"""

def build_user_msg(codebook, paper_id, paper_text, claims):
    lines = []
    for c in claims:
        tag = "  [FORECAST-TAGGED per sec.4.6]" if c.get("forecast") else ""
        lines.append(f'{c["id"]} | {c["anchor"]} | "{c["quote"]}"{tag}')
    return f"""You are the scoring instrument for a pre-registered study of paper-level behavior.
Apply the codebook below EXACTLY as written, including all sec.4.1 extraction conventions and
the sec.4.2 level rules as amended. Do not import outside knowledge of these papers, their
authors, or their reception. Score only what is asked.

<codebook>
{codebook}
</codebook>

<paper id="{paper_id}">
{paper_text}
</paper>

TASKS
Part 0: From the Abstract ONLY, list the sentences you would extract as claims under sec.4.1
(verbatim, trimmed to <=25 words each). Do not include forecast tagging here.
Part 1: For each claim below (id | anchor | quote), assign Level per sec.4.2 (with governing
marker), Tier per sec.4.3 (with <=10-word basis), and O per sec.4.4. For claims marked
[FORECAST-TAGGED]: confirm the tag (forecast_confirmed 0/1), record horizon and
interval_present, and tier per sec.4.6 (T1 cap absent a formal predictive interval).
{chr(10).join(lines)}
Part 2: Score E1 (0/1/2) and E1b (0/1) per sec.5, and P1a P1b P2a P2b P3 P4 P6 P7 (each 0/1)
per sec.6, from the full paper text. Give a <=15-word basis with page anchor for each.

{SCHEMA}"""

def call_api(model, user_msg, thinking_budget, max_tokens, temperature):
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key: sys.exit("ANTHROPIC_API_KEY not set. For a pipeline test use --mock.")
    body = {"model": model, "max_tokens": max_tokens, "temperature": temperature,
            "messages": [{"role": "user", "content": user_msg}]}
    if thinking_budget: body["thinking"] = {"type": "enabled", "budget_tokens": thinking_budget}
    for attempt in range(4):
        req = urllib.request.Request("https://api.anthropic.com/v1/messages",
              data=json.dumps(body).encode(), method="POST",
              headers={"content-type": "application/json", "x-api-key": key,
                       "anthropic-version": "2023-06-01"})
        try:
            with urllib.request.urlopen(req, timeout=600) as r: return json.load(r)
        except urllib.error.HTTPError as e:
            err = e.read().decode()[:400]
            if e.code == 400 and "thinking" in err and body.get("thinking"):
                print("  thinking param rejected; retrying without", file=sys.stderr)
                body.pop("thinking"); continue
            if e.code in (429, 500, 502, 503, 529) and attempt < 3:
                w = 15*(attempt+1); print(f"  HTTP {e.code}; retry in {w}s", file=sys.stderr)
                time.sleep(w); continue
            sys.exit(f"API error {e.code}: {err}")

def extract_scores(resp):
    texts = [b.get("text","") for b in resp.get("content",[]) if b.get("type")=="text"]
    raw = re.sub(r"```(json)?", "", "\n".join(texts)).strip()
    return json.loads(raw[raw.find("{"):raw.rfind("}")+1])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="claude-opus-5")
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--papers", default="LS11,FR11")
    ap.add_argument("--codebook", default="paper-behavior-codebook_v0.2.md")
    ap.add_argument("--outdir", default="scores")
    ap.add_argument("--thinking-budget", type=int, default=8000)
    ap.add_argument("--no-thinking", action="store_true")
    ap.add_argument("--max-tokens", type=int, default=14000)
    ap.add_argument("--temperature", type=float, default=1.0)
    ap.add_argument("--rate-in", type=float, default=5.0)
    ap.add_argument("--rate-out", type=float, default=25.0)
    ap.add_argument("--mock", action="store_true")
    ap.add_argument("--dump", action="store_true")
    a = ap.parse_args()
    here = pathlib.Path(__file__).parent
    cb = here / a.codebook
    if not cb.exists(): cb = here.parent / a.codebook
    if not cb.exists(): sys.exit(f"codebook not found: {a.codebook} (harness folder or parent)")
    codebook = cb.read_text()
    out = here / a.outdir; out.mkdir(exist_ok=True); (here/"runs").mkdir(exist_ok=True)
    tin = tout = 0
    for paper in a.papers.split(","):
        paper_text = (here / f"{paper.lower()}_fulltext.txt").read_text()
        claims = json.load(open(here / f"claims_{paper.lower()}.json"))
        msg = build_user_msg(codebook, paper, paper_text, claims)
        if a.dump:
            (here/"payloads").mkdir(exist_ok=True)
            (here/"payloads"/f"{paper}.txt").write_text(msg)
            print(f"[{paper}] payload written ({len(msg)} chars)"); continue
        for i in range(1, a.runs+1):
            tag = f"{paper}_r{i}"
            if a.mock:
                ref = json.load(open(here/"adjudicated_v02_reference.json"))[paper]
                scores = {"paper": paper, "part0_abstract_claims": ["<mock>"],
                          "claims": [dict(id=k, level=v["level"], marker="mock", tier=v["tier"],
                                          basis="mock", O=v["O"],
                                          **({"forecast_confirmed":1,"horizon":"mock","interval_present":0}
                                             if any(c["id"]==k and c.get("forecast") for c in claims) else {}))
                                     for k, v in ref["C"].items()],
                          "items": ref["PE"], "item_basis": {k:"mock" for k in ref["PE"]}}
            else:
                print(f"[{tag}] calling {a.model} ...", file=sys.stderr)
                resp = call_api(a.model, msg, 0 if a.no_thinking else a.thinking_budget,
                                a.max_tokens, a.temperature)
                json.dump(resp, open(here/"runs"/f"{a.outdir}_{tag}_raw.json","w"))
                u = resp.get("usage", {}); tin += u.get("input_tokens",0); tout += u.get("output_tokens",0)
                scores = extract_scores(resp)
            json.dump(scores, open(out/f"{tag}.json","w"), indent=1)
            print(f"[{tag}] -> {a.outdir}: {len(scores['claims'])} claims, {len(scores['items'])} items")
    if not a.mock and not a.dump:
        print(f"usage: {tin} in / {tout} out ~= ${tin/1e6*a.rate_in + tout/1e6*a.rate_out:.2f}")
if __name__ == "__main__": main()
