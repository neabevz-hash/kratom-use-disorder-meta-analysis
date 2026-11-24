# Проверка выписывания — файл 3 из 3

Черновик заполнил ИИ (Claude Opus 5.5) по полному тексту; у каждого значения указано место и цитата. Проверяете вы, один проход.

**Как проверять выборку:**
1. Откройте полный текст по ссылке у исследования.
2. **Ключевые числа** — сверить с таблицей или текстом статьи всегда: в таблице оценок шкала, порог, уровень, случаи и n; под таблицей n_users, sample_type, sampling, use_period, region.
3. Остальные поля и пункты JBI: проверить, что значение есть в цитате и место указано верно.
4. Неверное — исправьте строкой в блоке «Правки» этой выборки (по одной правке на строку):
   - `n_users = 395`, `sampling = convenience` — поле выборки;
   - `E2.cases = 78`, `E2.level = L2` — поле оценки E2 (subgroup, instrument, threshold, cumulative, level, cases, n, time_frame, primary_for_authors и др.);
   - `E2 удалить` — убрать оценку;
   - `+ оценка: subgroup=all; instrument=DSM-5-SUD; threshold=DSM-5 criteria>=4; cumulative=yes; level=L2; time_frame=past 12 months; cases=50; n=300; location=Table 2` — добавить оценку;
   - `jbi_6 = no` — пункт JBI;
   - `выборка удалить: причина` — если это не отдельная выборка или её нельзя брать;
   - после `#` — комментарий для Claude.
5. Когда выборка проверена, напишите `да` после «Проверено:».

**Как выписаны оценки.** Категории — как в статье (для DSM-5 обычно «нет», лёгкое, умеренное, тяжёлое; пожизненно и за год — отдельными строками); суммы «4 и выше» строит анализ, не вы. **cumulative** = yes, если категория открыта вверх («≥2», «6+»), no — закрытая полоса («2–3», «14–34»). **Уровень** — по нижней границе категории (таблица порогов, C1): DSM-5 и SUDST 0–1 → below, 2–3 → L1, 4–5 → L2, 6+ → L3; KDS 0–13 → below, 14+ → L2-scale; SDS и LDQ по порогу авторов → L2-scale; ASSIST 27+ → L2-screen; самодельные вопросы → not_levelled; порог по распределению выборки → E3.

**Подсказки в файле:** «⚠ Проверка скриптом» — где скрипт нашёл повод присмотреться (уровень не совпадает с таблицей порогов, категории не складываются в n, n оценки не равно n_users). «Расхождения в тексте» — ошибки самих авторов, которые нашёл ИИ. Посчитанные ИИ значения (% × n) выделены строкой **расчёт**.

**sample_type:** community_users, online_consumers, drug_users, treatment_other_sud, psychiatric_patients, students_youth, population_subsample, other. **sampling:** probability, census, respondent-driven, snowball, convenience, online opt-in, clinical consecutive, NR.

---

## ST12 · Hill 2024 · Journal of addiction medicine

Основной отчёт R1255: [текст](../../fulltext/text/R1255.txt) · [PDF](../../fulltext/pdf/R1255.pdf) — «Prevalence of Kratom Use Disorder Among Kratom Consumers.» — [DOI](https://doi.org/10.1097/adm.0000000000001290)
Расхождения в тексте: 1) Discussion (p.5) says 'a severe disorder being present among 13.9% of participants'. In Table 2, 13.9% is 73 of the 525 with KUD; of all 2061 participants it is 3.5%. Table counts used. 2) Severity counts add up (347+105+73=525). Frequency rows add up for KUD (525) and for the totals (2061). 3) Table 1 Education: the full-sample HS/GED figure of 456 does not equal KUD 118 + no-KUD 347 = 465, and the full-sample column sums to 2042. 4) Table 3 footnote **: leaves full-sample n=322, but KUD 14 + no-KUD 43 = 57. The 'Receive treatment' footnote gives full n=322, while 332 report an SUD diagnosis. 5) Geography is based on N=2009; 136 (6.8%) lived outside the United States, so the sample is not purely US. 6) The abstract's tolerance 81.3% and withdrawal 68.0% are among KUD cases; full-sample figures are 31.4% and 21.7% (Table 2).
Заметка ИИ: Draft for human check. The time frame of the DSM-5 criteria is not reported, so it is NR for every estimate. Appendix 1 (the survey) and the supplementary tables were not received. The cited earlier surveys (Garcia-Romeu 2020; Smith 2022) are separate samples and do not overlap with this 2023 survey.

### ST12-1 · US current kratom consumers, online survey (AKA listserv + Facebook), 2023, n=2061
Отчёты: R1255 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | DSM-5-SUD · DSM-5 criteria>=2 of 11 | **L1** | **525 / 2061** | 25.5 | Page 2, Results; Table 1 header; Abstract | «Among the total sample (N = 2061), KUD criteria were met by 25.5% of participants (n = 525)» |
| E2 | all | DSM-5-SUD · DSM-5 criteria 0-1 (none) | **below** | **1536 / 2061** | 74.5 | Page 3, Table 1 header | «Full Sample (N = 2061) KUD (n = 525) No KUD (n = 1536)» |
| E3 | all | DSM-5-SUD · DSM-5 criteria 2-3 (mild) | **L1** | **347 / 2061** | 16.8 | Page 3, Table 2 (Severity); Page 2, Results | «Of those who met the KUD criteria, most met criteria for a mild KUD (n = 347, 66.1%).» |
| E4 | all | DSM-5-SUD · DSM-5 criteria 4-5 (moderate) | **L2** | **105 / 2061** | 5.1 | Page 3, Table 2 (Severity) | «Moderate — — 105 20.0 — —» |
| E5 | all | DSM-5-SUD · DSM-5 criteria>=6 (severe) | **L3** | **73 / 2061** | 3.5 | Page 3, Table 2 (Severity) | «Severe — — 73 13.9 — —» |
| E6 | male | DSM-5-SUD · DSM-5 criteria>=2 of 11 | **L1** | **315 / 1078** | 29.2 | Page 3, Table 1 (Gender) | «Male 1078 52.3 315 60.0 763 49.7» |
| E7 | female | DSM-5-SUD · DSM-5 criteria>=2 of 11 | **L1** | **200 / 945** | 21.2 | Page 3, Table 1 (Gender) | «Female 945 45.9 200 38.1 745 48.5» |
| E8 | once daily users | DSM-5-SUD · DSM-5 criteria>=2 of 11 | **L1** | **48 / 224** | 21.4 | Page 4, Table 3 (How often use kratom) | «Once daily 224 10.9 48 9.1 176 11.5» |
| E9 | twice daily users | DSM-5-SUD · DSM-5 criteria>=2 of 11 | **L1** | **85 / 438** | 19.4 | Page 4, Table 3 (How often use kratom) | «Twice daily 438 21.3 85 16.2 353 23.0» |
| E10 | three times daily users | DSM-5-SUD · DSM-5 criteria>=2 of 11 | **L1** | **109 / 464** | 23.5 | Page 4, Table 3 (How often use kratom) | «Three times daily 464 22.5 109 20.8 355 23.1» |
| E11 | four times daily users | DSM-5-SUD · DSM-5 criteria>=2 of 11 | **L1** | **112 / 373** | 30.0 | Page 4, Table 3 (How often use kratom) | «Four times daily 373 18.1 112 21.3 261 17» |
| E12 | five times daily users | DSM-5-SUD · DSM-5 criteria>=2 of 11 | **L1** | **63 / 151** | 41.7 | Page 4, Table 3 (How often use kratom) | «Five times daily 151 7.3 63 12.0 88 5.7» |
| E13 | six times daily users | DSM-5-SUD · DSM-5 criteria>=2 of 11 | **L1** | **35 / 93** | 37.6 | Page 4, Table 3 (How often use kratom) | «Six times daily 93 4.5 35 6.7 58 3.8» |
| E14 | frequency 'Other' | DSM-5-SUD · DSM-5 criteria>=2 of 11 | **L1** | **73 / 318** | 23.0 | Page 4, Table 3 (How often use kratom) | «Other 318 15.4 73 13.9 245 16» |

- E1: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=2 criteria = L1; у авторов: «kratom use disorder (KUD)»; главная у авторов: yes; период: NR; заметка: Time frame of the criteria not stated in the methods.
- E2: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 0-1 criteria = below; у авторов: «No KUD»; главная у авторов: no; период: NR
- E3: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 2-3 criteria = L1; у авторов: «mild»; главная у авторов: no; период: NR; заметка: The printed 66.1% is of the 525 with KUD; the count is used here with the whole-sample denominator of 2061 (16.8%).
- E4: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 4-5 criteria = L2; у авторов: «moderate»; главная у авторов: no; период: NR; заметка: The printed 20.0% is of the 525 with KUD; whole-sample share 105/2061 = 5.1%.
- E5: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=6 criteria = L3; у авторов: «severe»; главная у авторов: no; период: NR; заметка: The printed 13.9% is of the 525 with KUD; whole-sample share 73/2061 = 3.5%. The Discussion wrongly says 13.9% 'of participants'.
- E6: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=2 criteria = L1; у авторов: «KUD»; главная у авторов: no; период: NR; заметка: No severity breakdown by sex.
- E7: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=2 criteria = L1; у авторов: «KUD»; главная у авторов: no; период: NR; заметка: Also reported: nonbinary 7/19; prefer not to say 3/19.
- E8: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=2 criteria = L1; у авторов: «KUD»; главная у авторов: no; период: NR
- E9: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=2 criteria = L1; у авторов: «KUD»; главная у авторов: no; период: NR
- E10: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=2 criteria = L1; у авторов: «KUD»; главная у авторов: no; период: NR
- E11: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=2 criteria = L1; у авторов: «KUD»; главная у авторов: no; период: NR
- E12: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=2 criteria = L1; у авторов: «KUD»; главная у авторов: no; период: NR
- E13: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=2 criteria = L1; у авторов: «KUD»; главная у авторов: no; период: NR
- E14: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=2 criteria = L1; у авторов: «KUD»; главная у авторов: no; период: NR; заметка: 'Other' frequency is not defined. It may include non-daily users, so it should not be coded as non-daily.

**Ключевые поля выборки:**
- **n_users: 2061** — Page 2, Results; Table 1 — «After restricting the dataset, a total of 2061 participants were included in the analysis»
- **sample_type: online_consumers** — Page 2, Methods, Sampling Procedures — «our cross-sectional, online survey was open to current kratom consumers and was hosted on Qualtrics»
- **sampling: online opt-in** — Page 2, Methods, Sampling Procedures — «Nonprobability sampling was used. We recruited from multiple sources to improve reach and voluntary response rates.»
- **use_period: current** — Page 2, Methods, Data Collection — «The survey began with an initial screening question to ensure participants reported current kratom consumption and were 18 years or older.»
- **region: North America** — Page 2, Results — «The majority of participants lived in the United States»

**Остальные поля:**
- country: USA — Page 2, Results; Table 1 (Geography) — «The majority of participants lived in the United States, with most distributed heavily in the South, followed by West and Midwest, with fewest in the Northeast.»
- data_years: 2023 — Page 2, Methods, Sampling Procedures — «Between February 10, 2023, and May 11, 2023, our cross-sectional, online survey was open to current kratom consumers»
- design: cross-sectional — Page 1, Abstract, Methods — «Our cross-sectional study used an online, anonymous survey between February and May 2023.»
- recruitment_channel: advocacy or vendor channels — Page 2, Methods, Sampling Procedures — «These included an email via the American Kratom Association listserv and a post on Facebook by various pro- and anti-kratom groups to encourage member particip…»
- regular_use_required: no — Page 2, Methods, Data Collection — «to ensure participants reported current kratom consumption and were 18 years or older»
- product_form: mixed — Page 4, Table 3 (Kratom use method) — «Capsules/tablets 359 17.4 ... Mixed in water/juice 1051 51.0 ... Brewed as a tea 145 7.0 ... Chewed leaf 10 0.5 ... Selected multiple methods 492 23.9»
- response_rate: NR — Page 2, Results — «There were 2824 responses to our online survey. Two hundred fifty-three participants were screened out because of not actively using kratom, an additional 380 …»
- age_mean: 47.8 — Page 2, Results — «a mean age of 47.8 years (SD = 13.5)»
- age_sd: 13.5 — Page 2, Results — «a mean age of 47.8 years (SD = 13.5)»
- pct_male: 52.3 — Page 2, Results; Table 1 — «with 52.3% of the sample identifying as male (n = 1078)»
- pct_other_opioid_use: 9.1 — Page 4, Table 3 — «Opioid use disorder 188 9.1»
- instruments: DSM-5 SUD criteria (11 criteria) adapted for kratom, self-report online checklist, English — Page 2, Methods, Data Collection and Measurement of KUD — «to assess the 11 symptoms of the DSM-5 diagnostic criteria for SUD, adapted for kratom. Participants met criteria for a KUD if they endorsed 2 or more of the 1…»
- industry_funding: NR — Page 1, footnote — «The authors report no conflicts of interest.»
- funding_coi: No funding statement; authors report no conflicts of interest. Recruitment partly via American Kratom Association listserv (not funding). — Page 1, footnote — «The authors report no conflicts of interest.»
- pub_status: journal — Page 1, header — «(J Addict Med 2024;18: 306–312)»
- language: English — Full text — «Prevalence of Kratom Use Disorder Among Kratom Consumers»
- notes: The time frame of the DSM-5 criteria (past 12 months or lifetime) is not stated, so it is coded NR. The kratom survey (Appendix 1) and supplementary tables were not received. Age and sex describe the whole analysed sample, which is the kratom-user sample (all are current users). pct_other_opioid_use = self-reported OUD diagnosis ever (188/2061, 9.1%), with no timing given; it is not current non-prescribed opioid use. 136 of 2009 (6.8%) lived outside the US. Response rate: NR; 2,061 of the 2,571 responses that passed screening were analysed (380 possible bots and 130 non-completers removed). N…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame was the American Kratom Association listserv and pro-/anti-kratom Facebook groups, which cover only part of US kratom consumers. — Page 2, Methods, Sampling Procedures — «an email via the American Kratom Association listserv and a post on Facebook by various pro- and anti-kratom groups»
2. способ отбора: **no** — Nonprobability, voluntary online opt-in with downstream sharing. — Page 2, Methods, Sampling Procedures — «Nonprobability sampling was used.»
3. размер выборки: **yes** — 2061 kratom users, which is at least 246. — Page 2, Results — «a total of 2061 participants were included in the analysis»
4. описание выборки и условий: **yes** — Age, sex, online setting, country (mostly USA, by region) and data collection dates all reported. — Page 2, Methods/Results; Table 1 — «52.3% of the sample identifying as male (n = 1078) and a mean age of 47.8 years (SD = 13.5)»
5. охват (пропуски): **yes** — 130 non-completers excluded, about 5.9% of the 2191 eligible non-bot responses; no missing KUD data among the 2061 analysed. — Page 2, Results — «another 130 participants were excluded from analyses because of not completing the survey»
6. валидность определения случая: **yes** — All 11 DSM-5 SUD criteria adapted for kratom were assessed one by one, with standard severity thresholds. — Page 2, Methods — «Participants met criteria for a KUD if they endorsed 2 or more of the 11 DSM-5 symptoms ... with any 2 to 3 criteria qualifying as mild, 4 to 5 criteria qualif…»
7. единое надёжное измерение: **yes** — Same online self-report checklist and threshold for all participants. — Page 2, Methods — «to assess the 11 symptoms of the DSM-5 diagnostic criteria for SUD, adapted for kratom»
8. статистика (числитель и знаменатель): **yes** — Numerator and denominator are clear (525/2061), so a CI can be calculated. — Page 2, Results; Table 1 — «Across the sample, 25.5% met the criteria for KUD (n = 525).»
9. отклик: **no** — Open online survey with no denominator of invited people; non-response not handled. — Page 2, Methods/Results — «There were 2824 responses to our online survey.»

Правки:
- 

Проверено: да

---

## ST13 · Abdullah 2019 · Malaysian Journal of Medicine and Health Sciences

Основной отчёт R2844: [текст](../../fulltext/text/R2844.txt) · [PDF](../../fulltext/pdf/R2844.pdf) — «Socio-demographic Characteristics, Kratom Use and Quality of Life (QoL) of Regular Kratom (Mitragyna speciosa Korth.) Users»
Расхождения в тексте: KDS severe cut-off: the Table III column header prints 'KDS >35', but the Table III footnote and the Data analysis section both define severe as 'KDS score ≥ 35'. Extracted as ≥35. Labels for the lower group vary: 'mild to moderate kratom dependence (KDS score < 35)' (Data analysis), 'mild to moderately severe kratom dependence' (abstract), 'mild and moderately severe' (Table III footnote). The groups add up: 107+43=150, matching N=150 in Table I. Abstract 'Sixty-percent ... > 6 years' and '55% (n=83/150) used >3 glasses' match Table I (90/150 and 83/150).
Заметка ИИ: The main dependence estimate is KDS severe (≥35), 43 of 150 (28.7%). Coded L2-scale, it undercounts KDS≥14 because the moderate band is folded into the <35 group. pct_other_opioid_use is set to 0 by design (exclusion criteria plus urine screen), not because it was measured. A reviewer should check for sample overlap with the Malay KDS validation study (Abdullah et al. 2018, ASEAN J Psychiatry), which is by the same team.

### ST13-1 · Regular kratom users, 3 community locations in Penang, Malaysia, years NR, n=150
Отчёты: R2844 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | KDS · KDS 35-48 (severe) of 0-48 | **L2-scale** | **43 / 150** | 28.7 | Page 4, Table III and footnote; Page 3, Data analysis | «KDS >35# (N=43) ... # KDS score < 35= mild and moderately severe kratom dependence, KDS score ≥ 35= severe kratom dependence» |
| E2 | all | KDS · KDS 0-34 (mild and moderate combined) of 0-48 | **below** | **107 / 150** | 71.3 | Page 4, Table III and footnote | «KDS <35# (N=107) ... # KDS score < 35= mild and moderately severe kratom dependence» |

- E1: cumulative: yes; источник порога: standard; правило: KDS row; 35-48 (high) band = L2-scale (the high band is not L3); у авторов: «severe kratom dependence»; главная у авторов: yes; период: NR; заметка: This is the only dependence category the authors report. The moderate band (14-34) is not reported separately, so KDS>=14 (the full L2-scale count) cannot be obtained. The table header says '>35' but the footnote and Data analysis say '≥35'.
- E2: cumulative: no; источник порога: study's own; правило: KDS row; band lower bound 0 = below (the band merges 0-13 low with 14-34 moderate); у авторов: «mild and moderately severe kratom dependence»; главная у авторов: no; период: NR; заметка: The authors merged the standard low (0-13) and moderate (14-34) bands into one group. The group contains an unknown number of L2-scale (14-34) cases, so it is not a clean non-case group.

**Ключевые поля выборки:**
- **n_users: 150** — Page 4, Table III — «KDS <35# (N=107) ... KDS >35# (N=43)»
- **sample_type: community_users** — Page 2, Study design and respondents — «Questionnaires administration and interview of respondents by the research team's psychiatrist and psychologist were carried out in the community halls of the targeted locations.»
- **sampling: snowball** — Page 2, Study design and respondents — «recruited 150 regular kratom users for a duration of 1 year by snowball and purposive sampling»
- **use_period: current** — Page 2, Study design and respondents — «(b) self-reported as a regular kratom user (used kratom ≥2 times daily), (c) must have more than 1 year kratom use history»
- **region: Southeast Asia** — Page 2, Study design and respondents — «three locations in the Malaysian state of Penang»

**Остальные поля:**
- country: MYS — Page 2, Study design and respondents — «This study was conducted in three locations in the Malaysian state of Penang which has high prevalence of kratom use.»
- data_years: NR — Page 2, Study design and respondents — «recruited 150 regular kratom users for a duration of 1 year by snowball and purposive sampling»
- design: cross-sectional — Page 1, Abstract (Methods) — «This cross-sectional survey recruited 150 kratom users»
- recruitment_channel: general — Page 2, Study design and respondents — «Initially, key informants who were ex-drug users and kratom users were identified and recruited in three targeted locations ... Then, they were asked to refer …»
- regular_use_required: regular use, ≥2 times daily, with more than 1 year of kratom use history — Page 2, Study design and respondents — «(b) self-reported as a regular kratom user (used kratom ≥2 times daily), (c) must have more than 1 year kratom use history»
- product_form: traditional leaf — Page 2-3, Mitragynine content — «We measured the mitragynine content of kratom juice which we purchased from each targeted locations ... The range of mitragynine level in one glass of kratom j…»
- response_rate: NR — Page 2, Study design and respondents — «Kratom users who fulfilled all inclusion criteria and without any exclusion criteria were enrolled in the study if they voluntarily agreed to participate»
- age_mean: 34.4 — Page 3, Table I — «Mean age 34.4 years (SD=11.2)»
- age_sd: 11.2 — Page 3, Table I — «Mean age 34.4 years (SD=11.2)»
- pct_male: 100 — Page 3, Table I — «Gender Male 150 100»
- pct_other_opioid_use: 0 — Page 2, Study design and respondents — «We excluded respondents who: (a) tested positive for other drug use besides kratom ... and (c) history of alcohol and illicit drug use other than kratom within…»
- instruments: Kratom Dependence Scale (KDS), Malay version, 16 items scored 0-3, total 0-48 — Page 2, Measures / Kratom Dependence Scale (KDS) — «The total score ranged from 0-48 with score of 0-13 designates mild severity, 14-34 designates moderate severity and 35-48 designates severe dependence. ... Th…»
- industry_funding: no — Page 5, Acknowledgements — «This work was supported by the Research University Grant of Universiti Sains Malaysia (1001CDADAH/816306) and (1001/PSOSIAL/8016015), and Higher Institution's …»
- funding_coi: Universiti Sains Malaysia university grants and HICoE grant; no conflict of interest statement in the text — Page 5, Acknowledgements — «This work was supported by the Research University Grant of Universiti Sains Malaysia»
- pub_status: journal — Page 1, header — «Mal J Med Health Sci 15(3): 4-9, Oct 2019»
- language: English — Full text — «ORIGINAL ARTICLE Socio-demographic Characteristics, Kratom Use and Quality of Life (QoL) of Regular Kratom (Mitragyna speciosa Korth.) Users»
- notes: Age and sex describe all 150 kratom users (whole sample = users). The sample is all male; the authors say no women came forward. pct_other_opioid_use = 0 is set by design: anyone positive on urine screening (morphine, methadone and others) or with illicit drug use in the past year was excluded. People with psychiatric or medical history were also excluded, which may lower dependence severity. The study's focus is quality of life (WHOQOL-BREF). Same team (Abdullah, Singh) published the Malay KDS validation (ref 13, 2018); a reviewer should check whether the samples overlap. Calendar years of d…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is 3 locations in one state (Penang), reached through key informants; it does not cover Malaysian kratom users, the population the paper describes. — Page 5, Discussion (limitations) — «this study was conducted only in the state of Penang and hence, the findings cannot be generalized to represent the entire kratom user population of the country»
2. способ отбора: **no** — Snowball and purposive sampling through key informants. — Page 2, Study design and respondents — «by snowball and purposive sampling»
3. размер выборки: **no** — n=150 kratom users, below 246. — Page 1, Abstract — «This cross-sectional survey recruited 150 kratom users»
4. описание выборки и условий: **unclear** — Age, sex, setting and country are reported; calendar dates of data collection are not (only a 1-year duration). — Page 2-3, Methods; Table I — «recruited 150 regular kratom users for a duration of 1 year»
5. охват (пропуски): **yes** — KDS groups add up to the full sample (107+43=150), so no dependence data are missing. — Page 4, Table III — «KDS <35# (N=107) ... KDS >35# (N=43)»
6. валидность определения случая: **yes** — KDS bands from the developers' validation in kratom users (Saingam 2014); the Malay version was validated in Malaysian kratom users (ref 13). — Page 2, Kratom Dependence Scale (KDS) — «35-48 designates severe dependence. It has excellent internal consistency (Cronbach's α) of 0.97 (2). The Malay version of the KDS also demonstrated excellent …»
7. единое надёжное измерение: **yes** — Everyone completed the same self-administered KDS, in the same setting, with the same cut-off. — Page 2, Measures — «Respondents were also administered the Kratom Dependence Scale (KDS) to assess severity of kratom dependence»
8. статистика (числитель и знаменатель): **yes** — Counts and denominator are clear (43/150), so a CI can be calculated. — Page 4, Table III — «KDS >35# (N=43)»
9. отклик: **unclear** — Snowball recruitment; the number approached or refusing is not reported. — Page 2, Study design and respondents — «enrolled in the study if they voluntarily agreed to participate and signed written informed consent»

Правки:
- E1.level = not_levelled  # C1: лёгкая и умеренная даны одной суммой — долю ≥14 не собрать (одобрено автором в чате 2026-11-23)

Проверено: да

---

## ST14 · Kanchanasim 2026 · Journal of Medical Bioscience

Основной отчёт R0243: [текст](../../fulltext/text/R0243.txt) · [PDF](../../fulltext/pdf/R0243.pdf) — «Prevalence of substance use and quality of life among support personnel in a tertiary care hospital in Bangkok»
Не выписано ИИ: Staff who never used kratom leaf or cocktail (170 non-leaf, 185 non-cocktail users) are not extracted. Risk bands for other substances and the urine screening results (n=199) are not kratom estimates and are not extracted.
Расхождения в тексте: Kratom counts agree across the text: Table 5 lifetime users (leaf 80, cocktail 65) match the Table 8 denominators and the Table 13/14 user columns. Band counts add up (73+7=80; 50+11+4=65), and the abstract percentages (91.25% and 76.92% low risk) match Table 8. Leaf high risk is printed '-' and was coded 0. The English abstract calls the cocktail both 'kratom tea' and 'kratom cocktail'. The job metadata gives 'Journal of Medical Bioscience 2026', but the text is a 2024 Chulalongkorn MSc thesis, so pub_status is thesis. Not kratom-related: the Table 21 header prints '(n=7)' on its first page and '(n=79)' on later pages.
Заметка ИИ: There is one sample with two kratom denominators. Leaf users (n=80) are the main one; cocktail users (n=65) are a second subgroup. Their overlap is not reported, so the total number of kratom users cannot be derived. The only kratom measure is ASSIST risk bands (L2-screen for >=27); there is no diagnostic or dependence-scale measure.

### ST14-1 · Hospital support staff, tertiary hospital, Bangkok, Thailand, 2024: lifetime kratom leaf users n=80 (and kratom cocktail users n=65, reported separately)
Отчёты: R0243 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | lifetime kratom leaf users | ASSIST · ASSIST kratom score 0-3 (low risk) | **below** | **73 / 80** | 91.2 | Page 46, Table 8; Page 35 (scoring) | «ใบกระท่อม (n=80) 73 91.25 7 8.75 - - ; 0 - 3 คะแนน หมายถึง ระดับความเสี่ยงตํ่า [0-3 = low risk]» |
| E2 | lifetime kratom leaf users | ASSIST · ASSIST kratom score 4-26 (moderate risk) | **not_levelled** | **7 / 80** | 8.8 | Page 46, Table 8; Page 35 (scoring) | «ใบกระท่อม (n=80) 73 91.25 7 8.75 - - ; 4 - 26 คะแนน หมายถึง ระดับความเสี่ยงปานกลาง [4-26 = moderate risk]» |
| E3 | lifetime kratom leaf users | ASSIST · ASSIST kratom score >=27 (high risk) | **L2-screen** | **0 / 80** | 0.0 | Page 46, Table 8; Page 35 (scoring) | «ใบกระท่อม (n=80) 73 91.25 7 8.75 - - ; 27 คะแนนขึ้นไป หมายถึง ระดับความเสี่ยงสูง [27+ = high risk]» |
| E4 | lifetime kratom cocktail users | ASSIST · ASSIST kratom cocktail score 0-3 (low risk) | **below** | **50 / 65** | 76.9 | Page 46, Table 8 | «นํ้าต้มใบกระท่อม (n=65) 50 76.92 11 16.92 4 6.15 [kratom cocktail (n=65): low 50, moderate 11, high 4]» |
| E5 | lifetime kratom cocktail users | ASSIST · ASSIST kratom cocktail score 4-26 (moderate risk) | **not_levelled** | **11 / 65** | 16.9 | Page 46, Table 8 | «นํ้าต้มใบกระท่อม (n=65) 50 76.92 11 16.92 4 6.15» |
| E6 | lifetime kratom cocktail users | ASSIST · ASSIST kratom cocktail score >=27 (high risk) | **L2-screen** | **4 / 65** | 6.2 | Page 46, Table 8 and text below | «ผู้ใช้สารเสพติดที่มีความเสี่ยงในระดับสูง มีจํานวน 4 สาร ... สารผสมนํ้าต้มใบกระท่อม (ร้อยละ 6.15) [high-risk users found for 4 substances, incl. kratom cocktail (6.15%)]» |

- E1: cumulative: no; источник порога: standard; правило: ASSIST row; low band 0-3 is below any case level; у авторов: «เสี่ยงต่ำ [low risk]»; главная у авторов: no; период: current; заметка: Denominator = all lifetime leaf users; 9 used leaf in the past 3 months (Table 5). The abstract reports low risk as 91.25%.
- E2: cumulative: no; источник порога: standard; правило: ASSIST row; 4-26 moderate = not_levelled; у авторов: «เสี่ยงกลาง [moderate risk]»; главная у авторов: no; период: current
- E3: cumulative: yes; источник порога: standard; правило: ASSIST row; >=27 high risk = L2-screen; у авторов: «เสี่ยงสูง [high risk]»; главная у авторов: yes; период: current; заметка: Printed '-', read as 0 (73+7=80). Authors give no use-disorder estimate. High risk is the band closest to dependence, and the authors list which substances had high-risk users.
- E4: cumulative: no; источник порога: standard; правило: ASSIST row; low band 0-3 is below any case level; у авторов: «เสี่ยงต่ำ [low risk]»; главная у авторов: no; период: current; заметка: Separate ASSIST item for boiled kratom-leaf mixtures. Denominator = lifetime cocktail users; 14 used it in the past 3 months. Overlap with leaf users is not reported.
- E5: cumulative: no; источник порога: standard; правило: ASSIST row; 4-26 moderate = not_levelled; у авторов: «เสี่ยงกลาง [moderate risk]»; главная у авторов: no; период: current
- E6: cumulative: yes; источник порога: standard; правило: ASSIST row; >=27 high risk = L2-screen; у авторов: «เสี่ยงสูง [high risk]»; главная у авторов: yes; период: current; заметка: Cannot be added to the leaf high-risk count because the overlap between leaf and cocktail users is unknown.

**Ключевые поля выборки:**
- **n_users: 80** — Page 46, Table 8 — «ใบกระท่อม (n=80) 73 91.25 7 8.75 - - [kratom leaves (n=80): low 73, moderate 7, high -]»
- **sample_type: other** — Page 16-17 (definitions); Page 33 — «บุคลากรฝ่ายสนับสนุน (Support personnel) หมายถึง บุคลากรที่ทํางานในโรงพยาบาลในตําแหน่งงานด้านการสนับสนุน [support personnel = hospital staff in support positions: central supply, laundry, nutrition, central transport]»
- **sampling: convenience** — Page 34 (Sampling technique) — «ไม่อาศัยความน่าจะเป็น (Non-probability Sampling) ... จากนั้นทําการสุ่มตัวอย่างแบบตามสะดวก (Convenience Sampling) [non-probability ... then convenience sampling]»
- **use_period: lifetime any** — Page 44, Table 5; Page 46, Table 8 — «ตลอดช่วงชีวิตที่ผ่านมา ... ใบกระท่อม 80 32.0 ... สารผสมนํ้าต้มใบกระท่อม 65 26.0 [lifetime: kratom leaf 80 (32.0%); kratom cocktail 65 (26.0%)], matching Table 8 n=80 and n=65»
- **region: Southeast Asia** — Page 3 (title) — «a tertiary care hospital in Bangkok»

**Остальные поля:**
- country: THA — Page 3 (title) — «Prevalence of substance use and quality of life among support personnel in a tertiary care hospital in Bangkok»
- data_years: 2024 — Page 39 (Chapter 4, Part 1) — «โรงพยาบาลระดับตติยภูมิแห่งหนึ่ง ในเขตกรุงเทพมหานคร ปี พ.ศ. 2567 [a tertiary hospital in Bangkok, B.E. 2567 (= 2024)]»
- design: cross-sectional — Page 33 (Chapter 3) — «การศึกษาวิจัยเชิงพรรณนา ณ ช่วงเวลาใดเวลาหนึ่ง (Cross – sectional descriptive study) [cross-sectional descriptive study]»
- recruitment_channel: general — Page 37 (Data collection, step 3) — «ผู้วิจัยจะดําเนินการติดต่อหัวหน้าฝ่ายของแต่ละหน่วยงาน ... และเข้าพบกลุ่มตัวอย่าง [researcher contacted the head of each unit ... and met participants at the wo…»
- regular_use_required: no — Page 16 (definitions) — «พฤติกรรมการใช้สารเสพติด (Substance use) หมายถึง การใช้สารเสพติดชนิดใดชนิดหนึ่งในช่วง 3 เดือนที่ผ่านมา และตลอดช่วงชีวิตที่ผ่านมา [use of any substance in past 3…»
- product_form: mixed — Page 16 (definitions); Page 46, Table 8 — «ใบกระท่อม สารผสมนํ้าต้มใบกระท่อม (สี่คูณร้อย แปดคูณร้อย วันทูคอล ฯลฯ) [kratom leaves; boiled kratom-leaf mixtures (4x100, 8x100, etc.)]»
- response_rate: NR — Page 34; Page 39 — «ประมาณ 592 คน ... เพิ่มขนาดตัวอย่างเป็น 250 คน [about 592 staff ... sample size set at 250]; number approached or refusing not reported»
- age_mean: 40.36 — Page 40, Table 3 — «(Mean=40.36, SD=11.763, Max=64, Min=20)»
- age_sd: 11.763 — Page 40, Table 3 — «(Mean=40.36, SD=11.763, Max=64, Min=20)»
- pct_male: 86.3 — Page 55, Table 13 — «ไม่ใช้สาร (n=170) ... ใช้สาร (n=80) ... ชาย 88 (51.8) 69 (86.3) [kratom leaf users (n=80): male 69 (86.3%)]»
- pct_other_opioid_use: NR — Page 44, Table 5; Page 45, Table 7 — «สารกลุ่มฝิ่น 7 2.8 - - [opioids: lifetime 7 (2.8%), past 3 months -]; มอร์ฟีน 1 0.40 [urine morphine positive 1]»
- instruments: ASSIST V3.1, Thai version (Assanangkornchai et al. 2011), interviewer-administered; separate kratom-leaf and kratom-cocktail substance items — Page 34-35 (Instruments, Part 2); Page 6 — «แบบคัดกรอง ... (ASSIST) ... พัฒนาโดยองค์การอนามัยโลก แปลภาษาไทยโดย สาวิตรี อัษณางค์กรชัย และคณะ, 2554 [developed by WHO, Thai translation by Assanangkornchai e…»
- industry_funding: no — Page 7 (Acknowledgements) — «ขอขอบคุณศูนย์ศึกษาปัญหาการเสพติด ที่ให้ความอุปการะ และสนับสนุนการดําเนินการวิจัยครั้งนี้ [Thanks to the Center for Addiction Studies for supporting this resear…»
- funding_coi: Supported by the Center for Addiction Studies (academic); no kratom-industry funding; COI statement not reported — Page 7 (Acknowledgements) — «ขอขอบคุณศูนย์ศึกษาปัญหาการเสพติด ที่ให้ความอุปการะ และสนับสนุนการดําเนินการวิจัยครั้งนี้ [Thanks to the Center for Addiction Studies for supporting this resear…»
- pub_status: thesis — Page 1; Page 3 — «Chulalongkorn University Theses and Dissertations (Chula ETD) ... A Thesis Submitted in Partial Fulfillment of the Requirements for the Degree of Master of Sci…»
- language: Thai (English abstract only) — Page 5-6; full text — «บทคัดย่อภาษาไทย ... บทคัดยอภาษาอังกฤษ [Thai abstract ... English abstract]»
- notes: Denominator: the main n_users (80) is lifetime kratom LEAF users; lifetime kratom COCKTAIL users (n=65) are a second subgroup. Leaf-cocktail overlap is not reported, so the combined number of kratom users cannot be derived (80-145). Age is for the whole sample (N=250); pct_male is for leaf users (Table 13); cocktail users are 84.6% male (Table 14); the whole sample is 62.8% male. ASSIST risk bands describe current use but were scored over lifetime users, of whom few used in the past 3 months (leaf 9, cocktail 14). No DSM, ICD or dependence-scale measure. Opioid use among kratom users is not r…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target population is the hospital's support staff, but the frame covered only 4 units (~592 staff); other support units were left out. — Page 33 (Population) — «ประชากรที่จะทําการศึกษา ... คือ บุคลากรฝ่ายสนับสนุนที่ทํางานใน หน่วยจ่ายกลางและหน่วยซักรีด หน่วยโภชนวิทยา หน่วยขนส่งกลางและยานยนต์ [studied population: staff o…»
2. способ отбора: **no** — Non-probability sampling followed by convenience sampling of volunteers; authors report that unit proportions could not be kept. — Page 34; Page 79 (Limitations 2) — «สุ่มตัวอย่างแบบตามสะดวก (Convenience Sampling) ... ไม่สามารถแบ่งสัดส่วนของบุคลากรในแต่ละหน่วยงานได้ [convenience sampling ... could not keep proportions per un…»
3. размер выборки: **no** — 80 lifetime leaf users (65 cocktail users), below 246. — Page 46, Table 8 — «ใบกระท่อม (n=80) ... นํ้าต้มใบกระท่อม (n=65)»
4. описание выборки и условий: **yes** — Age, sex (also for kratom users), setting, country and year (2024) are reported. — Page 39; Page 40, Table 3; Page 55, Table 13 — «ปี พ.ศ. 2567 ... เพศชายจํานวน 157 คน เพศหญิง 93 คน มีอายุเฉลี่ย 40.36 ปี [2024 ... 157 men, 93 women, mean age 40.36]»
5. охват (пропуски): **yes** — Risk bands are given for all 80 leaf and all 65 cocktail lifetime users; band counts add up to n. — Page 46, Table 8 — «ใบกระท่อม (n=80) 73 91.25 7 8.75 ... นํ้าต้มใบกระท่อม (n=65) 50 76.92 11 16.92 4 6.15»
6. валидность определения случая: **no** — Only ASSIST risk bands (a screen) were used; no diagnostic criteria and no cut-off validated for kratom. — Page 34-35 — «มีวัตถุประสงค์เพื่อค้นหาผู้ใช้สารเสพติดแบบเสี่ยงหรือแบบอันตราย โดยการจําแนกระดับความรุนแรงของความเสี่ยง [aims to identify risky/harmful use, classifying risk l…»
7. единое надёжное измерение: **yes** — The same Thai ASSIST, interviewer mode and scoring were used for everyone. — Page 6 — «Data were collected through interviews using the Alcohol, Smoking and Substance Involvement Screening Test (ASSIST V3.1)»
8. статистика (числитель и знаменатель): **yes** — Counts and denominators of kratom users are printed for each band, so CIs can be calculated. — Page 46, Table 8 — «นํ้าต้มใบกระท่อม (n=65) 50 76.92 11 16.92 4 6.15»
9. отклик: **unclear** — 250 volunteers from ~592 staff; the number approached or refusing is not reported; no comparison with non-responders and no weights. — Page 39 — «บุคลากรฝ่ายสนับสนุนจํานวน 250 คน ที่สมัครใจยินยอมเข้าร่วมโครงการวิจัย [250 support staff who volunteered]»

Правки:
- E1.subgroup = all  # основная выборка — 80 потребителей листа (одобрено автором 2026-11-23)
- E2.subgroup = all
- E3.subgroup = all

Проверено: да

---

## ST15 · Singh 2014 · Drug and alcohol dependence

Основной отчёт R3639: [текст](../../fulltext/text/R3639.txt) · [PDF](../../fulltext/pdf/R3639.pdf) — «Kratom (Mitragyna speciosa) dependence, withdrawal symptoms and craving in regular users.» — [DOI](https://doi.org/10.1016/j.drugalcdep.2014.03.017)
Приложен R3754: [текст](../../fulltext/text/R3754.txt) — «Measuring Dependence Severity Of Ketum (Mitragyna Speciosa) Use Among Ketum Leaf Users In Malysia»
Связь отчётов: Same sample of 293 regular male kratom users in Penang, Kedah and Perlis: R3639 (Singh, Müller & Vicknasingam 2014, Drug and Alcohol Dependence) and R3754 (thesis, USM; incomplete text)
Расхождения в тексте: 1) Daily-quantity OR: R3639 reports severe dependence OR 7.05 (95% CI 4.09–12.13) for >3 glasses/day. The R3754 abstract reports OR 4.09 (2.32–7.24) for >=4 glasses/day. The cut-points differ. 2) Single: R3639 text says 171/293 single, but Table 1 gives single/divorced 175. Married: Table 1 gives 118 (40%); the R3754 abstract says 41%. 3) Withdrawal: R3639 says 35% (103/293) moderate-to-severe; the R3754 abstract says 33% severe. 4) R3639 3.6: '73% (151/293)' is wrong arithmetic (151/293 = 51.5%). 5) R3639 3.4 prints 'p > 0.001', probably a typo for p < 0.001. 6) Table 1 age groups are '18–25' and '>26'; age 26 is not covered. 7) Sampling: R3639 says purposive; the R3754 abstract says purposive and quota; R3754 1.10 says purposive and chain referral. 8) The LDQ low band is never printed; low = 0/293 is implied but not reported.
Заметка ИИ: The thesis R3754 is incomplete (text stops at Chapter 2.2), so LDQ band cut-offs could not be checked. The threshold_source of 'study's own' for the LDQ bands is a provisional code. The adhoc 'all dependent' estimate is flagged for the reviewer to keep or drop.

### ST15-1 · Regular male kratom (ketum) juice users, community settings, Penang/Kedah/Perlis, Malaysia, 2012, n=293
Отчёты: R3639 (main); R3754

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | LDQ · LDQ moderate band (cut-offs not reported) of 0-30 | **L2-scale** | **132 / 293** | 45.1 | Page 3, 3.4 Kratom dependence; Abstract | «while 45% (132/293) had moderate Kratom dependence problems» |
| E2 | all | LDQ · LDQ severe (high) band (cut-off not reported) of 0-30 | **not_levelled** | **161 / 293** | 54.9 | Page 3, 3.4 Kratom dependence; Abstract; R3754 Abstract | «More than half of the respondents (161/293) faced severe Kratom dependence problems» |
| E3 | all | adhoc · Self-claimed dependence on kratom (all respondents) | **not_levelled** | **293 / 293** | 100.0 | Page 3, 3.4; Page 4, Discussion | «All regular users in this study claimed to be dependent on Kratom.» |

- E1: cumulative: no; источник порога: study's own; правило: LDQ row; authors' medium/moderate band = L2-scale; у авторов: «moderate Kratom dependence problems»; главная у авторов: yes; период: NR; заметка: Band limits are not given in R3639. The LDQ scoring section of the thesis (R3754 3.11.1, Table 4.4) is not in the text received.
- E2: cumulative: yes; источник порога: study's own; правило: LDQ row; a high band alone is not levelled; у авторов: «severe Kratom dependence problems»; главная у авторов: yes; период: NR; заметка: R3754 abstract: 'Fifty-five percent of the sample reported severe ketum dependence' (161/293 = 54.9%).
- E3: cumulative: yes; источник порога: study's own; правило: adhoc row; self-identified dependence is not levelled; у авторов: «claimed to be dependent on Kratom»; главная у авторов: no; период: NR; заметка: It is unclear whether this is a separate self-report item or simply restates the LDQ result (moderate 132 + severe 161 = 293; 'All others had moderate'). The reviewer should decide whether to keep it.

**Ключевые поля выборки:**
- **n_users: 293** — Page 2, 3.1; Page 3, 3.4 — «More than half of the respondents (161/293) faced severe Kratom dependence problems, while 45% (132/293) had moderate»
- **sample_type: community_users** — Page 2, 2.1 Study design — «A total of 293 male Kratom users from various community settings were recruited through purposive sampling.»
- **sampling: convenience** — Page 2, 2.1 Study design; R3754, Abstract and 1.10 — «recruited through purposive sampling. Staff from the National Anti-Drug Agency and village heads helped introducing key informants»
- **use_period: current** — Page 2, 3.1 — «The average frequency of current Kratom consumption in the respondents was 3.5 times per day»
- **region: Southeast Asia** — Page 2, 2.1 Study design — «three northern states (Penang, Perlis, and Kedah) of the peninsular Malaysia which neighbour the border of south Thailand»

**Остальные поля:**
- country: MYS — Page 2, 2.1 Study design — «in three northern states (Penang, Perlis, and Kedah) of the peninsular Malaysia»
- data_years: 2012 — Page 2, 2.1 Study design — «A cross-sectional study was conducted between January and December 2012»
- design: cross-sectional — Page 2, 2.1 Study design — «A cross-sectional study was conducted between January and December 2012»
- recruitment_channel: general — Page 2, 2.1 Study design — «Staff from the National Anti-Drug Agency and village heads helped introducing key informants who were familiar with the Kratom users in the respective communit…»
- regular_use_required: Kratom use for at least 6 months (users of <6 months excluded); described as drinking kratom several times per day for >6 months — Page 2, 2.1; Page 4, Discussion — «respondents who used Kratom for less than six months were excluded from the study as they did not yet represent a regular use.»
- product_form: traditional leaf — Page 2, 3.2 Kratom preparation and use — «The leaves of the Kratom plant were used to prepare Kratom juice. One commonly reported way is to boil the leaves together with clean tap-water for approx. 3–4…»
- response_rate: NR — R3754, 1.10 Study Limitation — «Potential ketum users in some targeted study locations refused to cooperate with the researcher.»
- age_mean: 28.9 — Page 2, 3.1 — «Respondents mean age in this study was 28.9 years.»
- age_sd: NR — Page 2, 3.1 — «Respondents mean age in this study was 28.9 years. Nearly half were 18–25 years old.»
- pct_male: 100 — Page 2, 3.1 — «Respondents in this study were all male Kratom users (n = 293)»
- pct_other_opioid_use: 0 — Page 2, 2.1 Study design — «Urine toxicology tests for methamphetamine, amphetamine, opiates, cannabis, methadone, benzodiazepine, buprenorphine, and ketamine were conducted to exclude re…»
- instruments: Leeds Dependence Questionnaire (LDQ), Malay translation, interviewer-administered — Page 2, 2.1 and 2.2 — «the Leeds Dependence Questionnaire (LDQ; Raistrick et al., 1994), Marijuana Withdrawal Checklist (MWC...), and Marijuana Craving Questionnaire-Short Form ... w…»
- industry_funding: no — Page 5, Acknowledgements — «This study was funded by the Ministry of Science Technology and Innovation Malaysia (MOSTI) ... and a Research Grant from the Academy of Sciences for the Devel…»
- funding_coi: MOSTI Malaysia, TWAS grant, Friedrich-Alexander-University Erlangen-Nuremberg; authors report no conflicts of interest — Page 5, Conflict of interest; Acknowledgements — «The authors reported no biomedical financial interests or potential conflicts of interest.»
- pub_status: journal — Page 1, header — «Drug and Alcohol Dependence 139 (2014) 132–137»
- language: English — Page 1 — «Kratom (Mitragyna speciosa) dependence, withdrawal symptoms and craving in regular users»
- notes: All 293 are male; age is the whole-sample mean (all are kratom users; SD NR). pct_other_opioid_use = 0 rests only on excluding people with an opiate-positive urine test. 36.5% (107/293) were ex-drug users. Some users add dextromethorphan cough syrup or nimetazepam (a benzodiazepine, which was screened) to the drink; dextromethorphan was not tested. Withdrawal (MWC) and craving (MCQ-SF) measures were also used but are not estimates. R3754 = PhD thesis (USM, April 2013) on the same sample. The text received stops in Chapter 2, so the LDQ scoring (3.11.1) and Table 4.4 are missing. R3754 also us…

**Риск смещения (JBI):**
1. рамка выборки: **no** — No sampling frame. Users were reached through key informants in selected communities of three states. — Page 2, 2.1; R3754, 1.10 — «there was no sampling frame available for ketum users»
2. способ отбора: **no** — Purposive sampling (the thesis adds quota and chain-referral); not a probability sample. — Page 2, 2.1 — «recruited through purposive sampling»
3. размер выборки: **yes** — 293 kratom users, which is at least 246. — Page 2, 3.1 — «Respondents in this study were all male Kratom users (n = 293)»
4. описание выборки и условий: **yes** — Age, sex, setting, country and dates of data collection are all reported. — Page 2, 2.1 and 3.1 — «conducted between January and December 2012 ... coffee-shops, community halls, clandestine Kratom makeshifts, and respondent's house»
5. охват (пропуски): **yes** — The LDQ categories add up to the full 293 (161+132), so no dependence data are missing. — Page 3, 3.4 — «(161/293) faced severe Kratom dependence problems, while 45% (132/293) had moderate»
6. валидность определения случая: **no** — LDQ was borrowed from alcohol/opiate research. Band cut-offs are not reported and have not been validated in kratom users. — Page 2, 2.2 — «At present, there is no tool specifically designed to measure Kratom dependence ... Thus the Leeds Dependence Questionnaire (LDQ; Raistrick et al., 1994)»
7. единое надёжное измерение: **yes** — The same Malay structured questionnaire was given to everyone by face-to-face interview. — Page 2, 2.1 — «using structured questionnaires which were translated into the local Malay language. Each interview session lasted between 30 and 45 min.»
8. статистика (числитель и знаменатель): **yes** — Numerators and denominators are given, so CIs can be calculated. — Page 3, 3.4 — «(161/293) ... (132/293)»
9. отклик: **unclear** — Response rate not reported. The thesis mentions refusals but gives no numbers. — R3754, 1.10 Study Limitation — «Ketum users in these locations were unwilling to participate in the study, because they were afraid that their personal information would be disclosed to the p…»

Правки:
- 

Проверено: да

