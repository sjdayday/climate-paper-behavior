# Paper-Behavior Codebook — v0.2 (pilot draft)

**Study:** Behavioral signatures distinguishing contrarian and mainstream climate-attribution papers
**Status:** DRAFT — not frozen. v0.2 enacts amendments r5, r6, r14, r15, r16a–e (changelog §16). Pilot papers: LS11, FR11 — **excluded from the confirmatory sample** (§2.4).

---

## 1. Purpose and design philosophy

This instrument scores *papers as behavior*. It does not adjudicate whether a paper's conclusions are correct. Every item is either (a) mechanical (computable by script) or (b) a judgment call small enough to be verified by a reader of any persuasion against a quoted, page-anchored passage. The study's credibility rests on that auditability, not on any claim that the scorer (an AI model) is neutral — a claim nobody should accept, including the scorer (§14).

Hypothesis under test: contrarian climate papers, as a group, exhibit features consistent with optimization for an educated lay audience rather than expert peers — confident claims outrunning in-paper validation, thin engagement with the strongest opposing evidence, omission of standard methodological practices. The instrument measures these symmetrically in both groups. Correctness is out of scope; some documented error categories are therefore deliberately unmeasured (Appendix B).

## 2. Unit, sampling frame, matching

Unchanged from v0.1 (author as clustering unit; Petersen et al. 2019 lists as primary frame; window 2003–2013 default; topic stratum attribution/decomposition/trend analysis; venue tier recorded as covariate, never matched; NIPCC-citation robustness frame; pilot pair LS11/FR11 excluded from confirmatory sample). Proposed r10–r12 (first-author-only primary, census + seeded draws, screening checklist) remain pending sign-off and are not yet enacted.

## 3. Sources and anchoring conventions

Every non-mechanical score carries (a) a verbatim quotation ≤ 25 words or an attested absence with the search terms used, and (b) a page anchor to the archived source (LS11: preprint archive pages; FR11: published ERL pages).

## 4. Index C — Rhetorical calibration

**4.1 Claim extraction.** From the Abstract and the final section, extract every sentence asserting a finding about the world derived from the paper's own analysis. Exclusions (integrated from pilot convention r5): pure methods descriptions; restatements of others' findings; normative/policy statements (flagged under §4.5, not scored); sentences describing the raw data record without analytic derivation; statements explicitly labeled assumptions ("we assume…" — noted, not scored). Explicit if–then claims are scored on the support for the inferential link, not the unasserted antecedent (level "Conditional", tier "link"; an adequately supported link scores O = 0). The sentence is the unit; if a sentence contains multiple distinct claims, score the strongest. Forward-looking claims are additionally tagged per §4.6.

**4.2 Certainty levels.** Governed by the epistemic marker(s) scoping the claim:

- **L1 Speculative:** may, might, could, possible, we speculate.
- **L2 Qualified:** suggest, indicate, appears, likely, probably, we estimate, consistent with; discourse verbs of argument (we have argued, we argue); internally hedged negation ("no clear/strong/convincing evidence for X").
- **L3 Assertive:** unhedged declaratives — is, shows, demonstrates, we find, we have shown, we can see, should be (conclusion-drawing).
- **L4 Emphatic:** any of — (i) a booster or absolute adverb scoping the claim: clearly, obviously, undoubtedly, certainly, definitely, truly, true, indeed, in fact, always, never, prove(s)/proved/proven, establish(es)/established, strictly, exactly, precisely, entirely, completely, purely, solely, only *(provisional enumeration; superseded verbatim by the pinned Hyland booster lexicon at freeze, Appendix C.1)*; (ii) a superlative or exhaustive comparative ("higher than any", "more than all"); (iii) an **unhedged negative-universal**: no X, none, not any, cannot, not able to ("does not provide any evidence", "none of these factors can…", "not able to reproduce"); (iv) an unqualified precise numeric forecast.

Decision rules: approximators (about, around, roughly, approximately, nearly, ~) are precision markers and never change the level. When multiple epistemic markers scope the same claim, the **weakest (most hedged) marker governs** ("suggests that X may…" → L1). A hedge governing the whole sentence sets the level regardless of embedded assertive verbs. Negated certainty is scored as a claim about the absence, at the level given by the rules above (unhedged universal negation → L4; internally hedged negation → L2).

**4.3 Evidential tiers.** The strongest support the paper itself provides for that claim:

- **T0:** No direct analytical support — asserted, or supported only by citation.
- **T1:** In-sample fit only.
- **T2:** Out-of-sample support for *this* claim — held-out data, cross-validation, or extrapolation **that the paper frames and evaluates as a test** (design stated, outcome reported). Extrapolation not framed and evaluated as a test remains T1.
- **T3:** Multiple independent data sources or methods converging within the paper, or formal uncertainty quantification (stated error model) bounding the claim.

Tiering of forward-looking claims is governed by §4.6.

**4.4 Scoring.** Permitted maximum certainty by tier: T0→L1, T1→L2, T2→L3, T3→L4. Per-claim overreach O = max(0, level − permitted). **Primary statistic CAL** = proportion of non-forecast claims with O ≥ 1 (denominator excludes forecast-tagged claims per §4.6). Secondary: mean overreach; count of L4 claims at tier ≤ T1.

**4.5 Normative flag.** Sentences drawing policy or urgency implications, in either direction, are logged verbatim and not scored.

**4.6 Forecast Index F (new in v0.2).** A claim asserting a state of the world at a time after the paper's publication is a **forecast**. Forecast claims are tagged (mechanically pre-tagged where feasible; the scorer confirms the tag), and for each the scorer records: horizon; whether a formal uncertainty interval accompanies it (0/1); and its level per §4.2. Forecasts are **excluded from CAL's numerator and denominator** (primary). *Sensitivity analysis CAL-FI* re-includes them, with tier capped at **T1 unless a formal predictive interval is stated** (then the paper's stated error model may earn T3). Rationale: the tier of a forecast is otherwise underdetermined between its in-paper basis and the unverifiable claim itself; the primary design removes the ambiguity instead of legislating it, and the flag table (horizon × interval) is itself a pre-registered outcome.

## 5. Index E — Contextual engagement

**E1** (0/1/2) as in v0.1, with the aligned-paper rule integrated (r6): the prevailing counter-position is the position of the contemporaneous IPCC assessment for papers opposing it; **for papers whose central claim aligns with the assessment, it is the most prominent contemporaneous published challenge to that claim** (identified by a fixed rule at freeze). **E1b** (0/1): load-bearing engagement citations are author self-citations. **E2–E4** mechanical, unchanged. P5-style pending items (r7 tightening) remain pending.

## 6. Index P — Methodological practices

As v0.1, with two clarifications:

- **P1a/P1b (out-of-sample):** "evaluated out-of-sample" follows the §4.3 T2 standard — framed and evaluated as a test. In-sample R² never qualifies.
- **P3 (sensitivity analysis):** "results **shown**" means numeric, tabular, or graphical results reported under the alternative specification, dataset, or input. A textual assertion that an unreported alternative gave similar results does not qualify. Worked example: coefficients reported for two calibration windows in a table, or a result plotted under two alternative input reconstructions, each qualifies.
- P2a, P2b, P4, P5 (era-conditional), P6, P7 unchanged (P7's exclusion of self-derived nulls unchanged).

## 7. Index A — Post-publication conduct

Unchanged from v0.1 (window +8 years; indexed sources; A1–A4; conditional analysis). r8 (admissibility of DOI'd open-review comments) remains pending.

## 8. Index S — Stylometry

Unchanged (S1–S5; Hyland lexicons pinned at freeze; S3 scope: article body including in-article appendices, excluding separate SI; S1/S2/S5 text scope to be fixed at freeze).

## 9. Composites and hypotheses

**CAL** (per §4.4, forecasts excluded) — H1: contrarian > mainstream. **ENG** = mean of E1/2, E2, E4, (1−E3) — H2: contrarian < mainstream. **PRAC** = mean of P1a, P1b, P2a, P2b, P3, P4, P6, P7 — H3: contrarian < mainstream. **Forecast table** (counts, horizons, interval presence by group) reported as a pre-registered descriptive outcome. CAL-FI reported as sensitivity.

## 10. Scoring protocol

As v0.1: pinned model and version; identical prompt containing only this codebook and the paper text (plus, for equivalence testing, the fixed claim list); 3 independent runs per paper; item-level majority; disagreement rate logged as the instability metric; page anchors mandatory; transcripts archived; 10% human spot-audit; adversarial audit invited. The equivalence harness (v2) is the reference implementation.

## 11. Legibility audit — unchanged.

## 12. Validity checks — unchanged.

## 13. Analysis plan

As v0.1 (author-cluster permutation; max-T across the three primaries; cluster-bootstrap effect sizes; instability reported), plus:

**13.1 Scorer/model equivalence protocol (r15).** Candidate scorer models are compared to the incumbent in a crossed design: both models, 3 runs each, identical payloads, majority-of-3 per model. Pass requires all of:
1. **Ceiling-relative agreement:** mean pairwise cross-model item agreement ≥ (incumbent's mean pairwise within-model agreement − 5 points), per paper.
2. **Composite equivalence:** |ΔCAL| ≤ 0.10 per paper between model majorities, with all composite direction orderings across papers preserved.
3. **Symmetry (load-bearing):** per-paper cross-agreement gap ≤ 10 points. Only stance-correlated divergence threatens validity; a uniform severity offset cancels when a single model scores everything.
Item sets, leak lists, and these thresholds are fixed before any equivalence run.

## 14. Threats and limitations — as v0.1, plus: single-item scores carry ~10% scorer test-retest noise (measured); inference is designed to run on majority-vote composites over an author-clustered sample, where this noise attenuates rather than biases (non-differential by construction when one model scores all papers).

## 15. Versioning and freeze rules — unchanged (v1.0 freeze before confirmatory sampling; post-freeze amendments logged with sensitivity analysis).

## 16. Changelog

**v0.2 (2026-08-28).** Basis: Opus equivalence probe, item-level adjudication (see analysis memo; per-item outcomes deliberately not restated here).
- **r5 integrated** into §4.1 (raw-data descriptions and labeled assumptions excluded; conditional rule).
- **r6 integrated** into §5 (aligned-paper counter-position rule).
- **r16a enacted** (§4.6): Forecast Index F; forecasts out of primary CAL; CAL-FI sensitivity with T1 cap absent a formal predictive interval.
- **r16b enacted** (§4.3): T2 requires framed-and-evaluated test.
- **r16c enacted** (§4.2): unhedged negative-universals → L4; internally hedged negation → L2. *(Ruling on the open option: "clear/strong/convincing" are treated as genuine hedges on the negation.)*
- **r16d enacted** (§4.2): booster/absolute-adverb triggers enumerated provisionally, superseded by the pinned Hyland lexicon at freeze. *(Ruling: absolute adverbs — strictly, exactly, entirely, etc. — are L4 triggers, since they strengthen claim content to totality; approximators remain level-neutral. Weakest-marker rule added for chained markers; "argued" fixed at L2, "shown/see" at L3.)*
- **r16e enacted** (§6): P3 "shown" defined; worked example added.
- **r14/r15 enacted** (§13.1): crossed equivalence protocol with ceiling-relative, composite, and symmetry criteria.
- **Erratum cross-reference:** Pilot Exhibit 1 (LS11) carries a logged erratum (P3; negative-universal level consistency) dated with this revision.
- **Pending, awaiting sign-off:** r7 (P5 code-only), r8 (open-review admissibility), r9 (aggregation weighting hierarchy), r10 (first-author-only), r11–r12 (census/seeded sampling, screening checklist); Appendix C.1/C.2 pinning.

**v0.1-r1 … r4** — as logged in v0.1 (E1b; P1a/b split; P2a/b split; normative flag).

## Appendices A–C

As v0.1 (worked examples; Benestad coverage map; pinned-instrument stubs), with one note on A.6: under v0.2, FR11's closing forward-looking clause is handled by Index F rather than Index C. Worked examples predate v0.2 rules; where a v0.2 rule speaks, the rule governs.
