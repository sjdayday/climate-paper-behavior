#!/usr/bin/env python3
"""Model-equivalence probe: re-score both pilot papers under a specified model.
Clean-context per run: codebook + pilot conventions + paper text + fixed claim list.
Usage: ANTHROPIC_API_KEY=... python3 run_equivalence.py --model claude-opus-5
       python3 run_equivalence.py --mock   (pipeline self-test, no API)"""
import argparse, json, os, sys, time, urllib.request, pathlib, re

CONVENTIONS = """PILOT CONVENTIONS (binding, from Exhibit 1 sec.7 / candidate r5):
(a) Sentences describing the raw data record without analytic derivation are NOT claims.
(b) Statements explicitly labeled assumptions ("we assume...") are NOT claims.
(c) Explicit if-then claims are scored on support for the inferential link, not the antecedent;
    an adequately supported link scores O=0 and is recorded as level 'Conditional', tier 'link'.
(d) Approximators (about, around, roughly) do not change Level. A hedge governing the whole
    sentence sets the Level regardless of embedded assertive verbs."""

SCHEMA = """Output ONLY valid JSON, no prose, no markdown fences, exactly this shape:
{"paper":"<ID>",
 "part0_abstract_claims":["<verbatim sentence trimmed <=25 words>", ...],
 "claims":[{"id":"A1","level":"L1|L2|L3|L4|Conditional","marker":"<governing word(s)>",
            "tier":"T0|T1|T2|T3|link","basis":"<=10 words","O":0},...],
 "items":{"E1":0,"E1b":0,"P1a":0,"P1b":0,"P2a":0,"P2b":0,"P3":0,"P4":0,"P6":0,"P7":0},
 "item_basis":{"E1":"<=15 words + anchor", ... one entry per item ...}}"""

def build_user_msg(codebook, paper_id, paper_text, claims):
    claim_lines = "\n".join(f'{c["id"]} | {c["anchor"]} | "{c["quote"]}"' for c in claims)
    return f"""You are the scoring instrument for a pre-registered study of paper-level behavior.
Apply the codebook below EXACTLY as written. Do not import outside knowledge of these papers,
their authors, or their reception. Score only what is asked.

<codebook>
{codebook}
</codebook>

{CONVENTIONS}

<paper id="{paper_id}">
{paper_text}
</paper>

TASKS
Part 0 (extraction probe): From the Abstract ONLY, list the sentences you would extract as
claims under codebook sec.4.1 and the conventions above (verbatim, trimmed to <=25 words each).
Part 1 (fixed-claim scoring): For each claim below (id | anchor | quote), assign Level per
sec.4.2 (with the governing marker), Tier per sec.4.3 (with a <=10-word basis), and O per sec.4.4.
Score the sentence as it appears in the paper at the given anchor.
{claim_lines}
Part 2 (paper-level items): Score E1 (0/1/2) and E1b (0/1) per sec.5, and P1a P1b P2a P2b P3 P4
P6 P7 (each 0/1) per sec.6, from the full paper text. Give a <=15-word basis with page anchor
for each. For E1 on a paper aligned with the contemporaneous assessment, use amended rule r6
(Exhibit 2 sec.7.1): the counter-position is the most prominent contemporaneous published
challenge to the paper's central claim.

{SCHEMA}"""

def call_api(model, user_msg, use_thinking, effort, max_tokens, temperature):
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key: sys.exit("ANTHROPIC_API_KEY not set. For a pipeline test use --mock.")
    body = {"model": model, "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": user_msg}]}
    if temperature is not None: body["temperature"] = temperature
    if use_thinking:
        body["thinking"] = {"type": "adaptive"}
        body["output_config"] = {"effort": effort}
    for attempt in range(4):
        req = urllib.request.Request("https://api.anthropic.com/v1/messages",
              data=json.dumps(body).encode(), method="POST",
              headers={"content-type": "application/json", "x-api-key": key,
                       "anthropic-version": "2023-06-01"})
        try:
            with urllib.request.urlopen(req, timeout=600) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            err = e.read().decode()[:400]
            if e.code == 400 and "temperature" in err and body.get("temperature") is not None:
                print("  temperature param rejected; retrying without", file=sys.stderr)
                body.pop("temperature"); continue
            if e.code == 400 and "thinking" in err and body.get("thinking"):
                print("  thinking param rejected; retrying without", file=sys.stderr)
                body.pop("thinking"); body.pop("output_config", None); continue
            if e.code in (429, 500, 502, 503, 529) and attempt < 3:
                wait = 15 * (attempt + 1); print(f"  HTTP {e.code}; retry in {wait}s", file=sys.stderr)
                time.sleep(wait); continue
            sys.exit(f"API error {e.code}: {err}")

def extract_scores(resp):
    texts = [b.get("text", "") for b in resp.get("content", []) if b.get("type") == "text"]
    raw = re.sub(r"```(json)?", "", "\n".join(texts)).strip()
    start, end = raw.find("{"), raw.rfind("}")
    return json.loads(raw[start:end + 1])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="claude-opus-5")
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--papers", default="LS11,FR11")
    ap.add_argument("--thinking-budget", type=int, default=None,
                     help="deprecated no-op; adaptive thinking + --effort is used instead")
    ap.add_argument("--effort", default="high", choices=["low", "medium", "high", "xhigh", "max"])
    ap.add_argument("--no-thinking", action="store_true")
    ap.add_argument("--max-tokens", type=int, default=14000)
    ap.add_argument("--temperature", type=float, default=None,
                     help="omit entirely unless set (Opus 5 / Sonnet 5 / Fable 5 reject explicit sampling params)")
    ap.add_argument("--rate-in", type=float, default=5.0, help="$/MTok input, for the cost line")
    ap.add_argument("--rate-out", type=float, default=25.0)
    ap.add_argument("--mock", action="store_true")
    ap.add_argument("--dump", action="store_true", help="write payloads/<paper>.txt and exit (manual paste)")
    a = ap.parse_args()
    here = pathlib.Path(__file__).parent
    codebook = (here / "../paper-behavior-codebook_v0.1.md").read_text()
    (here / "runs").mkdir(exist_ok=True); (here / "scores").mkdir(exist_ok=True)
    tin = tout = 0
    for paper in a.papers.split(","):
        paper_text = (here / f"{paper.lower()}_fulltext.txt").read_text()
        claims = json.load(open(here / f"claims_{paper.lower()}.json"))
        msg = build_user_msg(codebook, paper, paper_text, claims)
        if a.dump:
            (here / "payloads").mkdir(exist_ok=True)
            (here / "payloads" / f"{paper}.txt").write_text(msg)
            print(f"[{paper}] payload written to payloads/{paper}.txt ({len(msg)} chars)"); continue
        for i in range(1, a.runs + 1):
            tag = f"{paper}_r{i}"
            if a.mock:
                base = json.load(open(here / "fable_baseline.json"))[paper]
                scores = {"paper": paper, "part0_abstract_claims": ["<mock>"],
                          "claims": [{"id": k, "level": v["level"], "marker": "mock",
                                      "tier": v["tier"], "basis": "mock", "O": v["O"]}
                                     for k, v in base["C"].items()],
                          "items": base["PE"], "item_basis": {k: "mock" for k in base["PE"]}}
            else:
                print(f"[{tag}] calling {a.model} ...", file=sys.stderr)
                resp = call_api(a.model, msg, not a.no_thinking, a.effort,
                                a.max_tokens, a.temperature)
                json.dump(resp, open(here / "runs" / f"{tag}_raw.json", "w"))
                u = resp.get("usage", {}); tin += u.get("input_tokens", 0); tout += u.get("output_tokens", 0)
                scores = extract_scores(resp)
            json.dump(scores, open(here / "scores" / f"{tag}.json", "w"), indent=1)
            print(f"[{tag}] scored: {len(scores['claims'])} claims, {len(scores['items'])} items")
    if not a.mock:
        print(f"usage: {tin} in / {tout} out  ~= ${tin/1e6*a.rate_in + tout/1e6*a.rate_out:.2f} "
              f"at ${a.rate_in}/${a.rate_out} per MTok")
if __name__ == "__main__": main()
