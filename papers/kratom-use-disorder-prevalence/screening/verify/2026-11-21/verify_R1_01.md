# Проверка с метками ИИ, часть 1

Записи 1–150 из 251, с метками обеих моделей над строкой решения. Модели согласны и вы тоже — поставьте `=`; иначе свой код (`+`, `?` или `-`, причина не нужна). Если модели разошлись, `=` не годится — нужен ваш код. Решаете вы.

**Как размечать.** Под каждой записью есть строка **Решение:** — допишите в неё код, после кода можно оставить заметку.

| Код | Что значит |
| --- | --- |
| `+` | включить: количественное исследование людей, которые употребляют кратом (или выборка, где они есть: потребители наркотиков, пациенты на метадоне, студенты, население), и оценена зависимость или расстройство употребления кратома (критерии DSM-5 или DSM-IV, МКБ, шкалы KDS, SDS, ASSIST, интервью MINI или SCID) |
| `?` | не уверен — в сомнениях выбирайте это: лишний полный текст дешевле пропущенного исследования |
| `-1` | исключить: обзор, комментарий, теоретическая, правовая или регуляторная работа |
| `-2` | исключить: качественное исследование без подсчёта людей (интервью, форумы, Reddit); доклиника: животные, клетки, химия, ботаника, анализ продуктов |
| `-3` | исключить: нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки |
| `-4` | исключить: клинический случай или серия случаев; данные токсикологии, отравлений, смертей без опроса людей |
| `-5` | исключить: выборка набрана по проблемам с кратомом: лечение расстройства употребления кратома или абстиненции |
| `-6` | исключить: не про кратом (другие виды Mitragyna) или не про людей, которые его употребляют |
| `-7` | исключить: другое — напишите почему |

Пример: `**Решение:** -2 мыши`. Символы `+ ? -` и цифры одинаковы на русской и английской раскладке.

**Что ищем:** долю расстройства употребления кратома или зависимости среди тех, кто его употребляет. Она часто лежит в таблице с описанием выборки, а аннотация о ней молчит. Опрос употребляющих кратом, где не сказано, оценивали ли зависимость, — `?`. Работа только об абстиненции — тоже `?`. Подробно — протокол, §8.

---

### 1 · R0003

**Differentiation of kratom consumption amounts and correlation of consumption time periods effect to biochemical substance levels in male’s gastrointestinal tracts in Southern Border Provinces, Thailand**

2566 · มหาวิทยาลัยสุโขทัยธรรมาธิราช · thesis

วิทยานิพนธ์ (ส.ม. (บริหารโรงพยาบาล))--มหาวิทยาลัยสุโขทัยธรรมาธิราช, 2566การวิจัยครั้งนี้มีวัตถุประสงค์เพื่อศึกษา 1) ผลของการบริโภคพืชกระท่อมที่มีต่อสารชีวเคมีของระบบ ทางเดินอาหาร และ 2) ค่าการอักเสบในความแตกต่างทั้งด้านปริมาณและความสัมพันธ์ด้านระยะเวลาในผู้บริโภคเพศชาย การวิจัยนี้เป็นการวิจัยเชิงวิเคราะห์แบบภาคตัดขวาง ประชากรที่ศึกษาคือประชากรเพศชายที่บริโภค พืชกระท่อมและอาศัยอยู่ในพื้นที่จังหวัดยะลา ปัตตานี และนราธิวาส ใช้สูตรการคำนวณขนาดตัวอย่างกรณีไม่ ทราบประชากรและสุ่มตัวอย่างแบบหลายขั้นตอนจำนวน 87 ราย รวบรวมข้อมูลโดยใช้แบบสัมภาษณ์และเจาะ เก็บเลือด ทดสอบความเชื่อมั่นโดยหาค่าสัมประสิทธิ์แอลฟาของครอนบาคมีค่าเท่ากับ 0.71 วิเคราะห์ข้อมูลโดย หาค่าความถี่ ร้อยละ ค่าเฉลี่ย ส่วนเบี่ยงเบนมาตรฐาน เปรียบเทียบความแตกต่างโดยการทดสอบค่าทีแบบอิสระ ต่อกัน การทดสอบแมนท์วิทนียูเทส และหาความสัมพันธ์โดยค่าสัมประสิทธิ์สหสัมพันธ์เพียร์สัน สัมประสิทธิ์ สหสัมพันธ์เชิงอันดับของสเปียร์แมน พร้อมแสดงแผนภาพการกระจายของข้อมูล ผลการศึกษาพบว่า 1) ค่าเฉลี่ยของการตรวจวัดอัตราการตกตะกอนของเม็ดเลือดแดง มีแนวโน้มสูง กว่าค่าอ้างอิงและสูงกว่าค่ากลางของค่าอ้างอิงในขณะที่ค่าเฉลี่ยของสารชีวเคมีรายการอื่น ๆ อยู่ภายในค่าอ้างอิง ด้านปริมาณการบริโภค (< 40 กับ ≥ 40 ใบต่อวัน) ความถี่การบริโภค (< 10 กับ ≥ 10 ครั้งต่อวัน) และ จำนวน การบริโภค (< 8 กับ ≥ 8 แก้วต่อวัน) ทุกรายการไม่พบความแตกต่างอย่างมีนัยสำคัญทางสถิติที่ระดับ 0.05 และ 2) ความสัมพันธ์ด้านระยะเวลาการบริโภคกับสารชีวเคมีและค่าการอักเสบ พบว่าไม่มีความสัมพันธ์ต่อระดับสาร ชีวเคมียกเว้นค่าเฉลี่ยของการตรวจวัดอัตราการตกตะกอนของเม็ดเลือดแดงที่สูงขึ้นเล็กน้อย ถึงกระนั้นผู้บริโภค ยังคงต้องบริโภคในปริมาณที่เหมาะสมและใช้ในรูปแบบของการเป็นพืชสมุนไพรตามแนวทางของกระทรวง สาธารณสุขกำหนดอย่างเคร่งครัดต่อไปThis study aimed to 1) investigate the effect of kratom consumption on gastrointestinal biochemistry and 2) inflammation in terms of quantities and durations in a sample of male consumers. This is a cross-sectional analytical study focusing on the male population consuming kratom in Yala, Pattani, and Narathiwat provinces. We used the formula for calculating the sample size for an infinite population and multi-stage random sampling to obtain 87 participants. Data were gathered through interviews using a questionnaire and blood samples’ examination. The questionnaire’s Cronbach's alpha coefficient was calculated and found to be 0.71. The data were analyzed by determining frequency, percentage, mean, and standard deviation, comparing differences using the independent sample t-test, Mann-Whitney U-test, and identifying relationships using Pearson's correlation, Spearman rank correlation coefficient and scatter plot. The results showed that, 1)among the participants, the mean erythrocyte sedimentation rates (ESRs) tended to be higher than the reference values. However, the mean values of other biochemical substances were within the reference levels (not higher than the reference values). There were no significant differences in quantities consumed (<40 vs. ≥40 kratom leaves per day), frequency of consumption (<10 vs. ≥10 times per day), and number of glasses consumed (<8 vs. ≥8 glasses per day) at the 0.05 level. 2) There was no correlation between time periods of consumption and biochemical or inflammation levels, with the exception of slightly higher ESR values. However, consumers must take the right amount and use it as a medicinal plant in strict conformity with the Ministry of Public Health's guidelines

**ИИ:** разошлись — Opus ? (неясно, оценивали ли зависимость: Cross-sectional interview survey of 87 male kratom users; focus is blood chemistry, and the abstract doesn't say if dependence was assessed.); Sonnet -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: Cross-sectional study of 87 male kratom consumers measuring GI biochemistry and inflammation by consumption amount; no dependence or use-disorder assessment mentioned.)

**Решение:** ? опрос 87 потребителей в Таиланде: зависимость может быть в таблице

---

### 2 · R0050

**The perceive utility of kratom ( Mitragyna speciosa ) as a harm reduction agent among people who use drugs (PWUDs) in Malaysia**

2026 · Journal of Substance Use · article, journalarticle, journal-article · en · https://doi.org/10.1080/14659891.2026.2658809

ABSTRACT Background The use of kratom (Mitragyna speciosa) as a harm reduction agent remains poorly understood. Our study determined whether people who use drugs (PWUDs) utilize kratom for its perceived harm reduction benefits. Methods A total of 318 individuals who were undergoing drug rehabilitation and reported to have used kratom participated in this cross-sectional study. Results Majority were males (92%, n = 293/318) and their mean age was 32.7 (SD = 9.9). A majority (80%, n = 253) indicated that kratom offers harm-reduction benefits by mitigating drug-related harms. Similarly, 78% (n = 248/318) perceived that kratom consumption can help PWUDs maintain their abstinence. PWUDs also reported that kratom helped them reduce their frequency of illicit drug use (86%, n = 274/318) as well as intake (83%, n = 264/318). About 70% (n = 222/318) indicated that kratom has effects comparable to methadone and could be used as a substitute. Approximately 74% (n = 236/318) reported that kratom prevented their involvement in risky drug injecting practices. Our findings indicate that ATS poly-drug users are more likely than ATS users to use kratom as a harm reduction agent to minimize drug-related harms (OR = 2.2; 95% CI: 1.23–3.93; p < .007). Conclusions Kratom may be used as a safe harm reduction agent because of its harm-minimizing potential.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of 318 Malaysian PWUDs in rehab who used kratom; it focuses on perceptions, and the abstract doesn't say whether kratom dependence was assessed.

**Решение:** =

---

### 3 · R0060

**Determination of urinary mitragynine concentration and severity of kratom dependence among people with kratom dependence in Malaysia**

2026 · Asia-Pacific Journal of Molecular Biology and Biotechnology · article, journalarticle, journal article · en · https://doi.org/10.35118/apjmbb.2026.034.3.14

Kratom is used traditionally for its medicinal properties in Southeast Asia. The main alkaloid content of kratom leaves is mitragynine, and it binds to opioid receptors. Therefore, kratom exerts opioid-like effects and carries a risk of addiction if used for a long period of time. In this study, we aimed to evaluate the urinary mitragynine of people with kratom dependence and relate it to habitual use of kratom. The severity of kratom dependence among respondents is assessed using the Kratom Dependence Score method. The concentration of mitragynine in urine was analyzed using LC/MS/MS. Significant variation in urinary mitragynine concentration was observed, ranging from the lowest of 58 ng/mL to the highest of 18,000 ng/mL. Urinary mitragynine concentration showed no significant association with the severity of kratom dependence. While Kratom Dependence Score analysis revealed a positive association between the severity and duration of kratom use (p=0.024). Many (36%) of people with kratom dependence confessed to recreational kratom use in their twenties. Urinary concentration of mitragynine does not correlate with severity (H=1.267, df=2, p=0.531) and long-term kratom dependency (H=0.860, df=3, p=0.835).

**ИИ:** ? · обе модели · другое · KDS used, but the sample is called 'people with kratom dependence', so they may have been recruited because of it. Recruitment is unclear.

**Решение:** =

---

### 4 · R0076

**Ketamine Therapy for Chronic Pain Provides Added Benefits for Substance Misuse Therapy**

2026 · SVOA Medical Research · article, journalarticle · en · https://doi.org/10.58624/svoamr.2026.04.006

Background: Chronic pain is complicated by comorbid substance misuse. This multifaceted problem increases the risks of polypharmacy, overdose, impaired driving, and avoidable emergency care. Methods: This is an observational study of a convenience sample of twenty adult chronic pain patients who underwent regular monthly intramuscular ketamine for multimodal pain therapy. Ketamine was administered at 0.25 mg/kg per treatment session. Each treatment also involved lidocaine plus magnesium nerve blocks. The cohort was profiled by gender and substance misuse category (benzodiazepine, cocaine, kratom, opioid). Numeric pain score, Severity of Dependence Scale (SDS), and PHQ-9 scores were analyzed. Results: Females comprised 55% (11/20) and males 45% (9/20). Opioids were the most frequent misuse category (45%; 9/20), followed by benzodiazepines (25%; 5/20), cocaine (20%; 4/20), and kratom (10%; 2/20). After repeated treatments, substance misuse improved in all patients, with concordant improvements in mood, pain, and dependence severity. PHQ-9 improved from moderately severe to mild mood disorder, pain improved from severe to moderate, and SDS improved to satisfactory levels. Conclusion: These outcomes indicate that ketamine-based chronic pain therapy is a potential system for integrated substance-misuse therapy within value-based healthcare, highlighting measurable outcomes, risk mitigation, and public safety. Future studies should include larger prospective studies and collaboration with clinical pharmacists and public safety professionals.

**ИИ:** ? · обе модели · другое · Small chronic-pain cohort with SDS; 2 patients misused kratom. They may have been selected for kratom misuse, so the denominator is unclear.

**Решение:** =

---

### 5 · R0088

**Kratom Component in Clinical Trial for Opioid Use Disorder**

2026 · Psychiatric Times · article

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: Trade-magazine news piece about a kratom-derived compound being trialled for opioid use disorder; it is not a survey of kratom users.); Sonnet ? (нет аннотации: No abstract; Psychiatric Times item likely a news piece on a kratom component in an OUD trial, probably not a prevalence study, but unclear.)

**Решение:** - новостная заметка в Psychiatric Times

---

### 6 · R0105

**IDDF2026-ABS-0493 Cannabis and Kratom use and liver biochemistry in patients with gastrointestinal and liver diseases after legalization in Thailand**

2026 · Gut · article, conference-paper, proceedings-article · en · https://doi.org/10.1136/gutjnl-2026-iddf.222

Background Background and Aims: Since the legalization of cannabis and kratom in Thailand in 2022, their use has become widespread. However, data on their liver biochemistry in patients with underlying gastrointestinal and liver diseases remain limited. Methods We conducted a cross-sectional study among adult outpatients attending gastroenterology and hepatology clinics at a tertiary referral center in Southern Thailand between February 2024 and June 2025. Participants completed a structured questionnaire on cannabis and kratom use. Alanine aminotransferase (ALT) values over the preceding two years were retrieved retrospectively. Associations between substance use and longitudinal ALT levels were evaluated using linear mixed-effects models adjusting for age, sex, body mass index, cirrhosis, metabolic dysfunction–associated steatotic liver disease (MASLD), and alcohol consumption assessed by AUDIT. Results Among 819 participants, 60 (7.3%) reported cannabis use only, 60 (7.3%) kratom use only, 72 (8.8%) use of both substances, and 627 (76.6%) reported no use of either. Among 681 patients with chronic liver disease (CLD) and available ALT data, cannabis use was independently associated with a 17% higher ALT level compared with non-users (exp(β)=1.17, p=0.015). Kratom use was associated with a non-significant 10% lower ALT level (exp(β)=0.90, p=0.10). Higher ALT levels were also associated with male sex (exp(β)=1.26, p<0.001), younger age (per year: exp(β)=0.992, p<0.001), cirrhosis (exp(β)=1.13, p=0.014), MASLD (exp(β)=1.31, p<0.001), and hazardous alcohol consumption (exp(β)=1.38, p=0.014), whereas low-risk alcohol use was associated with lower ALT levels (exp(β)=0.87, p=0.012). Conclusions In this real-world cohort of patients with CLD, cannabis use was associated with modest but significant ALT elevation, whereas kratom use was not. These findings highlight the importance of routine screening, counseling, and monitoring of cannabis use in patients with CLD following legalization. Prospective studies with detailed exposure assessment are needed to clarify causality and long-term hepatic outcomes.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Outpatient survey identified 132 kratom users via structured questionnaire; abstract doesn't say whether kratom dependence was assessed.

**Решение:** =

---

### 7 · R0122

**An Initial Survey Assessing the Temporal Relationship of Kratom Initiation With Medical Treatment and Substance Use.**

2026 · Substance use : research and treatment · article, journal article, journalarticle · eng · https://doi.org/10.1177/29768357261465591

Intro: Kratom use is growing for both therapeutic and non-therapeutic effects. This survey assessed the temporal relationship between kratom initiation and prior, subsequent, or concurrent substance use or medical treatment. Methods: This cross-sectional, anonymous electronic survey was disseminated to American Kratom Association and Global Kratom Coalition members from 3/2025-9/2025. Adults aged ≥18 years who reported past or current kratom use were eligible. A novel questionnaire was generated assessing: kratom and other substance use characteristics; pursuit of medical treatment for selected diagnoses; and temporal relationships between kratom use and substance use or medical treatment. Results: Of 161 respondents included, most (95.7%) currently versus previously used kratom. Whole-leaf product use was reported most often (90.3%), with 38.3% reporting concentrated kratom extracts and 16.9% single alkaloid isolates. Reasons for kratom use were therapeutic (50.3%), non-therapeutic (16.1%), or both (33.5%). Therapeutic (self-treatment) use was most commonly cited for pain (86.2%), mental focus (52.3%), mental health (46.9%), sleep (43.1%), and substance use disorder (27.7%). Most respondents had used ≥1 other psychoactive substance in their lifetime, including cannabis (74.3%), alcohol (68.2%), stimulants (43.2%), sedatives (33.1%), non-prescribed opioids (26.4%), or tobacco (6.1%); 10.1% reported no prior substance use besides kratom. Whether used for non-therapeutic or therapeutic purposes, kratom was rarely initiated first. Among those with a substance use history, only 3-10% reported trying kratom prior to other substances reported. Among those with pertinent medical conditions, 0-20% initiated kratom before receiving medical care for their reported conditions. Conclusion: This study builds on previous research assessing kratom use motivations, providing insight into the temporal relationship between kratom initiation and substance use or medical treatment. Kratom was rarely the first substance or therapeutic treatment tried, but rather most individuals initiated it concurrently with or after discontinuing other substances or medical care. Larger follow-up studies are warranted to confirm these results.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of 161 people who use kratom; the abstract doesn't say whether kratom dependence or use disorder was assessed. Full text could show it.

**Решение:** =

---

### 8 · R0126

**Prevalence and correlates of kratom use among people who use drugs in Vancouver, Canada**

2026 · Harm Reduction Journal · article, journalarticle, journal article · en · https://doi.org/10.1186/s12954-026-01534-7

A product derived from the Mitragyna speciosa tree, kratom is gaining in popularity for its purported stimulant and analgesic effects and is used with both therapeutic, recreational and harm reduction (e.g., substitution) intent. We sought to identify the prevalence and correlates of lifetime kratom use among people who use unregulated drugs (PWUD). Data were drawn from a cross-sectional survey of PWUD, in addition to cannabis, participating in three open community-recruited prospective cohorts in Vancouver, Canada. We applied logistic regression analysis to identify demographic, behavioural and structural factors associated with ever using kratom. Between 2019 and 2021, 414 individuals were recruited including 111 (28.7%) females; the median age was 43.0 years (interquartile range: 30.2–54.6) and 30 (7.2%) participants reported ever using kratom. In the adjusted analysis, factors significantly associated with kratom use included age (adjusted Odds Ratio [aOR] per five years older = 0.55, 95% confidence interval [CI] 0.41, 0.73), using high potency cannabis products (aOR = 2.82, 95% CI 1.10, 7.23) and using cannabis for harm reduction purposes (aOR = 4.93, 95% CI 1.69, 14.33). In this community-based sample of PWUD set in the context of an ongoing overdose crisis, few endorsed any past use of kratom. For those who had used it, results suggest that kratom was being used therapeutically or as a method of harm reduction among PWUD. Further research is needed particularly to investigate the prevalence and predictors of kratom use, as well as the potential harms and benefits among other populations of PWUD.

**ИИ:** разошлись — Opus -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: PWUD survey assessing only lifetime kratom use and its correlates; no kratom dependence or use-disorder measure indicated.); Sonnet ? (неясно, оценивали ли зависимость: Survey of people who use drugs in Vancouver; 30 ever used kratom. Abstract reports only lifetime use correlates; unclear whether kratom dependence was assessed.)

**Решение:** ? опрос потребителей наркотиков в Ванкувере: мера зависимости может быть в расширенной анкете

---

### 9 · R0135

**Grey Market Substances and Atypical Withdrawal: Tianeptine Use as an Unintended Consequence of Self-Managed Kratom Cessation**

2026 · Journal of the Academy of Consultation-Liaison Psychiatry · journalarticle, article, journal-article · en · https://doi.org/10.1016/j.jaclp.2026.10.150

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract. The title points to a case report on switching from kratom to tianeptine, but the study design cannot be confirmed.); Sonnet -4 (клинический случай или серия случаев; данные токсикологии, отравлений, смертей без опроса людей: No abstract; title and venue suggest a consultation-liaison case report of tianeptine use after kratom cessation, not a prevalence study.)

**Решение:** - клинический случай в J Acad Consult Liaison Psychiatry

---

### 10 · R0188

**Kratom Use in the Czech Republic: Treatment Approaches in Various Target Groups and Settings**

2026 · Digital Repository (National Repository of Grey Literature) · dissertation · en

Background: Kratom (Mitragyna speciosa) has emerged as a substance of growing international public health and regulatory interest due to its increasing global use, expanding commercial market, and evolving regulatory landscape. However, important evidence gaps remain, particularly within European settings. Objective: The overall objective of this thesis was to examine kratom through a multidisciplinary perspective by integrating systematic evidence synthesis with empirical research conducted in the Czech Republic. Specifically, the thesis investigated patterns of kratom use among people who use drugs and adolescents, explored healthcare professionals' experiences and harm reduction perspectives, characterised emerging commercial kratom products, and evaluated changes in the Czech online market following the introduction of national regulation. Methods: A multimethod research design was employed, comprising two systematic reviews, a mixed-methods study, a quantitative cross-sectional study, a cross-sectional web-based market surveillance study, and a longitudinal web-based market surveillance study. Collectively, these studies examined kratom across epidemiological, clinical, market, and regulatory domains. Results: The findings demonstrate that kratom represents a heterogeneous phenomenon whose...

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Thesis includes quantitative surveys of kratom use among people who use drugs and adolescents; abstract doesn't say whether dependence was assessed.

**Решение:** =

---

### 11 · R0194

**Prevalence and Use Patterns of Kratom (Mitragyna speciosa Korth.) in a US Nationally Representative Sample.**

2026 · Journal of psychoactive drugs · article, journal article, journalarticle · eng · https://doi.org/10.1080/02791072.2025.2474249

ABSTRACT With increasing diversity of kratom (Mitragyna speciosa Korth.) products containing higher amounts of alkaloids including mitragynine and 7-hydroxymitragynine, safety becomes a public concern. The study aimed to estimate the prevalence of kratom use and to examine potential benefits and adverse effects based on kratom product formulations. A cross-sectional survey utilized a non-probabilistic nationally representative sampling with a total of 11,545 respondents of which 1,049 reported current kratom use, indicating a 9.1% prevalence. The most common kratom products used in the past 30 days were pills, gummies and powder formulations. Pain relief (n = 603, 57.5%) was the most common condition for using kratom, followed by relaxation/stress relief (n = 562, 53.6%) and boost energy (n = 520, 49.6%). The reported benefits were increased energy from tea bags and improved sleep with leaf or extract powders. A significant positive correlation was found between the increased frequency of consuming kratom shots/extract powder and pain relief (p = .009 and 0.015, respectively. A higher incidence of adverse effects was reported as the amount of kratom per dose increased with gummies/capsules/tablets/pills. The lack of standardization and consistency in kratom products results in unpredictable effects, emphasizing the need for increased research to establish reliable safety guidelines for dosage recommendations.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · US survey with 1,049 current kratom users; abstract covers use patterns, benefits and adverse effects but doesn't say if dependence was measured.

**Решение:** =

---

### 12 · R0220

**Diversification of Kratom in US Markets: Results from an Online Survey and Chemical Assay of Products.**

2026 · Substance use & misuse · article, dataset/dataset, journal article · eng · https://doi.org/10.1080/10826084.2025.2551707

Abstract Background Kratom (Mitragyna speciosa) products in the US have diversified from dried leaf to now include edibles, extracts, teas, and tonics. Higher alkaloid content and/or greater oral exposure across formulations expose consumers to potentially greater amounts of alkaloids per serving in a shorter duration of time, thereby potentially increasing product effect and risk profiles. Methods Six kratom vendors disseminated our anonymous online survey. Participants reported on products use patterns, perceived benefits, and adverse effects. Product samples were classified: powders, edibles, liquids, and teas and were analyzed for alkaloid content using UPLC-MS/MS. Results The final sample consisted of 421 participants, using 61 products. They were 61.8% male and 46.3% between 31 and 50 years. Whole-leaf powders were most popular and reported to provide more pain relief, energy, and improved sleep compared to other products. The most common adverse effect was constipation (73.4%). Edibles were associated with tolerance while liquids were associated with consuming more than intended. Alkaloid content was significantly higher in edibles and whole-leaf powders compared to teas and concentrated liquid extracts. Conclusions Diversification of kratom products and higher alkaloid content per serving or dose expose consumers to inadvertent toxicity. Further clinical investigation of risk profiles for different formulations is needed.

**ИИ:** разошлись — Opus + (употребляющие + мера зависимости: Online survey of 421 kratom consumers reports tolerance and using more than intended, which suggests DSM-5 use-disorder criteria were assessed.); Sonnet ? (неясно, оценивали ли зависимость: Online survey of 421 kratom users; tolerance and consuming more than intended reported, but unclear whether a dependence or use disorder measure was used.)

**Решение:** ? опрос 421 потребителя кратома в США: оценивались толерантность и критерии зависимости

---

### 13 · R0221

**Kava (Piper methysticum) consumption patterns and conceptualizations: results from an online survey.**

2026 · Substance abuse treatment, prevention, and policy · article, collection/collection, journal article · eng · https://doi.org/10.1186/s13011-026-00728-3

Abstract Background ‘Kava,’ or ‘kava kava,’ ( Piper methysticum ) is a psychoactive plant indigenous to the Pacific Islands. Historical consumption is reported to provide anxiolytic and sedating effects. In regions where kava is native, it has been used in religious and cultural practices, as well as for medicinal purposes. The mechanisms by which kavalactones – the best studied psychoactive constituent of kava – may mediate pharmacological effects include enhancing the GABA A receptor, blocking of sodium and calcium channels, blocking reuptake of norepinephrine dopamine, and inhibiting MAO-B. In the United States, products containing kava have proliferated in recent years alongside the rise of ethnobotanical tea bars serving kava preparations. Methods Between December–July 2024, an anonymous online survey on legal psychoactive products was conducted using convenience sampling. Eligible individuals had to be ≥ 18 years old and endorse lifetime use of kratom, kava, tianeptine, and/or akuamma seed. Results Of the 368 participants, almost half ( n = 180, 48.9%) had used kava during their lifetime. Those who reported lifetime use of kava were younger on average ( p = 0.001), more racially diverse ( p = 0.041), and had a higher proportion of being employed or in school ( p = 0.012) than those where did not use kava in their lifetime. Kava was purchased online (40.6%) or in ethnobotanical tea bars (31.7%). Many reported infrequent consumption (average = 4.4 months/year and 9.1 days/30 days). Lifetime use of alcohol, kratom, and cannabis was common. Approximately one-third of participants had consumed kava more than 100 times, with commonly reported perceived effects from kava experienced in the minutes and hours after consumption included reduced general anxiety (33.7%), improved mood (32.9%), reduced social anxiety (25.5%), and sedation (23.4%). Most respondents had favorable conceptualizations of kava, with only 11.7% characterizing that kava alone as habit-forming. Many (51.7%) conceptualized kava as an alcohol replacement with 18.3% and 16.7% using kava as a short- and/or long-term substitute for alcohol, respectively. Conclusions Kava use practices are diverse, though perceived kava effects appear mostly mild. The proliferation and diversification of kava products pre-mixed with other psychoactive botanicals requires study as the benefit-risk profile may change. Clinicians should be aware of kava use for harm-reduction and other purposes.

**ИИ:** ? · обе модели · другое · Kava-focused paper, but the survey sample includes kratom users; tables might report kratom use disorder, though the abstract gives only lifetime use.

**Решение:** =

---

### 14 · R0235

**Kratom (Mitragyna speciosa) Use and Opioid Tolerance: Implications for Pain Control in the ICU**

2026 · Journal of Pain and Symptom Management · article, journalarticle, journal-article · en · https://doi.org/10.1016/j.jpainsymman.2026.04.424

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the ICU pain-control title suggests a case report or commentary, but a study design with dependence data can't be ruled out.

**Решение:** =

---

### 15 · R0243

**Prevalence of substance use and quality of life among support personnel in a tertiary care hospital in Bangkok**

2026 · Journal of Medical Bioscience · article · en

Background: Substance use has become increasingly widespread, reaching into various sectors, including the healthcare system. This affects work performance, increases the risk of operational errors, and consequently impacts the credibility and image of the organization. Objectives: This research aimed to study the prevalence of substance use, factors related to substance use, and quality of life among support personnel working in a tertiary care hospital in Bangkok Methods: The current study was a cross-sectional descriptive study and collected data from 250 support staff working in a tertiary care hospital in Bangkok from December 2024 to April 2025. Data were collected through individual interviews using structured questionnaires, including demographic information, the Alcohol, Smoking and Substance Involvement Screening Test, and the World Health Organization Quality of Life Brief – Thai version. In addition, urine toxicology testing was conducted to detect the presence of cannabis, methamphetamine, and morphine. Data were analyzed using both descriptive and inferential statistics, including the chi-square test and logistic regression. Results: Among 250 support staff, the prevalence of substance use at least once in a lifetime was 94.0% and 70.8% in the past three months. The five most commonly used substances in the past three months were alcohol (66.0%), tobacco (27.6%), kratom leaf decoction mixtures (5.6%), kratom leaves (3.6%), and cannabis (1.2%). Most participants were classified as having a low risk level of substance use. However, tobacco were associated with a moderate risk level (55.2%). Gender, age, and department were significantly associated with the most commonly used substances, with being male and of younger age found to be the most influential factors associated with substance use and greater severity. Additionally, most participants reported a moderate level of quality of life (51.6%). Conclusion: The majority of support staff were found to have a moderate quality of life and reported having used at least one type of substance in their lifetime, with the most commonly used substances being legal products. Therefore, prioritizing health promotion programs that improve quality of life and address risk factors related to substance use is essential.

**ИИ:** + · обе модели · другая выборка, есть употребляющие и мера зависимости · Hospital staff survey used ASSIST and covered kratom leaves and decoction; ASSIST risk levels for kratom users are likely reported.

**Решение:** =

---

### 16 · R0261

**Unveiling the metabolic signatures of kratom use in humans via NMR-based blood plasma metabolomics.**

2026 · Food research international (Ottawa, Ont.) · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.foodres.2026.119743

Consumption of herbal-based beverages can alter metabolite profiles, reflecting metabolic changes related to their potential health effects. Kratom is traditionally consumed in Southeast Asia as a decoction to treat various ailments. In recent years, kratom has gained substantial popularity in Western countries for a range of off-label uses, however, reports of its adverse effects, including fatalities, have raised safety concerns. Because changes in metabolite profiles can indicate alterations in health status, metabolomics provides a valuable tool for assessing the potential benefits and risks of kratom. Although animal studies suggest that kratom influences metabolic pathways and behavior, human data remain limited. Therefore, this study aimed to characterize changes in blood plasma metabolites and associated metabolic pathways in regular kratom users using an NMR-based metabolomics approach. Blood plasma samples were collected from 37 regular kratom users and 12 control subjects (non-users), and analyzed using NMR spectroscopy. Multivariate analysis revealed a clear separation between the two groups, indicating distinct plasma metabolite profiles. A total of 17 metabolites were identified as different between the two groups based on 1 H CPMG, JRES and HSQC spectra. Among these, glycine, formate, dimethylamine and N-methyltyramine were significantly increased, whereas pyruvate, ʟ-pyroglutamic acid and citrate were significantly reduced in kratom users compared with non-users. Metabolite enrichment and pathway analyses revealed perturbations in glycine, serine, and threonine metabolism; pyruvate metabolism; glyoxylate and dicarboxylate metabolism; citrate cycle; glycolysis or gluconeogenesis; and glutathione metabolism in kratom users. The biological relevance of these metabolites and pathways is discussed. Overall, these findings provide a better understanding of the metabolic alterations associated with long term kratom consumption in humans.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Clinical metabolomics study of 37 regular kratom users; the sample description may report dependence, but the abstract doesn't say.

**Решение:** =

---

### 17 · R0263

**Exploring Kratom Use in High-Prevalence Areas of Southern Thailand: Attitudes, Knowledge, and Consumption Patterns – A Mixed-Methods Study**

2026 · Research Medical Journal · article, journalarticle, journal-article · en · https://doi.org/10.33165/rmj.2026.e272935

Background: Kratom (Mitragyna speciosa), a tropical tree native to Southeast Asia, has traditionally been used in Thailand for medicinal and recreational purposes. Although recently legalized for medicinal use, concerns remain regarding its safety and potential for abuse. Objectives: To investigate kratom consumption patterns and identify demographic, behavioral, and cognitive predictors of current and harmful use in high-prevalence rural communities in southern Thailand. Methods: A cross-sectional study was conducted among 169 participants from southern Thai communities with high kratom use. A structured questionnaire assessed demographics, attitudes, knowledge, and usage patterns. Harmful use was defined as consumption of more than 20 leaves per day. Multiple logistic regression analysis identified predictors of current and harmful use. Results: Among participants, 45 (26.6%) were current users, and of those 22 (48.9%) met the criteria for harmful use. Predictors of current use included younger age (adjusted OR [AOR], 0.97; 95% CI, 0.94-0.99), tobacco use (AOR, 16.12; 95% CI, 5.01-51.86), poor mental health (AOR, 8.8; 95% CI, 2.2-35.16), and favorable attitudes toward kratom (AOR, 1.12 per point; 95% CI, 1.06-1.18). Harmful use was associated with long-term consumption (AOR, 10.54; 95% CI, 1.01-109.9), boiling as the method of use (AOR, 80.96; 95% CI, 4.98-1315.6), and lower knowledge scores (AOR, 17.8; 95% CI, 1.57-201.68). Conclusions: Current and harmful kratom use are linked to specific demographic and behavioral factors. These findings support the need for targeted public health education and regulation in high-risk communities.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Thai community survey with 45 kratom users; 'harmful use' defined by leaf count, but full questionnaire may include dependence items.

**Решение:** =

---

### 18 · R0272

**Patterns of Kratom Use after Regulatory Changes: A Cross-Sectional Questionnaire Survey**

2026 · Digital Repository (National Repository of Grey Literature) · dissertation · cs

Background: Kratom (Mitragyna speciosa) has in recent years become one of the fastest- spreading psychoactive substances in the Czech Republic. Its use is associated with risks of dependence and other health complications. Since 2026, a regulation of psychomodulatory substances has been in effect in the Czech Republic, aiming to reduce the negative health and social impacts of the supply of psychoactive substances, and kratom was included under this regulation. This change created an opportunity to evaluate its impact on both users and the kratom market. Aims: The aim of the diploma thesis was to capture the current patterns of kratom use in the Czech Republic following the introduction of the new regulation and to map changes in user behaviour, kratom availability, sales practices, and users' risk perception. Changes in consumer habits and adherence to the recommendations stated on the packaging of regulated products were also monitored. The research further focused on the occurrence of symptoms of dependence and their associations with selected sociodemographic and user characteristics. Methods: The research had a quantitative cross-sectional design, using a custom anonymous online questionnaire created in Google Forms. The questionnaire included questions on sociodemographic data, patterns and...

**ИИ:** + · обе модели · употребляющие + мера зависимости · Czech online survey of kratom users assessing dependence symptoms and their correlates; thesis likely reports the proportion with dependence.

**Решение:** =

---

### 19 · R0326

**Hematological and clinical-chemistry parameters of kratom users: a comparative study of users and non-users in Southern Thailand.**

2026 · Scientific reports · article, comparative study, research-article · eng · https://doi.org/10.1038/s41598-026-35524-3

Kratom (Mitragyna speciosa) has transitioned from a traditional Southeast Asian remedy to a substance of global interest. The existing evidence on its safety is contradictory, with case reports from Western countries suggesting organ toxicity, while community-based studies in traditional settings show minimal adverse effects. This study aimed to evaluate the physiological impact of long-term, traditional kratom use in an endemic region of Southern Thailand. A cross-sectional study was conducted among 285 traditional kratom users and 296 non-user controls from the same community. Key hematological and clinical-chemistry parameters, including liver and kidney function markers, were compared. Analyses were stratified by sex and kratom use characteristics (duration and quantity) to assess subgroup-specific effects. Analysis of Covariance (ANCOVA) was used to adjust for potential confounding variables, including age, sex, BMI, smoking, and alcohol consumption. After adjusting for confounders, no clinically significant differences were observed in hepatic or hematological parameters, with mean values for both groups remaining within normal clinical reference ranges. However, kratom use was significantly associated with lower serum creatinine (p < 0.001) and higher eGFR (p = 0.002), a finding likely attributable to the lower BMI in the user group. Stratified analyses by duration and quantity revealed no clear dose-response relationship regarding organ toxicity, although higher consumption was associated with altered renal markers. These findings suggest that within a traditional-use setting, chronic kratom consumption was not associated with clinically significant hepatic or hematological toxicity. The observed association with renal markers is explained by differences in body composition rather than a direct pharmacological effect. These findings underscore the critical importance of controlling for lifestyle and demographic confounders in evaluating the health impacts of kratom.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Community sample of 285 traditional kratom users; abstract doesn't say whether dependence was measured, but it may appear in the sample description.

**Решение:** =

---

### 20 · R0356

**Kratom (Mitragyna speciosa) Use and Altered Opioid Responsiveness in the Perioperative Period**

2026 · RVU Elevate · poster/poster, conference-abstract · en · https://doi.org/10.82451/k51030

Background : Kratom (Mitragyna speciosa) is an increasingly used, largely unregulated botanical product in the United States, commonly taken for analgesia, mood symptoms, and mitigation of opioid withdrawal. Its primary alkaloids, mitragynine and 7-hydroxymitragynine (7-HMG), exhibit opioid and non-opioid receptor activity that may alter perioperative responses to anesthetic agents, sedatives, and opioids. Despite rising use, perioperative guidance remains limited.

**ИИ:** разошлись — Opus ? (другое: Truncated poster abstract on perioperative kratom effects; design unclear (likely case report or review), so dependence data are unlikely but not ruled out.); Sonnet -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: Perioperative poster that appears to be a narrative review of kratom pharmacology and anesthesia guidance; no sample of people who use kratom or dependence measure is described.)

**Решение:** - постерный тезис / обзор периоперационного ведения

---

### 21 · R0366

**Kratom Use and Associations With Mental Health in the United States.**

2026 · Journal of addiction medicine · article, journal article, journalarticle · eng · https://doi.org/10.1097/adm.0000000000001701

OBJECTIVES: To assess the US lifetime and past-year prevalence of kratom Mitragyna speciosa use and its associations with mental health and DSM-5 substance use disorder (SUD). METHODS: This study examined cross-sectional survey data collected from 169,408 non-institutionalized individuals aged 12 and older in US households between 2021 and 2024. Measures included kratom use, nonmedical use of cannabis, prescription drugs (opioids, sedatives/tranquilizers, stimulants), other drugs, mental health indicators (serious psychological distress, DSM-5 major depression, suicidal ideation), and DSM-5 SUD. RESULTS: Between 2021 and 2024, lifetime and past-year kratom use were highest among adults aged 21 to 34, 3.40% (95% CI: 3.17-3.65) and 1.01% (95% CI: 0.91-1.13), respectively. Among people who reported prior-to-past-year kratom use, most reported past-year cannabis (65.7%; 95% CI: 60.4-70.3) and had a past-year SUD (52.8%; 95% CI: 50.1-55.4), whereas an estimated 37.8% (95% CI: 37.2-47.3) experienced serious psychological distress. Similar results were observed for those who reported past-year kratom use. Multivariate logistic regression analysis revealed prior-to-past-year and past-year kratom use was associated with increased adjusted odds of past-year SUD (AOR: 4.36; 95% CI: 3.89-4.88 and AOR: 4.81; 95% CI: 3.99-5.80, respectively). Similar results were found for other substance use, DSM-5 major depression, and suicidal ideation. CONCLUSIONS: Over 5 million people in the United States used kratom in their lifetime, with the highest use at ages 21-34 years. Kratom use is increasing and strongly associated among individuals who use cannabis, have a DSM-5 SUD, and experience serious psychological distress. These findings reinforce a profile of individuals who use kratom, many with behavioral health symptoms, and need evidence-based treatment warranting consideration in clinical and policy efforts.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · US national survey (likely NSDUH) assessed kratom use and DSM-5 SUD; unclear whether kratom-specific use disorder was reported.

**Решение:** =

---

### 22 · R0430

**Characteristics of adverse reactions to kratom and implementation of harm reduction strategies in a sample of ethnobotanical tea bar patrons in Colorado.**

2026 · Harm reduction journal · article, preprint, journal article · eng · https://doi.org/10.1186/s12954-025-01382-x

Abstract Background Kratom is a psychoactive botanical that is increasingly popular in the United States. While potential risks of kratom use have been identified, research on harm reduction strategies and contextual factors contributing to adverse reactions is limited. Given that kratom is federally unregulated at present, and a variety of kratom products are widely available on the commercial market, more data are needed to inform harm reduction efforts and public health messaging. Methods 102 participants (mean age = 22.34 years, 39.2% women) were recruited from ethnobotanical tea bars in Northern Colorado to complete a survey on kratom use, which included questions pertaining to adverse experiences. Results Most participants (75.5%) reported experiencing an adverse reaction to kratom at least once in the past, with a wide range of kratom doses reportedly consumed during these experiences. Adverse reactions were most commonly reported to occur in the context of consuming kratom on an empty stomach, consuming alongside certain foods, lack of hydration, and combining kratom with other substances. Participants employed a variety of strategies in attempt to mitigate adverse reactions, such as stopping or pacing their use of kratom and other substances, modulating hydration and food intake, and engaging in rest and recovery behaviors. Conclusions Adverse reactions to kratom may be associated with certain contextual factors. Several techniques are reportedly used to mitigate adverse reactions, but the efficacy of these techniques is unknown. More data are needed to understand the causes and consequences of adverse reactions to kratom, and to better understand potential harm reduction strategies for reducing adverse experiences. More research could also shed light on the extent to which kratom serving size and various product formulations (e.g. whole leaf vs. extracts) are predictive of adverse effects.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of kratom tea bar patrons on adverse reactions; abstract doesn't say whether dependence or use disorder was assessed.

**Решение:** =

---

### 23 · R0452

**Psychoactive substances and their impact on the adolescent population**

2026 · Digitální knihovna Univerzity Pardubice (Univerzity Pardubice) · dissertation, thesis · cs

Bakalářská práce se věnuje problematice užívání psychoaktivních látek u dospívající populace ve věku 15-19 let. Teoretická část práce se zabývá klasifikací návykových látek, specifiky období adolescence a rizikovými faktory vzniku závislosti, včetně popisu nových trendů, jako jsou kratom a HHC. Praktická část práce je realizována formou kvantitativního průzkumného šetření. Jejím cílem je zmapovat prevalenci užívání psychoaktivních látek u dospívajících a pomocí screeningového nástroje CRAFFT identifikovat míru rizika spojeného s jejich konzumací. Práce analyzuje zkušenosti studentů s legálními i nelegálními látkami a zkoumá jejich motivaci k užívání. Výstupy práce poskytují náhled do aktuální situace v oblasti zneužívání návykových látek u mladistvých a mohou sloužit jako podklad pro tvorbu preventivních programů a edukačních materiálů v ošetřovatelské práci.The bachelor's thesis addresses the issue of psychoactive substance use among the adolescent population aged 15-19 years. The theoretical part of thesis deals with the classification of addictive substances, the specificities of the adolescent period, and the risk factors for the development of addiction, including a description of new trends such as krater and HHC. The practical part of the thesis is carried out in the form of a quantitative survey. Its aim is to map the prevalence of psychoactive substance use among adolescents and to identify the level of risk associated with their consumption using the CRAFFT screening tool. The thesis analyses students' experiences with both legal and illegal substances and examines their motivation for use. The outputs of the thesis provide an insight into the current situation regarding substance misuse among juveniles and may serve as a basis for the development of presentation programs and educational materials in nursing practice.Fakulta zdravotnických studiíStudent/ka úspěšně obhájil/a bakalářskou práci, odpověděl/a na doplňující otázky.Dokončená práce s úspěšnou obhajobo

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of adolescents using CRAFFT that mentions kratom; unclear whether kratom use or kratom-specific risk was assessed in the survey.

**Решение:** =

---

### 24 · R0462

**Chaos With Kratom: Kratom Use and Interactions With Immunosuppressants in Transplant Recipients**

2026 · Journal of the Academy of Consultation-Liaison Psychiatry · journalarticle, article, journal-article · en · https://doi.org/10.1016/j.jaclp.2026.10.298

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract. Could be a case series or review, but a chart review of kratom-using transplant recipients reporting use disorder is possible.); Sonnet -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: No abstract; the title and venue (C-L psychiatry journal) suggest a case report or commentary on kratom–immunosuppressant interactions, not a prevalence study.)

**Решение:** - клинический случай / серия реципиентов трансплантата

---

### 25 · R0492

**Prevalence of non-medical drug use and dependence among school-going adolescents in Malaysia**

2026 · Addicta The Turkish Journal on Addictions · article, journalarticle, review · en · https://doi.org/10.15805/addicta.2026.498

Drug abuse can be defined as the use of drugs in a manner that deviates from medical prescription. The negative effects of drug addiction are well known globally, and millions are estimated to suffer from drug use disorders and require treatment services. In Malaysia, recent studies have shown that the great majority of drug users are young adolescents. This trend has now spread to schools and has caused a significant rise in cases of drug abuse annually. Unfortunately, to date, there are no recent data regarding the prevalence of drug and substance abuse amongst school-going adolescents in Malaysia. This study aims to assess the rising prevalence of drug abuse among school-going adolescents in Malaysia through a nationwide representative survey. A total of 3,382 secondary school students participated in this study. They were selected from hotspot areas in Malaysia using a multistage stratified cluster sampling technique. The data were collected through face-to-face interviews, assisted by school counsellors. The Alcohol, Smoking, and Substance Involvement Screening Test (ASSIST) was utilized to measure the frequency of drug use according to type, and the adolescents’ involvement in drug abuse and drug-related behavior. Descriptive analysis was conducted using the Statistical Package for Social Sciences to determine the prevalence of drug abuse among the students. The prevalence of current drug abuse among the adolescent students was found to be 3.9 % for those who had used drugs in the past 30 days. Meanwhile, lifetime use was found to be 9.6%. The most popular drugs used were kratom (Mitragyna speciosa), followed by hallucinogens and cannabis. Most drug users were male students, and the average onset age of drug use was 16. Special attention and urgent action from relevant agencies are thus needed to address this critical issue in the country.

**ИИ:** + · обе модели · опрос населения с ASSIST, DSM или ICD · Nationwide adolescent survey that used ASSIST and found kratom was the most-used drug, so kratom ASSIST risk scores may be reported.

**Решение:** =

---

### 26 · R0499

**Observational real-world analysis of dose-dependent effects of Mitragyna speciosa (Korth.) on focus and energy.**

2026 · Frontiers in pharmacology · article, journal article, journalarticle · eng · https://doi.org/10.3389/fphar.2026.1838148

Background Mitragyna speciosa is a deciduous evergreen tree native to Southeast Asia. The term “kratom” is commonly used to refer to both the tree and its leaves, which have a long history of use as a restorative to provide energy, focus and relief of minor aches and pains associated with physical exertion. Consumption of kratom leaves, either chewed or prepared as a tea or decoction, continues in Southeast Asia to this day. Similar to Southeast Asia, U.S. consumers report taking kratom to alleviate pain, increase energy, and improve negative mood states. We have evaluated the real-world effectiveness of a full-spectrum proprietary kratom extract at doses aligned with traditional ethnopharmacological use, specifically for effects that match the traditional profile of stimulating and focusing effects. Methods This study represents a secondary analysis of data collected during a real-world, longitudinal observational study of adult U.S. participants using a kratom product composed of proprietary full spectrum leaf extract, designed to mimic a traditional kratom tea. Phytochemical equivalence to traditional preparations was established by comparing the alkaloid profile and presence of plant phenylpropanoids. Participants completed daily structured surveys over a 21-day period. Linear mixed-effects models were used to evaluate within-subject changes across baseline, week 1, and week 2 periods. Results Chemical analyses confirmed that the presence and relative ratios of alkaloids were comparable to those found in traditional kratom tea, supporting the extract as a standardized representation of traditional decoctions. At the 20 mg mitragynine-equivalent dose, participants showed statistically significant improvements in focus, problem solving, mental clarity, and energy (p &amp;lt; 0.05). Conclusion A kratom product formulated to be dose-aligned with a traditional kratom tea serving is associated with stimulant-like benefits, increasing energy and focus. This effects profile implies that the pharmacological activity at this dose likely reflects non-opioid receptor mechanisms. </jats:sec

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Longitudinal observational study of US kratom product users; abstract reports focus and energy outcomes, but the parent study may have assessed dependence.

**Решение:** =

---

### 27 · R0509

**Supplemental Material for Toward an Understanding of 7-Hydroxymitragynine (7-OH) Products: Initial Characterization of Use Patterns and Consumer Perceptions**

2026 · Experimental and Clinical Psychopharmacology · journalarticle, supplementary-materials · en · https://doi.org/10.1037/pha0000870.supp

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Supplement to a survey of 7-OH product consumers; no abstract, so it's unclear whether dependence or use disorder was assessed.

**Решение:** =

---

### 28 · R0510

**Tianeptine Products: Public Health Threat or Niche Substance use?**

2026 · Journal of psychoactive drugs · article, journal article, journalarticle · eng · https://doi.org/10.1080/02791072.2025.2570939

ABSTRACT Among adults who have used tianeptine, we aimed to determine demographic and substance-use patterns and gain insights into tianeptine doses, effects, and consumer conceptualizations. We also evaluated problematic use, quit attempts, and tianeptine-specific substance-use disorder (SUD). Between December 2023 and July 2024, an online survey was conducted. Participants were ≥18 years old and endorsed lifetime use of kratom, kava, tianeptine, and/or akuamma seed. Of the 369 respondents, 6.0% (n = 22) reported lifetime tianeptine use; they were 35.6 years old on average, White, and male (81.8%) and evinced diverse substance use. Mean age of tianeptine-use initiation age was 31.0. More within the tianeptine-use group believed they currently had any SUD (40.9% versus 20.2%, p = .0002), had ever been prescribed methadone/buprenorphine (27.3% versus 8.1%, p = .009), and were interested in recovery (72.7% versus 28.8%, p < .0001). Use motivations included euphoria, self-management of psychiatric symptoms, and drug substitution. Tianeptine-tolerance onset was considered rapid (59.1%), with one-third experiencing adverse effects. For past-year tianeptine SUD (n = 15), 13.3% of participants were mild, 53.3% were severe. Many tianeptine conceptualizations were unfavorable: “habit-forming” (68.2%), “addictive” (68.2%), “problematic” (59.1%); 86.3% believed overdose was possible. Tianeptine was used at low rates in this sample of adults who consumed gray-market supplements and included unfavorable perceptions.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Online survey of kratom/kava/tianeptine users that assessed SUD; this paper is about tianeptine SUD, and it's unclear whether kratom SUD is reported.

**Решение:** =

---

### 29 · R0523

**Užívání kratomu u sportovců v pražských posilovnách: dotazníkové šetření**

2026 · master thesis · ces/cze · http://www.nusl.cz/ntk/nusl-780586

Background: This thesis was developed in response to the growing popularity of kratom, which has significantly expanded in recent years in the Czech Republic, particularly among young adults and the physically active population. In the gym environment, it is increasingly perceived as an accessible means of enhancing energy, concentration, and performance, despite the fact that its effects and risks are not sufficiently explored. Objectives: The main aim of this thesis was to map the use of kratom among athletes attending gyms in Prague. The partial objectives were to determine whether sociodemographic and sport-related characteristics influence the use of kratom, to identify the reasons for its use, patterns of combination with other substances, perceived negative effects, and awareness of the risk of addiction. Methods: An online cross-sectional questionnaire study was conducted among visitors of Prague gyms, with data collection taking place from September 2025 to January 2026. The research sample consisted of 634 individuals over 18 years of age recruited through non- probability self-selection sampling with the use of the snowball technique. The data was analyzed using basic statistical methods and by examining relationships between variables. Results: The results show that approximately one...

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of gym-goers about kratom use, with negative effects and addiction awareness; truncated abstract doesn't say if dependence was measured.

**Решение:** =

---

### 30 · R0524

**Use of kratom among athletes in Prague gyms: a questionnaire survey**

2026 · Digital Repository (National Repository of Grey Literature) · dissertation, thesis · cs

Background: This thesis was developed in response to the growing popularity of kratom, which has significantly expanded in recent years in the Czech Republic, particularly among young adults and the physically active population. In the gym environment, it is increasingly perceived as an accessible means of enhancing energy, concentration, and performance, despite the fact that its effects and risks are not sufficiently explored. Objectives: The main aim of this thesis was to map the use of kratom among athletes attending gyms in Prague. The partial objectives were to determine whether sociodemographic and sport-related characteristics influence the use of kratom, to identify the reasons for its use, patterns of combination with other substances, perceived negative effects, and awareness of the risk of addiction. Methods: An online cross-sectional questionnaire study was conducted among visitors of Prague gyms, with data collection taking place from September 2025 to January 2026. The research sample consisted of 634 individuals over 18 years of age recruited through non- probability self-selection sampling with the use of the snowball technique. The data was analyzed using basic statistical methods and by examining relationships between variables. Results: The results show that approximately one...

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Thesis surveying gym-goers who use kratom; covers perceived negative effects and addiction awareness, but abstract is truncated and doesn't say if dependence was measured.

**Решение:** =

---

### 31 · R0536

**The prevalence of kratom use and association with co-occurring substance use among adolescents: a 2022 Bangkok behavioral surveillance survey, Thailand.**

2026 · Journal of ethnicity in substance abuse · article, journal article, journalarticle · eng · https://doi.org/10.1080/15332640.2024.2367233

Abstract Thailand removed kratom from the list of prohibited substances in 2021, possession and consumption of Kratom is now legal. It is prohibited from selling Kratom to anyone under the age of 18 and/or who is pregnant or breastfeeding. While there are benefits from kratom use with few reported adverse effects, escalating dose and increased use frequency raise the risk for toxic events in the setting of polysubstance use or development of a use disorder. We utilized data from the Behavior Surveillance Survey in Bangkok (n = 5,740) to examine the use of kratom with other substances use in the 12 months before the survey. The prevalence of past-year kratom use among students was 9.3% (95%CI = 8.7–9.9), with higher proportions of males (12.4 versus 6.1%, p < 0.001). The factors associated with past 12-month kratom use were academic performance (Medium GPA; AOR = 2.41, 95% CI = 1.76–3.29; Low GPA; AOR = 4.15, 95% CI = 2.94–5.87), close friend use substance (AOR = 1.94, 95% CI = 1.44–2.59), cannabis use (AOR = 6.84, 95% CI = 4.61–10.15), consumed alcohol (AOR = 2.32, 95% CI = 1.77–3.02), smoked conventional cigarettes (AOR = 4.20, 95% CI = 3.16–5.58), used e-cigarettes (AOR = 4.37, 95% CI = 3.30-5.79) used illicit opioids (AOR = 8.13, 95% CI = 4.35–15.18), and other illicit drug use (AOR = 9.15, 95% CI = 3.78–22.14). These findings may be useful for the initial targeting of efforts to reduce adolescent consumption of kratom. Future studies should examine the effect of regulatory policies or other Thai FDA-related policies use of illicit drugs and e-cigarettes on kratom use.

**ИИ:** разошлись — Opus -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: Adolescent surveillance survey reporting only past-year kratom use prevalence and correlates; no kratom dependence or use-disorder measure indicated.); Sonnet ? (неясно, оценивали ли зависимость: Adolescent school survey on kratom use prevalence and correlates; the abstract doesn't say whether kratom dependence or use disorder was assessed.)

**Решение:** - поведенческий надзор среди подростков: только доля употребления, нет меры зависимости

---

### 32 · R0543

**Associations between kratom (Mitragyna Speciosa) use and real-time anxiety and sadness: A 15-day ecological momentary assessment study.**

2026 · Drug and alcohol dependence · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.drugalcdep.2026.113383

Background Kratom (Mitragyna Speciosa) is increasingly used in the U.S. for self-management of pain and mental health symptoms, yet its real-time effects on emotional distress remain poorly understood. We used ecological momentary assessment (EMA) to examine momentary associations of kratom use with anxiety and sadness. Methods A secondary analysis was conducted among 357 adult kratom consumers who adults who consume kratom completed a 15-day EMA protocol. Multilevel models assessed whether kratom use events occurring within the prior 180min were associated with momentary anxiety and sadness, and whether these associations were moderated by past 30-day use of prescribed anxiolytic or antidepressant medications. Results After adjusting for covariates, both single and multiple kratom use events in the previous 180min were associated with lower momentary anxiety compared to no use. For sadness, only single use events were significantly associated with lower scores. Past 30-day prescribed anxiolytic and antidepressant use did not significantly moderate these associations. Higher baseline anxiety and depressive symptoms were associated with greater momentary anxiety and sadness across the 15-day study period. Conclusions Kratom use was associated with small reductions in anxiety and, to a lesser extent, sadness in naturalistic settings. These associations were not influenced by past 30-day history of anxiolytic and antidepressant use. These results highlight kratom's potential role in real-time self-management of emotional distress while underscoring the need for randomized controlled trials and longitudinal studies to determine its clinical significance and long-term impact on mental health.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · EMA study of 357 kratom consumers; the abstract doesn't mention a measure of use disorder, but the parent study likely assessed DSM-5 criteria.

**Решение:** =

---

### 33 · R0558

**Zkušenosti žáků vybrané základní školy s užíváním návykových látek**

2026 · master thesis · ces/cze · http://www.nusl.cz/ntk/nusl-780452

The diploma thesis deals with the issue of the use of addictive substances at the selected primary school in Cerhovice. The aim of the thesis is to analyse the level of awareness, attitudes, and personal experiences of lower secondary school pupils in relation to the use of addictive substances such as nicotine, marijuana, and kratom. The theoretical part focuses on defending the concept of an addictive substance, and the consequences of use from biological, psychological, and social perspectives. It also includes a description of the ontogenetic characteristics of pupils during adolescence. The practical part is based on quantitative research conducted through an anonymous questionnaire among pupils in the 8th and 9th grades of primary school. The research sample consisted of 21 respondents, including 11 boys and 10 girls. The obtained data were processed using descriptive statistics, particularly through absolute and relative frequencies, percentage expression, graphical presentation, and selected contingency tables. The results showed that 67 % of respondents had already tried a products containing an addictive substance, however, regular use was not confirmed in the studied sample. An important finding was that 86 % of pupils had witnessed the use of addictive substances in the classroom or at...

**ИИ:** разошлись — Opus -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: Small descriptive pupil survey of awareness, attitudes and trying substances including kratom; no regular use and no kratom dependence measure.); Sonnet ? (неясно, оценивали ли зависимость: Questionnaire of 21 school pupils on nicotine, marijuana and kratom use; abstract does not say whether kratom dependence was assessed, and regular use was not found.)

**Решение:** - школьный опрос 21 учащегося: нет меры зависимости от кратома

---

### 34 · R0589

**Aggression in a Cohort of Male Methamphetamine (METH) Users With and Without Kratom (Mitragyna speciosa Korth.) Use History in Malaysia.**

2026 · Journal of psychoactive drugs · article, journal article, journalarticle · eng · https://doi.org/10.1080/02791072.2024.2424277

ABSTRACT Methamphetamine (METH) consumption is associated with aggression. Decoction derived from the kratom (Mitragyna speciosa Korth.) leaf has been used as a METH substitute in Southeast Asia. Given its perceived benefit, we investigated the relationship between kratom use and aggression in a treatment sample of METH users with and without kratom use history. Four hundred and three male METH users participated in this cross-sectional study. A semi-structured questionnaire and several objective clinical measures were administered. Results indicate that there were no significant differences in aggression and its dimensions between METH users with and without kratom use history. However, two distinct Clusters (1 and 2) of METH users with kratom use history were studied. Users in Cluster 1 were characterized by a higher quantity and frequency of daily kratom use, longer duration of kratom use, and use of kratom at a younger age. Users in Cluster 2 exhibited the opposite characteristics. Kratom dependence and the first age of kratom use were identified as risk factors for aggression in Cluster 1. The frequency of daily kratom use appeared as a protective factor against aggression in Cluster 2. The results offer partial support to the instrumental kratom use concept; lower frequency (1 to 3 times) of kratom use may potentially minimize aggression in METH users presenting with mild to moderate kratom dependence.

**ИИ:** + · обе модели · другая выборка, есть употребляющие и мера зависимости · METH treatment sample including kratom users; kratom dependence was assessed and analysed as a risk factor for aggression.

**Решение:** =

---

### 35 · R0590

**Association between kratom (Mitragyna speciosa Korth.) use and methamphetamine craving in males who used methamphetamine with and without heroin use history.**

2026 · Journal of ethnicity in substance abuse · article, journal article, journalarticle · eng · https://doi.org/10.1080/15332640.2026.2717681

Field and preclinical studies suggest that kratom ( Mitragyna speciosa ) may have therapeutic potential in moderating methamphetamine (METH) craving. However, there is a lack of clinical studies to affirm this claim. This study explored patterns and motivations of kratom use among people who used METH with and without a history of heroin use, and determined the associations of kratom use patterns with METH craving. A treatment sample of 403 male respondents who had used METH, with and without kratom and with and without a history of heroin use was recruited for this cross-sectional study. A semi-structured questionnaire including Kratom Dependence Scale (KDS), Beck Depression Inventory (BDI), Beck Anxiety Inventory (BAI), and Visual Analog Scale was administered. Our results showed that none of the assessed kratom use indicators were identified as risk factors for the presence of METH craving. Only heroin use history (aOR = 2.61, p = 0.014) and somatic/vegetative symptoms related to depression (aOR = 1.26, p = 0.023) were risk factors for the presence of METH craving. A significant association between the severity of METH craving and age at first kratom use ( β = -0.19, p = 0.0497) was observed among people who used METH with a history of heroin use. Our findings suggest that kratom use patterns may influence METH craving among people who used METH with a history of heroin use. These findings further support the perceived self-therapeutic utility of kratom among people who use drugs (PWUDs).

**ИИ:** + · обе модели · другая выборка, есть употребляющие и мера зависимости · METH treatment sample including kratom users; Kratom Dependence Scale administered, so dependence prevalence among kratom users may be reported.

**Решение:** =

---

### 36 · R0595

**FACTORS ASSOCIATED WITH HEALTH LITERACY REGARDING KRATOM USE AMONG WORKING-AGE KRATOM USERS IN PATHUM THANI PROVINCE, THAILAND: A CROSS-SECTIONAL STUDY**

2026 · Southeast Asian Journal of Tropical Medicine and Public Health · article

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Cross-sectional survey of Thai kratom users with no abstract; dependence may have been assessed as a covariate.

**Решение:** =

---

### 37 · R0700

**Exploring the health and biochemical effects of kratom (Mitragyna speciosa) consumption within the local community of Putussibau district, Borneo, Indonesia**

2025 · Advances in Integrative Medicine · article, journalarticle, journal-article · en · https://doi.org/10.1016/j.aimed.2025.100555

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; community study of kratom consumers in Borneo, which may have assessed dependence alongside health and biochemical effects.

**Решение:** =

---

### 38 · R0729

**การพัฒนารูปแบบการดูแลหญิงตั้งครรภ์ที่มีผลตรวจเมทแอมเฟตามีนในปัสสาวะ โรงพยาบาลสมเด็จพระยุพราชธาตุพนม**

2025 · Journal of Environmental Education Medical and Health · article · th

This Research and Development aimed to study the model and outcomes of caring for pregnant women with methamphetamine test results in urine at Thatphanom Crown Prince Hospital. The sample consisted of 20 pregnant women with methamphetamine test results in urine Purposive Sampling. The single sample group measured before and after (One-group, Pretest-Posttest Design). The instruments used for data collection included personal data, the ASSIST Version 3.1 screening form, the ST-5 stress assessment form, knowledge about drug use in pregnant women, and the urine methamphetamine test results. Data analysis: personal data, the ASSIST Version 3.1 screening form, and the urine methamphetamine test results using the count, percentage, the ST-5 stress assessment form, and knowledge about drug use in pregnant women. The analysis used the mean and standard deviation. Compare before and after participating in the activity using Pair t-test statistics. The research results were after participating in the activity, the relevance scores for specific substances, including tobacco products, alcohol beverages, cannabis, amphetamine stimulants, kratom leaves, and kratom leaf decoction, were at a moderate level. Sedatives or sleeping pills and hallucinogens were at a low level. The stress assessment result (ST-5) before participating in the activity had an average score of 4.85 (SD=4.04), which was at a level suspected of having stress problems. After participating in the activity, the average score was 2.10 (SD=2.04), which decreased to a level without stress, with a statistically significant difference at the .05 level. Knowledge score on drug use during pregnancy Before participating in the activity, the average knowledge score was 8.00 (SD=2.15). After participating in the activity, the average knowledge score increased to 9.90 (SD=.44), with a statistically significant difference at the .05 level. The results of the urine methamphetamine test in pregnant women before and after participating in the activity showed that methamphetamine in the urine decreased from 100 percent to 15 percent.

**ИИ:** + · обе модели · другая выборка, есть употребляющие и мера зависимости · Pregnant methamphetamine-positive women screened with ASSIST 3.1; kratom leaf and decoction risk levels reported, so moderate-risk counts may be extractable.

**Решение:** =

---

### 39 · R0737

**Personal health concerns and signs of dependency as determinants of kratom use**

2025 · Journal of Substance Use · article, journalarticle, review · en · https://doi.org/10.1080/14659891.2025.2609263

ABSTRACT Objective Drawing on data gathered in the 2023 National Survey on Drug Use and Health, this study examined kratom use as a function of four demographic measures, personal health concerns, and whether individuals had experienced difficulties halting the use of specific drugs. Methods With kratom use as a response measure, logistic regression analyses tested the explanatory effects of demographic variables, estimates of overall health, concerns about substance use and mental health, and success (or lack of success) halting drug use across a 12-month period. Results Among respondents 18 years and older, 2.4% had used kratom. Individuals who considered themselves in poor health were more likely to have used kratom, as were those who had been concerned about their drug or alcohol use or their mental health. Individuals who had been unable to quit alcohol, marijuana, pain relievers, and tranquilizers were more likely to have used kratom. Conclusions Results appear consistent with studies observing kratom use among those with physical and mental health concerns as well as those attempting to stop using specific substances. The study recognizes the propensity of some individuals to use kratom in conjunction with other drugs for euphoric effects.

**ИИ:** разошлись — Opus ? (неясно, оценивали ли зависимость: NSDUH 2023 analysis of kratom use; dependency signs refer to other drugs, unclear whether kratom use disorder was assessed.); Sonnet -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: NSDUH 2023 analysis predicting kratom use from health concerns and difficulty quitting other drugs; no kratom dependence or use disorder measure reported.)

**Решение:** - анализ NSDUH 2023: в анкете нет модуля зависимости от кратома

---

### 40 · R0767

**Kratom a jeho užívání studenty vysokých škol**

2025 · bachelor thesis · ces/cze · http://www.nusl.cz/ntk/nusl-684843

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Czech bachelor thesis on kratom use among university students; no abstract, so it's unclear whether dependence was assessed.

**Решение:** =

---

### 41 · R0768

**Kratom and Its Use by University Students**

2025 · Digital Repository (National Repository of Grey Literature) · dissertation, thesis · cs · https://core.ac.uk/download/663955606.pdf

Katedra biologie a environmentálních studiíPedagogická fakultaFaculty of Educatio

**ИИ:** ? · обе модели · нет аннотации · Czech thesis on kratom use among university students; no usable abstract, so it is unclear whether dependence was assessed.

**Решение:** =

---

### 42 · R0788

**Clinical Outcomes and Healthcare Perspectives on Adolescent Kratom Use in the Czech Republic: A Study Protocol**

2025 · Adiktologie · article · https://doi.org/10.35198/01-2025-001-0002

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; study protocol on adolescent kratom use. It may have no data or a clinically selected sample, so check the full text.

**Решение:** =

---

### 43 · R0792

**Kratom – neue Phytoarzneidroge mit polypharmakologischen Effekten**

2025 · Zeitschrift für Phytotherapie · article, journalarticle, conference-paper · de · https://doi.org/10.1055/s-0045-1811467

Einleitung Die Blätter des Kratom-Baums ( Mitragyna speciosa Korth.) werden traditionell in Südostasien wegen ihrer analgetischen und stimulierenden Effekte genutzt [ 1 ]. In den letzten Jahren wurden zunehmend diverse Kratomprodukte weltweit auf den Markt gebracht [ 2 ]. Diese Produkte unterscheiden sich substanziell, sowohl in ihrer Alkaloidzusammensetzung und -konzentration mit potenziell phytotherapeutischen Effekten als auch bei Nebenwirkungen und Arzneimittelinteraktionen [ 3 ]. Methoden Zwischen 2020 und 2024 wurden 3 Studien in den USA durchgeführt, bei denen eine Kombination von anonymen Umfragen bei Kratombenutzern und LC-MS/MS-Analysen von Kratomprodukten genutzt wurde. Die Umfragen beinhalteten demografische Fragen, die erlebten positiven und negativen Effekte und Nutzprofile von diversen Kratomprodukten (Tee, Kapseln, Pulver, Extrakte). Die Konzentrationen von Mitragynin, 7-Hydroxymitragynin und bis zu 8 anderen Alkaloiden wurden ermittelt. Ergebnisse Von 4044 validierten Kratomnutzern identifizierten sich 70% als männlich, und fast die Hälfte (49,4%) war zwischen 30 und 50 Jahren alt. Am häufigsten wurden Kratomprodukte in Pulverform und als Kapseln verwendet. Über 60% der Benutzer konsumierten Kratom in Dosierungen von 1–5 g bis zu 3 x tägl. Eine positive Korrelation besteht zwischen häufiger Einnahme und Nebeneffekten wie Brechreiz und Konstipation. Kapseln, Tabletten und Gummis waren am häufigsten mit Nebeneffekten verbunden und hatten die höchste Konzentration von Mitragynin. Schlussfolgerung Mit steigender Verfügbarkeit von unterschiedlichen Kratomprodukten in den USA und weltweit ergeben sich neue potenzielle therapeutische Anwendungen und toxikologische Herausforderungen. Das komplexe Alkaloidprofil von Kratom sollte weiter auf pharmakologische Aktivitäten untersucht werden, um es mit neuen Benutzertrends und klinischen Anwendungen zu korrelieren und zu verstehen. Diese Arbeit entstand ohne finanzielle Unterstützung. Publication History Article published online: 08 September 2025 © 2025. Thieme. All rights reserved. Georg Thieme Verlag KG Oswald-Hesse-Straße 50, 70469 Stuttgart, Germany

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Conference abstract pooling three US surveys of 4044 kratom users; negative effects were assessed, but it doesn't say whether dependence was measured.

**Решение:** =

---

### 44 · R0815

**At least four groups of kratom consumers in the United States: latent-class analysis of motivations for kratom use.**

2025 · The American journal of drug and alcohol abuse · article, journal article, research support, n.i.h., intramural · eng · https://doi.org/10.1080/00952990.2024.2414319

Background: Kratom is a plant with alkaloids acting at opioid, serotonergic, adrenergic, and other receptors. Consumers report numerous use motivations. Objectives: To distinguish subgroups of kratom consumers by kratom-use motivations using latent-class analysis. Methods: From July to November 2022, we utilized convenience sampling and surveyed regular kratom consumers ( n = 395, 38.1 years (SD 11.2), 54.9% male, 81.3% White) regarding demographics, lifetime and past-year substance use and preferences, substance use disorder history, healthcare barriers, kratom-use motivations, and general health. We used latent-class analysis to identify subgroups by use motivation and calculated conditional probabilities (P c ) for variables in each class. Results: A four-class model best fit our data. The largest class (32.4%) was characterized by the use of kratom for self-treatment of chronic pain (P c = .91). The smallest class (19.2%) also reported using kratom for self-treatment, but usually as a long-term replacement for other substances (P c = .75). The other two classes (24.8% and 23.5%) reported using kratom for management of anxiety (P c = .87-.95) and depressive symptoms (P c = .61-.89) and for recreation (P c = .56- .86). These were distinguished from one another by probability of at least moderate kratom use disorder (P c = .17 vs. .53), with greater probability observed in the class with greater anxiety (P c = .13 vs. .50) and depressive (P c = .34 vs. .82) symptom severity and more likely recreational use motivation (P c = .56 vs. .86). Conclusion: Kratom consumers can be classified by their use motivations. As with other psychoactive substances, the range of motivations is consistent with the range of likely effects. It is not yet clear whether some motivations might indicate the risk of problems.

**ИИ:** + · обе модели · употребляющие + мера зависимости · Survey of 395 regular US kratom consumers that assessed kratom use disorder severity, with at least moderate KUD reported by latent class.

**Решение:** =

---

### 45 · R0816

**Clinically characterizing adults who use kava or kratom: Substance use disorder assessment challenges for increasingly popular botanical products.**

2025 · Drug and alcohol dependence reports · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.dadr.2025.100394

Background Kratom ( Mitragyna speciosa ) and kava ( Piper methysticum ) are psychoactive botanicals with growing popularity We aimed to characterize the clinical characteristics of people who have consumed these products. Methods We conducted an online survey of US adults who have used kava or kratom. Diagnostic and Statistical Manual-5 (DSM-5) substance use disorder (SUD) criteria were used to assess symptoms related to past-year kratom and/or kava use. Respondents were also asked to report on the compatibility of kava and kratom effects with daily living. Results Of the 367 participants, 91.3 % reported lifetime kratom use and 49.0 % reported lifetime kava use. There was substantial overlap of lifetime use of both substances (40.3 %). Past-year SUD diagnostic criteria for kratom were met by 38.1 % of participants; when this group was dichotomized by past-year kava use, those who also co-used kava had higher proportions of endorsing symptoms of "using more kratom than intended" and "needing to use larger amounts to feel the same effect" than those who used kratom without kava (p = 0.032 and p = 0.011, respectively). Meeting SUD criteria for kava was uncommon among those reporting past-year use (7.5 %), regardless of past-year kratom use. Kratom effects were perceived as helpful and compatible with daily living, though fewer reported this for kava effects. Conclusions Assessment of patients using kratom or kava may become challenging due to co-use. The relative rewarding and reinforcing effects of these botanicals alone or combined requires systematic study. SUD for either is possible but should be contextualized by patient-level factors including other substance use.

**ИИ:** + · обе модели · употребляющие + мера зависимости · Online survey of US adults who use kava or kratom; DSM-5 SUD criteria for kratom met by 38.1% in the past year.

**Решение:** =

---

### 46 · R0828

**Altered effective connectivity within the default mode network in kratom (Mitragyna speciosa) users: A resting-state fMRI study**

2025 · Neuroscience Research Notes · article, journalarticle, journal-article · en · https://doi.org/10.31117/neuroscirn.v8i3.400

Kratom (Mitragyna speciosa) is a Southeast Asian plant with stimulant and opioid-like properties, traditionally used for its medicinal effects. However, its increasing popularity and potential for dependence raise concerns about its impact on brain function. This study investigated alterations in effective connectivity (EC) within the default mode network (DMN), a network associated with self-related processes, in kratom users compared to healthy controls. Ten regular kratom users (mean age: 27.30 ± 3.97) and seven healthy controls (mean age: 20.72 ± 1.88) underwent resting-state functional magnetic resonance imaging (rs-fMRI). The EC analyses were performed using spectral dynamic causal modelling to examine directional influences between DMN regions. A fully connected model best represented EC in both groups; however, the control group lacked a significant connection between the right inferior parietal cortex (RIPC) and the posterior cingulate cortex (PCC). Kratom users exhibited hyperconnectivity between the medial prefrontal cortex (MPFC) and the left inferior parietal lobule (LIPL) connection compared to controls. Additionally, negative correlations were identified between the duration of kratom use and connectivity from PCC to RIPC. In contrast, positive correlations were observed between the duration of use and connectivity from RIPC to PCC. These findings suggest that kratom consumption may alter EC within the DMN, particularly the MPFC→LIPL connection, potentially due to chronic intake. This preliminary study provides neuroimaging insights into the effects of kratom on the brain and contributes to ongoing discussions regarding its potential for dependence and therapeutic applications.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · fMRI study of 10 regular kratom users; the abstract doesn't say whether dependence was measured, but the sample table might report it.

**Решение:** =

---

### 47 · R0841

**ปัจจัยทำนายพฤติกรรมการใช้กระท่อมของวัยรุ่นในเขตอำเภอเมือง จังหวัดนครราชสีมา**

2025 · THE JOURNAL OF PSYCHIATRIC NURSING AND MENTAL HEALTH · article · th

Objective: To study the factors that influence Teenagers' Kratom use behavior in the district of Mueang, Nakhon Ratchasima Province. Methods: The study participants were 136 Teenagers with Kratom use behavior in the district of Mueang, Nakhon Ratchasima Province, by purposive sampling. The research instrument consisted of three questionnaires; 1) demographic questionnaires 2) measures of knowledge, attitudes, motivation, media exposure and 3) measures of the Kratom use behavior. The data were analyzed by the Descriptive statistics, Pearson's product - moment correlation, and Multiple linear Regressions. Results: The results showed that Teenagers' Kratom use behavior in the district of Mueang, Nakhon Ratchasima province. The average score of knowledge was in the medium level (mean = 9.85, S.D. = 1.92), a medium level of attitudes (mean = 3.42, S.D. = 0.46), a high level of motivation (mean = 3.53, S.D. = 0.75), a high level of media exposure (mean = 3.60, S.D. = 0.70) and a medium level of Kratom use behavior (mean = 2.96, S.D. = 0.97. The attitudes, motivation, media exposure, and Kratom use behavior were significantly positively related (r = .570, .699, .519, p < .01 respectively). The knowledge, attitudes, motivation, and media exposure could jointly predict the Kratom use behavior among Teenagers accounted for 52.90 % of the variance with a statistical significance at the .01 level (R2 = .529, p < .01). The most influential variable was motivation (Beta = .532, p < .01), followed by attitudes (Beta = .202, p < .01). Conclusion: Motivational factors and attitudinal factors influence kratom use behavior among adolescents. If adolescents reduce their motivation and adjust their attitudes towards kratom use, it can lead to a reduction in kratom use behavior. This can lead to planning for the prevention of kratom use behavior among adolescents in the future.

**ИИ:** разошлись — Opus ? (неясно, оценивали ли зависимость: Survey of 136 teenagers who use kratom; the 'kratom use behavior' scale is not described and might include dependence items.); Sonnet -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: Survey of 136 adolescent kratom users on knowledge, attitudes, motivation and use behavior; no dependence or use-disorder measure apparent.)

**Решение:** ? опрос 136 подростков-потребителей кратома в Таиланде: шкала поведения может включать зависимость

---

### 48 · R0842

**Mapping Addictive Behaviors and Preventive Activities Among Students From Masaryk University: Preliminary Results**

2025 · The Paris Conference on Education, official conference proceedings · conference-paper · en · https://doi.org/10.22492/issn.2758-0962.2025.67

The life of university students is often viewed as a time of experimenting with different kinds of behaviors that may be risky.However, university students are usually not considered a highrisk group for problems related to substance use disorder.With this assumption, the support for students struggling with addiction may be insufficient.We are therefore conducting exploratory research to map the extent of this risky behavior as well as the students' experiences with preventive activities at Masaryk University (MU) in the Czech Republic.The ongoing study is conducted through a quantitative survey.We draw from questionnaires from previous similar studies at Masaryk University together with standardized ESPAD questionnaire.These materials were adjusted to fit the university environment and current trends in addictive behavior.With the usage of snowball sampling, students from all ten faculties of MU were invited to participate.The final sample consists of 1,214 students, mostly from the Faculty of Education.Regular use (a few times a month and more often) was stated most frequently for alcohol (52.1%).Regarding other drugs, the regular use occurred also in nicotine (28.3%),THC (3.8%), kratom (2.1%) and other drugs (each < 1%).Conversely, the experience with prevention at university was stated only by 5.6% of students.These preliminary results indicate that the need for preventive activities may largely exceed the prevention that is offered to students.The final results could therefore serve as the next step for creating a more effective support system.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · University student survey reports kratom use frequency; abstract doesn't say whether kratom dependence or use disorder was assessed.

**Решение:** =

---

### 49 · R0873

**Polysubstance use patterns among individuals applying for opioid-use disorder treatment in the U.S.**

2025 · Journal of Substance Use · article · https://doi.org/10.1080/14659891.2024.2372093

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. Polysubstance survey of OUD treatment applicants may have assessed kratom use and dependence; check full text.

**Решение:** =

---

### 50 · R0911

**Is bedtime use of kratom (Mitragyna speciosa) a sleep aid or disruptor? Examining its daily effects and individual differences.**

2025 · Experimental and clinical psychopharmacology · article, journal article, journalarticle · eng · https://doi.org/10.1037/pha0000794

Kratom ( Mitragyna speciosa ) is a psychoactive botanical native to Southeast Asia increasingly used in the United States for various self-reported benefits, including sleep improvement. However, empirical evidence concerning kratom's effects on sleep is limited. Here, we examined the association between bedtime kratom use and self-reported sleep outcomes in naturalistic settings across consecutive days, while also exploring sex and chronic pain status as potential moderators. A secondary analysis was conducted using the data from a 15-day ecological momentary assessment study of 357 U.S. adults who reported regularly using kratom. Participants made daily reports of their bedtime kratom use and rated their sleep duration and quality. Linear mixed-effects models assessed associations between bedtime kratom use and sleep outcomes, with sex and chronic pain status as moderators, controlling for age. Bedtime kratom use occurred on 23.4% of days and was associated with modest increases in sleep duration (13 min) and perceived quality (5.93-point increase on a 0-100 scale). Female respondents reported greater improvements in sleep quality (but not duration) than male respondents. Participants with chronic pain reported greater improvements in sleep duration and quality compared to those without chronic pain. Bedtime kratom use is associated with modest sleep duration and quality improvements, particularly in adults with chronic pain, and better sleep quality in female respondents. These findings among experienced kratom consumers suggest the need for human laboratory studies in kratom-naïve participants to determine causality and underlying mechanisms, which could help inform clinical guidance and policy as kratom use continues to rise. (PsycInfo Database Record (c) 2025 APA, all rights reserved).

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · EMA study of 357 regular US kratom users; the abstract doesn't say whether use disorder was assessed, but the parent study may report DSM-5 criteria.

**Решение:** =

---

### 51 · R0912

**Kratom (Mitragyna speciosa) use for self-management of pain: Insights from cross-sectional and ecological momentary assessment data.**

2025 · The journal of pain · article, journal article, research support, n.i.h., extramural · eng · https://doi.org/10.1016/j.jpain.2024.104726

Kratom (Mitragyna speciosa) is increasingly used in the US for self-management of pain, despite limited research on its efficacy and safety. To better understand how and why people use kratom for pain self-management, we analyzed baseline survey data (N = 395) and 15-day ecological momentary assessment (EMA) data (N = 357) from kratom consumers across the US. Although we recruited participants based on their kratom use, not on whether they used it for pain management, nearly half (49.1 %) met criteria for chronic pain, with many reporting substantial pain relief and high effectiveness of kratom in managing pain. A majority (69.2 %) reported difficulties in obtaining adequate pain treatment, and most indicated that these challenges impacted their decision to try kratom. Most participants did not report concerns about overuse or significant side effects. EMA data showed that, regardless of chronic-pain status, pain relief was the most frequently endorsed primary motivation for daily kratom use. There were no significant association between daily pain levels and kratom use frequency, and no difference in the daily kratom use between those with vs. without chronic pain. Recent kratom use was associated with lower current pain levels. Stronger subjective effects of kratom were associated with lower pain levels. This effect was significantly moderated by chronic-pain status: those with chronic pain showed a stronger link between subjective kratom effects and pain reduction. These findings underscore the urgent need for systematic, rigorous research on long-term implications, efficacy, and safety of kratom in pain management to guide informed clinical practices and regulatory policies. PERSPECTIVE: This study reveals that chronic pain is common among kratom consumers, who frequently use it for pain self-management and report significant relief, as shown by ecological momentary assessment. There is an urgent need for research into kratom's safety, efficacy, and mechanisms to guide clinical practice and inform policies.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · US baseline survey and EMA study of kratom consumers. The abstract doesn't say whether kratom use disorder criteria were assessed, but the baseline table may report them.

**Решение:** =

---

### 52 · R0922

**Substance use in the conscripts affiliated with the fort Ratchaburi Province**

2025 · Journal of Medical Bioscience · article · en · https://doi.org/10.58837/chula.jmbs.7.1.7

Background: Substance use problems impact both physical and mental health, spreading to many areas, including military forts, which represent the strength and stability of the nation. Objective: This study aimed to investigate the prevalence, behavior, attitudes, and factors related to substance use among the conscripts affiliated with the Fort Ratchaburi Province. Methods: A cross-sectional study collected data from 400 conscripts between July - September 2023 using questionnaires through individual interviews. The questionnaires included: 1) demographic information; 2) attitudes towards substance use; 3) The alcohol, smoking and substance involvement screening test; 4) The Thai substance use disorder screening test. A urine toxicology test was conducted for cannabis, opioid, and methamphetamine. The data were analyzed using descriptive and inferential statistics. Results: The prevalence of substance use, at least once in the lifetime and in the past three months, was 86.7% (n = 347) and 71.5% (n = 286), respectively. The five substances with the highest usage in the past three months were alcohol (54.0%), tobacco (53.3%), kratom leaves (33.3%), cannabis (30.8%), and mixtures of kratom leaf decoction (22.0%). Of 254 conscripts who used tobacco, 210 (82.7%) and 6 (2.4%) were found to be at moderate and high risk, respectively, of having tobacco problem. Substance use disorder (SUD) was found in 76.8%, 37.4%, 37.4%, 34.1%, 27.3, 26.7% of conscripts who used tobacco, alcohol, cannabis, kratom leaves, mixtures of kratom leaf decoction and amphetamine-type stimulants, respectively. The attitudes of the conscripts are mostly not aligned with substance use. Low educational level and income sufficiency were identified as factors associated with and predictors of substance use (P < 0.05). Conclusion: Most conscripts used substances. Although the majority of substances used in this study are legal, high prevalence of SUD was found, especially tobacco use disorder in conscripts who smoked cigarettes. Factors related to substance use include low level of education and income sufficiency.

**ИИ:** + · обе модели · другая выборка, есть употребляющие и мера зависимости · Survey of conscripts that used ASSIST and a Thai SUD screening test; it reports SUD in 34.1% of kratom leaf users and 27.3% of kratom cocktail users.

**Решение:** =

---

### 53 · R0945

**Association of behavioral economic demand for kratom with DSM-5 use disorder: quantity and likelihood-based demand approaches.**

2025 · Addictive behaviors reports · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.abrep.2025.100638

• Hypothetical purchase tasks can quantify the reinforcing efficacy of kratom. • Individual kratom demand is sensitive to recent, but not lifetime, kratom use disorder. • Quantity- and Likelihood-based purchase tasks capture different aspects of demand. Kratom products have increased in popularity in the United States due to their availability and their purported analgesic and stimulatory properties. We sought to examine if behavioral economic demand procedures widely used in addiction science would identify indicators of problematic kratom use and to evaluate the relative performance of differing demand approaches. Respondents with a lifetime history of kratom use (N = 117) completed two versions of a hypothetical kratom purchase task. The first version (“Quantity”) followed typical purchase task methods; respondents were asked how much kratom they would purchase across various prices. The second version (“Likelihood”) asked how likely respondents would be to purchase a single dose of kratom across the same price range. Logistic regression was used to determine the association of demand indices with the likelihood of meeting KUD criteria. For the Quantity version, higher demand intensity (OR = 2.16, p = 0.01) and lower demand elasticity (OR = 0.45, p = 0.01) were significantly associated with past year but not lifetime KUD ( p ’s > 0.10). For the Likelihood version, demand intensity, demand elasticity, and Pmax were not associated with KUD ( p ’s > 0.10); higher breakpoint was associated with past year, but not lifetime KUD (OR = 1.44, p = 0.04). This study is the first to demonstrate that purchase tasks can quantify the reinforcing efficacy of kratom and emphasizes the temporal specificity of the association between purchase tasks and problem behaviors. These findings also suggest that demand indices from Quantity- and Likelihood-based tasks differentially relate to KUD, emphasizing the importance of task and outcome selection.

**ИИ:** + · обе модели · употребляющие + мера зависимости · 117 people with lifetime kratom use were assessed for DSM-5 kratom use disorder, both past-year and lifetime.

**Решение:** =

---

### 54 · R0946

**Kratom use among ethnobotanical tea bar patrons in Colorado: Subjective drug effects, adverse reactions, and perceived benefits of use**

2025 · Center for Open Science · posted-content · https://doi.org/10.31219/osf.io/c4qvt

Introduction: Kratom use is increasing in the US, yet data characterizing use patterns, risks, and benefits is limited. Additionally, there are few data on the acute subjective effects of kratom in humans, and no studies to-date have examined kratom use within US public consumption settings, which have become increasingly popular in recent years. Methods: We administered surveys to 102 ethnobotanical tea bar patrons in northern Colorado. Surveys assessed demographic information, kratom use patterns, perceived benefits, and adverse reactions. We also assessed subjective drug effects acutely after participants consumed kratom at the bars. Data were analyzed using a mixed-methods approach.Results: Participants (mean age=22.34 years, 39.2% women), reported frequent kratom use (73.4% endorsed weekly use, 19.3% endorsed daily use). Reported benefits included mental and physical health benefits, social enhancement, and substance use harm reduction. Adverse reactions primarily involved gastrointestinal issues, though acute psychological effects (e.g., anxiety), and withdrawal symptoms were also cited. Kratom use in a bar setting was associated with acute stimulation and mild euphoria, and minimal sedation.Conclusions: Kratom use at ethnobotanical tea bars is increasingly common in the US. While most participants reported perceived benefits, the presence of adverse reactions highlight the need for more data on safety and risks of kratom use, particularly in social use spaces. Results also highlight the possible role of kratom in supporting non-abstinent recovery.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of 102 kratom tea bar patrons; withdrawal symptoms mentioned, but the abstract doesn't say whether dependence or use disorder was assessed.

**Решение:** =

---

### 55 · R0947

**Kratom use among ethnobotanical tea bar patrons in Colorado: Subjective drug effects, adverse reactions, and perceived benefits of use.**

2025 · Drug and alcohol dependence reports · article, preprint, journal article · eng · https://doi.org/10.1016/j.dadr.2025.100361

Introduction: Kratom use is increasing in the US, yet data characterizing use patterns, risks, and benefits is limited. Additionally, there are few data on the acute subjective effects of kratom in humans, and no studies to-date have examined kratom use within US public consumption settings, which have become increasingly popular in recent years. Methods: Using field methods, we administered surveys to 102 ethnobotanical tea bar patrons in northern Colorado. Surveys assessed demographic information, kratom use patterns, perceived benefits, and adverse reactions. We also assessed subjective drug effects acutely after participants consumed kratom at the bars. Data were analyzed using a mixed-methods approach. Results: Participants (mean age=22.34 years, 39.2 % women), reported frequent kratom use (73.4 % endorsed weekly use, 19.3 % endorsed daily use). Reported benefits included mental and physical health benefits, social enhancement, and substance use harm reduction. Adverse reactions primarily involved gastrointestinal issues, though acute psychological effects (e.g., anxiety), and withdrawal symptoms were also cited. Kratom use in a bar setting was associated with acute stimulation and mild euphoria, and minimal sedation. Conclusions: While most participants reported perceived benefits, the presence of adverse reactions highlight the need for more data on safety and risks of kratom use, particularly within public consumption spaces. Results also highlight the possible role of kratom in supporting substance use disorder recovery, with some ethnobotanical tea bars potentially functioning as recovery spaces.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of 102 kratom tea bar patrons that mentions withdrawal; the abstract does not say whether dependence or use disorder was assessed.

**Решение:** =

---

### 56 · R0957

**Mental effects and potential therapeutic use of kratom/mitragynine**

2025 · Research Publications (Maastricht University) · doctoral thesis, dissertation, thesis · en · https://doi.org/10.26481/dis.20250310ep

Kratom (Mitragyna speciosa) is a traditional Southeast Asian plant used medicinally since the 19th century. Recently, leaf extract products have become popular in Europe and the US, where the FDA classifies them as “new dietary ingredients” due to insufficient safety data. People worldwide use kratom to self-treat issues like pain, substance abuse, and mental health symptoms, with some using it for performance enhancementzwien and recreational purposes. Its main active compound, mitragynine, interacts with various opioid and non-opioid receptors in the nervous system. Many serious safety concerns have been linked to drug interactions, mainly reported in the West. Despite its global use and anecdotal evidence of benefits, there are few controlled clinical and toxicological studies in humans. More research is needed to clarify kratom’s safety, behavioral effects, therapeutic potential, and addictive risks. Understanding its benefits and risks is essential for informed use and policy. Thus, this thesis aimed to enhance understanding of kratom/mitragynine use and their behavioral effects by means of two literature reviews, a netnographic analysis, two online studies, and a placebo-controlled single-blind experimental study.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Thesis includes two online studies of kratom users; the abstract doesn't say if dependence or use disorder was assessed.

**Решение:** =

---

### 57 · R0977

**ประสิทธิภาพของการคัดกรองและการบำบัดแบบย่อสำหรับความเสี่ยงจากการใช้สารเสพติดและความเครียดในทหารเกณฑ์ สังกัดหน่วยทหารในจังหวัดปราจีนบุรี**

2025 · Journal of Dhamma for Life · article · th

This research is descriptive research with the objective to study potential efficacy of brief intervention for risk of substance use among Thai conscipts in Prachinburi Province, to study the factors that are related to the substance use behavior of conscripts under the military unit in Prachinburi province and to compare stress and substance use behavior before and after the abbreviated therapy of conscripts Under the military unit in Prachinburi Province. Collect data from conscripts under the military unit of Prachinburi province who use drugs and are at risk of using drugs who have been drafted for a period of more than 3 months by collecting data 2 times (before and after brief intervention). The research tools used include a general information questionnaire, stress assessment form, Alcohol, Smoking, and Substance Involvement Screening Test (ASSIST). The statistics used in the analysis are descriptive statistics and inferential statistics The results of the study showed that at least one substance use behavior (before and after brief intervention) 100.00 and 64.40 percent, respectively, which showed the effectiveness of brief intervention. The top 2 most used buses are alcoholic beverages, tobacco products, kratom and cocktail. There is a moderate risk. Most of the samples have a high level of pre-level of brief intervention (35.60 percent). After brief intervention, a low level of stress (51.10 percent). From the hypothesis test, it was found that stress is related to the drug use behavior of conscripts. The drug use behavior of conscripts under the military unit in Prachinburi Province decreased after receiving brief intervention statistically significant at the level of 0.05

**ИИ:** разошлись — Opus + (другая выборка, есть употребляющие и мера зависимости: Thai conscripts who use substances were screened with ASSIST; kratom and kratom cocktail use were reported with moderate risk scores.); Sonnet ? (неясно, оценивали ли зависимость: Thai conscripts screened with ASSIST; kratom and cocktail among top substances, but unclear whether kratom-specific ASSIST risk levels are reported. Full text needed.)

**Решение:** + скрининг тайских призывников по ASSIST: оценка риска и зависимости от кратома

---

### 58 · R1007

**Chemical Analysis and Alkaloid Intake for Kratom Products Available in the United States.**

2025 · Drug testing and analysis · article, journal article, journalarticle · eng · https://doi.org/10.1002/dta.3906

ABSTRACT Previously, we used ecological momentary assessment (EMA) to evaluate motivations and temporal patterns of kratom use for 15 days among US adult kratom consumers ( N = 357). Here we present the content analyses of the products used during that nationwide study, with quantification of 10 kratom alkaloids. The samples ( N = 341) were primarily whole‐leaf products, not extracts, and were similar to each other in their alkaloid composition, closely matching the chromatographic‐mass spectrometry fingerprint expected for Mitragyna speciosa leaf material. We found no evidence of adulteration with illicit or prescription drugs. With participants' self‐reported data on kratom amount per use, we calculated mitragynine intake per use: mean 31.3 mg and median 25.4 mg (range 2.0–205.9 mg). With self‐reported data on frequency, we calculated mitragynine intake per day, it ranged from 78.3 to 134.6 mg (mean) or 50.8 to 101.6 mg (median). This is the most comprehensive analysis of US whole‐leaf kratom products to date. The coupling of self‐report and product sample‐analysis data to quantify daily alkaloid intake is foundational for designing controlled clinical trials of kratom in healthy volunteers. These findings on kratom products' chemical composition and daily kratom alkaloid consumption can also inform clinicians, policymakers, and consumers, particularly for whole‐leaf material.

**ИИ:** разошлись — Opus ? (неясно, оценивали ли зависимость: Mostly product analysis, but it links to an EMA sample of 357 US kratom consumers; the sample table might report use-disorder criteria.); Sonnet -2 (качественное исследование без подсчёта людей (интервью, форумы, Reddit); доклиника: животные, клетки, химия, ботаника, анализ продуктов: Analytical product-testing study quantifying alkaloids in kratom samples; no dependence or use-disorder measure in the abstract (dependence data would be in the separate parent EMA paper).)

**Решение:** - аналитический анализ образцов продуктов, не эпидемиологический опрос

---

### 59 · R1010

**Characteristics of kratom and its use in the world and in the Czech Republic**

2025 · Digital Repository (National Repository of Grey Literature) · dissertation, thesis · cs · https://core.ac.uk/download/674778918.pdf

Shelkouskaya, J.: Characteristics of kratom and its use in the world and in the Czech Republic. Diploma thesis, Charles University in Prague, Faculty of Pharmacy in Hradec Králové, Department of Biological and Medical Sciences, Hradec Králové, 2025 Kratom (Mitragyna speciosa) is a plant native to Southeast Asia, traditionally used to relieve various health conditions and as a stimulant to enhance physical performance. In some cases, it has even been considered a potential substitute for opium. Kratom belongs to the genus Mitragyna, which also includes species found in other regions such as Africa and other parts of Asia, highlighting its biological diversity. From its native regions, kratom is exported to Europe and the United States, where it is widely available through both physical stores and online retailers. In these markets, kratom is primarily consumed for its psychoactive effects. According to vendors, different strains of kratom are associated with distinct effects, largely determined by the concentration of its main active alkaloids - mitragynine and 7- hydroxymitragynine. From a legal perspective, regulations on kratom vary widely across countries. In some, it is fully legal; in others, its use is restricted or entirely banned. This variation reflects ongoing concerns regarding its...Shelkouskaya, J.: Charakteristika kratomu a jeho využití ve světě a v ČR. Diplomová práce, Univerzita Karlova v Praze, Farmaceutická fakulta v Hradci Králové, Katedra biologických a lékařských věd, Hradec Králové, 2025 Kratom (Mitragyna speciosa) je rostlina pocházející z jihovýchodní Asie. V tradiční medicíně se využívá ke zmírňování různých zdravotních obtíží a jako stimulant pro zvýšení pracovní výkonnosti. V některých případech je dokonce považován za potenciální lék u závislosti na opiu. Kratom náleží do rodu Mitragyna, přičemž další druhy tohoto rodu lze nalézt také například v Africe a jiných částech Asie, což podtrhuje jeho biologickou rozmanitost. Ze své oblasti původu je kratom exportován do Evropy a USA, kde existuje rozsáhlá síť obchodů a e- shopů nabízejících různé varianty tohoto produktu. Zde se kratom především používá pro jeho psychoaktivní účinky. Podle prodejců každá varianta vykazuje specifické účinky, jež jsou úzce spojovány s obsahem hlavních aktivních složek - alkaloidů mitragyninu a 7- hydroxymitragyninu. Z právního hlediska se legislativní přístupy ke kratomu liší napříč kontinenty - zatímco v některých zemích je neregulovaný (legální; látka není výslovně zakázána ani regulována), v jiných zemích je kontrolovaný (látka je povolena jen za určitých podmínek, např. pro...Katedra biologických a lékařských vědDepartment of Biological and Medical SciencesFaculty of Pharmacy in Hradec KrálovéFarmaceutická fakulta v Hradci Králov

**ИИ:** ? · обе модели · другое · The thesis reads mostly like a review, but the abstract is cut off and it might include a Czech survey of people who use kratom.

**Решение:** =

---

### 60 · R1016

**High-risk sexual behavior among Malaysian adolescents who use drugs: a mixed-methods study of a sample in rehabilitation**

2025 · Journal of Substance Use · article · https://doi.org/10.1080/14659891.2024.2329885

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract. Malaysian adolescent drug-user samples often include kratom users; unclear whether kratom dependence was assessed.); Sonnet -6 (не про кратом (другие виды Mitragyna) или не про людей, которые его употребляют: No abstract; title concerns sexual risk behavior in adolescents in drug rehabilitation, with no mention of kratom or kratom dependence.)

**Решение:** - подростковая реабилитационная выборка: фокус на сексуальном поведении риска

---

### 61 · R1017

**Kratom (Mitragyna speciosa) use in a sample of drug-dependent adolescents in rehabilitation for drug use in Malaysia.**

2025 · Journal of ethnicity in substance abuse · article, journal article, journalarticle · eng · https://doi.org/10.1080/15332640.2023.2293941

Abstract Background Leaves derived from the Kratom (Mitragyna speciosa) tree have been traditionally ingested for their curative properties by diverse groups of the population including people who use drugs (PWUDs) in Southeast Asia. This study investigated the motives for using kratom among drug-dependent adolescents. Methods Eighty adolescents who were undergoing mandatory drug rehabilitation volunteered to participate in this mixed-method, cross-sectional study. All respondents answered a semi-structured questionnaire while a few were interviewed in-depth. Results The majority were males (70%, n = 56/80). The respondents’ mean age at admission was 18.2 years (SD = 1.40), and 65% were between 14 and 18 years old. Sixty-three percent (n = 50/80) had used crystal methamphetamine alone, while the rest had co-used crystal methamphetamine with heroin. About three-fifths (60%, n = 48/80) had a history of kratom use. Kratom was commonly used for many perceived benefits such as increasing energy, reducing crystal methamphetamine intake, intensifying euphoria, easing heroin withdrawal, as a heroin substitute and reducing heroin use. In addition, the multivariate analysis indicated that higher odds of kratom use were associated with those who were employed, used only crystal methamphetamine, were recent drug users, and had no prior incarceration history. Conclusion While kratom was being used for its multifold perceived benefits, it also functions as a means to self-treat withdrawal from illicit drug use among drug-dependent adolescents.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Adolescents in rehab for meth/heroin, 48 had used kratom. The abstract covers motives only, so it's unclear whether kratom dependence was assessed.

**Решение:** =

---

### 62 · R1022

**Kratom use in the Czech Republic**

2025 · Hygiena · article, journalarticle, journal-article · cs · https://doi.org/10.21101/hygiena.a1898

Cl: Clem studie bylo zmapovat uvn kratomu v populaci star 15 let v esk republice. Kratom je psychoaktivn ltka, jej uvn v poslednch letech vrazn narst. Metodika: Sbr dat probhal v rmci Nrodnho vzkumu uvn tabku a alkoholu v esk republice (NAUTA) v letech 2023 a 2024. Pouita byla metoda dotaznkovho eten formou standardizovanho rozhovoru mezi tazatelem a respondentem, kter umonila sledovat mru uvn kratomu v obecn populaci. Vyhodnocen je zaloeno na celkov prevalenci souasnho uvn kratomu, tj. podlu dennch a pleitostnch uivatel, a na denn prevalenci, tj. podlu osob, kter kratom v souasnosti uvaj kad den. Vsledky: Do eten se zapojilo 1 812 respondent v roce 2023 a 1 809 respondent v roce 2024. Celkov prevalence souasnho uvn kratomu doshla 0,8 % v roce 2023 a 2,0 % v roce 2024. Podl pravidelnch dennch uivatel byl nzk, avak meziron vzrostl z 0,1 % na 0,3 %. Nejvy prevalence souasnho uvn byla zaznamenna ve vkov skupin 15-24 let, v n dolo k nrstu z 3,2 % na 4,5 %. Mui vykazovali vy prevalenci ne eny. Kratom alespo jednou za ivot uilo 11,0 % mu oproti 7,6 % en, piem ve vkov skupin 15-24 let jej uila piblin tvrtina respondent. Nejastjm zpsobem zskn kratomu byl nkup prostednictvm e-shopu (tm 40 % uivatel). Vrazn vzrostl podl uivatel, kte vyuili nkupn automat, a to z 11,4 % v roce 2023 na 23,6 % v roce 2024. Zvr: Studie ukazuje zeteln nrst souasnho uvn kratomu v esk republice mezi lety 2023 a 2024, zejmna u mladch osob ve vku 15-24 let. Souasn potvrdila vysokou dostupnost tto ltky v situaci absence legislativn regulace, a to i pro nezletil. Vsledky zdrazuj nutnost sledovat vvoj uivatelskch trend i po zaveden novch opaten, konkrtn po zaveden regulace kratomu jako psychomodulan ltky.

**ИИ:** разошлись — Opus -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: Czech national population survey (NAUTA) reporting only current or daily kratom use prevalence and purchase sources; no dependence measure described.); Sonnet ? (неясно, оценивали ли зависимость: Czech national population survey (NAUTA) of kratom use; abstract reports prevalence and acquisition only, so it is unclear whether dependence was assessed.)

**Решение:** - опрос взрослого населения в Чехии: только доля употребления (1,6%), без меры зависимости

---

### 63 · R1055

**ปัจจัยที่มีผลต่อระดับสารบ่งชี้ทางชีวภาพของระบบทางเดินอาหารในผู้บริโภคพืชกระท่อมเพศชายในพื้นที่สามจังหวัดชายแดนภาคใต้ประเทศไทย: การศึกษาด้านระยะเวลาและปริมาณในการบริโภค**

2025 · Journal of the Medical Technologist Association of Thailand · article · th

The objective of this study was to investigate the effects of both the duration and quantity of kratom consumption on gastrointestinal biomarkers among 87 male participants residing in three southern border provinces of Thailand. This cross-sectional study employed interviews and blood samples for analysis of carcinoembryonic antigen (CEA), alpha-fetoprotein (AFP), carbohydrate antigen 19-9 (CA19-9), aspartate transaminase (AST), alanine transaminase (ALT), alkaline phosphatase (ALP), amylase, and erythrocyte sedimentation rate (ESR). The results indicated that individuals who consumed kratom exhibited a higher average ESR than the established reference value, whereas the mean values of the other biomarkers remained within the reference range. Comparison analysis revealed no statistically significant difference between the monitored biomarkers in term of the quantity (< 40 vs. ≥ 40 leaves per day), frequency (< 10 vs. ≥ 10 times per day), and number of glasses (< 8 vs. ≥ 8 glasses per day) of kratom consumed. When considering the correlations between period of consumption and biomarker levels, the study found that the AST level was inversely correlated with the consumption period (p = 0.02) without clinical significances. In contrast, other biomarkers were not significantly correlated. Nevertheless, it is recommended that kratom consumers strictly adhere to the guidelines set by the Ministry of Public Health regarding appropriate consumptions and utilizations of kratom as an herbal remedy.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Cross-sectional study of 87 male kratom users using interviews; abstract does not say whether dependence was assessed.

**Решение:** =

---

### 64 · R1076

**Association of mitragynine levels with lipid profiles in regular kratom (Mitragyna speciosa) users**

2025 · Medicine in Drug Discovery · article, journalarticle, journal-article · en · https://doi.org/10.1016/j.medidd.2025.100241

• Kratom users showed lower LDL, urea, creatinine, and higher eGFR than non-users. • Serum mitragynine correlated negatively with LDL and TG levels. • Most users consumed kratom for health, often > 21 leaves daily in concentrated brews. Kratom ( Mitragyna speciosa ) is widely consumed in Southeast Asia for both medicinal and recreational purposes, yet its impact on human health remains unclear. This study examined sociodemographic factors, consumption patterns, serum mitragynine (MG) levels, and clinical chemistry parameters among 90 male participants from the Putussibau District, West Kalimantan, Indonesia. Participants were categorized into kratom users (n = 64) and non-users (n = 26). The majority of users indicated that they consumed kratom for health-related reasons, most commonly for 2–5 years, and nearly half reported daily intake exceeding 21 leaves. Serum MG concentrations were significantly higher among users than non-users, although no associations were observed with duration or intensity of consumption. Clinical chemistry analysis revealed that kratom users had lower levels of LDL, BUN, urea, and creatinine, alongside higher eGFR values, while no significant differences were detected in liver enzymes, glucose, HDL, triglycerides, or inflammatory markers. Notably, serum MG was negatively correlated with LDL and triglyceride levels. Stratified analysis indicated that long-term use was associated with favorable hepatic and lipid profiles, suggesting possible adaptive metabolic responses, whereas higher daily intake produced mild, subclinical elevations in liver and renal markers. Additionally, systemic inflammation, reflected by increased hsCRP and IL-6, was linked to self-reported anxiety, highlighting a potential peripheral mechanism connecting kratom use to central nervous system (CNS) effects. Overall, these findings suggest that regular kratom use may elicit adaptive physiological changes with minimal biochemical perturbation at moderate intake levels. Further longitudinal and mechanistic studies are warranted to clarify causal pathways and long-term health implications of kratom use.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of 64 regular kratom users in Indonesia with a consumption questionnaire; the abstract doesn't say whether dependence was assessed.

**Решение:** =

---

### 65 · R1082

**Kratom's Use and Impact on Pediatric Populations.**

2025 · The journal of pediatric pharmacology and therapeutics : JPPT : the official journal of PPAG · journal article, journalarticle, note · eng · https://doi.org/10.5863/1551-6776-30.2.289

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: No abstract; "Note" record type and overview-style title suggest a commentary or review on pediatric kratom use, not a dependence survey.); Sonnet ? (нет аннотации: No abstract; record type is a Note, likely a commentary or review on pediatric kratom use, but content is unclear.)

**Решение:** - педиатрический обзор / комментарий

---

### 66 · R1092

**A network analysis of depression, anxiety, and their associations with kratom (Mitragyna speciosa) use among people who previously used methamphetamine.**

2025 · Journal of psychoactive drugs · article, journal article, journalarticle · eng · https://doi.org/10.1080/02791072.2025.2603333

Kratom has been widely reported to alleviate depression and anxiety; however, its effects on depression and anxiety in people who use methamphetamine (METH) are rarely investigated. This study constructed network structures of kratom use, depressive symptoms, and anxiety symptoms to gain a preliminary understanding of the possible psychopharmacological mechanisms by which kratom affects depression and anxiety. R package (Version 4.4.1) was used to construct network structures, calculate expected influence and bridge expected influence, estimate networks accuracy, and stability. A sample of 403 males who used METH with and without kratom-use history were recruited for this cross-sectional study. Compared with those without kratom-use history, those who co-used METH with kratom had several lower levels of depressive symptoms. The central depressive symptom was "sleep disturbance" (BDI-16) and the central anxiety symptom was "heart pounding or racing" (BAI-7). Kratom dosage per consumption was the most important kratom-use indicator that was associated with depression and anxiety. Our preliminary findings indicate that kratom may affect depression and anxiety in males who used METH in a dose-dependent and frequency-dependent manner. The most correlated symptoms and bridge nodes in this network analysis should be considered as potential targets for intervention.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of methamphetamine users, including people who use kratom, with kratom-use indicators; abstract doesn't say whether kratom dependence was assessed.

**Решение:** =

---

### 67 · R1093

**Correlates of alexithymia and its relationship with Kratom ( Mitragyna speciosa ) use in a cohort of male methamphetamine users in Malaysia**

2025 · Journal of Substance Use · article, journalarticle, journal-article · en · https://doi.org/10.1080/14659891.2025.2512519

ABSTRACT Background Alexithymia is a typical clinical manifestation of prolonged methamphetamine use and risk transdiagnostic factor for emotion-based psychiatric disorders. Kratom (Mitragyna speciosa) co-consumption is becoming prevalent among methamphetamine users in Southeast Asia. Given its therapeutic value in mitigating mood disorders, it was hypothesized that methamphetamine users self-manage alexithymia effects with kratom. Methods A total of 367 male methamphetamine users with and without kratom use history participated in this cross-sectional study. Validated scales encompassing the Malay version of the Kratom Dependence Scale (KDS), Beck Depression Inventory (BDI), Beck Anxiety Inventory (BAI), Toronto Alexithymia Scale (TAS-20), and Visual Analogue Scale (VAS) were administered. Results The level of alexithymia in methamphetamine users with kratom use history did not differ significantly from methamphetamine users without kratom use history. Similarly, among methamphetamine users with kratom use history, their alexithymia level did not contrast significantly across groups based on their duration (short vs. long-term) of methamphetamine and kratom use history. Indeed, only current age, age of first illicit drug use history, and anxiety were predictors for alexithymia level in methamphetamine users with kratom use history. Conclusions Kratom consumption cannot significantly predict alexithymia level. Its regular use did not appear to alleviate alexithymia in methamphetamine users.

**ИИ:** + · обе модели · другая выборка, есть употребляющие и мера зависимости · Methamphetamine users, some with a history of kratom use; the Malay Kratom Dependence Scale was given, so dependence prevalence may be reported.

**Решение:** =

---

### 68 · R1110

**The Relationship between Kratom Use and Academic Performance of Students in Humanities-Oriented Fields**

2025 · Univerzita Tomáše Bati ve Zlíně · thesis

Tato diplomová práce se zaměřuje na dosud málo prozkoumanou souvislost mezi užíváním kratomu a akademickou úspěšností studentů humanitně orientovaných oborů. V teoretické části je poskytnut komplexní pohled na historický, chemický a sociokulturní kontext kratomu a zároveň jsou diskutovány determinanty akademické úspěšnosti v kontextu nároků vysokoškolského studia a psychosociálních faktorů. Praktická část vychází z kvantitativního výzkumu realizovaného na Univerzitě Tomáše Bati ve Zlíně, kde bylo analyzováno 226 kompletně vyplněných dotazníků. Výsledky ukazují, že ačkoliv celková míra užívání kratomu je nízká, existují statisticky významné rozdíly v závislosti na pohlaví a ročníku studia. Zásadní zjištění spočívá ve výsledku, že studenti, kteří kratom užívají, subjektivně hodnotí svoji akademickou úspěšnost jako vyšší, což je ale v rozporu s jejich objektivně stanovenými výsledky (průměrným prospěchem za poslední semestr). Tento rozpor je vysvětlitelný indukovanými účinky kratomu, jako jsou euforie, zlepšená nálada a zvýšená sebedůvěra, které mohou vést k nadhodnocení vlastních schopností a ke zkreslenému sebevnímání. Studie tedy nejen podtrhuje potenciální negativní vliv užívání psychoaktivních látek na kognitivní funkce a studijní výkon, ale také zdůrazňuje nutnost preventivních opatření a podpůrných intervencí v akademickém prostředí.This master's thesis explores the little-studied link between kratom use and the academic performance of humanities students. The theoretical section offers a clear overview of the historical, chemical, and sociocultural aspects of kratom, as well as the factors that influence academic success in higher education, including various psychosocial elements. The practical part is based on a quantitative study conducted at Tomas Bata University in Zlín, where 226 completed questionnaires were analyzed. The results reveal that although overall kratom use is low, there are significant differences based on gender and year of study. A key finding is that students who use kratom tend to rate their own academic success higher, even though their actual performance (measured by the average grades from the last semester) is lower. This gap can be explained by the effects of kratom - such as euphoria, improved mood, and increased self-confidence - which may lead students to overestimate their abilities and have a distorted self-view. The study thus emphasizes not only the potential negative impact of psychoactive substances on cognitive functions and academic performance but also the need for preventive measures and supportive interventions within the academic environment.Ústav pedagogických vě

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Thesis surveying 226 university students on kratom use and grades; the abstract doesn't say whether kratom dependence was assessed.

**Решение:** =

---

### 69 · R1128

**The association between undergraduate majors and substance use and how mental health status affects that relationship**

2024 · University of Iowa · master thesis, text/master thesis · en · https://doi.org/10.25820/etd.007320

Previous findings demonstrate variability in substance use among undergraduate majors and demonstrate significant relationships between mental health status and substance use. However, there is a gap in the literature on whether mental health status plays a role in the relationship between college majors and substance use. This epidemiological study, which aims to address that gap, examined the relationship between major and substance use as the first goal. Its secondary goal was to examine how that relationship changed when accounting for mental health status. The study data stems from the Healthy Minds Survey, which is a public and cross-sectional dataset. Arts &amp; Humanities, STEM, Business, Education, and Social Sciences, Health, and Undecided and Other college majors were considered, with STEM used as the reference group. Substance use was defined as stimulants, opioids, hallucinogens, binge drinking, marijuana, cigarettes or vaping (nicotine), kratom, and benzodiazepines. Mental health status was operationalized as two types of variables: mental health symptom scales and mental health diagnoses. This study utilized logistic regression, focusing on a yes/no outcome for each substance by undergraduate major. Two categories of models were created: one that did not adjust for mental health variables, which included the mental health symptom scales and mental health diagnoses and mental health treatment, and another that did. Covariates that were in both models included variables capturing demographics which included but were not limited to family education level, chronic disease conditions, age, sexual orientation, and gender. Other covariates included chronic health conditions and substance use screening questions. There were statistical differences in the rate of substance use across majors. The relationship between undergraduate majors and substance use had inconsistent variations when adjusted for mental health status. In general, the associations between undergraduate major and substance use were relatively stable with and without adjustment for mental health. This suggests that mental health does not play a substantial role in the relationship of undergraduate majors and substance use.

**ИИ:** разошлись — Opus ? (неясно, оценивали ли зависимость: Student survey (Healthy Minds) measured kratom use as yes/no; mentions substance use screening questions, so kratom dependence assessment is unclear.); Sonnet -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: Healthy Minds Survey of undergraduates; kratom use is a yes/no outcome by major, with no kratom dependence or use-disorder measure.)

**Решение:** - студенческий опрос о специальностях и ПАВ: нет меры зависимости от кратома

---

### 70 · R1149

**Prevalence užívání kratomu u studentů gymnázia ve Zlínském kraji: dotazníková studie**

2024 · master thesis · ces/cze · http://www.nusl.cz/ntk/nusl-622374

Introduction: Kratom is a psychoactive substance made from the tropical tree Mitragyna speciosa, which is native to Southeast Asia. Today, it is already widespread throughout the world, mainly due to its paradoxically biphasic properties -stimulant and analgesic. In the Czech Republic, kratom is not regulated in any way, so it is easily available for all ages. This makes it attractive to a population of young people, including high school students. Objectives: The main objective was to find out the prevalence of kratom use among the students of the selected high school. Another objective was to find out the most common reasons for kratom use. The last objective was to examine the consequences associated with kratom use in the research population. Methods: Quantitative research was used to obtain the data. The research was conducted using an anonymous online questionnaire survey on a paid version of the Survio.com platform. For the research, the management of a selected upper secondary school in the Zlín region was contacted and agreed to conduct the research among students over 15 years of age (first, second, third and fourth years of a four-year secondary school and students of the quint, sexta, septima and octave of an eight-year secondary school). The Survio.com platform was used to collect the...

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of high school students on kratom use prevalence and its consequences; truncated abstract doesn't say whether dependence was assessed.

**Решение:** - опрос о вождении в состоянии опьянения, нет меры зависимости

---

### 71 · R1155

**Prevalence of kratom use among upper grammar school students in the Zlín region: questionnaire survey**

2024 · Digital Repository (National Repository of Grey Literature) · dissertation, thesis · cs · https://core.ac.uk/download/619649866.pdf

Východiska: Kratom je psychoaktivní substance pocházející z tropického stromu Mitragyna speciosa, který pochází z jihovýchodní Asie. Dnes je již rozšířený po celém světě, a to zejména díky paradoxně bifázickým vlasnostem - stimulačním a analgetickým. V České republice není kratom nijak legislativně upraven, takže je snadno dostupný pro všechny věkové kategorie. Díky tomu je atraktivní pro populaci mladých lidí, mezi něž patří i středoškolští studenti. Cíle: Hlavním cílem bylo zjistit, jaké je prevalence užívání kratomu mezi studenty vybraného gymnázia. Dalším cílem bylo zjistit, jaké jsou nejčastější důvody pro užívání kratomu. Posledním cílem bylo zkoumat následky spojené s užíváním kratomu ve výzkumném souboru. Soubor: Výzkumný soubor byl tvořen studenty vybraného vyššího gymnázia ve Zlínském kraji. Respondenti byli ve věku 15-19 let. Jednalo se nenáhodný kriteriální výběr respondentů. Celkem se do výzkumu zapojilo 258 studentů. Téměř třetina (27,9 %) respondentů byla tvořena studenty prvních ročníku. Druhou nejpočetnější skupinou byli studenti třetích ročníků (17,8 %). Více než polovina respondentů byly ženy (55,8 %). Druhou nejpočetnější skupinu tvořili muži (42,6 %) a třetí skupinou byli zástupci blíže nespecifikovaného genderu (1,6 %). Metody: Pro získání dat byl použit kvantitativní výzkum....Introduction: Kratom is a psychoactive substance made from the tropical tree Mitragyna speciosa, which is native to Southeast Asia. Today, it is already widespread throughout the world, mainly due to its paradoxically biphasic properties -stimulant and analgesic. In the Czech Republic, kratom is not regulated in any way, so it is easily available for all ages. This makes it attractive to a population of young people, including high school students. Objectives: The main objective was to find out the prevalence of kratom use among the students of the selected high school. Another objective was to find out the most common reasons for kratom use. The last objective was to examine the consequences associated with kratom use in the research population. Methods: Quantitative research was used to obtain the data. The research was conducted using an anonymous online questionnaire survey on a paid version of the Survio.com platform. For the research, the management of a selected upper secondary school in the Zlín region was contacted and agreed to conduct the research among students over 15 years of age (first, second, third and fourth years of a four-year secondary school and students of the quint, sexta, septima and octave of an eight-year secondary school). The Survio.com platform was used to collect the...Department of Addictology First Faculty of Medicine Charles University and General University Hospital in PragueKlinika adiktologie 1. LF UK a VFN1. lékařská fakultaFirst Faculty of Medicin

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Thesis surveying kratom use and its consequences among Czech students; the abstract is cut off and doesn't say whether dependence was measured.

**Решение:** ? EMA исследование 357 потребителей кратома: зависимость может быть в таблице характеристик

---

### 72 · R1161

**The Evaluation Of Endoplasmic Reticulum Stress Among Regular Kratom Users And Its Implications For Kratom Dependence And Kratom Induced Depressive Symptoms**

2024 · Universiti Sains Malaysia Institutional Repository (Universiti Sains Malaysia) · dissertation, review · en · https://core.ac.uk/download/690911992.pdf

Recent research showed that psychoactive substances can induce endoplasmic reticulum (ER) stress and unfolded protein response (UPR). This case-control study filled the research gap by: (1) determining the association between kratom use characteristics (such as the age of first kratom use, the duration of kratom use, the average frequency and quantity of daily kratom use, and the time since last kratom consumption prior to blood collection for analysis) and the mRNA and protein expression of ER stress sensors; and (2) assessing the correlations between the mRNA and protein expression of ER stress sensors and severity of kratom dependence and kratom induced depressive symptoms during kratom abstinence.

**ИИ:** + · обе модели · употребляющие + мера зависимости · Case-control thesis of regular kratom users that assessed how severe kratom dependence was; it may report how many met dependence criteria.

**Решение:** =

---

### 73 · R1170

**Characterization of kratom use and knowledge at a rural, Oregon community health center.**

2024 · Journal of the American Pharmacists Association : JAPhA · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.japh.2024.102138

BACKGROUND Kratom is an herbal supplement that has drawn attention for its use in the self-treatment of opioid withdrawal, and its widespread availability with minimal restrictions. Past web-based research has attempted to determine patterns and trends of use, but generalizability to underserved populations is unclear. OBJECTIVE The purpose of this study was to characterize behavior related to kratom, attitudes toward kratom, and knowledge of kratom in a rural, underserved population. METHODS We developed, refined, and administered a cross-sectional, 36-item survey to examine use, attitudes, and knowledge of kratom. We recruited participants and administered the survey alongside medical office appointments between January and April 2023. Data were summarized using descriptive statistics. RESULTS A convenient sample of 186 patients (of the 907-patient clinic panel) were invited to participate and 150 returned the survey. A majority of patients were female (52.0%) and White (86.6%), and about half had an income below the federal poverty level (48.5%). Seventeen participants reported prior experience with kratom use, with one actively using kratom. The most commonly reported reasons for use were pain (47.1%) and mental health (41.2%). Kratom knowledge was low regardless of kratom use history, with the majority of respondents correctly answering between 1 and 3 questions (n = 71 of 86; 82.3%) of the 5 knowledge-focused items. CONCLUSION Results suggest that while active kratom use is uncommon in this Oregon population, one in ten surveyed had used kratom. Regardless of past use, respondents had limited knowledge of kratom. Future research should focus on understanding trends in kratom use behaviors in underserved populations, addressing patient knowledge gaps, and evaluating patient safety and health equity implications.

**ИИ:** разошлись — Opus -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: Clinic patient survey covered only kratom use, reasons, attitudes and knowledge; no dependence or use-disorder measure described.); Sonnet ? (неясно, оценивали ли зависимость: Clinic patient survey with 17 kratom ever-users; abstract reports use, attitudes and knowledge, and doesn't say whether dependence was assessed.)

**Решение:** - опрос пациентов клиники: только доля употребления и знания, нет меры зависимости

---

### 74 · R1255

**Prevalence of Kratom Use Disorder Among Kratom Consumers.**

2024 · Journal of addiction medicine · article, journal article, journalarticle · eng · https://doi.org/10.1097/adm.0000000000001290

OBJECTIVES: Kratom leaf products are increasingly consumed in the United States, with many consumers reporting they experience beneficial effects from kratom use. However, there is a growing concern for kratom's potential to result in dependence when used regularly. As such, we sought to assess, using Diagnostic and Statistical Manual of Mental Disorders , (DSM-5) , diagnostic criteria for substance use disorder, the prevalence of "kratom use disorder" (KUD) among kratom consumers. METHODS: Our cross-sectional study used an online, anonymous survey between February and May 2023. Through nonprobability sampling, we recruited people older than 18 years who currently consume kratom. Participants were asked about their kratom consumption patterns, adverse effects perceived to stem from kratom consumption, comorbid diagnoses, and components for a DSM-5 , substance use disorder, adapted for kratom. RESULTS: Among the total sample ( N = 2061), KUD criteria were met by 25.5% of participants ( n = 525); the most commonly reported symptoms were tolerance ( n = 427, 81.3%) and withdrawal ( n = 357, 68.0%). After adjusting for age, gender, daily frequency of kratom consumption, and history of either a substance use disorder or a mental health condition, those with a concurrent diagnosis of another substance use disorder had 2.83 times higher odds of meeting KUD criteria (95% CI, 2.19-3.67) compared with those without one. CONCLUSIONS: In this large cross-sectional study, most participants who met the criteria for a KUD diagnosis were categorized as having a mild or moderate KUD. Individual characteristics associated with KUD were related to being male, young, consuming kratom frequently, and having psychiatric and substance use disorder comorbidities.

**ИИ:** + · обе модели · употребляющие + мера зависимости · Online survey of 2061 current kratom consumers; DSM-5 KUD criteria met by 25.5%.

**Решение:** =

---

### 75 · R1256

**Use of Cannabinoids by People Who Consume Kratom in the United States.**

2024 · Journal of addiction medicine · article, journal article, journalarticle · eng · https://doi.org/10.1097/adm.0000000000001346

OBJECTIVES: To estimate lifetime, past-year, and past-month prevalence of kratom, cannabis, and cannabidiol-only product use among adults 18 years and older in the United States, using 2 independent datasets. METHODS: Utilizing ( a ) the 2022 National Survey on Drug Use and Health (NSDUH) and ( b ) a 2022 online national convenience sample of adults who use kratom regularly (from our research group at the National Institute on Drug Abuse [NIDA]), we examined key demographic information as well as lifetime, past-year, and past-month substance use and preferences. RESULTS: Among the full sample of adults from the 2022 NSDUH, the prevalence of lifetime use was 49.69% for cannabis, 34.09% for cannabidiol-only products, and 1.93% for kratom. When solely examining participants who have used kratom, both independent datasets showed higher proportions of cannabis use over the lifetime-92.81% (95% confidence interval: 90.31-95.31) in the NSDUH subset and 92.16% (95% confidence interval: 89.37-94.95) in our NIDA sample. CONCLUSIONS: Our study demonstrates that people are co-using kratom with cannabis and/or cannabidiol-only products at the same time or during the same time period, though more research is needed to understand people's motivations and practices for such co-use. Co-use might result in herb-herb interactions that may impact research findings and clinical outcomes for people who use kratom.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · NSDUH plus a NIDA online sample of regular kratom users, focused on cannabis co-use; the abstract doesn't say whether kratom use disorder was assessed.

**Решение:** =

---

### 76 · R1278

**การใช้สารเสพติดของเยาวชนไทย**

2024 · Community Health Development Quarterly Khon Kaen University · article · th

The study of the epidemic situation of substance use is the cornerstone of solving the problem. This study aimed to determine the proportion of Thai youths (aged 10-18 years) who use substances in 2022. It was a cross-sectional descriptive study using a three-stage stratified cluster sampling. A total of 4,666 samples were obtained. A self-administered questionnaire collected data. Descriptive statistics and chi-square analyzed data. Of Thai youths aged 10-18, 16.6% reported their experiences of ever using any substances. Of these, 13.1% had used substances in the past 3 months. There were statistically significant differences between sexes and age groups. The popular substance used by youths were kratom (especially kratom liquid), sedatives, cannabis (especially dried cannabis), stimulants (especially YABA), depressants (especially tramadol and codeine), and hallucinogens, respectively. In addition, the behavior of using more than one substance simultaneously (polysubstance) was found. There are also substances used along with alcohol, as well as using substances together with e-cigarettes. Moreover, substances used along with alcohol and e-cigarettes have also emerged.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Thai youth survey with kratom as the most-used substance; it asks about past-3-month use and may be ASSIST-based, but dependence measures are unclear.

**Решение:** =

---

### 77 · R1294

**Prevalence and patterns of kratom use in the Czech population and risk of loss of controlled use over time: cross-sectional questionnaire survey**

2024 · Digital Repository (National Repository of Grey Literature) · dissertation, thesis · cs · https://core.ac.uk/download/619650299.pdf

Východiska: V posledních letech roste v ČR míra užívání kratomu. Jedná se o psychoaktivní látku rostlinného původu, jejíž dostupnost není v ČR dosud regulována zákonem, což způsobuje snadnou dostupnost i pro nezletilé. Jsou popsány různé vzorce užívání kratomu, přičemž není zřejmé, v jaké míře dochází k rozvoji problematického užívání či závislosti. Cíle: Hlavními cíli této práce bylo zmapovat užívání a dopady užívání kratomu v české populaci a analyzovat, jaký je výskyt různých vzorců užívání kratomu a zda, či v jaké míře, dochází ke ztrátě kontroly v průběhu užívání kratomu. Metody: Byla provedena průřezová online dotazníková studie. Výzkumný soubor tvořily osoby starší 18 let žijící na území České republiky, které mají zkušenost s užitím kratomu, vybrané nepravděpodobnostním výběrem na sociálních sítích. K náboru byly využity skupiny a fóra sdružující osoby se zkušeností s kratomem a uplatnila se i metoda sněhové koule, když někteří respondenti sdíleli pozvánku dále mezi svými kontakty. Výsledky: Dotazník vyplnilo 331 respondentů. Výzkumný soubor tvoří 259 respondentů, kteří uvedli užití kratomu někdy v životě, z nichž většinu tvořili muži (79,5 %), nejčastěji ve věkové skupině 15 až 34 let (76,1 %). Většina těch, kteří uvedli užívání v průběhu života, tak činila i v posledním roce a měsíci....Background: In recent years, the rate of kratom use has been increasing in the Czech Republic. It is a psychoactive substance of plant origin, the availability of which is not yet regulated by law in the Czech Republic, which causes easy availability even for minors. Different patterns of kratom use are described, and it is not clear to what extent problematic use or addiction develops. Objectives: The main objectives of this work were to map the use and effects of kratom use in the Czech population and to analyze the occurrence of different patterns of kratom use and whether, or to what extent, there is a loss of control during kratom use. Methods: A cross-sectional online questionnaire study was conducted. The research group consisted of persons older than 18 years living in the territory of the Czech Republic who have experience of using kratom, selected by non-probability sampling on social networks. Groups and forums bringing together people with experience with kratom were used for recruitment, and the snowball method was used, when some respondents shared the invitation further among their contacts. Results: 331 respondents completed the questionnaire. The research population consists of 259 respondents who reported using kratom at some point in their life, the majority of whom were men...Department of Addictology First Faculty of Medicine Charles University and General University Hospital in PragueKlinika adiktologie 1. LF UK a VFN1. lékařská fakultaFirst Faculty of Medicin

**ИИ:** разошлись — Opus + (употребляющие + мера зависимости: Online survey of 259 Czech kratom users explicitly assessing loss of control and development of addiction; specific measure not stated in truncated abstract.); Sonnet ? (неясно, оценивали ли зависимость: Czech online survey of 259 people who used kratom; examines loss of control and problematic use, but the abstract doesn't state a dependence or use-disorder measure.)

**Решение:** + опрос 259 потребителей кратома в Чехии: оценка потери контроля и зависимости

---

### 78 · R1331

**Substance abuse among new patients attending main government hospitals in Malaysia from 2018-2021: A comparison between before and during COVID-19 pandemic.**

2024 · PloS one · article, comparative study, research-article · eng · https://doi.org/10.1371/journal.pone.0309422

BACKGROUND: Substance abuse admission to health facilities following the pandemic is often met with challenges. COVID-19 is causing an insurmountable psychosocial impact on the whole of mankind. Marginalized communities, particularly those with substance use disorders (SUDs), are also likely to suffer from greater psychosocial burden. OBJECTIVES: This study sought to evaluate substance abuse trends before and during the pandemic. METHODS: A cross-sectional study was conducted among patients attending selected government hospitals in Malaysia. Data from the year 2018 to 2021 was utilized. RESULTS: A total of 9,606 patients consisting of 7881 males and 1725 females were identified. Most of the patients involved with substance abuse from 2018 to 2021 were males, aged between 26 and 44 years old, Malays, high school students, singles, workers of private sectors and those residing in urban areas. The most abused substances over the four years were tobacco (61.8%), followed by amphetamine-type stimulants (ATS) (43.1%), alcohol (39.7%), cannabis (17.2%), opioids (13.0%), and kratom (8.8%). Those who worked in the private sector and were self-employed or unemployed were more associated with substance abuse during the pandemic compared to those who worked in the government sector. Those with a history of psychiatric illness were more associated with abuse of substances during the pandemic than those without the history (adjusted OR: 1.18, 95% CI 1.09-1.29, p <0.001). CONCLUSIONS: Targeted exploration of factors affecting substance abuse in Malaysia is essential. The results of this study assist in identifying variations in substance abuse treatment characteristics for those admitted to treatment in Malaysia.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Hospital substance-abuse patient data reporting kratom abuse (8.8%); unclear whether kratom dependence/use disorder was diagnosed with defined criteria.

**Решение:** ? опрос 400 жителей сельских районов Таиланда: мера зависимости может быть в анкете

---

### 79 · R1372

**Latent class analysis of polysubstance use and association of various risk factors with polysubstance use among vocational students in Northern Thailand by sex differences and factors association**

2024 · Journal of Health Research · article · en · https://doi.org/10.56808/2586-940x.1100

Background: Using multiple substances carries higher risks and health consequences than using a single substance. This study aims to identify polysubstance user subgroups among vocational students in northern Thailand and evaluate associated risk factors by gender. Methods: This study was conducted among Thai vocational students. Latent class analysis (LCA) was utilized to identify classes of polysubstance use. Results: The questionnaire was completed by 2399 male and 1213 female respondents. LCA revealed distinct patterns of polysubstance use between male and female adolescents. A four-class solution was the best-fitting model for males: class 1 (1.42%) was characterized as the polysubstance user (all types) group; class 2 (22.23%) included the predominant alcohol and tobacco user group; class 3 (5.37%) formed the predominant alcohol, tobacco, cannabis, and kratom user group; and class 4 (70.98%) comprised the nonuser group. For females, a three-class solution was the best fit: class 1 (1.55%) included the polysubstance user (all types) group; class 2 (80.94%) comprised the nonuser group; and class 3 (17.51%) represented the predominant alcohol and tobacco user group. Factors that significantly increased the risk of polysubstance use among both male and female adolescents (p &lt; 0.05) were positive attitudes toward polysubstance use and tobacco or cannabis as their first substance used. Conclusion: Thailand should enforce existing legislation strictly and effectively to limit youth access to tobacco. It is important to provide medical information about the negative health effects of recreational cannabis use. Keywords: Adolescent, Drug abuse, Latent class analysis, Substance use, Vocational education

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of Thai vocational students that measured kratom use; abstract doesn't say whether ASSIST or dependence criteria were used.

**Решение:** =

---

### 80 · R1376

**Covid-19 Patients with First-Diagnosed Substance Use Disorders in Southern Thailand: A Study from a Field Hospital**

2024 · Journal of Health Science and Medical Research · article, journalarticle, review · en · https://doi.org/10.31584/jhsmr.20241070

Objective: This retrospective study investigated usage patterns, withdrawal symptoms, and treatments provided to COVID-19 patients with first-diagnosed substance use disorders at a field hospital in southern Thailand in 2021.Material and Methods: The medical records of all COVID-19 patients were reviewed, and descriptive statistics were calculated and reported. The process of analyzing data was carried out by utilizing Program R.Results: Of the 2116 patients, 12.9% had a history of substance and/or alcohol use without any prior diagnosis. Most patients were male (94.9%), and the mean age was 31.7 years old. Tobacco and kratom were the substances most frequently used by COVID-19 patients. Withdrawal symptoms were observed in approximately half of all patients with substance use disorders, particularly those who used kratom and opioids. The most commonly reported withdrawal symptoms were insomnia and muscle aches, and chlorpromazine and amitriptyline were the most prescribed psychotropic medications. The majority of patients with substance use disorders (93.8%) did not report any complications related to their COVID-19 infection.Conclusion: This study found that 12.9% of COVID-19 patients admitted to a field hospital in southern Thailand in 2021 had a newly diagnosed substance use disorder. The substances most commonly used by these patients were tobacco and kratom. Approximately half of the patients with substance use disorders experienced withdrawal symptoms, and kratom and opioids were the substances most frequently associated with these withdrawal symptoms.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Chart review of COVID patients with newly diagnosed SUD, kratom common; unclear whether kratom users without SUD diagnosis can be counted.

**Решение:** =

---

### 81 · R1382

**Use patterns of classic, novel, and herbal opioids**

2024 · Emerging Trends in Drugs Addictions and Health · article, research article · en · https://doi.org/10.1016/j.etdah.2024.100166

Background: Data on use patterns and psychological and physical effects of novel synthetic opioids (NSOs) and herbal opioids like kratom (Mitragyna speciosa) lags behind that of classic opioids. Aims: This study aimed to describe use patterns, adverse events, subjective experience and motivation of use with classic, novel and herbal opioids. Methods: A two-part survey was used. The first part examined the prevalence, use patterns (dosage, administration route, duration of effects), and associated adverse events of classic, novel and herbal opioids. The second part delved into detailed retrospective experiences of survey responders with an opioid of preferred choice, mostly kratom. Results: Between May 2020 and February 2023, 467 respondents started the survey, of which 310 met the inclusion criteria. Of these, 52 % (N = 161) completed the first part, 65.6 % (N = 105) started the second part of which 72 completed. Most respondents were male, highly educated, based in North America or Europe, often using multiple opioids. A total of twenty-seven different compounds were reported, of which hydrocodone/dihydrocodeine, kratom, acetylfentanyl, and U-47700 were used the most. A wide range of doses was reported for each compound. Median effect durations ranged between 3 and 4 h for most of the compounds. Administration routes varied, with oral intake being most prevalent. Fentanyl analogues were often administered intravenously. Physical/psychological adverse events were frequently reported by users of oxycodone, kratom, acetylfentanyl, and U-47700. User reports revealed that both kratom and classic opioids were used for recreational and medical purposes, including ameliorating pain, addiction/withdrawal, anxiety, and mood enhancement. Conclusion: Psychological and physical adverse events were widely present among classic, novel and herbal opioids suggesting a need for risk monitoring worldwide. Similarities between classic opioids and kratom include medical utility as well as addictive potential.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Online survey of opioid users, mostly kratom; says kratom has addictive potential, but doesn't say whether dependence criteria were assessed.

**Решение:** =

---

### 82 · R1402

**Kratom addiction per DSM-5 SUD criteria, and kratom physical dependence: Insights from dosing amount versus frequency.**

2024 · Drug and alcohol dependence · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.drugalcdep.2024.111329

Background: Kratom products are widely used in the United States, with inadequate understanding of how dosing amounts/frequencies relate to outcomes. Methods: Between July-November 2022, we enrolled 395 active US adult kratom consumers into a remote study with a baseline survey. We examined self-reported typical dose amounts and frequencies across people and product types, and their associations with outcomes: multiple regression was used to examine whether amounts and frequencies (doses/day) were associated with acute effects, withdrawal symptoms, scores on the Subjective Opioid Withdrawal Scale (SOWS), and addiction (operationalized as DSM-5-based symptoms of kratom-use disorder, KUD). Results: Participants were 54.9% male, aged 38.1 on average, and 81.3% White. Mean length of kratom use was 5.7 years. Most (95.9%) reported regularly using whole-leaf kratom products; 16 (4.1%) reported regular extract use. SOWS scores were mild to moderate on average (13.5, SD 11.9). KUD symptom counts were mostly in the mild/moderate range (80.7%). Withdrawal and KUD symptoms were more closely associated with dose frequency than dose amount. Men reported more acute effects, withdrawal symptoms with cessation, and KUD symptoms than women. Conclusions: Greater dose amount and frequency were systematically related to the number of withdrawal symptoms upon cessation and to KUD symptoms; the relationship was stronger for dose frequency than amount. Men may have more acute effects and more withdrawal and KUD symptoms than women. Although kratom may be used nonproblematically by some consumers, physical dependence (tolerance, withdrawal, or use to avoid withdrawal) and KUD become more likely with increasing dose frequency.

**ИИ:** + · обе модели · употребляющие + мера зависимости · Remote survey of 395 active US kratom users that assessed DSM-5 kratom use disorder symptom counts and severity.

**Решение:** ? опрос 262 водителей автобусов в Южном Таиланде: зависимость может быть в анкете

---

### 83 · R1407

**Pengaruh Penggunaan Kratom Secara Berlebihan Pada Remaja**

2024 · Jurnal Ilmiah Multidisiplin Keilmuan Mandira Cendikia · article · en

Perkembangan remaja dilihat dari adanya perubahan yang cepat dengan memunculkan sesuatu yang baru dan berbeda pada psikososial mereka. Sehingga keinginan untuk mencari tau meningkat dan kecintaan pada dirinya sendiri dengan banyaknya fantasi terhadap kehidupannya selama masa remaja.Tujuan dari penelitian ini yaitu untuk memahami efek kratom pada Kesehatan fisik dan mental remaja, termasuk efek samping jangka pendek dan jangka panjang. Manfaat penelitian ini yaitu untuk meningkatkan pemahaman dan kesadaran mengenai bahaya dari kratom secara berlebihan.

**ИИ:** разошлись — Opus ? (другое: Indonesian paper on excessive kratom use in adolescents; the abstract gives no design, so it may be a literature review or a survey.); Sonnet -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: Indonesian article on effects of excessive kratom use in adolescents; aims at understanding effects, appears a literature-based review with no prevalence or dependence data.)

**Решение:** - обзорная статья на индонезийском языке

---

### 84 · R1417

**A Cross Sectional Study on Psychoactive Drug Use Among School-Going Adolescents: Data from Drug Burdened Hot-Spots in Malaysia**

2024 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.4687653

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; Malaysian adolescent drug survey likely includes kratom (ketum), possibly with dependence measures like ASSIST.

**Решение:** =

---

### 85 · R1418

**Kratom Use and Suicidal Thoughts and Behaviors in the United States**

2024 · Elsevier BV · posted-content · https://doi.org/10.2139/ssrn.4862662

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Preprint with no abstract; probably a US population survey of kratom use. It is unclear whether kratom dependence or use disorder was measured.

**Решение:** - данные токсикологических центров NPDS, нет опроса потребителей

---

### 86 · R1423

**Informal Use of Kratom for the Self-treatment of Heroin and Amphetamine-Type Stimulant (ATS): Findings from a Sample of People Who Use Drugs (PWUDs) in Malaysia**

2024 · Emerging Trends in Drugs Addictions and Health · article, journalarticle, journal-article · en · https://doi.org/10.1016/j.etdah.2023.100121

Introduction: Malaysia has harsh drug laws and continue to jail people who use drugs (PWUDs). This study aims to describe the use of kratom among PWUDs in Malaysia. Methods: A total of 331 convicted PWUDs with kratom use history were randomly recruited from three penitentiaries for this cross-sectional study. Prison counsellors helped to conduct the surveys with a semi-structured questionnaire. Results: All males (n=331), 94% Malays, and 91% held employments prior to their incarceration. The samples mean age was 32.9 years (SD=7.3). The majority (59%, n=194/331) were amphetamine-type stimulant (ATS) users, only 41% had co-used heroin and ATS. Almost one-third (32%, n=105/331) had used drugs between 1 to 5 years, while 68% had used drugs for ≥6 years. Most (99%, n=321/331) have been jailed before, and 86% (n=284/331) had no formal drug rehabilitation history. Kratom decoction is separately and intermittently consumed with illicit drugs, though 61% (n=202/331) used ≤1 litter of brewed solution daily, it is commonly ingested to enhance energy, to abstain from illicit drug consumption, to reduce the frequency of methamphetamine use, as a substitute to heroin, to maintain abstinence, to suppress heroin withdrawal, and to reduce heroin use frequency, though a few claimed using it to enhance sexual performance, and obtain euphoria. In addition, 48% claimed that it takes approximately one-month to reduce or stop heroin use, while 57% of ATS users claimed the same after initiating kratom. Heroin users rated their withdrawal pain severity as no pain (23%), mild (43%), moderate (27%), and strong (7%) after kratom use. Conclusions: Though kratom has been banned, the infamous indigenous medicinal plant is widely used as a substitute to illicit substances, since it helps PWUDs to self-manage their substance use disorder (SUD). Hence, further clinical studies are needed to support kratom's medicinal use among PWUDs.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of 331 incarcerated PWUDs with kratom use history; the abstract doesn't say whether kratom dependence was assessed.

**Решение:** ? опрос потребителей наркотиков в США: ко-употребление и зависимость кратома

---

### 87 · R1425

**Ecological Momentary Assessment of Self-Reported Kratom Use, Effects, and Motivations Among US Adults.**

2024 · JAMA network open · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1001/jamanetworkopen.2023.53401

Importance: Kratom products, which are sold legally in most of the US, contain alkaloids with opioidergic, adrenergic, and serotonergic activity. Millions of people use kratom to relieve pain, improve mood, or self-manage substance use disorders (SUDs). Kratom use has primarily been examined via surveys, in which recall biases among satisfied users may lead to minimization of transient negative outcomes. Further prospective study of kratom use, such as with ecological momentary assessment (EMA), is needed. Objective: To characterize proximal motivators, effects, and patterns of kratom use and to assess whether use frequency is associated with motivations, effects, past-year criteria for SUD for kratom (KUD), or other substance use. Design, Setting, and Participants: For this prospective cross-sectional study, an intensive longitudinal smartphone-based EMA in which participants' current behaviors and experiences were repeatedly sampled in real time was conducted between July 1 and October 31, 2022. Participants comprised a convenience sample of US adults who used kratom at least 3 days per week for at least 4 weeks at the time of online screening. Criteria for past-year KUD were based on the Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition. Data analysis was performed between November 2022 and November 2023. Exposure: The exposure was 13 401 kratom-use events across 15 days. Main Outcomes and Measures: A baseline survey covering demographics, health, kratom attitudes and behaviors, use motivations, other substance use, and KUD was administered before EMA. Data for the following EMA entries were then collected: event-contingent entries for kratom use (product, dose, and proximal motivations), follow-up entries (short-term effects and consequences of use events), random-prompt entries (mood), beginning-of-day entries (effects of kratom on sleep), and end-of-day entries (daily subjective descriptions of kratom effects). Bayesian regression was used to estimate means and credible intervals. Results: A total of 357 participants completed the EMA. Their mean (SD) age was 38.0 (11.1) years; more than half were men (198 [55.5%]). Participants reported overall motivators of use on the baseline survey that involved managing psychiatric and SUD problems, but proximal motivators evaluated during the EMA involved situation-specific needs such as increasing energy and productivity and decreasing pain. Acute effects were considered congruent with daily obligations. Use patterns, despite having some distinguishing features, were generally similar in their motivators and effects; participants used kratom predominantly during the daytime and seemed to find use frequencies that suited their needs. Higher use patterns were associated with symptoms of physical dependence (eg, withdrawal or tolerance). Co-used substances included caffeine, nicotine, vitamins, and cannabis. Conclusions and Relevance: Most participants in this study reported using kratom in a seemingly nonproblematic way. When such use appeared problematic, the key element was usually that withdrawal avoidance became a proximal motivator. Longitudinal studies examining changes in kratom use patterns and effects over time are needed.

**ИИ:** + · обе модели · употребляющие + мера зависимости · EMA study of US adults who use kratom regularly; past-year DSM-5 kratom use disorder criteria were assessed at baseline.

**Решение:** ? опрос регулярных потребителей кратома и психиатрические симптомы

---

### 88 · R1427

**Novel methods for the remote investigation of emerging substances: Application to kratom.**

2024 · Experimental and clinical psychopharmacology · article, journal article, journalarticle · eng · https://doi.org/10.1037/pha0000656

The botanical product commonly called "kratom" is still relatively novel to the United States. Like other natural products marketed as supplements, kratom is highly variable, both in terms of the alkaloids naturally occurring in kratom leaves and in terms of processing and formulation. Kratom products sold in the United States are not well-characterized, nor are daily use patterns among regular users. Surveys and case reports have comprised most of the literature on kratom use among humans. To advance our understanding of real-world kratom use, we developed a protocol for the remote study of regular kratom-using adults in the United States. Our study had three aspects implemented in one pool of participants nationwide: an in-depth online survey, 15 days of ecological momentary assessment (EMA) via smartphone app, and the collection and assay of the kratom products used by participants during EMA. Here, we describe these methods, which can be used to investigate myriad drugs or supplements. Recruiting, screening, and data collection occurred between July 20, 2022 and October 18, 2022. During this time, we demonstrated that these methods, while challenging from a logistical and staffing standpoint, are feasible and can produce high-quality data. The study achieved high rates of enrollment, compliance, and completion. Substances that are emerging or novel, but still largely legal, can be productively studied via nationwide EMA combined with assays of shipped product samples from participants. We discuss challenges and lessons learned so other investigators can adapt these methods. (PsycInfo Database Record (c) 2024 APA, all rights reserved).

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Methods paper on an online survey and EMA study of regular US kratom users; the abstract doesn't say whether use disorder was assessed.

**Решение:** =

---

### 89 · R1428

**Responses to a "Typical" Morning Dose of Kratom in People Who Use Kratom Regularly: A Direct-Observation Study.**

2024 · Journal of addiction medicine · article, journal article, research support, n.i.h., extramural · eng · https://doi.org/10.1097/adm.0000000000001259

Introduction Use of kratom has outpaced systematic study of its effects, with most studies reliant on retrospective self-report. Methods We aimed to assess acute effects following kratom use in adults who use regularly, and quantify alkaloids in the products, urine, and plasma. Between July and November 2022, 10 adults came to our clinic and orally self-administered their typical kratom dose; blinding procedures were not used. Physiological measures included blood pressure, respiratory rate, heart rate, pulse oximetry, temperature, and pupil diameter. Subjective outcomes included Subjective Opioid Withdrawal Scale, Addiction Research Center Inventory, and Drug Effects Questionnaire. Psychomotor performance was also assessed. Results Participants were 6 men and 4 women, mean age 41.2 years. Nine were non-Hispanic White; 1 was biracial. They had used kratom for 6.6 years (SD, 3.8 years) on average (2.0–14.1). Sessions were 190.89 minutes on average (SD, 15.10 minutes). Mean session dose was 5.16 g (median, 4.38 g; range, 1.1–10.9 g) leaf powder. Relative to baseline, physiological changes were minor. However, pupil diameter decreased (right, b = −0.70, P &lt; 0.01; left, b = −0.73, P &lt; 0.01) 40–80 minutes postdose and remained below baseline &gt;160 minutes. Subjective Opioid Withdrawal Scale pre-dosing was mild (5.5 ± 3.3) and decreased postdose (b = [−4.0, −2.9], P &lt; 0.01). Drug Effects Questionnaire “feeling effects” increased to 40/100 (SD, 30.5) within 40 minutes and remained above baseline 80 to 120 minutes (b = 19.0, P = 0.04), peaking at 72.7/100; 6 participants rated euphoria as mild on the Addiction Research Center Inventory Morphine-Benzedrine-scale. Psychomotor performance did not reliably improve or deteriorate postdosing. Conclusions Among regular consumers, we found few clinically significant differences pre- and post-kratom dosing. Alkaloidal contents in products were within expected ranges.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Lab study of 10 regular kratom users; the abstract doesn't say if use-disorder criteria were assessed, though the sample description might report them.

**Решение:** =

---

### 90 · R1429

**Time course of kratom effects via ecological momentary assessment, by product type, dose amount, and assayed alkaloid content.**

2024 · Drug and alcohol dependence · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.drugalcdep.2024.112460

BACKGROUND AND AIMS: Using ecological momentary assessment (EMA), we undertook a natural experiment wherein kratom-product variability was a tool to assess kratom dose-response relationships based on product form and alkaloid level. METHODS: Between July-November 2022, 357 US kratom consumers (56.6 % male, 90.2 % non-Hispanic white) completed 15 days of EMA; 348 participants submitted samples of the products used most often during EMA. These were assayed for ten alkaloids using ultra-performance liquid chromatography-tandem mass spectrometry. Self-reported kratom effects were modeled as a function of kratom amount and alkaloid content. RESULTS: Participants used over 220 brands. The most-reported product forms were loose powder (55.8 %) and encapsulated powder (26.8 %); extracts were used less (419 uses across 9.48 % of participants). Of the 12,244 use-event entries, 7726 had follow-up data (15-180minutes after use) on felt effects. Effects were stronger in participants with a higher average amount per use. Within-person dose-response relationships were obscured by highly-consistent within-person dosages. Effects of loose powder decreased over three hours; effects of extracts started higher but decreased more rapidly. Dose-response relationships for specific alkaloids could not be reliably established because total alkaloid content and relative levels of specific alkaloids showed limited variability between products. Higher levels of corynoxine alkaloids were associated with slightly stronger effects, possibly an artifact of modeling data with low alkaloid variability. CONCLUSIONS: Alkaloid content was surprisingly consistent across kratom products, and participants were consistent in the amount they used across events. Firm conclusions about alkaloid-effect relationships for kratom will require experimenter-controlled manipulations of agent and dose.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · EMA study of 357 US kratom consumers; the abstract doesn't mention a use-disorder assessment, but the baseline sample description might report DSM-5 criteria.

**Решение:** =

---

### 91 · R1432

**อิทธิพลของทัศนคติต่อพฤติกรรมการใช้พืชกระท่อม ของผู้บริโภคในประเทศไทย**

2024 · MUT Journal of Business Administration · article · th

This research aims to study influence of attitudes on Kratom usage behavior through both direct and indirect effects; the indirect effects were investigated through conformity to subjective norms and the ability to control behavior. The population used in the study was Kratom consumers in the area under the supervision of the Institute for Survey and Monitoring of Narcotic Crops, Office of the Narcotics Control Board (ONCB), in 135 villages/communities located in 8 provinces of the Southern Region namely Nakhon Si Thammarat, Krabi, Phang Nga, Surat Thani, Ranong, Chumphon, Trang, and Phatthalung and 2 provinces in the Central Region, namely Nonthaburi and Pathum Thani. The samples used in the research were 255 people aged 20 years and above who are consuming or had consumed kratom. The tool used for collecting the data was a questionnaire. The data were processed and analyzed by statistical package. The descriptive statistics analyzed basic statistical values such as frequency, percentage, mean, and standard deviation, while the inferential statistics analyzed the indices of conformity for the Structural Equation Model such as Related Chi square, Adjusted Goodness of Fit Index (AGFI), and Root Mean Square Error of Approximation (RMSEA), and analyzed the regression coefficients of variable. The results of the study revealed that attitudes towards the use of Kratom had the direct influence on consumer behavior, subjective norms, and perceived behavior control, but did not have an indirect effect on subjective norms, and perceived behavior control.

**ИИ:** разошлись — Opus ? (неясно, оценивали ли зависимость: Survey of 255 Thai kratom consumers on attitudes and use behaviour; the abstract doesn't say whether dependence was assessed.); Sonnet -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: Survey of 255 kratom consumers in Thailand on attitudes, norms and behavior (TPB model); abstract shows no dependence or use-disorder measure.)

**Решение:** - опрос 255 потребителей в Таиланде по модели TPB: только установки и поведение, без меры зависимости

---

### 92 · R1437

**Kratom Use and Adverse Events: Findings From the NDEWS Rapid Street Reporting Study**

2024 · Drug and Alcohol Dependence · article, journalarticle, journal-article · en · https://doi.org/10.1016/j.drugalcdep.2023.110567

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. The title points to a street-intercept survey of kratom use and adverse events; unclear whether dependence or use disorder was measured.

**Решение:** =

---

### 93 · R1439

**Satu Kajian Ke Atas Penglibatan Remaja Dalam Masalah Penyalahgunaan Dadah Dan Ketum (Mitragyna Speciosa) Di Malaysia**

2024 · review · https://core.ac.uk/download/656685357.pdf

National Anti-Drug Agency (AADK) found most of the newly detected adolescent drug users were engaged in unsafe sexual behaviours and abusing ketum (Mitragyna speciosa) in the country. While they remain unapproachable and given the paucity of studies involving them, this mixed-method, cross-sectional study aims to investigate the risky sexual behaviours and motives of ketum use. A total of 80 adolescents (age between 13 and 19 years) who were undergoing mandatory drug rehabilitation under Section 6 of the Drug Dependants (Treatment and Rehabilitation) Act of 1983 were recruited through purposive sampling from two formal rehabilitation centres (PUSPEN). All the study data was collected with a self-administered, semi-structured questionnaire, while 21 respondents also participated in the in-depth, face-to-face interviews. Majority were males (70%, n=56/80), only 24 respondents were females. Most Malays (96%, n=77/80), while the samples mean age was 18.2 years (SD=1.40). Sixty-three percent (n=50/80) used methamphetamine only, and the samples mean duration of drug use was 3.15 years (SD=1.5). Sixty-nine percent had engaged in sex previously. High-risk sexual behaviours include having unprotected sex (11%), sex with more than one person (84%), and sex under the influence of drugs (94%). About 44% of the sample had intimate partners who use drugs. Most respondents (64%) were aware of the advantages of safe sex and were familiar with HIV transmission modes (74%). Results from multivariate logistic analysis indicate that females had significantly higher odds of engaging in unprotected sex and having intimate partners who use drugs, whereas, males were, however, more likely to have sex under the influence of drugs

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Mixed-method survey of adolescents in drug rehab, mostly for methamphetamine, covering ketum use motives; abstract cut off and no kratom dependence measure mentioned.

**Решение:** =

---

### 94 · R1486

**ปัจจัยที่มีความสัมพันธ์กับพฤติกรรมการบริโภคพืชกระท่อมของประชากรกลุ่มวัยแรงงานในพื้นที่ตลาดไท จังหวัดปทุมธานี**

2024 · วารสารวิจัยและพัฒนาระบบสุขภาพ · article · th

This research study is a cross-sectional analytical study aimed at study the factors associated to kratom consumption behavior among the work-force in TalaadThai, Pathum Thani Province. The study sample consisted of 276 workers aged 20-59 years from the TalaadThai area, calculated using Daniel's formula and selected through stratified random sampling. Data were collected using a questionnaire and analyzed with descriptive statistics, including frequency, percentage, mean, standard deviation, minimum, and maximum values. Inferential statistics included Eta coefficient, Pearson's Correlation coefficient, and multiple linear regression. The results showed that the majority of the sample was male (77.9%). Most participants had a moderate level of knowledge about kratom (61.2%), a moderate attitude towards kratom (74.3%), and moderate kratom consumption behavior (59.4%). The factors significantly associated with kratom consumption behavior included sex, disease, knowledge about kratom, and attitude towards kratom. The findings of this study can inform actions to reduce risky behavior related to kratom use. Efforts should focus on enhancing knowledge about kratom, particularly regarding its effects and legal aspects, as well as shaping attitudes towards kratom among the working-age group. This approach will help reduce kratom usage or prevent its misuse among this demographic.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Thai worker survey of kratom consumption behaviour, knowledge and attitude; unclear whether the behaviour scale included dependence items.

**Решение:** - студенческий опрос в Таиланде: знания и установки, нет меры зависимости

---

### 95 · R1492

**Effects of kratom on driving: Results from a cross-sectional survey, ecological momentary assessment, and pilot simulated driving Study.**

2024 · Traffic injury prevention · article, other literature type, journal article · eng · https://doi.org/10.1080/15389588.2024.2327827

Despite widespread kratom use, there is a lack of knowledge regarding its effects on driving. We evaluated the self-reported driving behaviors of kratom consumers and assessed their simulated-driving performance after self-administering kratom products. We present results from: 1) a remote, national study of US adults who regularly use kratom, and 2) an in-person substudy from which we re-recruited participants. In the national study (N = 357), participants completed a detailed survey and a 15-day ecological momentary assessment (EMA) that monitored naturalistic kratom use. For the remote study, outcomes were self-reported general and risky driving behaviors, perceived impairment, and driving confidence following kratom administration. For the in-person substudy, 10 adults consumed their typical kratom products and their driving performance on a high-fidelity driving simulator pre- and post-kratom administration was evaluated. Over 90% of participants surveyed self-reported driving under the influence of kratom. Most reported low rates of risky driving behavior and expressed high confidence in their driving ability after taking kratom. This was consistent with EMA findings: participants reported feeling confident in their driving ability and perceived little impairment within 15-180 min after using kratom. In the in-person substudy, there were no significant changes in simulated driving performance after taking kratom. Using kratom before driving appears routine, however, self-reported and simulated driving findings suggest kratom effects at self-selected doses among regular kratom consumers do not produce significant changes in subjective and objective measures of driving impairment. Research is needed to objectively characterize kratom's impact on driving in regular and infrequent consumers.This work was supported by the National Institute on Drug Abuse(NIDA) Intramural Research Program of the NIH and by NIDA grantsDA055571 (KES); DA031098 (JMR).https://www.tandfonline.com/doi/full/10.1080/15389588.2024.232782

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · National survey and EMA of regular US kratom users (N=357); the abstract does not say whether use disorder was assessed, but the sample table may report it.

**Решение:** =

---

### 96 · R1499

**Causes and Effects of Kratom Use among Humanities Students**

2024 · Univerzita Tomáše Bati ve Zlíně · thesis

Bakalářská práce se zabývá příčinami a dopady užívání kratomu u studentů humanitně orientovaných oborů.This bachelor thesis examines the causes and effects of kratom use among humanities majors.Ústav pedagogických vě

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Bachelor thesis on kratom use among students; the design (survey or qualitative) and any dependence measure are unclear from the abstract.

**Решение:** =

---

### 97 · R1501

**Návykové látky na bázi alkaloidů (kratom) a jejich zneužívání u populace dětí a mladistvých v ČR**

2024 · Vysoká škola báňská – Technická univerzita Ostrava · thesis · https://core.ac.uk/download/613580516.pdf

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Czech thesis on kratom misuse among children and adolescents; no abstract, may include a survey that assessed dependence.

**Решение:** =

---

### 98 · R1504

**ประสิทธิภาพของการคัดกรองและการบำบัดแบบย่อสำหรับความเสี่ยงจากการใช้สารเสพติดและความเครียดในทหารเกณฑ์ สังกัดหน่วยทหารในจังหวัดปราจีนบุรี**

2024 · Chula Digiverse · dissertation · th · https://doi.org/10.58837/chula.the.2024.785

การวิจัยครั้งนี้เป็นการวิจัยเชิงพรรณนา โดยมีวัตถุประสงค์เพื่อศึกษาประสิทธิภาพการบำบัดแบบย่อ (Brief Intervention) ต่อพฤติกรรมการใช้สารเสพติด ปัจจัยที่มีความสัมพันธ์กับพฤติกรรมการใช้สารเสพติด เปรียบเทียบความเครียดและพฤติกรรมการใช้สารเสพติด ก่อนและหลังการบำบัดแบบย่อของทหารเกณฑ์ สังกัดหน่วยทหารในจังหวัดปราจีนบุรี โดยเก็บรวบรวมข้อมูล 2 ครั้ง (ก่อนและหลังการบำบัดแบบย่อ) เครื่องมือที่ใช้ในการวิจัยประกอบด้วย แบบสอบถามข้อมูลทั่วไป แบบประเมินความเครียด แบบคัดกรองประสบการณ์ในการใช้ยาสูบ สุรา และสารเสพติดตัวอื่นๆ และการตรวจปัสสาวะ สถิติที่ใช้ในการวิเคราะห์ คือ สถิติเชิงพรรณนา และสถิติเชิงอนุมานผลการศึกษาพบว่า พฤติกรรมการใช้สารเสพติดอย่างน้อยหนึ่งชนิด ก่อนและหลังการบำบัดแบบย่อ มีสัดส่วนเท่ากับร้อยละ 100.00 และ 64.40 ตามลำดับ ซึ่งแสดงให้เห็นถึงความมีประสิทธิภาพการบำบัดแบบย่อ โดยสารที่มีการใช้มากที่สุด 5 อันดับแรก คือ เครื่องดื่มเครื่องดื่มแอลกอฮอล์, ผลิตภัณฑ์ยาสูบ, ใบกระท่อม, สารผสมน้ำต้มใบกระท่อม, และกัญชา โดยมีความเสี่ยงระดับปานกลาง มีความเครียดก่อนการบําบัดแบบย่อระดับสูง (35.60%) หลังการบําบัดแบบย่อส่วนใหญ่มีความเครียดระดับน้อย (51.10%) กลุ่มตัวอย่างส่วนใหญ่มีความเครียดก่อนการบำบัดแบบย่อระดับสูง (35.60%) หลังการบำบัดแบบย่อมีความเครียดอยู่ในระดับน้อย (51.10%) จากการทดสอบสมมติฐาน พบว่า อายุ ภูมิลำเนา รายได้ และความเครียดมีความสัมพันธ์กับพฤติกรรมการใช้สารเสพติดของทหารเกณฑ์ สังกัดหน่วยทหารในจังหวัดปราจีนบุรี อย่างมีนัยสำคัญทางสถิติที่ระดับ 0.05 นอกจากนี้พฤติกรรมการใช้สารเสพติดและความเครียดของทหารเกณฑ์ สังกัดหน่วยทหารในจังหวัดปราจีนบุรีลดลงหลังได้รับการบำบัดแบบย่อ อย่างมีนัยสำคัญทางสถิติที่ระดับ 0.05

**ИИ:** разошлись — Opus + (другая выборка, есть употребляющие и мера зависимости: Thai conscripts screened with ASSIST; kratom leaves and kratom cocktail among top substances, with risk levels reported.); Sonnet ? (неясно, оценивали ли зависимость: Thai conscripts screened with an ASSIST-type tool; kratom leaf and cocktail were top substances, but the abstract doesn't say whether kratom-specific risk scores are reported.)

**Решение:** + скрининг призывников по ASSIST, оценка уровня риска и зависимости от кратома

---

### 99 · R1537

**Characteristics of kratom use among the regular kratom users.**

2023 · Public Library of Science (PLoS) · https://doi.org/10.1371/journal.pone.0287466.s008

Characteristics of kratom use among the regular kratom users.</p

**ИИ:** ? · обе модели · нет аннотации · Looks like a PLoS supplementary table from a study of regular kratom users; the parent article may have assessed dependence.

**Решение:** =

---

### 100 · R1538

**Kratom use characteristics questionnaire (for regular kratom users only).**

2023 · https://doi.org/10.1371/journal.pone.0287466.s001

Kratom use characteristics questionnaire (for regular kratom users only).</p

**ИИ:** ? · обе модели · нет аннотации · Likely a supplementary questionnaire file from a study of regular kratom users; the parent article may report dependence.

**Решение:** =

---

### 101 · R1539

**Publication and licensing rights for Fig 3.**

2023 · https://doi.org/10.1371/journal.pone.0287466.s003

Background and aimsKratom (Mitragyna speciosa Korth.) is widely use worldwide despite its addictive potential. Although psychostimulant use has been linked to occurrence of endoplasmic reticulum (ER) stress, data is lacking on how regular kratom use affects ER stress. This case-control study first determined differences in ER stress sensor protein expression (BiP, sXBP1, ATF4, CHOP, JNK, and p-JNK) between regular kratom users and healthy controls. Second, it evaluated the association between kratom use characteristics, targeted ER stress sensor protein expression, and “kratom use disorder” diagnosed with Diagnostic and Statistical Manual for Mental Disorders 5th Edition (DSM-5) among regular kratom users.MethodsIn total, 60 regular kratom users and 50 healthy control-group participants were recruited and administered a sociodemographic and clinical characteristics questionnaire. While participants who used kratom were also administered a kratom use characteristics questionnaire. Blood samples were collected from all participants, and targeted ER stress sensor protein expression was determined via Western blot analysis.ResultsThe study’s findings revealed first that kratom users registered significantly higher protein expression in all targeted ER stress sensors compared to the control group. Second, higher protein expression of CHOP (B = 5.061, standard error [SE] = 2.547, Wald = 3.948, adjusted odds ratio [AOR] = 5.382, 95% confidence interval [CI] = 1.071 to 9.656, p = 0.047) and p-JNK (B = 5.795, SE = 2.635, Wald = 4.544, AOR = 17.025, 95% CI = 1.395 to 24.123, p = 0.017) increased the odds of kratom use disorder occurrence. Kratom use characteristics and other ER stress sensor protein expression were not associated with kratom use disorder.ConclusionRegular kratom use may induce protracted ER stress, leading to the decompensation of the unfolded protein response to maintain ER homeostasis. This effect may be linked to kratom use disorder occurrence.</div

**ИИ:** + · обе модели · употребляющие + мера зависимости · Figure record for a case-control study of 60 regular kratom users assessed for DSM-5 kratom use disorder.

**Решение:** =

---

### 102 · R1540

**Summary of the findings of this study.**

2023 · https://doi.org/10.1371/journal.pone.0287466.g003

The targeted ER stress sensor protein expressions were determined by Western blotting, which were presented as relative protein expression or fold change by comparing with the corresponding β-actin band. There were higher BiP protein expression in regular kratom users compared with healthy controls indicating greater degree of ER stress and UPR occurred upon chronic kratom consumption. The higher degree of protein expression of sXBP1, ATF4, CHOP, JNK, and p-JNK may demonstrate activation of the PERK-eIF2α-ATF4-CHOP, the IRE1α-sXBP1-CHOP, and the IRE1α-JNK-p-JNK pathways of the ER stress as well as persistence of ER stress which may have decompensated the UPR capacity to restore ER homeostasis. In addition, elevation of protein expression of CHOP and p-JNK, indicating a link between protracted ER stress, UPR and higher odds of occurrence of “kratom use disorder”. Hence, activation of the PERK-eIF2α-ATF4-CHOP, the IRE1α-XBP1-CHOP, and the IRE1α-JNK-p-JNK pathways of the ER stress may be associated with occurrence of “kratom use disorder” (publication and licensing rights for Fig 3 is illustrated in S3 Appendix). Abbreviations: ER = endoplasmic reticulum, UPR = unfolded protein reaction, ERAD = endoplasmic reticulum-associated degradation, PERK = protein kinase RNA-like ER kinase, IRE1α = inositol-requiring transmembrane kinase/endoribonuclease 1α, ATF6 = activating transcription factor 6, eIF2α = eukaryotic translation initiation factor 2A, TRAF2 = Tumor necrosis factor receptor-associated factor 2, ASK1 = Apoptosis signal-regulating kinase 1, and RIDD = regulated IRE1-dependent decay.</p

**ИИ:** + · обе модели · употребляющие + мера зависимости · Figure record from a study comparing regular kratom users with controls; reports odds of kratom use disorder, so prevalence is likely available.

**Решение:** =

---

### 103 · R1541

**The association between the kratom use characteristics, targeted ER stress sensor protein expression (BiP, sXBP1, ATF4, CHOP, JNK, and p-JNK) and substance use disorder related to kratom use among regular kratom users after controlling for confounding factors (such as age, cigarette smoking, and blood pressure) in a multiple logistic regression model.**

2023 · https://doi.org/10.1371/journal.pone.0287466.t001

The association between the kratom use characteristics, targeted ER stress sensor protein expression (BiP, sXBP1, ATF4, CHOP, JNK, and p-JNK) and substance use disorder related to kratom use among regular kratom users after controlling for confounding factors (such as age, cigarette smoking, and blood pressure) in a multiple logistic regression model.</p

**ИИ:** + · обе модели · употребляющие + мера зависимости · Supplementary item from a study of regular kratom users that modelled kratom-related substance use disorder, so prevalence is likely reported.

**Решение:** =

---

### 104 · R1542

**The blood investigation of the participants.**

2023 · https://doi.org/10.1371/journal.pone.0287466.s006

Background and aimsKratom (Mitragyna speciosa Korth.) is widely use worldwide despite its addictive potential. Although psychostimulant use has been linked to occurrence of endoplasmic reticulum (ER) stress, data is lacking on how regular kratom use affects ER stress. This case-control study first determined differences in ER stress sensor protein expression (BiP, sXBP1, ATF4, CHOP, JNK, and p-JNK) between regular kratom users and healthy controls. Second, it evaluated the association between kratom use characteristics, targeted ER stress sensor protein expression, and “kratom use disorder” diagnosed with Diagnostic and Statistical Manual for Mental Disorders 5th Edition (DSM-5) among regular kratom users.MethodsIn total, 60 regular kratom users and 50 healthy control-group participants were recruited and administered a sociodemographic and clinical characteristics questionnaire. While participants who used kratom were also administered a kratom use characteristics questionnaire. Blood samples were collected from all participants, and targeted ER stress sensor protein expression was determined via Western blot analysis.ResultsThe study’s findings revealed first that kratom users registered significantly higher protein expression in all targeted ER stress sensors compared to the control group. Second, higher protein expression of CHOP (B = 5.061, standard error [SE] = 2.547, Wald = 3.948, adjusted odds ratio [AOR] = 5.382, 95% confidence interval [CI] = 1.071 to 9.656, p = 0.047) and p-JNK (B = 5.795, SE = 2.635, Wald = 4.544, AOR = 17.025, 95% CI = 1.395 to 24.123, p = 0.017) increased the odds of kratom use disorder occurrence. Kratom use characteristics and other ER stress sensor protein expression were not associated with kratom use disorder.ConclusionRegular kratom use may induce protracted ER stress, leading to the decompensation of the unfolded protein response to maintain ER homeostasis. This effect may be linked to kratom use disorder occurrence.</div

**ИИ:** + · обе модели · употребляющие + мера зависимости · Supplementary file of a case-control study of 60 regular kratom users that diagnosed DSM-5 kratom use disorder.

**Решение:** - качественное исследование (интервью)

---

### 105 · R1543

**The differences in targeted ER stress sensor protein expression between regular kratom users and healthy non-drug using controls computed using Mann Whitney U test.**

2023 · https://doi.org/10.1371/journal.pone.0287466.g002

From the findings above, the median ER stress sensors protein expression (BiP, sXBP1, ATF4, CHOP, JNK and p-JNK) of the regular kratom users were all significantly higher than that of the healthy controls (all p values < 0.001). A = Photographic representation of the Western blot band of targeted ER stress sensors relative to β-actin band. Abbreviations: BiP = binding immunoglobulin protein, sXBP1 = spliced X-box-binding protein 1, ATF4 = activating transcription factor 4, JNK = c-Jun N-terminal kinase, p-JNK = phosphorylated c-Jun N-terminal kinase, CHOP = CCAAT-enhancer-binding protein homologous protein.</p

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Figure from a study of regular kratom users vs controls; the parent article may report dependence in its sample description.

**Решение:** =

---

### 106 · R1547

**Data sharing for research article entitled "Kratom Use Disorder and Unfolded Protein Response: Evaluating Their Relationship in a Case Control Study" published in Plos One.**

2023 · Figshare · dataset/dataset, dataset · en · https://doi.org/10.6084/m9.figshare.23440895

Kratom (Mitragyna speciosa Korth), traditionally used as remedies for various illnesses in Southeast Asia, is currently widely used globally to improve mood and anxiety, enhance endurance, and as a self-prescribed replacement for opioid dependence and as an analgesic for chronic pain. Despite its therapeutic potential, its capacity to induce withdrawal symptoms on abstinence and risk of kratom dependence due to its opioid-like effects has been a major drawback to its potential as a therapeutic agent. Endoplasmic reticulum (ER) stress occurred when there is a perturbation of protein folding in the ER lumen which leads to the accumulation of misfolded and unfolded protein in ER. Unfolded protein response (UPR) occurred upon ER stress which aims to counteract ER stress by reducing unfolded or misfolded protein to maintain ER homeostasis. However, if UPR is incapable of counteracting ER stress, the persistent occurrence of ER stress will ultimately lead to cell apoptosis. Psychostimulant use (methamphetamine and cocaine) has been linked to occurrence of ER stress. Despite kratom does exhibit psychostimulant properties, data on how regular kratom consumption and ER stress are link to kratom use disorder is lacking. Hence, this study filled the research gap by: [1] comparing ER stress sensor protein expression (BiP, XBP1, ATF4, CHOP, JNK, and p-JNK) between regular kratom users and healthy non-drug using controls, [2] determining the association between kratom use characteristics, targeted ER stress sensor protein expression, and “kratom use disorder” diagnosed with Diagnostic and Statistical Manual for Mental Disorders 5th Edition (DSM-5) among regular kratom users. In this study, we recruited 60 regular kratom users and 50 healthy control subjects and they were administered: demographic and clinical characteristics questionnaire (all participants), the kratom use characteristics questionnaire and DSM-5 diagnostic criteria for substance use disorder related to kratom use (only kratom users). Blood samples were collected from all participants and targeted ER stress sensor protein expression was analyzed with Western blotting. Our findings revealed that the relative protein expression of all the targeted ER stress sensors was higher among kratom users compared with healthy controls. In addition, the relative protein expression of CHOP, JNK, and p-JNK was higher compared to that of BiP, XBP1, and ATF4 among the kratom users. Higher protein expression of CHOP and p-JNK increased the odds of kratom use disorder occurrence. Kratom use characteristics and other ER stress sensor protein expression were not associated with kratom use disorder. Hence, we conclude regular kratom use may induce protracted ER stress leading to the decompensation of UPR to maintain ER homeostasis. This may link to higher odds of kratom use disorder. </p

**ИИ:** + · обе модели · употребляющие + мера зависимости · Dataset for a case-control study of 60 regular kratom users assessed with DSM-5 kratom use disorder criteria; judged by the parent article.

**Решение:** =

---

### 107 · R1559

**Factors associated with drug use during pregnancy and breastfeeding among females who use drugs (FWUDs) in Malaysia.**

2023 · Journal of ethnicity in substance abuse · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1080/15332640.2021.2019162

Females who use drugs (FWUDs) are at risk of continuing illicit substance use during pregnancy and breastfeeding. We investigated the prevalence rates and factors associated with these practices in a sample of 200 FWUDs recruited from a publicly-run drug rehabilitation center. A semi-structured questionnaire was used to collect the data. The majority (86%) was Malay (n = 171/200), currently single (71%, n = 141/200), and 51% had nine years of education. The mean age of respondents was 32.2 years (SD = 8.61). Thirty-eight percent (n = 75/200) reported ever using illicit substances during pregnancy, while 15% (n = 30/200) had used them during breastfeeding. Higher odds of using drugs during pregnancy were associated with having an intimate male drug-using partner and with persons who reported abandoning an infant in the past. Lower odds were linked with women who used heroin with ATS (relative to those who used only ATS), and shorter-term ATS (≤3 years) relative to long term ATS users. At a lower level of significance (p = 0.054), being married also lowered the odds. Higher odds of drug use during breastfeeding were associated with having an intimate male drug-using partner, and previous methadone use history, while lower odds were associated with short-term ATS use and being employed. The findings highlight the need for timely and targeted interventions to inform, engage and promote the participation of FWUDs in pre- and post-natal care services.

**ИИ:** разошлись — Opus -6 (не про кратом (другие виды Mitragyna) или не про людей, которые его употребляют: Study of drug use in pregnancy among Malaysian women in rehabilitation; centres on ATS and heroin, never mentions kratom or kratom dependence.); Sonnet ? (неясно, оценивали ли зависимость: Malaysian female drug users in rehab; kratom not mentioned in abstract, but kratom use and dependence could appear in the full text.)

**Решение:** - выборка пациентов набрана по обращению за лечением кратома

---

### 108 · R1587

**Kratom Use Among Pregnant and Lactating Individuals With Substance Use Disorder.**

2023 · Journal of addiction medicine · article, conference paper, journal article · eng · https://doi.org/10.1097/adm.0000000000001212

OBJECTIVE: Kratom ( Mitragyna speciosa ) use in pregnancy is associated with maternal and neonatal opioid withdrawal syndrome. However, kratom use patterns in the population of peripartum and postpartum individuals with substance use disorder (SUD) are unknown. The aim of this study was to determine the proportion of pregnant and postpartum individuals with SUD who report using kratom in pregnancy or lactation and the reasons for their use. METHODS: We conducted an anonymous survey of pregnant and postpartum individuals receiving care at a single center's multidisciplinary prenatal clinic for individuals with SUD. We collected participants' demographic and pregnancy characteristics. We assessed ever use of kratom, kratom use during pregnancy or lactation, and reasons for kratom use. Descriptive statistics were used to summarize the data. RESULTS: From January 2021 to May 2021, a total of 80 surveys were collected (81% response rate of 98 eligible individuals). Most respondents were pregnant (n = 50 [62.5%]). The most frequent substance(s) of use were opioids (n = 50 [62.5%]) and methamphetamine (n = 39 [48.8%]). Many (n = 26 [32.5%]) reported ever use of kratom use. Of all respondents, 4 (5%) reported use during pregnancy, and 1 (1%) reported use during lactation. Kratom was primarily used to relieve opioid withdrawal symptoms and for relaxation, pain control, and stress relief. CONCLUSION: In a survey of pregnant and postpartum individuals with SUD at a single high-risk pregnancy clinic, ever use of kratom was frequent, whereas peripartum use was rare.

**ИИ:** разошлись — Opus -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: Survey of pregnant/postpartum SUD patients assessed only kratom ever use, peripartum use and reasons; no kratom dependence measure.); Sonnet ? (неясно, оценивали ли зависимость: Survey of pregnant/postpartum SUD patients on kratom use; abstract reports no kratom dependence measure, but a sample table might include one. Check full text.)

**Решение:** - опрос беременных с расстройствами употребления ПАВ: только факт употребления кратома, нет меры зависимости кратома

---

### 109 · R1603

**Electrocardiogram Analysis for Kratom Users Utilizing Deep Residual Learning Network and Machine Learning**

2023 · Canadian Journal of Electrical and Computer Engineering · article, journalarticle, journal-article · en · https://doi.org/10.1109/icjece.2023.3320103

Kratom (Mitragyna speciosa Korth) is a common tropical plant found in Southeast Asia. Its leaves possess medicinal properties and are used to treat various ailments. However, the effects of kratom extract in terms of biological domains are still concerning. Although considerable studies have been conducted on the effects of kratom usage over the last few years, no study using in silico analysis of kratom users’ electrocardiogram (ECG) has been reported to date. This study aims to examine the long-term effects of kratom consumption using the ECG signals and deep learning (DL) network and machine learning techniques. Raw ECG signals were used as input for training and detecting abnormalities, and a deep residual learning network (DRLN) model was implemented to develop a feature extractor from single-lead datasets; the extracted features were used to train conventional machine learning classifiers. The confounding ECG abnormality factors, namely, age, sex, smoking, alcohol consumption, and exercise, were analyzed for association using the chi-square test. The main results of our study showed that kratom usage is not associated with ECG abnormalities. However, the ECG signal was affected more by gender than by the other factors; it exhibited the highest sensitivity and specificity (score = 0.63). While this study is limited to ECG abnormalities, the results indicate that long-term usage of kratom for its health benefits may be considered a safe and natural practice.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · ECG study of long-term kratom users; the abstract doesn't mention assessing dependence, though the sample table may report it.

**Решение:** =

---

### 110 · R1604

**(185) Over the Counter Kratom Use and Its Implications on Ejaculatory Dysfunction**

2023 · The Journal of Sexual Medicine · article, journalarticle, review · en · https://doi.org/10.1093/jsxmed/qdad060.178

Abstract Introduction The United States opioid epidemic remains responsible for 75,673 overdose deaths in 2021. Self-medication with kratom, a Southeastern Asian plant containing the mu opioid receptor agonists mitragynine and 7-hydroxymitragynine, is becoming increasingly prevalent. Kratom is legally available in most states with purported benefits in the self-treatment of opiate withdrawal and mood disorders. Anecdotal data linking kratom to male sexual health enhancement have not been formally investigated. Objective To objectively investigate the potential effect of kratom use on men's sexual health including ejaculatory and erectile function. Methods Under IRB approval, Twitter and Reddit (r/Kratom) were accessed to disseminate our survey featuring validated instruments (IIEF and the premature ejaculation diagnostic tool, PEDT). Sexual health prior to and after four weeks of kratom use were assessed. Descriptive statistics were used to ascertain differences between ejaculatory and erectile function with kratom use. Results Most males surveyed (n =165) were 18-40 years old (84.9%) and were white (86.7%). When examining kratom use, 82.4% (n= 136) of males used kratom for 1 or more years, with 95.8% using it at least weekly. Reasons for using kratom included an illicit drug dependency (17.6%), a prescription medicine dependency (14.5%), acute or chronic pain (39.4%), a mental health condition (63.6%), and issues with sexual health (4.8%). Of the 156 sexual health responses, 37.7% (n=59) and 20.5% (n=32) reported kratom having a positive and negative impact on their sexual health, respectively. Kratom use lead to increased time to ejaculation in 104 (66.6%) patients which was perceived as positive by 62 (59.6%). A subset of patients (n=78) answered questions about premature ejaculation prior to and after 4 weeks of kratom use. The mean pre and post kratom premature ejaculation diagnostic tool (PEDT) scores were 13.0 +/− 0.6 and 8.3 +/− 0.4 respectively (p &amp;lt; 0.001). Ejaculation prior to 5 minutes was improved after kratom use (n=40; 51.3% vs. n=10; 12.8%) (p &amp;lt; 0.0001). Post kratom use, more patients reported lack of frustration with ejaculation prior to desire (n=17; 21.8 % vs. n=48; 61.5%) (p &amp;lt; 0.001). Kratom users were unlikely to report concerns regarding fertility (n=1, 6.1%), testosterone levels (n=25, 15.2%), libido (n=38, 23.0%), or erectile dysfunction (ED) (n=30, 18.2%). The mean International Index of Erectile Function score was decreased with kratom use (26.6 +/− 0.6 vs. 25.9 +/− 0.5) (p &amp;lt; 0.05). Users rarely stopped kratom due to concerns regarding delayed ejaculation (n=5, 10%), low libido (n=8, 7.5 %), or ED (n=6, 7.9%). Conclusions Kratom users report delayed ejaculation, overall benefits to their sexual health, and a statistically significant impact on erectile function with kratom use. Clinicians treating male sexual health should be aware of kratom and its potential effect on ejaculatory and erectile function. Disclosure Any of the authors act as a consultant, employee or shareholder of an industry for: Boston Scientific.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Online survey of male kratom users on sexual health; abstract doesn't say whether kratom dependence or use disorder was assessed.

**Решение:** =

---

### 111 · R1605

**Investigating the Impact of Kratom (Mitragyna speciosa) Use Upon Male Sexual Health.**

2023 · Research and reports in urology · article, journal article, journalarticle · eng · https://doi.org/10.2147/rru.s390094

Nicholas A Deebel,1 Kyle Scarberry,2 Collette A O’Connor,1 Rahul Dutta,1 Ethan Matz,1 Colleen A Hanlon,3 Ryan P Terlecki1 1Department of Urology, Atrium Health Wake Forest Baptist Medical Center, Winston-Salem, NC, USA; 2Department of Urology, University Hospitals Cleveland Medical Center, Cleveland, OH, USA; 3Department of Cancer Biology, Wake Forest University School of Medicine, Winston-Salem, NC, USACorrespondence: Ryan P Terlecki, Department of Urology, Atrium Health Wake Forest Baptist Medical Center, 1 Medical Center Blvd, Winston-Salem, NC, 27157, Tel +1 336 716 4131, Fax +1 336 716 9042, Email rterlecki@wakehealth.eduPurpose: Kratom (Mitragyna speciosa) exhibits μ-receptor agonism and is used as an opioid substitute. While opioids are known to inhibit sexual behavior, less is known regarding kratom. We conducted a pilot study to assess the subjective impact of kratom upon male sexual health including erectile and ejaculatory function.Patients and Methods: Twitter and Reddit (r/Kratom) were accessed to disseminate our survey featuring validated instruments (the International Index of Erectile Function, IIEF, and the premature ejaculation diagnostic tool, PEDT). Sexual health prior to and after 4 weeks of kratom use was assessed.Results: Most males surveyed (n = 165) were 18– 40 years old (84.9%), with 95.8% of respondents using it at least weekly and 82.4% using kratom for ≥ 1 year. Reasons for use included treating pain (39.4%), and mental health conditions (63.6%). Kratom was associated with a positive (37.7%) and negative (20.5%) impact on sexual health. Kratom subjectively increased time to ejaculation in 104 (66.6%) patients, perceived as positive by 62 (59.6%). Seventy-eight patients answered questions about premature ejaculation. The median (with interquartile range, IQR, following;) pre-kratom and kratom use scores were 13.0; 8.0 and 6.5; 5.0, respectively (p < 0.001). Ejaculation before 5 minutes improved after kratom (51.3% vs 12.8%) (p < 0.0001). Following kratom use, patients reported lack of frustration with ejaculation prior to desire (21.8% vs 61.5%) (p < 0.001). The erectile function domain of the IIEF was statistically significantly different however – clinically similar pre-kratom use (29.0; 5.75) versus 27.0; 6.75 during kratom use (p = 0.037).Conclusion: Clinicians treating male sexual health should be aware of kratom and its potential effect on ejaculatory and erectile function.Keywords: kratom, Mitragyna speciosa, premature ejaculation, analgesia, sexual function

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Online survey of male kratom users on sexual health; abstract doesn't say whether dependence or use disorder was assessed.

**Решение:** - токсикологический обзор / серия случаев

---

### 112 · R1607

**Study on kratom usage effects at respiratory centre (brain stem) by functional MRI**

2023 · Universiti Sains Malaysia Institutional Repository (Universiti Sains Malaysia) · dissertation, review · en · https://core.ac.uk/download/667572145.pdf

Background: Mitragyna speciosa (Korth.) or kratom is an indigenous medicinal plant native to Southeast Asia, a tropical tree (Mitragyna speciosa) that contains compounds that can have psychotropic effects. Kratom leaves can be freshly chewed or by decoction preparation for herbal use. Kratom has effects similar to both opioids and stimulants. Despite increasing usage across the globe, the potential side effects and respiratory depression due to prolonged use of kratom are still unclear. Functional magnetic resonance imaging (fMRI) is a non-invasive imaging method for measuring brain activity by detecting neurophysiological changes in cerebral blood flow to predict neuronal activation in the brain. Methods: 22 regular kratom adult kratom users and 20 non-kratom users who underwent fMRI for prior research were included in this cross-sectional study. A non-invasive neuroimaging technique measuring brain activity by detecting neurophysiological changes in the cerebral blood flow and thus predicting neuronal activation within the brain. The activation on fMRI images were transferred to SPM format and calculated using Mathlab SPM12. Results: Area of brain activation referred to kratom group was calculated P<0.05, at least, 4487 (Z value 6.78) and at P< 0.001 noted 10300(Z value 6.78). While, area of brain activation in non-kratom user group was calculated, noted at P< 0.05 only 5 (Z value 5.2) and at P<0.001, no activation was depicted at brainstem. This suggests respiratory depression in the brainstem noted within Kratom users. Conclusion: Overall study shows long-term consumption of kratom is associated with respiratory depression affecting the brainstem within Kratom users as we noted significant activation- higher cluster level seen within brainstem. On the other hand, minimal activation noted within the brainstem in non Kratom users. However, further studies are needed to establish more data on use of kratom and its effects on brain function using more invasive and diagnostic methods like analysing blood gas parameters for more accurate results.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · fMRI study of 22 regular kratom users; abstract doesn't say whether dependence was measured, but sample description might report it.

**Решение:** =

---

### 113 · R1618

**Assessments of cognitive state of Mitragyna speciosa (ketum) users during relaxation state**

2023 · AIP conference proceedings · article, conference, conference paper · en · https://doi.org/10.1063/5.0115271

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; this is a conference paper on the cognitive state of ketum users and might report dependence characteristics.

**Решение:** =

---

### 114 · R1621

**Polysubstance use profiles among US adults using Kratom (Mitragyna speciosa): A latent class analysis using The National Survey on Drug Use and Health (NSDUH).**

2023 · The American journal on addictions · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1111/ajad.13345

Background & Objectives: Kratom (Mitragyna speciosa) use is associated with polysubstance use (PSU) and use disorders. However, additional research on PSU heterogeneity in populations using this novel psychoactive substance is necessary. The authors investigated patterns of past 12-month PSU among U.S. adults reporting past 12-month use of kratom and at least one additional substance. Methods: Latent class models were fit using 2019 National Survey on Drug Use and Health (NSDUH) data which was collected from 412 U.S. adults reporting past 12-month use of kratom and at least one of 11 additional substances. Results: Three distinct profiles were identified: “marijuana/alcohol/tobacco (MAT)” (63.3%), “marijuana/alcohol/tobacco + psychedelics (MAT+P)” (19.3%), and “marijuana/alcohol/tobacco + psychedelics/heroin/prescriptions (MAT+PHPR)” (17.4%). Conclusions & Scientific Significance: This is the first epidemiological study in which a latent class analysis was used to identify unique PSU profiles among US adults using kratom and other substances. Understanding the profiles of people using kratom in relation to the use of other drugs might help guide screening interventions, treatment needs, and policy.

**ИИ:** разошлись — Opus -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: NSDUH 2019 asked only about past-year kratom use, with no kratom dependence items; the study examines patterns of use with other substances.); Sonnet ? (неясно, оценивали ли зависимость: NSDUH 2019 sample of 412 US adults using kratom; abstract does not say whether kratom use disorder or dependence was assessed, so full text is needed.)

**Решение:** - опрос молодежи в США: только восприятие риска и доступность, без меры зависимости

---

### 115 · R1633

**Proceedings of the 2023 Cannabis Clinical Outcomes Research Conference (CCORC) Orlando, FL, USA, May 18 19, 2023**

2023 · Medical Cannabis and Cannabinoids · conference paper · https://doi.org/10.1159/000534044

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: Cannabis conference proceedings with no abstract; might include kratom survey abstracts (e.g., UF researchers), so check the full text.); Sonnet -6 (не про кратом (другие виды Mitragyna) или не про людей, которые его употребляют: Cannabis conference proceedings front matter with no abstract; the title is not about kratom or kratom dependence.)

**Решение:** - материалы конференции по каннабису, титульный лист

---

### 116 · R1635

**Correlations of kratom (Mitragyna speciosa Korth.) tea bag preparations and reported pharmacological effects.**

2023 · Journal of ethnopharmacology · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.jep.2023.116779

Ethnopharmacological relevance The use of herbal tea infusions is widespread in ethnomedicine throughout the world. One such ethnobotanical is kratom (Mitragyna speciosa Korth., Rubiaceae) which has gained considerable interest as an herbal supplement in recent years in the West beyond its native Southeast Asia. Traditional, kratom leaves are either chewed fresh or made into a tea infusion to treat fatigue, pain, or diarrhea. However, dried kratom leaf powder and hydroalcoholic extracts are more commonly used in Western countries, raising the question of exposure to kratom alkaloids and related effects. Aim of the study A specific kratom tea bag product was analyzed for mitragynine content using tea infusion preparation and methanolic extraction. Consumers of both the tea bag product and other kratom products completed an online anonymous survey to determine demographics, kratom use patterns, and self-reported beneficial and detrimental effects. Materials and methods Kratom tea bag samples were extracted using pH-adjusted water or methanol and analyzed using an established LC-QTOF method. A modified kratom survey was distributed to consumers of the kratom tea bag products and other kratom products over a 14-month period. Results Tea infusion extraction of tea bag samples resulted in lower mitragynine levels (0.062-0.131% (w/w)) compared to methanolic extraction (0.485-0.616% (w/w)). Kratom tea bag consumers did report similar, although often milder beneficial effects compared to consumers using other kratom products. Overall self-reported health was better among kratom tea bag consumers whereas improvement of a diagnosed medical condition was less in tea bag consumers compared to those using other kratom products. Conclusions Traditional tea infusions of Mitragyna speciosa dried leaves provide benefits to consumers despite substantially lower mitragynine content. These effects may be less pronounced but indicate that tea infusions provide a potentially safer formulation compared to more concentrated products.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Online survey of kratom consumers covering detrimental effects; the abstract does not say whether dependence or use disorder was assessed.

**Решение:** =

---

### 117 · R1636

**Correlations of kratom (Mitragyna speciosa Korth.) use behavior and psychiatric conditions from a cross-sectional survey.**

2023 · Experimental and clinical psychopharmacology · article, journalarticle, review · eng · https://doi.org/10.1037/pha0000632

Abstract Kratom ( Mitragyna speciosa Korth.) use has increased substantially over the past decade outside of its indigenous regions, especially for the self-treatment of psychiatric conditions. An anonymous, cross-sectional, online survey was completed by 4,945 people who use kratom (PWUK) between July 2019 and July 2020. A total of 2,296 respondents completed an extended survey utilizing clinical scales for attention deficit hyperactivity disorder (ADHD), post-traumatic stress disorder (PTSD), depressive and anxiety disorders.PWUK and met criteria for ADHD, PTSD, depressive or anxiety disorders were primarily middle-aged (31-50 years), employed, more likely to have college-level education (81.3% vs. 80.0%), and reported increased concurrent or prior use of kratom with cannabis products, cannabidiol, and benzodiazepines. In all psychiatric conditions, PWUK reported less depressive and anxious moods. Self-reported quality of life was worse in psychiatric conditions whereas current pain was more severe. Based on this observational study, further clinical studies are warranted for kratom.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Large online survey of people who use kratom; abstract doesn't say whether kratom dependence or use disorder was assessed.

**Решение:** =

---

### 118 · R1657

**Examining the Psychoactive Differences between Kratom Strains.**

2023 · International journal of environmental research and public health · article, preprint, journal article · eng · https://doi.org/10.3390/ijerph20146425

Kratom ( Mitragyna speciosa ) is a Southeast Asian plant containing various alkaloids that induce pharmacological effects in humans. In Western countries, online vendors sell a variety of different kratom strains which are marketed to have distinct effect profiles. However, as of yet such marketing claims are unsubstantiated, and therefore the current study investigated whether differently colored kratom products can induce distinct effects, as self-reported by users. Six hundred forty-four current kratom users were anonymously surveyed to compare the self-reported effects of and motivations for using kratom products sold as red, green, and white strains. Most of the survey respondents were customers of the same kratom vendor, the products of which had been analyzed for their alkaloid content by an independent laboratory. The survey respondents reported distinct subjective experiences for different kratom strains, in a manner congruent with common marketing descriptions. However, the product analyses revealed no significant cross-strain differences in alkaloid content, suggesting that the reported effect differences might be disproportionally influenced by marketing narratives and anecdotal reports. Future studies should engage a more diverse population and include kratom strains from various vendors. Controlled, blinded experiments could assess whether the reported effect differences stem from a placebo effect or from alternative factors, e.g., minor alkaloids and terpenes.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of 644 current kratom users about strain effects and motives; the abstract doesn't say whether dependence or use disorder was assessed.

**Решение:** ? онлайн-опрос потребителей кратома в США: мотивы и эффекты, зависимость может быть в анкете

---

### 119 · R1669

**Development and validation of ELISA for screening of Kratom (Mitragyna speciosa) habitual users using urinary AZ122 biomarker.**

2023 · Biotechnology and applied biochemistry · article, journal article, journalarticle · eng · https://doi.org/10.1002/bab.2392

Abstract Kratom ( Mitragyna speciosa Korth) has been used traditionally in Southeast Asia for its therapeutic properties. The major alkaloid of kratom, mitragynine, binds to opioid receptors to give opioid‐like effects that causes addiction. In our previous study, we have identified AZ122 as a unique biomarker in habitual or regular kratom users through analysis of their urinary protein profiles. We aimed to develop and validate a screening method by means of enzyme‐linked immunosorbent assay (ELISA) for detection of kratom habitual users. An ELISA approach was applied for the development of a screening method using urinary AZ122 as biomarker. Method validation was carried out using three quality control materials at different concentration of AZ122. The data was analyzed statistically using SPSS (Version 25). The ELISA was presented with Pearson correlation coefficient of 0.9993. The repeatability and reproducibility were presented at CV &lt;7%, while the accuracy ranged from 78 to 96% at various AZ112 concentrations. Upon testing on 176 male respondents ( n = 88 regular kratom users and n = 88 healthy controls), the specificity and sensitivity of the assay were both 100%. The ELISA has been validated and can be potentially used as a reliable screening test for detection of kratom habitual users.

**ИИ:** разошлись — Opus ? (неясно, оценивали ли зависимость: Mainly a lab assay validation, but it tested 88 regular kratom users. The sample description might report dependence; the abstract doesn't say.); Sonnet -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: Urinary biomarker ELISA validation in regular kratom users versus controls; no dependence or use-disorder measure reported.)

**Решение:** - валидация лабораторного теста ELISA, не эпидемиологический опрос

---

### 120 · R1683

**Exploring adolescents' practice and perspective on the use and misuse of kratom in northwest Malaysia.**

2023 · Journal of ethnicity in substance abuse · article, journal article, journalarticle · eng · https://doi.org/10.1080/15332640.2021.1906816

Abstract Kratom is a plant homogenous to Southeast Asia with a long history of traditional use as medicinal herbs. However, recent years have witnessed its pervasive infiltration into international audience with growing public health concern. This cross-sectional study was conducted from 1 August 2017 till 31 August 2018 aiming to explore the practice and perspectives of kratom use and misuse among adolescents in northwest Malaysia. The study involved a self-administered questionnaire that was designed for the purpose of the study. The instrument had undergone prior validation process with a good overall internal reliability for the knowledge domain (Cronbach’s alpha = 0.728) and attitude domain (Cronbach’s alpha = 0.700). The questionnaire was distributed to 135 respondents involving adolescents aged 13 to 19 years old via convenience (non-kratom user) and snowball sampling (kratom users). There were 65 (47.8%) kratom users, while 70 (51.5%) were kratom-naïve. Among the kratom users, peer influence was the most common reason for them to be first involved with kratom, 26 (41.3%) whereas the reasons for kratom use quoted were to improve physical stamina, 10 (16.4%), as painkiller, 9 (14.8%), and to be accepted by peers, 7 (11.5%). Multiple logistic regression found that older age (95% CI: 0.13, 0.58; p = 0.001) and being active smokers (95% CI: 39.33, 980.63; p < 0.001) significantly predict kratom use among adolescents. The emerging trend of kratom abuse and misuse especially among the younger generation in Malaysia is raising concern and warrants social and governmental vigilance.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Adolescent survey with 65 kratom users covering use and misuse; abstract doesn't say whether dependence or use-disorder items were measured.

**Решение:** =

---

### 121 · R1693

**Ketum (Mitragyna Speciosa Korth.) Consumption, Lipid Profile And Electrocardiogram (Ecg) Abnormalities**

2023 · review · https://core.ac.uk/download/611566062.pdf

Ketum (Mitragyna speciosa Korth.) a native medicinal plant of Southeast Asia, has been used in Malaysia for decades for its unique curative properties. Given its broad therapeutic properties and increasing utility, ketum’s long-term safety profile, especially on its cardiotoxicity risk remains poorly investigated in regular ketum users. Given this research limitation, this study aims to evaluate the electrocardiogram (ECG) abnormalities and lipid profile between regular ketum users and healthy control subjects. A total of 200 respondents (n=100 regular ketum users and n=100 healthy control subjects) were recruited through convenience sampling from the northern peninsular state of Penang for this clinical, cross-sectional study. All were required to undergo an ECG evaluation, and blood samples were also drawn to characterize the respondent’s lipid profile. All males, a majority were Malays (97%, n=194/200), and the samples mean age in this study was 33 years (SD=6.7), while ketum users mean duration of ketum use was 6.4 years (SD=4.31). Ketum users mean systolic and diastolic blood pressure rates were 132.9 beats per minute (SD=17.3) and 77.1 beats per minute (SD=11.1), respectively

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Clinical cross-sectional study of 100 regular ketum users; the abstract doesn't say whether dependence was assessed, though such samples often report it.

**Решение:** =

---

### 122 · R1719

**Užívání kratomu v České republice: dotazníkové šetření**

2023 · master thesis · ces/cze · http://www.nusl.cz/ntk/nusl-520890

Background: Kratom is a natural psychoactive substance origin to Southeast Asia, which use is expanding in the Czech Republic in recent years. The issue of kratom use is coming to the fore in 2022, mainly due to inappropriate regulation of kratom and reports of increasing kratom use not only among students and adults, but also among children and adolescents. So far, there is very little research data on the use of kratom in the Czech Republic. Objectives: The aim of the thesis was to find out and describe the patterns of kratom use in the population of its users in the Czech Republic. The research also focused on risk behaviors related to kratom use. The sub-goals of the research were to map the use of other psychoactive substances and to determine the connections with the use of kratom. Furthermore, to map the need of seeking professional help due to the kratom use, and to find out the opinion of kratom users on its legal regulation in the Czech Republic. Methods: The research was designed as a quantitative survey, a questionnaire was used to collect data, distributed in online form through social media. Data were collected from 23.10. to 6.11. 2022 and the research sample consisted of 1367 respondents. Data were analyzed in Microsoft Excel using descriptive statistics and pivot tables. Results:...

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Online survey of 1367 Czech kratom users covering risk behaviours and help-seeking; abstract truncated, so it is unclear whether dependence was measured.

**Решение:** =

---

### 123 · R1786

**Patterns of polysubstance use among adults in Malaysia-A latent class analysis.**

2023 · PloS one · article, other literature type, journal article · eng · https://doi.org/10.1371/journal.pone.0264593

INTRODUCTION: Polysubstance use is the use of more than one non-prescribed licit or illicit substance at one time. This is a common phenomenon, but little is known about the severity and the various substances used by adults in Malaysia. OBJECTIVE: To determine the pattern of polysubstance use and its associated factors among general adults in Malaysia. METHODOLOGY: This was a secondary data analysis from the National Health and Morbidity Survey (NHMS) 2019), a cross-sectional population survey with a two-stage stratified random sampling design. A total of 10,472 Malaysians aged 18 years and above participated in this survey. Polysubstance use was defined as concurrent use of more than one substance, either alcohol, tobacco, or drugs (opioids, marijuana, amphetamine/ methamphetamine or kratom). A latent class analysis (LCA) was used to identify the membership of polysubstance groups. The association of class membership with demographic profiles was examined using Multinomial Logistic Regression analysis. RESULTS: Fit indices (AIC = 16458.9, BIC = 16443.6) from LCA supported 3 classes solution: Class 1; "moderate-drug" group primarily combination used of tobacco and alcohol (2.4%), Class 2; "high-drug" group using multiple substance including kratom (0.3%) and Class 3; "low-drug" group reporting minimal alcohol and tobacco use or non-user (97.3%). The multinomial model showed young adults (18-40 years) had a higher likelihood of being polysubstance users both for moderate-drug class (OR = 4.1) and high-drug class (OR = 3.9) compared to older age (≥60 years). Chinese (OR = 18.9), Indian (OR = 23.3), Indigenous Sabah & Sarawak (OR = 34.6) and others ethnicity (OR = 8.9) showed higher odds of being moderate-drug users than Malays. The greater odds of moderate-drug use for males (OR = 35.5), working groups (OR = 1.5) and low education level group (OR = 3.2). CONCLUSION: Our study highlights patterns and demographics related to the use of polysubstances among adults in Malaysia. These results would help formulate specific prevention programmes for these high-risk groups.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Malaysian national survey (NHMS 2019) that included kratom use and mentions severity, possibly via ASSIST; whether kratom dependence was measured is unclear.

**Решение:** =

---

### 124 · R1803

**Using Kratom: Online and Local Stories of North Americans**

2023 · De Gruyter eBooks · part of book or chapter of book, book-chapter · en · https://doi.org/10.1515/9783986120184-018

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: Book chapter with no abstract; 'stories' suggests qualitative work, but survey data on North American kratom users can't be ruled out.); Sonnet -2 (качественное исследование без подсчёта людей (интервью, форумы, Reddit); доклиника: животные, клетки, химия, ботаника, анализ продуктов: Book chapter on online and local stories of North American kratom users; likely qualitative narrative analysis, no abstract, no dependence prevalence expected.)

**Решение:** - глава книги, качественные нарративы

---

### 125 · R1815

**Examining the paradoxical effects of kratom: a narrative inquiry.**

2023 · Frontiers in pharmacology · article, journal article, journalarticle · eng · https://doi.org/10.3389/fphar.2023.1174139

Introduction: Surveys and case reports have documented kratom use in the United States (US) for over a decade. However, those reports have generally not examined in depth the role kratom plays in the lives of those who use it regularly for sustained periods. Until there are controlled studies of the pharmacology and subjective effects of kratom alkaloids in humans, one of the best sources of insight on kratom-product use remains qualitative data with nuanced descriptions of kratom effects from those who use it regularly. Method: We conducted semistructured qualitative interviews with adults who regularly use kratom products, as part of a laboratory study of kratom-product self-administration. This qualitative component of the study was conducted as a narrative case-report series ( n = 10). Results: Despite some differences among participants, all experienced acute combination effects that were largely, even simultaneously, analgesic and stimulatory. Most participants had decreased their dosages over time, and one planned to quit. Five of the 10 participants met DSM-5-based criteria for kratom-use disorder (3 mild, 1 moderate, 1 severe, by symptoms counts). When kratom was inadvertently taken in larger than intended doses, participants described a constellation of symptoms that they called "the wobbles" (a jittery feeling accompanied by what seemed to be nystagmus); this was rare, but could be of scientific and clinical interest as a possible manifestation of serotonin syndrome. Most participants described tolerance but considered kratom generally safe at low-moderate doses, providing perceived benefits with less potential risk for adverse effects compared to pharmaceuticals or illicit drugs. Discussion: In-depth interview data like these help confirm and clarify findings from larger survey studies and clinician-driven case reports. They are needed to inform the policy practice regarding kratom and may also help inform future experimental designs.

**ИИ:** + · обе модели · употребляющие + мера зависимости · Qualitative part of a lab study of 10 regular kratom users; abstract reports 5/10 met DSM-5 kratom use disorder criteria.

**Решение:** ? опрос пациентов с хронической болью: употребление кратома и возможная зависимость

---

### 126 · R1820

**Knowledge and Understanding Kratom Consumption for Healthy of Teenagers in South of Thailand**

2023 · INTERNATIONAL JOURNAL OF MULTIDISCIPLINARY RESEARCH AND ANALYSIS · article, journalarticle, journalarticle/ · en · https://doi.org/10.47191/ijmra/v6-i5-37

The study explored the Knowledge and Understanding Kratom Consumption for Healthy of Teenagers in South of Thailand. The objective of this study to 1) Study knowledge and understanding Kratom Consumption for Healthy of Teenagers in South of Thailand. 2) Study factors related to knowledge and understanding Kratom Consumption for Healthy of Teenagers in South of Thailand. The questionnaire collected data of 400 samples and data were analyzed using SPSS program for frequency, percentage, mean, Chi- Square at statistical significance level 0.05. The most of sample are man and aged about 20 to 24 years and education level is Diploma. The income per month is 5,001-10,000 Bath and consumption period of Kratom is less than 1 month. The results of the hypothesis testing revealed that: 1) Demography factors did correlate with Knowledge and Understanding Kratom Consumption for Healthy of Teenagers in South of Thailand. 2) Motivation factors did correlate with Knowledge and Understanding Kratom Consumption for Healthy of Teenagers in South of Thailand.

**ИИ:** разошлись — Opus ? (неясно, оценивали ли зависимость: Questionnaire survey of 400 Thai youths who seem to use kratom; focuses on knowledge and motivation, and dependence assessment is not reported.); Sonnet -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: Questionnaire survey of 400 teenagers on knowledge and understanding of kratom consumption and motivation; no dependence or use disorder measure is mentioned.)

**Решение:** - опрос 400 подростков в Южном Таиланде: знания и мотивация, без меры зависимости

---

### 127 · R1829

**Identification And Development Of Urinary Protein Biomarker To Screen For Kratom Used In Regular Users**

2023 · review · https://core.ac.uk/download/611566254.pdf

Study aimed to characterize the urinary protein profile of regular kratom users to determine the impact of kratom on regular use of kratom. Furthermore, to identify a useful urinary biomarker that can be used to indicate kratom dependence and addiction by means of a screening method using ELIS

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Urinary biomarker study in regular kratom users aiming to indicate dependence; may have classified users by a dependence measure.

**Решение:** =

---

### 128 · R1857

**Kratom use disorder and unfolded protein response: Evaluating their relationship in a case control study.**

2023 · PloS one · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1371/journal.pone.0287466

BACKGROUND AND AIMS: Kratom (Mitragyna speciosa Korth.) is widely use worldwide despite its addictive potential. Although psychostimulant use has been linked to occurrence of endoplasmic reticulum (ER) stress, data is lacking on how regular kratom use affects ER stress. This case-control study first determined differences in ER stress sensor protein expression (BiP, sXBP1, ATF4, CHOP, JNK, and p-JNK) between regular kratom users and healthy controls. Second, it evaluated the association between kratom use characteristics, targeted ER stress sensor protein expression, and "kratom use disorder" diagnosed with Diagnostic and Statistical Manual for Mental Disorders 5th Edition (DSM-5) among regular kratom users. METHODS: In total, 60 regular kratom users and 50 healthy control-group participants were recruited and administered a sociodemographic and clinical characteristics questionnaire. While participants who used kratom were also administered a kratom use characteristics questionnaire. Blood samples were collected from all participants, and targeted ER stress sensor protein expression was determined via Western blot analysis. RESULTS: The study's findings revealed first that kratom users registered significantly higher protein expression in all targeted ER stress sensors compared to the control group. Second, higher protein expression of CHOP (B = 5.061, standard error [SE] = 2.547, Wald = 3.948, adjusted odds ratio [AOR] = 5.382, 95% confidence interval [CI] = 1.071 to 9.656, p = 0.047) and p-JNK (B = 5.795, SE = 2.635, Wald = 4.544, AOR = 17.025, 95% CI = 1.395 to 24.123, p = 0.017) increased the odds of kratom use disorder occurrence. Kratom use characteristics and other ER stress sensor protein expression were not associated with kratom use disorder. CONCLUSION: Regular kratom use may induce protracted ER stress, leading to the decompensation of the unfolded protein response to maintain ER homeostasis. This effect may be linked to kratom use disorder occurrence.

**ИИ:** + · обе модели · употребляющие + мера зависимости · Case-control study of 60 regular kratom users with DSM-5 kratom use disorder diagnosis; the full text should give the prevalence.

**Решение:** =

---

### 129 · R1861

**A Pilot Study of the Striatal Dopamine Transporter Levels in Kratom-Dependent and Normal Subjects Using 99mTc-TRODAT-1 Single Photon Emission Computed Tomography-Computed Tomography (SPECT-CT).**

2023 · Cureus · article, journal article, journalarticle · eng · https://doi.org/10.7759/cureus.43251

Objective The study aims to elucidate the effects of kratom addiction on dopamine transporter (DAT) using [2-[[2-[[[3-(4-chlorophenyl)-8-methyl-8-azabicyclo[3.2.1]oct-2-yl]methyl](2-mercaptoethyl)amino]ethyl]amino]ethanethiolato(3-)-N2,N20,S2,S20]oxo-[1R-(exo-exo)]-[ 99m Tc] technetium ( 99m Tc-TRODAT-1) brain single photon emission computed tomography-computed tomography (SPECT-CT) in kratom-dependent and healthy subjects. Materials and methods We recruited 12 kratom-dependent subjects and 13 healthy men to participate in this study. Addiction, craving, depression, and cognitive scores were assessed. All subjects received a single bolus injection of 99m Tc-TRODAT-1 with 914.1 MBq ± 65.5 of activity (mean ± SD). The brain SPECT-CT images were reconstructed using 3D ordered subset expectation maximization (3D-OSEM) along with attenuation correction (AC), scatter correction (SC), and resolution recovery (RR) with an iteration number of four and a subset of 10. The Cohen's Kappa interrater-reliability between two raters, the standardized uptake value of body weight (SUV BW ), and the asymmetrical index percentage (AI%) were evaluated. Results Kappa statistics showed a fine agreement of abnormal 99m Tc-TRODAT-1 uptake in the striatum region for the kratom-dependent group with the κ value of 0.69 (p = 0.0001), and the percentage of agreement for rater 1 and rater 2 was 56% and 64%, respectively. There was a reduction in average SUV in kratom-dependent subjects compared to healthy control subjects in the left caudate and left striatum (0.938 vs. 1.251, p = 0.014, and 1.055 vs. 1.29, p = 0.036, respectively). There was a significant difference in the AI% of the caudate region between the kratom-dependent group and the normal group (33% vs. 14%, p = 0.019). Conclusion Our findings signify that kratom addiction, may cause a change in DAT level and the results can be confirmed using 99m Tc-TRODAT-1 SPECT-CT.

**ИИ:** ? · обе модели · другое · Imaging study of 12 kratom-dependent men; addiction scores assessed, but unclear whether recruitment was of regular users or selected for dependence.

**Решение:** =

---

### 130 · R1866

**Elucidating The Effect Of Kratom On Striatal Dopamine Transporter Level Using 99mtc Trodat-1 Spect-ct In Kratom Users**

2023 · Universiti Sains Malaysia Institutional Repository (Universiti Sains Malaysia) · dissertation, review · en · https://core.ac.uk/download/755801162.pdf

Objective: To evaluate and compare striatal dopamine transporter (DAT) level in kratom users and healthy controls utilizing 99mTc-TRODAT-1 single photon emission computed tomography with computed tomography (SPECT-CT) and brain MRI. Methods: A cross-sectional study involving 12 kratom users and 13 healthy controls was done at Unit Perubatan Nuklear, Institut Perubatan dan Perubatan Termaju (IPPT) USM. All subjects were male, aged between 18 to 55 years old without neurological or psychological diseases. kratom users were dependent on kratom for more than a year period and were free from illicit drugs abuse. Urine toxicology was done to exclude illicit drug abuse. They were also screened using DSM-V criteria for opioid dependence along with PHQ-9 and MMSE questionnaires. All subjects underwent 99mTc-TRODAT-1 SPECT-CT and brain MRI. The standard uptake value corrected with body weight (SUVbw) of bilateral caudate, putamen and striatum as well as occipital were drawn guided structurally by brain MRI images which were co-registered with processed SPECT-CT images. SUVr was calculated by dividing the target SUV with the occipital SUV. Results: Qualitative evaluation by two nuclear medicine physician showed almost perfect agreement that there were reduced tracer uptake in the right putamen (κ=0.824, p=0.004) and left caudate (κ=0.824, p=0.004), consequently abnormal finding in the overall image (κ=1.0, p<0.001). Semiquantitative evaluation revealed significantly higher right caudate SUVr of 2.06±0.67 in kratom users compared to 1.51±0.31 in healthy controls (p=0.019), accordingly higher right striatum SUVr of 1.98±0.50 in kratom user compared to 1.62±0.37 in healthy controls (p=0.055). The right caudate to putaminal ratio was also significantly higher at 1.09±0.25 compared to 0.89±0.14 (p=0.026) accordingly. The caudate AI% was high at 32.97% in kratom users versus 14.37% in healthy controls (p=0.04). The questionnaires parameter showed no significant difference between group. Conclusions:In conclusion, chronic kratom usage causes significantly higher right caudate SUVr, mimicking a pattern more like a cocaine-stimulant effect rather than the chronic heroin pioid effect. Although the effect of smoking in kratom users on striatal DAT binding is inevitable in this study, 99mTc-TRODAT-1 SPECT-CT-MRI may still be used as a potential imaging modality to assess the effect of chronic kratom use with further investigations in the future.

**ИИ:** разошлись — Opus + (употребляющие + мера зависимости: Imaging study of regular kratom users not in treatment; screened with DSM-5 dependence criteria, which may give counts of those meeting criteria.); Sonnet ? (неясно, оценивали ли зависимость: SPECT study of 12 kratom users described as dependent and screened with DSM-5 opioid dependence criteria; unclear whether the number meeting criteria is reported, so full text is needed.)

**Решение:** + нейровизуализационное исследование потребителей кратома с оценкой критериев зависимости DSM-5

---

### 131 · R1888

**Peer Review #1 of "Exploring of cardiac autonomic activity with heart rate variability in long-term kratom (Mitragyna speciosa Korth.) users: a preliminary study (v0.1)"**

2022 · PeerJ · review, peer-review · en · https://doi.org/10.7287/peerj.14280v0.1/reviews/1

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Peer review of a study of long-term kratom users; judged by parent article. Unclear whether dependence was assessed.

**Решение:** =

---

### 132 · R1889

**Peer Review #2 of "Exploring of cardiac autonomic activity with heart rate variability in long-term kratom (Mitragyna speciosa Korth.) users: a preliminary study (v0.1)"**

2022 · PeerJ · review, peer-review · en · https://doi.org/10.7287/peerj.14280v0.1/reviews/2

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · другое · Peer-review record of a study of long-term kratom users; judged by its parent article, which may report dependence status. Retrieve the article.

**Решение:** ? опрос пациентов наркологических программ: употребление кратома и зависимость

---

### 133 · R1946

**The Prevalence and Psychosocial Correlates of Ketum (Mitragyna speciosa) Use among Individuals on Methadone Maintenance Therapy Programme in Hospital Taiping, Malaysia.**

2022 · Healthcare (Basel, Switzerland) · article, journal article, journalarticle · eng · https://doi.org/10.3390/healthcare10040746

Ketum use is significantly prevalent amongst individuals in the northern states of Peninsular Malaysia. This study aims to investigate the prevalence and psychosocial correlates of Ketum use in individuals who are in the Methadone Maintenance Therapy (MMT) Programme at the Hospital Taiping. This is a cross-sectional study conducted in the methadone clinic at the Hospital Taiping. The study instruments used were Subjective Opiate Withdrawal Scale (SOWS), Alcohol, Smoking and Substance Involvement Screening Test (ASSIST) questionnaire, and Kratom Dependence Scale (KDS). A total of 215 subjects were recruited for this study. The prevalence of ketum users was 49.3% ( n = 106). Chinese and Indian ethnicity had a lower tendency to use ketum compared to Malay ethnicity, with OR = 0.386 (95% CI 0.134, 1.113) and 0.119 (95% CI 0.035, 0.408), respectively. Individuals who used other illicit drugs had a higher tendency to use ketum with the adjusted OR = 9.914 (95% CI: 1.109, 88.602). Every one unit increase in SOWS increased the odds of being a ketum user by 1.340 (95% CI: 1.070, 1.677), whereas every one unit increase in duration in the MMT programme reduced the odds of being a ketum user by 0.990 (95% CI: 0.982, 0.998). Ketum use is prevalent amongst those in the MMT programme in this study. The high prevalence of ketum use is of concern and further interventions should be carried out to address this.

**ИИ:** + · обе модели · другая выборка, есть употребляющие и мера зависимости · Methadone patients; among 106 ketum users, dependence was measured with the Kratom Dependence Scale and ASSIST.

**Решение:** =

---

### 134 · R1947

**The prevalence and psychosocial correlates of ketum use among individuals on methadone maintenance therapy programme in Hospital Taiping / Choo, Ling Ling**

2022 · Universiti Malaya KNOVA - Knowledge Nexus and Open Vision Access · text

Background: Ketum use is significantly prevalent amongst individuals in northern states of Peninsular Malaysia. This study aims to investigate the prevalence and psychosocial correlates of Ketum use in individuals who are in the Methadone Maintenance Therapy (MMT) Programme in Hospital Taiping. Methods: This is a cross-sectional study conducted in the methadone clinic Hospital Taiping. Non-probability convenience sampling was used in this study. The study instruments used were Subjective Opiate Withdrawal Scale (SOWS), Alcohol, Smoking and Substance Involvement Screening Test (ASSIST) questionnaire, and Kratom Dependence Scale (KDS). Results: A total of 215 subjects were recruited in this study. The prevalence of ketum users was 49.3% (n=106). The factors which were significantly associated with ketum use (p \u3c 0.05) in MMT programme were ethnicity, duration in MMT programme, other illicit drugs use, and SOWS. Conclusion: Ketum use is prevalent amongst those in MMT programme in this study. The high prevalence of ketum use is of concern and further interventions should be carried out to address thi

**ИИ:** + · обе модели · другая выборка, есть употребляющие и мера зависимости · This thesis surveyed methadone patients and used the ASSIST and Kratom Dependence Scale; 106 of the 215 participants used ketum.

**Решение:** =

---

### 135 · R1970

**Regular Kratom ( Mitragyna speciosa Korth.) Use and Its Association With Endoplasmic Reticulum Stress Response.**

2022 · Journal of addiction medicine · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1097/adm.0000000000000988

OBJECTIVES: This study determined the association between expression of the endoplasmic reticulum (ER) stress sensor mRNA in the peripheral leukocytes and the patterns of kratom use and evaluated the correlations between the levels of the ER stress sensor mRNA and the severity of kratom dependence and kratom induced depressive symptoms among people who use kratom (PWUK). METHODS: A total of 20 PWUK and 20 age matched non-kratom using healthy controls were recruited. Data collected from PWUK included patterns of kratom use, severity of kratom dependence, and severity of depressive symptoms during abstinence from kratom. The mRNA expression of binding immunoglobulin protein ( BiP ), X-box binding protein 1, activating transcription factor 4, and C/-EBP homologous protein ( CHOP ) (major indicators of ER stress response) were analyzed using quantitative reverse transcription polymerase chain reaction in leucocyte-derived total RNA sample of the participants. RESULTS: PWUK regardless of their pattern of kratom use recorded significantly higher expression of BiP mRNA compared with controls. Expression of CHOP mRNA was only significantly higher in those who first consumed kratom at the age of 18 years and above and those who have been using kratom for longer than 6 years, compared with controls. Higher expression of BiP , ATF4 , and CHOP mRNA were significantly positive correlated with greater severity of kratom dependence. Although only higher expression of BiP and CHOP mRNA were significantly positively correlated with greater severity of depressive symptoms. CONCLUSIONS: Regular kratom consumption may activate the ER stress pathway and there may be a link between altered ER stress response and kratom dependence and kratom induced depressive symptoms.

**ИИ:** + · обе модели · употребляющие + мера зависимости · Twenty regular kratom users were assessed for severity of kratom dependence (likely KDS), so the full text may give how many were dependent.

**Решение:** =

---

### 136 · R1980

**Correlations of Kratom (Mitragyna speciosa Korth.) Use Behavior and Psychiatric Conditions from a cross-sectional survey**

2022 · Research Square · preprint, posted-content · https://doi.org/10.21203/rs.3.rs-1923353/v1

Abstract Kratom ( Mitragyna speciosa Korth.) use has increased substantially over the past decade outside of its indigenous regions, especially for the self-treatment of psychiatric conditions. An anonymous, cross-sectional, online survey was completed by 4,945 people who use kratom (PWUK) between July 2019 and July 2020. A total of 2,296 respondents completed an extended survey utilizing clinical scales for attention deficit hyperactivity disorder (ADHD), post-traumatic stress disorder (PTSD), depressive and anxiety disorders.PWUK and met criteria for ADHD, PTSD, depressive or anxiety disorders were primarily middle-aged (31-50 years), employed, more likely to have college-level education (81.3% vs. 80.0%), and reported increased concurrent or prior use of kratom with cannabis products, cannabidiol, and benzodiazepines. In all psychiatric conditions, PWUK reported less depressive and anxious moods. Self-reported quality of life was worse in psychiatric conditions whereas current pain was more severe. Based on this observational study, further clinical studies are warranted for kratom.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Large online survey of people who use kratom using clinical scales; abstract doesn't say if kratom dependence or use disorder was assessed.

**Решение:** =

---

### 137 · R1982

**Exploring the self-reported motivations of kratom (Mitragyna speciosa Korth.) use: a cross-sectional investigation.**

2022 · The American journal of drug and alcohol abuse · article, other literature type, journal article · eng · https://doi.org/10.1080/00952990.2022.2041026

ABSTRACT Background: Kratom (Mitragyna speciosa Korth.) use outside of Southeast Asia has increased over the past decade. Objectives: This investigation clarifies kratom’s role in perceived well-being, overall health, and temporal correlation with drug use to understand kratom’s role in the self-treatment of substance use disorders (SUDs). Methods: Between July 2019 and July 2020 an anonymous, cross-sectional, online survey was taken by 7,381 people who use kratom (PWUK) recruited through social media and other online resources. This included an assessment of (a) the relationship between self-reported overall health, concomitant use of drugs of misuse, and demographics; (b) the perceived effectiveness of kratom in self-treating diagnosed health conditions or symptoms; (c) the profile of PWUK primarily for drug dependence, pain, and mood or mental health conditions based on demographics. Results: A total of 5,152 valid responses (45.9% females/53.7% males) were collected. Kratom was primarily used for self-treating pain (73.0%) and improving emotional or mental health conditions (42.2%) without clinical supervision. Those with a SUD (synthetic opioids, methadone, benzodiazepines, or heroin) used kratom after discontinuing illicit or other drugs (94.8%). The primary substances taken before or concomitantly with kratom were cannabis, cannabidiol, benzodiazepines, or kava. PWUKs report a dose-dependent benefit for alleviating pain and relieving negative moods. Adverse effects were primarily gastrointestinal, typically at high (>5 g/dose) and frequent (>22 doses/week) dosing. Conclusions: Kratom was primarily used as a harm-reduction agent for SUDs and self-treatment of chronic conditions. Healthcare professionals need better information about kratom, its potential adverse effects, and clinically significant drug interactions.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Large online survey of people who use kratom; abstract does not say whether kratom dependence or use disorder was assessed.

**Решение:** =

---

### 138 · R1983

**How essential is kratom availability and use during COVID-19? Use pattern analysis based on survey and social media data.**

2022 · Substance abuse · article, journal article, research support, n.i.h., intramural · eng · https://doi.org/10.1080/08897077.2021.2007517

Background: Kratom, a tree native to Southeast Asia, is increasingly used in Western countries for self-treatment of pain, psychiatric disorders, and mitigation of withdrawal symptoms from drugs of abuse. Because kratom is solely supplied from its native locations, supply shortages during the COVID-19 pandemic may impact the availability of preparations and hence force consumers to change their patterns of use. The aim of this study was to understand if and how COVID-19 was influencing kratom purchasing and use. Methods: Additional questions specific to kratom availability and changes in use during COVID-19 were added to an international online survey with responses collected between January and July 2020. During the same period, kratom-related social media posts to Twitter, Reddit, and Bluelight were analyzed for themes similar to the survey questions. Results: The survey results indicated no changes in kratom use patterns although the sample size was relatively small ( n = 70) with younger consumers reporting a potential issue in obtaining their desired products from their usual sources. The survey respondents identified primarily as non-Hispanic whites (87.1%). Social media themes revolved primarily around quitting kratom during COVID-19, misinformation about the effects of kratom on COVID-19, and other non-COVID-related discussions. While some consumers may increase their kratom dose because of additional stress, a majority of discussions centered around reducing or rationing kratom due to COVID-19 or a perceived dependence. Access to quality kratom products was also a major discussion topic on social media. Conclusions: Kratom use patterns did not change due to COVID-19 but consumers were concerned about potential product shortages and resulting quality issues. Clinicians and public health officials need to be informed and educated about kratom use as a potential mitigation strategy for substance use disorders and for self-treatment of pain.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Online survey of kratom consumers (n=70) about COVID-19; the abstract does not say whether the parent survey assessed dependence or use disorder.

**Решение:** =

---

### 139 · R2010

**Prevalence of Drug and Substance Use among Malaysian Youth: A Nationwide Survey.**

2022 · International journal of environmental research and public health · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.3390/ijerph19084684

Uncontrolled drug and substance use (DSU) may pose unprecedented threats to nation building and a country&rsquo;s socioeconomic development. Despite considerable efforts made and resources used to address DSU concerns, Malaysia has seen a significant annual rise in cases of DSU. The bulk of the reported cases originate from youth between the ages of 15 and 40 years. To date, data related to DSU in Malaysia have been entirely dependent on operation statistics, arrest counts, and reported cases; DSU may therefore be under-reported and the data obtained not representative at the national level. This study aims to determine the prevalence of DSU among Malaysian youth through a large nationwide representative survey. Of the population of 11,129,316 youth aged 15&ndash;40 years, the prevalence of DSU among lifetime users was found to be 5.5%, while for those who had taken drugs in the past 30 days or who currently use them, the prevalence of DSU was found to be 3.5%. The most popular drugs for lifetime users were kratom or Mitragyna speciosa, while for current users the most popular drug was cannabis. The current study reports the magnitude of the problem at a country-wide level, which is a crucial preliminary effort for crafting evidence-based and well-informed policies

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Nationwide Malaysian youth survey; kratom was the most common lifetime drug. Unclear whether kratom dependence was measured (e.g., ASSIST).

**Решение:** =

---

### 140 · R2012

**Application of Proteomics in Diagnosis of Kratom Addiction**

2022 · Current Trends in Analytical and Bioanalytical Chemistry · article, journal-article · en · https://doi.org/10.36959/525/452

Kratom (Mitragyna speciosa) is a medicinal plant grown wildly in Southeast Asian. It has been used traditionally for its analgesic and relaxing effects after hard day of labors. The main alkaloid of kratom, mitragynine binds to opioid receptors to give opioid-like effects, therefore it has been widely utilized as opiate substitute.

**ИИ:** ? · обе модели · другое · The abstract is cut off. This may be a mini-review or a proteomics study of kratom users with addiction diagnosed; the full text is needed.

**Решение:** =

---

### 141 · R2013

**Characterization of urinary protein profile in regular kratom (Mitragyna speciosa korth.) users in Malaysia.**

2022 · Journal of addictive diseases · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1080/10550887.2021.1981122

Abstract Mitragyna speciosa (Korth.) also known as kratom or ketum has been traditionally used for its diverse medicinal value in Southeast Asia. Despite of its therapeutic value, kratom’s safety profile remains deficiently elucidated. Our study aims to characterize the urinary protein profile of regular kratom users to determine its toxic effects on renal functioning. A total of 171 respondents (comprising of n = 88 regular kratom users, and n = 83 healthy controls) were recruited for this study. Urine specimens were collected and analyzed using SDS-PAGE, followed by LC/MS/MS analysis. Our results show albumin is the primary, and most abundant form of protein excreted in kratom user’s urine specimens (n = 60/64), indicating that kratom users are predisposed to proteinuria. Kratom users had an elevated urinary protein (with an intensity of 66.7 kDa band), and protein: creatinine ratio (PCR) concentrations relative to healthy controls. However, kratom user’s urinary creatinine concentration was found to be in the normal range as the healthy control group. While, kratom users who tested positive for illicit drug use had an elevated urinary albumin concentration. Our preliminary findings indicate that regular consumption of freshly brewed kratom solution over a protracted period (for an average of eleven years) seems to induce proteinuria, suggestive of an early stage of kidney injury. Hence, further studies are urgently needed to confirm our findings, and establish kratom’s renal impairing effects.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Clinical study of 88 regular kratom users in Malaysia; the sample table might report dependence, but the abstract doesn't mention it.

**Решение:** =

---

### 142 · R2026

**Methadone Maintenance Treatment for Opioid Dependents: a Retrospective Study.**

2022 · East Asian archives of psychiatry : official journal of the Hong Kong College of Psychiatrists = Dong Ya jing shen ke xue zhi : Xianggang jing shen ke yi xue yuan qi kan · article, journal article, journalarticle · eng · https://doi.org/10.12809/eaap2214

Objectives To determine the prevalence of continued illicit drug use among people enrolled in methadone maintenance treatment (MMT), the association between hepatitis C status and methadone dosage, and the predictors for illicit drug abstinence during MMT. Methods Clinical records of active opioid dependents who underwent MMT between 1 January 2007 and 31 March 2021 in Hospital Tuanku Fauziah, Perlis, Malaysia were retrospectively reviewed. Data collected included baseline demographics, history of illicit drug use, temporal trend in methadone dosage modulation, and co-use of illicit drugs during the MMT. Results A total of 87 patients (mean age, 43.9 ± 8.33 years) were included. Their mean duration of involvement in MMT was 7.8 ± 3.69 years. The most commonly used drug was heroin (88.5%), followed by kratom (51.7%). Between 2019 and 2021, 61 (70.1%) patients had ceased abusing opioid, but 51 (58.6%) patients continued using any of the illicit drugs. Methamphetamine and amphetamine co-use was most common (n = 12, 37.5%). Hepatitis C status was not associated with the current methadone dose (U = 539.5, p = 0.186) or the highest dose required (t = -0.291, df = 74, p = 0.772). No predictor for illicit drug abstinence during MMT was identified. Methadone dose positively correlated with frequency of defaulting treatments ( r = 0.22, p = 0.042). Conclusion Among our patients, MMT for opioid dependents cannot sufficiently curb illicit drug use, and there is a shift toward stimulants abuse.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · MMT chart review found 51.7% kratom use; the abstract doesn't say whether kratom dependence was recorded or diagnosed.

**Решение:** - школьный опрос в Таиланде: распространенность ПАВ, без меры зависимости от кратома

---

### 143 · R2034

**Užívání kratomu u studentů pražských vysokých škol: dotazníkové šetření**

2022 · bachelor thesis · ces/cze · http://www.nusl.cz/ntk/nusl-509260

Background: In recent years it has been possible to note the increasing popularity of a psychoactive substance called kratom. It is a substance that is not legislated in the Czech Republic, which can affect its easy availability for users of all ages. At the same time, there are not enough studies in our country or abroad to research kratom or its use and potential risks. Objectives: The main objectives of this work describe the use of kratom among students at Prague universities and to find out if there was a link between use of kratom and the use of other addictive substances. Furthermore, the thesis also looked at how students perceived the risks associated with the use of this substance. Methods: The research was executed by quantitative data collection via an online questionnaire survey. The questionnaire was distributed by social network Facebook. The sample consisted of 1,496 respondents studying at Prague universities. The data was imported to Microsoft Excel. Afterwards it was organized and processed. Subsequently, a portion of the data was evaluated by using the Jamovi app. Results: A research of 1,496 students was found that 12% used kratom in their lives. The use of kratom in the last year was registered in 135 (9%) students and in 53 (4%) students in the last month. The study suggests...

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of Prague university students that measured kratom use; the abstract is cut off and doesn't say whether dependence or use-disorder criteria were assessed.

**Решение:** =

---

### 144 · R2035

**Use of kratom in students of Prague universities: a questionnaire survey**

2022 · Digital Repository (National Repository of Grey Literature) · dissertation, thesis · cs

Background: In recent years it has been possible to note the increasing popularity of a psychoactive substance called kratom. It is a substance that is not legislated in the Czech Republic, which can affect its easy availability for users of all ages. At the same time, there are not enough studies in our country or abroad to research kratom or its use and potential risks. Objectives: The main objectives of this work describe the use of kratom among students at Prague universities and to find out if there was a link between use of kratom and the use of other addictive substances. Furthermore, the thesis also looked at how students perceived the risks associated with the use of this substance. Methods: The research was executed by quantitative data collection via an online questionnaire survey. The questionnaire was distributed by social network Facebook. The sample consisted of 1,496 respondents studying at Prague universities. The data was imported to Microsoft Excel. Afterwards it was organized and processed. Subsequently, a portion of the data was evaluated by using the Jamovi app. Results: A research of 1,496 students was found that 12% used kratom in their lives. The use of kratom in the last year was registered in 135 (9%) students and in 53 (4%) students in the last month. The study suggests...Východiska: V posledních letech bylo možné zaznamenat zvyšující se oblibu psychoaktivní substance s názvem kratom. Jedná se o látku, která není v České republice pevně legislativně ukotvena, což může ovlivňovat její snadnou dostupnost pro uživatele všech věkových kategorií. Zároveň u nás i v zahraničí není dostatek studií, které by se věnovali kratomu samotnému nebo jeho užívání a potencionálním rizikům. Cíle: Hlavními cíli této práce bylo zmapovat užívání kratomu u studentů pražských vysokých škol a zjistit, zda v tomto výzkumném souboru existuje souvislost mezi jeho užíváním a užíváním návykových látek. Dále se také práce věnovala tomu, jak studenti vnímají rizika spojená s užíváním této látky. Metody: Výzkum byl realizován kvantitativním sběrem dat na podkladě on-line dotazníkového šetření. Dotazník byl distribuován pomocí sociální sítě Facebook. Výběrový soubor studie tvořilo 1 496 respondentů studujících pražskou vysokou školu. Následně byla data převedena do programu Microsoft Excel, v němž byla uspořádána a základně zpracována. Následně byla část dat vyhodnocena pomocí aplikace Jamovi. Výsledky: U výzkumného souboru 1 496 studentů bylo zjištěno, že 12 % někdy ve svém životě užilo kratom Užití kratomu v posledním roce bylo zaznamenáno u 135 dotázaných (9 %) a v posledním měsíci u 53 studentů...Department of Addictology First Faculty of Medicine Charles University and General University Hospital in PragueKlinika adiktologie 1. LF UK a VFN1. lékařská fakultaFirst Faculty of Medicin

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Student survey of kratom use with 135 past-year users; the abstract is cut off, so it is unclear whether dependence was assessed.

**Решение:** =

---

### 145 · R2038

**Vzorce užívání kratomu u pravidelných uživatelů: kvalitativní analýza**

2022 · master thesis · ces/cze · http://www.nusl.cz/ntk/nusl-510300

Background: Kratom is becoming a more famous psychoactive substance in the Czech Republic. However the research fields is not that fast as its use so there are not many studies in czech describing kratom or its use across his users. Aim: The aim of this master thesis is to findout patterns of drug use in regular useres from age 15 - 34.. Sample: The sample for this study is respondents aged 15 - 34 (young adults). The sample consisted of 10 respondents, 5 were women and 5 were men. The average age of the respondents was 27.2 years. The grat majority of respondents (N=9) are working and the last respondent (N=1) is still a student. Methods: Target group is selected by snowball sampling method. Data will be obtained through semi-structured interview and screenings questionnaires. The method of pattern formula and tuft creation method will be used to analyze collected data. We assume that the result of the work will be not only findinng patterns of kratom use, a description of its addiction or possible withdrawal syndrome, but also the elaboration of professional text Results: Respondents use kratom at least once a week, but their frequency and amount of the substance varies. Those who use kratom only once a day use 2,5 - 3 g. Those who use it 2 - 4 times a day consume a dose of 7,5 - 20 g. Users...

**ИИ:** ? · обе модели · другое · Qualitative thesis with 10 regular kratom users, but it also used screening questionnaires that may have counted dependence.

**Решение:** =

---

### 146 · R2039

**Patterns of kratom use among regular users: qualitative analysis**

2022 · Digital Repository (National Repository of Grey Literature) · dissertation, thesis · cs · https://core.ac.uk/download/534449169.pdf

Background: Kratom is becoming a more famous psychoactive substance in the Czech Republic. However the research fields is not that fast as its use so there are not many studies in czech describing kratom or its use across his users. Aim: The aim of this master thesis is to findout patterns of drug use in regular useres from age 15 - 34.. Sample: The sample for this study is respondents aged 15 - 34 (young adults). The sample consisted of 10 respondents, 5 were women and 5 were men. The average age of the respondents was 27.2 years. The grat majority of respondents (N=9) are working and the last respondent (N=1) is still a student. Methods: Target group is selected by snowball sampling method. Data will be obtained through semi-structured interview and screenings questionnaires. The method of pattern formula and tuft creation method will be used to analyze collected data. We assume that the result of the work will be not only findinng patterns of kratom use, a description of its addiction or possible withdrawal syndrome, but also the elaboration of professional text Results: Respondents use kratom at least once a week, but their frequency and amount of the substance varies. Those who use kratom only once a day use 2,5 - 3 g. Those who use it 2 - 4 times a day consume a dose of 7,5 - 20 g. Users...Východiska: V České republice se kratom stává rozšířenou psychoaktivní látkou. Výzkumné reakce na užívání této látky však nejsou tak rychle a není tedy mnoho odborných zdrojů popisující kratom nebo studií, které se zabývají jeho uživateli a jejich užíváním této látky. Cíle: Primárním cílem je popsat kvalitativními výzkumnými metodami vzorce užívání kratomu u pravidelných uživatelů. Soubor: Základním souborem pro tento výzkum jsou respondenti ve věku 15-34 let (tzv. mladí dospělí). Výzkumu se zúčastnilo 10 respondentů, z toho 5 žen a 5 mužů. Průměrný věk respondentů byl 27,2 let. Velká většina respondentů (N=9) byla pracujících. Poslední respondent (N=1) byl stále studentem. Metody: Pro získání respondentů byla vybrána metoda sněhové koule neboli snowball sampling. S respondenty bylo následně realizováno polostrukturované interview. Data byla analyzována pomocí metody vytváření trsů a gestaltů. Výsledky: Respondenti kratom užívají minimálně jednou týdně, ale jejich frekvenci a množství látky se liší. Ti, co kratom užívají pouze jednou denně, užívají 2,5 - 3 g. Ti, kteří ho užívají 2 - 4krát denně, konzumují dávku od 7,5 - 20 g. Látku uživatelé konzumují v podobě rozdrceného prášku rozmíchaného ve vodě nebo ochuceném džusu. Většina respondentů užívá kratom sama doma, ostatní v práci, s kolegy nebo s...Department of Addictology First Faculty of Medicine Charles University and General University Hospital in PragueKlinika adiktologie 1. LF UK a VFN1. lékařská fakultaFirst Faculty of Medicin

**ИИ:** ? · обе модели · другое · Qualitative interview thesis with 10 regular kratom users, but it mentions screening questionnaires and addiction; these may count dependence.

**Решение:** =

---

### 147 · R2041

**Association between kratom (Mitragyna speciosa) use and metabolic syndrome.**

2022 · Heliyon · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.heliyon.2022.e09468

Background and aims There are evidence about effects of kratom ( Mitragyna speciosa ) use on parameters related to metabolic syndrome (MetS). The present study aimed to determine the association between kratom use and MetS. Methods This study is a cross-sectional study of 581 subjects (kratom users and non-users) aged 18 and over from the Nam Phu sub-district, Surat Thani province, Thailand. The association was determined using multivariate logistic regression. Results MetS prevalence in kratom users and non-users was 11.9% (95% CI, 8.4-16.3%) and 21.6 % (95% CI, 17.1-26.8%), respectively. The use of kratom was associated with the lower odds of MetS (adjusted OR, 0.56; 95% CI, 0.33-0.96). Kratom use were associated with smaller waist circumference, lower triglycerides, and higher high-density lipoprotein. Conclusions The current study demonstrated a potential protective effect of kratom use against MetS.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Community survey of kratom users and non-users in Thailand; the abstract doesn't say whether dependence was assessed, though the sample table might report it.

**Решение:** =

---

### 148 · R2071

**Magnetic resonance imaging brain volumetry among adult malay male regular kratom leaves users**

2022 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; MRI study of regular kratom users might report dependence (e.g., KDS) in the sample description. "Review" label looks wrong.

**Решение:** =

---

### 149 · R2105

**Follow-Up: Effects of a Pandemic and Isolation on Alcohol and Psychoactive Medication Use in a Population of Rehabilitation and Pain Patients**

2022 · Annals of Clinical and Laboratory Science · article · https://pubmed.ncbi.nlm.nih.gov/36564077/

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -6 (не про кратом (другие виды Mitragyna) или не про людей, которые его употребляют: Lab study of alcohol and medication use in rehab and pain patients; no sign of kratom or a kratom dependence measure.); Sonnet ? (нет аннотации: No abstract. Pain and rehabilitation patients' substance use, likely urine testing. Kratom and dependence measures are unclear, so a full-text check is needed.)

**Решение:** - токсикологическое исследование пациентов реабилитации, кратом не является предметом исследования

---

### 150 · R2118

**A Preliminary Study On Pain Tolerance And Withdrawal Symptoms Among Active Ketum (Mitragyna Speciosa) Users In Malaysia**

2022 · review · https://core.ac.uk/download/597538914.pdf

Kratom is known locally as ketum or biak (Mitragyna speciosa) in Thailand, Malaysia, and Indonesia. Southeast Asian countries are home to the ketum plant. Ketum leaves are extensively used as an herbal supplement (traditional medicine) for self-treatment of medical conditions in the West and Southeast Asia, including pain and opioid use disorder (OUD). However, ketum consumption over a prolonged period was associated with withdrawal effects. Therefore, to systematically investigate the effects of ketum based on claims from previous research (pain tolerance and withdrawal symptoms), a human laboratory study was conducted with 26 male participants in Pusat Sejahtera, Universiti Sains Malaysia (USM). The study aimed to investigate withdrawal symptoms using a validated clinical measurement, the Clinical Opiate Withdrawal Scale (COWS), after 12 hours of ketum cessation. Secondly, the study investigated ketum effects on pain tolerance using the cold pressor task. Study findings suggested no significant association between ketum consumption with withdrawal symptoms and pain tolerance. However, mild withdrawal symptoms were observed during the 12 hours of ketum cessation such as runny nose, yawning, restlessness and axiety

**ИИ:** ? · обе модели · только абстиненция · Lab study of active ketum users reports only withdrawal (COWS); full text may show the share meeting DSM-5 use disorder criteria.

**Решение:** =
