# Equivalence harness v2 — crossed re-test under codebook v0.2

Executes the recommended sequence from the Opus probe analysis: r16 rubric patches enacted
(codebook v0.2, in this folder), crossed re-test of both models, allocation decision under
r15 (codebook sec.13.1). Pipeline-validated in mock mode 2026-08-28 (all criteria PASS at
100%, composites reproduce the adjudicated v0.2 reference: LS11 CAL 0.577 / PRAC 0.625,
FR11 CAL 0.000 / PRAC 0.750).

## Run it

    export ANTHROPIC_API_KEY=sk-ant-...
    python3 run_equivalence.py --model claude-fable-5 --rate-in 10 --rate-out 50 --outdir scores_fable
    python3 run_equivalence.py --model claude-opus-5 --outdir scores_opus
    python3 compare_crossed.py scores_fable scores_opus

~$5 + ~$2.50. First positional arg to compare_crossed.py is the INCUMBENT (Fable) — the
ceiling criterion is computed against its within-model agreement. Self-test without API:
`python3 run_equivalence.py --mock --outdir m1 && python3 run_equivalence.py --mock --outdir m2
&& python3 compare_crossed.py m1 m2`.

## What changed in v2

- Codebook v0.2 is the payload instrument (sec.4.1 conventions integrated; negative-universal
  and absolute-adverb level rules; T2 test-framing; P3 "shown" defined; Forecast Index F).
- Forecast claims (LS11 A7/C21, FR11 F11/F14) are pre-tagged; scorers confirm the tag and
  record horizon + interval; CAL primary excludes them, CAL-FI includes them (T1 cap rule).
- compare_crossed.py implements the r15 criteria: (1) cross-model mean pairwise agreement
  >= incumbent within-model agreement - 5 pts, per paper; (2) |dCAL| <= 0.10 per paper with
  all composite directions preserved; (3) per-paper cross-agreement gap <= 10 pts.
- Legacy compare.py (vs the historical single-run v0.1 baseline) retained for reference only;
  fable_baseline.json is superseded for decisions by the crossed design.
- adjudicated_v02_reference.json is for mock self-tests only and is never placed in payloads.

## Outputs

results_crossed.md (verdict) - per_item_crossed.csv (all runs, both models, per item) -
runs/ raw API responses (archive per sec.10).

## Integrity

`shasum -a 256 -c MANIFEST.sha256` after unzip. Word counts are NOT a valid cross-platform
check (locale-dependent); byte counts and hashes are.

## Deviations register (carried forward)

Fixed claim set (extraction tested via Part-0 only — 100% concordant in the Opus probe);
worked-example leakage per leak_sets.json (v0.2 changelog is rule-only by design and adds no
per-item leakage); thinking-budget parity via --thinking-budget; product-vs-API context for
any claude.ai-derived comparison.
