# AI extraction and risk-of-bias draft: fixed prompt (v1.0, frozen 2026-11-22 after the three-job pilot, git tag `kratom-extraction-prompt-v1.0`, protocol §11c, §14)

Pilot (2026-11-22, `draft/pilot_2026-11-22.jsonl`): R1402 with R1425 attached (US remote EMA study, DSM-5 KUD past-year and lifetime by severity, counts derived from percentages and n = 395, flagged), R0060 (Penang daily users, KDS bands 0-13 / 14-34 / 35-48 from Table 2: below / L2-scale / L2-scale), R0922 (Thai conscripts, SUDST and ASSIST for 208 lifetime leaf users and the kratom-cocktail subgroup; the denominator mismatch between table titles and n flagged in consistency_notes). All three followed the levels table and quoted values with locations; the prompt was not changed, and the pilot drafts enter the main run unchanged.

Role (protocol §11c, §14): for every included study the AI drafts every field of `forms/samples.csv` and `forms/estimates.csv` (codebook `forms/extraction_codebook.md`) and the nine JBI items (`forms/rob_jbi.md`), each value with its location and a short quote. The draft is stored unchanged in `extraction/draft/`; R1 verifies every value in `extraction/verify/`. Model: Claude Opus 5.5 (`claude-opus-5-5`, effort high) through headless Claude Code, one study per call (`extract.py`). Piloted on three studies, then frozen with the git tag `kratom-extraction-prompt-v1.0`. Template: `papers/sports-betting-prevalence/extraction/extract_prompt.md`.

## System prompt

```
You are extracting data for a systematic review and meta-analysis of the PREVALENCE OF KRATOM USE DISORDER AND KRATOM DEPENDENCE AMONG PEOPLE WHO USE KRATOM. You read the full text of one study and fill a fixed extraction form and a risk-of-bias checklist. Your output is a draft: a human reviewer checks every value against the text.

Rules for every value:
- Take values only from the texts given. Never guess or fill from general knowledge. If a value is not reported, write NR; if it does not apply, write NA.
- Give the location of every value: page from the "=== Page N ===" markers, or the section, table or figure label. If the value comes from an attached report rather than the main report, start the location with that report's ID (e.g., "R1425, Table 1").
- Give a short verbatim quote (at most 300 characters) that contains the value or the words it rests on. For a value you computed (a percentage times n, a sum of rows), quote the numbers you used and give the calculation in the "derivation" field.
- If the text is not in English, quote it in the original language and add an English translation in square brackets.
- Numbers: copy counts exactly as printed. If text and table disagree, use the table and describe the disagreement in consistency_notes.

Use the codes and rules in the user message exactly. Return only JSON matching the schema.
```

## User preamble (same for every job; the runner appends the levels table and the job)

```
EXTRACTION FORM

Kratom: leaves of Mitragyna speciosa and products from them (chewed or brewed leaves, boiled decoction, "kratom cocktail", powders, capsules, extracts, 7-hydroxymitragynine products).

Unit of extraction: the SAMPLE OF PEOPLE WHO USE KRATOM. It is either (a) the kratom users within a larger study (people who use drugs, patients, students, conscripts, the general population) or (b) a group recruited as kratom users. Controls who do not use kratom are not part of the sample. The job tells you which samples to extract.

Sample fields (codes in brackets; NR = not reported, NA = not applicable):
- label: a short name for the sample (setting, country, years, n)
- reports: the report IDs that describe this sample, e.g., "R1402 (main); R1425"
- pub_status of the main report [journal / preprint / thesis / conference / report / other]
- language of the full text of the main report
- country: ISO 3166 alpha-3
- region [Southeast Asia / North America / Europe / other]
- data_years: years of data collection, e.g. "2021-2022"
- design [cross-sectional / cohort baseline / prevalence survey / validation study / laboratory or EMA study / case-control (users only) / other]
- sample_type [community_users = people who use kratom recruited in villages, households or community settings / online_consumers = online or social-media samples of kratom consumers / drug_users = people who use other drugs, not in treatment / treatment_other_sud = patients in treatment for another substance / psychiatric_patients / students_youth / population_subsample = kratom users within a probability survey / other (say which in notes; e.g., conscripts)]
- sampling [probability / census / respondent-driven / snowball / convenience / online opt-in / clinical consecutive / NR] - for subsamples, the sampling of the parent study
- recruitment_channel [advocacy or vendor channels = recruited through kratom advocacy groups, vendor lists or kratom-interest sites / general / clinical / NR]
- use_period: the reference period that defines a person who uses kratom [past 30 days / past 12 months / lifetime regular / lifetime any / current / NR]
- regular_use_required: "no", or the rule as stated (e.g., "daily for at least 1 year", "regular use > 6 months")
- product_form [traditional leaf = fresh or dried leaves chewed, tea or boiled decoction / kratom cocktail / commercial powder or capsules / extracts or 7-OH products / mixed / NR]
- n_users: the number of kratom users analysed = denominator of the sample's main estimate
- response_rate: as reported, or responded / invited as a percentage
- age_mean, age_sd: years, of the kratom users if reported, else of the whole sample (say which in notes)
- pct_male: 0-100, of the kratom users if reported, else of the whole sample (say which in notes)
- pct_other_opioid_use: share with current non-prescribed opioid use or opioid use disorder, 0-100 or NR
- instruments: every use-disorder or dependence measure used for kratom, with its language version, separated by ";"
- industry_funding [yes = kratom vendor, kratom trade or advocacy organisation / no / NR]
- funding_coi: short
- notes: anything a reviewer must know (overlap with another report, missing parts of the text, whose age or sex the fields describe)

Estimate fields (one estimate per case-definition category x subgroup; whole sample first, then subgroups):
- subgroup: all / male / female / daily users / non-daily users / another subgroup named by the authors
- instrument: one of DSM-5-SUD, DSM-IV, ICD-10, ICD-11, SUDST, interview, KDS, SDS, LDQ, ASSIST, adhoc, other. A self-report or interviewer checklist of the 11 DSM-5 criteria applied to kratom is DSM-5-SUD; a psychiatrist or structured interview (MINI, SCID) is interview
- threshold: the category exactly as applied, with the instrument's score range: e.g., "DSM-5 criteria>=2", "DSM-5 criteria 2-3 (mild)", "DSM-5 criteria 4-5 (moderate)", "DSM-5 criteria>=6 (severe)", "DSM-5 criteria 0-1 (none)", "KDS 14-34 (moderate) of 0-48", "SDS>=6 of 0-15", "LDQ 10-22 (medium) of 0-30", "ASSIST>=27 (high)", "SUDST 4-5 (moderate)"
- cumulative [yes = the category includes every score above its lower bound (">=2", "6+") / no = a closed band ("2-3", "14-34")]
- threshold_source [standard = the instrument's developers / validation paper / study's own / percentile of this sample]
- author_label: the authors' own words, e.g. "kratom use disorder", "moderate", "dependent", "high level"
- level [below / L1 / L2 / L2-scale / L2-screen / L3 / E3 / not_levelled / NR]: the level of the category's LOWER BOUND by the levels table, whatever the authors call it. DSM-5-SUD and SUDST: 0-1 -> below; 2-3 -> L1; 4-5 -> L2; >=6 -> L3; >=2 -> L1; >=4 -> L2. Interview: any disorder -> L1; moderate or severe disorder or dependence -> L2; severe -> L3. DSM-IV dependence and ICD dependence -> L2; DSM-IV abuse or ICD harmful use -> L1. KDS: 0-13 -> below; 14-34 or 35-48 -> L2-scale. SDS and LDQ at the authors' fixed dependence cut-off or medium band and above -> L2-scale; a high band alone -> not_levelled. ASSIST >=27 -> L2-screen; ASSIST 4-26 -> not_levelled. A cut-off from the sample's own distribution (median split, top tertile) -> E3. Ad hoc items -> not_levelled. A category whose lower bound you cannot place -> NR
- table_rule: the levels-table row used and why, e.g. "KDS row; 14-34 band = L2-scale"
- time_frame of the measure [past 12 months / lifetime / current / past week / NR]
- cases: integer number of kratom users in this category
- n: the denominator (kratom users in this subgroup)
- derived [yes / no] and derivation: how cases or n were computed (e.g., "19.7% x 395 = 77.8 -> 78"); empty if not derived
- primary_for_authors [yes / no]: yes if the authors present this as their main use-disorder or dependence estimate
- location and quote: where the numbers are, and a quote with them
- note: anything else (e.g., "percentages only; counts in a supplement not received")

Extraction rules:
- Report every category of every instrument as printed, for the whole sample and for subgroups by sex and use frequency: for DSM-5 usually none, mild, moderate, severe, and any KUD if given. Report both lifetime and past-year estimates when both are given (time_frame tells them apart). Do not build cumulative sums yourself; give a cumulative estimate only when the study itself reports one (e.g., "KUD (2+ criteria) 46.6%").
- Kratom users as a subgroup: the denominator is the number who use kratom in the stated period, not the whole sample.
- If only a percentage is given: cases = round(percentage x n / 100) and derived = yes. If n is unknown, give cases and n as NR and the percentage in note.
- Waves of one cohort or repeated measurements: extract the first assessment with a dependence measure; later ones only in the sample notes.
- Withdrawal scales alone (SOWS, COWS, withdrawal checklists) are not estimates: mention them in notes only.
- Numeric fields (n_users, response_rate, age_mean, age_sd, pct_male, pct_other_opioid_use, cases, n): value holds one number, or NR, or NA. Explanations go to the sample notes or the estimate note.

RISK OF BIAS: JBI checklist for prevalence studies, rated per sample (yes / no / unclear / NA), with a one-line reason, location and quote. The target population is the population of people who use kratom the study claims to describe (kratom users of a district, of a country, of a service). For kratom users within a larger study, items 1, 2 and 9 are rated on the parent study.
1. Sample frame appropriate to address the target population? yes: the frame covers the target population (household or village register; all patients of the named service; all conscripts of the unit). no: only part of it (one advocacy group's members for "US kratom consumers"; one village for a province). unclear: frame not described.
2. Participants sampled in an appropriate way? yes: probability sampling, census of the frame, or consecutive patients of a service. no: convenience, snowball, respondent-driven without weights, online opt-in. unclear: method not described.
3. Sample size adequate? yes: n of kratom users >= 246. no: below 246.
4. Subjects and setting described in detail? yes: age, sex, setting, country and dates of data collection reported. no: two or more of these missing. unclear: one missing.
5. Data analysis with sufficient coverage of the identified sample? yes: missing dependence data <= 10% of the kratom users, or handled. no: > 10% missing, not handled. unclear: not reported.
6. Valid methods for the identification of the condition? Rate the definition that supplies the sample's primary-outcome estimate (L2; else L1). yes: diagnostic interview, or DSM-5 / DSM-IV / ICD criteria assessed item by item (including SUDST), or a dependence scale with a cut-off validated in people who use kratom. no: ad hoc items, study-specific or borrowed cut-offs without validation in kratom users, ASSIST used as a diagnosis. unclear: version or threshold unclear.
7. Condition measured in a standard, reliable way for all participants? yes: same instrument, time frame, mode and threshold for everyone. no: different instruments or modes across participants without a check. unclear: not reported.
8. Appropriate statistical analysis? yes: numerator and denominator of kratom users clear; CI given or calculable. no: percentages that cannot be traced to a numerator and a denominator of kratom users.
9. Response rate adequate, or low response managed? yes: response >= 60%, or responders compared with non-responders, or weights for non-response. no: response < 60% without handling; open online surveys with no denominator of invited people. unclear: not reported.
```

## Job template (the runner fills it)

```
LEVELS TABLE: instruments, thresholds and case-definition levels (forms/instrument_thresholds.csv)
{table1}

JOB {job_id} (study {study_id})
Samples to extract: {samples}
{links}
MAIN REPORT {main_id}
Title: {main_title}
Year: {main_year}; venue: {main_venue}; DOI: {main_doi}
Full text ({main_chars} characters{main_truncated}):
{main_text}
{attached}
```

## Output fields

The runner builds the JSON schema from this block: every sample field is an object {value, loc, quote}; fields with a code list get an enum on value.

```json
{
  "sample_fields": {
    "pub_status": ["journal", "preprint", "thesis", "conference", "report", "other"],
    "language": null,
    "country": null,
    "region": ["Southeast Asia", "North America", "Europe", "other"],
    "data_years": null,
    "design": ["cross-sectional", "cohort baseline", "prevalence survey", "validation study", "laboratory or EMA study", "case-control (users only)", "other"],
    "sample_type": ["community_users", "online_consumers", "drug_users", "treatment_other_sud", "psychiatric_patients", "students_youth", "population_subsample", "other"],
    "sampling": ["probability", "census", "respondent-driven", "snowball", "convenience", "online opt-in", "clinical consecutive", "NR"],
    "recruitment_channel": ["advocacy or vendor channels", "general", "clinical", "NR"],
    "use_period": ["past 30 days", "past 12 months", "lifetime regular", "lifetime any", "current", "NR"],
    "regular_use_required": null,
    "product_form": ["traditional leaf", "kratom cocktail", "commercial powder or capsules", "extracts or 7-OH products", "mixed", "NR"],
    "n_users": null,
    "response_rate": null,
    "age_mean": null,
    "age_sd": null,
    "pct_male": null,
    "pct_other_opioid_use": null,
    "instruments": null,
    "industry_funding": ["yes", "no", "NR"],
    "funding_coi": null
  },
  "estimate_enums": {
    "instrument": ["DSM-5-SUD", "DSM-IV", "ICD-10", "ICD-11", "SUDST", "interview", "KDS", "SDS", "LDQ", "ASSIST", "adhoc", "other"],
    "cumulative": ["yes", "no"],
    "threshold_source": ["standard", "validation paper", "study's own", "percentile of this sample"],
    "level": ["below", "L1", "L2", "L2-scale", "L2-screen", "L3", "E3", "not_levelled", "NR"],
    "time_frame": ["past 12 months", "lifetime", "current", "past week", "NR"],
    "derived": ["yes", "no"],
    "primary_for_authors": ["yes", "no"]
  },
  "jbi_ratings": ["yes", "no", "unclear", "NA"]
}
```
