# Notes — operational strip (v0.2)

Provenance and audit notes for `paper-behavior-codebook_v0.2_operational-strip.md`. **This companion file is not part of the scoring payload** — it names the hypothesis and the excluded sections, so it must never be pasted into a scorer prompt. Keep only the strip itself in the payload.

## What the strip is

A self-contained, hypothesis-blind scoring instrument: the operational scoring sections (§3–§8) plus the Scope paragraph and the pinned-instrument stubs those sections require. It is the "instrument" half of a scorer prompt; the operator still supplies the task/output wrapper (what to emit per item), exactly as `src/fable-vs-opus/run_equivalence.py` does.

## Provenance

- §3, §4, and the §5–§8 amendments: from `paper-behavior-codebook_v0.2.md` (built at repo HEAD `9dc2fc1`).
- §5–§8 **base** item definitions (E2–E4, P1a–P7, A1–A4, S1–S5): from `paper-behavior-codebook_v0.1.md`, which v0.2 carries by reference ("as v0.1", "unchanged"). The strip resolves those references inline.
- Amendments folded in: r5 (§4.1 extraction conventions), r6 (§5 aligned-paper counter-position), r16a–e (§4.2 level rules / §4.3 T2 test-framing / §4.6 Forecast / §6 P3 "shown"). No new rule; no score changed. This is a repackaging.

## Why blind (pending r32)

The full codebook states the directional hypothesis (§1, §9 H1–H3), names the sampling frame (§2: Petersen CCC/CCS lists, NIPCC robustness frame, pilot pair), and carries the analysis plan, threats, and changelog (§10–§16) — all priming for a scorer that should judge each paper on its own evidence. Candidate amendment **r32** (registered in the design-rationale doc, not enacted) proposes defining the payload as exactly these operational sections and scoring hypothesis-blind. This strip is that payload, produced ahead of the r32 decision. It does **not** supersede the codebook.

## Excluded from the strip, with reason

| Excluded | Reason |
|---|---|
| §1 hypothesis paragraph, §9 composites-and-hypotheses, §13–§16 | state or imply the expected direction (H1–H3) |
| §2 unit / sampling / matching | names the contrarian frame and the pilot corpus |
| Appendix A worked examples | contain fully scored answers for the pilot papers — answer-key leakage |
| Appendix B Benestad coverage map | frames the instrument around an error taxonomy |
| §10–§12 protocol / legibility / validity | describe how the *study* runs the scorer, not how to score one paper |

The §1 **first** paragraph (behavior-not-correctness, auditability) is non-directional and is kept, as the strip's "Scope" section.

## One unavoidable structural disclosure

§5 E1 requires the scorer to identify a paper's "prevailing counter-position," defined relative to the contemporaneous IPCC assessment (whether the paper opposes or aligns with it). E1 cannot be scored without this, so it stays in the strip. It reveals that the corpus contains both assessment-opposing and assessment-aligned papers; it states no expected direction and never labels either group. If a future design wants this removed too, E1 would need a stance-neutral re-operationalization — a candidate for the r32 discussion.

## Finding: the existing harness payload is incomplete

`src/fable-vs-opus/run_equivalence.py` feeds a **single** codebook file as the payload (default `paper-behavior-codebook_v0.2.md`; the v2 README confirms "codebook v0.2 is the payload instrument"). But v0.2's §5–§8 are deltas that say "as v0.1" / "unchanged" without restating the E2–E4, P, A, and S definitions — which live only in v0.1 and were **not** in the payload. The pilot/equivalence scorers therefore reconstructed those item definitions from the "unchanged" labels rather than reading them. That is a latent validity gap for a model-equivalence test (two models may reconstruct an unstated definition differently). This strip removes the gap by being self-contained; the same fix should be applied to the non-blind payload if the crossed re-test is rerun (feed v0.1+v0.2 together, or a self-contained merge).

## Keeping it in sync

The strip is derived, not canonical. Regenerate it whenever `paper-behavior-codebook_v0.1.md` or `_v0.2.md` changes. The canonical instrument remains the codebook; this is a payload build of it.
