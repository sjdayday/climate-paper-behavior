# Translation Review Packet: Rahmstorf, German-Language Communications on F&R11

**Purpose.** This packet lets a reviewer who does not read German audit Index C scoring of German-language communications. It is the prototype for the non-English branch of the automated communication stage.
**Scope.** Stefan Rahmstorf's in-window (2011-09-06 → 2012-12-06) public statements about Foster & Rahmstorf (2011) in German.
**Scorer.** Claude, 2026-09-25. Scoring was done on the German originals. The translations are for review only.
**Companion files.** Originals: `../sources/2011-12-08_klimalounge_globale-temperatur-reloaded_DE.txt`, `../sources/2012-09-27_klimalounge_populaerste-trickgrafik_DE.txt`. Paper-side scores: `../../pilot-exhibit-2_FR11.md`. Communication scores: `../pilot-exhibit-4_public-communications_LS11-FR11.md`, which this packet revises (§5).

---

## 1. Review protocol (proposed for the automated stage)

1. **Score the original, never the translation.** Level-setting words do not map one-to-one across languages. In this record, *praktisch nichts* can become "practically nothing" (a negative universal, L4) or "hardly anything" (L3). *Deutlich besser* can become "clearly better" (booster, L4) or "markedly better" (degree, level-neutral). A score built on a translation would inherit whichever rendering the translator happened to choose.
2. **For each scored claim, give the reviewer four things:**
   - the original sentence;
   - a literal gloss that keeps German word order and brackets the epistemic markers, so the reviewer can see which word carries the level;
   - an idiomatic translation;
   - a marker note naming the German marker, the level it was scored at, the plausible English renderings, and whether any of them would change the level.
3. **Flag translation sensitivity** wherever the level would change under a plausible alternative rendering (**TS = yes**). These items get the reviewer's attention first.
4. **Separate translator from scorer.** A model that translates and then scores its own translation can make correlated errors. For TS-flagged items, the reviewer (or the pipeline) runs the original sentence through a second, independent translation engine (DeepL, Google Translate) and checks how that engine renders the marker. Each marker note below has a "check phrase" for that purpose. If the engines disagree on marker strength, the item is escalated.
5. **Run a native-speaker audit** on every TS-flagged item plus a 10 % random sample of the rest. This matches the §10 spot-audit rate, applied per language.
6. **Pin a lexicon per language.** Codebook §4.2 enumerates English markers and defers to the Hyland lexicon at freeze. Each scored language needs its own pinned marker list, fixed before scoring. §4 gives a German starter list, built from the decisions made here.

## 2. Record located

| Item | Date | Status |
|---|---|---|
| KlimaLounge, "Globale Temperatur Reloaded" | 2011-12-08 | In window. Scored (§3.1). |
| KlimaLounge, "Die populärste Trickgrafik der Klimaskeptiker" | 2012-09-27 | In window. Scored (§3.2). |
| KlimaLounge posts citing F&R11: "Globale Temperatur 2012" (2013-01-20), "Beam me up, Scotty!" (2013-08-20), "Das globale Temperatur-Puzzle" (2013-12-16), "Purzelnde Rekorde" (2014-12-10), "Keine Pause, nirgends" (2015-05-15) | 2013–2015 | Out of window. Relevant to Index A (post-publication conduct). The 2013-08-20 post restates the F&R11 inference about the slower recent trend and cites Kosaka & Xie (2013) as confirming it. |
| German broadcast (ARD Morgenmagazin, Deutschlandfunk, RBB) | 2011 | No transcript located. In-window status and topic unverified. |
| Süddeutsche Zeitung article linked from the 2011-12-08 post | 2011-12 | Link dead (redirects to SZ home). Not recovered. |

## 3. Scored claims

Level codes and tiers follow codebook v0.2. Counterparts are claims in Exhibit 2 or passages in the F&R11 text. **TS** = translation-sensitive.

### 3.1 KlimaLounge, 2011-12-08

**Excluded, with reasons.** Methods descriptions ("Durch eine Korrelationsanalyse filtern wir den Effekt … heraus"). Statements about other analyses: BEST data "zeigen … keinerlei Anzeichen für eine rezente Verlangsamung" is about Berkeley Earth and Open Mind, and "Dabei stellten wir fest, dass es mitnichten eine Pause … gibt" refers to an earlier KlimaLounge analysis, not F&R11. Restatements of the WMO.

**FR1**
- DE: "Zum Trend tragen diese praktisch nichts bei"
- Gloss: To-the trend contribute these [practically] [nothing]
- EN: "These contribute practically nothing to the trend."
- Marker: *nichts* is a negative universal, and *praktisch* is an approximator, which never changes the level. So **L4**.
- Alternatives: "virtually nothing" gives L4. "Hardly anything" or "very little" gives L3, which would **change the level. TS = yes.** Check phrase: *praktisch nichts*.
- Counterpart: body/fig. 7 ("effects of volcanic eruptions and of ENSO are very short-term and that of solar variability very small") at L3. Tier T3. **O = 0, Δ = +1.** (Exhibit 4 scored this L3; revised in §5.)

**FR2**
- DE: "wenn man diese Schwankungen herausrechnet, stimmen die fünf Datenreihen deutlich besser überein als vorher"
- Gloss: if one these fluctuations calculates-out, agree the five data-series [markedly] better than before
- EN: "if these fluctuations are removed, the five series agree markedly better than before"
- Marker: *deutlich* here is a degree intensifier on "better", not an epistemic booster. So **L3**.
- Alternatives: "clearly better" would trigger the English booster rule and give **L4. TS = yes.** Check phrase: *deutlich besser*.
- Counterpart: F12/fig. 5 at L3. Tier T3. **O = 0, Δ = 0.**

**FR2b** (new; missed in Exhibit 4)
- DE: "Das liegt daran, dass die Unterschiede zwischen den Datenreihen nicht im Klimatrend liegen sondern in den kurzfristigen Schwankungen."
- EN: "This is because the differences between the series lie not in the climate trend but in the short-term fluctuations."
- Marker: unhedged declarative, **L3**. TS = no.
- Counterpart: F1/F3 (paper body: all five raw trends agree within errors). Tier T3. **O = 0, Δ = 0.** Rahmstorf's English IOP quote (FP2) makes the same claim hedged with "to a large extent"; the German version has no hedge. C-7 is defined against the paper, which has no directly matching sentence, so this is noted rather than scored.

**FR3**
- DE: "So fällt z.B. die Reaktion auf ein El Niño Ereignis in den Satellitendaten (rot und orange) rund doppelt so stark aus wie in den Bodendaten."
- EN: "For example, the response to an El Niño event is roughly twice as strong in the satellite data as in the surface data."
- Marker: *rund* is an approximator. **L3.** TS = no.
- Counterpart: F3 at L3. Tier T3. **O = 0, Δ = 0.**

**FR4**
- DE: "So ist in allen fünf Datenreihen selbst der Erwärmungstrend ab dem Jahr 2000 statistisch signifikant, und die beste Schätzung für diesen Trend liegt in allen Datenreihen sehr nah am Langzeittrend seit 1979"
- EN: "In all five series even the warming trend since 2000 is statistically significant, and the best estimate of this trend is in all series very close to the long-term trend since 1979."
- Marker: two claims in one sentence; the strongest, "ist … statistisch signifikant", is **L3**. TS = no.
- Counterpart: body/fig. 6. Tier T3. **O = 0.** (Exhibit 4 scored this sentence at the hedged half, L2; revised in §5.)

**FR5**
- DE: "Also auch hier keinerlei Hinweise auf eine Verlangsamung oder gar Pause in der globalen Erwärmung."
- Gloss: So also here [none-whatsoever] indications of a slowdown or even pause in the global warming
- EN: "So here too, no indication whatsoever of a slowdown, let alone a pause, in global warming."
- Marker: *keinerlei* is an emphatic negative universal. **L4.**
- Alternatives: "no indication(s)", "no sign at all". All are negative universals, so L4 either way. TS = no. Check phrase: *keinerlei Hinweise*.
- Counterpart: F10 at L4. Tier T3. **O = 0, Δ = 0.** C-7: the paper's "beyond the variability induced by these known natural factors" is not carried over, although the sentence follows the adjustment discussion directly. C-7 = 0, marginal.

**FR6**
- DE: "In allen fünf Datenreihen sind die beiden wärmsten Jahre 2009 und 2010."
- EN: "In all five series the two warmest years are 2009 and 2010."
- **L3.** Counterpart F5 at L3. Tier T3. **O = 0, Δ = 0.** The paper specifies the *adjusted* series; this sentence follows the discussion of removing fluctuations, so the context carries the qualifier.

**FR9** (new)
- DE: "Die WMO erwartet aufgrund des kühlenden Effekts von La Niña im Pazifik, dass das Jahr 2011 relativ kühl wird – konsistent mit der Analyse in unserem Paper."
- EN: "Because of La Niña's cooling effect in the Pacific, the WMO expects 2011 to be relatively cool, consistent with the analysis in our paper."
- Scored: the consistency clause only (the WMO expectation is a restatement). Marker: *konsistent mit* = "consistent with", **L2**. TS = no.
- Tier T3 (ENSO coefficients). **O = 0.**

### 3.2 KlimaLounge, 2012-09-27

**Excluded.** Claims about Rahmstorf's own replacement graphic ("Die Trends der CO2- und Temperatur-Kurven stimmen erstaunlich gut überein"); IPCC forcing figures; claims about Watts and Vahrenholt, logged as extra-paper (C-5).

**FR7a**
- DE: "Die von Watts gezeigten satellitenbasierten Troposphärentemperaturen zeigen übrigens praktisch den gleichen Erwärmungstrend wie die von den Wetterstationen gemessenen bodennahen Temperaturen (in beiden Fällen 0,17 °C pro Jahrzehnt über die letzten 30 Jahre)."
- EN: "The satellite-based troposphere temperatures shown by Watts, incidentally, show practically the same warming trend as the near-surface temperatures measured by weather stations (0.17 °C per decade over the last 30 years in both cases)."
- Marker: *praktisch* is an approximator. **L3.** TS = no.
- Counterpart: F1/Table 1 (raw trends 0.014–0.018 K/yr). Tier T3. **O = 0.**

**FR7b** (Exhibit 4's FR7, rescored)
- DE: "Allerdings ist die Variabilität bei den Troposphärendaten wesentlich größer, insbesondere die Reaktion auf El Niño (wie 1998) und die Sonnenzyklen (wir zeigen das in Foster & Rahmstorf, ERL 2011)."
- EN: "However, variability in the troposphere data is substantially larger, especially the response to El Niño (as in 1998) and the solar cycles (we show this in Foster & Rahmstorf, ERL 2011)."
- Marker: unhedged declarative with "wir zeigen" ("we show"), **L3**. *Wesentlich* is a degree intensifier, level-neutral. TS = no.
- Content check against the paper: the El Niño part is supported (F3, T3). The **solar** part is not. The paper states: "The response to solar variations is less pronounced, and the difference between LT and surface response is not statistically significant." The only support for a larger solar response is a non-significant point estimate, so tier ≤ T1. The paper's own significant finding for LT is **volcanic** response (F3), which the post leaves out.
- **O = 1.** Also flagged as a **fidelity error**: the communication attributes to the paper a finding the paper explicitly reports as not significant. Proposed item C-8 (§5).

**FR8** (unchanged from Exhibit 4)
- DE: "Die natürlichen Einflüsse (Vulkane, Sonnenzyklen) auf den Trend sind verschwindend gering im Vergleich zum anthropogenen CO2 (siehe z.B. Lean & Rind 2008, Foster & Rahmstorf 2011)."
- Gloss: The natural influences (volcanoes, solar-cycles) on the trend are [vanishingly small] in comparison to the anthropogenic CO2
- EN: "The natural influences (volcanoes, solar cycles) on the trend are vanishingly small compared with anthropogenic CO2 (see e.g. Lean & Rind 2008, Foster & Rahmstorf 2011)."
- Marker: *verschwindend gering* ("vanishingly small", "negligible") is an evaluative magnitude term, not an epistemic booster. **L3.**
- Alternatives: "negligible" or "vanishingly small" both give L3. "Practically zero" would read as an approximator plus a universal, and **L4** under a literal application of the English rules. TS = yes (low). Check phrase: *verschwindend gering*.
- Tier: T0 for the CO2 comparison. F&R11 isolates the trend "whatever its cause" and hedges the attribution ("most likely these are exclusively anthropogenic", L2). **O = 2, Δ = +1** (judgment log 5 in Exhibit 4 still applies).

**Totals for Rahmstorf's German record.** 11 claims scored, 2 overreaching (FR7b, FR8). Three items are translation-sensitive (FR1, FR2, FR8). In all three the level was set from the German. Under the English-rendering alternatives, FR1 and FR2 would have moved by one level; because they sit at T3, O would not change.

## 4. German marker lexicon (starter list, to be pinned at freeze)

| Level | Markers (examples) |
|---|---|
| L1 | vielleicht, möglicherweise, eventuell, könnte, mag sein, wir vermuten |
| L2 | wahrscheinlich, vermutlich, dürfte, deutet darauf hin, scheint, legt nahe, konsistent mit, wir schätzen, beste Schätzung, wir argumentieren |
| L3 | unhedged declaratives: ist/sind, zeigt, wir zeigen, wir finden, belegt (*see note*) |
| L4 | eindeutig, zweifellos, zweifelsfrei, klar (epistemic use), offensichtlich, in der Tat, tatsächlich (emphatic), beweist, bewiesen; negative universals: kein … (unhedged), keinerlei, nichts, nie, mitnichten, keineswegs |
| Level-neutral | approximators: praktisch, rund, etwa, ca., nahezu, fast, ungefähr; degree intensifiers: deutlich (comparative/degree use), wesentlich, erheblich, stark |

Notes. **deutlich** is level-neutral as a degree modifier ("deutlich besser", "deutlich wärmer") and **L4** as an epistemic adverb ("zeigt deutlich, dass …" = "clearly shows that"). The rule is decided by syntax: modifying an adjective or comparative means degree, and modifying a verb of showing or knowing means epistemic. **belegt** ("demonstrates, documents") sits between L3 and L4 and needs a ruling. **tatsächlich** is ambiguous between "actually" (L3) and "indeed" (L4).

## 5. Revisions to Exhibit 4 arising from this packet

| Item | Exhibit 4 | Revised | Reason |
|---|---|---|---|
| FR1 | L3, O 0 | **L4**, O 0, Δ +1 | *nichts* is a negative universal; *praktisch* is an approximator (level-neutral). The original English gloss "practically nothing" was right, but its level was not applied. |
| FR4 | L2, O 0 | **L3**, O 0 | Strongest-claim rule: "is statistically significant". |
| FR7 | O 0 | **FR7a (L3, O 0) + FR7b (L3, T≤1, O 1)** | FR7b's solar claim contradicts the paper. This was missed because level was checked but content was not. **It was not a translation error.** |
| FR2b, FR9 | not extracted | added, O 0 | Missed in the first pass. |
| **F&R11 totals** | 19 claims, CAL 0.053 | **22 claims, 2 overreaching, CAL = 0.091**; mean O = 3/22 = 0.14 | Alternative FR8 reading: CAL = 0.045 |

**Proposed C-8, fidelity error (0/1).** The communication attributes to the paper a finding the paper does not report, or reports as not significant. This is separate from overreach: FR7b's certainty level is modest (L3), but the content is wrong about the paper. Like C-7, it is mechanical once claims are matched, and it applies to both sides.

**Lesson for the automated stage.** Both of the substantive F&R11 problems (FR7b, FR8) are in German, and the first pass scored one of them wrong. The cause was a missing content check, not the translation. The English-only filter would have hidden both.

## Appendix: Full English translations (review aid; the German originals are authoritative)

### A.1 "Globale Temperatur Reloaded" (KlimaLounge, 2011-12-08, Stefan Rahmstorf)

There are three interesting pieces of news about global temperature: an entirely new dataset, a new analysis of the five established data series, and a first estimate of the value for 2011.

When, a year and a half to two years ago, a wave of attacks on climate research rolled through the blogs (alleged scandals such as "Climategate", "Amazongate", "Africagate" etc.) and from there also spilled into the mainstream media, the core issue was the reliability of the statements of the "climate council" IPCC and of the data on global temperature evolution (see e.g. the KlimaLounge commentaries here, here and here). The allegations of scandal and manipulation were thoroughly investigated and soon turned out to be false. Nevertheless, science analysed the events intensively and self-critically and drew consequences, e.g. in the form of a series of reforms of the IPCC. A number of media outlets also later took a self-critical look back at the allegations and found that there was practically nothing to them, e.g. the Frankfurter Rundschau, the Berlin tageszeitung and DIE ZEIT. (That there are also journalists who respond to criticism by suing or defaming is noted here only in passing; nuanced commentary on this can be found, among other places, here and here.)

But one aspect of the reckoning was still outstanding: how reliable are the global temperature data after all? In the Berkeley Earth Surface Temperature (BEST) project, an entirely new global temperature dataset was produced by scientists who previously had nothing to do with climate research and who had positioned themselves beforehand as decidedly sceptical of global warming. In addition, the project was partly funded by the oil industry (more background e.g. at BBC Online). The result for the global temperature evolution over land is now available. What should not have surprised any climate researcher, but evidently did surprise the scientists involved: once again it comes out pretty much exactly the same as the already existing datasets (see graphic). The physicist and project leader Richard Muller commented:

> Our biggest surprise was that the new results agreed so closely with the warming values published previously by other teams in the US and the UK.

For me this is a nice example of how science should work and, fortunately, usually does work: whatever prejudices the researchers involved may have had and whoever paid for the whole thing, the result is independent of it.

(Graphic reproduced with permission of BBC Online)

The graphic also shows that the new BEST data lie considerably closer to those of NASA GISS and NOAA than to the HadCRU data, which are somewhat cooler at the end — a discrepancy we have discussed earlier, among other places here. There we found that there is by no means a pause in global warming (which a news magazine at the time promptly dismissed as "black arithmetic"). The new BEST data, incidentally, also show no sign whatsoever of a recent slowdown of climate warming, which is brought up again and again in the media (this is shown in detail at Open Mind).

That brings us to the second topic: Environmental Research Letters has just published a paper by the statistician Grant Foster and me, in which we analyse the five available data series of global temperature (land + ocean) since 1979. Through a correlation analysis we filter out the effect of the three known short-term factors of fluctuation: El Niño, solar activity and volcanic eruptions. These contribute practically nothing to the trend, but if one removes these fluctuations, the five data series agree markedly better than before (see next graphic). This is because the differences between the data series lie not in the climate trend but in the short-term fluctuations. For example, the response to an El Niño event is about twice as strong in the satellite data (red and orange) as in the surface data. If these fluctuations are taken out, the differences between the data series therefore also shrink.

Because of the smaller year-to-year fluctuations, one can now also compute statistically significant trends over shorter periods. Thus in all five data series even the warming trend since 2000 is statistically significant, and the best estimate of this trend lies in all data series very close to the long-term trend since 1979 (Fig. 6 of the paper). So here too, no indication whatsoever of a slowdown, let alone a pause, in global warming. In all five data series the two warmest years are 2009 and 2010.

A first preview of the annual value for 2011 was meanwhile provided a few days ago by the World Meteorological Organization, WMO, in its provisional status report on the global climate in 2011 (see next graphic).

Because of the cooling effect of La Niña in the Pacific, the WMO expects the year 2011 to be relatively cool, consistent with the analysis in our paper. Relatively means that it should nonetheless still rank among the ten warmest years since records began. And it will apparently be the warmest La Niña year so far; those are the blue years in the graphic above.

*Update 16 Dec.:* A reader asked for comment on Durban. I recommend Mr Schellnhuber's FAZ interview: "The world map of climate protection has changed."

*Update 19 Dec.:* Since a fair amount of serious discussion has now been added regarding my "Africagate" criticism, to which I briefly alluded in the article above, a few links are collected here: Climate researcher Wolfgang Cramer, author of a PNAS article on the subject, analyses the scientific background on African drought risks and the recent media echo in the Vielfalter blog. The Heidelberg astrophysicist Markus Pössel examines, in "Rahmstorf in a distorting mirror", how the Spiegel Online story on the subject was constructed. In a second part he then goes into the scientific questions behind the whole story, and how these were presented in the articles by Irene Meichsner and Markus Lehmkuhl. The linguist Anatol Stefanowitsch discusses some interesting linguistic aspects and compares Meichsner's article with her two sources in "Copied without criticism?". The statement of the Potsdam Institute can be found here.

*Literature:* G. Foster and S. Rahmstorf, "Global temperature evolution 1979–2010", Environmental Research Letters, vol. 6, 2011, 044022. *Press on the paper:* Süddeutsche Zeitung; New Scientist; Washington Post.

### A.2 "Die populärste Trickgrafik der Klimaskeptiker" ["The climate sceptics' most popular trick graphic"] (KlimaLounge, 2012-09-27, Stefan Rahmstorf)

Probably the most popular deceptive graphic of the climate sceptics is the "world climate widget" of the US blogger Anthony Watts. We put it under the magnifying glass and show what the graphic would look like if done correctly.

The so-called "climate sceptics" have an arsenal of misleading graphics with which the human influence on climate is to be played down (two examples). Particularly widespread is the following image, which, regularly updated, is reproduced on many climate-sceptic websites.

*[Caption:] The "world climate widget" of US climate sceptic Anthony Watts, with our annotations (green). The original can be found on Watts' blog.*

What would a serious overview of temperature, CO2 and sunspots look like?

1. One should use annual values of near-surface air temperature. These are relevant to us humans; we do not live somewhere higher up in the troposphere. The satellite-based troposphere temperatures shown by Watts, incidentally, show practically the same warming trend as the near-surface temperatures measured by weather stations (0.17 °C per decade over the last 30 years in both cases). However, variability in the troposphere data is substantially larger, especially the response to El Niño (as in 1998) and the solar cycles (we show this in Foster & Rahmstorf, ERL 2011). Amid all the noise the trend is visually less apparent, especially if one also shows monthly rather than annual values. So we take the well-known dataset of global annual temperatures from NASA's Goddard Institute for Space Studies. (More on global temperature data at Spektrum.de.)

2. For a serious comparison with the temperature data, the scale of the CO2 data must be chosen correctly, so that it corresponds to the CO2 effect actually predicted by climate research. One can calculate this in a complicated way with a climate model, but one can also do a simple back-of-the-envelope calculation. The result: a CO2 rise from 280 to 380 ppm (corresponding to 1.7 watts per square metre of radiative forcing) leads immediately to about 0.8 degrees of global warming ("immediately" because there is later a time-delayed lag, but here we are comparing temperature and CO2 at the same time). This is worked out, e.g., in our book *Wie bedroht sind die Ozeane* (page 111).

In our graphic, therefore, for a serious comparison 100 ppm CO2 on the right axis must correspond to 0.8 degrees on the left axis. This also corresponds to the best IPCC estimate of the "Transient Climate Response" (TCR) of 2.1 °C at the time of CO2 doubling, since 2.1 °C for a 280 ppm rise again gives 0.8 °C per 100 ppm, see IPCC ch. 9.6.2.3. The TCR is smaller than the climate sensitivity (best estimate 3 °C for CO2 doubling), because warming takes time and "lags behind" the later equilibrium value.

We show the annual values of the famous CO2 measurement series on Mauna Loa in Hawaii, which began in 1958.

3. And finally, one should honestly show the time series of sunspots (also annual values) and not just a snapshot. Here too the question of correct scaling arises (even if it is not so important, since solar activity shows only cycles and no appreciable trend). We choose the scaling that, according to the correlation analysis of Lean and Rind (2008), corresponds to the effect on global temperature actually detectable in the data, i.e. an amplitude of the sunspot cycle of about 0.05 °C. (More on the sun's influence on temperature at Spektrum.de.)

And this is what the picture then looks like:

*(Graphic: Prof. Stefan Rahmstorf, Creative Commons BY-ND)*

The trends of the CO2 and temperature curves agree astonishingly well. Astonishing because CO2 is not the only factor influencing temperature. This agreement has two reasons:

(1) The other anthropogenic influences are partly warming (other greenhouse gases such as methane), partly cooling (air pollution through aerosols). The two roughly balance. (The IPCC report gives the anthropogenic radiative forcing of CO2 alone as 1.7 W/m², that of all anthropogenic factors combined as 1.6 W/m².)

(2) The natural influences (volcanoes, solar cycles) on the trend are vanishingly small compared with anthropogenic CO2 (see e.g. Lean & Rind 2008, Foster & Rahmstorf 2011).

The short-term temperature fluctuations around the trend naturally have other causes and have nothing to do with CO2; I have explained them in more detail here.

It takes quite something to make, from the data shown, a graphic that deceives the layperson into believing that CO2 is unimportant and the sun important for the global temperature evolution over the last sixty years! Anyone peddling this graphic has taken leave of any serious factual discussion and taken the path of deception.

And who is energetically spreading Anthony Watts' dubious trick graphic in Germany? It is the former RWE manager Fritz Vahrenholt, on whose *Kalte Sonne* home page this graphic is permanently displayed at the top. The layperson is amazed and the expert wonders: how can someone who presents himself as a scientist ("I am a professor of chemistry!") work with such con-man tricks? And how can someone who works with such con-man tricks (it is by no means the only one) be appointed to the steering committee for a climate report of the technology academy Acatech?

P.S. Mr Vahrenholt now has a good opportunity to prove that he is using this misleading graphic not deliberately but only out of ignorance of the basic climate data. He should immediately replace the Watts graphic with our serious presentation of the data curves. We will gladly provide it (Creative Commons, see above). We are encouraged by the fact that after our most recent post Vahrenholt corrected his false claim that this year's record minimum of Arctic sea ice was only 2 % below that of 2007.

*Update 28 Sept.:* I just stumbled across a fitting quotation, from a speech this week by US Congressman Ed Markey on the 50th anniversary of the publication of Rachel Carson's *Silent Spring*: [English in original] "Rachel Carson was attacked by the chemical industry using a playbook that the tobacco industry first developed: Discredit the messenger, foster doubt and denial about the science, and call for additional research. Whether it's harmful chemicals, tobacco use, or climate science, all too often the affected industries employ a three-D strategy: discredit, deny, and delay." Perhaps it reminds Mr Vahrenholt of his youth (Seveso is everywhere).

*Update 30 Sept.:* One of our readers, Bernd Herd, has programmed a widget from the graphic above that can be resized and is transparent, so it can be placed on any background. See his comments here and here. This is how blogging creates real added value; many thanks for that!

*On our own account:* the day before yesterday our book *Wolken, Wind & Wetter* was named Environment Book of the Year 2012 by the Deutsche Umweltstiftung!
