# Dismissive-register lexicon: v0.1 (pilot; protocol PC-9)

Machine-readable file: `register_dismissive_v0.1.json`. Counting script: `scripts/register_count.py`.
Audited pilot output: `pilot/register/`.

## Categories

| Code | Category | English examples | German examples |
|---|---|---|---|
| R1 | Group labels and epithets | denier, alarmist, warmist, "fake skeptics", cult, cyclomania | Klimaleugner, Alarmist, sogenannte „Klimaskeptiker“ |
| R2 | Competence disparagement | stupid, ignorant, "you don't understand", "did you even read", "rank beginner", sophist | dumm, Unkenntnis, ahnungslos |
| R3 | Motive and honesty attribution | dishonest, fraud, trick, hoodwinked, agenda, propaganda, censorship, "blatant untruth", "desperate to deny" | Täuschung, Trick(grafik), Bauernfängertricks, unseriös, irreführend, vorgaukeln |
| R4 | Ridicule and profanity | nonsense, absurd, childish, "is this a joke", "stay classy", bullshit | Unsinn, Schwachsinn, lächerlich |
| R5 | Exclusion and admonition | "you won't be missed", "control yourself", "be more humble", "get a grip" | „aus jeder ernsthaften Sachdiskussion verabschiedet“ |

## Counting rules (v0.1)

1. Quoted spans longer than 3 words (someone else's words) are removed first. Short scare quotes stay.
2. R2 "know/understand" patterns are skipped when the subject is *I* or *we*, or is omitted. Self-hedging ("I do not know the mechanism") is the opposite of dismissive.
3. Identical sentences within a unit (page titles, breadcrumbs) count once.
4. Every hit is audited: **keep** or **drop**, with a reason. Pilot drop reasons: self-reference, rebuttal of an accusation ("Are you implying that we lied?"), reporting an accusation, negation ("far from alarmist"), quoted scripture, generic hypothetical, a term mentioned in scare quotes, page furniture.
5. Each kept hit gets a **target**: **P** (named or addressed person), **G** (group or institution), **W** (work or argument). The mechanical first pass codes P if the sentence addresses "you" or names the addressee, G if it has a collective noun or pronoun, and W otherwise. The audit corrects this.

## Pilot performance

144 raw hits, of which 121 are true positives (84 % precision after the v0.1 fixes; see the JSON notes). False negatives are unmeasured. Known misses: sarcasm without lexical markers ("I'm shocked", "Not."), euphemism, German compounds.

## Before pinning

- Measure recall on a hand-coded sample, stratified by author and language.
- Add a German decompounding step (for "Skeptikerpropagande"-type compounds).
- Decide whether evaluative work-terms ("flawed", "failed") belong in R4 or stay out. They are frequent on both sides and aimed at work, not people.
- Add lexicons for other D7 languages.
