# Model-equivalence probe harness (candidate r13 evidence)

Re-scores both pilot papers under a specified model, clean-context per run (codebook + pilot
conventions + paper text + fixed claim list — nothing else), then compares against the Fable
baseline under the three pre-set criteria. Built and pipeline-validated 2026-08-27; the mock
self-test reproduces the Fable exhibits exactly (LS11 28 claims/16 overreach, FR11 14/0).

## Run it (Claude Code or any shell)

    export ANTHROPIC_API_KEY=sk-ant-...
    python3 run_equivalence.py --model claude-opus-5        # 6 calls: 3 runs x 2 papers
    python3 compare.py                                       # writes results.md + per_item.csv

Sonnet arm: `--model claude-sonnet-5 --rate-in 2 --rate-out 10` (intro pricing through
2026-08-31; $3/$15 thereafter). Estimated cost: ~$2-3 Opus, ~$1 Sonnet, per full 6-run pass.
Useful flags: `--runs`, `--no-thinking`, `--thinking-budget`, `--temperature`, `--mock`
(pipeline self-test, no API), `--dump` (write paste-ready payloads, no API).

## Outputs

`runs/` raw API responses (archive these; §10 transcript requirement) · `scores/` extracted
per-run JSON · `results.md` criteria verdict · `per_item.csv` item-level comparison with
stability and leak flags.

## Pre-set pass criteria (fixed before any run)

1. **Agreement floor:** ≥90% of judgment items (claim O values + E/P items), majority-of-3
   vs Fable, per paper.
2. **No composite direction flip:** CAL_LS11 > CAL_FR11 and PRAC_FR11 > PRAC_LS11 must hold
   under the candidate model.
3. **Symmetry:** per-paper agreement gap ≤10 percentage points (with the binomial caveat:
   38 vs 24 items — report counts, not just percentages).

Decision rule from the allocation discussion: pass ⇒ re-anchor the pilot to the cheaper model
and use one model for the entire judgment core; asymmetric fail ⇒ that asymmetry is itself a
finding (model substitution would introduce stance-correlated misclassification) and gets a
paragraph in the write-up.

## Honest deviations from a full equivalence test

- **Fixed claim set.** Extraction is tested only by the Part-0 abstract probe (compare its
  output against exhibit IDs A1–A7 / F1–F5 by hand); full-extraction agreement is untested.
- **Worked-example leakage.** The frozen codebook's Appendix A and §16 reveal Fable's scores
  for some items; `leak_sets.json` enumerates them and `compare.py` reports agreement both
  all-items and leak-excluded. Treat the leak-excluded number as the stricter test.
- **Thinking parity.** The Fable pilot used extensive deliberation; the candidate model gets
  `--thinking-budget` (default 8000). Effort and model are partially confounded.
- **Baseline is single-run.** The Fable pilot was 1 run/paper (logged limitation), so
  "agreement with Fable" means agreement with one draw from Fable. If the candidate passes,
  re-anchoring also upgrades the pilot to the 3-run instability protocol for free.
- **Context provenance.** The baseline was produced in claude.ai (product system prompt
  present); candidate runs are API-clean. Model and context differ jointly for the baseline.

## Fallbacks without an API key

- **Incognito chat, model picked in the dropdown, outside the Project** (a Project chat would
  inject Project knowledge + memory into the run): `python3 run_equivalence.py --dump`, paste
  `payloads/LS11.txt` as the sole message, save the JSON reply as `scores/LS11_r1.json`;
  repeat x3 per paper; then `python3 compare.py`. Deviation: no seed/temperature control and
  the product system prompt is present.
- **Not usable for Opus:** the in-app artifact API path (auth handled by the platform) is
  pinned to Sonnet 4.6 — it can provide a Sonnet-tier lower-bound probe only.

## File manifest

`run_equivalence.py` runner · `compare.py` comparator · `ls11_fulltext.txt` /
`fr11_fulltext.txt` payload texts (LS11 = archive pp. 1–20 + SI, refs omitted; FR11 = body
with §5 summarized, refs omitted — mechanical E-items are out of equivalence scope) ·
`claims_*.json` fixed claim lists (quotes + anchors, no scores) · `fable_baseline.json` ·
`leak_sets.json`.
