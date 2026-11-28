# Paper-Behavior Scoring Instrument (v0.2, operational)

A self-contained instrument for scoring a single paper. Give the scorer **this file plus one paper's anchored full-text transcript**, and nothing else. Score each item against anchored evidence; do not judge the correctness of the paper's science.

## Scope

This instrument scores *papers as behavior*. It does **not** adjudicate whether a paper's conclusions are correct. Every item is either (a) mechanical (computable from the text) or (b) a judgment call small enough to be verified by a reader of any persuasion against a quoted, page-anchored passage. Apply every item identically regardless of the paper's stance or conclusions. Score only what the item defines; do not import outside knowledge about the paper, its authors, or the correctness of its science.

## 3. Sources and anchoring conventions

Every non-mechanical score must carry (a) a verbatim quotation of ≤ 25 words, **or** an attested absence after a full-text search for stated terms, and (b) a page or line anchor to the archived source transcript. Anchors reference the archived transcript supplied with the paper (page markers in the transcript). Absence attestations must state the search terms used.

## 4. Index C — Rhetorical calibration

**4.1 Claim extraction.** From the **Abstract and the final section** (however titled — Conclusions, Summary, Discussion and conclusion), extract every sentence asserting a finding about the world derived from the paper's own analysis. Exclusions: pure methods descriptions; restatements of others' findings; normative/policy statements (flagged under §4.5, not scored); sentences describing the raw data record without analytic derivation; statements explicitly labeled assumptions ("we assume…" — noted, not scored). Explicit if–then claims are scored on the support for the inferential link, not the unasserted antecedent (level "Conditional", tier "link"; an adequately supported link scores O = 0). The sentence is the unit; if a sentence contains multiple distinct claims, score the strongest. Forward-looking claims are additionally tagged per §4.6.

**4.2 Certainty levels.** Governed by the epistemic marker(s) scoping the claim:

- **L1 Speculative:** may, might, could, possible, we speculate.
- **L2 Qualified:** suggest, indicate, appears, likely, probably, we estimate, consistent with; discourse verbs of argument (we have argued, we argue); internally hedged negation ("no clear/strong/convincing evidence for X").
- **L3 Assertive:** unhedged declaratives — is, shows, demonstrates, we find, we have shown, we can see, should be (conclusion-drawing).
- **L4 Emphatic:** any of — (i) a booster or absolute adverb scoping the claim: clearly, obviously, undoubtedly, certainly, definitely, truly, true, indeed, in fact, always, never, prove(s)/proved/proven, establish(es)/established, strictly, exactly, precisely, entirely, completely, purely, solely, only *(provisional enumeration; superseded verbatim by the pinned Hyland booster lexicon at freeze, stub C.1)*; (ii) a superlative or exhaustive comparative ("higher than any", "more than all"); (iii) an **unhedged negative-universal**: no X, none, not any, cannot, not able to ("does not provide any evidence", "none of these factors can…", "not able to reproduce"); (iv) an unqualified precise numeric forecast.

Decision rules: approximators (about, around, roughly, approximately, nearly, ~) are precision markers and never change the level. When multiple epistemic markers scope the same claim, the **weakest (most hedged) marker governs** ("suggests that X may…" → L1). A hedge governing the whole sentence sets the level regardless of embedded assertive verbs. Negated certainty is scored as a claim about the absence, at the level given by the rules above (unhedged universal negation → L4; internally hedged negation → L2).

**4.3 Evidential tiers.** The strongest support *the paper itself* provides for that claim:

- **T0:** No direct analytical support — asserted, or supported only by citation.
- **T1:** In-sample fit only (goodness of fit on data used for fitting).
- **T2:** Out-of-sample support for *this* claim — held-out data, cross-validation, or extrapolation **that the paper frames and evaluates as a test** (design stated, outcome reported). Extrapolation not framed and evaluated as a test remains T1.
- **T3:** Multiple independent data sources or methods converging within the paper, **or** formal uncertainty quantification (stated error model) bounding the claim.

Tiering of forward-looking claims is governed by §4.6.

**4.4 Scoring.** Permitted maximum certainty by tier: T0→L1, T1→L2, T2→L3, T3→L4. Per-claim overreach **O = max(0, level − permitted)**. Paper-level statistic **CAL** = proportion of non-forecast claims with O ≥ 1 (denominator excludes forecast-tagged claims per §4.6). Secondary: mean overreach; count of L4 claims at tier ≤ T1.

**4.5 Normative flag (recorded, not scored).** Sentences drawing policy or urgency implications, in either direction, are logged verbatim and not scored.

**4.6 Forecast tagging.** A claim asserting a state of the world at a time after the paper's publication is a **forecast**. Forecast claims are tagged (confirm any pre-supplied tag), and for each the scorer records: horizon; whether a formal uncertainty interval accompanies it (0/1); and its level per §4.2. Forecasts are **excluded** from CAL's numerator and denominator. A sensitivity statistic **CAL-FI** re-includes them, with tier capped at **T1 unless a formal predictive interval is stated** (then the paper's stated error model may earn T3). Record each forecast's (horizon, interval, level) regardless.

## 5. Index E — Contextual engagement

- **E1 (judgment, auditable):** Does the paper identify the prevailing counter-position to its central claim and engage it? **0** = not acknowledged; **1** = acknowledged without engagement (bare citation or dismissal); **2** = engaged (specific counter-evidence discussed with stated reasons for departure). The "prevailing counter-position" is the position of the contemporaneous IPCC assessment chapter relevant to the claim for a paper opposing that assessment; **for a paper whose central claim aligns with the assessment, it is the most prominent contemporaneous published challenge to that claim** (identified by a fixed rule at freeze).
- **E1b (qualifier):** If E1 = 2, does the engagement's evidential basis rest on author self-citations? **1** = yes (all load-bearing citations in the engagement passage share an author with the paper); **0** = no.
- **E2 (mechanical):** Fraction of reference-list entries that are peer-reviewed journal articles (categories: journal / assessment report / book or chapter / other).
- **E3 (mechanical):** Self-citation fraction — entries sharing ≥ 1 author with the paper.
- **E4 (mechanical):** Presence in the reference list of ≥ 1 entry from the pinned benchmark attribution corpus (stub C.2; finalized before freeze by a mechanical top-N-citations rule).

## 6. Index P — Methodological practices

Binary unless noted. "Reported" means in the paper or its supplementary material.

- **P1a:** Any model component evaluated out-of-sample (held-out data, verified extrapolation, or cross-validation). In-sample R² does not qualify. "Evaluated out-of-sample" follows the §4.3 **T2** standard — the extrapolation must be framed and evaluated by the paper as a test (design stated, outcome reported).
- **P1b:** The paper's *headline claim* is supported by an out-of-sample evaluation (same T2 standard).
- **P2a:** Uncertainty reported on fitted parameters (standard errors, CIs).
- **P2b:** Uncertainty propagated to the headline quantitative conclusion (interval stated on the number the abstract leads with).
- **P3:** Sensitivity analysis — results **shown** under ≥ 1 alternative specification, dataset, or input choice. "Results shown" means numeric, tabular, or graphical results reported under the alternative; a textual assertion that an unreported alternative gave similar results does not qualify. *Worked example: coefficients reported for two calibration windows in a table, or a result plotted under two alternative input reconstructions, each qualifies.*
- **P4:** Data sources fully specified and publicly available.
- **P5:** Code or full analytical recipe available. *Recorded for all papers; excluded from the composite for papers published before 2015 (era norm).*
- **P6:** A specific physical mechanism is identified for each fitted or proposed driver (stated mechanism with citation; the citation's independence is captured by E3, not here).
- **P7:** Degrees-of-freedom discipline — the paper reports accounting for autocorrelation, effective sample size, or model-selection multiplicity when computing significance or errors, **using a null model not derived from the fitted model itself** (a noise test that presupposes the fitted structure does not qualify).

## 7. Index A — Post-publication conduct

Window: publication + 8 years. Admissible sources: indexed comments/replies, journal correction notices, and the authors' subsequent indexed publications. Blogs and news are excluded from scoring (may inform narrative).

- **A1 (context):** ≥ 1 formal published comment or rebuttal exists.
- **A2:** If A1, the authors published a reply.
- **A3:** Any correction, corrigendum, or in-print acknowledgment of a criticized point.
- **A4 (count):** Instances in the authors' subsequent papers citing the criticized result without acknowledging the published criticism.

A-items are analyzed conditionally on A1 = 1 and reported as secondary.

## 8. Index S — Stylometry (mechanical)

Computed by script; no scorer judgment. Lexicons pinned in stub C.1 (Hyland 2005 hedge and booster lists).

- **S1:** Hedge density (hedges per 1,000 words). *Deferred until the lexicon is frozen; do not improvise the list.*
- **S2:** Booster density (boosters per 1,000 words). *Deferred until the lexicon is frozen.*
- **S3:** Figure count ÷ (equation count + 1). Scope: article body including in-article appendices, excluding separately filed supplementary information.
- **S4:** Flesch reading ease of Abstract + final section.
- **S5:** First-person-plural rate per 1,000 words. *(Text scope for S1/S2/S5 fixed at freeze.)*

Secondary/exploratory: included because they are cheap and scorer-bias-proof.

---

## Pinned-instrument stubs (required by §5 and §8; unfrozen)

**C.1 Lexicons.** Hedges and boosters: Hyland (2005), *Metadiscourse*, Appendix lists, verbatim. No additions or deletions permitted after freeze. *(Until frozen: S1/S2 deferred; the §4.2(i) booster enumeration is the provisional stand-in for Index C only.)*

**C.2 Benchmark attribution corpus (E4).** Rule: the N = 10 most-cited attribution papers published 1995–2010 (citations counted in a fixed index, snapshot dated at freeze), plus the contemporaneous IPCC WG1 attribution chapter. Candidate slate pending the mechanical count: IPCC AR4 Ch. 9 (Hegerl et al. 2007); Stott et al. 2000; Tett et al. 1999; Meehl et al. 2004; Thompson et al. 2009; Lean & Rind 2008; Hegerl et al. 2001. The list is fixed by the rule, not by this candidate slate.

**C.3 Search-term sets for absence attestations.** Per item, fixed at freeze; drafts embedded in the item definitions above.
