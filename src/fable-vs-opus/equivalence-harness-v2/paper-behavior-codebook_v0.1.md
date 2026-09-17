# Paper-Behavior Codebook — v0.1 (pilot draft)

**Study:** Behavioral signatures distinguishing contrarian and mainstream climate-attribution papers
**Status:** DRAFT — not frozen. Open for revision until v1.0 freeze. Pilot revisions are logged in §16.
**Pilot papers:** Loehle & Scafetta (2011) [LS11]; Foster & Rahmstorf (2011) [FR11]. Both are **excluded from the confirmatory sample** because this codebook was tuned on them (§2.4).

---

## 1. Purpose and design philosophy

This instrument scores *papers as behavior*. It does not adjudicate whether any paper's conclusions are correct. Every item is either (a) mechanical (computable by script from the text) or (b) a judgment call small enough to be verified by a reader of any persuasion against a quoted, page-anchored passage. The study's credibility rests on that auditability, not on any claim that the scorer (Claude) is neutral — a claim nobody should accept, including the scorer (§14).

The hypothesis under test: contrarian climate papers, as a group, exhibit features consistent with optimization for an educated lay audience rather than for expert peers — confident claims outrunning in-paper validation, thin engagement with the strongest opposing evidence, and omission of standard methodological practices. The instrument measures those features symmetrically in both groups.

A deliberate trade-off: because correctness is out of scope, some error categories in Benestad et al. (e.g., misconceived mathematics) are intentionally *not* covered. The instrument detects behavior *correlated with* error-proneness, not errors. Appendix B maps coverage and gaps.

## 2. Unit, sampling frame, matching

**2.1 Unit of analysis:** the individual peer-reviewed paper. Author is the clustering unit (§13).

**2.2 Primary sampling frame:** the contrarian (CCC) and climate-scientist (CCS) author lists constructed by Petersen, Vincent & Westerling (2019), *Nature Communications* 10:3502 (in project as s41467-019-09959-4). These lists predate this study and were built by third parties, removing our discretion over group assignment. From each list, sample peer-reviewed, climate-relevant papers on which the listed individual is first or corresponding author, published in the window **2003–2013** (default; fixed at freeze), restricted to the topic stratum *attribution / decomposition / trend analysis of instrumental or proxy temperature records*.

**2.3 Matching variables:** topic stratum, publication window, paper length class (letter vs. full article), author-team size class. **Venue tier is deliberately NOT a matching variable.** Where a paper is published is plausibly endogenous to the behavior under study (papers optimized for lay persuasion may not clear review at selective venues); matching on venue would control away part of the signal. Venue tier is recorded as a covariate and reported descriptively.

**2.4 Pilot pair (rationale and disclosed mismatches):**

- **LS11** — Loehle & Scafetta (2011), "Climate Change Attribution Using Empirical Decomposition of Climatic Data," *Open Atmospheric Science Journal* 5:74–86. Source: archived arXiv preprint 1206.5845v1 (per-page archive in repo).
- **FR11** — Foster & Rahmstorf (2011), "Global temperature evolution 1979–2010," *Environmental Research Letters* 6:044022 (8 pp).

Match quality: same publication year; same object of study (the instrumental global temperature record); same method family (statistical decomposition of the record into exogenous components plus a linear trend, as opposed to GCM-based detection–attribution); both two-author short empirical papers; both explicitly engaged with the public debate over recent warming rates; mirror-image conclusions. Runners-up considered: Lean & Rind (2008) — method-identical but off-window; Huber & Knutti (2011) — right question and year, but energy-balance-based, a different method family. Disclosed mismatches: venue tier (OASJ vs. ERL — recorded, not matched, per §2.3); analysis period (1850–2010 vs. 1979–2010); LS11 makes a century-scale forecast, FR11 does not.

Pilot papers are excluded from confirmatory analysis. A disclosed sensitivity analysis may add them back.

**2.5 Robustness frame (secondary):** papers cited approvingly in NIPCC *Climate Change Reconsidered* reports, with topic-matched mainstream comparators. Addresses the concern that the Petersen contrarian list conditions on media visibility.

## 3. Sources and anchoring conventions

Every non-mechanical score must carry (a) a verbatim quotation of ≤ 25 words or an attested absence after full-text search for pre-specified terms, and (b) a page anchor. Anchors reference the archived source in the repo. For LS11, anchors are archive page numbers of the preprint (published OASJ pagination 74–86 differs; the preprint is the anchored source). For FR11, anchors are the published ERL page numbers (1–8). Absence attestations must state the search terms used.

## 4. Index C — Rhetorical calibration

**4.1 Claim extraction rule.** From the **Abstract and the final section** (however titled — Conclusions, Summary, Discussion and conclusion), extract every sentence that asserts a finding about the world derived from the paper's own analysis. Exclude: pure methods descriptions, restatements of others' findings, and normative/policy statements (the latter are flagged, not scored — §4.5). The sentence is the unit; if a sentence contains multiple distinct claims, score the strongest.

**4.2 Certainty levels.** Governed by the strongest epistemic marker scoping over the claim:

- **L1 Speculative:** may, might, could, possible, we speculate.
- **L2 Qualified:** suggest, indicate, appears, likely, probably, we estimate, consistent with.
- **L3 Assertive:** unhedged declaratives — is, shows, we find, we have shown, should be (conclusion-drawing).
- **L4 Emphatic:** certainty boosters or exhaustive/comparative superlatives — clearly, obvious(ly), no doubt, true, only, cannot be, any/none-quantified comparisons ("higher than any"), and unqualified precise numeric forecasts.

Decision rules: approximators (about, around, roughly, ~) are precision markers, not epistemic hedges — they do **not** lower the level. A hedge governing the whole sentence ("Our results suggest that X should be...") sets the level (here L2), regardless of embedded assertive verbs. Negated certainty ("no clear evidence for X") is scored as a claim about X's absence at the level of the governing marker.

**4.3 Evidential tiers.** The strongest support *the paper itself* provides for that claim:

- **T0:** No direct analytical support — asserted, or supported only by citation.
- **T1:** In-sample fit only (goodness of fit on data used for fitting).
- **T2:** Out-of-sample support — held-out data, verified extrapolation, or cross-validation, for *this* claim.
- **T3:** Multiple independent data sources or methods converging within the paper, **or** formal uncertainty quantification (with stated error model) bounding the claim.

**4.4 Scoring.** Permitted maximum certainty by tier: T0→L1, T1→L2, T2→L3, T3→L4. Per-claim overreach = max(0, level − permitted). Paper-level primary statistic **CAL** = proportion of claims with overreach ≥ 1. Secondary: mean overreach; count of L4 claims at ≤ T1. Forecast claims are additionally flagged with horizon and presence/absence of an uncertainty interval.

**4.5 Normative flag (recorded, not scored).** Sentences drawing policy or urgency implications (in either direction) are logged verbatim. [Added in pilot — see §16.]

## 5. Index E — Contextual engagement

- **E1 (judgment, auditable):** Does the paper identify the prevailing counter-position to its central claim and engage it? 0 = not acknowledged; 1 = acknowledged without engagement (bare citation or dismissal); 2 = engaged (specific counter-evidence discussed with stated reasons for departure). "Prevailing counter-position" is operationalized as the position of the contemporaneous IPCC assessment chapter relevant to the claim.
- **E1b (qualifier):** If E1 = 2, does the engagement's evidential basis rest on author self-citations? 1 = yes (all load-bearing citations in the engagement passage share an author with the paper); 0 = no. [Added in pilot — see §16.]
- **E2 (mechanical):** Fraction of reference-list entries that are peer-reviewed journal articles (categories: journal / assessment report / book or chapter / other).
- **E3 (mechanical):** Self-citation fraction — entries sharing ≥ 1 author with the paper.
- **E4 (mechanical):** Presence in the reference list of ≥ 1 entry from the pre-listed benchmark attribution corpus (Appendix C.2; finalized before freeze by a mechanical top-N-citations rule).

## 6. Index P — Methodological practices

Binary unless noted. "Reported" means in the paper or its supplementary material.

- **P1a:** Any model component evaluated out-of-sample (held-out data, verified extrapolation, or cross-validation). In-sample R² does not qualify.
- **P1b:** The paper's *headline claim* is supported by an out-of-sample evaluation. [P1 split in pilot — see §16.]
- **P2a:** Uncertainty reported on fitted parameters (standard errors, CIs).
- **P2b:** Uncertainty propagated to the headline quantitative conclusion (interval stated on the number the abstract leads with). [P2 split in pilot — see §16.]
- **P3:** Sensitivity analysis — results shown under ≥ 1 alternative specification, dataset, or input choice.
- **P4:** Data sources fully specified and publicly available.
- **P5:** Code or full analytical recipe available. *Recorded for all papers; excluded from the composite for papers published before 2015 (era norm).*
- **P6:** A specific physical mechanism is identified for each fitted or proposed driver (stated mechanism with citation; the citation's independence is captured by E3, not here).
- **P7:** Degrees-of-freedom discipline — the paper reports accounting for autocorrelation, effective sample size, or model-selection multiplicity when computing significance or errors, using a null model not derived from the fitted model itself (a noise test that presupposes the fitted structure does not qualify).

## 7. Index A — Post-publication conduct

Window: publication + 8 years. Admissible sources: indexed comments/replies, journal correction notices, and the authors' subsequent indexed publications. Blogs and news are excluded from scoring (may inform narrative).

- **A1 (context):** ≥ 1 formal published comment or rebuttal exists.
- **A2:** If A1, the authors published a reply.
- **A3:** Any correction, corrigendum, or in-print acknowledgment of a criticized point.
- **A4 (count):** Instances in the authors' subsequent papers citing the criticized result without acknowledging the published criticism.

A-items are analyzed conditionally on A1 = 1 and reported as secondary (power is limited by how many papers attracted formal comment).

## 8. Index S — Stylometry (mechanical)

Computed by script; no scorer judgment. Lexicons pinned in Appendix C.1 (Hyland 2005 hedge and booster lists).

- **S1:** Hedge density (hedges per 1,000 words).
- **S2:** Booster density (boosters per 1,000 words).
- **S3:** Figure count ÷ (equation count + 1).
- **S4:** Flesch reading ease of Abstract + final section.
- **S5:** First-person-plural rate per 1,000 words.

Secondary/exploratory: discriminative validity unknown; included because they are cheap and scorer-bias-proof.

## 9. Composites and hypotheses

- **CAL** = proportion of overreaching claims (§4.4). *H1: contrarian > mainstream.*
- **ENG** = mean of rescaled E1 (with E1b as a recorded qualifier), E2, E4, and reversed E3. *H2: contrarian < mainstream.*
- **PRAC** = mean of P1a, P1b, P2a, P2b, P3, P4, P6, P7 (P5 era-conditional). *H3: contrarian < mainstream.*

H1–H3 are the pre-registered primary, directional hypotheses. Indices A and S are secondary/exploratory. All items are defined and scored identically in both groups.

## 10. Scoring protocol

Scorer: Claude, model identifier and version pinned at freeze; identical prompt for every paper containing only this codebook and the paper text. Each paper scored in **3 independent runs**; item-level majority vote; disagreement rate logged per item as an instability metric and reported. Paper order randomized. Every non-mechanical score carries the §3 anchor. Full transcripts archived in the repo (`sources/behavior-study/transcripts/`). Human spot-audit: a pre-set random 10% of judgment items re-verified by Steve against anchors; adversarial audit openly invited on the full transcript archive.

## 11. Legibility audit

Before confirmatory scoring: for each sampled paper, a methods-and-results excerpt is prepared with identity, venue, acknowledgments, and reference list removed. A separate Claude run guesses group membership. Report accuracy/AUC. Pre-stated interpretation: if AUC > 0.8, blinding is deemed cosmetic; the study's defense then rests entirely on item-level auditability (§1), and results are framed accordingly. No outcome of this audit halts the study; it conditions the framing.

## 12. Validity checks

Pooled across groups: do PRAC and CAL predict whether a paper attracted ≥ 1 formal published comment (A1)? Reported as a criterion-validity check. (A1 is objective; "successful rebuttal" is not operationalized — too judgment-laden.) Known limitation: comments are also attracted by visibility; interpret modestly.

## 13. Analysis plan

Group comparison on CAL, ENG, PRAC by permutation test with **author-cluster** resampling (papers travel with their first/corresponding author; the contrarian corpus is heavily author-concentrated). Familywise error across the three primaries controlled by max-T within the same permutation scheme. Secondary indices reported with the same machinery, labeled exploratory. Effect sizes with cluster-bootstrap CIs. Descriptive covariates: venue tier, year, length. Instability metric (§10) reported alongside every item-level result. No interim analyses.

## 14. Threats and limitations (to appear verbatim in any write-up)

1. **Scorer bias, asymmetric exposure.** Claude's training corpus discusses flaws in heterodox climate papers more than flaws in mainstream ones. Mitigations: symmetric operational definitions fixed before scoring; anchored auditability; instability reporting; human spot-audit; publication of all transcripts. Not eliminable — disclosed.
2. **Stance legibility.** Blinding to group labels does not blind to stance. Handled by §11, honestly.
3. **Construct validity.** ENG/PRAC differences may partly reflect venue resources and review standards rather than audience design. Venue tier reported as covariate; inference worded accordingly.
4. **Selection.** The Petersen contrarian list conditions on visibility; the robustness frame (§2.5) partially addresses this. Claims are about the sampled corpora, not all contrarian work.
5. **No intent inference.** The design can show the corpora differ behaviorally in the direction predicted by audience-optimization. It cannot show authorial intent — and the Merchants-of-Doubt mechanism does not require it: an amplification ecosystem can select for these features regardless of author psychology. Findings will be worded as *selection-or-production* compatible.
6. **Correctness out of scope.** See §1 and Appendix B.
7. **Single-scorer design.** One model family scores everything. A second-model replication is a desirable extension, not part of v1.

## 15. Versioning and freeze rules

v0.1 = this pilot draft. Revisions during piloting are logged in §16 with rationale. **v1.0 freeze occurs before any confirmatory paper is sampled or scored.** Post-freeze amendments require a logged justification and a sensitivity analysis under the pre-amendment rules. The frozen codebook, sample list, and analysis code are committed to the repo before scoring begins.

## 16. Changelog (pilot revisions, logged)

- **v0.1-r1 — E1b added.** LS11 scores E1 = 2 (it engages the IPCC counter-position, archive p. 19) but the load-bearing rebuttal citation is a self-citation. E1 alone was too coarse; the qualifier records this without changing E1's definition.
- **v0.1-r2 — P1 split into P1a/P1b.** LS11's two-stage design contains a genuine out-of-sample element (cycles calibrated pre-1950, extrapolated forward) while its headline claims rest on in-sample fit. A single binary forced a false choice.
- **v0.1-r3 — P2 split into P2a/P2b.** LS11 reports a standard error on the fitted residual slope but no interval on the headline "half of IPCC" attribution or the 2100 forecast; FR11 propagates errors to its headline trend. The split captures the difference the original item blurred.
- **v0.1-r4 — Normative flag (§4.5) added.** FR11's closing urgency sentence is a policy implication, not an empirical claim; scoring it under C was category error, ignoring it was information loss. Flagged, not scored — symmetrically in both directions.

---

## Appendix A — Worked examples (pilot)

Levels/tiers per §4; anchors per §3. These examples are calibration exhibits, not the full pilot scoring.

**A.1 LS11 — C-item, maximal overreach.**
Claim (archive p. 19): "It had far higher pattern accuracy than any traditional analytical computer general circulation climate model output."
Level: **L4** (exhaustive comparative, "than any"). Tier: **T0** — no GCM output is analyzed or compared quantitatively anywhere in the paper (absence attested; search terms: "GCM", "general circulation", "model output", "pattern accuracy"). Overreach = **3** (maximum). This is the instrument's clearest positive.

**A.2 LS11 — C-item, calibrated claim (decision-rule demonstration).**
Claim (archive p. 2, Abstract): "Our results suggest that ... the anthropogenic contribution to climate change since 1970 should be around half of that previously claimed by the IPCC [2007]."
Governing marker "suggest" → **L2** (§4.2: "around" is an approximator and does not raise or lower the level; "should be" is embedded under "suggest"). Tier: **T1** — the attribution split rests on the in-sample decomposition (fit statistics, archive p. 8). Permitted at T1 is L2 → overreach = **0**. The instrument scores this headline claim as *calibrated*: the hedging verb matches the evidential tier. The paper's overreach lives elsewhere (A.1; and archive p. 20, "no more than 0.4 °C is likely to be" — L2 claim, T0 support for the UHI-adjusted figure, overreach 1).

**A.3 LS11 — P7 = 0.**
The residual-trend error "0.66 +/- 0.08 ºC/century (R2 = 0.59)" (archive p. 8) is reported with no autocorrelation or effective-df correction anywhere in the text (absence attested; search terms: "autocorrel", "effective", "degrees of freedom", "AR(1)"). The supplementary noise exercise (archive p. 38) adds white noise *to the fitted model* and re-fits — a null derived from the fitted structure itself, which §6/P7 excludes by definition. P7 = 0, both prongs anchored.

**A.4 LS11 — P1a = 1, P1b = 0.**
P1a: the cycle component is calibrated on pre-1950 data and extrapolated ("fit the model to the period prior to elevated greenhouse gases and then extrapolate it forward," archive p. 6; executed p. 8) — a genuine out-of-sample element. P1b: the headline claims (attribution split; 2100 forecast of "about 0.6 °C above 2000," archive p. 15) rest on the full-record in-sample fit and an unverifiable extrapolation; no out-of-sample support. This pair motivated revision r2.

**A.5 FR11 — C-item, high-tier assertive claim.**
Claim (p. 4): "there has not been any cessation, or even any slowing, of global warming over the last decade," introduced by "it becomes obvious" → **L4**. Tier: **T3** — five independent data sets, trend-by-start-year analysis with 2-σ errors under a stated ARMA(1,1) error model (p. 4 fig. 6; appendix pp. 7–8). Permitted at T3 is L4 → overreach = **0**. Demonstrates the instrument permits strong language when the paper's own machinery carries it.

**A.6 FR11 — instrument edge, honestly recorded.**
"This is the true global warming signal." (p. 6) scores L4/T3, overreach 0 — yet "true" overstates what an adjusted estimate is. The C-instrument passes it; the register is captured instead by S2 (booster density) and the ontological overstatement is noted qualitatively. The closing sentence ("...powerful evidence ... emphasizing the urgency of confronting the human influence on climate," p. 7) is normative → flagged under §4.5, not scored. Mainstream rhetoric is not invisible to the instrument; it is routed to the right items.

**A.7 FR11 — P3 = 1, P7 = 1.**
P3: input substitutions (SOI for MEI; Ammann et al. for Sato AOD; sunspot number for TSI) with "None of these substitutions affected the results in a significant way" (p. 2), plus leave-one-factor-out regression checks (p. 2). P7: explicit ARMA(1,1) effective-df correction with equations (appendix, pp. 7–8); note also the discounting of the marginally significant UAH quadratic term (p. 5) — conservative multiplicity behavior, recorded in narrative.

**A.8 LS11 — E1 = 2, E1b = 1.**
Engagement passage (archive p. 19): the paper states the IPCC counter-position ("more than 90% of the warming ... caused by anthropogenic forcing," with reference to AR4 figures 9.5a/b) and argues against it — E1 = 2. The load-bearing rebuttal citation is "[Scafetta, 2010]," an author self-citation → E1b = 1. FR11 comparison: engages the "discrepancies between the different global temperature records" debate (p. 1) with the paper's own five-dataset analysis as the rebuttal evidence — E1 = 2, E1b = 0.

## Appendix B — Benestad error-taxonomy coverage map

| Benestad category | Covered by | Notes |
|---|---|---|
| Statistical interval misinterpretation | C, P2a/b | via claim-evidence pairing |
| Effective-df failures | P7 | |
| Curve-fitting without out-of-sample evaluation | P1a/b | |
| Incomplete physics | P6 | presence of stated mechanism only |
| Timescale mismatches | P6, E1 | partial |
| Multiplicity | P7 | |
| Biased analytical design | P3 | partial |
| Selective data use | P3, P4 | partial |
| Misrepresentation of other publications | E1, A | partial; correctness of representation not adjudicated |
| Circular/self-derived null models | P7 | explicit exclusion clause |
| Missing contextual information | E1, E1b, E4 | the most common Benestad finding; primary ENG target |
| Unexamined presumptions | P6 | weak coverage |
| False dichotomy / irrelevant analogies | — | not covered (argument-quality adjudication) |
| Misconceived mathematics | — | deliberately not covered (correctness out of scope, §1) |
| Questionable data representation (figures) | — | not covered in v1; candidate for a figure-practices item in v2 |
| Implausible physics | — | not covered (correctness out of scope) |

## Appendix C — Pinned instruments (stubs; finalized at freeze)

**C.1 Lexicons.** Hedges and boosters: Hyland (2005), *Metadiscourse*, Appendix lists, verbatim. No additions or deletions permitted after freeze.

**C.2 Benchmark attribution corpus (E4).** Rule: the N = 10 most-cited attribution papers published 1995–2010 (citations counted in a fixed index, snapshot dated at freeze), plus the contemporaneous IPCC WG1 attribution chapter. Candidate members pending the mechanical count: IPCC AR4 Ch. 9 (Hegerl et al. 2007); Stott et al. 2000; Tett et al. 1999; Meehl et al. 2004; Thompson et al. 2009; Lean & Rind 2008; Hegerl et al. 2001. The list is fixed by the rule, not by this candidate slate.

**C.3 Search-term sets for absence attestations.** Per item, fixed at freeze; drafts embedded in the item definitions above.
