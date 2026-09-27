# Pilot Exhibit 5: Public Communications of Connolly et al. (2021)

**Instrument.** Protocol v0.2 (draft), `sources/communication-behavior-protocol_v0.2.md`. Stage 1 counterparts are the claim IDs in `../scoring-exhibit-3_Connolly-etal-2021_v0.2.md` (A1–A4, C1–C15) plus anchored body passages.
**Corpus.** `public-communications-inventory-CN21.md`. Verbatim captures are in `sources/`.
**Scorer/run.** Claude, single run, 2026-09-26. Pilot convention: judgment log in place of three runs.
**Status.** Exploratory; CN21 is outside the sampling frame (Exhibit 3 header).

## 0. Bottom line

- **Drift was upward and concentrated on one claim type.** 27 of 34 claims matched a Stage 1 counterpart. Of those 27, **22 moved up**, 4 held level and 1 moved down (mean Δ = +0.96, against +0.58 for the LS11 author posts and +0.12 for FR11; Exhibit 4). Communication CAL is **0.676** (paper 0.263). The two recordings (§2.5–2.6, added 2026-09-27) run lower on CAL than the written items (0.50 against 0.75), but drift the same way. In speech, the range claims keep their dataset qualifier; the IPCC-conduct claims escalate, as they do in writing.
- **The paper's empirical core stayed calibrated.** Dataset dependence and the range of solar contributions were restated at T3 with O = 0 (CN-T5, CN-T6, OL-2). The overreach sat where the paper's own overreach was (Exhibit 3's "adversarial attribution" signature): claims about the **IPCC's conduct and intent**. In the paper these are L2 at T0 ("appears to have tried", "appear to have overlooked", "we argue … premature"). In public they became "only included 'low solar variability' datasets", "mostly missed or simply neglected", "it is clear that data sets are being selected…", and in Soon's words "blatant untruth" and "hide-and-seek game".
- **Two fidelity errors (PC-8).**
  - The launch release says "their results can be generalized for global temperatures". The paper says its analysis "was explicitly confined to the Northern Hemisphere", and that only its urbanization recommendation is relevant globally.
  - Soon says the paper "concludes that all these conclusions are not only premature but factually misleading and confusing". The paper says "premature" only.
- **Three dropped qualifiers (PC-7).** Among them, R. Connolly's interview line "you can show that all of the warming is caused by the sun" rests on one TSI estimate. The paper says that estimate "suggests that all of the warming trend (although this estimate ends in 1998) … can be explained". In the interview "suggests" becomes "show", "explained" becomes "caused", and the 1998 caveat is gone.
- **Qualification retained where the authors quote their own abstract.** The open letter reproduces the hedged abstract verbatim (PC-7 = 1) and describes the paper as "much more circumspect and cautious" than AR6. The same letter asks Climate Feedback to rate the Epoch Times article "Correct" and "Accurate". That article's paraphrase says the authors "show conclusively" that most or all warming may have nothing to do with man. This is endorsement of escalated secondary coverage, and it is proposed as exploratory item PC-10.
- **HC-L reading.** CN21 fits **two-stage escalation**, not substitution: a paper with moderate CAL and communications that escalate. It is also *selective*: the escalation falls on the claim type that already overreached in the paper.

## 1. Attribution rulings for this corpus

1. **CERES launch post.** CERES is the research center run by the lead authors (R. Connolly, Soon, M. Connolly), and the post is bylined "CERES team". Protocol v0.1 §3.3 admits only quoted text from press releases, a rule written with university press offices in mind. Proposed v0.2 rule (§3.3a): when a release is issued by an organization an in-scope author leads, and bylined collectively, the unquoted text is admissible as author text, flagged, with a sensitivity analysis excluding it. It is scored here with that flag (CN-T rows).
2. **Co-author quotes in the launch release** are author statements. Where a quote is not about the paper's analysis and the release gives no attribution, the claim is scored as **ambiguous attribution** per §4.2 and flagged (Willson).
3. **Epoch Times.** Only text inside quotation marks attributed to an author counts. Terms and title fragments in quotes, and a sentence the journalist quotes from the paper itself, are dropped.

## 2. Scored claims

Levels follow codebook §4.2 and tiers follow Stage 1; Δ is measured against the matched Stage 1 claim; "—" means no matched counterpart.

### 2.1 Launch release, CERES-team text (flagged §1.1)

| # | Claim (≤ 25 words) | Level | Counterpart (level) | Tier | O | Δ | Flags |
|---|---|---|---|---|---|---|---|
| CN-T1 | the IPCC "only considered a small subset of the published TSI datasets … this subset only included 'low solar variability' datasets" | L4 (only) | A4 "failed to adequately consider all the relevant estimates of TSI" (L2) | T1 | 2 | +2 | |
| CN-T2 | "As a result, the IPCC was premature in ruling out a substantial role for the Sun in recent climate change." | L3 | A4 (L2) | T1 | 1 | +1 | |
| CN-T3 | the IPCC "may have been premature in their conclusion that recent climate change is mostly caused by human greenhouse gas emissions" | L1 | A4 (L2) | T1 | 0 | −1 | same release as CN-T2 |
| CN-T4 | "their results can be generalized for global temperatures" | L3 | paper: "explicitly confined to the Northern Hemisphere" | T0 | 2 | — | **PC-8**; PC-7 = 0 |
| CN-T5 | "scientists come to opposite conclusions about the causes of recent climate change depending on which datasets they consider" | L3 | A3 (L2) | T3 | 0 | +1 | |
| CN-T6 | right-hand panels lead to "the exact opposite conclusion … mostly due to natural cycles, chiefly long-term changes in the energy emitted by the Sun" | L3 | A3 (L2) | T3 | 0 | +1 | |
| CN-T7 | "This implies that most, if not all, of the long-term temperature changes are due to natural factors." | L3 | body: single-combination fit "suggests" (L2) | T1 | 1 | +1 | |

### 2.2 Named co-author quotes in the launch release

| # | Author | Claim (≤ 25 words) | Level | Counterpart | Tier | O | Δ | Flags |
|---|---|---|---|---|---|---|---|---|
| Q-RC1 | R. Connolly | "I fear that by effectively only considering the datasets and studies that support their chosen narrative, the IPCC have seriously hampered scientific progress" | L2 (I fear) | C15 (L2) | T0 | 1 | 0 | |
| Q-RC2 | R. Connolly | "I am particularly disturbed by their inability to satisfactorily explain the rural temperature trends." | L3 | C11 (L2) | T1 | 1 | +1 | |
| Q-VH | Velasco Herrera | sun–climate connections "that the UN IPCC reports had mostly missed or simply neglected" | L3 | C5 "appear to have overlooked" (L2) | T0 | 2 | +1 | |
| Q-SC1 | Scafetta | the IPCC claim of a negligible solar effect "is only based on global circulation model predictions …" | L4 (only) | A4 (L2) | T1 | 2 | +2 | |
| Q-SC2 | Scafetta | "the natural component of climate change is minimized, while the anthropogenic one is maximized" | L3 | A4 (L2) | T1 | 1 | +1 | |
| Q-HU | Humlum | "This study clearly demonstrates the high importance of carefully looking into all aspects of all available data." | L4 (clearly) | A3 (L2) | T3 | 0 | +2 | |
| Q-WI1 | Willson | "scientific observations in recent decades have demonstrated that there is no 'climate change crisis'" | L4 | none | T0 | 3 | — | ambiguous attribution |
| Q-WI2 | Willson | "The Earth's climate is determined primarily by the radiation it receives from the Sun." | L3 | none | T0 | 2 | — | ambiguous attribution |
| Q-SO1 | Soon | "the Sun's role in recent climate change should never have been as systematically undermined as it was by the IPCC's reports" | L3 | C5 (L2) | T0 | 2 | +1 | |

Not scored: Henry (his own stellar data; program-level); Fedorov, Zhang and Yan (promotional evaluations of the paper); Elias (normative "must be considered"); Szarka (definition of climate change; extra-paper).

### 2.3 Epoch Times interview quotes (2021-08-16)

| # | Author | Claim (≤ 25 words) | Level | Counterpart | Tier | O | Δ | Flags |
|---|---|---|---|---|---|---|---|---|
| ET-RC1 | R. Connolly | "you can show that all of the warming is caused by the sun" | L3 | body §5 (Figure 16(b) discussion): one estimate "suggests that all of the warming trend (although this estimate ends in 1998)…" (L2) | T1 | 1 | +1 | PC-7 = 0 (1998 caveat; "explained" → "caused") |
| ET-RC2 | R. Connolly | "the IPCC seems to have decided to consider only those data sets and studies that support their chosen narrative" | L2 (seems) | C2 (L2) | T0 | 1 | 0 | |
| ET-RC3 | R. Connolly | "it is clear that data sets are being selected that support the IPCC view while data contradicting it have been excluded" | L4 (clear) | C2 (L2) | T1 | 2 | +2 | intent hedged ("difficult to say") in the same sentence |
| ET-RC4 | R. Connolly | "trying to force a premature consensus unfortunately hinders scientific progress—it is unhelpful and leads to an unjustified confidence in the conclusions" | L3 | C15 (L2) | T0 | 2 | +1 | |
| ET-SO2 | Soon | "our new and comprehensive research paper concludes that all these conclusions are not only premature but factually misleading and confusing" | L3 | C15 "premature" (L2) | T0 | 2 | — | **PC-8** |
| ET-SO3 | Soon | "Our scientific review shows that the changes in the Sun's irradiance are a plausible and important factor that can explain most of the observed changes" | L3 | A3 (L2) | T3 | 0 | +1 | PC-7 = 0 ("everything from no role…" dropped) |

Not scored (extra-paper or normative, logged): Soon's "mislead most of the unsuspecting public", "childish hide-and-seek game", "abuse of science by the IPCC"; Szarka on the 1992 definition of climate change.

### 2.4 Open letter (2021-09-10; R. Connolly, Soon, M. Connolly)

| # | Claim (≤ 25 words) | Level | Counterpart | Tier | O | Δ | Flags |
|---|---|---|---|---|---|---|---|
| OL-1 | quotes the abstract's hedged attribution sentence verbatim | — | A3–A4 | — | — | — | PC-7 = 1 (qualifier retained) |
| OL-2 | "plausible estimates for the solar contribution range from 0%-100% of the long-term warming since the mid-19th century!" | L3 | A3 (L2) | T3 | 0 | +1 | |
| OL-3 | IPCC's approach "appears to be to use 'expert judgement' to identify the most 'likely' perspective … and then … to dismiss those studies which dissent" | L2 | C2 (L2) | T0 | 1 | 0 | |
| — | asks that Climate Feedback's verdict on the Epoch Times article become "Correct" and "Accurate" | — | — | — | — | — | proposed PC-10 (endorsement of escalated coverage) |

### 2.5 Climate Discussion Nexus video, "Looking at the Sun" (2022-06-01; R. Connolly interviewed)

Source: YouTube auto-captions (ASR), `sources/transcripts/CN21_CDN_2022-06-01_rJIw7ulYaGk_asr-en.txt`. Only R. Connolly's three spoken passages are author text; the host's narration is not. Quotes are from the ASR text and still need a hand check against the audio (D4). Square brackets mark ASR corrections: the captions render ACRIM as "acronym" and "explain everything" (probably) as "explain aging".

| # | Claim (≤ 25 words) | Level | Counterpart | Tier | O | Δ | Flags |
|---|---|---|---|---|---|---|---|
| CDN-RC1 | PMOD "applied a series of adjustments … kind of got rid of that rise in solar activity in the 80s and 90s and replace it with a decline" [10:19] | L3 | body (ACRIM-gap review); no indexed claim | T2 | 0 | — | ASR |
| CDN-RC2 | "if the [ACRIM] composite is correct … some of the warming in the 80s and 90s could be due to the solar activity"; "if PMOD is correct … can't really explain any" [10:50–11:31] | L2 | A3 (L2) | T3 | 0 | 0 | PC-7 = 1 (conditional kept); ASR |
| CDN-RC3 | "we can explain … from nothing to almost all of the temperature changes … depending on whether [ACRIM] is correct or PMOD is correct" [17:23] | L3 | A3 (L2) | T3 | 0 | +1 | PC-7 = 1 (dataset dependence kept; the paper's 16-series range is compressed to two composites); ASR |

Not scored (extra-paper, PC-5, logged): "a lot of scientists … feel a lot of pressure to conform … their work to the IPCC … the IPCC has become a very dominant political body within the scientific community" [13:04], framed as "my own experience". The host's lines ("fiddling data series", "substitute abuse for argument") are the outlet's, not the author's; they are relevant to PC-10 only if the author later endorses the video (he links it from his own site's interview page, which counts as distribution, not endorsement of the wording).

### 2.6 Heartland podcast (2021-10-27; R. Connolly interviewed by H. S. Burnett, 52 min)

Source: local Whisper transcript (whisper.cpp 1.9.4, large-v3-turbo) of the archived MP3, `sources/transcripts/CN21_Heartland-podcast_2021-10-27.*` (audio SHA-256 in the `.meta.json`). The ASR has **no speaker labels**. Speaker attribution below is my reading of turn-taking and content. Each quote was string-checked against the transcript; none has yet been checked against the audio.

| # | Claim (≤ 25 words) | Level | Counterpart | Tier | O | Δ | Flags |
|---|---|---|---|---|---|---|---|
| HP-1 | "for the fifth assessment report, all four of the estimates that were used were what we call low variability estimates" [15:34] | L3 | body (CMIP5 forcing datasets); no indexed claim | T2 | 0 | — | ASR |
| HP-2 | "this is how they can say unequivocally or extremely likely … because none of the models, when they plug in one of these four TSI data sets, will show any … natural warming" [18:04] | L3 | A4 (L2) | T1 | 1 | +1 | ASR |
| HP-3 | "we found 16 different estimates of TSI … if you're just using all of the ones that … show the same decline … you're not actually doing a comprehensive scientific review" [19:31–20:04] | L3 | A4 "failed to adequately consider" (L2) | T1 | 1 | +1 | ASR |
| HP-4 | rural series: "the recent warming was similar to the warming in the 40s, which is definitely not the same as you get with the standard data sets" [22:47] | L4 (definitely) | C11 (L2) | T1 | 2 | +2 | **program-level** (framed as the 2015 paper; CN21 repeats the rural series); ASR |
| HP-5 | "by cherry-picking … your temperature data sets, and cherry-picking your solar data sets, you could explain anything from 0% solar role to 100% solar role" [24:39] | L3 | A3 (L2) | T3 | 0 | +1 | PC-7 = 1 (dataset dependence kept); register hit ("cherry-picking"); ASR |
| HP-6 | with results this different, "you're not converging towards a consensus" [25:26] | L3 | C15 "premature" (L2) | T0 | 2 | +1 | ASR |
| HP-7 | "Now, the IPCC began with certainties." [31:40] | L3 | none (the paper quotes the Bacon line without applying it to the IPCC's origins) | T0 | 2 | — | ASR |

Logged, not scored:
- **Extra-paper (PC-5).** UNEP "had already decided before the first assessment report … that human-caused climate change was an urgent catastrophe" [34:02]; the fact-check story: Climate Feedback "made 11 of the 14 errors that count as misinformation", the Epoch Times article "made zero" [42:17–42:25]; "narrative-driven journalism" [44:16 on]; the IPCC's urban-warming figure [21:49].
- **PC-10, second instance.** Asked whether the Epoch Times article "fairly represented what your study said", Connolly answers "Yeah" [37:22]. He later says Climate Feedback should call it "correct and accurate, which it is" [43:42] and praises it as "balanced reporting". That article paraphrases the study as showing "conclusively" that most or all warming may not be human-caused. The host's own introduction says the same (natural factors "accounted for most, if not all" recent climate change [0:49]), and Connolly does not correct it.
- **Moderation against the host.** When Burnett argues that a settled science should lose its funding [29:22–30:08], Connolly says "I've just got to push back a little bit and defend my scientific colleagues" [30:09]. His objection is to how grants are structured, not to his colleagues' good faith.
- **Register.** Not counted yet. The lexicon run needs speaker-separated text, and the ASR has no speaker labels. See log 7.

## 3. Statistics

| | Claims | O ≥ 1 | CAL | Mean O | Matched | Δ up / 0 / down | Mean Δ | PC-8 | PC-7 = 0 |
|---|---|---|---|---|---|---|---|---|---|
| All | 34 | 23 | **0.676** | 1.09 | 27 | 22 / 4 / 1 | **+0.96** | 2 | 3 |
| Excl. CERES-team text (§1.1) | 27 | 19 | 0.704 | 1.15 | 21 | 17 / 4 / 0 | +1.00 | 1 | 2 |
| Excl. ambiguous (Willson) | 32 | 21 | 0.656 | 1.00 | 27 | 22 / 4 / 1 | +0.96 | 2 | 3 |
| Excl. program-level (HP-4) | 33 | 22 | 0.667 | 1.06 | 26 | 21 / 4 / 1 | +0.92 | 2 | 3 |
| Spoken only (§2.5–2.6) | 10 | 5 | 0.500 | 0.80 | 7 | 6 / 1 / 0 | +1.00 | 0 | 0 |
| Written only (§2.1–2.4) | 24 | 18 | 0.750 | 1.21 | 20 | 16 / 3 / 1 | +0.95 | 2 | 3 |
| Paper (Exhibit 3) | 19 | 5 | 0.263 | 0.26 | | | | | |

## 4. Register (PC-9, exploratory)

Author text in this corpus (launch release, interview quotes, open letter; 5,093 words) has **4.5 dismissive-register hits per 1,000 words**, 39 % of them person-directed. Most come from two sources:
- the open letter's accusations against the fact-checkers ("misinformation", "censorship", "smearing"), aimed at named editors;
- Soon's interview quotes about the IPCC ("blatant untruth", "hoodwinked", "one-trick agenda", "childish hide-and-seek game", "abuse of science").

The opposing register in the same article is Gavin Schmidt's "This is total nonsense that no one sensible should waste any time on." It is recorded for the dyadic analysis and not scored as author text. Details: `../../register/`.

## 5. Judgment log

1. **CN-T3 against CN-T2.** The release hedges its lede ("may have been premature") and asserts the same claim in its opening summary paragraph ("was premature"). This is the within-document asymmetry Exhibit 1 found in LS11 (abstract against conclusion), reversed in position.
2. **ET-RC3.** The sentence hedges intent ("Whether they were deliberately doing it or whether it was simply confirmation bias is difficult to say") and asserts selection ("it is clear"). Scored at the strongest claim (L4). The intent hedge is noted as a genuine qualification.
3. **ET-RC1 tier.** The "all of the warming" case is one of 16 × 5 fits, in-sample, with no uncertainty (P2a = 0), so T1. The range claim across the grid (OL-2) keeps T3.
4. **"Premature."** The paper's most-repeated public word is its own conclusion term (A4, C15). Level changes come from the verbs around it ("was", "only", "should never have"), not from the word.
5. **Pending items (D4).** The Heartland podcast is now scored (§2.6). The prediction held: most of its claim-bearing talk is about conduct (IPCC, UNEP, fact-checkers), not the analysis. Only 7 of its passages carry scorable claims about the paper. The NTD segment has still not been relocated.
6. **CDN video: format effect.** In a produced interview, the author's spoken claims about the science stayed conditional and calibrated (§2.5). The escalation in this video is in the host's narration. The conduct claim R. Connolly does make is extra-paper and framed as personal experience. The written channels (release, interview quotes) remain where his escalation sits.
7. **Speaker attribution in the podcast.** Whisper gives no speaker labels. I attributed turns from context (question/answer structure, first-person references to "our paper", the host's own introduction). Two passages are uncertain and left unscored: "they're basically playing Pontius Pilate" [40:32] and "Science doesn't work by democracy" [4:20], which is probably Connolly's. For confirmatory work, D4 needs a diarization step (for example pyannote before Whisper) or a human pass that marks the turns. The register count for this item waits on that.
8. **HP-4 is program-level.** Connolly presents the rural result as a 2015 finding. It is scored because CN21 repeats the rural Northern Hemisphere series (C11). Dropping it moves CAL from 0.676 to 0.667 (row above).
