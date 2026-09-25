# Pilot Exhibit 4: Public Communications of L&S11 and F&R11 Scored with Index C

**Question.** Can the Index C overreach scoring used on the papers also score the authors' public statements about those papers? And did the authors qualify their claims appropriately when they discussed the findings in public?
**Corpus.** The in-window items in `public-communications-inventory-LS11-FR11.md` (compiled 2026-09-18), read 2026-09-25 from live pages or Wayback captures (sources in §8).
**Instrument.** Codebook v0.2 §4, with the adaptation rules in §1 below. These rules are proposed here and have not been enacted.
**Scorer/run.** Claude, single run, 2026-09-25. Pilot-exhibit conventions apply: one run plus a full judgment log.
**Status.** Exploratory. It sits outside the pre-registered design, which scores papers only.

---

## 0. Bottom line

1. **Yes, Index C can score the communications, but it needs three additions.** Level scoring (§4.2) works as written on blog and press-release sentences. The workable design gives each communication claim the **evidential tier of the paper claim it restates**, since a blog post adds no new evidence, and scores its **level fresh**. That produces two measures: overreach O, as in §4.4, and **drift Δ**, the level change from the paper's version of the same claim. Three failure modes remain that the current instrument cannot see. The additions for them are in §5.
2. **L&S11. The launch communications mostly copied the abstract's calibration, but the headline claims were escalated.** Eight of twelve matched claims kept their paper level. The four that changed all moved upward, and the largest moves were on the most-quoted claims:
   - an attribution that the paper **labels an assumption** became the headline "Human Effect on Climate Clearly Detected";
   - "may be due to a natural 60-year cycle" became "In fact … well predicted by";
   - "better than any model we have seen" became "better than any other attribution study".

   Scafetta's later posts moved the attribution share from "more than half" to "at least 2/3 … as proven". CAL across the communications is **0.77**, against 0.57 for the paper. Forecast language went the other way: it was *softer* in public than in the paper. Explicit humility statements ("Time will tell", "my model is not a 'oracle crystal ball'") appear next to emphatic claims and do not scope them.
3. **F&R11. The communications reproduce the paper's language closely, often word for word, and CAL is 0.09, against 0.00 for the paper** (revised 2026-09-25; see the German review packet). There are two real problems, both in one German post from September 2012. First, Rahmstorf cited F&R11 for comparing the natural influences with **anthropogenic CO2**. The paper explicitly declines that step: it isolates the trend "whatever its cause". Second, he cited F&R11 as showing a stronger satellite-data response to **solar cycles**, a difference the paper reports as not statistically significant. The low score also reflects a **ceiling effect**. The paper already uses top-level language at top-level evidence, so dropped scope qualifiers cannot register as overreach. The clearest case is Rahmstorf's "groundless misconception" quote, which drops the paper's "beyond the variability induced by these known natural factors".
4. **Program-level claims.** Much of what the L&S11 authors said in public in 2012 comes from Scafetta's later JASTP paper, and much of the F&R11 authors' late-window material comes from Rahmstorf–Foster–Cazenave 2012. Neither is scored against the pilot papers (§4).

## 1. Adaptation rules applied (proposed, not enacted)

- **C-1 Unit and extraction.** The unit is a sentence, written or quoted directly from an author, that asserts a finding traceable to the paper. The §4.1 exclusions apply. Headlines count when the author wrote them: WUWT guest posts carry author-written titles. Comment threads are not itemized, following inventory scope; they are sampled qualitatively in §6.
- **C-2 Tier inheritance.** Each claim is matched to a scored paper claim (IDs from Exhibits 1 and 2) or, where needed, to a paper body passage. It takes that claim's tier. A claim that widens scope past what the paper supports takes the tier the paper provides for the *wider* claim. A claim without paper support is T0.
- **C-3 Drift.** Δ = level(communication) − level(paper counterpart). It is reported alongside O. Δ can register escalation even where O is capped by a high tier.
- **C-4 Attribution to source.** A claim is scored against the pilot paper only if it is about the pilot paper's analysis. Claims resting on a later paper by the same authors are logged as **program-level** and are not scored (§4).
- **C-5 Extra-paper claims.** Claims about other work or about opponents (GCMs, the IPCC, "fake skeptics"), and policy statements, are logged by category and not scored. §4.1 already excludes them for papers.
- Forecasts are tagged under §4.6 and excluded from CAL. German items are scored from the original; English glosses are given in brackets.

## 2. L&S11: scored communication claims

Sources: **CE/W** = the launch post, identical body on Climate Etc. (bylined Loehle) and WUWT (bylined Loehle and Scafetta), 2011-07-25. **S-Jan** = WUWT, 2012-01-09. **S-Mar** = WUWT, 2012-03-11.

| # | Src | Claim (≤ 25 words) | Level | Paper counterpart (level) | Tier | O | Δ |
|---|---|---|---|---|---|---|---|
| LC1 | W headline | "Human Effect on Climate Clearly Detected" | L4 (clearly) | Abstract: "Herein we assume that the residual upward warming … has been mostly induced by … anthropogenic emissions" (labelled assumption, unscored); body: "likely a signal of anthropogenic warming" (L2) | T1 | 2 | +2 |
| LC2 | CE/W | "The resulting full natural plus anthropogenic model … fits the entire 160 year record very well." | L3 | A2 (L3) | T1 | 1 | 0 |
| LC3 | CE/W | "Residual analysis does not provide any evidence for a substantial cooling effect due to sulfate aerosols from 1940 to 1970." | L4 (neg.-universal) | A3 (L4, per erratum) | T1 | 2 | 0 |
| LC4 | CE/W | "In fact, the cooling observed during that period is well predicted by a natural 60-year cycle" | L4 (in fact) | A4 "may be due to" (L1) | T1 | 2 | **+3** |
| LC5 | CE/W | "New solar activity proxy models developed in the paper suggest a mechanism for both the 60-year climate cycle and a portion of the long-term warming trend." | L2 | A5 (L2) | T1 | 0 | 0 |
| LC6 | CE/W | "About 60% of the warming observed from 1970 to 2000 was very likely caused by this natural 60-year climatic cycle" | L2 (likely) *see log 2* | A6 "suggest … around half" (L2); C13 (L3) | T1 | 0 | 0 |
| LC9 | CE/W concl. 1 | "The estimated AGW component matches theory … The timing of AGW effects (beginning in 1942) also matches expectations." | L3 | none in scored sections | T1 | 1 | n/a |
| LC10 | CE/W concl. 2 | "The fitted components match solar model forcings within their uncertainty." | L3 | A5 "suggest a mechanism" (L2) | T1 | 1 | +1 |
| LC11 | CE/W concl. 3 | "The estimated sensitivity matches a no-amplification (neutral) climate sensitivity, or even a slight negative feedback case." | L3 | C6 (L3) | T1 | 1 | 0 |
| LC12 | CE/W concl. 4 | "This 0.66 value is an upper bound in our estimation (due to possible poorly corrected UHI and LULC effects …)" | L2 (in our estimation) | C20 (L2) | T0 | 1 | 0 |
| LC14 | CE/W concl. 6 | "Our result matches the historical record better than any other attribution study and better than GCM outputs." | L4 (superlative) | C11 (L4, T0); body "better than any model we have seen" | T0 | 3 | 0, **scope widened** |
| SJ1 | S-Jan | "we have argued that the global instrumental surface temperature records … suggest that the climate system is resonating and/or synchronized to numerous astronomical oscillations" | L2 | C1 (L2) | T1 | 0 | 0 |
| SC1 | S-Mar | "the 60-year natural cycle (plus the other cycles) contributed at least 2/3 of the 1970-2000 warming, as proven in my papers" | L4 (proven; at least) | C13 "more than half" (L3) | T1 | 3 | +1, magnitude ½ → ⅔ |

**Forecasts (§4.6, excluded from CAL).**

| # | Claim | Level | Paper counterpart | Δ | Interval |
|---|---|---|---|---|---|
| LC7 | "climate may remain approximately steady until 2030-2040, and may at most warm 0.5-1.0°C by 2100" | L1 | A7 (L1) | 0 | range given, no error model |
| LC13 | "Cooling/flat temperatures till 2030 are likely (as also predicted by others)." | L2 | C21 (L3) | **−1** | none |

**Normative flag (§4.5).** Concl. 4: "Warming … of 0.66 oC/Century is not alarming". The paper's p20 normative sentence reappears in stronger form.
**Provisional, not in totals.** Loehle's 2012-04-17 statement, known only from a secondary report: the paper "attributes about 40% of recent warming to human activity". That would be L3 against A6 (L2), T1, O = 1, Δ = +1. It needs the primary text before it can count.

**L&S11 statistics.** 13 claims scored and 10 overreaching, so **CAL = 0.769** (paper 0.571). Mean O = 17/13 = **1.31** (paper 0.82). L4 at tier ≤ T1: **5** (paper 3). Across the 12 claims with a paper counterpart, drift was +3, +2, +1 and +1, and zero for the other 8. None moved down. The one downward move is a forecast (LC13).

## 3. F&R11: scored communication claims

Sources: **OM** = Open Mind, 2011-12-06 (Foster). **KL1** = KlimaLounge, 2011-12-08 (Rahmstorf, German). **IOP** = IOP press release, 2011-12-05, with the quote attributed to Rahmstorf by name. **KL2** = KlimaLounge, 2012-09-27 (Rahmstorf, German).

| # | Src | Claim (≤ 25 words) | Level | Counterpart | Tier | O | Δ |
|---|---|---|---|---|---|---|---|
| FT1 | OM | "by removing their influence from the temperature record makes the progress of global warming much more clear" | L3 | F2 (L3) | T3 | 0 | 0 |
| FT3 | OM | "the continued course of warming over the entire time span (including the last decade) is undeniable" | L4 | F9 (L4) | T3 | 0 | 0 |
| FT4 | OM | "in all five adjusted data sets, the last two years (2009 and 2010) are the two hottest" | L3 | F5 (L3) | T3 | 0 | 0 |
| FT5 | OM | "None of the data sets shows any evidence that the global warming rate has changed recently." | L4 | F10 (L4) | T3 | 0 | 0 |
| FT6 | OM | "All five data sets show statistically significant warming since 2000." | L3 | body result (fig. 6) | T3 | 0 | n/a |
| FT7 | OM | "el Nino and volcanic aerosols have a stronger influence on lower-atmosphere temperature … than on surface temperature" | L3 | F3 (L3) | T3 | 0 | 0 |
| FT8 | OM | "uncertainty levels in trend estimates using surface and satellite data are comparable" | L3 | body (Table 1) | T3 | 0 | n/a |
| FT9 | OM | "That shows, with great clarity and impact, the real global warming signal." | L4 | F13 (L4) | T3 | 0 | 0 |
| FR1 | KL1 | "Zum Trend tragen diese praktisch nichts bei" [these contribute practically nothing to the trend] | L4 (neg.-universal; *praktisch* = approximator) *rev.* | body/fig. 7 (L3) | T3 | 0 | +1 |
| FR2 | KL1 | "stimmen die fünf Datenreihen deutlich besser überein als vorher" [the five series agree much better than before] | L3 | F12/fig. 5 | T3 | 0 | n/a |
| FR3 | KL1 | "Reaktion auf ein El Niño Ereignis in den Satellitendaten … rund doppelt so stark … wie in den Bodendaten" [El Niño response about twice as strong in satellite data] | L3 | F3 (L3) | T3 | 0 | 0 |
| FR4 | KL1 | "die beste Schätzung für diesen Trend liegt in allen Datenreihen sehr nah am Langzeittrend seit 1979" [best estimate very close to the long-term trend] | L3 (strongest claim in the sentence: "ist … statistisch signifikant") *rev.* | fig. 6 | T3 | 0 | n/a |
| FR2b | KL1 | "die Unterschiede zwischen den Datenreihen nicht im Klimatrend liegen sondern in den kurzfristigen Schwankungen" [the differences lie not in the trend but in the short-term fluctuations] *added* | L3 | F1/F3 | T3 | 0 | 0 |
| FR9 | KL1 | 2011 relatively cool, "konsistent mit der Analyse in unserem Paper" [consistent with the analysis in our paper] *added* | L2 | ENSO coefficients | T3 | 0 | n/a |
| FR5 | KL1 | "keinerlei Hinweise auf eine Verlangsamung oder gar Pause in der globalen Erwärmung" [no indication whatsoever of a slowdown or pause] | L4 | F10 (L4) | T3 | 0 | 0 |
| FR6 | KL1 | "In allen fünf Datenreihen sind die beiden wärmsten Jahre 2009 und 2010." [2009 and 2010 are the two warmest years in all five series] | L3 | F5 (L3) | T3 | 0 | 0 |
| FP1 | IOP (Rahmstorf) | "the idea that the global warming trend has slowed or even paused over the last decade or so is a groundless misconception" | L4 (absolute) | F10 (L4) | T3 | 0 | 0, **qualifier dropped** |
| FP2 | IOP (Rahmstorf) | "differences between the five data sets reside, to a large extent, in their short-term variability and not in the climatic trend" | L3 | F1/F3 | T3 | 0 | 0 |
| FP3 | IOP (Rahmstorf) | "After the variability is removed, all five data sets are very similar" | L3 | F12 | T3 | 0 | 0 |
| FR7a | KL2 | satellite data show "praktisch den gleichen Erwärmungstrend" as surface data [practically the same warming trend] | L3 | F1/Table 1 | T3 | 0 | 0 |
| FR7b | KL2 | "die Variabilität bei den Troposphärendaten wesentlich größer, insbesondere die Reaktion auf El Niño … und die Sonnenzyklen (wir zeigen das in Foster & Rahmstorf" [especially the response to El Niño and the solar cycles; we show this in F&R] *rev.* | L3 | F3 for El Niño; for solar, the paper says the LT–surface difference "is not statistically significant" | ≤ T1 (solar) | **1** | fidelity error (C-8) |
| FR8 | KL2 | "Die natürlichen Einflüsse (Vulkane, Sonnenzyklen) auf den Trend sind verschwindend gering im Vergleich zum anthropogenen CO2 (siehe z.B. … Foster & Rahmstorf 2011)" [natural influences on the trend are vanishingly small compared with anthropogenic CO2] | L3 | F9 parenthetical "(most likely these are exclusively anthropogenic)" (L2); paper isolates the trend "whatever its cause" (Introduction) | T0 for the CO2 comparison *see log 5* | **2** | +1 |

**Forecast (excluded).** FP4, Foster in the IOP release: "The unabated warming is powerful evidence that we can expect further temperature increase in the next few decades". This is F14 word for word: L4, Δ 0, no interval. **Normative flags:** FP4's trailing clause, identical to the paper's, and OM's "it should put an end to real skeptics claiming that global warming has recently stopped".
**Qualification added, not scored:** OM describes the adjusted data as "mostly (but not completely!) free of their influence". That is more careful than the paper's F8 ("isolating").

**F&R11 statistics (revised 2026-09-25).** 22 claims scored and 2 overreaching (FR7b, FR8), so **CAL = 0.091** (paper 0.000); if FR8 is read the alternative way (log 5), CAL = 0.045. Mean O = 3/22 = **0.14**. Drift was zero on matched claims except FR1 (+1, still O = 0 at T3) and FR8 (+1). *First-pass values: 19 claims, CAL 0.053.* The German items (FR1–FR9) are documented for non-German reviewers, with marker notes and full translations, in `translation-review/rahmstorf-DE_review-packet.md`. That file also proposes C-8 (fidelity error).

## 4. Program-level and extra-paper material (logged, not scored)

**Program-level (C-4).** These claims rest on later papers, not the pilot papers.
- S-Jan (almost entirely), the widget page, and Forbes all draw on Scafetta's JASTP 2012 paper. Examples: "I have proved that all GCMs adopted by the IPCC fail…"; "0.3–1.2 °C by 2100"; "the IPCC projections for the 21st century cannot be trusted". S-Mar's "overestimated … by about 2.6 time on average" and "no more that 0.2-0.3 oC of the observed 0.8 oC" also belong here. L&S11 itself said "two to three times" and "no more than 0.4°C is likely".
- F&R11 authors: Tamino, 2012-12-01, "Clearly (unless you're in denial) observed temperature change has proceeded in excellent agreement with IPCC projections". Rahmstorf, IOP/PIK 2012-11-28, "the IPCC is far from alarmist … That applies not just for sea-level rise, but also to extreme events and the Arctic sea-ice loss". Both are Rahmstorf–Foster–Cazenave 2012. The extension to extreme events and sea ice goes beyond that paper's own scope as well, and would score T0 if the program were scored.

**Extra-paper claims (C-5).** L&S11 launch: "Current methods based on climate models are unfortunately circular"; S-Jan: "we probably do not need to destroy our economy". F&R11: OM "Fake 'skeptics' like to claim…"; KL2 on Vahrenholt, "Bauernfängertricks" [con-man tricks]. Much of the persuasive weight of the communications sits in this excluded category on **both** sides. The contemptuous register is roughly symmetric: "childish trick", "stupid, before than being dishonest" on one side; "fake skeptics", "Bauernfängertricks" on the other. Index C does not measure register at all.

## 5. Does the instrument travel? What works and what doesn't

**Works as written.**
- The §4.2 level rules applied cleanly to blog prose, press quotes and German text. The only new judgment call was IPCC-calibrated vocabulary (log 2).
- Tier inheritance (C-2) plus drift (C-3) caught the escalations with no outside science. As with C9 in Exhibit 1, each flag compares the authors' public sentence with their own paper.
- §4.6 carried over unchanged and surfaced one real finding: L&S11 forecasts were hedged *more* in public than in the paper.

**Three blind spots, with proposed items.**
1. **Promoting an assumption to a finding.** §4.1 (r5) removes labelled assumptions from paper scoring, so the paper-side record has no entry when a communication asserts one. LC1 was scored against the body's L2 sentence; the abstract's "Herein we assume" alone would give no counterpart. *Proposed C-6:* log any communication claim whose paper counterpart is a labelled assumption, with a binary flag ("assumption promoted"), alongside O.
2. **Dropped qualifiers under a T3 ceiling.** At T3 every level is permitted, so O cannot register when a hedge or scope limit is removed. FP1 drops "beyond the variability induced by these known natural factors"; LC14 drops "we have seen". Drift catches level changes only, not scope changes. *Proposed C-7, qualifier retention (0/1):* does the communication keep each explicit scope, condition or uncertainty qualifier attached to the counterpart claim in the paper? This is mechanical given the matched pair, and it treats the two sides alike: it fires on FP1 and LC14 both.
3. **Humility statements that scope nothing.** Scafetta's posts contain "my model is not a 'oracle crystal ball'", "Perhaps, the model I proposed in just another illusion", and "Time will tell". Nearby sentences say "greatly outperform all current GCMs" and "as proven in my papers". Under the weakest-marker rule the hedge governs only the sentence it scopes, which is correct. A reader, though, takes the post as a whole. *Proposed:* count free-standing epistemic-humility sentences separately (an S-style density), so neither side gets credit for boilerplate and neither loses credit for it.

**Design limits to record.**
- The communication sample is **selected by the authors**: they choose which claims to repeat. Comparing CAL between papers and communications mixes calibration with selection. Drift over matched pairs is the cleaner statistic.
- Verbal items (ICCC-6/7 talks) are unscored. Comment threads, where the L&S11 authors were most active, are out of scope.
- The English-only filter removes most of Rahmstorf's broadcast record (inventory note). The two German blog posts are scored here from the original.
- Program-level attribution (C-4) is a judgment on which paper a sentence rests on. On the L&S11 side, most 2012 material falls outside the pilot paper under it.

## 6. Qualitative notes

- **Comment threads, L&S11 (sampled).** Loehle's WUWT replies on launch day are *more* hedged than the post in places. Examples: "We assume that this MAY somehow affect solar output/magnetic field etc."; "there are many complications that no doubt deserve investigation"; "we argue that the 0.66 deg C/century is an upper bound–the reviewers made us take out our attempt to estimate and subtract this factor". The same replies assert "The model predicted the downturn at 2000 based on fitting only up to 1950" (cf. C14). If threads are ever itemized, expect mixed direction there.
- **Self-correction, F&R11.** Foster's code-release post, nine days after publication, publicly corrects an axis-label error in fig. 3 and releases the full R code, with an update when a subroutine was found missing. This is post-publication conduct the A-index would miss, like the self-initiated re-test noted in Exhibit 2 §4.
- **Public test, L&S11.** The widget page frames the forecast as a test, "will the forecast hold, or my proposed model is just another failed attempt …? Time will tell", and exempts ENSO-scale excursions in advance. The inventory appendix documents what followed: one update, deletion without a verdict, and later vindication claims on stale data series. That is a Forecast-Index outcome, not a calibration one.

## 7. Judgment log

1. **LC1 tier.** Scored T1 against the body sentence "likely a signal of anthropogenic warming" (L2). If only the abstract's labelled assumption counts, the tier is T0 and O = 3. The conservative reading is used.
2. **"Very likely" (LC6).** §4.2 lists "likely" as L2 and has no rule for IPCC-calibrated modifiers, where "very likely" means ≥ 90 % probability. Scored L2. Suggested rule: a calibrated likelihood term with no stated probability model scores one level higher (LC6 → L3, O = 1). It would apply equally to both groups.
3. **LC12 is both a claim and a caveat.** The upper-bound sentence adds a qualification, so the reader is warned, but it asserts a bound whose correction the paper never quantifies (T0, as in C20). Scored O = 1, matching C20.
4. **LC14 scope.** "Any model we have seen" (body) became "any other attribution study". The level is unchanged; the widened scope is recorded under proposed C-7.
5. **FR8 reading.** Read narrowly, it says volcanic and solar contributions to the 1979–2010 trend are near zero. F&R11 shows that at T3 (fig. 7), giving O = 0. As written, the claim compares those contributions with *anthropogenic CO2*. The paper refuses that attribution step ("to isolate the remaining global warming trend, whatever its cause", Introduction) and offers only a hedged parenthetical, so as a claim about CO2 it rests on citation (T0), giving O = 2. The sentence's own comparison is scored. This is the one F&R11 item to route to human audit.
6. **SJ1 and SC1 attribution.** Both name L&S11 among "my papers". SC1's "at least 2/3" matches no L&S11 figure. L&S11 has "more than half" and "about 60%", and the ⅔ may come from JASTP. It is scored against C13 because the post frames it as the conclusion of the published cycle program that includes L&S11. Scoring it as program-level instead would give L&S11 CAL = 9/12 = 0.75.
7. **Inventory corrections.** (a) The 2011-12-05 IOP release attributes the "groundless misconception" quote to **Rahmstorf by name**; the inventory says it is unattributed. (b) The live Climate Etc. URL returned "Not found" in the in-app browser on 2026-09-25, which reproduces the owner's report. The 2017 Wayback capture loads and was used. (c) The Forbes page did not render in the browser. Its quotes were taken through a text-extraction fetch, and because they are program-level (JASTP) they are unscored.

## 8. Sources read (2026-09-25)

- Climate Etc., Loehle, 2011-07-25: Wayback 20170711213953 capture of judithcurry.com/2011/07/25/loehle-and-scafetta-on-climate-change-attribution/
- WUWT launch, 2011-07-25: Wayback 20200213070301 capture (post body and 40 Loehle-attributed comments located)
- WUWT: 2012-01-09 guest post; 2012-02-10 widget announcement; 2012-03-11 widget update (live pages)
- WUWT widget reference page: Wayback 20120413172650 capture
- Forbes (Bell), 2012-01-10: text-extraction fetch only
- Open Mind: 2011-12-06 (×2), 2011-12-15, 2012-12-01 (live)
- RealClimate, 2011-12-06 (group byline; excluded as not attributable to one author; content restates the paper faithfully)
- KlimaLounge: 2011-12-08 and 2012-09-27 (live)
- ScienceDaily: 2011-12-05 IOP release and 2012-11-28 release; Phys.org, 2012-11-28 (live)
- Not read: ThinkProgress PIK reproduction (403); Loehle 2012 statement (no primary text); ICCC-6/7 talks (video; unscored)

**Archive.** Verbatim text captures of the 14 pages read in the browser are in `pilot/communications/sources/`, with provenance headers and SHA-256 hashes in `MANIFEST.md`. Every communication quote above was checked mechanically against those captures, and every paper quote against the repo's LS11/FR11 full texts. Three items were read only through a model-mediated text-extraction fetch and have no verbatim capture: Forbes (program-level, unscored), RealClimate (excluded) and Phys.org (duplicates the ScienceDaily release, which is captured). Loehle's 2012 statement (provisional) is known only from a secondary report.
