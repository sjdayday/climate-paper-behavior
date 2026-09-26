# Register and reply-claim data (pilot; protocol v0.2 PC-9, §3.4a)

| File | Contents |
|---|---|
| `units_all.json` | All 343 author units (30 primary items or quotes, 313 replies) with id, paper, side, author, language, type, date, addressee, thread and text |
| `register_units.csv` | Per-unit word count and R1–R5 hit counts (mechanical pass, before audit) |
| `register_hits_audited.csv` | Every hit with its sentence, the mechanical target code, and the audit code (keep/drop, reason, target P/G/W) |
| `dyads.json` | Author→addressee dyads with ≥ 3 exchanges: sequence of hits per exchange, first-half and second-half rates, span, threads |
| `reply_claims_LS11_FR11.json` | Exploratory claim scores for replies (Exhibit 4 Addendum 1 §1) |

Regenerate the mechanical pass with:
`python3 scripts/register_count.py sources/lexicons/register_dismissive_v0.1.json pilot/register/units_all.json <units.csv> <hits.csv>`
The audit codes are in `register_hits_audited.csv` and are not regenerated.
