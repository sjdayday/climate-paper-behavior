# Paper-Behavior Codebook — Candidate Amendments r19–r30

**Applies to:** `paper-behavior-codebook_v0.2.md` (pilot draft, not frozen).  
**Status:** CANDIDATES. Nothing here is enacted and the codebook files are unchanged. Each item awaits Steve's sign-off (table in §8).  
**Drafted:** 2026-11-13, by Claude, from a review of the research on AI text coding against codebook v0.2, Pilot Exhibits 1–3 and the equivalence harness.  
**Companion:** `scorer-validity-explainer_draft1.md` gives the reasoning and the literature at length. This file gives the proposed text.  
**Numbering:** continues the codebook series. Pending items r7–r12 and candidates r17–r18 are not restated; interactions are listed in §6.

A note on authorship: the scorer under review is Claude, and Claude drafted these. Read them as one party's proposals.

Each entry gives the problem, the evidence, text written to be pasted into the named section if adopted, the cost, and the decision needed. Numbers marked as estimates are mine and unmeasured.

---

## 1. Summary

| ID | Touches | Change in one line | Must be settled | Main cost |
|---|---|---|---|---|
| r19 | new §12.2; §10 | Calibration substudy: blind, from-scratch human reference coding on a seeded sample of authors in both groups | Design at freeze; coding during the confirmatory phase | Coder time (est. ~100 h) |
| r20 | §10 | Re-scope the 10% spot-audit as anchor verification; stratify it; record who verifies | At freeze | Small |
| r21 | new §13.2 | Reference-coded contrast, bias-adjusted contrast, tipping point, wording rule | At freeze | Analysis code |
| r22 | new §12.3 | Counterfactual tests of the instrument: evidence-edit and stance-mirror | Before freeze | Preparation time |
| r23 | new §11.1; §12 | Recognition probe; the A1 criterion check no longer treated as independent | At freeze; probe before scoring | Small |
| r24 | §14; §13; §13.1 | Replace "non-differential by construction"; report instability by group; scope note on the symmetry criterion | At freeze | None |
| r25 | §5; §9 | ENG: ceiling rule, status of H2, E1's open rule, E4, E1b | Before freeze | Decisions |
| r26 | §2.4; App. B; §15 | Six more pilot papers from outside the frame, weighted to mainstream; counterpart coverage map; items invited from the other side | Before freeze | Scoring, research, outreach |
| r27 | §2.5; §14.4 | Name the citation-ranked comparison group as a threat; add a comparator not selected on citations | At freeze | Extra scoring |
| r28 | §10; §14 | Record exact model identifiers and request parameters; add model retirement as a threat | At freeze | None |
| r29 | new §13.3; §14.7 | Pre-registered configuration arms (second model, paraphrased codebook, optional other developer); report all; labeling rule | At freeze | API cost (est. a few hundred dollars per full arm) |
| r30 | new §12.4 | Single-pass versus item-isolated scoring probe | Before freeze | Small |

"Before freeze" means the result can change the instrument. "At freeze" means text to fix in v1.0.

If resources bind, the core is r19 with r21, which are the only items that put a number on stance-correlated scorer error, and r25 with r26, which are the only ones that can change what is measured. r20, r23, r24 and r28 cost almost nothing.

---

## 2. Group A — Measuring scorer error against independent human coding

### r19 — Calibration substudy (new §12.2)

**Problem.** The codebook names stance-correlated scorer error as its first threat (§14.1) and nothing in v0.2 measures it. The §10 audit re-verifies the scorer's own anchored calls and is carried out by the study author. Calibration work of this kind was recommended in an earlier design discussion but never entered the codebook.

**Evidence.**
- Ashwin, Chhabra & Rao (2025) compared model coding of interview transcripts with expert coding. Model errors were related to interviewees' characteristics on many codes, and a downstream coefficient changed sign and significance. Their test is a regression of coder error on unit characteristics.
- Egami et al. (2023) showed that using model labels directly biased downstream estimates even when the labels were 80–90% accurate. Their correction needs expert labels on a sample with known inclusion probability, and it takes those labels as the standard, which presupposes they were made without sight of the model's output.
- Baumann et al. (2025) found human labels to be the main protection against false positives.
- Pilot Exhibit 1's erratum logs two scorer errors on LS11: one harsh to the contrarian paper (P3) and one lenient to it (negative-universal levels). Two errors estimate nothing, but they show the quantity exists.

**Proposed text.**

> **12.2 Calibration substudy.**
>
> (a) *Sample.* A seeded random draw of *m* authors per group from the confirmatory sample and, for each drawn author, one of that author's sampled papers chosen by the same generator. The seed and *m* are committed at freeze (default *m* = 12). Inclusion probabilities are recorded.
>
> (b) *Coders.* Each calibration paper is coded by two people working independently and from scratch. They receive the frozen codebook and the paper text. They do not see scorer output, anchors, transcripts, or each other's codes. Neither is the study author.
>
> (c) *Scope.* Index C in full (claim extraction from the Abstract and final section, forecast tag, level, tier), E1 and E1b, and every P item. Absences are established by reading the paper, not by the C.3 search terms.
>
> (d) *Reference standard.* Items on which the two coders agree form the reference. Disagreements go to a third coder under the same blinding. Raw and resolved codes are archived and hashed before any coder sees scorer output. Inter-coder agreement (Krippendorff's α) is reported per item family.
>
> (e) *Outputs, by group, with cluster-bootstrap intervals (authors as clusters).* Scorer recall and precision on claim extraction; level agreement; tier agreement; sensitivity and specificity of the overreach flag (O ≥ 1) and of each P item; and, per paper, composite(scorer) − composite(reference) for CAL and PRAC.
>
> (f) *Test.* Scorer-minus-reference error is regressed on group, per item family, with authors as clusters (after Ashwin et al. 2025). The between-group difference in each error rate is the pre-registered quantity.
>
> (g) *Use.* Results feed §13.2. No outcome halts the study; it conditions the analysis and the wording, as §11 does.

**Precision, roughly (my estimate).** The pilot papers yielded 28, 14 and 19 claims. At 12 papers per group and about 20 claims each, a between-group difference of about 9 points in a claim-level error rate is detectable at 80% power from a 10% base rate if claims were independent. With a design effect of 2 for clustering within papers, about 12–13 points.

**Cost.** Coder time. My guess is 1.5–3 hours per paper per coder, so about 100 coder-hours at *m* = 12, plus adjudication. Time one pilot paper before committing to *m*.

**Decision needed.**
1. Who codes. Options: (i) two paid coders with quantitative training and no publication record on climate attribution; (ii) one coder nominated from each side of the debate; (iii) Steve plus one independent coder, disclosed as the weaker design.
2. The value of *m*.
3. Whether r10 (first-author-only) is settled first, since it fixes which papers an author contributes.

### r20 — Re-scope the §10 spot-audit

**Problem.** As written (v0.1 §10), the audit is "a pre-set random 10% of judgment items re-verified by Steve against anchors." Random sampling is right. Three limits are not stated.
- It is verification, not coding. A person who has seen the score and the quoted passage is checking a proposal, and the person is the study's author.
- It cannot see absences. Overreach is driven by tiers below T3, and every such tier asserts that no stronger support exists anywhere in the paper (§3; Appendix A.1). An anchor can show a claim. It cannot show that support is missing, and re-running the C.3 search terms checks the search. The draft term lists also come from the pilot papers' vocabulary.
- Its frame is scored items, so claims the scorer never extracted are outside it. The harness README records full-extraction agreement as untested, because the equivalence runs use a fixed claim list.

**Proposed text** (replaces the last sentence of v0.1 §10).

> **Anchor verification.** A pre-set random 10% of judgment items, stratified by group and by score direction (overreach or none; practice present or absent), is re-verified against its anchor. For each item the verifier records *supported*, *not supported* or *indeterminate*. The verifier's identity is recorded, along with the fact that they see the scorer's output and know the hypothesis. At least half of the sampled items are verified by someone other than the study author. Results are reported by group.
>
> This check shows whether scored items are supported by what they cite. It does not show that support or practices recorded as absent are absent, or that claim extraction is complete. Those are measured in §12.2.
>
> Adversarial audit of the full transcript archive remains openly invited.

**Cost.** Small.

**Decision needed.** Who verifies the half not done by Steve.

### r21 — Analyses that use the reference coding (new §13.2)

**Problem.** r19 produces error rates. The analysis plan needs a pre-stated use for them, or they become a post hoc lever.

**Evidence.** Egami et al. (2023) for the logic of the correction. Baumann et al. (2025) for its cost: in their tests the correction estimators cut false positives but raised false negatives by up to 60 points, and an analysis on 100 human labels alone gave the lowest false-positive risk on average.

**Proposed text.**

> **13.2 Reference-anchored analyses** (pre-registered; secondary to §13).
>
> (a) *Reference-coded contrast.* The group difference in CAL and in PRAC is computed on the calibration sample from reference codes alone and reported with its interval, beside the scorer-based estimate on the same papers.
>
> (b) *Bias-adjusted contrast.* For each calibration paper, *d* = composite(scorer) − composite(reference). δ is the weighted mean of *d* in the contrarian calibration sample minus the weighted mean of *d* in the mainstream calibration sample, with weights from the §12.2 inclusion probabilities, so that δ estimates the bias in the §13 author-averaged statistic. The adjusted contrast is Δ − δ, where Δ is the §13 scorer-based contrast. Its interval comes from a joint cluster bootstrap over authors.
>
> (c) *Tipping point.* For each primary hypothesis the write-up states the value of δ that would reduce the contrast to zero, beside the estimated δ and its interval.
>
> (d) *Wording rule.* If the interval for the adjusted contrast excludes zero in the predicted direction, the result is described as holding after correction for measured scorer error. If it includes zero, the write-up says the scorer-based result is not confirmed by reference coding, whatever the §13 p-value.

**Notes.**
- (b) is the difference-in-means case of the design-based correction in Egami et al. (2023): the scorer-based estimate on everything, minus the average scorer-minus-reference gap on a known-probability subsample. It is unbiased for the reference-coded contrast whatever the scorer's error structure, provided the reference coding is independent of the scorer.
- It costs precision, because δ rests on 2*m* papers. If the spread of *d* across papers is 0.15, the standard error of δ at *m* = 12 is about 0.06 (my estimate). For scale, the pilot pair's CAL values are 0.577 and 0.000.
- That loss of precision is why §13 stays primary and (d) governs the wording.
- The regression-form estimators (DSL; Confidence-Driven Inference, Gligorić et al. 2025) are not proposed as primary. They are built for regression on document-level data, not for author-block permutation on author-averaged composites.

**Cost.** Analysis code.

**Decision needed.** Whether (d) is acceptable, since it lets a significant §13 result be reported as unconfirmed. The alternative is to make the adjusted contrast co-primary.

---

## 3. Group B — Is the score sensitive to stance?

### r22 — Counterfactual tests of the instrument (new §12.3)

**Problem.** The design argues that items are close to clerical. Two things are untested: whether a score moves when the thing it is supposed to measure changes, and whether it stays put when only the paper's stance changes. Both can be tested by experiment before any confirmatory paper is touched.

**Evidence.**
- Dycke & Gurevych (2026) edited sound AI and NLP papers to plant flaws in their research logic and compared model-written reviews of the two versions. The flaws had no significant effect on the reviews. Their setting is free-form reviewing, not anchored item scoring, so this does not show the instrument fails. It shows the skill cannot be assumed.
- Kim et al. (2026, preprint) held public comments constant and varied only the attributed identity of the commenter. Summaries differed with attributed occupation across every model tested.
- Halterman & Keith (preprint) propose behavioral tests of this kind as a standard check on whether a model follows a codebook.

**Proposed text.**

> **12.3 Counterfactual tests of the instrument.** Run before freeze, on material outside the confirmatory sample. Results are published whatever they show.
>
> (a) *Evidence-edit test: does the score respond to what it should?* From at least six source papers outside the confirmatory sample (the pilot papers and papers outside the §2.2 window, from both groups), a logged set of edited versions is prepared. Each edit changes the in-paper support for one identified claim and nothing else. Four edit types, each applied at least five times: (1) delete the passage reporting a held-out test; (2) keep an extrapolation but remove the sentences that frame and evaluate it as a test; (3) remove the stated error model behind an interval; (4) insert a sentence asserting that a result was validated or robust, with no result shown. Each edited paper is scored under the §10 protocol. Expected: under (1)–(3) the targeted claim's tier falls as §4.3 requires; under (4) no tier or P item rises. Reported: the share of edits scored as the codebook requires, by edit type and by source-paper group, and the share of untargeted items that change, for comparison with the run-to-run rate.
>
> (b) *Stance-mirror test: does the score ignore what it should?* At least 20 matched pairs of short passages (a methods summary and three concluding sentences) are written to a template. Within a pair the certainty markers, the evidence described and the length are the same. Only the direction of the conclusion relative to the contemporaneous assessment is reversed. Passages are scored on Index C. Reported: within-pair differences in level, tier and O. The expectation is no mean difference, tested against an equivalence margin fixed at freeze (placeholder: 0.25 of a level).
>
> (c) *Use.* An item that fails (a) is not measuring what its definition says and is revised or dropped before freeze. A difference outside the margin in (b) is reported in §14 as a measured stance effect and carried into the reading of §13.2.
>
> (d) *Preparation.* Edits and passages are written to a protocol fixed in advance, checked by a second person for parity, archived with hashes, and never written in the same session as a scoring run.

**Limits.** Synthetic passages are not papers, so a pass on (b) does not establish invariance on real ones. The scorer may recognize the pilot papers, and what it remembers could mask the effect of an edit. These tests are cheap evidence about the instrument. They do not replace r19.

**Cost.** Mostly preparation, a few days by my estimate. Roughly 30–50 scoring runs.

**Decision needed.** The counts and the margin; who writes the edits and who checks them.

### r23 — Recognition probe; the A1 criterion check (new §11.1; §12)

**Problem.** §14.1 already says the scorer's training data discusses flaws in contrarian papers more than flaws in mainstream ones. The mitigations listed there disclose the problem. None estimates its size. The harness prompt tells the scorer not to import outside knowledge of the papers or their reception, which is a request and cannot be verified to work. Two specific consequences are unaddressed.
- §12 checks whether CAL and PRAC predict A1 (a formal published comment exists). The scorer may know which papers drew comments, so agreement is not independent evidence. §12 lists visibility as the limitation, not this.
- Exhibit 3's judgment log (item 9) says the practice checklist "independently flagged, before any reference to that rebuttal," the gaps the published rebuttal exploits. That independence cannot be established.

**Evidence.** Mostly the design's own threat list. The literature is thin here. Dycke & Gurevych built their framework to run on unseen papers to avoid contamination. Ashwin et al. read their models' over-assignment of codes as preconceptions carried in from training.

**Proposed text.**

> **11.1 Recognition probe.** Before scoring, a separate run receives only the bibliographic record of each sampled paper (authors, year, title, venue) and is asked (i) to state the paper's method and main conclusion and (ii) to state anything it knows about published comments, rebuttals, corrections or public dispute concerning it. Each answer is coded 0 (nothing), 1 (vague or partly wrong) or 2 (specific and correct) against the paper and the A-index record, by a person, to a rubric fixed at freeze. Reported: recall by group, and the association of CAL and PRAC with reception recall within each group.
>
> **§12, added.** Because the scorer may know which papers attracted formal comment (§14.1), agreement between the indices and A1 is not independent evidence of validity. The check is reported overall and separately for papers with reception recall of 0.
>
> **§12, exploratory.** If any papers by frame authors in the topic stratum were published after the pinned model's training cutoff, they are scored and reported descriptively as an out-of-memory sample.

**Proposed annotation for Exhibit 3, judgment log item 9** (not applied; exhibits are preserved as issued).

> *Annotation, [date].* The statement that the checklist flagged these gaps independently of the published rebuttal cannot be established. The scorer may have met the rebuttal in training (codebook §14.1). The flags stand on their anchors. The claim of independence is withdrawn.

**Limits.** What a model reports knowing is an imperfect measure of what it knows. It may know more than it says, and it may invent. A recall score of 0 is weak evidence of no knowledge.

**Cost.** One short run per paper, plus coding the answers.

**Decision needed.** Adopt the probe; add the Exhibit 3 annotation.

### r24 — Replace "non-differential by construction" (§14; §13; §13.1)

**Problem.** v0.2 added to §14 that run-to-run noise "attenuates rather than biases (non-differential by construction when one model scores all papers)." That holds for a uniform severity offset between two models. It does not hold for one scorer's own errors, which is what Ashwin et al. measured. It is not guaranteed even for run-to-run noise, which can differ between groups.

**Evidence.**
- The first equivalence probe (`results.md`) reports non-unanimous items across three runs of the candidate model at 8% on FR11 and 13% on LS11, about 2 of 24 and 5 of 38 items. Two papers support no conclusion about groups. They show the quantity is measurable and need not be equal.
- That figure was measured with the claim list fixed, so it excludes extraction variance.
- §13.1's symmetry criterion compares the two models with each other. Both come from one developer (§14.7).
- Baumann et al. (2025) found no correlation between human inter-annotator agreement on a task and the risk of wrong conclusions from model labels. Agreement statistics are not validity evidence.

**Proposed text.**

> **§14, replacing the sentence added in v0.2.** Single-item scores showed about 10% run-to-run disagreement in the first equivalence probe (non-unanimous items across three runs of the candidate model: 8% on FR11, 13% on LS11), measured with the claim list fixed, so extraction variance is excluded. Majority-of-3 voting and aggregation into composites reduce its effect. Whether this noise, or systematic scorer error, differs between groups is an empirical question and not a property of the design. Instability is reported by group (§13), and systematic error by group is estimated in §12.2.
>
> **§13, added.** The instability metric is reported by group as well as by item, with the between-group difference and its cluster-bootstrap interval.
>
> **§13.1, added after criterion 3.** Criterion 3 detects stance-correlated divergence *between* the two models. It cannot detect error the two share. That is addressed by §12.2 and §12.3.

**Cost.** None.

**Decision needed.** Adopt the wording.

---

## 4. Group C — What the items sample

### r25 — ENG: ceiling rule, status of H2, E1's open rule, E4, E1b (§5; §9)

**Problem.** In the pilot, two of ENG's four components did not vary.

| Paper | E1 | E1b | E2 | E3 | E4 | ENG |
|---|---|---|---|---|---|---|
| LS11 | 2 | 1 | 0.885 | 0.128 | 1 | 0.939 |
| FR11 | 2 | 0 | 0.895 | 0.000 | 1 | 0.974 |
| Connolly et al. 2021 | 2 | 0 | 0.925 | 0.194 | 1 | 0.933 |

ENG spans 0.04 across the three papers, and almost all of that is E3 (self-citation). E1b, the one E-judgment that varied, sits outside the composite. Appendix B names "missing contextual information" as the primary ENG target, and the pilot gives no sign that ENG registers it. A paper written to dispute the IPCC position will usually state that position and argue against it, which is what E1 = 2 asks for. Exhibit 3 calls Connolly et al. "exemplary on the letter of the item."

Caveats: three papers; the pilot pair was chosen partly because both engage the public debate (§2.4); Connolly et al. is a 68-page review.

Three further gaps.
- r6 says an aligned paper's counter-position is "identified by a fixed rule at freeze." That rule is unwritten.
- With r6, E1 has two operationalizations selected by a judgment about the paper's stance. v0.1 §9's "defined and scored identically in both groups" no longer describes it.
- E4 received no counterpart to r6. Its benchmark corpus (Appendix C.2) is the mainstream attribution canon for every paper.

**Proposed text.**

> **§9, ceiling rule (all composites).** After the extended pilot (r26) and before freeze, a component that takes the same value in at least 90% of pilot papers is removed from its composite and reported descriptively. If E1 is removed, or fewer than three components of ENG remain, H2 becomes a secondary hypothesis and max-T (§13) runs over the remaining primaries. The decision and the pilot table are logged in §16.
>
> **§9, wording.** Replace "All items are defined and scored identically in both groups" with: "All items are scored by the same rules in both groups. E1 is the one item whose operationalization depends on a judgment about the paper's stance (§5)."
>
> **§5, stance classification.** Whether a paper's central claim opposes or aligns with the contemporaneous assessment is recorded as its own item, with a quotation and anchor, before E1 is scored.

**Decisions needed** (no text proposed, because I have no rule I can defend for the first).
1. *E1's counter-position for aligned papers.* There is no mechanical counterpart to "the contemporaneous assessment." Each candidate has a cost.
   - (a) The challenge the paper itself names. Checkable from the paper; lets a paper pick a weak foil.
   - (b) The most-cited opposing paper in the topic stratum over the preceding five years. Mechanical; selects on citations and needs a stance-classified corpus.
   - (c) Score E1 only for opposing papers and report it outside the composite. Plain about the asymmetry; loses the item for half the sample.
2. *E4.* (a) Drop it from ENG under the ceiling rule. (b) Keep it as a descriptive check. (c) Replace it with the share of the benchmark corpus cited, which varies more but is still relative to the consensus literature.
3. *E1b.* Whether it enters ENG.
4. *The name.* If ENG ends as E2 and E3, it measures reference-list practice and should be called that.

**Cost.** Decisions only, once r26's pilot papers are scored.

### r26 — Extended pilot, counterpart coverage map, items invited from the other side (§2.4; Appendix B; §15)

**Problem.** Identical rules for both groups do not make the choice of rules even-handed.
- Appendix B is a coverage map of the error taxonomy in Benestad et al. (2016), which catalogues problems found in a selection of 38 contrarian papers. Twelve of its sixteen categories are mapped to items. There is no counterpart map for failure modes alleged against mainstream papers.
- The pilot has scored two contrarian papers and one mainstream paper. The one mainstream paper surfaced r6, which Exhibit 2 describes as an asymmetry in the instrument caught only because a mainstream paper was piloted. It also surfaced Appendix A.6, where FR11's "This is the true global warming signal" passes Index C with no overreach, and the A-index blind spot logged in Exhibit 2 (self-initiated re-testing is invisible).
- The instrument was piloted on short empirical papers (Exhibit 3, judgment log item 1).

**Evidence.** Coan et al. (2021) built their taxonomy of contrarian claims from contrarian blogs and think-tank output, and note themselves that a small share of its categories are things contrarians tend to say that are not contrary to mainstream views. An instrument built from one side's output inherits that side's outline.

**Proposed text.**

> **§2.4, added.** Before freeze the pilot is extended by at least six papers drawn from outside the confirmatory frame (outside the §2.2 window, or not by a listed author), so that no confirmatory unit is used up. At least four are mainstream, including at least one detection-and-attribution paper based on climate-model simulations and at least one that attracted a formal published comment. At least two are contrarian, including at least one that does not cite the contemporaneous assessment. The selection rule and the candidates are logged before any is scored. Each is scored as a pilot exhibit with a judgment log.
>
> **Appendix B′, counterpart coverage map.** A table of failure modes alleged against mainstream attribution papers in formal published comments and in the 2013 ESDD open-review record, each mapped to the item that would register it or marked not covered, on the same footing as Appendix B. Compiled before freeze, with sources listed.
>
> **§15, added.** Before freeze, the draft codebook is sent to at least three authors or commentators from the contrarian side of the published or open-review record, with an invitation to propose items or objections. Each proposal receives a logged disposition: adopted, adopted in modified form, or declined with a reason other than the proposer's stance. The log is published with the frozen codebook.

**Why outside the frame.** The contrarian side is planned as a census (r11–r12). Every pilot paper taken from the frame is a confirmatory unit lost.

**Cost.** Scoring six pilot papers; compiling B′; outreach. The outreach discloses the study before data collection and some recipients will decline or respond publicly. A fallback that contacts nobody is to compile proposed criteria from the existing ESDD open-review comments.

**Decision needed.** Each of the three parts separately. The third is the one with consequences outside the repo.

### r27 — The comparison group (§2.5; §14.4)

**Problem.** §14.4 covers selection on the contrarian side (the Petersen list conditions on visibility) and §2.5 adds a robustness frame for it. Nothing covers the other side. The Petersen climate-scientist list is the 386 most-cited authors. Selection on citation rank plausibly selects for the practices PRAC and CAL reward, so the primary contrast compares prominent contrarians with the most-cited mainstream scientists, not with typical ones. This is the endogeneity that ruled out citation-ranking papers within author in the r11–r12 discussion.

**Proposed text.**

> **§14.4, added.** The climate-scientist list is ranked by citations. The primary contrast is therefore between prominent contrarian authors and the most-cited mainstream authors. Differences may partly reflect what citation rank selects for. Claims are worded accordingly.
>
> **§2.5, added: second robustness frame.** A mainstream comparator not selected on citations: first authors of papers in the same topic stratum and window, drawn by seeded random sample from a fixed bibliographic query (query string, index and snapshot date committed at freeze), excluding anyone on either Petersen list. Scored and analyzed like the NIPCC frame: secondary, same machinery.

**Cost.** Writing the query; scoring the extra papers. A sample half the size of the primary mainstream sample would show direction.

**Decision needed.** Adopt the threat wording; adopt the second frame and its size.

---

## 5. Group D — How the scorer is run

### r28 — Configuration record; model retirement (§10; §14)

**Problem.** §10 pins "model identifier and version" at freeze and lists no request parameters. The v2 harness sets them: temperature 1.0, thinking budget 8,000 tokens, maximum output 14,000 tokens, and model names passed as `claude-fable-5` and `claude-opus-5`. Whether those names are dated snapshots or aliases should be confirmed at freeze. §14 does not mention that the instrument stops being runnable when the model is withdrawn.

**Evidence.** Baumann et al. (2025) list decoding parameters among the choices to pre-register. Ollion et al. (2024) set out the reproducibility problem with proprietary models. Ornstein et al. (2025) report that the models behind their own published results were later withdrawn from the public API.

**Proposed text.**

> **§10, added.** The frozen record states, for each scorer: the exact model identifier recorded from each API response where the response reports one (not only the name passed in the request), the dates of the runs, temperature, thinking budget, maximum output tokens, and every other request parameter the harness sets. The harness script and its hash are committed with the frozen codebook.
>
> **§14, added (8). Model retirement.** The scoring model is proprietary and will be withdrawn at some point. After that the instrument cannot be re-run. What remains checkable is the transcript archive and every anchored item, and the study's claims are worded to rest on that archive.

**Cost.** None.

**Decision needed.** Adopt.

### r29 — Configuration arms and a reporting rule (new §13.3; §14.7)

**Problem.** The confirmatory run uses one model, one wording of the codebook and one set of parameters. §13.1 treats the second model as a possible replacement, and §14.7 lists a second-model replication as "a desirable extension, not part of v1." The research on this practice says a single configuration is the weak point.

**Evidence.** Baumann et al. (2025) re-ran 37 annotation tasks from 21 published studies with 18 models and tested 2,361 hypotheses of the same shape as H1–H3 (a two-group difference in a model-coded label).
- Conclusions were wrong for roughly 31% of hypotheses with the most capable models and for about half with small ones.
- Error rates approached 70% for results close to p = 0.05.
- Careful prompt design explained under 1% of the variance in risk, yet a few reworded prompts were enough to manufacture significance for nearly any hypothesis.
- Their recommendations: pre-register every configuration choice, report results from all pre-registered configurations, never rest a test on one configuration.

Barrie, Palaiologou & Törnberg supply the stability measure used in (c) below. Transfer is by analogy: Baumann et al. used short texts, single labels and temperature 0.

**Proposed text.**

> **13.3 Configuration arms** (pre-registered; all reported).
>
> (a) *Primary.* The pinned scorer, the frozen codebook, three runs, item-level majority (§10).
>
> (b) *Second-model arm.* The model not chosen under §13.1 scores the full confirmatory sample under the same protocol.
>
> (c) *Paraphrase arm.* On a seeded subsample of 20 authors, the primary scorer is run with three paraphrased codebooks in which the item definitions of §4–§6 are reworded without change of meaning. Paraphrases are written and checked for equivalence before freeze, and archived. Reported: agreement across paraphrases (Krippendorff's α, after Barrie et al.), overall and by group, and the three composites under each paraphrase.
>
> (d) *Other-developer arm (optional).* A model from a different developer scores the subsample in (c). This replaces "a desirable extension, not part of v1" in §14.7.
>
> (e) *Reporting.* One table gives every arm's estimate, interval and p-value for H1–H3. A primary result is described as *robust to configuration* if its direction holds in every arm and its interval excludes zero in both (a) and (b). Otherwise it is described as *configuration-sensitive*. A primary p-value between 0.01 and 0.10 is described as *unresolved*, whatever the arms show, and the spread across arms is displayed.

**Cost.** The v2 harness README puts the pilot's crossed run at about $5 for Fable and $2.50 for Opus (two papers, three runs each, claim list supplied). Scaled to the illustrative 150–180 papers, a full arm is on the order of $200–450, more if confirmatory papers are longer or extraction adds output. This is my scaling of the README's figures, not a quote.

**Decision needed.** Full sample or subsample for (b); the 0.01–0.10 band; whether to run (d).

### r30 — Single-pass versus item-isolated scoring (new §12.4)

**Problem.** In the harness, one message carries the codebook, the paper, the claim list and every E and P item, so each item is scored with the reasoning for every other item in view. Raters who form an overall impression tend to let it color individual items (the halo effect). If that happens here it is a channel from stance to every item at once, and it inflates the correlation among the three composites.

**Evidence.** Dycke & Gurevych (2026) tested a single-pass, whole-paper output. Pita (2026, preprint; I have read only the abstract) argues for decomposing a construct into components that are each tested against extracted evidence and combined by an explicit rule. The codebook already decomposes the construct. This probe tests whether scoring the components together matters.

**Proposed text.**

> **12.4 Single-pass versus item-isolated scoring.** Before freeze, on the pilot set. The §10 protocol scores every item for a paper in one context. Each judgment item is additionally scored in a call of its own that contains the item's definition and the paper text and no other item's result. Reported, by group: agreement between single-pass and isolated scores per item, and inter-item correlations under each mode. If the two modes differ by more than the run-to-run rate on any item family, the scoring architecture (single-pass, isolated, or isolated for that family) is decided before freeze and the reason logged in §16.

**Limits.** An isolated call still sees the whole paper. This measures contamination between items, not the effect of stance. Stance effects are r19 and r22.

**Cost.** Extra calls on a handful of pilot papers.

**Decision needed.** Run it or not.

---

## 6. Interactions with pending items

| Pending | Interaction |
|---|---|
| r9 (aggregation weighting) | Fixes the statistic that r21's weights must match. Settle r9 first. |
| r10 (first-author-only) | Fixes which papers a calibration author contributes (r19a). |
| r11–r12 (census, seeded draws, screening) | r27 reuses the seeded-draw machinery. r26 draws pilots from outside the frame so the census is not reduced. |
| r17 (P5 in the composite) | Changes PRAC as used in r19(e) and r21. |
| r18 (meta-discourse versus actor-conduct claims) | Changes extraction as coded in r19(c). Settle before coders are trained. |
| r7, r8 | None. |

## 7. Already covered in v0.2 — no amendment proposed

- E1 for assessment-aligned papers (r6, §5). The rule's detail is open (r25), the principle is in place.
- Model and version pinned at freeze (§10).
- Freeze before any confirmatory paper is sampled or scored; post-freeze amendments logged with sensitivity analysis (§15).
- Asymmetric exposure disclosed (§14.1), and the harness prompt tells the scorer not to import outside knowledge.
- Single-scorer design disclosed (§14.7).
- Venue endogeneity (§2.3, §14.3) and visibility conditioning on the contrarian list (§14.4, §2.5).
- Pilot papers excluded from the confirmatory sample (§2.4); scorer errors logged with their direction (Exhibit 1 erratum).

## 8. Sign-off

| ID | Adopt / modify / decline | Notes |
|---|---|---|
| r19 | | coders: ; m: |
| r20 | | second verifier: |
| r21 | | (d) wording rule, or co-primary: |
| r22 | | counts: ; margin: |
| r23 | | Exhibit 3 annotation: |
| r24 | | |
| r25 | | E1 rule (a/b/c): ; E4 (a/b/c): ; E1b: ; name: |
| r26 | | pilot: ; B′: ; outreach: |
| r27 | | second frame size: |
| r28 | | |
| r29 | | (b) full or subsample: ; band: ; (d): |
| r30 | | |

## 9. Sources

Full references and reading limits are in `scorer-validity-explainer_draft1.md` §6–§7. In brief:

- Ashwin, Chhabra & Rao (2025), *Sociological Methods & Research*. https://doi.org/10.1177/00491241251338246 (read in the 2023 arXiv version, arXiv:2309.17147)
- Barrie, Palaiologou & Törnberg, "Prompt Stability Scoring for Text Annotation with Large Language Models." arXiv:2407.02039
- Baumann et al. (2025), "Large Language Model Hacking." arXiv:2509.08825
- Benestad et al. (2016), *Theoretical and Applied Climatology* 126:699–703
- Coan, Boussalis, Cook & Nanko (2021), *Scientific Reports* 11:22320
- Dycke & Gurevych (2026), *Transactions of the ACL* 14:465–488. https://aclanthology.org/2026.tacl-1.22/
- Egami, Hinck, Stewart & Wei (2023), NeurIPS 36. arXiv:2306.04746
- Gligorić et al. (2025), NAACL. https://aclanthology.org/2025.naacl-long.179/
- Halterman & Keith, "Codebook LLMs." arXiv:2407.10747
- Kim et al. (2026), "All Public Voices Are Equal, But Are Some More Equal Than Others to LLMs?" arXiv:2604.17247
- Ollion, Shen, Macanovic & Chatelain (2024), *Nature Machine Intelligence* 6:4–5
- Ornstein, Blasingame & Truscott (2025), *Political Science Research and Methods* 13:264–281
- Petersen, Vincent & Westerling (2019), *Nature Communications* 10:3502
- Pita (2026), "Correct codes for the wrong reasons?" arXiv:2606.28574
