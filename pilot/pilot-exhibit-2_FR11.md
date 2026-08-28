# Pilot Scoring Exhibit 2 of 2 — Foster & Rahmstorf (2011)

**Paper:** Foster G. & Rahmstorf S. (2011), "Global temperature evolution 1979–2010," *Environmental Research Letters* 6:044022 (8 pp).
**Anchored source:** published ERL article (anchors = published pages 1–8; full text archived to repo from this session's fetch).
**Instrument:** Codebook v0.1 with pilot conventions logged in Exhibit 1 §7 and below (candidate amendments r5–r8).
**Scorer/run:** Claude, single run, 2026-08-23. The §10 three-independent-run protocol applies to confirmatory scoring; pilot exhibits substitute a full judgment log.
**Status:** Pilot exhibit. This paper is excluded from the confirmatory sample (codebook §2.4).

---

## 1. Index C — Rhetorical calibration

Extraction scope: Abstract (p. 1) and "6. Conclusions" (pp. 6–7). Quotes trimmed to ≤ 25 words. Level codes L1–L4, tiers T0–T3, O = overreach.

### Abstract (p. 1)

| # | Claim (trimmed) | Level (marker) | Tier (basis) | O |
|---|---|---|---|---|
| F1 | "All five series show consistent global warming trends ranging from 0.014 to 0.018 K yr−1." | L3 (show) | T3 (five datasets; SEs, Table 1) | 0 |
| F2 | "the global warming signal becomes even more evident as noise is reduced" | L3 | T3 (variance accounting, Table 2) | 0 |
| F3 | "Lower-troposphere temperature responds more strongly to El Niño … and to volcanic forcing than surface temperature data." | L3 | T3 (coefficients across datasets, fig. 3, Table 2) | 0 |
| F4 | "adjusted data show warming at very similar rates to the unadjusted data, with smaller probable errors, and the warming rate is steady" | L3 | T3 (Table 1; fig. 6 with 2-σ ARMA-corrected errors; quadratic test) | 0 |
| F5 | "In all adjusted series, the two hottest years are 2009 and 2010." | L3 | T3 (all five adjusted series, fig. 5) | 0 |

### Conclusions (pp. 6–7)

| # | Claim (trimmed) | Anchor | Level | Tier | O |
|---|---|---|---|---|---|
| F6 | "This analysis confirms the strong influence of known factors on short-term variations in global temperature" | p6 | L3 (confirms) | T3 | 0 |
| F7 | "LT temperature is affected by these factors much more strongly than surface temperature" | p6 | L3 | T3 | 0 |
| F8 | "it enables us to remove an estimate of their influence, thereby isolating the global warming signal" | p6 | L3 | T3 | 0 |
| F9 | "adjusted data show clearly … that the rate of global warming … has been remarkably steady during the 32 years" | p6 | L4 (clearly) | T3 | 0 |
| F10 | "There is no indication of any slowdown or acceleration of global warming, beyond the variability induced by these known natural factors." | p6 | L4 ("no … any") | T3 (all-start-years trends, fig. 6; quadratic test, p5) | 0 |
| F11 | "none of these factors can be expected to exert a significant influence on the continuation of global warming over the coming decades" | p6 | L3 ("can be expected") | T3 basis, extrapolated (factor magnitudes, fig. 7) | 0 |
| F12 | "The close agreement between all five adjusted data sets suggests that it is meaningful to average them" | p6 | L2 (suggests) | T3 | 0 |
| F13 | "This is the true global warming signal." | p6 | L4 ("true") | T3 | 0 |
| F14 | "Its unabated increase is powerful evidence that we can expect further temperature increase in the next few decades" | p7 | L4 ("powerful") | T3 basis, extrapolated | 0 |

**Forecast flags (F11, F14):** decadal horizon; no uncertainty interval on either forward-looking statement.
**Normative flag (§4.5), p7:** trailing clause of F14 — "emphasizing the urgency of confronting the human influence on climate." Logged, not scored.

### Index C statistics

Claims scored: **14** (5 abstract + 9 conclusions). Overreaching: **0** → **CAL = 0.000**. Mean overreach = **0.00**. Emphatic claims (L4) at tier ≤ T1: **0**. L4 claims at T3: 4 (F9, F10, F13, F14). Forecast flags: 2, neither with an interval. Normative flags: 1.

Register note (per codebook Appendix A.6): the instrument permits F13's "true" and F14's "powerful" because top-tier support licenses top-rung language under §4.4; the ontological overstatement in "true" (an adjusted estimate is an estimate) and the paper's free use of boosters are routed to S2 for capture, not lost. Two parenthetical attributions worth recording: F9's "(most likely these are exclusively anthropogenic)" is itself a hedged (L2) attribution claim resting on elimination of the three named factors plus context — scored within F9's strongest-claim rule, no separate overreach; and F8's "isolating" asserts a complete separation that the method only approximates — inside the letter of L3 at T3, noted for register.

## 2. Index E — Contextual engagement

**E1 = 2 (engaged), under amended operationalization — see candidate amendment r6 below.** The v0.1 rule defines the counter-position as "the position of the contemporaneous IPCC assessment," which is undefined for a paper whose central claim aligns with that assessment. Discovered scoring this paper. Amended reading applied: for assessment-aligned papers, the counter-position is the most prominent contemporaneous published challenge to the paper's central claim — here, the claim that warming had stopped or that the records disagree. The paper names it — "debate has arisen over discrepancies between the different global temperature records, and over the exact magnitude of, and possible recent changes in, warming rates" (p1) — and engages it directly (five-record comparison; fig. 6's all-start-years trend analysis addresses start-year selection head-on).
**E1b = 0.** The engagement's load-bearing evidence is the paper's own new analysis plus non-self citations (Peterson & Baringer 2009); no author self-citations exist in the paper.
**E2 = 17/19 = 0.895.** Reference list (pp. 7–8) totals 19 entries. Non-journal (2): IPCC 2007 (assessment report); Wolter & Timlin 1993 (workshop proceedings). Remaining 17 journal articles. (Dataset URLs appear as footnotes, not references.)
**E3 = 0/19 = 0.000.** No reference shares an author with the paper.
**E4 = 1.** Benchmark-corpus candidates cited: IPCC 2007; Lean & Rind 2008.

## 3. Index P — Methodological practices

| Item | Score | Basis / anchor |
|---|---|---|
| P1a out-of-sample (any component) | **0** | No held-out data, cross-validation, or verified extrapolation anywhere; the all-start-years trend scan (fig. 6) and quadratic test (p5) are specification analyses on the same sample (absence attested; terms: out-of-sample, cross-valid, held out, forecast verification) |
| P1b out-of-sample (headline claim) | **0** | Follows from P1a |
| P2a uncertainty on parameters | **1** | Standard errors on all raw and adjusted trends and lags (Table 1, p3) |
| P2b uncertainty propagated to headline | **1** | The abstract's leading numbers are the adjusted trends with autocorrelation-corrected errors (Table 1; fig. 2 with 2-σ bars) |
| P3 sensitivity analysis | **1** | Input substitutions — SOI for MEI, Ammann et al. for Sato AOD, sunspot number for TSI — with outcome reported: "None of these substitutions affected the results in a significant way" (p2); plus leave-one-factor-out regression checks (p2) and collinearity screening (p2) |
| P4 data specified & public | **1** | Every dataset cited with public URL footnotes (p2) |
| P5 code available | **0** | Not in paper or SM (recorded; era-excluded, pre-2015). Narrative: the appendix supplies the complete statistical recipe with equations, and author-released code circulated off-journal; third parties reproduced the analysis. Softness of the "full analytical recipe" clause → candidate amendment r7 |
| P6 mechanism stated per driver | **1** | ENSO (internal ocean–atmosphere mode; Trenberth et al. 2002), volcanic aerosols (Sato et al. 1993; IPCC 2007), TSI (Fröhlich 2006; Lean & Rind 2008), residual trend attributed to anthropogenic forcing (Lean & Rind 2008; IPCC 2007) — all cited to non-self sources |
| P7 degrees-of-freedom discipline | **1** | Explicit ARMA(1,1) effective-df correction with derivation (appendix, pp. 7–8), adopted because AR(1) demonstrably underestimates the autocorrelation (fig. A.1); conservative multiplicity behavior also recorded: the one marginally significant quadratic term (UAH, p = 0.03) is discounted because "it shows in no other data set" (p5) |

## 4. Index A — Post-publication conduct (window 2011–2019)

**A1 = 0.** No indexed formal comment or rebuttal located (searches recorded: paper title + "comment"/"reply", ERL). Criticism within the window exists only in blogs (excluded from scoring by §7 rule).
**A2–A4: not applicable** (conditional on A1 = 1).
Narrative note, outside the A-item definitions: the authors themselves revisited and re-tested the paper's central steady-trend claim against updated data in an indexed follow-up (Rahmstorf, Foster & Cahill, *ERL* 2017) — self-initiated post-publication stress-testing, recorded because the A-index as designed only captures conduct *responding to criticism* and would otherwise miss it. Possible future item; not scored.

## 5. Index S — Stylometry (mechanical)

**S1 hedge density / S2 booster density: deferred** pending the pinned Hyland (2005) lexicon file (Appendix C.1); improvising the lists would violate the no-additions rule. Noted: S2, once computed, is expected to register this paper's booster usage (F9, F13, F14) — the routing described in §1 depends on it.
**S3 = 9/8 = 1.125.** Eight main figures plus fig. A.1; seven numbered equations (A.1)–(A.7). Scope convention as in Exhibit 1 (in-article appendix included).
**S4 = 32.0** (Flesch reading ease, scored sections).
**S5 = 7.7 per 1,000 words** (we/our/us, scored sections; scope note as in Exhibit 1).

## 6. Composites

**CAL = 0.000 · ENG = (1.000 + 0.895 + 1.000 + 1.000)/4 = 0.974 · PRAC = 6/8 = 0.750.** (P5 recorded, era-excluded.)

## 7. Judgment log and candidate amendments arising from this exhibit

1. **r6 (E1 operationalization gap).** The v0.1 counter-position rule presumes a paper opposing the IPCC assessment and is undefined for assessment-aligned papers — an asymmetry in the instrument itself, caught only because a mainstream paper was piloted. Proposed fix for freeze: "For papers whose central claim aligns with the contemporaneous assessment, the prevailing counter-position is the most prominent contemporaneous published challenge to that claim, identified by a fixed rule set at freeze."
2. **P1a = 0 is the pilot's sharpest cross-paper demonstration that the instrument follows its rules.** The mainstream paper fails both out-of-sample items that the contrarian paper partially passes (LS11 P1a = 1). FR11's design simply contains no held-out evaluation; robustness to input substitution (P3) is not out-of-sample support and was not allowed to masquerade as such.
3. **F11/F14 forecast flags:** the paper's forward-looking statements carry no uncertainty intervals — the same flag LS11's forecasts received. The flag count is symmetric across the pair (2–2), as is the normative-flag count (1–1).
4. **"True"/"isolating" register calls** (§1) documented so that a hostile auditor can check that mainstream rhetoric was seen, categorized, and routed rather than ignored.
5. **A-index blind spot** (§4 narrative note): conduct-under-criticism items cannot register self-initiated re-testing; logged as a design observation for Steve's decision, not an amendment proposal.
