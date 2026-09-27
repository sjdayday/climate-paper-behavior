# Pilot Exhibit 5: Public Communications of Connolly et al. (2021)

**Instrument.** Protocol v0.2 (draft), `sources/communication-behavior-protocol_v0.2.md`. Stage 1 counterparts are the claim IDs in `../scoring-exhibit-3_Connolly-etal-2021_v0.2.md` (A1–A4, C1–C15) plus anchored body passages.
**Corpus.** `public-communications-inventory-CN21.md`. Verbatim captures are in `sources/`.
**Scorer/run.** Claude, single run, 2026-09-26. Pilot convention: judgment log in place of three runs.
**Status.** Exploratory; CN21 is outside the sampling frame (Exhibit 3 header).

## 0. Bottom line

- **Drift was upward and concentrated on one claim type.** 22 of 27 claims matched a Stage 1 counterpart. Of those 22, **17 moved up**, 4 held level and 1 moved down (mean Δ = +0.91, against +0.58 for the LS11 author posts and +0.12 for FR11; Exhibit 4). Communication CAL is **0.667** (paper 0.263). The three claims from the CDN video (added 2026-09-26, §2.5) are all calibrated; before them CAL was 0.75.
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

## 3. Statistics

| | Claims | O ≥ 1 | CAL | Mean O | Matched | Δ up / 0 / down | Mean Δ | PC-8 | PC-7 = 0 |
|---|---|---|---|---|---|---|---|---|---|
| All | 27 | 18 | **0.667** | 1.07 | 22 | 17 / 4 / 1 | **+0.91** | 2 | 3 |
| Excl. CERES-team text (§1.1) | 20 | 14 | 0.700 | 1.15 | 16 | 12 / 4 / 0 | +0.94 | 1 | 2 |
| Excl. ambiguous (Willson) | 25 | 16 | 0.640 | 0.96 | 22 | 17 / 4 / 1 | +0.91 | 2 | 3 |
| Before the CDN video | 24 | 18 | 0.750 | 1.21 | 20 | 16 / 3 / 1 | +0.95 | 2 | 3 |
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
5. **Pending items (D4)** could change the picture. The Heartland podcast, 52 minutes of R. Connolly, is probably the largest single source of claims. Its title ("Exposing efforts to suppress research…") suggests the conduct-claim pattern continues. Its MP3 is dead on heartland.org but archived by the Wayback Machine (2021-10-27, 39.7 MB); it needs local transcription (`scripts/transcribe_local.sh`). The NTD segment was not relocated. Not scored.
6. **CDN video: format effect.** In a produced interview, the author's spoken claims about the science stayed conditional and calibrated (§2.5). The escalation in this video is in the host's narration. The conduct claim R. Connolly does make is extra-paper and framed as personal experience. The written channels (release, interview quotes) remain where his escalation sits.
