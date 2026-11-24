# Data extraction codebook (v1.0)

Two linked tables, as in the misophonia and sports-betting reviews. `samples.csv` has one row per independent sample of people who use kratom. `estimates.csv` has one row per case definition × sample × subgroup (all, male, female, use frequency). Unknown = `NR` (not reported); not applicable = `NA`. The form is deliberately short: only the fields the analyses in protocol §15 use.

**Procedure (protocol §11c).**
- The AI assistant pre-fills every field from the full text with the source location (page, table or figure) and a short quote. The draft is stored unchanged in `extraction/draft/`.
- R1 verifies every field against the source in Markdown files (`extraction/verify_md.py`) and accepts or corrects it. The verified values go to `samples.csv` and `estimates.csv`.
- Fields marked **[K]** are key fields: R1 always checks them against the source table or text.
- The share of AI-drafted values that R1 corrected and the share of AI quotes found verbatim in the source are reported.
- The form is piloted on three studies before use. Any rule added in the pilot goes to `deviations.md` with a date.

## samples.csv

| Field | Rule |
| --- | --- |
| `sample_id` | `S###`; one per independent sample of people who use kratom |
| `study_id` | `ST###`; links multiple samples and reports |
| `report_ids` | `rec_id`s of all reports of this sample, `;`-separated; the first one supplies data |
| `first_author`, `year`, `doi` | of the main report |
| `pub_status` | journal / preprint / thesis / conference / report / other |
| `language` | language of the full text |
| `country` | ISO 3166 alpha-3; multi-country samples: `MULTI` + list in `notes` |
| `region` **[K]** | Southeast Asia / North America / Europe / other (filled from country) |
| `data_years` | years of data collection, e.g. `2021-2022`; `NR` |
| `design` | cross-sectional / cohort baseline / prevalence survey / validation study / laboratory or EMA study / other |
| `sample_type` **[K]** | community_users (people who use kratom recruited in villages, households, community settings) / online_consumers (online or social-media samples of kratom consumers) / drug_users (people who use other drugs, not in treatment) / treatment_other_sud (patients in treatment for another substance, e.g. methadone) / psychiatric_patients / students_youth / population_subsample (kratom users within a probability survey) / other |
| `sampling` **[K]** | probability / census / respondent-driven / snowball / convenience (community) / online opt-in / clinical consecutive / NR |
| `recruitment_channel` | advocacy or vendor channels (e.g. kratom advocacy groups, vendor mailing lists) / general / clinical / NR |
| `use_period` **[K]** | reference period for being a person who uses kratom: past 30 days / past 12 months / lifetime regular / lifetime any / current (unspecified) / NR |
| `regular_use_required` | yes (with the stated rule, e.g. `daily for >= 6 months`) / no |
| `product_form` | traditional leaf (chewed, tea, boiled decoction) / kratom cocktail / commercial powder or capsules / extracts or 7-OH products / mixed / NR |
| `n_users` **[K]** | number of people who use kratom analysed = denominator of the main estimate |
| `response_rate` | as reported, or n responded / n invited |
| `age_mean`, `age_sd` | years, of the kratom users if reported, else of the whole sample (say which in `notes`) |
| `pct_male` | 0–100 |
| `pct_other_opioid_use` | share with current non-prescribed opioid use or opioid use disorder, if reported |
| `instruments` | all dependence or use-disorder measures used, `;`-separated, with language version |
| `industry_funding` | yes (kratom vendor or advocacy organisation) / no / NR |
| `jbi_1` … `jbi_9` | yes / no / unclear / NA (see `rob_jbi.md`) |
| `jbi_notes` | one line per item rated no or unclear |
| `notes` | anything else |

## estimates.csv

| Field | Rule |
| --- | --- |
| `estimate_id` | `E####` |
| `sample_id` | link |
| `subgroup` | all / male / female / daily users / non-daily users / other (state which) |
| `instrument` **[K]** | short name as in `instrument_thresholds.csv` (DSM-5-SUD, DSM-IV, ICD-10, ICD-11, interview, KDS, SDS, ASSIST, adhoc) |
| `threshold` **[K]** | exactly as applied, e.g. `DSM-5 criteria>=2`, `DSM-IV dependence`, `KDS>=X`, `ASSIST>=27`, `MINI 7.0` |
| `threshold_source` | standard / validation paper / study's own / percentile of this sample (→ E3, not pooled) |
| `author_label` | authors' wording, e.g. "kratom use disorder", "moderate", "dependent" |
| `level` **[K]** | L1 / L2 / L2-scale / L2-screen / L3 / adhoc by the levels table (`instrument_thresholds.csv`), whatever the authors' label |
| `cumulative` | yes = "this category and above"; no = a single category (mild only, moderate only). Single categories are summed into cumulative levels at analysis |
| `time_frame` | past 12 months / lifetime / NR |
| `cases` **[K]** | integer; if only a % is given: round(% × n / 100), and `derived = yes` |
| `n` **[K]** | denominator for this estimate (people who use kratom) |
| `derived` | yes / no |
| `primary_for_authors` | yes, if the authors call this their main estimate |
| `location` | page, table or figure where the numbers are |
| `notes` | |

## Extraction rules

- **Kratom users as a subgroup.** When a study of drug users, patients or students reports dependence for those who use kratom, the denominator is the number who use kratom in the period. If dependence is reported only for the whole sample (including non-users), the estimate is not eligible (E2).
- **DSM-5 categories.** Extract every severity category reported (mild, moderate, severe, none). Cumulative levels are built at analysis: L1 = mild+, L2 = moderate+, L3 = severe.
- If counts in the text and a table disagree, take the table and note it.
- **Waves of one cohort:** the first wave with a dependence measure enters; later waves are noted only.
- **Overlap:** samples reported in several papers (common in Malaysian community studies) are linked by site, years and n; the most complete report supplies the data.
