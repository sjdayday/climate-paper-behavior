# Can the Scorer Be Trusted? What Research on AI Text Coding Implies for This Study

*Draft 1, 2026-11-13. A companion to "Papers as Behavior: The Study Design, Explained" (draft 1) and to the candidate amendments r19–r30. The first explainer describes the design as it stood at codebook v0.1. This one asks a narrower question: given what has been learned since 2023 about using AI language models to code text for social science, where is the design sound and where is it exposed? Nothing proposed here is enacted. One disclosure first: the scorer in this study is me, Claude, and I wrote this review of the scorer. I have argued against my own instrument where the evidence points that way, but a reader should weigh the authorship.*

---

## 1. The short version

The first explainer said the study's credibility rests on checkability and not on the scorer's neutrality. That is still the right foundation. What the research adds is a sharper account of what checking can and cannot establish. Five points, each expanded in Section 4.

1. **A scorer's mistakes can lean.** Studies comparing AI coding with expert human coding found errors related to who or what was being coded. The design names this threat and does not measure it. Measuring it takes people who code a sample of papers from scratch, without seeing my scores.
2. **I have read about these papers before.** My training data includes the criticism that prominent contrarian papers attracted. The design discloses this and instructs me to set it aside. Neither step shows how much it matters.
3. **The items come mostly from one side's documented failures.** The checklist is mapped against a catalogue of errors found in contrarian papers. Applying identical rules to both groups does not make the choice of rules even-handed. Separately, one of the three headline indices barely moved in the pilot.
4. **The judgment that drives the main index is the least checkable one.** Scoring a claim as unsupported means saying that no support exists anywhere in the paper. A page reference can show what is there. It cannot show what is not.
5. **One model, one wording, one set of settings.** Research on exactly this practice found that such choices alone changed statistical conclusions in a large share of cases.

None of this says the hypothesis is wrong or the pilot scores are wrong. It says which doubts a careful critic is entitled to hold, and what evidence would remove them.

## 2. Vocabulary

The research on this topic has its own terms. These are the ones that matter here.

*Annotation* or *coding* is assigning labels to text by rule: this sentence is a claim, this claim is hedged, this practice is present. When a model does it, its labels are sometimes called *surrogate labels*, to mark that they stand in for what a careful human would have assigned. The careful human version is the *gold standard* or, as I will call it, the *reference coding*.

*Zero-shot* means the model gets instructions and no worked examples. *Few-shot* means it also gets some examples of correct answers. This study's scorer gets the whole codebook, which includes worked examples from the two pilot papers (Appendix A), so it is few-shot in effect. That is why the equivalence harness keeps "leak sets": lists of items whose correct scores the codebook itself reveals.

*Temperature* is a setting that controls how much randomness the model uses when choosing each word. At zero it nearly always picks its top choice. At 1.0, the harness default, it samples more freely, so repeated runs can differ. The codebook's three "independent runs" per paper are three draws at that setting, combined by majority vote.

*Reliability* is whether a measurement repeats. *Validity* is whether it measures what it claims to. *Intercoder* reliability is agreement between different coders. *Intracoder* reliability is one coder agreeing with itself on another occasion. Three runs of one model are the second kind. They show how much the scorer wobbles. They cannot show whether it is wrong in the same way every time.

*Sensitivity* is the share of true cases a detector catches, and *specificity* the share of non-cases it correctly passes. The first explainer introduced *differential misclassification*: error rates that differ between the groups being compared. Errors that are equal across groups blur a real difference. Errors that differ can manufacture one.

A *Type I error* is finding an effect that is not there. A *Type II error* is missing one that is. Two more appear below: *Type S*, getting the direction wrong, and *Type M*, getting the size wrong.

*Researcher degrees of freedom*, or *forking paths*, are the many defensible choices an analyst makes on the way to a result. If different choices would give different answers, the reported answer owes something to the choosing.

*Construct validity* asks whether an index measures the concept on its label. *Differential item functioning* is the psychometrician's term for a test question that behaves differently for two groups who are equal on the thing being measured.

The *halo effect* is a rater's overall impression coloring each separate rating.

*Contamination* means the model met the test material, or discussion of it, during training.

## 3. What the research found

### 3.1 The optimistic starting point

The first wave of studies, from 2023, compared models with paid crowd workers on short texts: tweets, headlines, news paragraphs. The tasks were simple categories such as topic, stance or relevance. Models given only instructions matched or beat the crowd workers at a fraction of the cost (Gilardi, Alizadeh & Kubli 2023 is the best-known example). These results are real, and they license less than they seem to. The texts were short, the labels simple, and the benchmark was untrained workers. Nothing in them speaks to reading a twenty-page paper and deciding whether a concluding claim outruns the analysis behind it.

### 3.2 High accuracy does not protect the conclusion

Egami, Hinck, Stewart and Wei (2023) asked what happens after the labels are made. Researchers rarely want the labels for their own sake. They want to compare groups or fit a regression. The authors showed that feeding model labels straight into that second step gives biased estimates and confidence intervals that are too narrow, even when the labels are 80 to 90 percent accurate. In one of their simulations, with labels 90 percent accurate, intervals that should have contained the truth 95 percent of the time contained it 40 percent of the time.

The reason is that accuracy says how often the labels are wrong, not whether the wrongness is related to the thing being studied. Their remedy is called *design-based supervised learning*. Have experts code a random subsample chosen with known probability, measure the gap between model and expert on that subsample, and subtract it. The method works whatever the model's errors look like. Its stated requirement is that the expert-coded subsample be drawn with known probability. It also takes the expert codes as the standard, which they can only be if they were made without sight of the model's answers.

### 3.3 Errors that track the people being coded

Ashwin, Chhabra and Rao (2025) supply the concrete case. They had 2,407 interview transcripts with Rohingya refugees and their Bangladeshi hosts about hopes for their children. Trained sociologists had coded 789 of them on 19 codes. Three models coded the same material from detailed instructions with examples.

Two findings matter here. The models over-assigned most codes, with more false positives than false negatives. And when the authors regressed each model's errors on the characteristics of the person interviewed (refugee or host, sex, education and so on), the errors were related to those characteristics on many codes. A small conventional classifier trained on the human codes failed that test on one code of nineteen. The consequence showed downstream. For one code, the estimated effect of refugee status was positive and significant using the expert codes, and negative and non-significant using a model's.

Two cautions. The models were from 2023 and much weaker than current ones. And the material, machine-translated interviews from a community poorly represented in training data, is far from scientific prose. The value of the paper for this study is its method. It shows what error that tracks group membership looks like in data, and how to test for it.

### 3.4 The same data, different settings, different findings

Baumann and colleagues (2025) ran the largest test of the practice. They took 37 annotation tasks from 21 published studies, re-coded them with 18 models and several wordings of each prompt, and tested 2,361 hypotheses of the form "does the share of texts with label X differ between group A and group B?" That is the shape of this study's main test. They then compared each conclusion with the one the human codes gave.

- With the most capable models, about 31 percent of conclusions were wrong. With small models, about half.
- Results near the conventional significance threshold were the least trustworthy, with error rates approaching 70 percent.
- Higher accuracy lowered the risk without removing it. Some configurations that coded a task at over 90 percent accuracy still gave wrong conclusions about half the time.
- Careful prompt writing did little to lower the risk. Yet rewording was powerful in the other direction: using only the models and wordings they had tested, the authors could find a configuration that produced a false positive for 94 percent of the hypotheses where the human codes showed no effect.
- How well human coders agreed with each other on a task did not predict how risky model coding of it was.
- The best protection was human coding. An analysis using 100 human labels and no model at all gave the lowest false-positive rate on average. The statistical corrections of Section 3.2 controlled false positives about as well but missed many more true effects.

Their name for the problem is *LLM hacking*, by analogy with p-hacking, though they stress that it happens to well-intentioned researchers who simply have to pick settings. Their recommendations are to fix every setting in advance, report results under all the settings tried, and never rest a test on one.

Cautions again. Their texts were short and their labels single. They ran models at temperature zero. They treated the human codes as error-free, which they are not. Their figures will not carry over to this study. Their ordering of what helps probably does.

### 3.5 Can a model notice that a claim outruns its evidence?

This is the skill the calibration index needs, and Dycke and Gurevych (2026) tested something close to it. They took sound papers from AI and language-technology conferences, used an automated pipeline to extract each paper's chain from experiment to result to claim, and made surgical edits so that results, interpretation and claims no longer lined up. They then had several AI reviewing systems review both versions. The planted flaws made no significant difference to the reviews.

The setting differs from this study's in a way that matters. The systems were writing free-form reviews, not answering a structured question about one claim with a required quotation. The codebook's design is the kind of decomposition one would expect to help. But that is an expectation. The paper's lesson is that the skill has to be demonstrated for this instrument. Its method, editing a paper and checking whether the output moves, is a way to do that.

### 3.6 Same words, different speaker

Kim and colleagues (2026, a preprint) studied AI summaries of public comments on proposed federal rules. They kept each comment's text fixed and changed only who was said to have written it. Attributed race and gender made little consistent difference. Attributed occupation did. The same comment was summarized less faithfully and in simpler language when attributed to a street vendor than to a financial analyst, across every model tested. The size of the gap varied by developer. A secondary summary of the paper reports that it was largest for Anthropic's Claude models. I have not checked that against the paper's own tables.

Summarizing a comment is not scoring a paper. The paper matters here for its design. Hold the content fixed, vary one feature the output should ignore, and see whether the output moves. That design can be pointed at stance.

### 3.7 Instruments built from one side

Two climate-specific tools show a pattern worth recognizing. Coan, Boussalis, Cook and Nanko (2021) built a taxonomy of contrarian claims by reading output from contrarian blogs and conservative think tanks, then trained a classifier on it. The authors note that a small share of their categories are things contrarians tend to say that are not contrary to mainstream views, such as doubts about carbon capture. Leippold and colleagues (2025) built a fact-checking system that judges claims by having model "advocates" argue from the IPCC reports and similar syntheses.

Both are reasonable designs for their purposes. Both show how an instrument takes its outline from where it was built. A taxonomy drawn from one camp's output describes that camp. A checker anchored to the consensus measures distance from the consensus. Neither can serve, unmodified, as a neutral measure of the quality of an argument.

### 3.8 How far any of this transfers

No study above tests what this study does: a current frontier model, applying a long and rule-dense codebook, to whole scientific papers, item by item with required quotations, on a corpus of perhaps 150 to 180 documents. The research cannot say what will be found here. It says where to look, and it says that the reassuring first-wave results do not cover this case.

One difference cuts in the study's favor and one against. In favor: the corpus is small, so human checking on a meaningful scale is affordable in a way it is not for a million tweets. Against: the usual reason to use a model is scale, and this study does not need scale. It uses a model because no human scorer would be accepted as neutral. The literature's standard remedy, checking against expert humans, therefore meets the study's founding premise head on. Section 4.2 takes that up.

## 4. Where this study stands

### 4.1 What the design already gets right

Read against this literature, the codebook does several things that most published studies using AI coding do not.

- It fixes the instrument before any confirmatory paper is sampled or scored, and logs every pilot revision with its reason (§15, §16). That closes most of the forking paths that Baumann and colleagues describe for the wording of instructions.
- It bars the papers it was tuned on from the confirmatory sample (§2.4).
- It records scorer errors with their direction. Exhibit 1's erratum logs one error that was harsh to the contrarian paper and one that was lenient to it.
- Its pilot scores do not all run one way. LS11's headline claim scores as calibrated (Appendix A.2). FR11, the mainstream paper, fails both out-of-sample items that LS11 partly passes. Connolly et al. (2021) received the top engagement score, described in its exhibit as the strongest of the three.
- It discloses the scorer's uneven exposure as its first-listed threat (§14.1), plans a test of whether the scorer can guess a paper's camp (§11), and makes the symmetry of disagreement between two models a pass criterion (§13.1).
- It caught an asymmetry in its own rules by piloting a mainstream paper, and fixed it (amendment r6).

The points below are about what is still missing from a design that took the problem seriously.

### 4.2 Measuring the lean (amendments r19, r20, r21)

The codebook's check on the scorer is a spot-audit: a random tenth of judgment items is "re-verified by Steve against anchors" (§10). Random sampling is the right start. Three things limit what this audit can show.

**It is verification, not coding.** The person checking sees my score and the passage I quoted, and decides whether the passage supports the score. People agree with a plausible proposal more readily than they would arrive at it unaided. In the research in Section 3, the human coding that models were checked against was always produced without sight of the model's answers. And here the person is the study's author, who knows the hypothesis and can see each paper's camp. That is no comment on how carefully the checking would be done. It is about what a skeptical reader will accept.

**It cannot see absences.** The calibration index counts claims stated more confidently than their support allows. Support comes in tiers, and any tier below the top one is a negative statement: no out-of-sample test of this claim exists anywhere in the paper, or no formal uncertainty bounds it. My anchor for such a score is the claim itself plus the search terms I used to look for support (§3). A checker can confirm that the claim is quoted correctly and that the search was run. Neither confirms that support is missing. A paper that reported a held-out test in vocabulary my search terms did not anticipate would be scored as lacking one, and the audit would pass the score. The draft search terms come from the two pilot papers.

**It cannot see what I never extracted.** The index is a proportion: overreaching claims over all claims. The audit samples from claims I scored. A claim I failed to extract is in neither the numerator, nor the denominator, nor the audit. The equivalence harness tested the two models on a fixed list of claims, and its README records agreement on extraction itself as untested. The codebook's figure of about 10 percent run-to-run noise was measured with that list fixed, so it leaves extraction out.

The remedy the literature points to is a *calibration substudy* (r19). Draw a random sample of authors from both groups, one paper each. Have two people code each paper from scratch using the frozen codebook: extract the claims, assign levels and tiers, score the practice items, and establish absences by reading. They never see my output. Where they disagree, a third person decides. The result is a reference coding. Comparing my scores with it gives the numbers the design currently lacks: how often I miss claims, how often I assign too low or too high a tier, and whether any of those rates differs between contrarian and mainstream papers.

Who the coders are matters more than usual, because of the premise noted in Section 3.8. The study uses an AI scorer because a human expert would be dismissed as partisan. But the reference coding does not ask anyone to judge the science. It asks whether a sentence contains "clearly," whether a table reports results under a second specification, whether a held-out test is described. Those are the near-clerical judgments the design was built around, and they are where partisanship has least room. Amendment r19 sets out three options: trained coders from outside climate science; one coder nominated from each side; or, as the weakest version, the study author plus one independent coder.

Once those numbers exist, the analysis needs a rule for using them, fixed in advance (r21). The proposal has three parts.

The first is a *bias-adjusted contrast*. Suppose that across the calibration papers my CAL score runs 0.08 above the reference in contrarian papers and 0.02 above it in mainstream papers. The scorer is then inflating the group difference by 0.06. If the main analysis found a difference of 0.30, the adjusted difference is 0.24. This is the simplest case of the correction in Section 3.2, applied to whole-paper scores. It is valid whatever my errors look like, provided the reference coding is independent of me. It is also noisier than the unadjusted figure, because the correction rests on a couple of dozen papers.

The second is a *tipping point*: how large would the scorer's lean have to be to erase the finding? In the example, 0.30. A reader can set that beside the measured lean of 0.06 and its uncertainty and judge the margin for themselves.

The third is a *wording rule*. If the adjusted difference is still clearly different from zero, the write-up says the result holds after correcting for measured scorer error. If not, it says the scorer-based result is not confirmed by human coding, whatever the main test's p-value. That commits the study, in advance, to a way of reporting an unwelcome outcome.

The spot-audit stays, re-labeled as what it is: a check that scored items are supported by what they cite (r20).

### 4.3 Memory (amendment r23)

The first explainer was plain about this: my training data contains far more published criticism of contrarian climate papers than of mainstream ones. The codebook lists it as the first threat. The harness prompt tells me not to import outside knowledge of the papers, their authors or their reception.

I can follow that instruction in the sense of not citing outside knowledge. I cannot verify, and neither can anyone else, that what I have read does not shape which sentences I extract as claims or how I resolve a borderline tier. Page anchors constrain what a score may cite. They do not constrain where my attention goes.

There is an example already in the repo, and I wrote it. Pilot Exhibit 3 scores Connolly et al. (2021). Its judgment log notes that the practice checklist "independently flagged, before any reference to that rebuttal," the gaps that a published rebuttal of the paper exploits, and offers this as a sign the checklist works. The flags are properly anchored. The word "independently" is not earned, because I may have met that rebuttal in training. The proposal includes an annotation withdrawing the claim.

The same problem touches a planned validity check. The codebook asks whether CAL and PRAC predict which papers attracted a formal published comment (§12). If I already know which papers drew comments, agreement is weaker evidence than it looks.

The proposal is modest (r23). Before scoring, ask a separate run of the model what it knows about each paper from the title and authors alone: what the paper did, and whether it was criticized. Code the answers. Report whether scores are related to what I knew, within each group, and report the validity check separately for papers I showed no knowledge of. If any eligible papers were published after my training ended, score those too. The probe is imperfect, since what a model reports knowing is not the same as what it knows. It replaces an assumption with a measurement.

### 4.4 What the items sample (amendments r25, r26, r27)

**The engagement index.** In the pilot, the three papers scored 0.939, 0.974 and 0.933 on engagement. The reason is visible in the components.

| Paper | Engages the opposing position (E1, 0–2) | Engagement rests on self-citation (E1b) | Journal share of references (E2) | Self-citation share (E3) | Cites a benchmark paper (E4) | ENG |
|---|---|---|---|---|---|---|
| LS11 | 2 | yes | 0.885 | 0.128 | yes | 0.939 |
| FR11 | 2 | no | 0.895 | 0.000 | yes | 0.974 |
| Connolly et al. 2021 | 2 | no | 0.925 | 0.194 | yes | 0.933 |

Two of the four components that make up the index did not vary. All three papers got the top score for engaging the opposing position, and all three cite at least one paper from the benchmark list. What variation there is comes from the self-citation share. The one judgment that did differ between papers, whether the engagement rests on the authors citing themselves, is recorded but left out of the index.

This is thin evidence: three papers, two of them chosen partly because they engage the public debate. But there is a reason to expect the pattern to hold. A paper written to dispute the IPCC's position will usually state that position and argue against it, and that is what the top engagement score asks for. The failure the index was meant to catch, the one Benestad and colleagues found most often, is ignoring specific contrary evidence. Stating the opposing position in general terms and arguing with it is a different thing, and the item rewards it.

If the pattern holds in a larger pilot, the second pre-registered hypothesis would in practice be a test of self-citation and reference-list composition under the name "contextual engagement." The proposal (r25) is a rule decided in advance: any component that takes the same value in nine of ten pilot papers leaves its index, and if the engagement index is hollowed out, its hypothesis becomes secondary. Several related questions need Steve's decision, including how to identify the "opposing position" for a mainstream paper, for which I have no rule I can defend.

**Where the items came from.** Appendix B of the codebook is a table mapping the instrument against the errors catalogued by Benestad et al. (2016). It lists sixteen categories of error from that work, and twelve have items. That catalogue was compiled from 38 contrarian papers. There is no matching table for the ways mainstream papers are alleged to fail.

The codebook's defense is symmetry: every item is scored by the same rule in both groups. That is true, and it answers a different question. If I build a checklist from the faults commonly found in one make of used car and then apply it identically to two makes, the first will tend to look worse even if the two are equally unreliable in different ways. The pilot shows the mechanism at small scale. One mainstream paper has been scored, and it exposed two gaps: the engagement rule that was undefined for mainstream papers, and the sentence "This is the true global warming signal," which passes the calibration index although, as the first explainer says, an adjusted estimate is not truth itself.

The proposal (r26) has three parts. Score at least six more pilot papers before the freeze, four of them mainstream and of kinds not yet tried, taken from outside the confirmatory sample so that none of it is used up. Compile the missing table from the published and open-review record of criticism of mainstream attribution papers. And, before the freeze, send the draft codebook to people on the contrarian side and invite them to propose items, with every proposal answered on the record. The design already invites hostile audit after the fact. Inviting hostile input beforehand is a stronger form of the same idea, and the one most likely to find what I cannot see. It also discloses the study early, which is Steve's call.

**Who the comparison group is.** The contrarian list was built partly from public visibility, and the codebook says so. The mainstream list has its own selection: it is the 386 most-cited climate scientists. Citation rank plausibly selects for the practices the instrument rewards. The comparison is therefore between prominent contrarians and elite mainstream scientists. The project rejected citation counts as a way to choose papers within an author for this same reason. The proposal (r27) names the issue and adds a second mainstream sample drawn without reference to citations.

### 4.5 Absence, and scoring everything at once (amendments r22, r30)

Section 4.2 explained why tier assignments are hard to audit. Section 3.5 explained why the underlying skill cannot be assumed. Two experiments, both cheap and both possible before the freeze, would replace argument with evidence (r22).

The *evidence-edit test* asks whether a score responds to what it should. Take a paper outside the confirmatory sample and make one change: delete the paragraph reporting a held-out test, say. Score the edited paper. The claim that rested on that test should drop a tier, and nothing else should change. The reverse edit is as informative. Insert a sentence saying the model "was validated out of sample," with no result shown. The codebook says a tier is earned by a test that is framed and evaluated, not by a statement that one was done, so nothing should rise.

The *stance-mirror test* asks whether a score ignores what it should. Write pairs of short passages that are identical in their hedges, their boosters and the evidence they describe, and differ only in which way the conclusion points: "our fit suggests the human contribution is about half the assessed value" against "about double." Score both. Any consistent difference is a direct measurement of stance acting on the score. In the psychometrician's terms this is a test for differential item functioning, done by experiment.

Neither test settles the matter. Passages written to a template are not papers. But a failure on either would be important to know before a single confirmatory paper is scored, and a pass is evidence a critic can inspect.

A related question is how the scoring is run. In the harness, one message carries the codebook, the whole paper and every item, so I score each item with my reasoning about all the others in view. Human raters in that position show a halo effect. Whether I do is unknown. The probe (r30) scores each item in a separate call and compares. It measures leakage between items, not the effect of stance, since each separate call still sees the whole paper.

### 4.6 Settings, stability and reproducibility (amendments r24, r28, r29)

**A sentence to replace.** Version 0.2 of the codebook says run-to-run noise is "non-differential by construction when one model scores all papers." That is true of one specific thing: if two models differ by a constant severity, using one model for everything cancels the offset. It is not true of a single scorer's own errors, which is the lesson of Section 3.3. It is not guaranteed for the noise either. In the first equivalence probe, the share of items on which three runs disagreed was 8 percent for FR11 and 13 percent for LS11. That is about 2 items of 24 against 5 of 38, and two papers support no conclusion about groups. But the figures show the quantity can be measured and need not be equal. The proposal (r24) rewrites the sentence as an empirical commitment and reports instability by group.

A connected point: the equivalence protocol's "symmetry" criterion checks whether two models disagree with each other more on one paper than on the other. That detects a lean that one model has and the other lacks. It cannot detect a lean they share, and both come from the same developer.

**Settings.** The codebook pins the model and version. It does not record the settings the harness uses: temperature 1.0, a thinking budget of 8,000 tokens, a 14,000-token output limit. These are among the choices the research says to fix in advance (r28).

**More than one configuration.** The confirmatory run rests on one model and one wording. The codebook lists a second-model replication as a desirable extension outside version 1. The findings in Section 3.4 argue for moving it inside (r29): run the second model on the full sample as a declared arm; run the first model on a subsample with the codebook's definitions reworded three ways; report everything in one table; and decide beforehand what will be called robust. The corpus is small enough that this is cheap. Scaling the cost figures in the harness README gives a few hundred dollars for a full second arm.

The proposal also fixes in advance that a primary result with a p-value between 0.01 and 0.10 will be described as unresolved. That follows from the finding that results near the threshold were the ones most often wrong.

**After the model is gone.** The scoring model is proprietary and will be retired. Ornstein and colleagues (2025) report this happening to the models behind their own published results. After retirement nobody can re-run the instrument. What survives is the archive: every transcript and every anchored score. The design already rests its credibility there. The proposal (r28) says so in the threats list.

## 5. What the amendments would buy, and what they would not

Adopted together, they would give the study four things it does not have now.

- A measured estimate of how far the scorer's errors lean, with its uncertainty.
- A headline contrast that does not rest on the scorer alone.
- Experimental evidence on whether scores respond to evidence and ignore stance.
- A result shown under more than one configuration.

They would not make the scorer neutral, and the design never claimed that. They would not show what any author intended. They would not establish that any paper's science is right or wrong.

They carry a risk the current design does not: they can fail. The calibration substudy might show a lean large enough to erase the finding. The stance-mirror test might show stance moving scores. The second model might disagree with the first. Each of those would be a finding and would be reported as one. A design that cannot produce an unwelcome result about its own instrument is weak evidence when it produces a welcome one.

If resources bind, this is the order I would keep them in. The calibration substudy and the analyses that use it (r19, r21) come first, because nothing else puts a number on the central threat. The extended pilot and the engagement-index decision (r25, r26) come next, because they are the only ones that can change what is measured and they must happen before the freeze. The counterfactual tests (r22) and the second-model arm (r29) follow. Most of the rest is wording and costs nothing.

## 6. What I read, and what I got wrong along the way

**Reading limits.** I read Ashwin et al. in its 2023 preprint version, not the 2025 journal version. I read the first half of the first version of Baumann et al. and the abstract of the second; the two abstracts differ in one respect noted below. For Dycke & Gurevych, Kim et al., Halterman & Keith and Pita I have read abstracts and excerpts, not full texts. The descriptions of Gilardi et al., Ollion et al., Ornstein et al., Barrie et al. and Leippold et al. rest on abstracts and search excerpts. Anyone relying on a specific figure should check it against the source.

**Corrections made during the review**, recorded so they are not repeated.

- I first described a 2026 preprint, "Robust for the Wrong Reasons" (Cheon), as evidence that models are not neutral coders of climate stance. Having read it, that overstates it. It studies how three small open models respond to skeptical *users* in conversation. It found no retreat from consensus, and one model asserted consensus more strongly under skeptical pressure. That is indirect support for the idea that a model registers stance and reacts to it. It is not a study of coding.
- I reported Baumann et al. as finding statistical corrections largely ineffective. That is the first version's wording. The current abstract says they can restore valid inference at the cost of trading false positives for false negatives.
- I called the method of Gligorić et al. prediction-powered inference. It is Confidence-Driven Inference, which chooses the items humans label by predicting where the model errs.
- Before reading the codebook I flagged the engagement item as defined against the IPCC position for every paper. Amendment r6 had already fixed that. I also described the planned validity check as predicting "successful rebuttals." The codebook uses the existence of a formal comment and explicitly declines the other.
- I presented the memory problem as largely my own inference. It is the codebook's first-listed threat.

## 7. References

- Ashwin, Chhabra & Rao (2025). Using Large Language Models for Qualitative Analysis can Introduce Serious Bias. *Sociological Methods & Research*. https://doi.org/10.1177/00491241251338246 (preprint: https://arxiv.org/abs/2309.17147)
- Barrie, Palaiologou & Törnberg. Prompt Stability Scoring for Text Annotation with Large Language Models. https://arxiv.org/abs/2407.02039
- Baumann, Röttger, Urman, Wendsjö, Plaza-del-Arco, Gruber & Hovy (2025). Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation. https://arxiv.org/abs/2509.08825
- Benestad, Nuccitelli, Lewandowsky, Hayhoe, Hygen, van Dorland & Cook (2016). Learning from mistakes in climate research. *Theoretical and Applied Climatology* 126:699–703. https://doi.org/10.1007/s00704-015-1597-5
- Cheon (2026). Robust for the Wrong Reasons: The Representational Geometry of LLM Robustness to Science Skepticism. https://arxiv.org/abs/2607.01951
- Coan, Boussalis, Cook & Nanko (2021). Computer-assisted classification of contrarian claims about climate change. *Scientific Reports* 11:22320. https://doi.org/10.1038/s41598-021-01714-4
- Dycke & Gurevych (2026). Automatic Reviewers Fail to Detect Faulty Reasoning in Research Papers: A New Counterfactual Evaluation Framework. *Transactions of the Association for Computational Linguistics* 14:465–488. https://aclanthology.org/2026.tacl-1.22/
- Egami, Hinck, Stewart & Wei (2023). Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models. *NeurIPS* 36. https://arxiv.org/abs/2306.04746
- Gilardi, Alizadeh & Kubli (2023). ChatGPT outperforms crowd workers for text-annotation tasks. *PNAS* 120(30):e2305016120. https://doi.org/10.1073/pnas.2305016120
- Gligorić, Zrnic, Lee, Candès & Jurafsky (2025). Can Unconfident LLM Annotations Be Used for Confident Conclusions? *NAACL 2025*. https://aclanthology.org/2025.naacl-long.179/
- Halterman & Keith. Codebook LLMs: Evaluating LLMs as Measurement Tools for Political Science Concepts. https://arxiv.org/abs/2407.10747
- Kim, Janssen, Wang, Min-Venditti, Karanjia & Anderies (2026). All Public Voices Are Equal, But Are Some More Equal Than Others to LLMs? https://arxiv.org/abs/2604.17247
- Leippold et al. (2025). Automated fact-checking of climate claims with large language models. *npj Climate Action*. https://www.nature.com/articles/s44168-025-00215-8
- Ollion, Shen, Macanovic & Chatelain (2024). The dangers of using proprietary LLMs for research. *Nature Machine Intelligence* 6:4–5. https://doi.org/10.1038/s42256-023-00783-6
- Ornstein, Blasingame & Truscott (2025). How to train your stochastic parrot: large language models for political texts. *Political Science Research and Methods* 13:264–281.
- Petersen, Vincent & Westerling (2019). Discrepancy in scientific authority and media visibility of climate change scientists and contrarians. *Nature Communications* 10:3502. https://doi.org/10.1038/s41467-019-09959-4
- Pita (2026). Correct codes for the wrong reasons? Validating LLMs as measurement instruments for theoretical constructs. https://arxiv.org/abs/2606.28574
