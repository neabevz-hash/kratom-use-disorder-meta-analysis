# Проверка выписывания — файл 2 из 2

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

## ST11 · Singh 2013 · 

Основной отчёт R3754: [текст](../../fulltext/text/R3754.txt) — «Measuring Dependence Severity Of Ketum (Mitragyna Speciosa) Use Among Ketum Leaf Users In Malysia»
Связь отчётов: Probably the same sample as Singh, Müller & Vicknasingam (2014, Drug and Alcohol Dependence, 10.1016/j.drugalcdep.2014.03.017; 293 regular users, Penang, Kedah, Perlis), not retrieved
Расхождения в тексте: The abstract says sampling was 'purposive and quota'. Section 1.10 says 'purposive and chain referral'. I coded sampling as snowball (chain referral). In the abstract, the dependence result (55% severe) is the same in the Malay version (p. xxi: 'Lima-puluh lima peratus ... pergantungan terhadap ketum yang teruk') and the English version (p. xxiii). The tables could not be checked because they were not received.
Заметка ИИ: The received text is incomplete. It stops partway through Chapter 2, section 2.2, page 24. Not received: Chapter 3 (methods: inclusion criteria, LDQ scoring and cut-offs, translation, data years), Chapter 4 (results, including Table 4.1 demographics, Table 4.4 dependence severity and Figure 4.7), Chapters 5 and 6, and the appendices. All dependence data therefore come from the abstract. Other results in the abstract are not estimates: 'need to use ketum daily' 79%, 'unable to control ketum desire' 72%, and severe withdrawal on the MWC 33%. They are only described in the notes. Also published …

### ST11-1 · Ketum leaf users, Penang/Kedah/Perlis, northern Peninsular Malaysia, PhD thesis 2013, n=293 (all male)
Отчёты: R3754 (main); probably same sample as Singh, Müller & Vicknasingam 2014 DAD (10.1016/j.drugalcdep.2014.03.017), not retrieved

**Оценки — ключевые числа сверить по таблице статьи:**

| | Подгруппа | Шкала · порог | Уровень | Случаи / n | % | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | all | LDQ · LDQ 'severe dependence' category (score cut-off not in received text; LDQ range 0-30) | **NR** | **161 / 293** | 54.9 | Abstract, p. xxii-xxiii (Malay abstract p. xxi gives the sa… | «Fifty-five percent of the sample reported severe ketum dependence, 33% reported severe ketum withdrawal and 23% reported high ketum craving.» |

- E1: cumulative: yes; источник порога: study's own; правило: LDQ row; lower bound of 'severe' category cannot be placed (scoring section 3.11.1 not received): if top band alone -> …; у авторов: «severe ketum dependence»; главная у авторов: yes; период: NR; **расчёт: 55% x 293 = 161.15 -> 161**; заметка: Cumulative coding assumed (severe = all scores above cut-off). Full category distribution and medium vs long-term breakdown (Table 4.4, Figure 4.7, p. 145) not in received text.

**Ключевые поля выборки:**
- **n_users: 293** — Abstract, p. xxii — «A total of 293 ketum users were surveyed»
- **sample_type: community_users** — Section 1.10, p. 17-18 — «ketum users were scattered in small numbers across the study locations, as well as, there was no sampling frame available for ketum users.»
- **sampling: snowball** — Section 1.10, p. 18; Abstract, p. xxii — «Both purposive and chain referral sampling techniques were used to recruit respondents for this study.»
- **use_period: NR** — Section 3.7 inclusion criteria not in received text — «3.7 Study Inclusion Criteria........................................................................... 111»
- **region: Southeast Asia** — Abstract, p. xxii — «three northern states of peninsular Malaysia (Penang, Kedah and Perlis)»

**Остальные поля:**
- country: MYS — Abstract, p. xxii — «A total of 293 ketum users were surveyed from three northern states of peninsular Malaysia (Penang, Kedah and Perlis).»
- data_years: NR — Methods chapter (3.3) not in received text — «3.3 Sampling and Data Collection................................................................. 107»
- design: cross-sectional — Abstract, p. xxii — «A cross-sectional study design using non-probability sampling techniques (purposive and quota) was used to collect data.»
- recruitment_channel: general — Section 1.10, p. 18 — «all the interviews were carried out in places which were convenient for both the interviewer and interviewee.»
- regular_use_required: regular use (exact rule NR; inclusion criteria section not received) — Section 1.10, p. 17 — «the study was a cross-sectional survey study mainly designed to determine severity of ketum dependence in regular ketum users.»
- product_form: traditional leaf — Abstract, p. xxiii; Section 1.10, p. 19 — «Those who consumed ≥4 glasses of ketum daily (each glass is equivalent to 350ml of fresh ketum juice)»
- response_rate: NR — Section 1.10, p. 18 — «Potential ketum users in some targeted study locations refused to cooperate with the researcher.»
- age_mean: NR — Abstract, p. xxii — «46% were between the ages of 18-25 years»
- age_sd: NR — Abstract, p. xxii — «46% were between the ages of 18-25 years»
- pct_male: 100 — Abstract, p. xxii — «Respondents were all male, majority of Malay ethnicity.»
- pct_other_opioid_use: NR — Section 1.10, p. 18-19 — «Many ketum users in some of the targeted study locations were using other illicit drugs, or were mixing their ketum drinks with other substances, thus making t…»
- instruments: Leeds Dependence Questionnaire (LDQ) adapted for ketum; language version NR (translation procedure section 3.13 not received; probably Malay) — Abstract, p. xxii; Section 1.9, p. 17 — «Four study instruments specifically the Leeds Dependence Questionnaire, Marijuana Withdrawal Checklist, Marijuana Craving Questionnaire-Short Form, and Addicti…»
- industry_funding: no — Acknowledgement, p. ii — «I would also like to thank the Ministry of Sains and Technology (MOSTI) for financially supporting my research work.»
- funding_coi: Funded by Malaysian Ministry of Science and Technology (MOSTI); COI statement NR — Acknowledgement, p. ii — «thank the Ministry of Sains and Technology (MOSTI) for financially supporting my research work.»
- pub_status: thesis — Title page — «Thesis submitted in fulfilment of the requirements for the degree of Doctor of Philosophy April 2013»
- language: English (abstract also in Malay) — Abstract, p. xxii; Abstrak, p. xx — «MEASURING DEPENDENCE SEVERITY OF KETUM (MITRAGYNA SPECIOSA) USE AMONG KETUM LEAF USERS IN MALAYSIA ABSTRACT»
- notes: The received text is incomplete: it stops in Chapter 2 (p. 24). Not received: methods (Ch. 3), results (Ch. 4), discussion and appendices. All values come from the abstract and Chapter 1. Age: only the share aged 18-25 (46%) is reported; there is no mean or SD. All respondents were male, so the sample is the same as the kratom users. Users of other illicit drugs and people who mixed ketum with other substances were described as unsuitable, so these were probably exclusion criteria (Section 3.8 not received). The MWC (a withdrawal checklist; 33% severe withdrawal), the MCQ-SF (craving) and the…

**Риск смещения (JBI):**
1. рамка выборки: **no** — Target is ketum users in Malaysia; recruitment limited to selected locations in three northern states with no sampling frame. — Section 1.10, p. 17-18 — «our results cannot be generalized to all ketum users in the northern states or elsewhere»
2. способ отбора: **no** — Non-probability purposive, quota and chain-referral sampling. — Abstract, p. xxii; Section 1.10, p. 18 — «non-probability sampling techniques (purposive and quota)»
3. размер выборки: **yes** — n=293 kratom users (>=246). — Abstract, p. xxii — «A total of 293 ketum users were surveyed»
4. описание выборки и условий: **unclear** — Sex, age distribution, setting and country given; dates of data collection not in received text. — Abstract, p. xxii — «Respondents were all male, majority of Malay ethnicity. Eighty-five percent were employed, 46% were between the ages of 18-25 years»
5. охват (пропуски): **unclear** — Missing LDQ data not reported in received text (results chapter missing). — Chapter 4 not received — «4.5.1 Severity of Ketum Dependence..................................................... 144»
6. валидность определения случая: **unclear** — LDQ adapted for ketum; the cut-off behind 'severe dependence' is not in received text, and no LDQ cut-off validated in kratom users is reported. — Abstract, p. xxii-xxiii — «Fifty-five percent of the sample reported severe ketum dependence»
7. единое надёжное измерение: **yes** — Same instruments used for all respondents in interviews by trained interviewer(s). — Section 1.10, p. 18; ToC 3.12 — «all the interviews were carried out in places which were convenient for both the interviewer and interviewee.»
8. статистика (числитель и знаменатель): **yes** — Denominator 293 clear; percentage given so numerator and CI calculable (count itself not in received text). — Abstract, p. xxii-xxiii — «Fifty-five percent of the sample reported severe ketum dependence»
9. отклик: **unclear** — Response rate not reported; refusals mentioned but not quantified. — Section 1.10, p. 18 — «Ketum users in these locations were unwilling to participate in the study, because they were afraid that their personal information would be disclosed to the p…»

Правки:
- 

Проверено: да

