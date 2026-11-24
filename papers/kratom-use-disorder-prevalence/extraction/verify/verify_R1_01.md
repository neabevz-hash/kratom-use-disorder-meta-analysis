# Проверка выписывания — файл 1 из 2

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

## ST01 · Ang 2026 · Asia-Pacific Journal of Molecular Biology and Biotechnology

Основной отчёт R0060: [текст](../../fulltext/text/R0060.txt) · [PDF](../../fulltext/pdf/R0060.pdf) — «Determination of urinary mitragynine concentration and severity of kratom dependence among people with kratom dependence in Malaysia» — [DOI](https://doi.org/10.35118/apjmbb.2026.034.3.14)
Расхождения в тексте: 1) Daily frequency: Table 2 gives 1-3 times/day = 63 and 4-6 = 29. Text p.7 and p.9 say 61% and 31%. Table values used. 2) Duration of use: Table 2 gives 1-10 y = 65, 11-20 = 28, 21-30 = 5, 31-40 = 2. Text p.6 says '8%' more than 20 years ago (table: 7), '36%' for 10-20 years (table: 28) and '57%' within the past 10 years (table: 65). Discussion p.9 says 35% for 10-20 years. 3) Urine drug screen: Table 2 gives 'Positive 3' and 'Negative 0'. Negative should be 97, so this is a table error. 4) KDS counts agree between Table 2 and the text on p.6 (45/46/9 of 100).
Заметка ИИ: Draft for human review. The KDS band score system matches the levels table (0-13 below; 14-34 and 35-48 = L2-scale). This study (R0060) is itself one of the sources cited in the levels table for the KDS bands. The study is mainly a urinary mitragynine LC/MS/MS study; the dependence data are its secondary descriptive output.

### ST01-1 · Penang community daily male kratom users, Malaysia, 2024-2025, n=100
Отчёты: R0060 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | KDS · KDS 0-13 (mild) of 0-48 | **below** | **45 / 100** | 45.0 | Table 2 (p.5); Page 6, Kratom use history; bands Page 3; ti… | «Kratom dependence score Mild 45 45 Moderate 46 46 Severe 9 9» |
| E2 | all | KDS · KDS 14-34 (moderate) of 0-48 | **L2-scale** | **46 / 100** | 46.0 | Table 2 (p.5); Page 6, Kratom use history | «According to the KDS, 45, 46 and 9 of the 100 respondents were mild, moderate and severe on kratom, respectively.» |
| E3 | all | KDS · KDS 35-48 (severe) of 0-48 | **L2-scale** | **9 / 100** | 9.0 | Table 2 (p.5); Page 6, Kratom use history | «Kratom dependence score Mild 45 45 Moderate 46 46 Severe 9 9» |

- E1: cumulative: no; источник порога: standard; правило: KDS row; 0-13 band = below (not a case); у авторов: «mild»; главная у авторов: yes; период: past 12 months; заметка: Bands from p.3: '0-13 = mild; 14-34 = moderate; 35-48 = severe'. KDS stem: 'During the past 12 months, how often have you had the following symptoms?' The authors call all respondents 'people with kratom dependence' even in the mild band.
- E2: cumulative: no; источник порога: standard; правило: KDS row; 14-34 band = L2-scale; у авторов: «moderate»; главная у авторов: yes; период: past 12 months; заметка: Moderate+severe (55/100) is not reported by the study as a combined figure, so it is not extracted.
- E3: cumulative: no; источник порога: standard; правило: KDS row; 35-48 band = L2-scale (high band is not L3); у авторов: «severe»; главная у авторов: yes; период: past 12 months; заметка: Authors label this band 'severe'. By the levels table it is L2-scale, not L3.

**Ключевые поля выборки:**
- **n_users: 100** — Table 2 (p.5) — «Respondent's number 100 100»
- **sample_type: community_users** — Page 3, Study design, respondents, and location — «Respondents were recruited from the community setting, where kratom use is endemic in the northern state of Penang (Malaysia).»
- **sampling: convenience** — Page 3, Study design; Page 9, limitations — «recruited through purposive and convenience sampling for this cross-sectional study.»
- **use_period: past 12 months** — Page 3, Inclusion and exclusion criteria — «3) had used kratom at least once daily in the last one year.»
- **region: Southeast Asia** — Page 3, Study design, respondents, and location — «northern state of Penang (Malaysia)»

**Остальные поля:**
- country: MYS — Page 3, Study design, respondents, and location — «Respondents were recruited from the community setting, where kratom use is endemic in the northern state of Penang (Malaysia).»
- data_years: 2024-2025 — Page 3, Data collection — «The study data was collected between November 2024 and January 2025.»
- design: cross-sectional — Page 3, Study design, respondents, and location — «A total of 100 respondents of people with regular kratom use were recruited through purposive and convenience sampling for this cross-sectional study.»
- recruitment_channel: general — Page 3, Study design, respondents, and location — «Respondents were recruited from the community setting»
- regular_use_required: self-reported regular user who used kratom at least once daily in the last one year — Page 3, Inclusion and exclusion criteria — «2) self-reported as a regular kratom user, and 3) had used kratom at least once daily in the last one year.»
- product_form: traditional leaf — Page 9, Discussion — «Some respondents confessed that they obtained kratom juice from illegal kratom juice sellers, and some said that they prepared kratom juice by boiling kratom l…»
- response_rate: NR — Page 5, Respondents' socio-demographic characteristics — «Despite an attempt to recruit female users with kratom dependence, the effort was unsuccessful as they refused to participate due to social censure and stigma.»
- age_mean: 44.07 — Page 5, Results; Table 2 — «The respondents' age ranged from 18-76 years old, with a mean age of 44.07 years (SD:13.14)»
- age_sd: 13.14 — Page 5, Results; Table 2 — «with a mean age of 44.07 years (SD:13.14)»
- pct_male: 100 — Table 2 (p.5) — «Gender (Male) 100 100»
- pct_other_opioid_use: 0 — Table 2 (p.5); Page 6 — «Illicit drug MOP 0 0 ... MTD 0 0 ... Out of 100 respondents, only 3 were tested positive for illicit drug use, namely benzodiazepines.»
- instruments: Kratom Dependence Scale (KDS, Saingam et al. 2014), 16 items scored 0-3 (range 0-48), interviewer-administered face to face; language version not stated (items printed in English in Table 1) — Page 3, Kratom Dependence Scale (KDS); Table 1 (p.4) — «In this study, KDS developed by Saingam et al (2014) was used to evaluate the severity of kratom dependence of the 100 respondents, the 16 questions are shown …»
- industry_funding: no — Page 9, Acknowledgements — «This study was supported by the Ministry of Science, Technology and Innovation (MOSTI), Malaysia, under TeD 1 Grant [TDF10231723].»
- funding_coi: Government grant (MOSTI Malaysia, TeD 1 Grant TDF10231723); authors declare no conflict of interest. One author is affiliated with USAINS Biomics / USAINS Holding Sdn Bhd (university holding company), not a kratom vendor. — Page 9, Acknowledgements; Conflict of Interest; Page 1 affi… — «The authors have declared that no conflict of interest exists.»
- pub_status: journal — Page 1, header — «AsPac J. Mol. Biol. Biotechnol. 2026 ... Vol. 34 (3): 160-170 ... RESEARCH ARTICLE»
- language: English — Full text — «Determination of urinary mitragynine concentration and severity of kratom dependence among people with kratom dependence in Malaysia»
- notes: Age and sex fields describe the whole sample, which is entirely kratom users. Every respondent is male (99 Malay, 1 Chinese); women refused to take part. Every respondent is a daily user, so no sex or frequency subgroups are extracted. The authors call every respondent 'people with kratom dependence' because of the daily-use inclusion rule, not because of the KDS result. People with significant health problems (kidney disease, diabetes, hypertension) were excluded. All respondents were employed. pct_other_opioid_use = 0 rests only on the urine rapid test (morphine MOP 0, methadone MTD 0). Sel…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Title claims people with kratom dependence in Malaysia, but the frame was community settings in one state (Penang). No register or listing frame is described, and women were not reached. — Page 3, Study design; Page 9, limitations — «Respondents were recruited from the community setting, where kratom use is endemic in the northern state of Penang (Malaysia).»
2. способ отбора: **no** — Purposive and convenience sampling. — Page 9, Discussion (limitations) — «this study is based on purposive and convenient sampling, therefore it may not reflect the actual kratom dependency scenario.»
3. размер выборки: **no** — Only 100 kratom users, which is below 246. — Table 2 (p.5) — «Respondent's number 100 100»
4. описание выборки и условий: **yes** — Age, sex, setting (Penang community), country and dates of data collection are all reported. — Page 3, Data collection; Page 5, Results — «The study data was collected between November 2024 and January 2025.»
5. охват (пропуски): **yes** — KDS categories cover all 100 respondents (45+46+9=100), so no dependence data are missing. — Page 6, Kratom use history — «According to the KDS, 45, 46 and 9 of the 100 respondents were mild, moderate and severe on kratom, respectively.»
6. валидность определения случая: **unclear** — The KDS is a kratom dependence screen (Saingam 2014, Thai). The language version used in Malaysia is not stated, and there is no Malaysian validation. Validation of the 14-34/35-48 band cut-offs cannot be checked from t… — Page 3, KDS; Page 8, Discussion — «we have applied the score number system developed by Saingam et al. (2014) to evaluate kratom dependence severity of the respondents.»
7. единое надёжное измерение: **yes** — Same KDS, same past-12-month frame and same thresholds for everyone, all given face to face by two trained research assistants. — Page 3, Data collection — «All the interviews were conducted through face-to-face interviews by two trained research assistants in the community.»
8. статистика (числитель и знаменатель): **yes** — Counts and denominator are clear (45/46/9 of 100), so a CI can be calculated, though none is given. — Table 2 (p.5) — «Kratom dependence score Mild 45 45 Moderate 46 46 Severe 9 9»
9. отклик: **unclear** — Response rate is not reported. The only non-response mentioned is women's refusal; numbers approached are not given. — Page 5, Results — «Despite an attempt to recruit female users with kratom dependence, the effort was unsuccessful as they refused to participate due to social censure and stigma.»

Правки:
- 

Проверено: да

---

## ST02 · Hill 2025 · Drug and alcohol dependence reports

Основной отчёт R0816: [текст](../../fulltext/text/R0816.txt) — «Clinically characterizing adults who use kava or kratom: Substance use disorder assessment challenges for increasingly popular botanical products.» — [DOI](https://doi.org/10.1016/j.dadr.2025.100394)
Не выписано ИИ: Kava-only users are excluded: 32 lifetime and 32 past-year kava users without past-year kratom use. Kava use disorder estimates (Table 4) are excluded because they concern kava, not kratom. Two cases were excluded by the authors for never using kava or kratom.
Расхождения в тексте: The text and abstract say 38.1% of past-year kratom users met KUD criteria, but the text gives n=103. 38.1% of 323 is 123, and the Table 3 severity counts also sum to 123 (mild 60 + moderate 29 + severe 34; none 200). The 103 appears to be a typo, possibly carried over from the cravings item (n=103), so the table value of 123 is used. The subgroup figures agree with the table: with kava 44.1% (n=45 = 22+10+13); without kava 35.3% (78 = 38+19+21). Table 4 note a says 'adapted for kratom' in the kava table; this looks like a copy error and does not affect the kratom estimates. The kratom compatibility item has n=312, not 323. In the text, the 'helpful' 84.0% and 'compatible' 12.0% figures match the with-kava column, not the total column (82.05%).
Заметка ИИ: One sample was extracted: 323 past-year kratom users. No age or sex is reported for the past-year group, so both were computed from Table 1 for the 335 lifetime kratom users. No funding statement appears in the text received; the competing-interest statement discloses past paid advisory roles with the International Plant and Herbal Alliance. The supplementary survey instrument was not received.

### ST02-1 · US online survey of kava/kratom users, past-year kratom users, Dec 2023-Jul 2024, n=323
Отчёты: R0816 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | DSM-5-SUD · DSM-5 criteria 0-1 (none) of 0-11 | **below** | **200 / 323** | 61.9 | Table 3 | «Past-year DSM−5 Kratom Use Disorder Severity ... None / 200 / 61.92» |
| E2 | all | DSM-5-SUD · DSM-5 criteria 2-3 (mild) | **L1** | **60 / 323** | 18.6 | Table 3 | «Mild / 60 / 18.58» |
| E3 | all | DSM-5-SUD · DSM-5 criteria 4-5 (moderate) | **L2** | **29 / 323** | 9.0 | Table 3 | «Moderate / 29 / 8.98» |
| E4 | all | DSM-5-SUD · DSM-5 criteria>=6 (severe) | **L3** | **34 / 323** | 10.5 | Table 3 | «Severe / 34 / 10.53» |
| E5 | all | DSM-5-SUD · DSM-5 criteria>=2 | **L1** | **123 / 323** | 38.1 | Results, Characteristics of past-year kratom use; Table 3 | «KUD criteria were met by 38.1 % (n = 103) of participants reporting any kratom use in the past year.» |
| E6 | past-year kratom use without past-year kava use | DSM-5-SUD · DSM-5 criteria 0-1 (none) of 0-11 | **below** | **143 / 221** | 64.7 | Table 3 | «None / 200 / 61.92 / 143 / 64.71 / 57 / 55.88» |
| E7 | past-year kratom use without past-year kava use | DSM-5-SUD · DSM-5 criteria 2-3 (mild) | **L1** | **38 / 221** | 17.2 | Table 3 | «Mild / 60 / 18.58 / 38 / 17.19 / 22 / 21.57» |
| E8 | past-year kratom use without past-year kava use | DSM-5-SUD · DSM-5 criteria 4-5 (moderate) | **L2** | **19 / 221** | 8.6 | Table 3 | «Moderate / 29 / 8.98 / 19 / 8.60 / 10 / 9.80» |
| E9 | past-year kratom use without past-year kava use | DSM-5-SUD · DSM-5 criteria>=6 (severe) | **L3** | **21 / 221** | 9.5 | Table 3 | «Severe / 34 / 10.53 / 21 / 9.50 / 13 / 12.75» |
| E10 | past-year kratom use without past-year kava use | DSM-5-SUD · DSM-5 criteria>=2 | **L1** | **78 / 221** | 35.3 | Results, Characteristics of past-year kratom use | «for respondents reporting past-year kratom use without kava use, KUD prevalence was lower, at 35.3 %.» |
| E11 | past-year kratom use with past-year kava use | DSM-5-SUD · DSM-5 criteria 0-1 (none) of 0-11 | **below** | **57 / 102** | 55.9 | Table 3 | «None / 200 / 61.92 / 143 / 64.71 / 57 / 55.88» |
| E12 | past-year kratom use with past-year kava use | DSM-5-SUD · DSM-5 criteria 2-3 (mild) | **L1** | **22 / 102** | 21.6 | Table 3 | «Mild / 60 / 18.58 / 38 / 17.19 / 22 / 21.57» |
| E13 | past-year kratom use with past-year kava use | DSM-5-SUD · DSM-5 criteria 4-5 (moderate) | **L2** | **10 / 102** | 9.8 | Table 3 | «Moderate / 29 / 8.98 / 19 / 8.60 / 10 / 9.80» |
| E14 | past-year kratom use with past-year kava use | DSM-5-SUD · DSM-5 criteria>=6 (severe) | **L3** | **13 / 102** | 12.7 | Table 3 | «Severe / 34 / 10.53 / 21 / 9.50 / 13 / 12.75» |
| E15 | past-year kratom use with past-year kava use | DSM-5-SUD · DSM-5 criteria>=2 | **L1** | **45 / 102** | 44.1 | Results, Characteristics of past-year kratom use | «KUD diagnostic threshold was met by a slightly greater proportion (44.1 %, n = 45) for respondents with past-year consumption of both kratom and kava.» |

- E1: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 0-1 criteria = below; у авторов: «None»; главная у авторов: no; период: past 12 months
- E2: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 2-3 criteria = L1; у авторов: «Mild»; главная у авторов: no; период: past 12 months
- E3: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 4-5 criteria = L2; у авторов: «Moderate»; главная у авторов: no; период: past 12 months
- E4: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=6 criteria = L3; у авторов: «Severe»; главная у авторов: no; период: past 12 months
- E5: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=2 criteria = L1; у авторов: «KUD criteria were met»; главная у авторов: yes; период: past 12 months; **расчёт: 38.1% x 323 = 123.1 -> 123; matches table mild+moderate+severe 60+29+34=123**; заметка: Text prints n=103, which does not match 38.1% of 323 or the table counts (123). The table value is used.
- E6: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 0-1 criteria = below; у авторов: «None»; главная у авторов: no; период: past 12 months; заметка: Subgroup named by authors (kava co-use).
- E7: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 2-3 criteria = L1; у авторов: «Mild»; главная у авторов: no; период: past 12 months
- E8: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 4-5 criteria = L2; у авторов: «Moderate»; главная у авторов: no; период: past 12 months
- E9: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=6 criteria = L3; у авторов: «Severe»; главная у авторов: no; период: past 12 months
- E10: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=2 criteria = L1; у авторов: «KUD prevalence»; главная у авторов: no; период: past 12 months; **расчёт: 35.3% x 221 = 78.0 -> 78; matches table 38+19+21=78**
- E11: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 0-1 criteria = below; у авторов: «None»; главная у авторов: no; период: past 12 months; заметка: Subgroup named by authors (kava co-use).
- E12: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 2-3 criteria = L1; у авторов: «Mild»; главная у авторов: no; период: past 12 months
- E13: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 4-5 criteria = L2; у авторов: «Moderate»; главная у авторов: no; период: past 12 months
- E14: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=6 criteria = L3; у авторов: «Severe»; главная у авторов: no; период: past 12 months
- E15: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=2 criteria = L1; у авторов: «KUD diagnostic threshold was met»; главная у авторов: no; период: past 12 months; заметка: Matches table 22+10+13=45.

**Ключевые поля выборки:**
- **n_users: 323** — Table 3 — «Clinical characteristics of kratom use among participants reporting past-year kratom use with and without past-year kava use (N = 323).»
- **sample_type: online_consumers** — Methods, Data collection — «Digital flyers advertising substances of interest were distributed online (e.g, X, Reddit). Kava- and kratom-specific flyers were used»
- **sampling: online opt-in** — Methods, Data collection; Limitations — «This cross-sectional study comprised a small convenience sample of kratom and kava consumers»
- **use_period: past 12 months** — Results, Characteristics of past-year kratom use; Table 3 — «Table 3 shows respondent characteristics for those who had used kratom within the past-year (N = 323)»
- **region: North America** — Abstract — «We conducted an online survey of US adults who have used kava or kratom.»

**Остальные поля:**
- country: USA — Abstract, Methods — «We conducted an online survey of US adults who have used kava or kratom.»
- data_years: 2023-2024 — Methods, Data collection — «Our cross-sectional online survey collected data between December 2023 and July 2024.»
- design: cross-sectional — Methods, Data collection — «Our cross-sectional online survey collected data between December 2023 and July 2024.»
- recruitment_channel: general — Methods, Data collection — «Digital flyers advertising substances of interest were distributed online (e.g, X, Reddit).»
- regular_use_required: no — Methods, Sample — «participants had to be > 18 years of age and to endorse lifetime use of one of the following substances: kratom, kava, akuamma seed, and/or tianeptine.»
- product_form: NR — Methods — «both botanicals are now sold in various product formulations across the US»
- response_rate: NR — Results — «A total of 406 adults completed the survey. Four cases were removed for not providing an age of > 18 years; 33 were removed for completing the survey in an unr…»
- age_mean: 40.1 — Table 1 — «Age Mean (SD) | 42.30 | (13.00) | 41.13 | (15.49) | 37.36 | (9.99)»
- age_sd: 12.0 — Table 1 — «Age Mean (SD) | 42.30 | (13.00) | 41.13 | (15.49) | 37.36 | (9.99)»
- pct_male: 60.6 — Table 1 — «Male | 114 | 60.96 | 22 | 68.75 | 89 | 60.14»
- pct_other_opioid_use: NR — Table 2 — «Prescription opioids (not prescribed) | 72 | 38.50 | 4 | 12.50 | 61 | 41.22»
- instruments: DSM-5 SUD past-year symptom checklist adapted for kratom (11 criteria; 13 self-report items, online, English) — Methods, Survey; Table 3 note a — «Participants could select multiple criteria, which were based on the 11 components of the DSM-5 criteria for a substance use disorder diagnosis, adapted for kr…»
- industry_funding: NR — Declaration of Competing Interest — «Within the past two years KES and EWB have served as paid scientific advisors to the International Plant and Herbal Alliance though do not have active relation…»
- funding_coi: Funding source not reported in text. COI: two authors (KES, EWB) were paid scientific advisors to the International Plant and Herbal Alliance in past two years and serve as expert witnesses in kratom legal cases. — Declaration of Competing Interest — «KES and EWB have served as paid scientific advisors to the International Plant and Herbal Alliance though do not have active relationships. KES and EWB also se…»
- pub_status: journal — Header — «Drug and alcohol dependence reports; DOI: 10.1016/j.dadr.2025.100394»
- language: English — Full text — «Clinically characterizing adults who use kava or kratom: Substance use disorder assessment challenges for increasingly popular botanical products»
- notes: Sample = past-year kratom users (N=323) of 335 lifetime kratom users (187 kratom-only + 148 both); 32 kava-only excluded. Age and sex are not given for the past-year group. They were computed for the 335 lifetime kratom users by pooling the Table 1 columns: age mean (187x42.30+148x37.36)/335=40.1; pooled SD ~12.0 (within- plus between-group variance); male (114+89)/335=60.6%. No opioid use is reported as current. Lifetime non-prescribed prescription-opioid use: 72/187 and 61/148 (39.7% of lifetime kratom users). Product form not reported. The data come from a larger survey of dietary-suppleme…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Frame is people reached by online flyers on social media (X, Reddit). This does not cover US kratom users. — Methods, Data collection — «Digital flyers advertising substances of interest were distributed online (e.g, X, Reddit).»
2. способ отбора: **no** — Convenience online opt-in sample. — Limitations — «This cross-sectional study comprised a small convenience sample of kratom and kava consumers»
3. размер выборки: **yes** — 323 past-year kratom users, which is at least 246. — Table 3 — «participants reporting past-year kratom use with and without past-year kava use (N = 323)»
4. описание выборки и условий: **yes** — Age, sex, online setting, country and dates are reported. Age and sex are given for lifetime-use groups. — Methods; Table 1 — «Our cross-sectional online survey collected data between December 2023 and July 2024.»
5. охват (пропуски): **yes** — The KUD severity distribution covers all 323 past-year kratom users (200+60+29+34=323). Invalid cases were removed before analysis. — Table 3 — «None | 200 | 61.92 ... Mild | 60 | 18.58 ... Moderate | 29 | 8.98 ... Severe | 34 | 10.53»
6. валидность определения случая: **yes** — DSM-5 SUD criteria adapted for kratom were assessed item by item with standard severity thresholds. — Table 3 note a — «If someone had 2–3 components, they were classified as having mild use disorder for kratom. If someone had 4–5 components, they were classified as having moder…»
7. единое надёжное измерение: **yes** — Same online self-report checklist, past-year time frame and thresholds for all participants. — Methods, Survey — «DSM-5 assessment for past-year SUD for kava and kratom»
8. статистика (числитель и знаменатель): **yes** — Counts and denominators are given in Table 3, so a CI can be calculated. The text gives n=103 for any KUD, but the table sums to 123 (38.1%). — Table 3; Results — «KUD criteria were met by 38.1 % (n = 103) of participants reporting any kratom use in the past year.»
9. отклик: **no** — Open online survey with no denominator of invited people. Response rate cannot be calculated or managed. — Results — «A total of 406 adults completed the survey.»

Правки:
- 

Проверено: да

---

## ST03 · Nimphae 2025 · Journal of Medical Bioscience

Основной отчёт R0922: [текст](../../fulltext/text/R0922.txt) · [PDF](../../fulltext/pdf/R0922.pdf) — «Substance use in the conscripts affiliated with the fort Ratchaburi Province» — [DOI](https://doi.org/10.58837/chula.jmbs.7.1.7)
Не выписано ИИ: Conscripts who did not use kratom and the rows for other substances (tobacco, alcohol, cannabis, amphetamine-type stimulants, opioids and others) were not extracted. Lifetime users of mixtures of kratom leaf decoction (n=143) were not made a separate sample, because they overlap with the leaf users by an unknown amount. Their estimates are given as a flagged subgroup inside the single sample.
Расхождения в тексте: 1) Denominators: Tables 4 and 5 use n=208 (lifetime leaf users, Table 3), even though Table 4 is titled 'past 3 months' and Table 5 'past 12 months'. Only 133 used leaves in the past 3 months, so people with no recent use are counted in the denominator. 2) SUDST labels: the Methods call the bands 'low / moderate / high level', while Table 5 calls them 'Mild / Moderate / Severe'. 3) The abstract prints '27.3' without a % sign. 4) Every figure checks against the table counts: SUDST leaves 137+46+23+2=208; any SUD 71/208=34.1%; cocktail 104+26+11+2=143; any SUD 39/143=27.3%; ASSIST leaves 100+101+7=208; cocktail 77+61+5=143. The only discrepancy is cocktail low risk: 77/143=53.8%, printed as 53.9%. 5) The text and abstract match the tables.
Заметка ИИ: Reference period for the denominator: LIFETIME use of kratom leaves (n=208). The authors' main estimate is past-12-month SUD (SUDST >=2) at 34.1% (71/208). The ASSIST time frame is the past 3 months, which has no exact code, so it is coded 'current'. Sex is not reported (the sample is presumably all male); age is for all 400 conscripts.

### ST03-1 · Conscripts at a fort in Ratchaburi Province, Thailand, 2023: lifetime kratom leaf users (n=208)
Отчёты: R0922 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | SUDST · SUDST 0-1 (no disorder) of 0-11 | **below** | **137 / 208** | 65.9 | Page 5, Table 5 | «Table 5. Substance use disorders in the past 12 months. ... Kratom leaves (n = 208) 137 65.9» |
| E2 | all | SUDST · SUDST 2-3 (low/mild) of 0-11 | **L1** | **46 / 208** | 22.1 | Page 5, Table 5 | «Kratom leaves (n = 208) 137 65.9 46 22.1 23 11.1 2 1.0» |
| E3 | all | SUDST · SUDST 4-5 (moderate) of 0-11 | **L2** | **23 / 208** | 11.1 | Page 5, Table 5 | «Kratom leaves (n = 208) 137 65.9 46 22.1 23 11.1 2 1.0» |
| E4 | all | SUDST · SUDST >=6 (high/severe) of 0-11 | **L3** | **2 / 208** | 1.0 | Page 5, Table 5 | «Kratom leaves (n = 208) 137 65.9 46 22.1 23 11.1 2 1.0» |
| E5 | all | SUDST · SUDST >=2 (any SUD) of 0-11 | **L1** | **71 / 208** | 34.1 | Page 1, Abstract; Page 4, Results | «SUD was found in 76.8%, 37.4%, 37.4%, 34.1%, 27.3%, 26.7% the of conscripts who used tobacco, alcohol, cannabis, kratom leaves, mixtures of kratom leaf decoction and amphetamine-type stimulants, respectively.» |
| E6 | all | ASSIST · ASSIST 0-3 (low risk) | **below** | **100 / 208** | 48.1 | Page 5, Table 4 | «Table 4. The level of risk from substance use in past 3 months. ... Kratom leaves (n = 208) 100 48.1 101 48.6 7 3.4» |
| E7 | all | ASSIST · ASSIST 4-26 (moderate risk) | **not_levelled** | **101 / 208** | 48.6 | Page 5, Table 4 | «Kratom leaves (n = 208) 100 48.1 101 48.6 7 3.4» |
| E8 | all | ASSIST · ASSIST >=27 (high risk) | **L2-screen** | **7 / 208** | 3.4 | Page 5, Table 4 | «Kratom leaves (n = 208) 100 48.1 101 48.6 7 3.4» |
| E9 | kratom cocktail (mixtures of kratom leaf decoction) lifetime users | SUDST · SUDST 0-1 (no disorder) of 0-11 | **below** | **104 / 143** | 72.7 | Page 5, Table 5 | «Mixtures of kratom leaf decoction (n = 143) 104 72.7 26 18.2 11 7.7 2 1.4» |
| E10 | kratom cocktail (mixtures of kratom leaf decoction) lifetime users | SUDST · SUDST 2-3 (low/mild) of 0-11 | **L1** | **26 / 143** | 18.2 | Page 5, Table 5 | «Mixtures of kratom leaf decoction (n = 143) 104 72.7 26 18.2 11 7.7 2 1.4» |
| E11 | kratom cocktail (mixtures of kratom leaf decoction) lifetime users | SUDST · SUDST 4-5 (moderate) of 0-11 | **L2** | **11 / 143** | 7.7 | Page 5, Table 5 | «Mixtures of kratom leaf decoction (n = 143) 104 72.7 26 18.2 11 7.7 2 1.4» |
| E12 | kratom cocktail (mixtures of kratom leaf decoction) lifetime users | SUDST · SUDST >=6 (high/severe) of 0-11 | **L3** | **2 / 143** | 1.4 | Page 5, Table 5 | «Mixtures of kratom leaf decoction (n = 143) 104 72.7 26 18.2 11 7.7 2 1.4» |
| E13 | kratom cocktail (mixtures of kratom leaf decoction) lifetime users | SUDST · SUDST >=2 (any SUD) of 0-11 | **L1** | **39 / 143** | 27.3 | Page 4, Results | «SUD was found in 76.8%, 37.4%, 37.4%, 34.1%, 27.3%, 26.7% the of conscripts who used tobacco, alcohol, cannabis, kratom leaves, mixtures of kratom leaf decoction» |
| E14 | kratom cocktail (mixtures of kratom leaf decoction) lifetime users | ASSIST · ASSIST 0-3 (low risk) | **below** | **77 / 143** | 53.8 | Page 5, Table 4 | «Mixtures of kratom leaf decoction (n = 143) 77 53.9 61 42.7 5 3.5» |
| E15 | kratom cocktail (mixtures of kratom leaf decoction) lifetime users | ASSIST · ASSIST 4-26 (moderate risk) | **not_levelled** | **61 / 143** | 42.7 | Page 5, Table 4 | «Mixtures of kratom leaf decoction (n = 143) 77 53.9 61 42.7 5 3.5» |
| E16 | kratom cocktail (mixtures of kratom leaf decoction) lifetime users | ASSIST · ASSIST >=27 (high risk) | **L2-screen** | **5 / 143** | 3.5 | Page 5, Table 4 | «Mixtures of kratom leaf decoction (n = 143) 77 53.9 61 42.7 5 3.5» |

- E1: cumulative: no; источник порога: validation paper; правило: SUDST row; 0-1 = below; у авторов: «No disorder»; главная у авторов: no; период: past 12 months; заметка: Kratom leaves; denominator is lifetime users.
- E2: cumulative: no; источник порога: validation paper; правило: SUDST row; 2-3 = L1; у авторов: «Mild (methods: low level of SUD)»; главная у авторов: no; период: past 12 months; заметка: Kratom leaves.
- E3: cumulative: no; источник порога: validation paper; правило: SUDST row; 4-5 = L2; у авторов: «Moderate»; главная у авторов: no; период: past 12 months; заметка: Kratom leaves.
- E4: cumulative: yes; источник порога: validation paper; правило: SUDST row; >=6 = L3; у авторов: «Severe (methods: high level of SUD)»; главная у авторов: no; период: past 12 months; заметка: Kratom leaves.
- E5: cumulative: yes; источник порога: validation paper; правило: SUDST row; >=2 = L1; у авторов: «Substance use disorder (SUD)»; главная у авторов: yes; период: past 12 months; **расчёт: 34.1% x 208 = 70.9 -> 71 (also 46+23+2 = 71 from Table 5)**; заметка: The paper itself reports this cumulative 'any SUD' figure (34.1%).
- E6: cumulative: no; источник порога: standard; правило: ASSIST row; 0-3 low risk is below the moderate band = below; у авторов: «Low risk»; главная у авторов: no; период: current; заметка: ASSIST covers the past 3 months (coded 'current'). The denominator includes lifetime users with no use in the past 3 months.
- E7: cumulative: no; источник порога: standard; правило: ASSIST row; 4-26 = not_levelled; у авторов: «Moderate risk»; главная у авторов: no; период: current; заметка: Past 3 months (coded 'current').
- E8: cumulative: yes; источник порога: standard; правило: ASSIST row; >=27 = L2-screen; у авторов: «High risk»; главная у авторов: no; период: current; заметка: Past 3 months (coded 'current').
- E9: cumulative: no; источник порога: validation paper; правило: SUDST row; 0-1 = below; у авторов: «No disorder»; главная у авторов: no; период: past 12 months; заметка: Separate substance row. Overlaps with the leaf users by an unknown amount; it is not a subset of n=208 and must not be added to it.
- E10: cumulative: no; источник порога: validation paper; правило: SUDST row; 2-3 = L1; у авторов: «Mild»; главная у авторов: no; период: past 12 months; заметка: Cocktail row; overlaps with leaf users.
- E11: cumulative: no; источник порога: validation paper; правило: SUDST row; 4-5 = L2; у авторов: «Moderate»; главная у авторов: no; период: past 12 months; заметка: Cocktail row; overlaps with leaf users.
- E12: cumulative: yes; источник порога: validation paper; правило: SUDST row; >=6 = L3; у авторов: «Severe»; главная у авторов: no; период: past 12 months; заметка: Cocktail row; overlaps with leaf users.
- E13: cumulative: yes; источник порога: validation paper; правило: SUDST row; >=2 = L1; у авторов: «Substance use disorder (SUD)»; главная у авторов: no; период: past 12 months; **расчёт: 27.3% x 143 = 39.0 -> 39 (also 26+11+2 = 39 from Table 5)**; заметка: Cocktail row; overlaps with leaf users.
- E14: cumulative: no; источник порога: standard; правило: ASSIST row; 0-3 = below; у авторов: «Low risk»; главная у авторов: no; период: current; заметка: Past 3 months (coded 'current'). Cocktail row; overlaps with leaf users. 77/143 = 53.8%, printed as 53.9%.
- E15: cumulative: no; источник порога: standard; правило: ASSIST row; 4-26 = not_levelled; у авторов: «Moderate risk»; главная у авторов: no; период: current; заметка: Past 3 months (coded 'current'). Cocktail row.
- E16: cumulative: yes; источник порога: standard; правило: ASSIST row; >=27 = L2-screen; у авторов: «High risk»; главная у авторов: no; период: current; заметка: Past 3 months (coded 'current'). Cocktail row.

**Ключевые поля выборки:**
- **n_users: 208** — Page 5, Table 5 — «Kratom leaves (n = 208) 137 65.9 46 22.1 23 11.1 2 1.0»
- **sample_type: other** — Page 2, Materials and methods — «The subjects were 400 conscripted soldiers affiliated with a fort in Ratchaburi Province; they had been in the fort for more than three months.»
- **sampling: NR** — Page 2, Materials and methods — «They participated in the research voluntarily by signing the consent form.»
- **use_period: lifetime any** — Page 4, Table 3; Page 5, Tables 4 and 5 — «Kratom leaves 208 52.0 133 33.3 [Lifetime n (%), Past 3 months n (%)]; Table 5: Kratom leaves (n = 208)»
- **region: Southeast Asia** — Page 2, Materials and methods — «400 conscripted soldiers affiliated with a fort in Ratchaburi Province»

**Остальные поля:**
- country: THA — Page 2, Materials and methods — «The subjects were 400 conscripted soldiers affiliated with a fort in Ratchaburi Province»
- data_years: 2023 — Page 1, Abstract (Methods) — «collected data from 400 conscripts between July - September 2023»
- design: cross-sectional — Page 2, Materials and methods — «This cross-sectional descriptive study has been approved by the Institutional Review Board»
- recruitment_channel: general — Page 2, Materials and methods — «400 conscripted soldiers affiliated with a fort in Ratchaburi Province; they had been in the fort for more than three months»
- regular_use_required: no — Page 4, Table 3 — «Lifetime ... Kratom leaves 208 52.0»
- product_form: mixed — Page 4, Table 3; Page 5, Table 5 — «Kratom leaves 208 52.0 ... Mixtures of kratom leaf decoction 143 35.8»
- response_rate: NR — Page 2, Materials and methods — «They participated in the research voluntarily by signing the consent form.»
- age_mean: 21.5 — Page 3, Table 1 — «(mean = 21.5, SD = 1.9, min = 18, max = 27)»
- age_sd: 1.9 — Page 3, Table 1 — «(mean = 21.5, SD = 1.9, min = 18, max = 27)»
- pct_male: NR — Page 2, Introduction — «serving the country as a conscript is one of the duties of every Thai man»
- pct_other_opioid_use: NR — Page 4, Table 3 — «Opioids 13 3.3 5 1.3»
- instruments: Substance Use Disorder Screening Test (SUDST, Thai; 11 yes/no DSM-5-based items); ASSIST version 3.1 (Thai translation by Assanangkornchai et al.) — Page 2, Materials and methods — «ASSIST version 3.1 ... translated into Thai by Asanangkornchai S, et al. ... the Substance use disorder screening test (SUDST) (9), developed by Sangdueanchai …»
- industry_funding: no — Page 8, Acknowledgements — «We did not receive any specific grant for this study from any funding agency in the public, commercial, or not-for-profit sectors.»
- funding_coi: No specific grant; authors declare no conflicts of interest — Page 8, Acknowledgements; Conflicts of interest statement — «None of the authors declare any potential or actual relationship, activity, or interest related to the content of this article.»
- pub_status: journal — Page 1, header — «J Med Biosci Vol. 7 No. 1 January - June 2025; 61 - 69 Original article»
- language: English — Page 1 — «Substance use in the conscripts affiliated with the fort Ratchaburi Province»
- notes: The kratom users are a subsample of 400 conscripts. The denominator is lifetime users of kratom leaves (n=208; 133 used in the past 3 months). Users of 'mixtures of kratom leaf decoction' (kratom cocktail; lifetime n=143) are a separate row in the tables. How many people are in both groups is not reported, so the two groups cannot be combined. Cocktail estimates are given as a separate subgroup, not as part of the 208. Age (mean 21.5, SD 1.9) is for all 400 conscripts. Sex is not reported; the paper only says conscription is a duty of Thai men, which implies an all-male sample. The urine test…

**Риск смещения (JBI):**
1. рамка выборки: **yes** — The frame is the conscripts of the named fort who had been there more than 3 months, which is the population the study claims to describe. — Page 2, Materials and methods — «The subjects were 400 conscripted soldiers affiliated with a fort in Ratchaburi Province; they had been in the fort for more than three months.»
2. способ отбора: **unclear** — The paper does not say how the 400 were selected; it only says participation was voluntary. — Page 2, Materials and methods — «They participated in the research voluntarily by signing the consent form.»
3. размер выборки: **no** — 208 kratom leaf users, which is below 246. — Page 5, Table 5 — «Kratom leaves (n = 208)»
4. описание выборки и условий: **unclear** — Age, setting, country and dates are reported. Sex is not stated explicitly (only implied by conscription of Thai men). — Page 3, Table 1; Page 2 — «(mean = 21.5, SD = 1.9, min = 18, max = 27) ... from July to September 2023»
5. охват (пропуски): **yes** — The SUDST categories add up to all 208 kratom leaf users, so no dependence data are missing. — Page 5, Table 5 — «Kratom leaves (n = 208) 137 65.9 46 22.1 23 11.1 2 1.0»
6. валидность определения случая: **yes** — The SUDST is a validated checklist with one item per DSM-5 criterion, scored by criterion count (treated as a DSM-5 checklist in the levels table). — Page 2, Materials and methods — «SUDST ... based on the DSM-5 diagnosis ... It consists of 11 yes/no questions, with score 2 - 3 indicates a low level, 4 - 5 suggests a moderate level and 6 or…»
7. единое надёжное измерение: **yes** — Everyone answered the same questionnaires in individual interviews, with the same thresholds. — Page 2, Materials and methods — «Data were collected using questionnaires through individual interviews from July to September 2023.»
8. статистика (числитель и знаменатель): **yes** — Counts and the kratom-user denominator are printed, so CIs can be calculated. — Page 5, Tables 4 and 5 — «Kratom leaves (n = 208) 137 65.9 46 22.1 23 11.1 2 1.0»
9. отклик: **unclear** — No response rate or number of conscripts invited is reported. — Page 2, Materials and methods — «They participated in the research voluntarily by signing the consent form.»

Правки:
- 

Проверено: да

---

## ST04 · Yang 2023 · PloS one

Основной отчёт R1857: [текст](../../fulltext/text/R1857.txt) — «Kratom use disorder and unfolded protein response: Evaluating their relationship in a case control study.» — [DOI](https://doi.org/10.1371/journal.pone.0287466)
Приложен R1161: [текст](../../fulltext/text/R1161.txt) — «The Evaluation Of Endoplasmic Reticulum Stress Among Regular Kratom Users And Its Implications For Kratom Dependence An…»
Связь отчётов: Same Penang case-control sample of 60 regular kratom users (USM/AMDI, recruited 2019-2020): R1857 (PLOS ONE 2023) and R1161 (PhD thesis, 2024)
Не выписано ИИ: 50 healthy non-drug-using controls (never used kratom), excluded by protocol because they are not kratom users. 40 potential kratom users excluded at eligibility screening (positive urine drug test, illicit drug use, medical or psychiatric illness); no dependence data for them.
Расхождения в тексте: R1857 text: 41.7% (n = 25) of 60, consistent (25/60 = 41.67%). R1857's statistical analysis section says descriptive statistics for 'KDS scores' were computed, but the article shows no KDS results. R1161 (thesis) says the KDS was given to all 60 users (Fig 4.17 'The severity of kratom dependence among the kratom users'; Table 4.2), but the thesis text received stops in Chapter 2 (section 2.4.1). KDS bands and counts therefore could not be extracted. The thesis abstract calls the users 'regular kratom users' recruited from the same community, and the funding (FRGS) matches. No conflicting numbers were found between the reports in the parts received.
Заметка ИИ: Draft extraction. Main gaps: S2/S3 Tables (age, sex, use characteristics) were not received, and the R1161 results chapter (KDS) is missing from the text supplied. Please get the full thesis (Table 4.1, Table 4.2, Fig 4.17) to add the KDS estimate and age/sex. KUD instrument coded as interview (psychiatrist DSM-5 assessment), L1, past 12 months.

### ST04-1 · Penang community regular kratom users, Malaysia, 2019-2020, n=60 (case-control study, users only)
Отчёты: R1857 (main); R1161

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | interview · DSM-5 criteria>=2 of 11 (psychiatrist assessment) | **L1** | **25 / 60** | 41.7 | R1857, Results, Participants; Methods, Outcome variable | «The prevalence of kratom use disorder among the regular kratom users in this study was 41.7% (n = 25).» |
| E2 | all | interview · DSM-5 criteria 0-1 of 11 (psychiatrist assessment; no KUD) | **below** | **35 / 60** | 58.3 | R1857, Methods, Outcome variable; Results, Participants | «This assessment classified regular kratom users into "those with kratom use disorder" or "those without kratom use disorder".» |

- E1: cumulative: yes; источник порога: standard; правило: interview row (psychiatrist applying DSM-5 criteria); any disorder = L1; у авторов: «kratom use disorder»; главная у авторов: yes; период: past 12 months; заметка: 25/60 = 41.7%, matches the text. Severity (mild/moderate/severe) not reported. Could also be coded DSM-5-SUD (same level, L1). The sample excluded anyone with other drug or alcohol use or psychiatric or medical illness.
- E2: cumulative: no; источник порога: standard; правило: interview row; no disorder = below; у авторов: «those without kratom use disorder»; главная у авторов: no; период: past 12 months; **расчёт: 60 - 25 = 35**; заметка: Complement of the KUD category; the count is not printed.

**Ключевые поля выборки:**
- **n_users: 60** — Methods, Study design and participants — «Hence, in total, 60 regular kratom users and 50 healthy, non-drug-using control-group members participated in the study»
- **sample_type: community_users** — Methods, Study design and participants — «five to six informants who regularly used kratom were recruited from the targeted community to assist the research team in recruiting participants»
- **sampling: snowball** — Methods, Study design and participants — «This study's participants were recruited using exponential discriminative snowball sampling.»
- **use_period: current** — Methods, Study design and participants — «(1) a daily kratom consumption history of 12 consecutive months»
- **region: Southeast Asia** — Methods, Study design and participants — «recruited from the same targeted community in the State of Penang in Malaysia»

**Остальные поля:**
- country: MYS — Methods, Study design and participants — «recruited from the same targeted community in the State of Penang in Malaysia»
- data_years: 2019-2020 — Methods, Study design and participants — «Subject recruitment and data collection commenced from January 2019 to January 2020.»
- design: case-control (users only) — Methods, Study design and participants — «This case-control study was conducted from January 2019 to December 2020.»
- recruitment_channel: general — Methods, Study design and participants — «the informants recruited potential regular kratom users and healthy control-group participants, who referred additional prospective participants to the study»
- regular_use_required: daily kratom consumption for 12 consecutive months — Methods, Study design and participants — «we defined regular kratom use as having history of daily consumption of kratom for 12 consecutive months»
- product_form: traditional leaf — Methods, Explanatory variables (2) Kratom use characteristi… — «On average, how many glasses of kratom juice do you drink on a daily basis?»
- response_rate: NR — Methods, Study design and participants — «Initially, 100 potential kratom users and 100 potential control subjects were identified by snowball sampling. After being screened for the study's eligibility…»
- age_mean: NR — Results, Participants — «All participants' sociodemographic and clinical characteristics are summarized in S2 Table.»
- age_sd: NR — Results, Participants — «All participants' sociodemographic and clinical characteristics are summarized in S2 Table.»
- pct_male: NR — Results, Participants — «All participants' sociodemographic and clinical characteristics are summarized in S2 Table.»
- pct_other_opioid_use: 0 — Methods, Screening (3) illicit drug and alcohol use — «Those who had any past and current history of any illicit drug and alcohol use that were screened were excluded from the study.»
- instruments: DSM-5 substance use disorder criteria for kratom (11 criteria), assessed by the study psychiatrist (language of assessment NR; participants had to speak Malay); Kratom Dependence Scale (KDS) per R1161 (version NR; results not in the text received) — Methods, Outcome variable; R1161, Abstract — «assessment of participants was performed by the psychiatrist in the research team using the DSM-5 diagnostic criteria»
- industry_funding: no — Funding Statement — «This work was supported by the Fundamental Research Grant Scheme of the Ministry of Higher Education Malaysia ... and Reseach Grant from Xinxiang Medical Unive…»
- funding_coi: Public/academic grants (Malaysian Ministry of Higher Education FRGS; Xinxiang Medical University). Funders had no role. No competing-interests statement in the text received. — Funding Statement — «The funders has no role in study design, collection, analysis, or interpretation of data, writing the manuscript, and the decision to submit the manuscript for…»
- pub_status: journal — Header — «Year: 2023; venue: PloS one; DOI: 10.1371/journal.pone.0287466»
- language: English — Full text — «Kratom use disorder and unfolded protein response: Evaluating their relationship in a case control study»
- notes: Same 60 users as R1161 (Yang Bin PhD thesis, USM 2024). The thesis says the KDS and BDI-II were given to all users, but the thesis text received stops in Chapter 2, so no KDS results could be extracted. Age, sex and use characteristics are in S2/S3 Tables (not received); in the main text age is coded only as <40 vs >=40. Users with any past or current illicit drug or alcohol use (urine tested), psychiatric illness, medical illness or ER-stress-altering medication were excluded (40 of 100 potential users), so this is a selected kratom-only sample. use_period coded 'current' (daily use for 12 c…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame was the informant networks of one targeted community in Penang, not the population of regular kratom users in Malaysia or Penang. The authors say it may not be representative. — Discussion, limitations — «this study recruited participants only from Penang State ... our study may not represent the entire kratom user population in Malaysia»
2. способ отбора: **no** — Snowball sampling through informants. — Methods, Study design and participants — «This study's participants were recruited using exponential discriminative snowball sampling.»
3. размер выборки: **no** — 60 kratom users, below 246. — Methods, Study design and participants — «in total, 60 regular kratom users and 50 healthy, non-drug-using control-group members participated»
4. описание выборки и условий: **no** — Setting, country and dates are reported. Age and sex of the users are not in the text received (only in S2 Table, not received), so two items are missing. — Results, Participants — «All participants' sociodemographic and clinical characteristics are summarized in S2 Table.»
5. охват (пропуски): **yes** — No missing data reported. — Methods, Statistical analysis — «There was no missing data.»
6. валидность определения случая: **yes** — The psychiatrist assessed the DSM-5 SUD criteria for kratom item by item (11 criteria listed, >=2 in 12 months). — Methods, Outcome variable — «The presence of at least two of the above diagnostic criteria for 12 consecutive months fulfilled a diagnosis of kratom use disorder, in which assessment of pa…»
7. единое надёжное измерение: **yes** — The same psychiatrist assessment, criteria, time frame and threshold were applied to all regular kratom users. — Methods, Outcome variable — «This assessment classified regular kratom users into "those with kratom use disorder" or "those without kratom use disorder".»
8. статистика (числитель и знаменатель): **yes** — Numerator 25 and denominator 60 are clear, so a CI can be calculated. — Results, Participants — «The prevalence of kratom use disorder among the regular kratom users in this study was 41.7% (n = 25).»
9. отклик: **unclear** — No refusals are reported among kratom users (3 refusals among controls only). The number invited or approached is not clear for snowball recruitment. — Methods, Study design and participants — «Additionally, three prospective control-group participants were excluded because they refused to participate in the study for no stated reason.»

Правки:
- 

Проверено: да

---

## ST05 · Koktavá 2024 · Digital Repository (National Repository of Grey Literature)

Основной отчёт R1294: [текст](../../fulltext/text/R1294.txt) — «Prevalence and patterns of kratom use in the Czech population and risk of loss of controlled use over time: cross-sectional questionnaire survey»
Не выписано ИИ: Respondents who never used kratom (331 - 259 = 72) are controls and were excluded. The 35 lifetime users with no past-30-day use did not get the SDS. They stay in the descriptive sample (n=259) but are not in the SDS denominator (n=224).
Расхождения в тексте: 1) SDS denominator: the 28.6% (≥6) is of 'souboru' with no n. The SDS went only to past-30-day users, and Graf 20 has n=224, so 224 was used. 2) SDS item 3 wording differs: results p.52 say 'Trápilo Vás někdy, že si nedáte kratom?' [bothered that you won't take kratom], while the appendix item 38 says 'Trápilo Vás někdy, že berete kratom?' [bothered that you take kratom]. 3) Table 15: 127 successful quitters vs 124 in the text. 4) 259 is printed as 78.0% of 331; it is actually 78.2%. 5) Table 20: stimulants 49 = '49.0%', but 49/217 = 22.6%. 6) Table 13 'not used' 5.9% vs 5.8% elsewhere. 7) Form section says 'Z 244 dotázaných' although n=224. 8) The discussion says three quarters reported long-term health problems; the results say 55/224 (25.0%). 9) Table 22's 12-month column omits the rarer frequencies and lists 17 'not used in past 30 days' in a 244 total. 10) The age table has a 15-19…
Заметка ИИ: One sample was extracted. Lifetime users (n=259) are the study sample. Only past-30-day users (n=224) answered the SDS, so they are its denominator. The only dependence measure is an author-adapted Czech SDS. The ≥6 share (28.6%) appears only as a percentage, and the count 64 is derived. No page markers exist in the text; printed thesis page numbers are used.

### ST05-1 · Czech online survey of adults who used kratom, Facebook kratom groups, Feb-Mar 2024 (lifetime users n=259; SDS among past-30-day users n=224)
Отчёты: R1294 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | SDS · SDS>=6 of 0-15 | **L2-scale** | **64 / 224** | 28.6 | p. 57, section 9.1 (Discussion); p. 54, Graf 20 | «Přibližně pětina souboru získala nula bodů, celkem 6 a více bodů získalo 28,6 % souboru. [About a fifth of the sample scored zero; in total 28.6% of the sample scored 6 or more points.]» |
| E2 | all | SDS · SDS=0 of 0-15 | **below** | **47 / 224** | 21.0 | p. 54, text above Graf 20 | «Nejpočetnější skupina získala skóre 0 (n = 47). Následoval bodový zisk 1 (n = 28), 5 (n = 26) a 2 (n = 23).» |

- E1: cumulative: yes; источник порога: study's own; правило: SDS row; authors' fixed cut-off >=6 = L2-scale (no kratom-validated cut-off); у авторов: «6 a více bodů [6 or more points] (no dependence label; authors say most respond…»; главная у авторов: yes; период: NR; **расчёт: 28.6% x 224 = 64.06 -> 64 (if the denominator were the 259 lifetime users: 74.07 -> 74)**; заметка: Denominator taken as 224 because only past-30-day users got the SDS and Graf 20 has n=224. The text says only 'souboru' [the sample]. The authors cite cut-offs of 2-5 for other drugs and give no rationale for 6. SDS items have no time frame. Count not printed.
- E2: cumulative: no; источник порога: study's own; правило: SDS row; score 0 is below any dependence cut-off = below; у авторов: «skóre 0 / nula bodů [score 0 / zero points]»; главная у авторов: no; период: NR; заметка: Context only. 47/224 = 21.0%, consistent with 'about a fifth'. Other single-score counts: 1 = 28, 2 = 23, 5 = 26; the rest are only in Graf 20 (image not received).

**⚠ Проверка скриптом (обратите внимание):**
- all: категории (E2+E1) дают 111, а n = 224

**Ключевые поля выборки:**
- **n_users: 224** — p. 54, Graf 20; p. 32 — «Graf 20 Počty bodů u jednotlivých respondentů (n = 224) [Scores of individual respondents]; 224 (86,5 %), že užili kratom v posledních 30 dnech»
- **sample_type: online_consumers** — p. 24, section 7.4 — «Dotazník byl nasdílen do různých skupin sdružujících osoby se zájmem o kratom. [The questionnaire was shared in various groups of people interested in kratom.]»
- **sampling: online opt-in** — p. 22, section 7.2 — «Výzkumný soubor byl vybrán nepravděpodobnostním výběrem za pomoci distribuce po sociální síti... případně se uplatnila i metoda sněhové koule [non-probability selection via social network distribution... snowball method also applied]»
- **use_period: past 30 days** — p. 23-24, section 7.3; p. 54, Graf 20 — «Poslední část dotazníku se věnovala pouze těm, kteří kratom užili v posledních 30 dnech... K tomu byla použita škála závažnosti [The last part was only for those who used kratom in the past 30 days... the severity scale was used]»
- **region: Europe** — p. 22, section 7.2 — «žijícími na území České republiky [living in the Czech Republic]»

**Остальные поля:**
- country: CZE — p. 22, section 7.2 — «Výzkumný soubor byl tvořen osobami staršími 18 let žijícími na území České republiky. [The study sample consisted of people over 18 living in the Czech Republi…»
- data_years: 2024 — p. 24, section 7.4 — «Data určená pro ostrý výzkum byla sbírána během února a března 2024 pomocí sociální sítě Facebook. [Data for the main study were collected in February and Marc…»
- design: cross-sectional — p. 23, section 7.3 — «Jedná se o kvantitativní výzkum, konkrétněji o dotazníkovou průřezovou studii. [Quantitative research, specifically a cross-sectional questionnaire study.]»
- recruitment_channel: advocacy or vendor channels — p. 22, section 7.2; p. 55, section 9 — «K distribuci byly využity skupiny a fóra sdružující osoby se zkušeností s kratomem [Groups and forums of people with kratom experience were used]; ve facebooko…»
- regular_use_required: no — p. 23, section 7.2 — «Kritéria pro účast ve výzkumu byla: Věk minimálně 18 let. Místo aktuálního pobytu na území České republiky. Informovaný souhlas [Criteria: age at least 18; res…»
- product_form: commercial powder or capsules — p. 45, section 8.3 — «Nejčastěji užívanou formou kratomu mezi respondenty je bezesporu prášek. Ten užívá 96,0 % dotázaných. [The most used form is powder, used by 96.0%.]»
- response_rate: NR — p. 59, section 9.3 — «i když skupiny obsahovaly tisíce členů, výsledný počet odpovědí není příliš vysoký [although the groups had thousands of members, the number of responses is no…»
- age_mean: 28.6 — p. 26, section 8.1 — «Průměrný věk ve výzkumném vzorku byl 28,6 let a medián byl 25,5 roku. [Mean age in the sample was 28.6 years, median 25.5.]»
- age_sd: NR — p. 26, section 8.1 — «Průměrný věk ve výzkumném vzorku byl 28,6 let a medián byl 25,5 roku. Nejnižší věk byl 18 let a nejvyšší 65 let.»
- pct_male: 79.5 — p. 26, section 8.1 — «Výzkumu se zúčastnilo 206 mužů, což je 79,5 %, a 53 žen, což činí 20,5 %. [206 men (79.5%) and 53 women (20.5%).]»
- pct_other_opioid_use: NR — p. 38, Tabulka 20 — «Tlumivé látky (benzodiazepiny, opiáty, sedativa, …) 32 15,1 [Depressants (benzodiazepines, opiates, sedatives) 32, 15.1% - ever combined with kratom]»
- instruments: Severity of Dependence Scale (Gossop 1995), 5 items scored 0-3 (0-15), Czech adaptation for kratom made by the author within her own questionnaire (no validation reported) — p. 23-24, section 7.3 — «Autorka se při tvorbě dotazníku inspirovala Škálou závažnosti závislosti (Severity of dependence scale) (Gossop et al., 1995)... Maximální možný bodový zisk je…»
- industry_funding: NR — Whole text (no funding statement) — «Bakalářská práce (Bc.). Univerzita Karlova, 1. lékařská fakulta, Klinika adiktologie. Vedoucí bakalářské práce doc. MUDr. Viktor Mravčík, Ph.D.»
- funding_coi: No funding or conflict-of-interest statement; unfunded bachelor's thesis at Charles University (supervisor V. Mravčík) — Identifikační záznam — «Bakalářská práce (Bc.). Univerzita Karlova, 1. lékařská fakulta, Klinika adiktologie.»
- pub_status: thesis — Title page; Identifikační záznam — «Bakalářská práce (Bc.). Univerzita Karlova, 1. lékařská fakulta, Klinika adiktologie. [Bachelor's thesis, Charles University, First Faculty of Medicine]»
- language: Czech (English abstract) — Whole text; Abstract — «Míra a vzorce užívání kratomu v dospělé populaci a riziko ztráty kontroly v průběhu užívání kratomu: dotazníková průřezová studie»
- notes: Bachelor's thesis. 331 analysed respondents (332 minus 1 excluded); 259 lifetime users make up the study sample; 244 past-12-month users; 224 past-30-day users. Only past-30-day users (n=224) got the SDS, so n_users=224 is the denominator of the SDS estimate. Age (mean 28.6) and % male (79.5) are for the 259 lifetime users. Derived from Table 9 percentages: about 186 men and 38 women among the 224. The SDS items have no time frame ('ever'). Withdrawal-like feelings after stopping, 158/259 (61.0%), recorded as context only. Tried to quit 174/259; unsuccessful 47/174 (ad hoc, not extracted). Th…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is adult kratom users in the Czech Republic; the frame was Facebook kratom-interest groups only. — p. 24, section 7.4 — «Dotazník byl nasdílen do různých skupin sdružujících osoby se zájmem o kratom.»
2. способ отбора: **no** — Non-probability purposive online sampling plus snowball. — p. 22, section 7.2 — «nepravděpodobnostním výběrem ... (záměrný výběr) a případně se uplatnila i metoda sněhové koule»
3. размер выборки: **no** — The SDS denominator is 224 past-30-day users, below 246. — p. 54, Graf 20 — «Počty bodů u jednotlivých respondentů (n = 224)»
4. описание выборки и условий: **yes** — Age, sex, setting (online Facebook groups), country and dates (Feb-Mar 2024) are all reported. — p. 24, 7.4; p. 26, 8.1 — «sbírána během února a března 2024 pomocí sociální sítě Facebook ... Průměrný věk ve výzkumném vzorku byl 28,6 let»
5. охват (пропуски): **yes** — Graf 20 gives SDS scores for all 224 past-30-day users; no missing SDS data apparent. — p. 54, Graf 20; p. 32 — «Graf 20 Počty bodů u jednotlivých respondentů (n = 224)»
6. валидность определения случая: **no** — SDS adapted by the author without validation; the 6+ cut-off was not validated in kratom users, and the authors note no kratom cut-off exists and that diagnostic value is limited. — p. 57, section 9.1 — «Neexistuje však jednoznačná odpověď na to, co už závislost je a co není. Kratom také není zahrnut do vyhodnocovacích tabulek... diagnostický přínos použitého n…»
7. единое надёжное измерение: **yes** — The same self-administered Google Forms SDS and scoring were used for all past-30-day users. — p. 23-24, section 7.3 — «Respondentům bylo v dotazníku položeno všech 5 otázek. Odpověď „nikdy/téměř nikdy“ byla hodnocena 0 body ... „vždy, téměř vždy“ 3 body.»
8. статистика (числитель и знаменатель): **unclear** — Only a percentage (28.6%) of 'the sample' is given; the count is not printed. The denominator is probably 224 (Graf 20) but could be 259. No CI. — p. 57, section 9.1 — «celkem 6 a více bodů získalo 28,6 % souboru»
9. отклик: **no** — Open online survey posted to groups; no denominator of invited people and no handling of non-response. — p. 59, section 9.3 — «i když skupiny obsahovaly tisíce členů, výsledný počet odpovědí není příliš vysoký»

Правки:
- 

Проверено: да

---

## ST06 · Rogers 2024 · Drug and alcohol dependence

Основной отчёт R1402: [текст](../../fulltext/text/R1402.txt) — «Kratom addiction per DSM-5 SUD criteria, and kratom physical dependence: Insights from dosing amount versus frequency.» — [DOI](https://doi.org/10.1016/j.drugalcdep.2024.111329)
Приложен R1425: [текст](../../fulltext/text/R1425.txt) — «Ecological Momentary Assessment of Self-Reported Kratom Use, Effects, and Motivations Among US Adults.»
Связь отчётов: Same NIDA nationwide remote EMA study of US adults who use kratom regularly (enrolled July-November 2022, n = 395 surveyed): R1402 (baseline DSM-5 KUD by severity) and R1425 (EMA paper)
Не выписано ИИ: Not extracted as separate samples: the 357 EMA completers (R1425; 238/357 = 66.7% with KUD >=2), which are a subset of the 395, and the EMA use-pattern clusters A-E (R1425). No KUD prevalence by sex or by use frequency was reported. Men had higher symptom counts, but only in regression models.
Расхождения в тексте: 1) KUD prevalence: R1402 gives past-year KUD (>=2) 46.6% and lifetime 63.5% (n=395 implied). R1425 gives 238/357 (66.7%) meeting KUD (>=2) among EMA completers and says the survey covered 'past-year criteria'. That figure is closer to R1402's lifetime figure. R1402 values used, per the job. 2) R1402 abstract: 'KUD symptom counts were mostly in the mild/moderate range (80.7%)'. This does not match the text: of lifetime KUD cases, mild+moderate is 52.9/63.5 = 83.3%; of past-year cases it is 40.0/46.6 = 85.8%. 3) Demographics: R1402 says 81.3% White and 61.3% full-time employed; the R1425 table for the same 395 says White 359 (90.9%) and full-time 223 (56.5%). Age (38.1, SD 11.2) and male share (54.9%, 217/395) agree. 4) Dates: R1402 says enrolled July-November 2022; R1425 says recruited July 1-October 31, 2022. 5) Counts are derived from percentages; derived subcategories sum to the deriv…
Заметка ИИ: Draft for reviewer check. Supplement (Supplemental Table 1 with KUD counts and other SUDs; full survey) not received. Location labels are section names because the text has no page markers. Codes a reviewer should check: recruitment channel (social media plus advocacy/vendor channels), and design coded as an EMA study (the estimate comes from the baseline survey).

### ST06-1 · US nationwide remote EMA study of adults who use kratom regularly, baseline survey, 2022, n=395
Отчёты: R1402 (main); R1425

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | DSM-5-SUD · DSM-5 criteria>=2 | **L1** | **184 / 395** | 46.6 | R1402, KUD descriptive results | «Past-year KUD (2+ past-year symptoms) was met by 46.6%, with 27.3% being mild, 12.7% moderate, and 6.6% severe.» |
| E2 | all | DSM-5-SUD · DSM-5 criteria 2-3 (mild) | **L1** | **108 / 395** | 27.3 | R1402, KUD descriptive results | «Past-year KUD (2+ past-year symptoms) was met by 46.6%, with 27.3% being mild, 12.7% moderate, and 6.6% severe.» |
| E3 | all | DSM-5-SUD · DSM-5 criteria 4-5 (moderate) | **L2** | **50 / 395** | 12.7 | R1402, KUD descriptive results | «Past-year KUD (2+ past-year symptoms) was met by 46.6%, with 27.3% being mild, 12.7% moderate, and 6.6% severe.» |
| E4 | all | DSM-5-SUD · DSM-5 criteria>=6 (severe) | **L3** | **26 / 395** | 6.6 | R1402, KUD descriptive results; Discussion | «Participants endorsed 1.9 past-year KUD symptoms on average, with 6.6% meeting the symptom-count cutoff (6 or more symptoms) for severe KUD.» |
| E5 | all | DSM-5-SUD · DSM-5 criteria>=2 | **L1** | **251 / 395** | 63.5 | R1402, KUD descriptive results | «Lifetime KUD criteria (2+ lifetime symptoms) were met by 63.5%, with 33.2% being mild (2–3), 19.7% moderate (4–5), and 10.6% severe (6+).» |
| E6 | all | DSM-5-SUD · DSM-5 criteria 2-3 (mild) | **L1** | **131 / 395** | 33.2 | R1402, KUD descriptive results | «with 33.2% being mild (2–3), 19.7% moderate (4–5), and 10.6% severe (6+)» |
| E7 | all | DSM-5-SUD · DSM-5 criteria 4-5 (moderate) | **L2** | **78 / 395** | 19.7 | R1402, KUD descriptive results | «with 33.2% being mild (2–3), 19.7% moderate (4–5), and 10.6% severe (6+)» |
| E8 | all | DSM-5-SUD · DSM-5 criteria>=6 (severe) | **L3** | **42 / 395** | 10.6 | R1402, KUD descriptive results | «with 33.2% being mild (2–3), 19.7% moderate (4–5), and 10.6% severe (6+)» |

- E1: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=2 criteria = L1; у авторов: «Past-year KUD (2+ past-year symptoms)»; главная у авторов: yes; период: past 12 months; **расчёт: 46.6% x 395 = 184.07 -> 184**; заметка: Denominator taken as all 395 survey completers (not stated). R1425 reports 238/357 (66.7%) meeting KUD >=2, described as past-year; see consistency notes.
- E2: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 2-3 criteria = L1; у авторов: «mild»; главная у авторов: no; период: past 12 months; **расчёт: 27.3% x 395 = 107.84 -> 108**; заметка: Percentage only.
- E3: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 4-5 criteria = L2; у авторов: «moderate»; главная у авторов: no; период: past 12 months; **расчёт: 12.7% x 395 = 50.17 -> 50**; заметка: Percentage only.
- E4: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=6 criteria = L3; у авторов: «severe»; главная у авторов: no; период: past 12 months; **расчёт: 6.6% x 395 = 26.07 -> 26**; заметка: Percentage only.
- E5: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=2 criteria = L1; у авторов: «Lifetime KUD criteria (2+ lifetime symptoms)»; главная у авторов: no; период: lifetime; **расчёт: 63.5% x 395 = 250.83 -> 251**; заметка: Percentage only; denominator taken as 395.
- E6: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 2-3 criteria = L1; у авторов: «mild (2–3)»; главная у авторов: no; период: lifetime; **расчёт: 33.2% x 395 = 131.14 -> 131**; заметка: Percentage only.
- E7: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 4-5 criteria = L2; у авторов: «moderate (4–5)»; главная у авторов: no; период: lifetime; **расчёт: 19.7% x 395 = 77.82 -> 78**; заметка: Percentage only.
- E8: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=6 criteria = L3; у авторов: «severe (6+)»; главная у авторов: no; период: lifetime; **расчёт: 10.6% x 395 = 41.87 -> 42**; заметка: Percentage only.

**Ключевые поля выборки:**
- **n_users: 395** — Results — «After screening, 1152 candidates were sent enrollment invitations (to reach an IRB-approved enrollment ceiling of 400), and 395 completed the survey.»
- **sample_type: online_consumers** — R1425, Table (How did you hear about the study?) — «Reddit | 131 (36.7) | 14 (36.8) | 145 (36.7); Facebook ... 88 (22.3); American Kratom Association ... 66 (16.7)»
- **sampling: online opt-in** — Conclusions — «The current findings have the limitations inherent to retrospective self-report and possible self-selection bias»
- **use_period: current** — Abstract; R1425, Study Sample — «we enrolled 395 active US adult kratom consumers»
- **region: North America** — Abstract — «we enrolled 395 active US adult kratom consumers»

**Остальные поля:**
- country: USA — Abstract, Methods — «we enrolled 395 active US adult kratom consumers into a remote study with a baseline survey»
- data_years: 2022 — Study recruitment and sample — «Between July-November 2022, we enrolled US adults who use kratom regularly into a nationwide ecological momentary assessment (EMA) study»
- design: laboratory or EMA study — Study recruitment and sample — «we enrolled US adults who use kratom regularly into a nationwide ecological momentary assessment (EMA) study (Smith et al., 2024), that included a baseline sur…»
- recruitment_channel: advocacy or vendor channels — R1425, Table — «American Kratom Association | 62 (17.4) | 4 (10.5) | 66 (16.7) ... Online retailer or vendor that sells kratom | ... | 22 (5.6) ... Local kratom advocacy group…»
- regular_use_required: >=3 times weekly for >=4 weeks — R1425, Study Sample, Recruitment, and Screening — «Inclusion criteria were as follows: kratom use (≥3 times weekly for ≥4 weeks), age 18 years or older, US residency»
- product_form: commercial powder or capsules — Effective-ineffective dosing ranges; Typical dose amounts — «Most participants reported regularly using whole-leaf kratom products (95.9%); only 16 (4.1%) reported regular extract use.»
- response_rate: 34.3 — Results — «1152 candidates were sent enrollment invitations (to reach an IRB-approved enrollment ceiling of 400), and 395 completed the survey.»
- age_mean: 38.1 — Results — «Participants were aged 38.1 on average (SD = 11.2)»
- age_sd: 11.2 — Results — «Participants were aged 38.1 on average (SD = 11.2)»
- pct_male: 54.9 — Results — «Their sex/gender was 54.9% male (demographics in Table 1).»
- pct_other_opioid_use: NR — R1425, Table; Motivations for Use — «Currently in alcohol or drug recovery | 135 (37.8) | 10 (26.3) | 145 (36.7)»
- instruments: DSM-5 SUD criteria for kratom (11 criteria, self-report online survey; English); [withdrawal only, not an estimate: SOWS 16 items modified for kratom plus 7 extra items] — SUD for kratom; Kratom withdrawal — «SUD for kratom (KUD) was assessed using the 11 DSM-5 diagnostic criteria (American Psychiatric Association, 2013).»
- industry_funding: NR — Study recruitment and sample — «This study was approved by the National Institutes of Health Institutional Review Board.»
- funding_coi: Funding and COI statements not in the supplied text; NIH IRB approval and a 'NIDA research team' suggest NIDA intramural research, but funding is not stated. — Study recruitment and sample; R1425, Table — «This study was approved by the National Institutes of Health Institutional Review Board.»
- pub_status: journal — Header — «Year: 2024; venue: Drug and alcohol dependence; DOI: 10.1016/j.drugalcdep.2024.111329»
- language: English — Full text — «Kratom addiction per DSM-5 SUD criteria, and kratom physical dependence: Insights from dosing amount versus frequency»
- notes: Calculation: response 395/1152 = 34.3%. R1425 (EMA paper) covers the same 395 enrolled; 357 finished the EMA. Age, sex and n describe all 395 enrolled kratom users (all are users). Recruitment: mostly Reddit (36.7%) and Facebook (22.3%); the text does not say whether these were kratom-specific forums. About 26% came through the American Kratom Association, vendors, local advocacy groups or kratom stores, so the channel code needs a reviewer check. 36.7% were in alcohol or drug recovery; 28% of EMA completers used kratom as a long-term opioid substitute. Current non-prescribed opioid use or OU…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is US adult regular kratom consumers. The frame was self-selected volunteers who reached the study through social media, advocacy and vendor channels. — R1425, Table; R1402 Conclusions — «possible self-selection bias: they are confined to a sample primarily comprising consumers of whole-leaf-kratom products»
2. способ отбора: **no** — Online opt-in, self-selected sample; no probability sampling. — Conclusions — «limitations inherent to retrospective self-report and possible self-selection bias»
3. размер выборки: **yes** — n = 395 kratom users, which is at least 246. — Results — «395 completed the survey»
4. описание выборки и условий: **yes** — Age, sex, remote nationwide US setting and dates (July-Nov 2022) all reported. — Results; Study recruitment and sample — «Participants were aged 38.1 on average (SD = 11.2)... Their sex/gender was 54.9% male»
5. охват (пропуски): **unclear** — Missing KUD item data not reported; percentages given without a stated denominator. — KUD descriptive results — «Lifetime KUD criteria (2+ lifetime symptoms) were met by 63.5%»
6. валидность определения случая: **yes** — All 11 DSM-5 SUD criteria for kratom assessed item by item (self-report). — SUD for kratom — «SUD for kratom (KUD) was assessed using the 11 DSM-5 diagnostic criteria»
7. единое надёжное измерение: **yes** — Same online baseline survey, criteria and thresholds for all participants. — Study recruitment and sample; SUD for kratom — «we enrolled US adults who use kratom regularly into a nationwide ecological momentary assessment (EMA) study (Smith et al., 2024), that included a baseline sur…»
8. статистика (числитель и знаменатель): **yes** — Percentages only, but they can be traced to the 395 survey completers, so counts and CIs can be calculated. Note the denominator is implied, not stated. — KUD descriptive results — «Past-year KUD (2+ past-year symptoms) was met by 46.6%, with 27.3% being mild, 12.7% moderate, and 6.6% severe.»
9. отклик: **no** — 395 of 1152 invited completed (34.3%). Responders were not compared with non-responders and no weights were used. — Results — «1152 candidates were sent enrollment invitations (to reach an IRB-approved enrollment ceiling of 400), and 395 completed the survey.»

Правки:
- 

Проверено: да

---

## ST07 · Kunová 2022 · Digital Repository (National Repository of Grey Literature)

Основной отчёт R2039: [текст](../../fulltext/text/R2039.txt) — «Patterns of kratom use among regular users: qualitative analysis»
Расхождения в тексте: 1) LDQ classification: section 2.5.1 (p. 27) prints the bands <10 low, 10-22 medium and >22 high. Table 3 (p. 28) gives R2 = 10 and R5 = 10, which falls in the medium band. Yet the text below the table puts R2 and R5 in the low group and names only R1, R3, R4 and R7 as medium (4/10). Following the rule to use the table, the estimates apply the printed bands to the Table 3 scores: 6/10 medium and 4/10 low. The author's own figure of 4/10 is given in the estimate notes. 2) Frequency of R5: section 3.2.1 (p. 35) says R2 and R5 use 'at least 2-4 times a week' (R5 twice daily). But p. 36 lists R5 among 'daily users' consuming 2-3 g/day, and Table 4 gives R5 3 g/day. The daily/non-daily subgroups follow the 3.2.1 grouping. 3) The LDQ form in Příloha 3 is generic ('drink or psychoactive substances', 'please specify'), and its past-week frame is stated only there. The text does not say explicit…
Заметка ИИ: Grey-literature master's thesis (Czech), qualitative design, n=10. The page numbers are the printed thesis pages; the text has no '=== Page ===' markers. The LDQ bands are not validated in kratom users, and it is unclear whether the LDQ was anchored to kratom. All subgroup estimates were derived from individual-level Tables 2-4.

### ST07-1 · Czechia, regular (≥weekly) kratom users aged 15-34, snowball sample, qualitative interviews with LDQ, thesis 2022, n=10
Отчёты: R2039 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | LDQ · LDQ <10 (low) of 0-30 | **below** | **4 / 10** | 40.0 | Tabulka 3, p. 28; 2.5.1, p. 27 | «< 10 = nízká závislost ... R6 1 ... R8 7 R9 6 R10 6» |
| E2 | all | LDQ · LDQ 10-22 (medium) of 0-30 | **L2-scale** | **6 / 10** | 60.0 | Tabulka 3, p. 28; 2.5.1, p. 27 | «10 – 22 = střední závislost ... R1 11 R2 10 R3 11 R4 18 R5 10 ... R7 16» |
| E3 | all | LDQ · LDQ >22 (high) of 0-30 | **not_levelled** | **0 / 10** | 0.0 | Tabulka 3, p. 28; 2.5.1, p. 27 | «> 22 = vysoká závislost ... R4 18 (highest score)» |
| E4 | male | LDQ · LDQ 10-22 (medium) of 0-30 | **L2-scale** | **3 / 5** | 60.0 | Tabulka 2, p. 24; Tabulka 3, p. 28 | «R2 M ... R3 M ... R6 M ... R7 M ... R8 M; LDQ R2 10 R3 11 R6 1 R7 16 R8 7» |
| E5 | female | LDQ · LDQ 10-22 (medium) of 0-30 | **L2-scale** | **3 / 5** | 60.0 | Tabulka 2, p. 24; Tabulka 3, p. 28 | «R1 Ž ... R4 Ž ... R5 Ž ... R9 Ž ... R10 Ž; LDQ R1 11 R4 18 R5 10 R9 6 R10 6» |
| E6 | daily users | LDQ · LDQ 10-22 (medium) of 0-30 | **L2-scale** | **4 / 8** | 50.0 | 3.2.1, p. 35; Tabulka 3, p. 28 | «Skupina č. 1 užívá kratom jednou denně, pravidelně, alespoň 5 dní v týdnu (R6, R9, R10). Skupina č. 2 užívá dvakrát až čtyřikrát denně, alespoň 5 dní v týdnu (R1, R3, R4, R7, R8).» |
| E7 | non-daily users | LDQ · LDQ 10-22 (medium) of 0-30 | **L2-scale** | **2 / 2** | 100.0 | 3.2.1, p. 35; Tabulka 3, p. 28 | «Dva respondenti (R2, R5) užívají minimálně dvakrát až čtyřikrát týdně ... R2 10 ... R5 10» |

- E1: cumulative: no; источник порога: standard; правило: LDQ row; low band below the medium band = below; у авторов: «nízká závislost [low dependence]»; главная у авторов: no; период: past week; **расчёт: Count of Table 3 scores <10: R6 1, R8 7, R9 6, R10 6 = 4**; заметка: Author's text counts 6 respondents (R2, R5, R6, R8, R9, R10) as 'low or almost no dependence'. But R2 and R5 score 10, which falls in the printed medium band. The table is used here.
- E2: cumulative: no; источник порога: standard; правило: LDQ row; medium band and above = L2-scale; у авторов: «střední závislost [medium dependence]»; главная у авторов: yes; период: past week; **расчёт: Count of Table 3 scores 10-22: R1 11, R2 10, R3 11, R4 18, R5 10, R7 16 = 6**; заметка: Author's text: 'u respondentů (R1, R3, R4, R7) ... se jedná už o střední závislost' = 4/10. That leaves out R2 and R5 (score 10). Bands are attributed to LDQ sources, not validated in kratom users. Unclear whether the LDQ was anchored to kratom.
- E3: cumulative: yes; источник порога: standard; правило: LDQ row; high band alone = not levelled; у авторов: «vysoká závislost [high dependence]»; главная у авторов: no; период: past week; **расчёт: No Table 3 score >22 (maximum 18)**; заметка: Zero cases.
- E4: cumulative: no; источник порога: standard; правило: LDQ row; medium band = L2-scale; у авторов: «střední závislost [medium dependence]»; главная у авторов: no; период: past week; **расчёт: Males per Table 2: R2, R3, R6, R7, R8; Table 3 scores 10, 11, 1, 16, 7 -> 3 in 10-22**; заметка: Not reported by the author; derived from individual data. By the author's text classification it would be 2/5.
- E5: cumulative: no; источник порога: standard; правило: LDQ row; medium band = L2-scale; у авторов: «střední závislost [medium dependence]»; главная у авторов: no; период: past week; **расчёт: Females per Table 2: R1, R4, R5, R9, R10; scores 11, 18, 10, 6, 6 -> 3 in 10-22**; заметка: Not reported by the author; derived. By the author's text classification it would be 2/5.
- E6: cumulative: no; источник порога: standard; правило: LDQ row; medium band = L2-scale; у авторов: «střední závislost [medium dependence]»; главная у авторов: no; период: past week; **расчёт: Daily (≥5 days/week) = groups 1 (R6, R9, R10) + 2 (R1, R3, R4, R7, R8); scores 1, 6, 6, 11, 11, 18, 16, 7 -> 4 in 10-22**; заметка: Derived. Author's groups: group 1 (once daily) 0/3; group 2 (2-4 times daily) 4/5.
- E7: cumulative: no; источник порога: standard; правило: LDQ row; medium band = L2-scale; у авторов: «střední závislost [medium dependence]»; главная у авторов: no; период: past week; **расчёт: Non-daily (2-4 times/week): R2 and R5; scores 10 and 10 -> 2 in 10-22**; заметка: Derived. Both scores sit exactly at the band's lower limit, and the author's text classifies both as low (0/2). Table 4 lists R5 as 3 g/day, so R5's frequency is inconsistent.

**Ключевые поля выборки:**
- **n_users: 10** — 2.3, p. 23; Tabulka 3, p. 28 — «Výzkumu se zúčastnilo 10 respondentů, z toho 5 žen a 5 mužů. [10 respondents took part, 5 women and 5 men.]»
- **sample_type: community_users** — 2.4, p. 25 — «nulté fázi, kterou jsem do výzkumu nominovala pomocí sdílením plakátu s informacemi ohledně výzkumu na sociálních sítí... První vlnou generace tak byly kontakty z řad mých přátel. [zero phase recruited by sharing a poster on social networks... the first wave …»
- **sampling: snowball** — 2.4, p. 25 — «Pro získání respondentů byla vybrána metoda sněhové koule neboli snowball sampling. [The snowball sampling method was chosen to recruit respondents.]»
- **use_period: current** — 2.3, p. 25 — «Kritériem pro zapojení do výzkumu je užívání kratomu minimálně jednou týdně. [The inclusion criterion is kratom use at least once a week.]»
- **region: Europe** — Abstract (English) — «Kratom is becoming a more famous psychoactive substance in the Czech Republic.»

**Остальные поля:**
- country: CZE — Abstract (English) — «Kratom is becoming a more famous psychoactive substance in the Czech Republic.»
- data_years: NR — Prohlášení (p. before abstract); 2.5 — «V Praze, 15.7. 2022 [Prague, 15 July 2022] (date of thesis declaration; interview dates not reported)»
- design: cross-sectional — Abstract; 2.5, p. 26 — «S respondenty bylo následně realizováno polostrukturované interview. [Semi-structured interviews were then conducted with the respondents.]»
- recruitment_channel: general — 2.4, p. 25 — «bude osloveno vícero prvotních respondentů z řad mých známých a z členů internetových skupin nebo sociálních sítích [several initial respondents will be approa…»
- regular_use_required: current use at least once a week — 2.3, Kritéria pro zapojení, p. 25 — «• Věková hranice 15 – 34 let (tzv. mladí dospělí),) • užívání kratomu minimálně jednou týdně [age 15-34; kratom use at least once a week]»
- product_form: commercial powder or capsules — 4 Shrnutí výsledků, p. 51; 3.2.4, p. 39 — «Všichni respondenti konzumují kratom v podobě rozemletého prášku v nápoji. [All respondents consume kratom as ground powder in a drink.]»
- response_rate: NR — 2.4, p. 25 — «Pro získání respondentů byla vybrána metoda sněhové koule [snowball method chosen; number approached not reported]»
- age_mean: 27.2 — 2.3, p. 23 — «Průměrný věk respondentů byl 27,2 let. [The mean age of respondents was 27.2 years.]»
- age_sd: 2.8 — Tabulka 2, p. 24 (computed) — «R1 Ž 25; R2 M 25; R3 M 26; R4 Ž 29; R5 Ž 31; R6 M 28; R7 M 27; R8 M 22; R9 Ž 31; R10 Ž 28»
- pct_male: 50 — 2.3, p. 23 — «Výzkumu se zúčastnilo 10 respondentů, z toho 5 žen a 5 mužů.»
- pct_other_opioid_use: NR — 2.3, p. 24 — «V posledních 12 měsících respondenti reportují užití marihuany, MDMA, kokainu, psilocybinu, poppers, GHB a ketaminu. [In the past 12 months respondents report …»
- instruments: LDQ (Leeds Dependence Questionnaire, 10 items scored 0-3, range 0-30; Czech translation in Příloha 3; reference period past week; substance to be specified by respondent) — 2.5.1, p. 27; Příloha č. 3, p. 66 — «Jedná se o 10 – položkový, sebe posuzující dotazník... maximální možné dosažení bodů je 30. [a 10-item self-rated questionnaire... maximum score 30]»
- industry_funding: NR — Whole text — «Děkuji Mgr. Jaroslavu Vackovi, Ph.D. za odbornou pomoc při vedení této práce. [Acknowledgement of supervisor only; no funding statement]»
- funding_coi: No funding or conflict-of-interest statement; Master's thesis (Charles University), supervisor J. Vacek — Poděkování; Identifikační záznam — «Vedoucí práce Vacek, Jaroslav. [Supervisor Vacek, Jaroslav.]»
- pub_status: thesis — Title page; Identifikační záznam — «Diplomová práce (Mgr.). Univerzita Karlova v Praze, 1. lékařská fakulta, Klinika adiktologie. [Master's thesis, Charles University, First Faculty of Medicine, …»
- language: Czech (English abstract) — Whole text — «Vzorce užívání kratomu u pravidelných uživatelů: kvalitativní analýza [Patterns of kratom use among regular users: qualitative analysis]»
- notes: Qualitative master's thesis; LDQ administered within online interviews (Google Meet). Age and sex describe all 10 respondents (all are kratom users). age_sd computed from Table 2 ages (sample SD = sqrt(71.6/9) = 2.82); not reported by author. Interview dates not reported (thesis dated July 2022; respondents mention covid). The Czech LDQ form (Příloha 3) refers to 'drink or psychoactive substances' and asks the respondent to specify the substance; the text does not state explicitly that kratom was specified, though results are presented as kratom dependence. All respondents drink alcohol regul…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is regular kratom users (young adults) in Czechia; frame is author's friends and social media contacts. — 2.4, p. 25 — «První vlnou generace tak byly kontakty z řad mých přátel. [The first wave were contacts among my friends.]»
2. способ отбора: **no** — Snowball sampling. — 2.4, p. 25 — «Pro získání respondentů byla vybrána metoda sněhové koule neboli snowball sampling.»
3. размер выборки: **no** — n = 10 kratom users, below 246. — 2.3, p. 23 — «Výzkumu se zúčastnilo 10 respondentů, z toho 5 žen a 5 mužů.»
4. описание выборки и условий: **unclear** — Age, sex, setting and country reported; dates of data collection not reported. — 2.3, p. 23-24; 2.5, p. 26 — «Rozhovory probíhaly online pomocí platformy Google Meets s časovou dotací 30 – 40 minut [Interviews ran online via Google Meet, 30-40 minutes]»
5. охват (пропуски): **yes** — LDQ score printed for all 10 respondents. — Tabulka 3, p. 28 — «Tabulka 3: Výsledky dotazníku The Leeds Dependence Questionnaire ... R1 11 ... R10 6»
6. валидность определения случая: **no** — LDQ bands not validated in kratom users; also unclear whether the form was anchored to kratom. — 2.5.1, p. 27; Příloha č. 3, p. 66 — «< 10 = nízká závislost, 10 – 22 = střední závislost, > 22 = vysoká závislost. ... zamyslete se nad hlavními skupinami látek, prosím specifikujte [think of main…»
7. единое надёжное измерение: **yes** — Same LDQ, same past-week frame, filled within the online interview for all respondents. — 2.5, p. 26-27 — «V neposlední řadě respondenti vyplnili „The Leeds Dependence Questionnaire“ [Finally, respondents completed the LDQ]»
8. статистика (числитель и знаменатель): **yes** — Individual scores and n printed so numerator/denominator traceable, but the author's text classification conflicts with the printed bands (see consistency notes). — Tabulka 3, p. 28 — «R1 11 R2 10 R3 11 R4 18 R5 10 R6 1 R7 16 R8 7 R9 6 R10 6»
9. отклик: **unclear** — Snowball recruitment; number approached or refusing not reported. — 2.7, p. 30 — «Respondenti se například nebudou chtít zúčastnit výzkumu [respondents may not want to take part] (no numbers given)»

Правки:
- 

Проверено: да

---

## ST08 · Saengmolee 2022 · Prince of Songkla University

Основной отчёт R2129: [текст](../../fulltext/text/R2129.txt) — «Characterization of Physiological Biomarkers in Long-Term Kratom (Mitragyna speciosa Korth.) Users: A Preliminary Study»
Не выписано ИИ: Controls who do not use kratom (n=24 analysed of 36 recruited) are not extracted. The HRV subsample (19 LKU), path-analysis subsample (n=24) and dose subgroups (LTH n=14 vs VH n=14) are not extracted as separate samples. Dose subgroups have only mean KDS scores, shown in Fig 3.8B, and no band counts.
Расхождения в тексте: 1) Table 3.2 prints the KDS bands as 0-13 and 13-34, so they overlap. Coded as 14-34 per the levels table. 2) The SD of the dependence score is printed as "25.07 ± 96", which is implausible on a 0-48 scale; probably a typo. 3) Table 3.1 gives LKU ≤50 y n=9 and >50 y n=19, and controls ≤50 n=12 and >50 n=12. The note under Fig 3.4 gives ≤50: control n=9 and LKU n=12, which contradicts the table. The control total mean age (56.64) also does not fit the controls' subgroup means (40.08, 64.75). The IEEE appendix (Fig 5) gives ≤50 LKU n=9, controls n=12, which agrees with Table 3.1. 4) The text says the KDS is based on "DSM-VI" (sic, DSM-IV). 5) Path analysis: a negative coefficient (β = -13.373) is described as "contributing to increasing in Kratom dependence score". 6) The 74 participants are described as a "total sample" in the thesis and as "volunteers" in the appendix article. 7) Percen…
Заметка ИИ: I set primary_for_authors to "no" for all three bands because the authors never present a dependence prevalence; please check. The thesis has no "=== Page N ===" markers, so locations use the printed page numbers. Sampling is coded convenience because the appendix article calls participants "volunteers"; the thesis itself does not describe the recruitment method. The time frame of the KDS is not stated. Withdrawal was not measured with a scale.

### ST08-1 · Long-term kratom leaf chewers, Surat Thani & Songkhla, Thailand (EEG study), n=28
Отчёты: R2129 (main; PhD thesis, includes Appendix A = IEEE Sensors J 2022 article on the same sample)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | KDS · KDS 0-13 (low) of 0-48 | **below** | **4 / 28** | 14.3 | p. 65, Table 3.2 | «Dependent score ... Low (0-13) n(%) 4 (14.28)» |
| E2 | all | KDS · KDS 14-34 (moderate) of 0-48 (printed 13-34) | **L2-scale** | **20 / 28** | 71.4 | p. 65, Table 3.2 | «Moderate (13-34) n(%) 20 (71.44)» |
| E3 | all | KDS · KDS 35-48 (high) of 0-48 | **L2-scale** | **4 / 28** | 14.3 | p. 65, Table 3.2 | «Hight (35-48) n(%) 4 (14.28)» |

- E1: cumulative: no; источник порога: validation paper; правило: KDS row; 0-13 band = below; у авторов: «Low»; главная у авторов: no; период: NR; заметка: The authors do not present any band as a prevalence estimate. KDS was used as a continuous outcome.
- E2: cumulative: no; источник порога: validation paper; правило: KDS row; moderate band (printed 13-34, read as 14-34) = L2-scale; у авторов: «Moderate»; главная у авторов: no; период: NR; заметка: Printed band 13-34 overlaps the low band 0-13. Read as 14-34 per the levels table.
- E3: cumulative: no; источник порога: validation paper; правило: KDS row; 35-48 band = L2-scale (not L3); у авторов: «Hight [High]»; главная у авторов: no; период: NR; заметка: Mean KDS printed as 25.07 ± 96.

**Ключевые поля выборки:**
- **n_users: 28** — p. 65, Table 3.2; p. 64, Table 3.1 — «LKU (n= 28)»
- **sample_type: community_users** — p. 45, 2.2 Subjects; p. 64, Table 3.1 — «38 long-term Kratom users (LKU) collected from Ban Nasarn district, Surat Thani province, and Natavee district, Songkhla province»
- **sampling: convenience** — Appendix A (IEEE Sens J 2022), p. 6089, II.A Participants — «A total of 74 volunteers: 36 normal male participants and male 38 LKU were collected from Ban Nasarn district, Surat Thani province, and Natavee district, Songkhla province»
- **use_period: current** — Appendix A (IEEE Sens J 2022), p. 6089, Fig. 1 note — «we included LKU those who consumed Kratom ≥ two years due to Kratom-related unpleasant side effects [26] and who last consumed Kratom at least 2-hours before experimenting»
- **region: Southeast Asia** — p. 45, 2.2 Subjects — «Ban Nasarn district, Surat Thani province, and Natavee district, Songkhla province»

**Остальные поля:**
- country: THA — p. 45, 2.2 Subjects — «collected from Ban Nasarn district, Surat Thani province, and Natavee district, Songkhla province»
- data_years: NR — NA — «NR»
- design: laboratory or EMA study — p. 46, 2.3 Procedure — «the physiological signals from EEG and ECG were recorded for 3 minutes at rest with an eyes-closed condition. After physiological recording, the subjects were …»
- recruitment_channel: NR — p. 45, 2.2 Subjects — «To match the background factors of LKU, the LKU were recruited at first followed by the controls.»
- regular_use_required: long-term use: kratom consumption ≥ 2 years — Appendix A (IEEE Sens J 2022), p. 6089, Fig. 1 note — «we included LKU those who consumed Kratom ≥ two years»
- product_form: traditional leaf — Abstract, p. vi — «long-term kratom users (LKU) who chewed kratom leaves; n = 28»
- response_rate: NR — NA — «NR»
- age_mean: 52.41 — p. 64, Table 3.1 — «Total (mean ± SD) ... 52.41 ± 15.45 (n=28)»
- age_sd: 15.45 — p. 64, Table 3.1 — «52.41 ± 15.45 (n=28)»
- pct_male: 100 — p. 45, 2.2 Subjects — «Finally, 52 male subjects (24 controls and 28 LKU for EEG evaluation»
- pct_other_opioid_use: NR — NA — «NR»
- instruments: Krathom/Kratom Dependence Scale (KDS), 16 items, Saingam et al. 2014; language version not stated (Thai setting) — p. 53, 2.8 Neurobehavioral testing — «The LKU group was instructed to rate their Kratom dependence with 16-items of KDS scales ... (Saingam et al., 2014).»
- industry_funding: no — p. vii, Acknowledgement — «The financial supported by grants from Graduate School Dissertation Funding for Thesis and Revenue Budget Fund, and Educational Institutions Scholarship for Ou…»
- funding_coi: University funding (Prince of Songkla University graduate school grants and scholarship); COI statement NR — p. vii, Acknowledgement — «Graduate School Dissertation Funding for Thesis and Revenue Budget Fund, and Educational Institutions Scholarship for Outstanding GPA, Prince of Songkla Univer…»
- pub_status: thesis — Title page — «A Thesis Submitted in Partial Fulfillment of the Requirements for the Degree of Doctor of Philosophy in Physiology Prince of Songkla University 2022»
- language: English (abstract also in Thai) — p. vi — «ABSTRACT A neurophysiological outcome associated with long-term kratom chewing in traditional use context is still unknown.»
- notes: All participants are male; age and sex values describe the 28 LKU. 38 LKU were recruited and 28 met inclusion criteria for EEG; the HRV subsample had 19 LKU and path analysis 24. Women were not recruited because they hesitated to take part (appendix p. 6089). Appendix A (IEEE Sens J 2022) reports the same sample; it is the same study, not a separate one. Inclusion criteria (use ≥2 y, last use ≥2 h before testing) come from the appendix article; the thesis Figure 2.1 is not in the text. Data years are NR; the ethics code HSc-HREC-63 may point to 2020 but the text never states the dates. 85.7% …

**Риск смещения (JBI):**
1. рамка выборки: **unclear** — No sampling frame described; users from two districts were recruited, with no register or list mentioned. — p. 45, 2.2 Subjects — «Seventy-four male subjects were a total sample (36 controls and 38 long-term Kratom users (LKU) collected from Ban Nasarn district, Surat Thani province, and N…»
2. способ отбора: **no** — Volunteer (non-probability) recruitment; males only, because women declined to take part. — Appendix A (IEEE Sens J 2022), p. 6089, II.A — «A total of 74 volunteers: 36 normal male participants and male 38 LKU were collected»
3. размер выборки: **no** — 28 kratom users is below 246. — p. 65, Table 3.2 — «Low (0-13) n(%) ... 4 (14.28) ... Moderate (13-34) n(%) 20 (71.44) ... Hight (35-48) n(%) 4 (14.28)»
4. описание выборки и условий: **unclear** — Age, sex, setting and country are reported; dates of data collection are not. — p. 64, Table 3.1; p. 45 — «52.41 ± 15.45 (n=28) ... Farmers n(%) 24 (85.71)»
5. охват (пропуски): **yes** — KDS bands cover all 28 analysed users (4+20+4=28); the 10 excluded users failed inclusion criteria, which is not missing outcome data. — p. 65, Table 3.2 — «4 (14.28) 20 (71.44) 4 (14.28)»
6. валидность определения случая: **yes** — KDS bands come from the scale's validation in Thai kratom users (Saingam 2014). The bands are printed with overlapping bounds (0-13 / 13-34). — p. 53 — «The KDS provided the levels of Kratom dependence into 3 levels: low (KDS score: 0-13), moderate (KDS score: 13-34), and high (KDS score: 35-48) levels.»
7. единое надёжное измерение: **yes** — Every user self-rated the same 16-item KDS after the physiological recording. — p. 46, 2.3; p. 53 — «The LKU group was instructed to rate their Kratom dependence with 16-items of KDS scales»
8. статистика (числитель и знаменатель): **yes** — Counts and the denominator (n=28) are printed, so a CI can be calculated. — p. 65, Table 3.2 — «Moderate (13-34) n(%) 20 (71.44)»
9. отклик: **unclear** — No response rate or count of invited people is reported. — p. 45 — «The inclusion and exclusion criteria are shown (Figure 2.1).»

Правки:
- 

Проверено: да

---

## ST09 · Smith 2022 · Journal of addiction medicine

Основной отчёт R2149: [текст](../../fulltext/text/R2149.txt) — «Assessment of Kratom Use Disorder and Withdrawal Among an Online Convenience Sample of US Adults.» — [DOI](https://doi.org/10.1097/adm.0000000000000986)
Приложен R2153: [текст](../../fulltext/text/R2153.txt) · [PDF](../../fulltext/pdf/R2153.pdf) — «Searching for a Signal: Self-Reported Kratom Dose-Effect Relationships Among a Sample of US Adults With Regular Kratom …»
Связь отчётов: Same US mTurk re-contact survey of adults with lifetime kratom use (April-May 2021, n = 129 evaluable): R2149 (KUD and withdrawal) and R2153 (dose-effect paper)
Не выписано ИИ: Parent mTurk survey (n=2,615; Sep 2020-Mar 2021): not a kratom-user sample, and no KUD measure is reported for the 289 eligible lifetime users. Regular-use subgroup (n=104): has withdrawal checklist data only, with no KUD breakdown.
Расхождения в тексте: 1) Lifetime KUD in R2149 Table 1 does not hold together. 'None' is 69.0% (implying 31.0% any lifetime KUD, which matches R2153's 40/129), but the group columns show only 68 (52.7%) never KUD, so 61/129 (47.3%) were current or remitted. The lifetime bands (69.0 + 21.7 + 0.5 + 0.5 = 91.7%) do not sum to 100. A value of 0.5% is not possible with n=129, and the lifetime moderate/severe shares are below the past-year shares. Treat the lifetime estimates with caution. 2) Past-year bands: 14.0/7.0/8.5% of 129 = 18/9/11, which sum to 38 = current KUD group; this part is consistent. 3) Severe band: table prints ≥6, text prints '>6 symptoms'. 4) White: 69.0% in text, 79.1% in R2149 Table 1, and R2153 gives 102 at 71.9% (102/129 is actually 79.1%). 5) Response: R2149 gives 129/289 (44.6%); R2153 gives 134/283 (47.4%) complete, then 5 removed. 6) Item endorsement: the Abstract says 9.3% reported re…
Заметка ИИ: Primary estimate is current (past-year) DSM-5 KUD, 38/129 (29.5%). Its severity counts were derived from the percentages. Female, male and past-30-day-user estimates were derived from the Table 1 column percentages. The lifetime severity figures were extracted as printed but are internally inconsistent.

### ST09-1 · US mTurk re-contact survey of adults with lifetime kratom use, April-May 2021, n=129
Отчёты: R2149 (main); R2153

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | DSM-5-SUD · DSM-5 criteria>=2 (current past-year KUD) | **L1** | **38 / 129** | 29.5 | R2149, Table 1 header; Abstract | «Current KUD (N=38) 29.5% ... Full Sample (N=129); 29.5% met current (past-year) KUD threshold.» |
| E2 | all | DSM-5-SUD · DSM-5 criteria 0-1 (none) | **below** | **91 / 129** | 70.5 | R2149, Table 1 (current severity) | «Severity criteria met for current (past year) Kratom Use Disorder ... None (<2 symptoms) / 70.5» |
| E3 | all | DSM-5-SUD · DSM-5 criteria 2-3 (mild) | **L1** | **18 / 129** | 14.0 | R2149, Table 1 (current severity); Abstract | «For past-year KUD, severity was: 14.0% mild, 7.0% moderate, and 8.5% severe.» |
| E4 | all | DSM-5-SUD · DSM-5 criteria 4-5 (moderate) | **L2** | **9 / 129** | 7.0 | R2149, Table 1 (current severity) | «Moderate (4–5 symptoms) / 7.0» |
| E5 | all | DSM-5-SUD · DSM-5 criteria>=6 (severe) | **L3** | **11 / 129** | 8.5 | R2149, Table 1 (current severity) | «Severe (≥6 symptoms) / 8.5» |
| E6 | all | DSM-5-SUD · DSM-5 criteria 0-1 ever (never met KUD criteria) | **below** | **68 / 129** | 52.7 | R2149, Table 1 header; Abstract | «Never KUD (N=68) 52.7%; Over half (52.7%) of respondents never met KUD diagnostic criteria» |
| E7 | all | DSM-5-SUD · DSM-5 criteria>=2 ever, but none met in the past 12 months (remitted) | **L1** | **23 / 129** | 17.8 | R2149, Table 1 header; Results | «Remitted± KUD (N=23) 17.8%; 17.8% were assessed remitted (based on DSM-5 remission criterion of 12 months without meeting diagnostic threshold)» |
| E8 | all | DSM-5-SUD · DSM-5 criteria>=2 lifetime (lifetime KUD) | **L1** | **40 / 129** | 31.0 | R2153, Table 1 (p.7) | «Qualified for lifetime kratom use disorder 40 31.00» |
| E9 | all | DSM-5-SUD · DSM-5 criteria 0-1 (none), lifetime | **below** | **89 / 129** | 69.0 | R2149, Table 1 (lifetime severity) | «Severity criteria met for ever lifetime Kratom Use Disorder based on DSM-5 checklist. ... None (<2 symptoms) / 69.0» |
| E10 | all | DSM-5-SUD · DSM-5 criteria 2-3 (mild), lifetime | **L1** | **28 / 129** | 21.7 | R2149, Table 1 (lifetime severity) | «Mild (2–3 symptoms) / 21.7» |
| E11 | all | DSM-5-SUD · DSM-5 criteria 4-5 (moderate), lifetime | **L2** | **1 / 129** | 0.8 | R2149, Table 1 (lifetime severity) | «Moderate (4–5 symptoms) / 0.5» |
| E12 | all | DSM-5-SUD · DSM-5 criteria>=6 (severe), lifetime | **L3** | **1 / 129** | 0.8 | R2149, Table 1 (lifetime severity) | «Severe (≥6 symptoms) / 0.5» |
| E13 | female | DSM-5-SUD · DSM-5 criteria>=2 (current past-year KUD) | **L1** | **13 / 67** | 19.4 | R2149, Table 1 (Female row) | «Female / 34.2 / / 43.5 / / 64.7 / / 51.9 / / 0.007» |
| E14 | male | DSM-5-SUD · DSM-5 criteria>=2 (current past-year KUD) | **L1** | **25 / 62** | 40.3 | R2149, Table 1 (Female row) | «Female / 34.2 / / 43.5 / / 64.7 / / 51.9 / / 0.007» |
| E15 | past-30-day kratom users | DSM-5-SUD · DSM-5 criteria>=2 (current past-year KUD) | **L1** | **25 / 56** | 44.6 | R2149, Table 1 (Kratom past-30-day row) | «Kratom / 65.8 / 17.8 ± 12.5 / 17.4 / 6.1 ± 10.3 / 39.7 / 7.5 ± 10.9 / 43.4 / 11.1 ± 12.4 / < 0.001» |

- E1: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=2 criteria = L1; у авторов: «current (past-year) KUD»; главная у авторов: yes; период: past 12 months; заметка: The count is the size of the current KUD group.
- E2: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 0-1 = below; у авторов: «None (<2 symptoms)»; главная у авторов: no; период: past 12 months; **расчёт: 70.5% x 129 = 90.9 -> 91 (equals 129-38)**
- E3: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 2-3 = L1; у авторов: «Mild (2–3 symptoms)»; главная у авторов: no; период: past 12 months; **расчёт: 14.0% x 129 = 18.06 -> 18**; заметка: The mild, moderate and severe counts (18+9+11) sum to 38, the current KUD group. The percentages use the full sample (129), not the 38.
- E4: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 4-5 = L2; у авторов: «Moderate (4–5 symptoms)»; главная у авторов: no; период: past 12 months; **расчёт: 7.0% x 129 = 9.03 -> 9**
- E5: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=6 = L3; у авторов: «Severe (≥6 symptoms)»; главная у авторов: no; период: past 12 months; **расчёт: 8.5% x 129 = 10.97 -> 11**; заметка: The table prints ≥6; the Results text prints '>6 symptoms'.
- E6: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; never >=2 criteria = below; у авторов: «Never KUD»; главная у авторов: no; период: lifetime; заметка: Conflicts with lifetime 'None (<2 symptoms)' 69.0% in the same table; see consistency_notes.
- E7: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; lifetime >=2 criteria = L1 (not current); у авторов: «Remitted KUD»; главная у авторов: no; период: lifetime; заметка: Implied ever-KUD (current + remitted) is 61/129 (47.3%). This sum is not reported and was not built here.
- E8: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=2 criteria = L1; у авторов: «Qualified for lifetime kratom use disorder»; главная у авторов: no; период: lifetime; заметка: From the attached report R2153. Matches R2149 lifetime 'None' 69.0% (100-69.0=31.0), but conflicts with current+remitted 61/129.
- E9: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 0-1 = below; у авторов: «None (<2 symptoms)»; главная у авторов: no; период: lifetime; **расчёт: 69.0% x 129 = 89.01 -> 89**
- E10: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 2-3 = L1; у авторов: «Mild (2–3 symptoms)»; главная у авторов: no; период: lifetime; **расчёт: 21.7% x 129 = 27.99 -> 28**; заметка: The lifetime bands sum to 91.7%, so the lifetime severity data are internally inconsistent.
- E11: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 4-5 = L2; у авторов: «Moderate (4–5 symptoms)»; главная у авторов: no; период: lifetime; **расчёт: 0.5% x 129 = 0.645 -> 1**; заметка: No count out of 129 gives 0.5% (1/129 = 0.78%). The figure is probably an error, and it is lower than past-year moderate (7.0%), which is not logically possible.
- E12: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=6 = L3; у авторов: «Severe (≥6 symptoms)»; главная у авторов: no; период: lifetime; **расчёт: 0.5% x 129 = 0.645 -> 1**; заметка: Not possible with n=129, and lower than past-year severe (8.5%). Probably an error.
- E13: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=2 criteria = L1; у авторов: «current KUD»; главная у авторов: no; период: past 12 months; **расчёт: Cases: 34.2% female x 38 current KUD = 13.0 -> 13. n: female 34.2%x38 + 43.5%x23 + 64.7%x68 = 13+10+44 = 67 (R2153: 67 female)**; заметка: Derived from the column percentages.
- E14: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=2 criteria = L1; у авторов: «current KUD»; главная у авторов: no; период: past 12 months; **расчёт: Cases: 38 - 13 female = 25. n: 129 - 67 female = 62**; заметка: Male is assumed to be non-female; the authors report female only.
- E15: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=2 criteria = L1; у авторов: «current KUD»; главная у авторов: no; период: past 12 months; **расчёт: Cases: 65.8% x 38 = 25.0 -> 25. n: 43.4% x 129 = 56.0 -> 56 (= 25 + 17.4%x23=4 + 39.7%x68=27)**; заметка: The authors do not present this as a subgroup. It was derived from the past-30-day use row.

**⚠ Проверка скриптом (обратите внимание):**
- all: категории (E6+E7+E9+E10+E11+E12) дают 210, а n = 129

**Ключевые поля выборки:**
- **n_users: 129** — R2149, Table 1 — «Full Sample (N=129)»
- **sample_type: online_consumers** — R2149, Methods — «For our kratom survey we recontacted only respondents who reported ever using kratom on the larger parent survey to answer additional questions about their kratom use.»
- **sampling: online opt-in** — R2149, Methods; R2153, p.3 — «Amazon Mechanical Turk (mTurk), an online crowdsourcing platform ... was utilized for recruitment in both of our cross-sectional survey studies to obtain national convenience samples»
- **use_period: lifetime any** — R2149, Methods — «respondents who reported lifetime kratom use on a separate, larger online survey unrelated to kratom were successfully re-recruited»
- **region: North America** — R2149, Methods — «to obtain national convenience samples»

**Остальные поля:**
- country: USA — R2149, Methods — «was utilized for recruitment in both of our cross-sectional survey studies to obtain national convenience samples»
- data_years: 2021 — R2149, Methods — «Between April 15 through May 15, 2021 (N=129/289) respondents who reported lifetime kratom use on a separate, larger online survey unrelated to kratom were suc…»
- design: cross-sectional — R2149, Methods — «we re-recruited online respondents who reported lifetime kratom use on an unrelated survey into our cross-sectional kratom survey study»
- recruitment_channel: general — R2153, p.4, 2.2 — «This strategy resulted in a convenience sample of US adults with kratom use history who had not (initially) self-selected based on their kratom use.»
- regular_use_required: no — R2149, Methods — «we recontacted only respondents who reported ever using kratom on the larger parent survey»
- product_form: commercial powder or capsules — R2153, p.6 3.2 and Table 1; p.12 — «respondents most frequently reported consuming kratom via capsules (n = 47), grams (n = 37), spoonfuls (n = 25), tablespoons (n = 11), and then cups of tea (n …»
- response_rate: 44.6 — R2149, Abstract Results — «A total of 129/289 (44.6%) evaluable surveys were obtained.»
- age_mean: 34.8 — R2149, Table 1; Results — «The sample (N=129) was 34.8 years old on average, 51.9% female»
- age_sd: 8.4 — R2149, Table 1 — «Age (years) | 100.0 | 33.7 ± 6.9 | 100.0 | 33.5 ± 8.7 | 100.0 | 35.9 ± 9 | 100.0 | 34.8 ± 8.4»
- pct_male: 48.1 — R2149, Results; R2153 Table 1 — «The sample (N=129) was 34.8 years old on average, 51.9% female, and 69.0% White.»
- pct_other_opioid_use: NR — R2149, Table 1 — «Nonmedical prescription opioids | 15.8 | 3.9 ± 5.6 | 26.1 | 6 ± 8.8 | 13.2 | 3.1 ± 7 | 16.3 | 3.9 ± 6.8»
- instruments: DSM-5 SUD checklist adapted for kratom (self-report, English; 13 items covering 11 criteria; lifetime and past-year) — R2149, Methods; Table 1 — «we report preliminary findings pertaining to assessment of KUD using the DSM-5 SUD checklist adapted for kratom. Specifically, the DSM-5 SUD symptom list was m…»
- industry_funding: no — R2149, Funding; Footnotes — «Support was provided by the Intramural Research Program of the NIH NIDA for KES, JMR, DHE. Support was provided by NIDA T32DA07209 for JCS. ... Conflicts of In…»
- funding_coi: NIH NIDA Intramural Research Program; NIDA T32DA07209; no conflicts of interest declared — R2149, Funding; Footnotes — «Support was provided by the Intramural Research Program of the NIH NIDA ... Conflicts of Interest: None»
- pub_status: journal — R2149, header — «Published in final edited form as: J Addict Med. 2022 Nov-Dec;16(6):666–670.»
- language: English — R2149, full text — «Assessment of Kratom Use Disorder and Withdrawal Among an Online Convenience Sample of US Adults»
- notes: Age and sex are for all 129 respondents, who are all lifetime kratom users. pct_male = 100 - 51.9% female (R2153: 67/129 female). Parent study: mTurk survey Sep 2020-Mar 2021 (n=2,615 valid) of adults with past-6-month alcohol-only or opioid/stimulant use (kratom counted as an opioid for eligibility). Sample type could also be read as drug_users; respondents were not recruited through kratom channels. Opioid use in past 30 days, full sample: nonmedical Rx opioids 16.3%, nonmedical buprenorphine 3.1%, fentanyl 2.3%; the share using any of these is not reported, so pct_other_opioid_use = NR. 80…

**Риск смещения (JBI):**
1. рамка выборки: **no** — The frame is mTurk workers from one parent survey who reported lifetime kratom use. This is only part of US adults who use kratom. — R2149, Methods; R2153, 5 Limitations — «findings are not generalizable to all people with kratom use histories, including those who engage with other platforms.»
2. способ отбора: **no** — Online opt-in convenience sampling through mTurk. — R2149, Methods — «was utilized for recruitment in both of our cross-sectional survey studies to obtain national convenience samples»
3. размер выборки: **no** — n=129 kratom users, below 246. — R2149, Abstract — «A total of 129/289 (44.6%) evaluable surveys were obtained.»
4. описание выборки и условий: **yes** — Age, sex, setting (online mTurk), country (US) and dates are all reported. — R2149, Methods; Results — «The sample (N=129) was 34.8 years old on average, 51.9% female, and 69.0% White.»
5. охват (пропуски): **yes** — All 129 evaluable respondents are classified into the current, remitted or never KUD groups (38+23+68=129). — R2149, Table 1 — «Current KUD (N=38) 29.5% | Remitted± KUD (N=23) 17.8% | Never KUD (N=68) 52.7% | Full Sample (N=129)»
6. валидность определения случая: **yes** — The primary estimate (past-year KUD, ≥2 criteria) comes from the DSM-5 SUD criteria, adapted for kratom and assessed item by item. — R2149, Methods — «the DSM-5 SUD symptom list was modified by inserting “kratom” as the drug specifier»
7. единое надёжное измерение: **yes** — Everyone completed the same online self-report checklist with the same thresholds. — R2149, Methods; Table 1 — «Severity criteria met for current (past year) Kratom Use Disorder diagnostic criteria based on DSM-5 checklist»
8. статистика (числитель и знаменатель): **yes** — The primary numerator and denominator (38/129) are clear, so a CI can be calculated. The lifetime severity percentages, however, cannot be traced to counts. — R2149, Table 1 — «Current KUD (N=38) 29.5%»
9. отклик: **yes** — Response was 44.6%, but the authors compared eligible people with completers and found no differences. That comparison is in a supplement that was not received, and it is eligible-vs-completers rather than responders vs… — R2149, Discussion — «As shown in Table 1 of supplementary materials, no statistically significant differences on demographic, pain, and psychiatric factors were found between perso…»

Правки:
- 

Проверено: да

---

## ST10 · Garcia-Romeu 2020 · Drug and alcohol dependence

Основной отчёт R2648: [текст](../../fulltext/text/R2648.txt) — «Kratom (Mitragyna speciosa): User demographics, use patterns, and implications for the opioid epidemic.» — [DOI](https://doi.org/10.1016/j.drugalcdep.2020.107849)
Расхождения в тексте: Abstract: 56 (2%) had past-year moderate or severe kratom SUD. Results: 'Less than 3% met diagnostic criteria for moderate and severe'. These agree loosely (56/2798 = 2.0%). The 2% in the abstract is the more exact figure and is used. 'None' (87.7%) is a percentage only; Table 2, which probably gives the mild, moderate and severe counts and the comparison by motive, is missing from the supplied text. Unrelated discrepancy: the abstract gives 17 (0.6%) seeking treatment for adverse effects, and the Results give 1.9% (n=17) of those reporting adverse effects. These use different denominators, so they do not conflict.
Заметка ИИ: Draft extraction from the text supplied (no tables). A reviewer should check Table 2 of the published article for the mild, moderate and severe DSM-5 counts and for subgroup (opioid-reduction vs other) SUD figures. The mean 'troubled by kratom use' rating was 3.2 (SD 9.8) on a 0-100 VAS; this is not an estimate. 3% of respondents lived outside the US.

### ST10-1 · Johns Hopkins online survey of past-year kratom users, mainly USA, 2017 (n=2,798)
Отчёты: R2648 (main)

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | DSM-5-SUD · DSM-5 criteria>=4 (moderate or severe) of 0-11 | **L2** | **56 / 2798** | 2.0 | Abstract, Results | «Fifty-six individuals (2%) met DSM-5 criteria for a past-year moderate or severe kratom-related substance use disorder (SUD).» |
| E2 | all | DSM-5-SUD · DSM-5 criteria 0-1 (none) of 0-11 | **below** | **2454 / 2798** | 87.7 | Results, Symptoms of withdrawal following kratom abstinence | «Most respondents (87.7%) did not meet diagnostic criteria for a past-year kratom-related substance use disorder (SUD) based on the DSM-5 symptom checklist.» |

- E1: cumulative: yes; источник порога: standard; правило: DSM-5-SUD row; >=4 criteria = L2; у авторов: «past-year moderate or severe kratom-related substance use disorder (SUD)»; главная у авторов: yes; период: past 12 months; заметка: The Results section says only 'Less than 3% met diagnostic criteria for moderate and severe kratom-related SUD'. Separate moderate and severe counts are presumably in Table 2, which was not in the supplied text.
- E2: cumulative: no; источник порога: standard; правило: DSM-5-SUD row; 0-1 criteria = below; у авторов: «did not meet diagnostic criteria for a past-year kratom-related SUD»; главная у авторов: no; период: past 12 months; **расчёт: 87.7% x 2798 / 100 = 2453.8 -> 2454**; заметка: Only a percentage is given in the text. The 'any SUD' share (~12.3%) and the mild band were not printed in the supplied text and were not calculated here.

**⚠ Проверка скриптом (обратите внимание):**
- all: категории (E2+E1) дают 2510, а n = 2798

**Ключевые поля выборки:**
- **n_users: 2798** — Results, Sample characteristics — «Of these, 28 were removed due to inconsistent responses or technical issues, resulting in a final sample of 2,798 kratom users.»
- **sample_type: online_consumers** — Methods, Data collection — «participants were recruited using online advertisements and email announcements distributed via sites of interest to kratom users (e.g., American Kratom Association, Erowid, Reddit)»
- **sampling: online opt-in** — Discussion — «The major limitation of this and other internet-based surveys of kratom users is the self-selected convenience sample queried.»
- **use_period: past 12 months** — Methods, Data collection — «Participants were required to be age 18 years or older, English language proficient, and have used kratom in the past year.»
- **region: North America** — Abstract — «located in the US (97%)»

**Остальные поля:**
- country: USA — Abstract, Results — «predominantly White (90%), female (61%), and located in the US (97%)»
- data_years: 2017 — Methods, Data collection — «Between January 2017 and December 2017 participants were recruited using online advertisements and email announcements»
- design: cross-sectional — Methods, Data collection — «We conducted this cross-sectional, anonymous online survey»
- recruitment_channel: advocacy or vendor channels — Results, Sample characteristics — «Fifty-three percent of the final sample learned about the survey through the American Kratom Association and 44.2% found it through Facebook or other social me…»
- regular_use_required: no — Methods, Data collection — «have used kratom in the past year»
- product_form: mixed — Results, Reasons for kratom use and use patterns — «Ingesting kratom orally in powder form was the most common method of administration (43.6%) followed by drinking as a prepared beverage (e.g., tea, smoothie; 3…»
- response_rate: NR — Results, Sample characteristics — «Of the 4,302 individuals who began the survey, 2,826 (66%) met all study inclusion criteria and completed the entire survey.»
- age_mean: 40.2 — Results, Sample characteristics — «Respondents were on average 40.2 years old (SD=11.8)»
- age_sd: 11.8 — Results, Sample characteristics — «Respondents were on average 40.2 years old (SD=11.8)»
- pct_male: 39.3 — Results, Sample characteristics — «Respondents were on average 40.2 years old (SD=11.8) and majority female (60.7%).»
- pct_other_opioid_use: NR — Results, Sample characteristics; Discussion — «followed by tobacco (42.2%), cannabis (37.2%), and opioids (33.0%)... It was also impossible to distinguish medically prescribed from illicit use of opioid med…»
- instruments: DSM-5 substance use disorder symptom checklist applied to kratom, past year, self-report online (English) — Methods, Measures — «Participants completed a DSM-5 substance use disorder (SUD) symptom checklist to assess whether past-year kratom use met diagnostic criteria for a kratom-relat…»
- industry_funding: NR — Full text (no funding statement in supplied text) — «Fifty-three percent of the final sample learned about the survey through the American Kratom Association»
- funding_coi: NR; the supplied text has no funding or COI statement. Recruitment went mainly through the American Kratom Association (advocacy), but nothing says it funded the study. — Full text — «distributed via sites of interest to kratom users (e.g., American Kratom Association, Erowid, Reddit)»
- pub_status: journal — Header (Drug and Alcohol Dependence 2020) — «Year: 2020; venue: Drug and alcohol dependence; DOI: 10.1016/j.drugalcdep.2020.107849»
- language: English — Full text — «Kratom (Mitragyna speciosa): User demographics, use patterns, and implications for the opioid epidemic»
- notes: Age and sex describe the whole final sample, which is all kratom users (n=2,798). pct_male is 100 minus 60.7% female; it assumes only two sex categories (Table 1 not supplied). Response rate is NR: 66% is eligible completers among the 4,302 who started an open survey. Past-year opioid use was 33.0%, but prescribed and illicit use are not distinguished. A pilot of n=36 via Amazon MTurk was paid. The SOWS (withdrawal only) was given to people endorsing possible withdrawal; it is context only. Tables 1-2 were missing from the supplied text. Product form: powder 43.6%, prepared beverage 37.0%.

**Риск смещения (JBI):**
1. рамка выборки: **no** — Recruitment was through kratom-interest and advocacy sites (53% via AKA), so the frame covers only part of US kratom users. — Methods, Data collection; Results — «Fifty-three percent of the final sample learned about the survey through the American Kratom Association»
2. способ отбора: **no** — Self-selected online convenience (opt-in) sample. — Discussion — «the self-selected convenience sample queried»
3. размер выборки: **yes** — n = 2,798 kratom users, which is at least 246. — Results, Sample characteristics — «resulting in a final sample of 2,798 kratom users»
4. описание выборки и условий: **yes** — Age, sex, setting (online), country (US 97%) and dates (Jan-Dec 2017) are all reported. — Abstract; Methods — «mean age 40 (SD=12); predominantly White (90%), female (61%), and located in the US (97%)»
5. охват (пропуски): **unclear** — Only people who completed the whole survey were analysed. The report does not separate eligible people who dropped out from ineligible starters. — Results, Sample characteristics — «Of the 4,302 individuals who began the survey, 2,826 (66%) met all study inclusion criteria and completed the entire survey.»
6. валидность определения случая: **yes** — The DSM-5 SUD criteria were applied to kratom item by item through a symptom checklist. — Methods, Measures — «Participants completed a DSM-5 substance use disorder (SUD) symptom checklist to assess whether past-year kratom use met diagnostic criteria»
7. единое надёжное измерение: **yes** — Everyone completed the same online self-report checklist with the same past-year time frame. — Methods, Measures — «DSM-5 substance use disorder (SUD) symptom checklist to assess whether past-year kratom use met diagnostic criteria»
8. статистика (числитель и знаменатель): **yes** — The numerator and denominator are clear (56/2,798), so a CI can be calculated. — Abstract — «Fifty-six individuals (2%) met DSM-5 criteria for a past-year moderate or severe kratom-related SUD»
9. отклик: **no** — Open online survey with no denominator of invited people and no handling of non-response. — Methods, Data collection — «participants were recruited using online advertisements and email announcements distributed via sites of interest to kratom users»

Правки:
- 

Проверено: да

