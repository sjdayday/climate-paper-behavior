# Paper-Behavior Codebook — v0.2 (pilot draft)

**Study:** Behavioral signatures distinguishing contrarian and mainstream climate-attribution papers
**Status:** DRAFT — not frozen. v0.2 enacts amendments r5, r6, r14, r15, r16a–e, and r31 (documentation-only, 2026-11-14) (changelog §16). Candidate amendments r19–r30 are under review in `sources/paper-behavior-codebook_candidate-amendments_r19-r30.md`; r31 takes the next free number in the series. Pilot papers: LS11, FR11 — **excluded from the confirmatory sample** (§2.4).

---

## 1. Purpose and design philosophy

This instrument scores *papers as behavior*. It does not adjudicate whether a paper's conclusions are correct. Every item is either (a) mechanical (computable by script) or (b) a judgment call small enough to be verified by a reader of any persuasion against a quoted, page-anchored passage. The study's credibility rests on that auditability, not on any claim that the scorer (an AI model) is neutral — a claim nobody should accept, including the scorer (§14).

Hypothesis under test: contrarian climate papers, as a group, exhibit features consistent with optimization for an educated lay audience rather than expert peers — confident claims outrunning in-paper validation, thin engagement with the strongest opposing evidence, omission of standard methodological practices. The instrument measures these symmetrically in both groups. Correctness is out of scope; some documented error categories are therefore deliberately unmeasured (Appendix B).

### 1.1 Design rationale: derivation of the feature families (r31; documentation-only)

**1.1.1 Derivation principle.** The hypothesis is a claim about intended audience. Audiences differ in two ways that matter for instrument design: what they can **check**, and what they **reward**. A feature family is admitted when (i) peer-optimization and lay-optimization predict **divergent optima** on it, and (ii) the divergence is **observable** from the paper and the indexed public record without adjudicating scientific correctness. The admitted families tile the paper's life cycle — in the text (C, S), in relation to the field (E), before submission (P), after publication (A):

- **C — Calibration.** Peers re-derive whether stated confidence matches evidential warrant; lay readers consume confidence directly as a credibility cue. Decoupling confidence from tier is cheap and effective for one audience, costly before the other.
- **E — Engagement.** Peers know what was omitted; lay readers do not. Ignoring the counter-position is nearly free under lay-optimization.
- **P — Practices.** Uncertainty propagation, degrees-of-freedom discipline, and out-of-sample tests are costly signals legible mainly to experts — effort with little lay payoff.
- **A — Post-publication conduct.** The peer game continues after publication (indexed critique, replies, corrections); the lay-persuasion game largely ends at uptake.
- **S — Stylometry.** The direct textual fingerprint of the intended reader: readability, boosters, self-mention, figure/equation balance.

Structurally, the set is three constructs, each operationalized twice, plus one: C and S measure audience-tuned confidence at two grains (claim-level judgment; document-level mechanics — deliberate redundancy for triangulation); E and A measure relation to the critical community at two time points; P stands alone. The derivation is a sufficiency argument, not a uniqueness proof: other decompositions exist. These five also survived the study's auditability requirement (§1, §3) — each admits page-anchored, quote-bounded scoring or pure mechanical computation.

**1.1.2 Admission filters.** Candidate families were screened against five filters: **F1** no correctness adjudication; **F2** the paper's or authors' own conduct — never their identity, and never the ecosystem's reception of the work; **F3** anchorable — scorer judgment bounded and verifiable under §3 conventions; **F4** recoverable from the artifact plus indexed record across the full sampling window; **F5** era/venue robustness, or explicit era-conditioning.

**1.1.3 Families considered and excluded.**

| Family considered | Failed | Note |
|---|---|---|
| Error/correctness counting (replication-based) | F1 | The founding exclusion; the approach of [1]. Collapses into the object-level dispute; differential-misclassification risk (§1, Appendix B). |
| Author identity: credentials, affiliation, funding sources, COI content | F2 | Unit is the paper; identity features import ad hominem inference; ecosystem-level identity effects are the terrain of [2]. Funding-*disclosure presence* as a P-item also fails F5 (disclosure mandates vary by venue and era). |
| Venue features (journal rank, review rigor) | F2 + endogeneity | Venue is partly an *outcome* of the behavior under study (gatekeeping selects on it); recorded as covariate only (§2), never matched. |
| Reception/uptake (media coverage, citations received, altmetrics, think-tank adoption) | F2 | The ecosystem's behavior toward the paper, not the authors'. Boundary rule: authors' own post-publication conduct is in (Index A); others' response is out, except A1, scored only as the trigger condition for A2. |
| Graphical rhetoric (axis truncation, baseline selection, smoothing choices) | F3 → F1 | Every drafted item collapsed into "is this the *right* baseline?" — i.e., back into F1. S3 is retained as its mechanical shadow. Flagged for post-pilot revisit if anchorable. |
| Argumentation structure (Toulmin coding, argument mining) | F3/F4 | Historically poor inter-coder reliability at whole-paper grain; automated extraction unvalidated for this use. |
| Press-release/outreach behavior | F4, partly F2 | Unrecoverable for older sample papers; often institutional rather than author conduct. Model if ever recoverable: [7]. |
| "Mathiness"/obscurantism as a judgment family | folded into S3 | [19] shows added mathematics can *raise* non-expert quality ratings — one reason Index S directionality is exploratory, not confirmatory. |

**1.1.4 Precedent literature.** Each family has an established literature in at least one domain; the per-family nearest neighbors are:

- **C:** hedging/booster corpus linguistics [3, 4] — the lexicon source pinned for §4.2 and S1/S2 (Appendix C.1); biomedical "spin" coding of claim strength against evidential warrant [5, 6]; exaggeration relative to source evidence in press releases [7]; booster inflation over time [8]. Qualitative climate precedent for mainstream *under*-claiming ("erring on the side of least drama") [9] — one motivation for scoring CAL symmetrically in both groups.
- **E:** citation-function classification [10, 11]; citation-distortion network analysis [12]. Closest precedents anywhere: reference-corpus and in-text citation comparisons of IPCC vs. NIPCC assessment reports [13, 14, 15], including four-way coding of each citation's function relative to mainstream claims (supporting / not supporting / uncertainty-creating / neutral) [15].
- **P:** reporting-guideline adherence audits (CONSORT/PRISMA family); transparency-indicator metascience [16, 17]; automated statistical-consistency checking [18]. Within climate, [1] is precedent *and foil*: it replicates errors; Index P is the de-contested redesign, scoring practice presence instead of adjudicating mistakes.
- **A:** thinnest precedent as a scored index. Nearest neighbor [20]: a 330-journal audit finding 1.9% of sampled articles drew any indexed post-publication critique, with 44 of 58 critiques receiving author replies, 41 of which asserted the original conclusions were unchanged. Those base rates underwrite A2's discriminating power and identify A3's open boundary case ("analysis modified, conclusions maintained") as the modal reply posture across science.
- **S:** the stylometric tradition; readability drift over time [21]. Climate-direct precedent [22]: computational text analysis of IPCC AR5 WG1 vs. NIPCC CCR-II finding the IPCC authors used *more* cautious, tentative language — the direction H1 predicts — with explicit abstention from adjudicating either report's accuracy. Think-tank doubt-corpus text mining [23].

Common limitation of the climate precedents [13–15, 22]: the unit is the assessment report — **N = 2 corpora**, the pseudoreplication this study's author-clustered, matched journal-article design (§2, §13) is built to escape. The biomedical literatures have the sample sizes but score quality variance *within* the mainstream, not a contrarian/mainstream contrast. The useful contrast class is CARDS [24], which classifies *what* contrarian claims assert; this instrument scores *how papers warrant* claims — orthogonal constructs. To the authors' knowledge (as of 2026-11-14), no study combines all five families at the journal-article level on an author-clustered matched sample; a systematic scoping search confirming this is a pre-registration deliverable, **pending**.

**1.1.5 Bibliography.** Verification classes: **[p]** = source document held in the project; **[v]** = identifiers machine-verified against Crossref or another external record (passes of 2026-11-14; verification script archived at `scripts/cite_verify.py`). Page fields follow the verified record. One entry, [4], is a monograph for which no Crossref record of the cited edition was located; its identifiers (author/title/publisher/year) stand as cited.

1. [p] Benestad R.E. et al. (2016). Learning from mistakes in climate research. *Theor. Appl. Climatol.* 126:699–703. [doi:10.1007/s00704-015-1597-5](https://doi.org/10.1007/s00704-015-1597-5)
2. [p] Petersen A.M., Vincent E.M. & Westerling A.L. (2019). Discrepancy in scientific authority and media visibility of climate change scientists and contrarians. *Nat. Commun.* 10:3502. [doi:10.1038/s41467-019-09959-4](https://doi.org/10.1038/s41467-019-09959-4)
3. [v] Hyland K. (1998). *Hedging in Scientific Research Articles.* Amsterdam: John Benjamins (Pragmatics & Beyond New Series 54). [doi:10.1075/pbns.54](https://doi.org/10.1075/pbns.54)
4. Hyland K. (2005). *Metadiscourse: Exploring Interaction in Writing.* London: Continuum. *(Monograph; no Crossref record of the 2005 edition located, 2026-11-14.)*
5. [v] Boutron I., Dutton S., Ravaud P. & Altman D.G. (2010). Reporting and interpretation of randomized controlled trials with statistically nonsignificant results for primary outcomes. *JAMA* 303(20):2058. [doi:10.1001/jama.2010.651](https://doi.org/10.1001/jama.2010.651)
6. [v] Chiu K., Grundy Q. & Bero L. (2017). 'Spin' in published biomedical literature: a methodological systematic review. *PLOS Biology* 15(9):e2002173. [doi:10.1371/journal.pbio.2002173](https://doi.org/10.1371/journal.pbio.2002173)
7. [v] Sumner P. et al. (2014). The association between exaggeration in health related science news and academic press releases: retrospective observational study. *BMJ* 349:g7015. [doi:10.1136/bmj.g7015](https://doi.org/10.1136/bmj.g7015)
8. [v] Vinkers C.H., Tijdink J.K. & Otte W.M. (2015). Use of positive and negative words in scientific PubMed abstracts between 1974 and 2014: retrospective analysis. *BMJ* 351:h6467. [doi:10.1136/bmj.h6467](https://doi.org/10.1136/bmj.h6467)
9. [v] Brysse K., Oreskes N., O'Reilly J. & Oppenheimer M. (2013). Climate change prediction: erring on the side of least drama? *Glob. Environ. Change* 23(1):327–337. [doi:10.1016/j.gloenvcha.2012.10.008](https://doi.org/10.1016/j.gloenvcha.2012.10.008)
10. [v] Moravcsik M.J. & Murugesan P. (1975). Some results on the function and quality of citations. *Soc. Stud. Sci.* 5(1):86–92. [doi:10.1177/030631277500500106](https://doi.org/10.1177/030631277500500106)
11. [v] Teufel S., Siddharthan A. & Tidhar D. (2006). Automatic classification of citation function. In *Proc. EMNLP 2006*. [doi:10.3115/1610075.1610091](https://doi.org/10.3115/1610075.1610091)
12. [v] Greenberg S.A. (2009). How citation distortions create unfounded authority: analysis of a citation network. *BMJ* 339:b2680. [doi:10.1136/bmj.b2680](https://doi.org/10.1136/bmj.b2680)
13. [v] Jankó F., Móricz N. & Papp-Vancsó J. (2014). Reviewing the climate change reviewers: exploring controversy through report references and citations. *Geoforum* 56:17–34. [doi:10.1016/j.geoforum.2014.06.004](https://doi.org/10.1016/j.geoforum.2014.06.004)
14. [v] Jankó F., Papp Vancsó J. & Móricz N. (2017). Is climate change controversy good for science? IPCC and contrarian reports in the light of bibliometrics. *Scientometrics* 112(3):1745–1759. [doi:10.1007/s11192-017-2440-9](https://doi.org/10.1007/s11192-017-2440-9)
15. [v] Jankó F. et al. (2020). Sources of doubt: actors, forums, and language of climate change skepticism. *Scientometrics* 124(3):2251–2277. [doi:10.1007/s11192-020-03552-z](https://doi.org/10.1007/s11192-020-03552-z)
16. [v] Hardwicke T.E. et al. (2020). An empirical assessment of transparency and reproducibility-related research practices in the social sciences (2014–2017). *R. Soc. Open Sci.* 7:190806. [doi:10.1098/rsos.190806](https://doi.org/10.1098/rsos.190806)
17. [v] Serghiou S. et al. (2021). Assessment of transparency indicators across the biomedical literature: how open is open? *PLOS Biology* 19(3):e3001107. [doi:10.1371/journal.pbio.3001107](https://doi.org/10.1371/journal.pbio.3001107)
18. [v] Nuijten M.B., Hartgerink C.H.J., van Assen M.A.L.M., Epskamp S. & Wicherts J.M. (2016). The prevalence of statistical reporting errors in psychology (1985–2013). *Behav. Res. Methods* 48(4):1205–1226. [doi:10.3758/s13428-015-0664-2](https://doi.org/10.3758/s13428-015-0664-2)
19. [v] Eriksson K. (2012). The nonsense math effect. *Judgm. Decis. Mak.* 7(6):746–749. [doi:10.1017/S1930297500003296](https://doi.org/10.1017/S1930297500003296)
20. [v] Hardwicke T.E., Thibault R.T., Kosie J.E., Tzavella L., Bendixen T., Handcock S.A., Köneke V.E. & Ioannidis J.P.A. (2022). Post-publication critique at top-ranked journals across scientific disciplines: a cross-sectional assessment of policies and practice. *R. Soc. Open Sci.* 9(8):220139. [doi:10.1098/rsos.220139](https://doi.org/10.1098/rsos.220139)
21. [v] Plavén-Sigray P., Matheson G.J., Schiffler B.C. & Thompson W.H. (2017). The readability of scientific texts is decreasing over time. *eLife* 6:e27725. [doi:10.7554/eLife.27725](https://doi.org/10.7554/eLife.27725)
22. [v] Medimorec S. & Pennycook G. (2015). The language of denial: text analysis reveals differences in language use between climate change proponents and skeptics. *Climatic Change* 133(4):597–605. [doi:10.1007/s10584-015-1475-2](https://doi.org/10.1007/s10584-015-1475-2)
23. [v] Boussalis C. & Coan T.G. (2016). Text-mining the signals of climate change doubt. *Glob. Environ. Change* 36:89–100. [doi:10.1016/j.gloenvcha.2015.12.001](https://doi.org/10.1016/j.gloenvcha.2015.12.001)
24. [v] Coan T.G., Boussalis C., Cook J. & Nanko M.O. (2021). Computer-assisted classification of contrarian claims about climate change. *Sci. Rep.* 11 (2021). [PMC8595491](https://pmc.ncbi.nlm.nih.gov/articles/PMC8595491)

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

**v0.2-r19 (2026-11-14).**
- **r19 enacted (§1.1):** design-rationale section added — derivation principle, admission filters F1–F5, excluded-family register, precedent bibliography with verification classes [p]/[v]/[k]. **Documentation-only: no scoring rule changed.** [k]-class citation identifiers are queued for verification at the Appendix C pinning step.
- **r17 registered as pending** (source: Scoring Exhibit 3, Connolly et al. 2021): internal conflict — §6 keeps P5 era-conditional (in composite for post-2015 papers) while §9's PRAC list omits P5 entirely. Resolve before freeze; exhibits report both composite values meanwhile.
- **r18 registered as pending** (source: Scoring Exhibit 3): §4.1 extraction convention — claims attributing conduct to specific actors are scored; field-state meta-discourse ("the debate is ongoing") is excluded; characterization-of-a-cited-document's-content is excluded as restatement, while inference about the citing actor's intent is scored.
- **r19 verification pass completed (2026-11-14, later same day):** api.crossref.org added to the environment allowlist; 13 of the 14 formerly [k]/unlinked entries machine-verified and upgraded to [v] with DOIs (entries 3, 5, 7–12, 17–19, 21, 23). Entry [4] (Hyland 2005): no Crossref record of the cited monograph edition located; book identifiers stand as cited, class tag removed. Verification script (`cite_verify.py`) archived with the study files. The [k] class is now empty and retired from the class note.

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
