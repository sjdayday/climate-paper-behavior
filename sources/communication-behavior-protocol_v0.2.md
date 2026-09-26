# Communication-Behavior Protocol: v0.2 (pilot draft)

**Study:** Behavioral signatures distinguishing contrarian and mainstream climate-attribution papers. **Stage 2: public communication about the papers.**
**Companion to:** `paper-behavior-codebook_v0.2.md` (Stage 1). Section references of the form "codebook §x" point there.
**Status:** DRAFT, not frozen. v0.2 records decisions D2, D3, D4 and D6 (2026-09-26) and lessons from the second pilot round (Exhibit 4 Addendum 1; Exhibit 5, Connolly et al. 2021). D1, D5 and D7 remain open. Pilot materials: `pilot/communications/` (LS11, FR11) and `pilot/connolly-2021/communications/` (CN21). Rule-ID cross-references are in Appendix A.

---

## 1. Purpose and construct

Stage 1 scores a paper as behavior. It asks whether the paper's claims are calibrated to the evidence the paper itself provides. Stage 2 scores a **separate, related behavior**: how the authors present their own paper to public, non-specialist audiences. The Stage 2 construct is **fidelity to the paper**, not calibration to evidence. A communication is judged against the paper as written, because the paper is the only evidence the authors can point to for that claim.

The two stages combine through a decomposition. A communication claim takes its evidential tier from the matched paper claim (PC-2) and is scored for level afresh. Therefore:

> level(public) = level(paper) + Δ, at the shared tier,

and public overreach splits into a **paper-stage** component (Stage 1 CAL) and a **communication-stage** component (drift Δ). Neither stage's scores enter the other's hypotheses. Their relationship is a separate, pre-registered question (§6, HC-L).

As in Stage 1, correctness is out of scope, intent is not inferred (codebook §14.5), and the design's credibility rests on item-level auditability, not on scorer neutrality.

## 2. Sequencing and independence

1. **Stage 1 first, frozen.** Stage 2 retrieval and scoring start only after Stage 1 confirmatory scoring is complete, audited and committed for every paper. The frozen Stage 1 record includes the per-paper claim list: IDs, verbatim text, levels, tiers, and any explicit qualifiers attached to each claim.
2. **One-way dependency.** The Stage 2 scorer receives the paper text and the frozen Stage 1 claim list as fixed inputs. No Stage 2 output can revise a Stage 1 score. If a Stage 2 run turns up an apparent Stage 1 error, it goes to an erratum log that is reported with Stage 1, following its own amendment rules (codebook §15). Stage 2 scores use the frozen Stage 1 values, not corrected ones, and a sensitivity analysis applies the corrections.
3. **Separate runs.** Stage 2 runs never share a context with Stage 1 runs. This guards against contamination in both directions: a scorer that has just read a blog's escalation is not a neutral reader of the abstract.
4. **Separate hypothesis family.** Multiplicity control runs within the Stage 2 family (§9). Stage 2 results cannot rescue or undercut Stage 1 hypotheses H1–H3.

## 3. Sample, window and eligibility

**3.1 Papers and authors.** The Stage 2 frame is the Stage 1 confirmatory sample. For each paper, retrieval covers the authors in the Stage 1 author scope. That scope depends on pending amendment r10 (first-author-only primary): if r10 is adopted, Stage 2 follows it for primary analysis and retrieves co-authors for sensitivity. Pilot papers LS11 and FR11 are excluded, as in Stage 1.

**3.2 Window.** From 3 months before to 12 months after the paper's publication date (earliest of online-first or issue date).

**3.3 Admissible items.** An item is admissible if it is public, non-scholarly, inside the window, and **authored by or directly attributed to** an in-scope author. Admissible types:
- blog posts or guest posts bylined to the author;
- op-eds;
- press releases, **only** for text in quotation marks attributed to a named author (but see §3.3a);
- interviews in print, online or broadcast, **only** for direct quotes. Broadcast and recorded items are **transcribed** (D4): audio → text, archived with the audio's SHA-256 hash, the transcription tool and version, and a human check of every scored quote against the audio. Platform auto-captions count as transcripts with an ASR flag;
- recorded public talks outside scientific conferences;
- author-maintained public pages, such as a forecast widget;
- social media posts by the author's own account (**D2: included**). Retrieval needs authenticated platform access, an author-provided archive, or archive captures (§3.7). Where none is available, the item class is recorded as **not retrievable**, which is a retrieval limit, not a null.

**3.3a Releases from author-led organizations.** When a release is issued by an organization an in-scope author leads or co-leads, and is bylined collectively ("CERES team"), its unquoted text is admissible as author text. It is **flagged**, and a sensitivity analysis excludes it. The pilot case is the CN21 launch release.

**3.4 Excluded.** Scholarly channels (journals, preprints, conference talks, open-review comments). Journalist paraphrase, and quotations lifted from the paper text. Press-office or institutional text not attributed to a named author. Group-bylined posts not attributable to one author (unless §3.3a applies). Third-party translations or reproductions of author items (for example EIKE translations): the original is captured instead.

**3.4a Comment threads (D3: exploratory, census).** Author replies in reader-comment threads under admissible items, and in threads under the authors' own posts, are captured as a **census**, not a sample (rationale: Exhibit 4 Addendum 1 §1.3). They are scored with the same items as primary material but reported as a separate, **exploratory** stratum that never enters primary composites. Each reply records its thread, timestamp, addressee (when identifiable) and exchange index within its dyad (PC-9b). Threads are captured from archives when live pages paginate or truncate, and **completeness is reported per thread** (captured author replies and total comment count).

**3.5 Authorship of headlines and captions.** A headline or caption counts as author text only with evidence of authorship: the venue's guest-post convention, the author's own byline on the page, or a statement. Otherwise it is logged and not scored. This matters because the most escalated item in the pilot was a headline.

**3.6 Language.** There is **no language filter**. All languages are retrieved and scored under §8. Language is recorded for every item.

**3.7 Retrieval protocol.**
- Retrieval uses fixed search templates: the author name × paper title keywords × window, run across web search, archive services and named venue types. Templates are fixed at freeze and applied identically to both groups. They run in English and in each author's working languages (institutional affiliation country plus any language of the author's known public output).
- Every retrieved item is archived as a verbatim text capture, with URL, retrieval date, capture method and SHA-256 hash, plus a Wayback reference where one exists. The pilot format is `pilot/communications/sources/MANIFEST.md`.
- Items that cannot be retrieved (dead links, paywalls, missing transcripts, sign-in walls) are recorded with their reason.
- **Archive first for threads.** Live comment systems may render only part of a thread (pilot: 25 of 119 comments). Wayback captures from within or near the window are the preferred source, with the live page as fallback.
- **Social media (D2).** Retrieval uses a platform research API or an author-provided archive, with archive captures of profile timelines as fallback.
- **Transcription (D4).** Recordings are downloaded only where the download is permitted, transcribed locally, and hashed as in §3.3.
- **Null results are data.** A paper with no admissible items is recorded as such (HC0), not dropped.

## 4. Claim extraction and matching

**4.1 Extraction (PC-1).** From each admissible item, extract every sentence that asserts a finding traceable to the paper. Codebook §4.1 exclusions apply: methods descriptions, restatements of others' findings, raw-data descriptions, labelled assumptions and normative statements. If a sentence contains several distinct claims, score the one with the **highest level** (codebook §4.1 "strongest"). Where claims at the same level have different tiers, the **lowest tier** governs (pilot convention, Exhibit 4 FR7b).

**4.2 Attribution: paper or program (PC-4).** A claim is **paper-attributable** if it names or links the paper, **or** if it matches a frozen paper claim or body passage in content and appears in an item that references the paper. A claim resting on the authors' other or later publications is **program-level**: it is logged but not scored. Ambiguous cases are scored as paper-attributable and flagged, and a sensitivity analysis drops the flagged cases. A co-author's quote in the paper's own launch release counts as ambiguous when its content is not in the paper (pilot: Willson, CN21).

**4.3 Matching.** Each paper-attributable claim is matched to a frozen Stage 1 claim ID or, failing that, to an anchored passage in the paper body. Unmatched claims with no support in the paper are tier **T0**.

**4.4 Extra-paper claims (PC-5).** Claims about other work, opponents, institutions or policy are logged by category and not scored. Categories: characterizations of opponents or their methods; claims about institutions such as the IPCC; policy or economic claims; claims about the scientific process. The share of such content is an outcome (HC5).

## 5. Items

For every scored claim:

| Item | Definition | Type |
|---|---|---|
| **Level** | Codebook §4.2, applied to the **original-language** text with that language's pinned lexicon (§8.1). | L1–L4 |
| **PC-2 Tier** | Inherited from the matched paper claim or passage. If the communication **widens scope** beyond the matched claim, it takes the tier the paper provides for the wider claim. | T0–T3 |
| **O** | max(0, level − permitted(tier)), codebook §4.4. | 0–3 |
| **PC-3 Drift Δ** | level(communication) − level(matched paper claim). Defined for matched claims only. | integer |
| **PC-6 Assumption promotion** | The matched paper content is a labelled assumption (codebook §4.1/r5), and the communication asserts it at L3 or above as a finding. | 0/1 |
| **PC-7 Qualifier retention** | Defined where the matched paper claim carries ≥ 1 explicit qualifier (scope limit, condition, uncertainty statement or interval). Scores 1 if every such qualifier is kept or paraphrased, 0 otherwise. Mechanical given the frozen qualifier list (§2.1). | 0/1 |
| **PC-8 Fidelity error** | The communication attributes to the paper a finding the paper does not report, reports as not significant, or reports with the opposite sign. | 0/1 |
| **Forecast tag** | Codebook §4.6: horizon, whether an interval is given, and level. Forecasts are excluded from communication CAL. | tag |
| **Normative flag** | Codebook §4.5. | log |
| **PC-10 Endorsement of escalated coverage** (exploratory) | The author explicitly endorses, as accurate, a third-party account of the paper that itself contains claims at a higher level than the paper (pilot: CN21 open letter asking that the Epoch Times article be rated "Correct" and "Accurate"). | 0/1 per item |

**PC-9 Register (exploratory; D6).** Computed per unit (primary item or reply), independently of claim scoring:
- **PC-9a counts.** A mechanical pass with the pinned dismissive-term lexicon (`sources/lexicons/register_dismissive_*.json`; categories R1 group labels, R2 competence, R3 motive and honesty, R4 ridicule and profanity, R5 exclusion and admonition), per 1,000 words, after removing quoted material longer than 3 words. Every hit is then **audited** (keep or drop, with a reason) and given a **target** code: P (a named or addressed person), G (a group or institution), W (a work or argument). Reported per author × item type.
- **PC-9b relational variables.** For replies: addressee, dyad (author → addressee), exchange index within the dyad, cumulative prior exchanges across threads, and days since the dyad's first exchange. For primary items: whether a named opponent is addressed.
- **PC-9c counterpart register.** Where a news item quotes an opposing scientist in the same exchange (pilot: Schmidt's "total nonsense" in the CN21 Epoch Times article), that quote is recorded as counterpart context for the dyad. It is not scored as author text.

Per item: word count; **humility-statement count**, meaning free-standing sentences of epistemic humility that scope no specific claim ("time will tell"), reported per 1,000 words; and extra-paper category counts.

**Composites (per paper, then author-averaged per the Stage 1 aggregation rule r9).**
- CAL-comm: share of non-forecast claims with O ≥ 1.
- DRIFT: mean Δ over matched claims.
- RETAIN: mean PC-7.
- PROMO: PC-6 count ÷ number of labelled assumptions in the paper.
- FID: PC-8 count ÷ scored claims.
- SEL: defined under HC4.
- XP: extra-paper share, as sentences ÷ total extracted sentences.

## 6. Hypotheses

Direction is stated as contrarian (K) relative to mainstream (M).

- **HC0, propensity (confirmatory, two-sided).** The share of papers with ≥ 1 admissible item differs between groups. No direction is predicted: mainstream authors have institutional press machinery, and contrarian authors have blog and think-tank platforms (pilot inventory). Items per communicating paper and channel mix are reported descriptively. All other HC estimands are **conditional on communicating** and are reported that way.
- **HC4, selection (confirmatory).** Within each communicating paper, the paper-stage overreach of the claims the authors **repeat** in public exceeds that of the claims they **leave out**: SEL = mean O(repeated) − mean O(not repeated), using frozen Stage 1 values. Tested within each group against 0, and between groups (K > M). Because each paper is compared with itself, paper quality and author style drop out. This is the design's strongest inference.
- **HC1, drift.** DRIFT: K > M.
- **HC2, qualifier retention.** RETAIN: K < M.
- **HC3, assumption promotion.** PROMO: K > M.
- **HC5, extra-paper load.** XP: K > M.
- **HC-L, link between stages (two-sided).** The author-level association between Stage 1 CAL and Stage 2 DRIFT:

| Result | Reading |
|---|---|
| Negative or null association, with DRIFT near 0 for K | **Substitution**: the contrarian paper is itself the lay-audience document, and little is left to escalate. |
| Positive association, or DRIFT > 0 for K at moderate CAL | **Two-stage escalation**: hedged where reviewers look, asserted where readers quote from. |

- **HC6, register (exploratory; D6).**
  - HC6a: PC-9a person-directed rate differs by group (two-sided; the pilot found no group difference in total rate but a difference in target).
  - HC6b (relational): within authors, replies inside repeated dyads (≥ 3 exchanges) carry higher person-directed rates than other replies (pilot ratio ≈ 2.5).
  - HC6c (evolution): at the corpus level, register rises over calendar time, estimated with author and dyad effects separated from era (§9).
- **Descriptive (pre-registered, no test).** FID rates by group. The forecast table from the communications (horizon × interval × Δ against the paper's forecast). Humility-statement density.

**Confirmatory status rule.** HC0 and HC4 are confirmatory. HC1–HC3 are **promoted to confirmatory** if, when retrieval is complete and **before any Stage 2 scoring**, each group has ≥ 10 communicating author-clusters with ≥ 1 matched claim. Otherwise they are reported as secondary. The counts are fixed from retrieval metadata alone. HC5 and HC-L are secondary in all cases. HC6 is exploratory in all cases.

## 7. Scoring protocol

- **Scorer and prompt.** The pinned Stage 1 model and version (codebook §10). The prompt contains only this protocol, the paper text, the frozen Stage 1 claim list for that paper, and the communication item in its original language.
- **Runs.** 3 independent runs per item; item-level majority; per-item instability logged (codebook §10). Item order is randomized across papers and groups.
- **Anchors.** Every score carries a verbatim quote of ≤ 25 words in the original language, the item's archive reference, and the matched Stage 1 claim ID or paper anchor.
- **Transcripts** are archived with the Stage 1 transcripts under a `stage2/` subfolder.
- **Legibility.** Stance is plainly legible in public communications, so no blinding is attempted. Codebook §11's framing applies: the defense is auditability.

## 8. Communications in languages other than English

The pilot showed that level-setting words do not map one-to-one across languages. For example, *praktisch nichts* can be "practically nothing" (L4) or "hardly anything" (L3), and *deutlich besser* can be "clearly better" (L4) or "markedly better" (level-neutral). The rules below keep scoring faithful to the original while keeping it auditable by a reviewer who does not read that language.

**8.1 Score the original.** Levels are assigned from the original text using that language's **pinned marker lexicon** (`sources/lexicons/`). Each lexicon is fixed at freeze, alongside the English Hyland lexicon (codebook Appendix C.1), and lists L1–L4 markers, negative universals, level-neutral approximators and degree intensifiers, with rulings for ambiguous words. A language met during retrieval that has no pinned lexicon gets one before any of its items are scored. It is logged as a post-freeze amendment (codebook §15), with a sensitivity analysis that excludes that language.

**8.2 Review packet.** For each non-English item, the pipeline produces a packet (prototype: `pilot/communications/translation-review/rahmstorf-DE_review-packet.md`) containing:
- a full translation of the item into the reviewer's language, labelled as a review aid;
- for each scored claim: the original sentence, a literal gloss with the level-setting markers bracketed, an idiomatic translation, and a **marker note** (the marker, the level assigned, plausible renderings in the reviewer's language, and whether any would change the level);
- a **translation-sensitivity (TS) flag** where a plausible alternative rendering would change the level;
- a **check phrase** (the marker in context) for independent translation.

**8.3 Translator independence.** For every TS-flagged claim, the marker's rendering is checked with a second translation engine from a different provider. If the engines disagree on marker strength, the claim is escalated to native-speaker audit.

**8.4 Native-speaker audit.** This covers all TS-flagged and escalated claims, all PC-8 fidelity errors in the language, and a 10 % random sample of the rest. Auditors see the original, the paper and the protocol, not the scorer's reasoning, and then record agreement.

**8.5 Analysis.** Language is a recorded covariate. Pre-registered sensitivity analyses: (a) English-only; (b) excluding TS-flagged claims; (c) excluding languages without a completed native-speaker audit. Any language filter that affects the groups unequally is reported as such, as the pilot did for German broadcast.

## 9. Analysis plan

- **Same machinery as Stage 1** (codebook §13): author-cluster permutation tests, max-T familywise control **within the Stage 2 confirmatory family**, and cluster-bootstrap CIs for effect sizes. Instability is reported alongside every item-level result.
- **HC4** is a within-paper contrast aggregated to author clusters. The between-group test permutes group labels over clusters.
- **HC-L** uses a cluster-level correlation, with a permutation CI.
- **Conditioning.** Every estimate except HC0 is conditional on communicating. Reports state that the conditioning event (HC0) may itself differ by group.
- **Sensitivity analyses:** program-level ambiguity (§4.2); language (§8.5); Stage 1 errata (§2.2); headline-authorship uncertainty (§3.5); author-led-organization text (§3.3a); ASR-only transcripts (§3.3).
- **Comment-thread stratum (§3.4a).** Analyzed separately from primary items and never pooled into primary composites. Replies are aggregated to author clusters. For register, a mixed model with author and dyad random effects, exchange index and calendar time as fixed effects (HC6b and HC6c) separates relational effects from author baselines and from era.
- **Evolution of the discussion (HC6c).** The Stage 1 window (2003–2013 default) gives little calendar range. Estimating change over time needs an **era-stratified extension** of the communication sample, with the same authors observed across eras where possible (within-author change controls for style), fixed before retrieval. Pilot contrast (2011–12 and 2021, different authors and genres) is illustrative only.

## 10. Human audit

Steve spot-audits a pre-set random 10 % of judgment items against their anchors, plus **all PC-8 fidelity errors** and **all PC-6 promotions**. These are the most consequential flags and the easiest to check. Adversarial audit is invited on the full archive. Non-English items follow §8.4.

## 11. Threats and limitations

1. **Selection into communicating.** Who communicates, and through which channels, differs by group and by era. HC0 measures it, but conditional estimates remain conditional.
2. **Author choice of claims.** Authors choose which claims to repeat, so CAL-comm mixes calibration with selection. DRIFT, RETAIN and HC4 are the cleaner statistics.
3. **Archive asymmetry and attrition.** Contrarian blog content is often preserved by critics and aggregators, while mainstream press material is syndicated. Pages die: 3 of roughly 20 pilot links were dead. Retrieval failures are recorded by group.
4. **Ecosystem editing.** Headlines, press offices and hosts shape public text. §3.3–3.5 limit scoring to author-attributable text, which undercounts ecosystem amplification by design.
5. **Tier inheritance propagates Stage 1 error.** A Stage 1 tier error carries into Stage 2 overreach. Handled by using the frozen audited Stage 1 record plus the errata sensitivity analysis (§2.2).
6. **Program-level attribution** is a judgment call. It is flagged and sensitivity-tested.
7. **Translation.** The §8 safeguards reduce this risk but do not eliminate it. Languages without native auditors are the weakest link.
8. **Scorer bias** (codebook §14.1) applies with more force here, because communications carry overt stance. Mitigations: symmetric definitions, anchors, instability reporting and audit.
9. **Register measurement.** PC-9 is lexicon-based: it misses sarcasm ("I'm shocked"), euphemism and German compounds ("Skeptikerpropagande"), and it over-counts rebuttals of accusations until audited. Rates are comparable within a language, and only approximately across languages.
10. **Retrieval-limited classes.** Social media and untranscribed recordings may be systematically missing for some authors or eras. Missingness is recorded by class and group.

## 12. Versioning and freeze

v0.2 is this draft. Stage 2 v1.0 is frozen **before any confirmatory communication is retrieved**. The frozen items are: this protocol, the retrieval templates, the lexicons for anticipated languages, and the confirmatory-status threshold. The Stage 1 v1.0 freeze and confirmatory scoring precede it (§2.1). Amendments follow codebook §15.

## 13. Decisions

**Decided (2026-09-26).**
- **D2. Social media: included** (§3.3, §3.7).
- **D3. Comment threads: exploratory, scored as a census** (§3.4a). Census rather than a capped sample: a simulated cap of 10 per author per thread kept 30 % of claim-bearing replies and left 1 % of dyads intact (Exhibit 4 Addendum 1 §1.3).
- **D4. Broadcast: transcribed** (§3.3, §3.7).
- **D6. Register: exploratory item PC-9** with pinned lexicon (§5, HC6).

**Open.**
- **D1. Author scope.** Follow r10 once decided. Until then: all authors retrieved, first or corresponding author as primary.
- **D5. Confirmatory threshold** for HC1–HC3 (proposed: ≥ 10 communicating clusters per group).
- **D8 (new). Era-stratified extension** for HC6c: which eras, and whether to follow the same authors across them (§9).
- **D9 (new). PC-10** (endorsement of escalated coverage): keep as exploratory, or drop.
- **D7. Lexicon languages.** Which languages to pin before freeze. At minimum German, since a pilot author communicates publicly in German. Other languages to be decided from the confirmatory sample's author affiliations once the sample is drawn.

## Appendix A. Rule-ID cross-reference to the pilot

Pilot Exhibit 4 and the German review packet used the labels C-1 … C-8. These were renamed PC-1 … PC-8 here to avoid confusion with Index C claim IDs (C1, C2, …) in the Stage 1 exhibits.

| Pilot label | Protocol | Topic |
|---|---|---|
| C-1 | PC-1 | Unit and extraction |
| C-2 | PC-2 | Tier inheritance |
| C-3 | PC-3 | Drift Δ |
| C-4 | PC-4 | Paper vs program attribution |
| C-5 | PC-5 | Extra-paper claims |
| C-6 | PC-6 | Assumption promotion |
| C-7 | PC-7 | Qualifier retention |
| C-8 | PC-8 | Fidelity error |
| (new in v0.2) | PC-9 | Register (a counts, b relational, c counterpart) |
| (new in v0.2) | PC-10 | Endorsement of escalated coverage |

## Appendix B. Record schema (one row per scored claim)

`paper_id, group, author, item_id, item_url, archive_hash, item_type, language, item_date, days_from_pub, claim_text_orig, claim_text_en (review aid), attribution {paper|program|ambiguous}, matched_stage1_id, paper_anchor, level, level_marker_orig, ts_flag, tier, O, delta, pc6, pc7 (NA if no qualifier), pc8, forecast {0/1}, horizon, interval {0/1}, normative {0/1}, run1, run2, run3, majority, instability`

Item-level table: `item_id, paper_id, author, type, language, words, humility_count, xp_sentences, total_sentences, retrieval_status, stratum {primary|reply}, pc10, R1..R5 counts, register_hits_audited, target_P, target_G, target_W`.

Reply table (§3.4a): `reply_id, thread_id, thread_capture {live|archive}, thread_comment_total, author, timestamp, addressee, dyad_id, exchange_index, prior_exchanges_all_threads, days_since_dyad_start`.

Transcript record (§3.3): `item_id, audio_sha256, tool, tool_version, asr_flag, quotes_hand_checked {0/1}`.

## Changelog

**v0.2 (2026-09-26).** Decisions D2, D3, D4 and D6 recorded. Added §3.3a (author-led-organization releases), §3.4a (comment-thread census stratum), retrieval rules for archives, social media and transcription, PC-9 register (a/b/c), PC-10 endorsement, HC6a–c, the mixed-model and era-extension analysis notes, threats 9–10, and new open decisions D8–D9. Basis: Exhibit 4 Addendum 1 (LS11, FR11 re-score) and Exhibit 5 (CN21).

**v0.1 (2026-09-25).** Initial draft. Built from Pilot Exhibit 4 (LS11/FR11 communications), the German review packet, and the stage-separation design set out on 2026-09-25: separate behaviors, a one-way dependency, and the decomposition of public overreach into paper-stage and communication-stage components.
