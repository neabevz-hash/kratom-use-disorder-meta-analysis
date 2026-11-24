# Protocol: Prevalence of kratom use disorder and dependence among people who use kratom — a systematic review and meta-analysis

**Version 1.0, frozen on 2026-11-21** (git tag `kratom-prereg-v1.0`) before the final search and before any title/abstract screening. Structured by PRISMA-P 2015 (Moher et al., 2015; Shamseer et al., 2015); item numbers in brackets. Built on the sports-betting protocol (`papers/sports-betting-prevalence/protocol.md`, v1.0) and the misophonia protocol (`papers/misophonia-prevalence/protocol.md`, v1.0). Every reference was verified by DOI via Crossref on 2026-11-21.

---

## Administrative information

**[1] Title.** Prevalence of kratom use disorder and dependence among people who use kratom: a systematic review and meta-analysis across case definitions, regions and sample types.

**[2] Registration.** OSF Registries, registered on 2026-11-21 at 15:02 UTC: https://osf.io/6d7n3, DOI [10.17605/OSF.IO/6D7N3](https://doi.org/10.17605/OSF.IO/6D7N3); the final search started after it (15:04 UTC). The registration package was not attached to the registration (`deviations.md`, D1). Generalized Systematic Review Registration form (van den Akker et al., 2023), with the frozen protocol and the registration package (`registration/make_osf_package.py`: protocol, forms, search and screening code, the AI screener prompt, the check-run logs); field texts in `registration/osf.md`. The final search starts after the registration. Adding the registration identifiers here is the only change made to this file after freezing.

**[3a] Author and contact.** Martin Rekhert, MA student in clinical psychology, Turan University, Almaty, Kazakhstan. ORCID 0009-0001-2402-2031. mrexert@gmail.com.

**[3b] Contributions.** Single author (R1): conceptualisation, eligibility decisions at every stage, data extraction, risk-of-bias appraisal, interpretation, final manuscript. An AI assistant (Claude Opus 5.5, Anthropic, run through Claude Code; Claude Sonnet 5.5 as the second screening pass) is used as a tool for the tasks in §9–§11 and §15: search code, de-duplication, draft screening labels, draft full-text proposals, draft extraction and risk-of-bias ratings, analysis code, translation and text drafts. It is disclosed in the Methods and in the AI declaration. Every AI output is a draft: R1 checks each AI label, extracted value and rating against the source and accepts or overrides it, so all final decisions are R1's.

**[4] Amendments.** Any change after registration is dated, justified and logged in `deviations.md`, and reported in the registration and in the paper.

**[5] Support.** No funding, no sponsor, no conflicts of interest. No funding from the kratom industry or from organisations campaigning for or against kratom regulation.

---

## Introduction

**[6] Rationale.**

Kratom (*Mitragyna speciosa*) is a tree of Southeast Asia whose leaves contain mitragynine and 7-hydroxymitragynine, alkaloids with partial agonist activity at the μ-opioid receptor. In Thailand and Malaysia the leaves have been chewed or brewed for generations; in the United States and Europe kratom is sold as powders, capsules and extracts and used to self-manage pain, mood and opioid withdrawal. Since 2025 products with concentrated or semi-synthetic 7-hydroxymitragynine have widened the range of exposure and drawn regulatory attention. Clinicians and regulators need to know how often regular use turns into a use disorder.

Pooled estimates exist for neighbouring questions only. El-Sehrawy et al. (2026) pooled the prevalence of kratom use in populations (21 studies; current use 1.6%). Yang, Müller and Singh (2024) pooled correlations between kratom use and mental-health indicators (36 studies). Govarthnapany et al. (2026) reviewed kratom use in adolescents and students without pooling. Systematic reviews of case reports describe kratom dependence and withdrawal in patients, not their frequency among people who use kratom. No published meta-analysis estimates the proportion of people who use kratom who meet criteria for kratom use disorder or dependence. One registered review (PROSPERO CRD420261530340, registered 27 October 2026) covers the whole clinical literature on kratom — patterns of use, toxicity, dependence, withdrawal and treatment — and lists the prevalence of use disorder among many outcomes, to be pooled if studies are comparable (`novelty/novelty.md`).

Single-study estimates vary widely: about a quarter to a third of US consumers recruited online met DSM-5 criteria (Smith et al., 2022; Hill et al., 2024), whereas among regular users of traditional kratom in Malaysia more than half had severe dependence (Singh et al., 2014) and nearly all met substance use disorder criteria (Singh et al., 2019). Studies from the same networks also report how symptom counts spread across severity levels (Rogers et al., 2024). The variation probably reflects the setting (traditional daily leaf use in Southeast Asia versus commercial products in the United States), the sample (community users, online consumers, people in treatment for other substances) and the case definition (DSM-5 criteria with mild, moderate and severe levels, DSM-IV dependence, dependence scales). A pooled, definition-aware estimate that examines this variation is missing.

**[7] Objectives.**

Review question (CoCoPop; Munn et al., 2015):
- **Condition:** kratom use disorder (DSM-5) or kratom dependence (DSM-IV, ICD-10, ICD-11, a dependence scale, a diagnostic interview).
- **Context:** any country, setting and year.
- **Population:** people who use kratom (§8), not recruited because of kratom problems.

Objectives:
1. **Primary.** Estimate the prevalence of moderate-to-severe kratom use disorder or dependence (level L2, §13) among people who use kratom.
2. Estimate the prevalence at each case-definition level: L1 any use disorder (DSM-5 mild or more, DSM-IV abuse or dependence, ICD harmful use or dependence), L2 moderate-to-severe disorder or dependence, L3 severe disorder.
3. Estimate the prevalence separately for Southeast Asia and North America, and by sample type.
4. Examine sources of heterogeneity: instrument, sample type, regular use required for entry, reference period of use, product form, other opioid use, recruitment through kratom advocacy or vendor channels, year of data collection, age, sex composition, risk of bias.

The review is descriptive and tests no confirmatory hypotheses. Expectations stated in advance, to be checked rather than tested: prevalence decreases from L1 to L3; samples from Southeast Asia give higher estimates than samples from North America; samples that require regular or daily use give higher estimates than samples of any users; samples recruited through advocacy or vendor channels give lower estimates.

---

## Methods

### [8] Eligibility criteria

**Study designs.** Cross-sectional surveys; the baseline wave of cohort studies; screening phases of other studies; national and regional drug-use surveys (journal articles and reports); laboratory, ecological momentary assessment and clinical studies that recruited people who use kratom and report how many met a case definition; any design that reports how many people who use kratom met a case definition.

**Kratom.** Leaves of *Mitragyna speciosa* and products from them: fresh or dried leaves chewed, tea or boiled decoction, the "kratom cocktail" (4×100), powders, capsules, extracts, and products with mitragynine or 7-hydroxymitragynine. Other *Mitragyna* species are not kratom.

**Inclusion criteria.**
- I1. The sample, or a reported subsample, consists of people who use kratom in a stated reference period (past 30 days, past 12 months, lifetime regular use, current use; lifetime any use coded). Samples that require regular or daily use are eligible and coded.
- I2. The sample was not recruited because of kratom problems.
- I3. Kratom use disorder or dependence was assessed with DSM-5 substance use disorder criteria applied to kratom (self-report checklist or interview), DSM-IV abuse or dependence criteria, ICD-10 or ICD-11 criteria, a dependence scale (Krathom/Ketum Dependence Scale, Severity of Dependence Scale, Leeds Dependence Questionnaire and others) with a fixed cut-off, ASSIST risk scores for kratom, or a clinician or structured diagnostic interview.
- I4. The study reports the number or proportion of people who use kratom meeting at least one case definition together with the denominator, or enough data to derive them.
- I5. Any language, any publication year, any publication status: journal article, preprint, thesis, conference abstract or report with sufficient data.

**Exclusion criteria.**
- E1. Samples recruited because of kratom problems: people in treatment for kratom use disorder or kratom withdrawal, kratom-related emergency or poison-centre cases. Samples in treatment for another substance (for example, methadone patients) are eligible and coded as a sample type.
- E2. Use disorder or dependence reported only for a whole sample that includes people who do not use kratom, with no figure for those who use it.
- E3. Case definitions derived from the sample's own distribution (median split, top tertile): recorded, not pooled.
- E4. Measures that are not case definitions of use disorder or dependence: withdrawal symptoms or a withdrawal scale alone, frequency or quantity of use, single self-identification items ("I feel addicted") — recorded, not pooled.
- E5. Reviews, editorials, qualitative studies without counts, case reports and case series.
- E6. Duplicate reports of the same sample; reports are linked and the most complete one supplies the data.
- E7. Pharmacokinetic or safety studies in people who do not use kratom; preclinical studies.

### [9] Information sources

Turan University has no subscription access to Web of Science, PsycINFO or Embase. Coverage relies on open indexes, Scopus through its search API, non-English terms and citation searching:

- **PubMed**; **Europe PMC** (MEDLINE, PMC and preprints from medRxiv, Research Square, PsyArXiv, SSRN, Preprints.org); **OpenAlex**; **Semantic Scholar**; **Scopus** (Search API: titles and identifiers; abstracts come from the other sources); **Crossref** (posted content, reports, theses, journals of Southeast Asia that deposit DOIs, including Thai Journals Online); **DataCite** (theses, OSF, Zenodo, figshare); **OpenAIRE Graph** and **CORE** (institutional repositories, theses, reports).
- **Non-English terms** in OpenAlex: Thai (กระท่อม, ใบกระท่อม), Malay and Indonesian (ketum, daun ketum, air ketum, daun kratom), Russian, Japanese, Chinese and Korean (§10).
- **Citation searching:** the reference lists of the syntheses in §6 and of other reviews of kratom use (El-Sehrawy et al., 2026; Yang et al., 2024; Govarthnapany et al., 2026; Swogger & Walsh, 2018; Stanciu et al., 2019; Govarthnapany et al., 2025; Burgoa et al., 2026), through OpenAlex; after full-text screening, backward and forward citation searching of the included studies through OpenAlex. Records from citation searching are screened like the others.

**Seed set.** Nine studies of people who use kratom that assessed use disorder or dependence, taken from the reference lists of Yang et al. (2024), El-Sehrawy et al. (2026), Smith et al. (2022) and Hill et al. (2024), first authors and years checked against Crossref on 2026-11-21 (`search/seed_set.csv`, `search/seed_candidates.py`, built before the check run). Recall is reported for the check run and for the final search; misses are examined one by one.

### [10] Search strategy

Two concepts. **Concept A (kratom)** is searched in every source: kratom, kratoms, krathom, kratum, ketum, kakuam, biak-biak, "Mitragyna speciosa", mitragynine, 7-hydroxymitragynine, mitragynine pseudoindoxyl (PubMed adds the MeSH term Mitragyna). No date or language limits. **Concept B (people who use kratom, or dependence)** is applied locally to the retrieved title and abstract by `search/dedup.py`, identically for all sources, because the sources differ in Boolean support: dependence terms (depend*, use disorder, addict*, withdraw*, DSM, ICD, craving, toleran*, problematic, compulsive, abuse, misuse, harmful use, loss of control, SDS, KDS, substance use) or human-sample terms (user(s), consumer(s), respondent(s), participant(s), survey, questionnaire, interview, cross-sectional, people/persons/individuals who, prevalence, epidemiolog*, student(s), adolescent(s), youth, general population, villager(s), chewer(s), eater(s), drinker(s), regular or daily use, the Malay and Indonesian equivalents, and use and dependence terms in Czech, Polish, German, Spanish, Portuguese and French). A record without an abstract passes if its title has a use, user or dependence term (use, using, consum*, user, depend*, addict*, withdraw*, disorder, abuse, misuse, survey, people, patient(s), treatment, chew*, eat*, drink*, smok*, habit, epidem*, prevalen*, social, psych*, health, clinic*). Records in Thai, Chinese, Japanese, Korean or Cyrillic script and records found only through citation searching are kept without concept B. Exact strings: `search/search.py` and `search/dedup.py`; reported per PRISMA-S (Rethlefsen et al., 2021).

| Source | Query form |
| --- | --- |
| PubMed | concept A terms in `[tiab]`, `kratom*[tiab]`, `"Mitragyna"[Mesh]` |
| Europe PMC | `TITLE_ABS:"…"` with concept A |
| OpenAlex | `title_and_abstract.search` with concept A |
| OpenAlex, non-English | กระท่อม, ใบกระท่อม, кратом, митрагинин, クラトム, ミトラガイニン, 卡痛, 帽柱木, 크라톰, daun ketum, air ketum, daun kratom |
| Semantic Scholar | bulk search with concept A |
| Scopus | `TITLE-ABS-KEY(kratom OR krathom OR kratum OR ketum OR kakuam OR "biak-biak" OR "mitragyna speciosa" OR mitragynine OR "7-hydroxymitragynine")` |
| Crossref | relevance-sorted `query.bibliographic` queries (kratom, kratom use, kratom users, kratom dependence, kratom use disorder, ketum, krathom, Mitragyna speciosa, mitragynine), kept while title or abstract contains a kratom term |
| DataCite | concept A in titles, descriptions and subjects |
| OpenAIRE, CORE | kratom, krathom, ketum, Mitragyna speciosa, mitragynine |
| Citation searching | reference lists of seven syntheses (OpenAlex `referenced_works`), records with a kratom term |

**Check run of the v1.0 code (2026-11-21; `search/runs/2026-11-21-check/`).**

| Source | Records |
| --- | --- |
| OpenAlex | 2,903 |
| Semantic Scholar | 2,431 |
| OpenAIRE | 2,447 |
| CORE | 2,308 |
| Crossref | 2,166 |
| Scopus | 1,778 |
| Europe PMC | 1,213 |
| PubMed | 1,203 |
| DataCite | 817 |
| Citation searching (276 references of seven syntheses; 190 with a kratom term) | 190 |
| OpenAlex, non-English | 72 |
| **Total** | **17,528** |

- After de-duplication: 4,385 unique records; removed before screening: 118 non-study records, 33 vendor advertisements (rule 6) and 1,930 records outside concept B (rule 7; 791 of them without an abstract); **2,304 to screen** (1,771 passed concept B on title and abstract, 359 on the title alone, 174 in non-Latin script; 392 have no abstract; 133 come only from Scopus, 336 only from pointer sources).
- All 190 records from citation searching were also found by the database searches.
- Recall on the seed set: **9 of 9**.
- Concept B was checked on random samples of the removed records: almost all are chemistry, botany, pharmacology, animal studies, case reports and news items. The check found Czech theses on kratom use whose titles had no English term; use and dependence terms in Czech, Polish, German, Spanish, Portuguese and French were added to concept B before freezing (29 more records to screen).
- Stand test of the screener prompt (`screening/llm/stand_test_2026-11-21-check_*.jsonl`, `screening/stand_test_ids.py`): 13 records chosen to cover each decision type (three seed studies, a national survey of kratom use, a systematic review, a Reddit analysis, poison-centre data, a laboratory study of regular users, psychiatric inpatients, a case report, an animal study, a record without abstract, a record with Thai text). Both passes gave an expected label on all 13; they differed only on the national survey of kratom use (Opus exclude, Sonnet unsure).

The final search runs with the v1.0 code after registration and before screening; dates, counts and software versions go to `search_log.json`. Raw exports are archived with the data release.

### [11] Study records

**[11a] Data management.** As in the misophonia and sports-betting reviews: git repository with dated commits; de-duplication on DOI (version suffixes ignored), PMID and normalised title with years within ±1 (`search/dedup.py`); pointer sources attached to the database record with the same title; records that every source types as a non-study record removed automatically. Rule 6: records found only outside PubMed, Europe PMC and Scopus whose title reads as kratom shop or vendor advertising ("best kratom", "kratom vendors", "buy kratom", strain or capsule reviews, promo codes) are removed. Rule 7: concept B (§10). Records removed by rules 5–7 stay in `records_unique.jsonl` with the reason and are reported as "removed before screening". Data and code are released on GitHub with a Zenodo DOI at submission.

**[11b] Selection process.**
- **Title and abstract: two AI passes, R1 decides every record that either pass keeps; double AI exclusions are audited by a blind calibration sample** (the scheme of the AI-dependence and sports-betting reviews).
  1. **Blind calibration.** Before seeing any AI label, R1 screens a random sample of 300 records (`screening/calibration.py`: `random.Random(20261121).sample` over sorted record IDs, shown in the sampled order). Labels: include / unsure / exclude with a reason code. R1 sees title, abstract, year, venue, record type, language and DOI link; no author names. Decisions are committed before any AI label is shown.
  2. **AI draft, two passes.** Claude Opus 5.5 (`claude-opus-5-5`) and Claude Sonnet 5.5 (`claude-sonnet-5-5`), both at effort high, label every record independently with the same frozen prompt (`screening/llm_screener_prompt.md`): include / unsure / exclude, a reason code and a one-sentence note, "unsure" whenever in doubt — in particular when the abstract does not say whether dependence or use disorder was assessed. SHA-256 hashes of both label files are committed before unblinding.
  3. **Verification.** R1 reviews, with the AI labels visible, every record that at least one pass labelled include or unsure, and accepts or overrides the labels. R1's decision is final; include and unsure go to full text. Records labelled exclude by both passes are excluded without further human review; their list, with reason codes and notes, is part of the open data.
  4. **Safeguard.** If, in the calibration sample, a record that R1 labelled include or unsure was labelled exclude by both passes, R1 screens all double-excluded records outside the calibration sample whose title or abstract contains a human-sample term (users, consumers, respondents, participants, survey, questionnaire, interview, cross-sectional, people/persons/individuals who, prevalence, patients, students, adolescents, villagers, chewers, drinkers, DSM, use disorder, the Malay and Indonesian equivalents, or Thai script), or that have no abstract, with the AI labels hidden, in random order (seed 20261122); every record R1 then marks include or unsure goes to full text.
  - **Tool:** Markdown decision files from `screening/screen_md.py`, codes `+` include, `?` unsure, `-1`…`-7` exclude with a reason (1 review or commentary; 2 qualitative without counts, or preclinical; 3 no dependence or use-disorder measure; 4 case report, case series, toxicology or poison-centre data; 5 sample recruited because of kratom problems; 6 not kratom or not people who use it; 7 other, with a note), `=` to accept the AI label when both passes agree. Each file is committed blank before R1 starts and again when R1 finishes.
  - **Reported:** κ and Gwet's AC1 (Gwet, 2008) between R1 (blind) and each AI pass and their union; sensitivity and specificity with Clopper–Pearson 95% CIs; overrides by direction; whether the safeguard was triggered; how many included studies the AI had labelled exclude.
  - **Rationale:** single-reviewer screening misses about 13% of eligible studies (Waffenschmidt et al., 2019); LLM screeners reach high sensitivity on titles and abstracts (Oami et al., 2024). Two independent AI passes lower the chance of a missed record; the blind calibration measures the miss rate of the AI rule, and the safeguard returns the double exclusions to R1 if it misses even one calibration record.
- **Full text.** Open-access versions only (Unpaywall, PMC, repositories, preprint servers, publishers' report pages); authors are not contacted. Non-English texts (Thai, Malay, Indonesian and others) are machine-translated by the AI assistant (Jackson et al., 2019); R1 checks the numbers against the original tables. The AI drafts a proposal per report: eligible or not, the primary exclusion reason, and where the counts for people who use kratom are (table, page, quote); R1 checks each proposal and decides. Reports without an open full text are listed as "reports not retrieved".
- **Linking reports.** Reports of one sample are linked and the sample is counted once; overlap is judged from site, years of data collection and sample size (several Malaysian community studies may share samples).
- **AI prompts after screening.** Full-text, extraction and risk-of-bias prompts are written before full-text screening, piloted on three studies, frozen with git tags and committed before use.

**[11c] Data collection process.**
- **Forms.** Two linked tables: `forms/samples.csv` (one row per independent sample of people who use kratom) and `forms/estimates.csv` (one row per case definition × sample × subgroup). Codebook: `forms/extraction_codebook.md`.
- **AI draft.** The AI assistant pre-fills every field with its source location (table, page or quote); the draft is stored unchanged (`extraction/draft/`).
- **Verification.** R1 verifies every value against the source in Markdown files (`extraction/verify_md.py`); key items (denominator of people who use kratom, case counts at each level, instrument and cut-off, reference period of use, sample type, region) are always checked against the source table. The share of AI values that R1 corrected and the share of AI quotes found verbatim in the source are reported.
- **Checks.** Cases ≤ n; cumulative levels consistent (L3 ≤ L2 ≤ L1); category counts add up to the total; percentages match counts within rounding; retractions and expressions of concern checked through Crossref.

### [12] Data items

Per sample: report details; country and region; years of data collection; design; sampling method; sample type (community users / online consumers / people who use other drugs / patients in treatment for another substance / psychiatric patients / students and youth / kratom users within a population survey / other); recruitment through kratom advocacy or vendor channels; reference period of use; whether regular or daily use was required for entry; product form (traditional leaf, tea or decoction / kratom cocktail / commercial powder or capsules / extracts or 7-hydroxymitragynine products / mixed); n analysed; age (mean, SD); percentage male; share with current non-prescribed opioid use; instruments (name, version, language, time frame); for every case definition: threshold, number of cases and denominator, overall and by sex; funding and kratom-industry funding.

### [13] Outcomes and prioritisation

**Outcome.** Proportion of people who use kratom meeting a case definition of kratom use disorder or dependence (cases / N).

**Case-definition levels.** Fixed with the protocol and applied regardless of the label used by study authors. The table with sources (`forms/instrument_thresholds.csv`) is completed for every instrument found in the included studies before extraction, using only development and validation papers; the completion is logged as a clarification, not a change of rule.

| Level | Definition |
| --- | --- |
| L1 any use disorder | DSM-5 kratom use disorder, ≥ 2 criteria (mild or more; American Psychiatric Association, 2013); DSM-IV abuse or dependence; ICD-10 harmful use or dependence; ICD-11 harmful pattern or dependence; any disorder by interview |
| L2 moderate-to-severe disorder or dependence | DSM-5 ≥ 4 criteria; DSM-IV dependence (≥ 3 of 7 criteria), which corresponds closely to DSM-5 moderate-to-severe disorder (Compton et al., 2013); ICD-10 or ICD-11 dependence; dependence or moderate-to-severe disorder by interview. Coded **L2-scale**: a dependence scale (Krathom Dependence Scale, Saingam et al., 2014; Severity of Dependence Scale, Gossop et al., 1995; Leeds Dependence Questionnaire, Raistrick et al., 1994; and others) at a validated cut-off or the authors' fixed cut-off. Coded **L2-screen**: ASSIST high risk (score ≥ 27; Humeniuk et al., 2008) |
| L3 severe disorder | DSM-5 ≥ 6 criteria; severe disorder by interview |

Levels are cumulative: a sample reporting DSM-5 severity categories contributes L1 (mild+), L2 (moderate+) and L3 (severe).

**Primary outcome.** Prevalence of L2 (moderate-to-severe use disorder or dependence, including L2-scale and L2-screen) among people who use kratom, all eligible samples. L2 is chosen as primary because it is the level at which DSM-5, DSM-IV, ICD and dependence scales can be compared.

**Secondary outcomes:** prevalence at L1 and L3; prevalence by region (Southeast Asia, North America, other) and by sample type.

**One estimate per sample for each analysis.**
- Within a level, in this order: interview; DSM-5 criteria assessed item by item; DSM-IV or ICD criteria; dependence scale; ASSIST; if several remain, the instrument the authors designate as primary; otherwise the median logit prevalence (with an even number, the lower of the two middle values).
- Reference period: past-12-month use; otherwise the period reported (coded). Time frame of the disorder: past 12 months; otherwise lifetime (coded).
- Whole-sample estimates in all pooled analyses; subgroup estimates (by sex, use frequency) only in the analyses that need them.

All estimates enter the multilevel moderator analysis (§15b).

### [14] Risk of bias in individual studies

JBI Critical Appraisal Checklist for Studies Reporting Prevalence Data, nine items (Munn et al., 2014, 2015), rated yes / no / unclear with decision rules adapted to people who use kratom (`forms/rob_jbi.md`):
- item 1 — sampling frame appropriate to the target population of people who use kratom;
- item 2 — sampling: probability, census or consecutive patients = yes (for kratom users within population surveys, the parent survey's sampling);
- item 3 — sample size against the precision for an expected prevalence of 20% ± 5 percentage points (n ≥ 246);
- item 6 — valid identification: interview, or DSM or ICD criteria assessed item by item, or a dependence scale with a cut-off validated in people who use kratom = yes;
- item 9 — response rate ≥ 60%, or non-response handled.

The AI drafts each rating with a supporting quote; R1 verifies and decides. No summary score; items 2, 6 and 9 drive the sensitivity analyses.

### [15] Data synthesis

**[15a] Narrative synthesis.** Study characteristics by region and sample type; an evidence map of instruments × cut-offs × levels; estimates excluded under E3 and E4 listed, not pooled.

**[15b] Meta-analysis.**
- **Primary model.** Random-effects binomial–normal generalised linear mixed model on the logit scale (`metafor::rma.glmm`, `measure = "PLO"`, ML), preferred over inverse-variance pooling of transformed proportions and over the Freeman–Tukey back-transformation (Stijnen et al., 2010; Schwarzer et al., 2019; Lin & Chu, 2020).
- **Reported:** pooled prevalence with 95% CI and 95% prediction interval (IntHout et al., 2016); τ² on the logit scale; I², interpreted through the prediction interval (Migliavaca et al., 2022).
- **Minimum data:** at least three independent samples per pooled estimate.
- **Subgroups:** case-definition level (L1–L3); region (Southeast Asia / North America / other); sample type.
- **Moderator analysis using all estimates.** Three-level model (estimates in samples in studies): `lme4::glmer`, binomial likelihood, nested random intercepts; as a check, `metafor::rma.mv` on logits with cluster-robust inference (Van den Noortgate et al., 2013; Pustejovsky & Tipton, 2022).
  - Pre-specified multivariable model: case-definition level, region, regular use required for entry.
  - Exploratory moderators, one at a time, each only when k ≥ 10: instrument within L2; sample type; reference period of use; product form; share with non-prescribed opioid use; recruitment through advocacy or vendor channels; year of data collection; mean age; percentage male; JBI items 2, 6 and 9; publication status; kratom-industry funding.
  - If a variance component is estimated at zero, that level is dropped and the simpler model reported.

**[15c] Sensitivity analyses** (on the primary outcome):
1. excluding L2-scale and L2-screen estimates (DSM, ICD and interview only);
2. only probability, census or consecutive samples (JBI item 2 = yes);
3. only valid identification (JBI item 6 = yes);
4. response rate ≥ 60% or not applicable;
5. excluding samples in treatment for another substance and psychiatric patients;
6. excluding samples recruited through advocacy or vendor channels or with kratom-industry funding;
7. excluding preprints, theses, conference abstracts and reports;
8. excluding samples with n < 100;
9. inverse-variance random-effects pooling of logits (REML, Hartung–Knapp) instead of the GLMM;
10. leave-one-out and influence diagnostics.

**[15d] If pooling is not appropriate** (fewer than three samples in a stratum), estimates are tabulated and shown in forest plots without a pooled value.

**Software.** R 4.6.1 with metafor, lme4 and clubSandwich; versions in `analysis/sessionInfo.txt`. Python 3.12 for search, de-duplication, decision files and the AI runner; Claude Code (headless) for AI drafts, with the version stored with every output. Windows 11.

### [16] Meta-biases

- Funnel-plot asymmetry tests are unreliable for proportions (Hunter et al., 2014) and are not used as inference; logit prevalence is plotted against its standard error, prevalence is regressed on 1/√n, and peer-reviewed estimates are compared with grey literature.
- Selective reporting within studies: case definitions announced in the methods compared with those reported.
- Kratom-industry funding and recruitment through advocacy or vendor channels are coded and tested as moderators.

### [17] Confidence in cumulative evidence

GRADE adapted for event rates (Iorio et al., 2015): risk of bias (share of weight from samples with "no" on JBI items 2, 6 or 9), inconsistency (prediction interval width), imprecision (CI half-width above 5 percentage points), indirectness (sample types far from the target population; few countries), publication bias. Summary-of-findings table.

---

## Load for the human reviewer (fixed in advance; one round)

Based on the check run of 2026-11-21; the final numbers are reported in the PRISMA flow diagram.

| Stage | Who | Approximate volume |
| --- | --- | --- |
| Title and abstract, blind calibration | R1 | 300 records |
| Title and abstract, verification | R1 | about 600–900 of the 2,304 records (those that at least one AI pass kept); `=` accepts the label when both passes agree. The double AI exclusions are not reviewed unless the safeguard triggers; then R1 screens those with a human-sample term in title or abstract or without an abstract blind, one character per record |
| Full-text screening | R1 verifies an AI proposal | about 150–300 reports sought, of which about half are expected to be open (about 80–170 decisions), each with the location of the counts |
| Instrument cut-offs | R1 verifies an AI draft | about 5–8 instruments, once each (levels table) |
| Data extraction | R1 verifies an AI draft | about 15–30 samples; per sample about 20 fields and 1–4 estimates, each with its source location |
| Risk of bias | R1 verifies an AI draft | 9 items per included study, each with a quote |

No author contacts. No further human coding rounds are planned. There is no second human reviewer, and double AI exclusions at the title-and-abstract stage are not reviewed by a human unless the safeguard triggers; these are limitations, partly offset by two independent AI passes, the blind calibration sample with a reported miss rate, R1's decision on every record kept and every full text, and verification of every extracted value.

---

## References

- American Psychiatric Association (2013). Diagnostic and Statistical Manual of Mental Disorders. https://doi.org/10.1176/appi.books.9780890425596
- Burgoa, S., Guirguis, E., Dunn, A., Llorens, C., Knecht, M., Rose, G., & Sacca, L. (2026). Mapping the Evidence on Kratom Use, Health Outcomes, and Policy Gaps in the United States: A Scoping Review. *Substance Use & Misuse*, 1-33. https://doi.org/10.1080/10826084.2026.2697988
- Compton, W. M., Dawson, D. A., Goldstein, R. B., & Grant, B. F. (2013). Crosswalk between DSM-IV dependence and DSM-5 substance use disorders for opioids, cannabis, cocaine and alcohol. *Drug and Alcohol Dependence*, *132*(1-2), 387-390. https://doi.org/10.1016/j.drugalcdep.2013.02.036
- El-Sehrawy, A. M. A., Mohammad, S. I., Vasudevan, A., Singh, M., Abdulakimov, G., Makhmudova, A., Al-Rashidi, R. R., Kadier, M., Jabir, M. S., & Basunduwah, T. S. (2026). Global prevalence of kratom use: a meta-analysis focusing on regional and population-level disparities. *Journal of Ethnicity in Substance Abuse*, 1-20. https://doi.org/10.1080/15332640.2026.2706579
- Gossop, M., Darke, S., Griffiths, P., Hando, J., Powis, B., Hall, W., & Strang, J. (1995). The Severity of Dependence Scale (SDS): psychometric properties of the SDS in English and Australian samples of heroin, cocaine and amphetamine users. *Addiction*, *90*(5), 607-614. https://doi.org/10.1046/j.1360-0443.1995.9056072.x
- Govarthnapany, N., Dékány, L., Gabrhelík, R., & Singh, D. (2026). Kratom use in adolescents and college students: a systematic review of prevalence, patterns, and risk factors across community and rehabilitation settings. *The American Journal of Drug and Alcohol Abuse*, *52*(1), 5-17. https://doi.org/10.1080/00952990.2025.2609965
- Govarthnapany, N., Gabrhelik, R., & Singh, D. (2025). Kratom ( Mitragyna speciosa Korth.) Use Among Poly-Drug Users in Southeast Asia: A Systematic Review. *Journal of Psychoactive Drugs*, *58*(4), 421-431. https://doi.org/10.1080/02791072.2025.2465797
- Gwet, K. L. (2008). Computing inter‐rater reliability and its variance in the presence of high agreement. *British Journal of Mathematical and Statistical Psychology*, *61*(1), 29-48. https://doi.org/10.1348/000711006x126600
- Hill, K., Grundmann, O., Smith, K. E., & Stanciu, C. N. (2024). Prevalence of Kratom Use Disorder Among Kratom Consumers. *Journal of Addiction Medicine*, *18*(3), 306-312. https://doi.org/10.1097/adm.0000000000001290
- Humeniuk, R., Ali, R., Babor, T. F., Farrell, M., Formigoni, M. L., Jittiwutikarn, J., De Lacerda, R. B., Ling, W., Marsden, J., Monteiro, M., Nhiwatiwa, S., Pal, H., Poznyak, V., & Simon, S. (2008). Validation of the alcohol, smoking and substance involvement screening test (ASSIST). *Addiction*, *103*(6), 1039-1047. https://doi.org/10.1111/j.1360-0443.2007.02114.x
- Hunter, J. P., Saratzis, A., Sutton, A. J., Boucher, R. H., Sayers, R. D., & Bown, M. J. (2014). In meta-analyses of proportion studies, funnel plots were found to be an inaccurate method of assessing publication bias. *Journal of Clinical Epidemiology*, *67*(8), 897-903. https://doi.org/10.1016/j.jclinepi.2014.03.003
- IntHout, J., Ioannidis, J. P. A., Rovers, M. M., & Goeman, J. J. (2016). Plea for routinely presenting prediction intervals in meta-analysis. *BMJ Open*, *6*(7), e010247. https://doi.org/10.1136/bmjopen-2015-010247
- Iorio, A., Spencer, F. A., Falavigna, M., Alba, C., Lang, E., Burnand, B., McGinn, T., Hayden, J., Williams, K., Shea, B., Wolff, R., Kujpers, T., Perel, P., Vandvik, P. O., Glasziou, P., Schunemann, H., & Guyatt, G. (2015). Use of GRADE for assessment of evidence about prognosis: rating confidence in estimates of event rates in broad categories of patients. *BMJ*, *350*(mar16 7), h870-h870. https://doi.org/10.1136/bmj.h870
- Jackson, J. L., Kuriyama, A., Anton, A., Choi, A., Fournier, J. P., Geier, A. K., Jacquerioz, F., Kogan, D., Scholcoff, C., & Sun, R. (2019). The Accuracy of Google Translate for Abstracting Data From Non–English-Language Trials for Systematic Reviews. *Annals of Internal Medicine*, *171*(9), 677-679. https://doi.org/10.7326/m19-0891
- Lin, L., & Chu, H. (2020). Meta-analysis of Proportions Using Generalized Linear Mixed Models. *Epidemiology*, *31*(5), 713-717. https://doi.org/10.1097/ede.0000000000001232
- Migliavaca, C. B., Stein, C., Colpani, V., Barker, T. H., Ziegelmann, P. K., Munn, Z., Falavigna, M., & Prevalence Estimates Reviews—Systematic Review Methodology Group (PERSyst) (2022). Meta‐analysis of prevalence: I 2 statistic and how to deal with heterogeneity. *Research Synthesis Methods*, *13*(3), 363-367. https://doi.org/10.1002/jrsm.1547
- Moher, D., Shamseer, L., Clarke, M., Ghersi, D., Liberati, A., Petticrew, M., Shekelle, P., Stewart, L. A., & PRISMA-P Group (2015). Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015 statement. *Systematic Reviews*, *4*(1), 1. https://doi.org/10.1186/2046-4053-4-1
- Munn, Z., Moola, S., Lisy, K., Riitano, D., & Tufanaru, C. (2015). Methodological guidance for systematic reviews of observational epidemiological studies reporting prevalence and cumulative incidence data. *International Journal of Evidence-Based Healthcare*, *13*(3), 147-153. https://doi.org/10.1097/xeb.0000000000000054
- Munn, Z., Moola, S., Riitano, D., & Lisy, K. (2014). The development of a critical appraisal tool for use in systematic reviews addressing questions of prevalence. *International Journal of Health Policy and Management*, *3*(3), 123-128. https://doi.org/10.15171/ijhpm.2014.71
- Oami, T., Okada, Y., & Nakada, T. a. (2024). Performance of a Large Language Model in Screening Citations. *JAMA Network Open*, *7*(7), e2420496. https://doi.org/10.1001/jamanetworkopen.2024.20496
- Pustejovsky, J. E., & Tipton, E. (2022). Meta-analysis with Robust Variance Estimation: Expanding the Range of Working Models. *Prevention Science*, *23*(3), 425-438. https://doi.org/10.1007/s11121-021-01246-3
- Raistrick, D., Bradshaw, J., Tober, G., Weiner, J., Allison, J., & Healey, C. (1994). Development of the Leeds Dependence Questionnaire (LDQ): A questionnaire to measure alcohol and opiate dependence in the context of a treatment evaluation package. *Addiction*, *89*(5), 563-572. https://doi.org/10.1111/j.1360-0443.1994.tb03332.x
- Rethlefsen, M. L., Kirtley, S., Waffenschmidt, S., Ayala, A. P., Moher, D., Page, M. J., Koffel, J. B., PRISMA-S Group, Blunt, H., Brigham, T., Chang, S., Clark, J., Conway, A., Couban, R., de Kock, S., Farrah, K., Fehrmann, P., Foster, M., Fowler, S. A., …, & Young, S. (2021). PRISMA-S: an extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews. *Systematic Reviews*, *10*(1), 39. https://doi.org/10.1186/s13643-020-01542-z
- Rogers, J. M., Weiss, S. T., Epstein, D. H., Grundmann, O., Hill, K., & Smith, K. E. (2024). Kratom addiction per DSM-5 SUD criteria, and kratom physical dependence: Insights from dosing amount versus frequency. *Drug and Alcohol Dependence*, *260*, 111329. https://doi.org/10.1016/j.drugalcdep.2024.111329
- Saingam, D., Assanangkornchai, S., Geater, A. F., & Lerkiatbundit, S. (2014). Validation of Krathom ( Mitragyna speciosa Korth.) Dependence Scale (KDS): A Dependence Screen for Internationally Emerging Psychoactive Substance. *Substance Abuse*, *35*(3), 276-283. https://doi.org/10.1080/08897077.2014.924464
- Schwarzer, G., Chemaitelly, H., Abu‐Raddad, L. J., & Rücker, G. (2019). Seriously misleading results using inverse of Freeman‐Tukey double arcsine transformation in meta‐analysis of single proportions. *Research Synthesis Methods*, *10*(3), 476-483. https://doi.org/10.1002/jrsm.1348
- Shamseer, L., Moher, D., Clarke, M., Ghersi, D., Liberati, A., Petticrew, M., Shekelle, P., Stewart, L. A., & the PRISMA-P Group (2015). Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015: elaboration and explanation. *BMJ*, *349*(jan02 1), g7647-g7647. https://doi.org/10.1136/bmj.g7647
- Singh, D., Abdullah, M. F., Vicknasingam, B. K., & Müller, C. P. (2019). Substance Use Disorder Related to Kratom (Mitragyna speciosa) Use in Malaysia. *Current Psychopharmacology*, *8*(1), 64-71. https://doi.org/10.2174/2405461503666180420120649
- Singh, D., Müller, C. P., & Vicknasingam, B. K. (2014). Kratom (Mitragyna speciosa) dependence, withdrawal symptoms and craving in regular users. *Drug and Alcohol Dependence*, *139*, 132-137. https://doi.org/10.1016/j.drugalcdep.2014.03.017
- Smith, K. E., Dunn, K. E., Rogers, J. M., Garcia-Romeu, A., Strickland, J. C., & Epstein, D. H. (2022). Assessment of Kratom Use Disorder and Withdrawal Among an Online Convenience Sample of US Adults. *Journal of Addiction Medicine*, *16*(6), 666-670. https://doi.org/10.1097/adm.0000000000000986
- Stanciu, C. N., Gnanasegaram, S. A., Ahmed, S., & Penders, T. (2019). Kratom Withdrawal: A Systematic Review with Case Series. *Journal of Psychoactive Drugs*, *51*(1), 12-18. https://doi.org/10.1080/02791072.2018.1562133
- Stijnen, T., Hamza, T. H., & Özdemir, P. (2010). Random effects meta-analysis of event outcome in the framework of the generalized linear mixed model with applications in sparse data. *Statistics in Medicine*, *29*(29), 3046-3067. https://doi.org/10.1002/sim.4040
- Swogger, M. T., & Walsh, Z. (2018). Kratom use and mental health: A systematic review. *Drug and Alcohol Dependence*, *183*, 134-140. https://doi.org/10.1016/j.drugalcdep.2017.10.012
- van den Akker, O. R., Peters, G. J. Y., Bakker, C. J., Carlsson, R., Coles, N. A., Corker, K. S., Feldman, G., Moreau, D., Nordström, T., Pickering, J. S., Riegelman, A., Topor, M. K., van Veggel, N., Yeung, S. K., Call, M., Mellor, D. T., & Pfeiffer, N. (2023). Increasing the transparency of systematic reviews: presenting a generalized registration form. *Systematic Reviews*, *12*(1), 170. https://doi.org/10.1186/s13643-023-02281-7
- Van den Noortgate, W., López-López, J. A., Marín-Martínez, F., & Sánchez-Meca, J. (2013). Three-level meta-analysis of dependent effect sizes. *Behavior Research Methods*, *45*(2), 576-594. https://doi.org/10.3758/s13428-012-0261-6
- Waffenschmidt, S., Knelangen, M., Sieben, W., Bühn, S., & Pieper, D. (2019). Single screening versus conventional double screening for study selection in systematic reviews: a methodological systematic review. *BMC Medical Research Methodology*, *19*(1), 132. https://doi.org/10.1186/s12874-019-0782-0
- Yang, Y., Müller, C. P., & Singh, D. (2024). Kratom (Mitragyna speciosa) Use and Mental Health: A Systematic Review and Multilevel Meta-Analysis. *European Addiction Research*, *30*(4), 252-274. https://doi.org/10.1159/000539338
- Registration cited: PROSPERO CRD420261530340 (https://www.crd.york.ac.uk/PROSPERO/view/CRD420261530340).
