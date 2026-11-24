# Регистрация на OSF: пошагово и тексты полей

Шаблон — **Generalized Systematic Review Registration** (van den Akker et al., 2023, https://doi.org/10.1186/s13643-023-02281-7), тот же, что у мизофонии и ставок на спорт: 61 текстовое поле и 2 поля для файлов. Тексты ниже на английском, вставляются как есть.

## Шаги

С 16.11.2026 OSF не создаёт новые проекты (переход платформы; help.osf.io, статьи 759 и 768). Регистрации это не касается: их создают **без проекта**, а файлы загружают прямо в поля формы (всего до 5 ГБ). Шаблон Generalized Systematic Review остаётся.

1. **Новая регистрация без проекта.** https://osf.io → *My Registrations* → **Add a Registration** (или сразу https://osf.io/registries/osf/new):
   - на вопрос «Do you have content for registration in an existing OSF project?» — **No**;
   - шаблон — **Generalized Systematic Review Registration** → *Create Draft*. Черновик сохраняется сам, ссылка придёт на почту; черновики — https://osf.io/my-registrations?tab=drafts.
2. **Метаданные:** Title — `Prevalence of kratom use disorder and dependence among people who use kratom: systematic review and meta-analysis`; Description — ниже; License — *CC-By Attribution 4.0 International*; Subjects — *Social and Behavioral Sciences → Psychology → Clinical Psychology* и *Medicine and Health Sciences → Public Health*; Tags — ниже; Contributors — только вы.
3. **Поля формы** — по разделам ниже, тексты вставляются как есть.
4. **Файлы** — из `registration/osf_package/`, прямо в поля с файлами:
   - поле после *Screener instructions* (раздел Screening): `llm_screener_prompt.md`, а также `Rekhert_kratom_protocol_v1.0.pdf` (протокол) и `kratom-prereg-v1.0.zip` (весь пакет: протокол, формы, скрипты поиска и отбора, логи проверочного прогона, README);
   - поле после *Extractor instructions* (раздел Extraction): `extraction_codebook.md`.
   - Если поле берёт только один файл — в Screening загрузите `kratom-prereg-v1.0.zip`: в нём есть и протокол, и промпт. После отправки файлы уже не добавить.
5. **Отправка.** *Review* → *Register* → **Make registration public immediately**.
6. **Мне:** ссылку (`https://osf.io/xxxxx`) и DOI (`10.17605/OSF.IO/XXXXX`). Я впишу их в протокол и README и запущу финальный поиск; после него — калибровка вслепую.

---

## Metadata

**Description.** Protocol (v1.0) of a systematic review and meta-analysis of the prevalence of kratom use disorder and kratom dependence among people who use kratom (Mitragyna speciosa). Estimates are pooled separately for each case-definition level (any use disorder; moderate-to-severe use disorder or dependence, including dependence scales and ASSIST high risk; severe use disorder) across all sample types, and separately for Southeast Asia, where kratom leaves are used traditionally, and North America, where kratom is sold as a commercial product. Sources of heterogeneity (sample type, regular use, instrument, product form, recruitment channel) are examined with a three-level model. Screening uses a blind calibration sample and two independent AI passes; all final decisions are the author's.

**Tags.** kratom; Mitragyna speciosa; kratom use disorder; dependence; substance use disorder; prevalence; meta-analysis; systematic review; DSM-5; Southeast Asia; United States; LLM-assisted screening

---

## Review Methods

**Type of review**
Systematic review and meta-analysis of prevalence (proportions), with a random-effects binomial–normal GLMM on the logit scale, a three-level moderator model and meta-regression. The protocol follows PRISMA-P 2015; the review will be reported per PRISMA 2020 and PRISMA-S. Review question framed with CoCoPop (condition: kratom use disorder or dependence; context: any country and year; population: people who use kratom, not recruited because of kratom problems).

**Review stages**
Preparation (novelty check, protocol, check run of the search) → Registration (OSF) → Final search → Title/abstract screening: blind calibration by the reviewer on 300 random records, two independent AI passes on all records, reviewer decision on every record that either pass keeps, conditional blind screening of double AI exclusions → Full-text screening (open-access texts only; AI proposal, reviewer decision) → Citation searching of included studies → Completion of the instrument-threshold table → Data extraction (AI draft, reviewer verification of every value) → Risk of bias (JBI prevalence checklist; AI draft, reviewer decision) → Synthesis → GRADE → Manuscript.

**Current review stage**
Protocol frozen on 21 November 2026 (v1.0, git tag kratom-prereg-v1.0); the files uploaded here are built from that tag, unchanged. A check run of the frozen search code ran on 21 November 2026 (17,528 records, 4,385 unique, 2,304 to screen, recall 9 of 9 on the seed set; stand test of the screener prompt: 13 of 13 records labelled as expected by both passes). The final search, screening and all later stages start after this registration. No study has been screened.

**Start date**
The author has followed and read the literature on kratom use since 2022; work on this review (topic scoping and the first novelty check) started on 2026-11-15.

**End date**
Not fixed in advance.

**Background**
Kratom (Mitragyna speciosa) leaves contain mitragynine and 7-hydroxymitragynine, alkaloids with partial agonist activity at the μ-opioid receptor. In Thailand and Malaysia the leaves are chewed or brewed traditionally; in the United States and Europe kratom is sold as powders, capsules and extracts, and since 2025 also as concentrated 7-hydroxymitragynine products. Pooled estimates exist only for neighbouring questions: the prevalence of kratom use in populations (El-Sehrawy et al., 2026) and correlations between kratom use and mental health (Yang, Müller & Singh, 2024). No published meta-analysis estimates the proportion of people who use kratom who meet criteria for kratom use disorder or dependence. One registered broad clinical review (PROSPERO CRD420261530340) lists this prevalence among many outcomes. Single-study estimates range from a minority of US consumers recruited online to most or nearly all regular users of traditional kratom tea in Malaysia; a definition-aware pooled estimate that examines this variation is missing.

**Primary research question(s)**
What is the pooled prevalence of moderate-to-severe kratom use disorder or kratom dependence (DSM-5 ≥ 4 criteria, DSM-IV dependence, ICD dependence, a dependence scale at a fixed cut-off, ASSIST high risk, or dependence by interview) among people who use kratom?

**Secondary research question(s)**
(1) Pooled prevalence at each case-definition level: any use disorder (DSM-5 ≥ 2 criteria, DSM-IV abuse or dependence, ICD harmful use or dependence), moderate-to-severe disorder or dependence, severe disorder (DSM-5 ≥ 6 criteria). (2) Prevalence in Southeast Asia and in North America, and by sample type (community users, online consumers, people who use other drugs, patients in treatment for another substance, psychiatric patients, students and youth, kratom users within population surveys). (3) Sources of heterogeneity: instrument, regular use required for entry, reference period, product form, other opioid use, recruitment through advocacy or vendor channels, year, age, sex composition, risk of bias.

**Expectations / hypotheses**
Expectations stated in advance, to be checked rather than tested as confirmatory hypotheses: prevalence decreases from any use disorder to severe disorder; samples from Southeast Asia give higher estimates than samples from North America; samples that require regular or daily use give higher estimates than samples of any users; samples recruited through advocacy or vendor channels give lower estimates.

**Dependent variable(s) / outcome(s) / main variables**
Proportion of people who use kratom meeting a case definition of kratom use disorder or dependence (cases / N), recorded for every case definition × sample × subgroup. Case-definition levels are fixed in the protocol (§13) and the instrument-threshold table (forms/instrument_thresholds.csv), applied regardless of the authors' labels. Primary outcome: level L2 (moderate-to-severe disorder or dependence).

**Independent variable(s) / intervention(s) / treatment(s)**
Not applicable (prevalence review). The population is people who use kratom (leaves, tea, decoction, kratom cocktail, powders, capsules, extracts, 7-hydroxymitragynine products) in a stated reference period, not recruited because of kratom problems. Other Mitragyna species are not kratom.

**Additional variable(s) / covariate(s)**
Moderators (protocol §15b): case-definition level, region and regular use required for entry (pre-specified multivariable model); instrument within L2; sample type; reference period of use; product form; share with non-prescribed opioid use; recruitment through kratom advocacy or vendor channels; year of data collection; mean age; percentage male; JBI items 2, 6 and 9; publication status; kratom-industry funding.

**Software**
Python 3.12 (search via the PubMed E-utilities, Europe PMC, OpenAlex, Semantic Scholar, Scopus Search, Crossref, DataCite, OpenAIRE and CORE APIs; de-duplication; calibration sampling) — search/search.py, search/dedup.py, search/recall.py. Markdown decision files written and parsed by screening/screen_md.py. Claude Code in headless mode running Claude Opus 5.5 (claude-opus-5-5) and Claude Sonnet 5.5 (claude-sonnet-5-5) for AI drafts (screening/llm_screen.py). R 4.6.1 with metafor, lme4 and clubSandwich for the analysis.

**Funding**
None. The review is unfunded.

**Conflicts of interest**
None. The author has no financial or professional relationship with kratom vendors, kratom advocacy organisations, organisations campaigning for kratom regulation, or any instrument's developers. The AI assistant used as a tool is produced by Anthropic; the author has no relationship with Anthropic beyond a paid subscription.

**Overlapping authorships**
None. The author has not authored or co-authored any study likely to be included.

---

## Search Strategy

**Databases**
PubMed; Europe PMC (MEDLINE, PMC and preprints from medRxiv, Research Square, PsyArXiv, SSRN, Preprints.org); OpenAlex (including non-English terms); Semantic Scholar; Scopus (Search API: titles and identifiers, no abstracts); Crossref (posted content, reports, theses, Southeast Asian journals that deposit DOIs); DataCite (theses, OSF, Zenodo, figshare); OpenAIRE Graph; CORE. No subscription access to Web of Science, PsycINFO or Embase.

**Interfaces**
PubMed — NCBI E-utilities; Europe PMC — REST API (searchPOST); OpenAlex — API (title_and_abstract.search; openalex: filter for citation searching); Semantic Scholar — Graph API bulk search; Scopus — Elsevier Search API (STANDARD view, start-based paging); Crossref — REST API (query.bibliographic, sorted by score); DataCite — REST API; OpenAIRE Graph — API v1 (researchProducts); CORE — API v3. All run from search/search.py.

**Grey literature**
Reports and theses through Crossref, DataCite, OpenAlex, OpenAIRE and CORE; preprints through Europe PMC, OpenAlex, Crossref and DataCite.

**Inclusion and exclusion criteria**
Framework: CoCoPop. Inclusion: (I1) a sample or reported subsample of people who use kratom in a stated reference period (regular use allowed and coded); (I2) not recruited because of kratom problems; (I3) kratom use disorder or dependence assessed with DSM-5 criteria (checklist or interview), DSM-IV abuse or dependence criteria, ICD-10 or ICD-11 criteria, a dependence scale (KDS, SDS and others) at a fixed cut-off, ASSIST, or a diagnostic interview; (I4) number or proportion meeting a case definition with the denominator; (I5) any language, year and publication status. Exclusion: (E1) samples recruited because of kratom problems (treatment for kratom use disorder or withdrawal, kratom-related emergency or poison-centre cases); (E2) case counts only for whole samples including people who do not use kratom; (E3) cut-offs from the sample's own distribution (recorded, not pooled); (E4) withdrawal alone, frequency or quantity of use, single self-identification items (recorded, not pooled); (E5) reviews, editorials, qualitative studies without counts, case reports and case series; (E6) duplicate reports; (E7) pharmacokinetic or safety studies in people who do not use kratom, preclinical studies.

**Query strings**
Concept A (kratom), searched in every source: kratom, kratoms, krathom, kratum, ketum, kakuam, biak-biak, "Mitragyna speciosa", mitragynine, 7-hydroxymitragynine, mitragynine pseudoindoxyl.
PubMed: each term in [tiab] OR kratom*[tiab] OR "Mitragyna"[Mesh].
Europe PMC: TITLE_ABS:"<term>" for each term, joined by OR.
OpenAlex: title_and_abstract.search with the terms joined by |.
OpenAlex, non-English: กระท่อม, ใบกระท่อม, кратом, митрагинин, クラトム, ミトラガイニン, 卡痛, 帽柱木, 크라톰, daun ketum, air ketum, daun kratom.
Semantic Scholar: bulk search with the terms joined by |.
Scopus: TITLE-ABS-KEY(kratom OR krathom OR kratum OR ketum OR kakuam OR "biak-biak" OR "mitragyna speciosa" OR mitragynine OR "7-hydroxymitragynine").
Crossref: queries kratom, kratom use, kratom users, kratom dependence, kratom use disorder, ketum, krathom, Mitragyna speciosa, mitragynine; records kept while title or abstract contains a kratom term; a query stops at the first page of 1,000 with fewer than five such records.
DataCite: titles, descriptions and subjects with the terms.
OpenAIRE Graph and CORE: kratom, krathom, ketum, Mitragyna speciosa, mitragynine (CORE: title or abstract, one query per term).
Concept B (people who use kratom, or dependence), applied to title and abstract after retrieval by search/dedup.py, identically for all sources: dependence terms (depend*, use disorder, addict*, withdraw*, DSM, ICD, craving, toleran*, problematic, compulsive, abuse, misuse, harmful use, loss of control, SDS, KDS, substance use) or human-sample terms (user(s), consumer(s), respondent(s), participant(s), survey, questionnaire, interview, cross-sectional, people/persons/individuals who, prevalence, epidemiolog*, student(s), adolescent(s), youth, general population, villager(s), chewer(s), eater(s), drinker(s), regular or daily use; Malay and Indonesian equivalents). Records without an abstract pass on a broader title list (use, using, consum*, user, depend*, addict*, withdraw*, disorder, abuse, misuse, survey, people, patient(s), treatment, chew*, eat*, drink*, smok*, habit, epidem*, prevalen*, social, psych*, health, clinic*). Records in Thai, Chinese, Japanese, Korean or Cyrillic script and records found only by citation searching skip concept B.

**Search validation procedure**
Recall is checked against a seed set of nine studies of people who use kratom that assessed use disorder or dependence, taken from the reference lists of Yang et al. (2024), El-Sehrawy et al. (2026), Smith et al. (2022) and Hill et al. (2024) (search/seed_set.csv), built before the check run. Check run on 21 November 2026: 9 of 9. Recall is reported again for the final search; any miss is examined.

**Other search strategies**
Backward citation searching of seven syntheses on kratom use (search/search.py, source "citations"); after full-text screening, backward and forward citation searching of the included studies through OpenAlex, with the same screening procedure.

**Procedures to contact authors**
Authors are not contacted (the author's decision, as in the author's previous reviews). Studies without extractable counts are listed as such.

**Results of contacting authors**
Not applicable.

**Search expiration and repetition**
If more than six months pass between the final search and submission, the search is updated with the same strings and code; only new records are screened, by the same procedure. No living review is planned.

**Search strategy justification**
The literature on kratom is small (a few thousand records in total) and dominated by pharmacology, chemistry, botany and case reports. Concept A alone finds all of it; concept B, applied identically to title and abstract of every record, removes records that mention neither people who use kratom nor dependence, so that the AI passes and the reviewer screen only records that could report a prevalence among people. Records without abstracts pass on a broad title list, and non-English-script records skip concept B. The seed set checks recall.

**Miscellaneous search strategy details**
All automated searches run from search/search.py, which logs query strings, dates, record counts and timings (search_log.json). De-duplication (search/dedup.py, from the author's earlier reviews) merges records on DOI (ignoring version suffixes), PMID and exact normalised title with years within ±1; pointer sources are attached to the database record with the same title; records typed as non-study records by every source, vendor advertising found only outside PubMed, Europe PMC and Scopus (rule 6), and records outside concept B (rule 7) are removed before screening and listed with the reason.

---

## Screening

**Screening stages**
(1) Title and abstract: blind calibration by the reviewer on 300 random records; two independent AI passes (Claude Opus 5.5 and Claude Sonnet 5.5) on all records; the reviewer decides every record that at least one pass labelled include or unsure; records excluded by both passes are excluded unless the safeguard is triggered. (2) Full text: open-access texts only; the AI drafts a proposal (eligible or not, reason, location of the counts); the reviewer decides every report.

**Screened fields / blinding**
Title, abstract, year, venue, record type, language and DOI link; author names are not shown. In the calibration sample the reviewer sees no AI labels; in verification both AI labels and notes are shown. The AI passes see title, year, venue, record type and abstract, not the record ID or authors.

**Used exclusion criteria**
At title and abstract: 1 review, commentary or regulatory paper; 2 qualitative study without counts, or preclinical, chemical, botanical or analytical study; 3 no dependence or use-disorder measure for kratom; 4 case report, case series, toxicology or poison-centre data; 5 sample recruited because of kratom problems; 6 not kratom (other Mitragyna species) or not about people who use it; 7 other, with a note. At full text: the criteria E1–E7 above.

**Screener instructions**
The AI screener prompt is uploaded (llm_screener_prompt.md). Reviewer instructions sit at the top of every Markdown decision file (screening/screen_md.py): codes + include, ? unsure, -1…-7 exclude with reason, = accept the AI label when both passes agree; "in doubt — unsure".

**Screening reliability**
Agreement between the reviewer's blind calibration decisions and each AI pass and their union: Cohen's κ and Gwet's AC1; sensitivity and specificity of the rule "exclude only if both passes exclude" with Clopper–Pearson 95% CIs; agreement between the two AI passes.

**Screening reconciliation procedure**
The reviewer's decision is final. Safeguard: if any calibration record that the reviewer labelled include or unsure was excluded by both AI passes, the reviewer screens, with labels hidden and in random order (seed 20261122), every double-excluded record outside the calibration sample that has a human-sample term in title or abstract or has no abstract; records the reviewer then marks include or unsure go to full text.

**Sampling and sample size**
Calibration sample: 300 records drawn with random.Random(20261121).sample over the sorted record IDs of the final screening list (screening/calibration.py).

**Screening procedure justification**
Single-reviewer screening misses about 13% of eligible studies (Waffenschmidt et al., 2019); LLM screeners reach high sensitivity on titles and abstracts (Oami et al., 2024). Two independent AI passes reduce the chance of a missed record, the blind calibration measures the miss rate of the AI rule, and the safeguard returns double exclusions to the reviewer if the rule misses even one calibration record. The same scheme was used in the author's reviews of AI dependence and sports betting.

**Data management and sharing**
Decision files, AI label files (with SHA-256 hashes committed before unblinding), the prompt hash and the Claude Code version for every AI decision are kept in git and released with the data on GitHub and Zenodo at submission.

**Miscellaneous screening details**
Reports of one sample are linked and counted once (site, years and sample size). Full-text, extraction and risk-of-bias prompts are written before full-text screening, piloted on three studies, frozen with git tags and committed before use. Non-English full texts are machine-translated by the AI assistant; the reviewer checks numbers against the original tables.

---

## Extraction

**Entities to extract**
Per sample: report details, country and region, years of data collection, design, sampling, sample type, recruitment channel, reference period of use, regular use required, product form, n analysed, age, percentage male, share with non-prescribed opioid use, instruments, funding and kratom-industry funding, JBI items. Per estimate: subgroup, instrument, threshold and its source, authors' label, level (L1, L2, L2-scale, L2-screen, L3, ad hoc), time frame, cases, denominator, location in the report. Codebook uploaded (extraction_codebook.md).

**Extraction stages**
(1) Completion of the instrument-threshold table from development and validation papers only, before extraction. (2) AI draft of every field with source location and quote, stored unchanged. (3) Reviewer verification of every value against the source in Markdown files (extraction/verify_md.py).

**Extractor instructions**
Codebook uploaded (extraction_codebook.md): field rules, extraction rules for subgroups, DSM-5 severity categories, disagreements between text and tables, cohort waves and overlapping reports.

**Extractor masking**
None.

**Extraction reliability**
Single reviewer verifying an AI draft. Reported: share of AI values corrected by the reviewer (overall and for key fields) and share of AI quotes found verbatim in the source.

**Extraction reconciliation procedure**
The reviewer's value is final. Automatic checks: cases ≤ n; cumulative levels consistent (L3 ≤ L2 ≤ L1); category counts add up; percentages match counts within rounding; retractions checked through Crossref.

**Extraction procedure justification**
AI drafts with source locations make full verification by a single reviewer feasible; every value is checked against the source, and key fields always against the source table.

**Data management and sharing**
AI drafts, verification files and final tables (forms/samples.csv, forms/estimates.csv) are kept in git and released on GitHub and Zenodo at submission.

**Miscellaneous extraction details**
The form is piloted on three studies; any rule added in the pilot goes to deviations.md with a date.

---

## Synthesis and Quality Assessment

**Planned data transformations**
Cumulative levels built from category counts (DSM-5 mild, moderate, severe); cases derived from percentages and denominators where needed (flagged); logit transformation within the GLMM.

**Missing data**
Samples without extractable counts are listed, not imputed. Missing moderator values are coded as not reported; moderator analyses use the samples with data.

**Data validation**
Automatic consistency checks (see Extraction reconciliation) and reviewer verification of every value against the source.

**Quality assessment**
JBI Critical Appraisal Checklist for Studies Reporting Prevalence Data (Munn et al., 2014, 2015), nine items, decision rules adapted to people who use kratom (forms/rob_jbi.md; sample size n ≥ 246 for ±5 percentage points at an expected 20%). AI draft with quotes; reviewer decision. No summary score. GRADE adapted for event rates (Iorio et al., 2015).

**Synthesis plan**
Random-effects binomial–normal GLMM on the logit scale (metafor::rma.glmm, measure = "PLO") for each level, region and sample type with at least three independent samples; 95% CI and 95% prediction interval; τ² and I². One estimate per sample per analysis by a fixed priority (interview; DSM-5 criteria item by item; DSM-IV or ICD criteria; dependence scale; ASSIST; then the authors' primary; then the median logit). Three-level moderator model using all estimates (lme4::glmer, binomial; check with metafor::rma.mv and cluster-robust inference): pre-specified multivariable model with level, region and regular use required; exploratory moderators one at a time when k ≥ 10.

**Criteria for conclusions / inference criteria**
The review is descriptive: estimates are interpreted through their CIs and prediction intervals and graded with GRADE; differences between subgroups are described with their CIs and moderator tests, without confirmatory hypothesis tests.

**Synthesist blinding**
None.

**Synthesis reliability**
Analysis code is released; results are reproduced from a clean copy of the repository before submission.

**Synthesis reconciliation procedure**
Not applicable (single author).

**Publication bias analyses**
Funnel-plot asymmetry tests are not used as inference for proportions (Hunter et al., 2014); logit prevalence is plotted against its standard error, prevalence is regressed on 1/√n, and peer-reviewed estimates are compared with grey literature. Kratom-industry funding and recruitment through advocacy or vendor channels are tested as moderators.

**Sensitivity analyses / robustness checks**
On the primary outcome: (1) DSM, ICD and interview estimates only (no scales or ASSIST); (2) probability, census or consecutive samples; (3) valid identification (JBI item 6 = yes); (4) response rate ≥ 60%; (5) excluding patients in treatment for another substance and psychiatric patients; (6) excluding advocacy- or vendor-recruited or industry-funded samples; (7) excluding preprints, theses, conference abstracts and reports; (8) excluding n < 100; (9) inverse-variance REML pooling of logits with Hartung–Knapp; (10) leave-one-out and influence diagnostics.

**Synthesis procedure justification**
GLMMs avoid the problems of transformed-proportion pooling and Freeman–Tukey back-transformation (Stijnen et al., 2010; Schwarzer et al., 2019; Lin & Chu, 2020); prediction intervals convey heterogeneity (IntHout et al., 2016; Migliavaca et al., 2022); three-level models use all estimates without double counting samples (Van den Noortgate et al., 2013).

**Synthesis data management and sharing**
Analysis scripts, data and results are released on GitHub with a Zenodo DOI at submission.

**Miscellaneous synthesis details**
Fewer than three samples in a stratum: estimates are tabulated and shown in forest plots without a pooled value.
