# Проверка с метками ИИ, часть 2

Записи 151–251 из 251, с метками обеих моделей над строкой решения. Модели согласны и вы тоже — поставьте `=`; иначе свой код (`+`, `?` или `-`, причина не нужна). Если модели разошлись, `=` не годится — нужен ваш код. Решаете вы. Последние 6 — калибровочные записи, где ваша слепая метка разошлась с правилом ИИ: она показана над метками.

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

### 151 · R2123

**For Better or Worse: Self-reported Changes in Kratom and Other Substance Use as a Result of the COVID-19 Pandemic.**

2022 · Substance abuse : research and treatment · article, journal article, journalarticle · eng · https://doi.org/10.1177/11782218221123977

Background: Kratom is taken to self-treat pain and symptoms of psychiatric disorders, including substance-use disorders (SUDs) and opioid withdrawal. Before COVID-19, kratom use was increasing in the US, however, there are few published data on whether that trend continued during the COVID-19 pandemic, which could have affected kratom use in multiple ways. Aim: To examine COVID-19-related changes in kratom use and how these changes were experienced, relative to changes in other commonly used substances. Methods: Using Amazon Mechanical Turk, 2615 evaluable surveys were completed between September 2020 and March 2021. Responses from past-month and past-year kratom-using adults (N = 174) indicating changes for the better or worse were examined using generalized linear mixed effects models, and relevant open-text responses (n = 85) were thematically coded. Results: For kratom 33% (n = 58) reported a Covid-related increase and 24% (n = 42) reported a Covid-related decrease. Controlling for changes in amount used, alcohol (OR = 5.02), tobacco (OR = 4.72), and nonmedical opioid use (OR = 3.42) were all more likely to have changed for the worse, compared with kratom use. Relative to decreases in kratom use, decreases in alcohol (OR = 3.21) and tobacco (OR = 6.18) use were more likely to be changes for the better. Cannabis use was the only substance to display a probability lower than 50% of being a decrease for the better, and of the increases, cannabis use displayed the highest probability of being for the better. Conclusions: Increases in kratom and cannabis use were less likely than alcohol and tobacco to be reported as changes for the worse, and decreases in kratom and cannabis use were more likely than alcohol and tobacco to be reported as changes for the better. These findings indicate that people differently conceptualize their relationships with kratom and cannabis, compared to their relationships with alcohol and tobacco.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · MTurk survey of 174 kratom users about COVID-related changes; abstract does not say whether kratom use disorder or dependence was assessed.

**Решение:** =

---

### 152 · R2130

**Consumer-Grade Brain Measuring Sensor in People With Long-Term Kratom Consumption**

2022 · IEEE Sensors Journal · article, journal article, journal-article · en · https://doi.org/10.1109/jsen.2022.3147207

Neurophysiological characteristics of long-term Kratom users have been challenged for identification due to the lack of evidence. Long-term and high Kratom consumption caused concern, particularly in older adults. Thus, the study aims to explore EEG biomarkers in long-term Kratom users (LKU) based on consumer-grade EEG systems. The fifty-two participants were collected EEG using MUSE portable system during resting-state to examine EEG biomarkers with the proposed features: theta/alpha ratio and power variance function (PVF) in theta and alpha bands. The statistical analysis was further carried out to test the existent difference between controls and LKU in various age ranges (≤50 and >50 years of age) and different doses of Kratom consumption (low to high doses and very high dose). Subsequently, the statistical-based EEG biomarkers were extracted and performed classification among four classifiers (Random forest, Support vector machine, ${K}$ -Nearest Neighbor, and Logistic regression. As a result, the TAR ratio was remarkably different between groups over 50 years of age. Furthermore, TAR and PVF in the alpha band were dominant in those who consumed Kratom at a very high dose and was classified well by support vector machine using the features combination (accuracy at 83.33% ± 10.24, sensitivity at 90.00% ± 10.00, specificity at 75.00% ± 13.44). Our preliminary results concluded that the proposed EEG features were an important EEG biomarker for LKU with a large effect size. This finding led us to the promising aspect of applying machine learning-based EEG biomarkers to screen the overdose of Kratom consumption in the future.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · EEG study recruiting long-term kratom users; the abstract doesn't say whether dependence was assessed, but the sample description might report it.

**Решение:** =

---

### 153 · R2145

**The Use of Kratom (Mitragyna speciosa Korth.) Among People Who Co-use Heroin and Methamphetamine in Malaysia.**

2022 · Journal of addiction medicine · article, journal article, research support, n.i.h., intramural · eng · https://doi.org/10.1097/adm.0000000000000876

Objectives: Kratom ( Mitragyna speciosa Korth.), an indigenous medicinal plant, has been widely used as a traditional remedy in Southeast Asia. However, its combined consumption with other substances has received scarce attention. This study investigates the use of kratom among adults with a history of using heroin and methamphetamine in Malaysia. Methods: A total of 332 patients who were mandated to undergo drug rehabilitation participated in this cross-sectional study. The study data were collected through face-to-face interviews using a semi-structured questionnaire. Results: The majority were males (95%, n = 314/332) and Malays (98%, n = 325/332) with a mean age of 32.3 years (SD = 9.16). Over two thirds of the respondents used kratom to alleviate heroin withdrawal symptoms and to reduce methamphetamine intake; 59% used it as a substitute for heroin and methamphetamine. A similar proportion used kratom to reduce heroin intake (58%), while only 15% used it for its euphoric effects. Multivariate analysis showed that previous attendees of government rehabilitation programs had lower odds of using kratom as a heroin substitute. Conclusions: The potential of kratom to alleviate heroin withdrawal symptoms, and to reduce methamphetamine and heroin intake, among people who co-use heroin and methamphetamine warrants further research.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Rehab patients who co-use heroin and methamphetamine and report kratom use motives; the abstract doesn't say whether kratom dependence was measured.

**Решение:** ? опиоид-зависимые пациенты на метадоне: мера зависимости кратома может быть в таблице

---

### 154 · R2146

**Treatment Barriers Associated with Amphetamine-Type Stimulant (ATS) Use in Malaysia**

2022 · Journal of Psychoactive Drugs · article · https://doi.org/10.1080/02791072.2021.1900627

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; Malaysian drug-user survey focused on ATS, could include kratom use or dependence, but this is unlikely from the title.); Sonnet -6 (не про кратом (другие виды Mitragyna) или не про людей, которые его употребляют: Title concerns treatment barriers for amphetamine-type stimulant use in Malaysia; kratom is not mentioned and no abstract is available.)

**Решение:** - исследование барьеров лечения при употреблении стимуляторов амфетаминового ряда, не про кратом

---

### 155 · R2151

**Kratom use as more than a "self-treatment".**

2022 · The American journal of drug and alcohol abuse · article, journal article, research support, n.i.h., extramural · eng · https://doi.org/10.1080/00952990.2022.2083967

ABSTRACT Background: Mitragyna speciosa (kratom) is increasingly used in the United States for its pharmacological effects. Kratom’s relative novelty makes for a dynamic situation, such that use motivations are not firmly established and may be changing. Investigators and clinicians require frequent updates on kratom trends. Objectives: To assess the current state of kratom-use initiation, sourcing, motivations, preference, conceptualizations, and perceived stigma, using survey responses from current and former users. Methods: Between April-May 2021 we recontacted 289 respondents who reported lifetime kratom use (on an unrelated survey) to answer kratom-specific questions. Results: The sample (N=129) was majority female (51.9%) and white (71.9%). Most (69.0%) reported first trying kratom after 2015. Mean age of use initiation (29.9 years) was older than for other substances, including opioids. Kratom ranked as a preferred substance by 48.5%. The strongest drug association with past-year kratom use was vaped nicotine (OR=3.31,95% CI 1.23-8.88). Use was less likely among those prescribed buprenorphine in the past year (OR=0.03, CI 0.01-0.28). Past-month cannabis use (OR=4.18,CI 1.80-9.72) had the strongest association with past-month kratom use. Over 40 use motivations were endorsed, many (but not all) supporting the “self-treatment” narrative of kratom use, including use as an opioid, alcohol, or stimulant substitute. Treatment shortfalls were associated with decisions to try kratom. Conclusions: Kratom use motivations are diversifying, with multiple factors driving use. As sales continue to increase, the public-health, clinical, and policy responses to kratom should be grounded in rigorous bench-to-bedside scientific research. Comprehensive study of kratom is currently lacking.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of 129 current/former kratom users on motivations and use patterns; abstract doesn't say whether dependence or use disorder was assessed.

**Решение:** =

---

### 156 · R2153

**Searching for a Signal: Self-Reported Kratom Dose-Effect Relationships Among a Sample of US Adults With Regular Kratom Use Histories.**

2022 · Frontiers in pharmacology · article, journal article, journalarticle · eng · https://doi.org/10.3389/fphar.2022.765917

There is limited understanding regarding kratom use among US adults. Although motivations for use are increasingly understood, typical kratom doses, threshold of (low and high) doses for perceived effectiveness, and effects produced during cessation are not well documented. We aimed to extend prior survey work by recruiting adults with current and past kratom exposure. Our goal was to better understand kratom dosing, changes in routines, and perception of effects, including time to onset, duration, and variability of beneficial and adverse outcomes from use and cessation. Among respondents who reported experiencing acute kratom effects, we also sought to determine if effects were perceived as helpful or unhelpful in meeting daily obligations. Finally, we attempted to detect any signal of a relationship between the amount of kratom consumed weekly and weeks of regular use with ratings of beneficial effects from use and ratings of adverse effects from cessation. We conducted an online survey between April-May 2021 by re-recruiting participants from a separate study who reported lifetime kratom use. A total of 129 evaluable surveys were collected. Most (59.7%) had used kratom &amp;gt;100 times and reported currently or having previously used kratom &amp;gt;4 times per week (62 weeks on average). Under half (41.9%) reported that they considered themselves to be a current “regular kratom user.” A majority (79.8%) reported experiencing acute effects from their typical kratom dose and that onset of effects began in minutes but dissipated within hours. Over a quarter reported that they had increased their kratom dose since use initiation, whereas 18.6% had decreased. Greater severity of unwanted effects from ≥1 day of kratom cessation was predicted by more weeks of regular kratom use ( β = 6.74, p = 0.02). Acute kratom effects were largely reported as compatible with, and sometimes helpful in, meeting daily obligations. In the absence of human laboratory studies, survey methods must be refined to more precisely assess dose-effect relationships. These can help inform the development of controlled observational and experimental studies needed to advance the public health understanding of kratom product use.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Online survey of US adults with regular kratom use; reports cessation effects, but the abstract doesn't say whether dependence or use disorder was measured.

**Решение:** =

---

### 157 · R2155

**Substance use and mental health in pregnant women during the COVID-19 pandemic**

2022 · Journal of Reproductive and Infant Psychology · article · https://doi.org/10.1080/02646838.2021.1916815

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract. A substance-use survey of pregnant women might have measured kratom use and dependence, but the title doesn't say.); Sonnet -6 (не про кратом (другие виды Mitragyna) или не про людей, которые его употребляют: Title concerns general substance use and mental health in pregnant women during COVID-19; no indication of kratom, and no abstract available.)

**Решение:** - опрос беременных женщин о психическом здоровье и общих ПАВ, не про кратом

---

### 158 · R2180

**Local culture of kratom (Mitragyna speciosa) consumption in Kapuas Hulu district**

2022 · AIP conference proceedings · article, conference, conference paper · de · https://doi.org/10.1063/5.0104736

Kratom leaves (Mitragyna speciosa Korth) have been used by people in West Kalimantan, especially Kapuas Hulu District, as local culture, for traditional medicine. This research was conducted to obtain facts and data on utilization and complaints due to the use of kratom leaves in local culture by the people of Kapuas Hulu Regency. Data obtained by interview using a questionnaire and the determination of the respondents is done by snowball. The relationship between period, dose and frequency of kratom leaf consumption and complaints was searched statistically using the chi-quadrate. It was found that 152 respondents who consumed kratom leaves. The main reason respondents consume kratom leaves to overcome fatigue or get stamina (49%) and to treat illness 25%. Generally, 46% of respondents consume kratom leaves for less than 1 year, although 25% of them are more than 5 years. Most of the respondents consumed kratom leaf powder at a dose of ¼ teaspoon (0.5 g) with the highest frequency once a day (27.94%). Chi-square analysis showed that there was no very significant relationship between the period of drinking kratom leaves and complaints, but there was a very significant relationship between the dose of kratom leaf consumption and complaints and between the frequency of drinking kratom leaves and complaints. There were no complaints such as symptoms of narcotics and drug users. Generally, respondents stated that they did not experience complaints 93.42%. About 6.58% of complaints were feeling tired, drowsy and achy.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Questionnaire survey of 152 kratom users on complaints; unclear whether the 'narcotic-user symptoms' items included dependence criteria.

**Решение:** =

---

### 159 · R2378

**Is kratom (Mitragyna speciosa Korth.) use associated with ECG abnormalities? Electrocardiogram comparisons between regular kratom users and controls.**

2021 · Clinical toxicology (Philadelphia, Pa.) · article, other literature type, comparative study · eng · https://doi.org/10.1080/15563650.2020.1812627

Abstract Objectives Little is known about the cardiotoxic effects of kratom (Mitragyna speciosa Korth.), a medicinal plant. This analytical cross-sectional study investigated the prevalence of electrocardiogram (ECG) abnormalities and QTc intervals in regular kratom users compared with non-kratom-using control subjects. Methods We enrolled regular kratom users and non-kratom-using control subjects from three communities. Demographic data, clinical data, kratom use characteristics, and ECG findings were recorded. The mitragynine content of kratom juice was quantified using a validated gas chromatography–mass spectrometry (GC–MS) method. Results A total of 200 participants (100 kratom users and 100 control subjects) participated in this study. The prevalence of ECG abnormalities in kratom users (28%) did not differ from that of control subjects (32%). Kratom use was not associated with ECG abnormalities, except for significantly higher odds of sinus tachycardia (OR = 8.61, 95% CI = 1.06–70.17, p = 0.035) among kratom users compared with control subjects. The odds of observing borderline QTc intervals were significantly higher for kratom users compared with control subjects, regardless of the age of first use, the duration of use, the daily quantity consumed, and the length of time that had elapsed between last kratom use and ECG assessment. Nevertheless, there were no differences in the odds of having prolonged QTc intervals between kratom users and controls. The estimated average daily intake of mitragynine consumed by kratom users was 434.28 mg. Conclusion We found no link between regular kratom use and electrocardiographic abnormalities with an estimated average daily intake of 434.28 mg of mitragynine.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Community sample of 100 regular kratom users; the abstract doesn't say whether dependence was assessed, but the sample table might report it.

**Решение:** =

---

### 160 · R2379

**Assessment of Cardiovascular Functioning Among Regular Kratom (Mitragyna speciosa Korth) Users: A Case Series.**

2021 · Frontiers in pharmacology · article, journal article, journalarticle · eng · https://doi.org/10.3389/fphar.2021.723567

Multiorgan toxicities have been extensively reported in kratom ( Mitragyna speciosa Korth) users in Western countries but not in Southeast Asia. Existing literature argued that this discrepancy may be due to underreporting of kratom-related toxicity cases in Southeast Asia. Hence, this case series filled the research gap by clinically assessing the cardiovascular functioning and serum mitragynine level of regular kratom users in its traditional settings in Malaysia. Nine regular kratom users without history of polysubstance use were recruited from the same community via snowball sampling and were subjected to electrocardiogram (ECG) and echocardiogram assessments. Serum mitragynine analysis was also performed by solid-phase extraction and liquid chromatography-tandem mass spectrometry. The mean serum mitragynine level was 10.3 mg/L (SD = 6.9) and ranged from 2.5 mg/L to 22.4 mg/L. Those who consumed an average daily quantity of four or more glasses of brewed kratom juice ( p = 0.045) and those who had prolonged QTc intervals ( p = 0.017) had significantly higher serum mitragynine level. Echocardiographic findings of all the respondents were normal except one reported left ventricular hypertrophy and another had trivial tricuspid regurgitation with pulmonary artery systolic pressure (PASP) of 10 + 5 mmHg. Regular kratom use without concomitant use of other illicit substances may not provoke any risk of cardiovascular impairment or toxicity except for prolonged QTc interval, which appeared to be dose dependent. However, as this study was limited by a small sample size, future studies with larger sample size are warranted to confirm our findings.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Community sample of nine regular kratom users in Malaysia, not clinical patients; abstract does not say if dependence was assessed.

**Решение:** =

---

### 161 · R2380

**Effect of regular kratom (Mitragyna speciosa Korth.) use on quality of life of people who use kratom.**

2021 · Substance abuse · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1080/08897077.2021.1876809

Background : Kratom ( Mitragyna speciosa Korth.) is a traditional folk remedy used in Southeast Asia and is known to have a significant opioid-like effect. However, it is unknown whether kratom consumption can impair quality of life (QoL). This study aimed to examine the QoL of people who use kratom by comparing it with that of healthy non-kratom using controls and to determine the association between patterns of kratom use and QoL among people who use kratom. Methods : 200 respondents (100 subjects who use kratom and 100 healthy controls) were recruited for this cross-sectional study. The World Health Organization Quality of Life-BREF was administered to all the respondents to assess QoL, while the Kratom Dependence Scale (KDS) was used to assess the severity of kratom dependence among the subjects who use kratom. Results : The physical health, psychological, and environment QoL scores of the subjects who use kratom were significantly lower than those of the healthy controls. Multiple linear regression analysis revealed greater KDS score and longer duration of kratom use were significant predictors of physical health QoL, while only greater KDS score significantly predicted psychological and environment QoL scores. Conclusion : Prolonged kratom use and kratom dependence may negatively impact the QoL of people who use kratom, hence kratom addiction has to be treated adequately.

**ИИ:** + · обе модели · употребляющие + мера зависимости · Cross-sectional study of 100 people who use kratom, with dependence measured on the Kratom Dependence Scale; full text may report dependence prevalence.

**Решение:** =

---

### 162 · R2415

**Non-invasive Detection of Ketum Users through Objective Analysis of EEG Signals**

2021 · Journal of Physics Conference Series · article, other literature type, conference · en · https://doi.org/10.1088/1742-6596/2071/1/012045

Ketum leaves are traditionaly used for treatment of backpain and reduce fatigue. However, in recent years people use ketum leaves to substitute traditional drugs as they can easily be obtained at a low cost. Currently, a robust test for ketum detection is not available. Although ketum usage detection via test strip is available, however, the method is possible to be polluted by other substances and can be manipulated. Brain signals have unique characteristics and are well-known as a robust method for recognition and disease detection. Thus, this study has been done to distinguish between ketum users and non-users via brain signal characteristics. Eight participants were chosen, four of whom are heavy ketum users and four non-users with no health issues. Data were collected using the eegoSports device in relaxed state. In pre-processing, notch filter and Independent Component Analysis (ICA) were used to remove artifacts. Wavelet Packet Transform (WPT) was used to reduce the large data dimension and extract features from the brain signal. To select the most significant features, T-Test was used. Support Vector Machine (SVM), K-Nearest Neighbour, and Ensemble classifier were used to categorize the input data into ketum users and non-users. Ensemble classifier was found to be able to predict the testing instances with 100 accuracy for open and closed eyes task with Teager energy and energy to standard deviation ratio as the features. © 2021 Institute of Physics Publishing. All rights reserved

**ИИ:** разошлись — Opus ? (неясно, оценивали ли зависимость: EEG classification study with four heavy ketum users; dependence assessment unlikely but not ruled out in the abstract.); Sonnet -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: EEG classification of 4 heavy ketum users vs 4 non-users; no dependence or use-disorder measure reported.)

**Решение:** - экспериментальное ЭЭГ исследование 4 человек, нет эпидемиологической выборки

---

### 163 · R2440

**Effects of a Pandemic and Isolation on Alcohol and Psychoactive Medication Use in a Population of Rehabilitation and Pain Patients**

2021 · Annals of Clinical and Laboratory Science · article · https://pubmed.ncbi.nlm.nih.gov/34686512/

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -4 (клинический случай или серия случаев; данные токсикологии, отравлений, смертей без опроса людей: Title and lab-science venue suggest drug-testing data on alcohol and medications in patients, with no kratom dependence assessment.); Sonnet ? (нет аннотации: No abstract; pandemic substance use study in rehabilitation and pain patients may include kratom, but title does not mention kratom or dependence.)

**Решение:** - токсикологический надзор / данные отравлений

---

### 164 · R2451

**Comparison of biochemical and safety parameters of regular kratom ( Mitragyna speciosa Korth.) users at two different time periods**

2021 · Journal of Substance Use · article, journal article, journal-article · en · https://doi.org/10.1080/14659891.2021.1999513

ABSTRACT Introduction Kratom is a medicinal plant native to Southeast Asia. This present study was primarily undertaken to investigate changes in the vital signs, hematological, and biochemical parameters of regular kratom users. Method Five male regular kratom users were recruited for this longitudinal study. Subjects volunteered to undergo two sessions of blood tests and vital signs assessments after a 3-month interval (baseline: T1; after 3 months: T2). Result There were no significant alterations found in the hematological and biochemical of kratom users, except for a decrease in white cell count after a 3-month interval. In general, the kidney, liver function tests, thyroid, and glucose parameters were not significantly affected. Calcium, total protein, and globulin levels were significantly increased at T2 compared to T1, but all these parameters were within the normal reference range. There were alterations in the lipid profile, where total cholesterol and LDL cholesterol parameters were elevated at both T1 and T2, while significant increase in HDL cholesterol, and decrease in triglycerides levels were observed at T2 compared to T1. Conclusion Our results indicated that continuous consumption of kratom decoction at a daily mitragynine dose of 76.3–114.8 mg did not appear to alter the safety hematological and biochemical parameters of kratom users.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Small longitudinal clinical study of regular kratom users; abstract doesn't mention dependence, but the sample description may report it.

**Решение:** =

---

### 165 · R2456

**Kratom Use in the US: Both a Regional Phenomenon and a White Middle-Class Phenomenon? Evidence From NSDUH 2019 and an Online Convenience Sample.**

2021 · Frontiers in pharmacology · article, journal article, journalarticle · eng · https://doi.org/10.3389/fphar.2021.789075

Kratom products available in the United States are becoming increasingly diverse both in terms of content and in terms of how they are marketed. Prior survey research indicates that kratom has been primarily used in the US to self-treat anxiety, depression, pain, fatigue, and substance use disorder (SUD) symptoms. Kratom is also well-known for its use as a short- or long-term full opioid agonist substitute. Therefore, use may be greater in regions particularly impacted by addiction to prescription opioids. Use may also be greater in demographic groups targeted by media outlets (such as specific podcasts) in which kratom is touted. Here, we aimed to determine whether lifetime and past-year kratom use were associated with region of residence and with being young, White, post-secondary educated, and employed. To strengthen confidence in our findings, we analyzed data from two sources: our own crowdsourced online convenience sample and the 2019 National Survey on Drug Use and Health (NSDUH). In our sample (N = 2,615), 11.1% reported lifetime and 6.7% reported past-year kratom use, and the odds of kratom use were higher among people who were White, younger, at least high school educated, employed, and above the poverty line, as well as those reporting nonmedical opioid use, past-year SUD, or lifetime SUD treatment; residence was not a significant predictor. In NSDUH data, suburban residence and other demographic factors, concordant with those from the crowdsourced sample, were associated with kratom use. Taken together, the findings support a general "White middle-class suburban" profile of the modal kratom user, but more research is needed to understand it. In the interim, focus should be on our finding that lifetime nonmedical opioid use was associated with an up to five times greater likelihood of past-year kratom use, suggesting that drug-use history may presently be the strongest predictor of kratom use.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Online survey and NSDUH data on kratom use; past-year SUD was assessed, but it is unclear whether kratom-specific use disorder was measured.

**Решение:** =

---

### 166 · R2465

**Prevalence and description of kratom (Mitragyna speciosa) use in the United States: a cross-sectional study.**

2021 · Addiction (Abingdon, England) · article, journal article, journalarticle · eng · https://doi.org/10.1111/add.15082

Abstract Background and aims Mitragyna speciosa (‘kratom’) contains mu opioid partial agonists. It is widely available, and occasionally used as a home remedy for opioid use disorder. The Drug Enforcement Agency considers kratom a drug of concern; however, prevalence of use and role in drug misuse are unknown. This study aimed to characterize kratom use in the United States. Design Cross‐sectional Survey of Non‐Medical Use of Prescription Drugs (NMURx) Program, 2018 third quarter and 2019 first quarter. Setting A validated non‐probability online survey in the United States. Participants A total of 59 714 respondents aged 18 years or older, weighted to represent the adult US population ( n = 252 063 800). Measurements In addition to prevalence of past‐year kratom and other drug use, behavior proportions were estimated. The Drug Abuse Screening Test (DAST‐10) estimated consequences of drug abuse. Findings The estimated prevalence of past‐year kratom use in the adult US population was 0.8% [95% confidence interval (CI) = 0.7–0.9], representing 2 031 803 adults. Life‐time prevalence was 1.3% (95% CI = 1.2–1.4), representing 3 353 624 adults. Kratom users were younger (mean 35 years, P &lt; 0.001), with higher proportions of males (61.0 versus 48.6%, P &lt; 0.001), students (14.1 versus 7.5%, P &lt; 0.001) and health‐care professionals (9.7 versus 4.5%, P &lt; 0.001) and fewer bachelor's/advanced degree graduates (33.4 versus 42.6%, P &lt; 0.001) compared with non‐users. Results were inconclusive on whether there was a difference in kratom use by race, household income or employment status. Among those with past‐year kratom use, 36.7% (95% CI = 32.1–41.3) non‐medically used prescription opioids, 21.7% (95% CI = 18.0–25.5) used illicit opioids, 54.4% (95% CI = 49.5–59.3) used another illicit drug and 67.1% (95% CI = 62.5–71.8) used cannabis. The DAST‐10 profile was more often substantial/severe in kratom users (21 versus 1%, P &lt; 0.001) compared with non‐users. Conclusions Estimated United States past‐year prevalence of kratom use is 0.8%, and kratom users tend to have more serious substance abuse profiles than non‐users or users of cannabis, alcohol or cigarettes. To our knowledge, this is the first description of kratom use at the national level.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · National survey of kratom users; only the general DAST-10 is reported, with no kratom-specific dependence measure. Full text could show more.

**Решение:** =

---

### 167 · R2491

**Patterns of Kratom Use among Male Drug Users in the Deep South of Thailand**

2021 · Thai Journal of Public Health · article · en

Kratom (Mitragyna speciosa) is a psychoactive plant which is native to Southeast Asia and is currently used recreationally. Psychoactive substances in kratom can interact with other substances and result in fatal physiological effects. However, no study has assessed substance use among men who used kratom in the deep south of Thailand. The objective of this study was to describe the patterns of kratom use among drug users in the deep south of Thailand and their associated factors. We established data collection sites in three provinces in the deep south region of Thailand and recruited 414 male drug users to participate in a survey interview by respondent-driven sampling. We assessed participant characteristics, self-reported history and patterns of drug use, and history of treatment for drug addiction using descriptive statistics and multivariate logistic regression analyses. Overall, 353 (85.3%) reported using kratom in the past 6 months. Among men who used kratom, 218 (61.8%) reported polydrug use, most commonly with methamphetamine. Kratom polydrug use was less common among those from Yala Province and among those who used drugs with peers. Kratom polydrug use was more common among those who had received drug treatment within the past 6 months, those who had received treatment ≥2 times, and those who had received treatment from facilities that were potentially connected to the Thai military. Treatment providers from the non-health sectors should make sure to comprehensively assess and ensure availability of treatments for multiple drug use.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of 414 male drug users, 353 of whom used kratom; the abstract does not say whether kratom dependence or use disorder was assessed.

**Решение:** =

---

### 168 · R2516

**Prevalence of Kratom Use and Co-Occurring Substance Use Disorders in the United States**

2021 · The Primary Care Companion For CNS Disorders · article, journal article, journalarticle · eng · https://doi.org/10.4088/pcc.21br02930

Kratom is a novel psychoactive drug often used to self-manage pain and opioid withdrawal. This article describes the prevalence of kratom use and co-occurring substance use disorders using the National Survey on Drug Use and Health.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · NSDUH population survey of kratom use and co-occurring SUDs; NSDUH likely lacks kratom use disorder items, but the abstract doesn't say.

**Решение:** =

---

### 169 · R2551

**Lipid profile of regular kratom (Mitragyna speciosa Korth.) users in the community setting v1**

2020 · protocols.io · article, posted-content, preprint · en · https://doi.org/10.17504/protocols.io.bfuwjnxe

The protocol describe the steps involved in conducting fasting lipid profile and liver function test from the blood samples of regular kratom users and healthy non-kratom using subjects in this study. This tests were conducted in an ISO 15189-certified laboratory at Advanced Medical and Dental Institute, Universiti Sains Malaysia. The blood parameters which were determined quantitatively included serum triglyceride (TG), total cholesterol (TC), high-density lipoprotein (HDL), total protein (TP), albumin, alkaline phosphatase (ALP), alanine transaminase (ALT), aspartate transaminase (AST), total bilirubin (TB) and direct bilirubin (DB). While globulin was determined from simple subtraction of albumin from total protein value, indirect bilirubin was determined by subtraction of direct bilirubin from total bilirubin value, and low-density lipoprotein (LDL) was calculated via Friedwald equation.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Lab protocol for a study of regular kratom users; the parent article might report dependence characteristics, but the abstract doesn't mention any.

**Решение:** =

---

### 170 · R2593

**Self-reported Health Diagnoses and Demographic Correlates With Kratom Use: Results From an Online Survey.**

2020 · Journal of addiction medicine · article, journal article, journalarticle · eng · https://doi.org/10.1097/adm.0000000000000570

OBJECTIVES: To determine whether diagnosed pre-existing health conditions correlate with Kratom demographics and use patterns. METHODS: A cross-sectional, anonymous US national online survey was conducted among 8049 Kratom users in October, 2016 to obtain demographic, health, and Kratom use pattern information. RESULTS: People who use Kratom to mitigate illicit drug dependence self-reported less pain and better overall health than individuals who used Kratom for acute/chronic pain. Self-reported improvements in pre-existing mental health symptoms (attention deficit and hyperactivity disorder/attention deficit disorder, anxiety, bipolar disorder, post-traumatic stress disorder, and depression) attributed to Kratom use were greater than those related to somatic symptoms (back pain, rheumatoid arthritis, acute pain, chronic pain, fibromyalgia). Demographic variables, including female sex, older age, employment status, and insurance coverage correlated with increased likelihood of Kratom use. CONCLUSIONS: Kratom use may serve as a self-treatment strategy for a diverse population of patients with pre-existing health diagnoses. Healthcare providers need to be engaging with patients to address safety concerns and potential limitations of its use in clinical practice for specific health conditions.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Large online survey of kratom users (2016 dataset that may have included DSM-5 items); abstract doesn't mention dependence assessment.

**Решение:** =

---

### 171 · R2625

**Prevalence and characteristics of self-reported kratom use in a representative US general population sample.**

2020 · Journal of addictive diseases · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1080/10550887.2020.1788914

Abstract Background Reports of kratom (Mitragyna speciosa) use, a medicinal plant widely found in Southeast Asia, are on the rise in the US. However, the prevalence and characteristics of individuals who use kratom in the US is unknown. Objective To estimate lifetime prevalence of, and descriptive characteristics associated with, kratom use in a sample of the US general population. Methods A cross-sectional survey was administered online by Qualtrics® research panel aggregator. Utilizing quota-based sampling, data was collected from a US sample aged 18–59 years, representative to age, geographic region, ethnicity, income, and education level. Data was collected regarding respondent demographic/clinical characteristics, as well as frequency/patterns of kratom and other drug use. Results Among 1,842 respondents, 112 (6.1%) reported use of kratom within their lifetime. Respondents who used kratom were largely between 25–44 years old, male, employed, and at higher educational levels. A total of 24.1% to 47.3% of respondents indicated self-reported diagnoses for addiction, and 42.9% reported having previously received treatment for addiction. A total of 71.4% to 92% of respondents who used kratom also reported use of other drugs, including nicotine, cannabis, cocaine, ecstasy, methamphetamine, and heroin. Conclusions To our knowledge, this analysis provides the first estimate of kratom use in the general US population, providing insight on demographic/clinical characteristics of individuals reporting use.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · General population survey of people who used kratom; it reports self-reported addiction diagnoses, but the abstract doesn't say if kratom-specific dependence was measured.

**Решение:** =

---

### 172 · R2629

**Impact of the UK Psychoactive Substances Act on awareness, use, experiences and knowledge of potential associated health risks of novel psychoactive substances**

2020 · British Journal of Clinical Pharmacology · article · https://doi.org/10.1111/bcp.14123

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · UK survey of novel psychoactive substance use with no abstract; kratom may be covered, but kratom dependence was probably not assessed.

**Решение:** =

---

### 173 · R2648

**Kratom (Mitragyna speciosa): User demographics, use patterns, and implications for the opioid epidemic.**

2020 · Drug and alcohol dependence · article, journal article, research support, n.i.h., extramural · eng · https://doi.org/10.1016/j.drugalcdep.2020.107849

Background Kratom, a Southeast Asian plant with opioid-receptor mediated effects, has emerged as a potential substance of abuse, with limited data on its use and effects. This study characterized kratom user demographics, use patterns, and perceived drug effects. Methods A cross-sectional, anonymous online survey was conducted between January and December 2017. Results 2,798 kratom users - mean age 40 (SD = 12); predominantly White (90 %), female (61 %), and located in the US (97 %) - completed the survey. Kratom was primarily taken orally in doses of 1-3 g (49 %), with daily use (59 %) being most common. Kratom was used for pain (91 %), anxiety (67 %), and depression (65 %), with high ratings of effectiveness. 1,144 (41 %) used kratom to stop or reduce prescription or illicit opioid use, citing decreased opioid withdrawal and craving related to kratom use, with 411 reporting >1-year continuous abstinence from opioids attributed to kratom use. Roughly one-third of respondents reported adverse effects of kratom, largely rated as mild in severity and lasting ≤24 h. Seventeen participants (0.6 %) sought treatment for adverse effects. Fifty-six individuals (2 %) met DSM-5 criteria for a past-year moderate or severe kratom-related substance use disorder (SUD). When asked how troubled they felt regarding their kratom use, the mean (SD) rating was 3.2 (9.8) on a scale from 0 to 100. Conclusion Kratom is used among White, middle-aged Americans for symptoms of pain, anxiety, depression, and opioid withdrawal. Although regular use was typical, kratom-related SUD and serious adverse effects were uncommon. Additional research on kratom epidemiology and pharmacology is imperative in light of the present opioid epidemic.

**ИИ:** + · обе модели · употребляющие + мера зависимости · Online survey of 2,798 kratom users; 2% met DSM-5 criteria for moderate or severe kratom use disorder.

**Решение:** =

---

### 174 · R2676

**New Johns Hopkins Survey Finds Kratom May Have Low Abuse Potential**

2020 · article · en

Of the 41% of kratom users who reported taking it for opioid withdrawal, 35% went >1 year without taking opioids or heroin.

**ИИ:** ? · обе модели · другое · News item about the Johns Hopkins kratom user survey on abuse potential. Secondary report; trace to the original study, which may have assessed DSM-5 criteria.

**Решение:** =

---

### 175 · R2752

**Pharmacokinetic And Pharmacodynamic Modeling Of Mitragynine In PainTolerance**

2020 · review · https://core.ac.uk/download/529918651.pdf

Mitragyna speciosa, also known as ‘Ketum’or ‘Biak-biak’ in Malaysia and Kratom in Thailand, is a native plant to Southeast Asia. It has a long history of folk medicine use in Southeast Asia and recently has gained popularity in Western countries. Mitragynine (MG) is the principal alkaloid found in the leaves of Mitragyna speciosa and has been reported to be responsible for the plant’s therapeutic actions. Pain relief is among many self-reported beneficial kratom effects. However, there have not been any controlled clinical studies reported on the analgesic property of Ketum employed a standardized formulation. The objective of this study is to evaluate the PKPD of mitragynine in human subjects. In view of this, work was undertaken in Universiti Sains Malaysia to scientifically assess the pain relief effects of Ketum decoction in a randomized, double-blind, placebo- controlled study. Ketum and placebo decoctions were prepared and standardized as a formulation to be administered to the subjects in the clinical study

**ИИ:** разошлись — Opus ? (неясно, оценивали ли зависимость: Kratom decoction pain RCT at USM; subjects may be regular kratom users; abstract doesn't say whether dependence was assessed.); Sonnet -2 (качественное исследование без подсчёта людей (интервью, форумы, Reddit); доклиника: животные, клетки, химия, ботаника, анализ продуктов: Randomized placebo-controlled PK/PD study of Ketum decoction for pain tolerance in human subjects; no dependence or use-disorder measure, and subjects are not described as kratom users.)

**Решение:** - фармакокинетический эксперимент с моделированием боли у добровольцев

---

### 176 · R2767

**Self-Report Data on Regular Consumption of Illicit Drugs and HIV Risk Behaviors after Kratom (Mitragyna Speciosa korth.) Initiation among Illicit Drug Users in Malaysia.**

2020 · Journal of psychoactive drugs · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1080/02791072.2019.1686553

ABSTRACT This study sought to determine the relationship between kratom (Mitragyna speciosa) initiation and regular consumption of illicit drugs and HIV risk behaviors in a cohort of illicit drug users in Malaysia. 260 illicit drug users with current kratom use were recruited through convenience sampling for this cross-sectional study. All were male, with the majority being Malays (95%, n = 246/260). Results suggest that kratom initiation was associated with significant decrease in the regular use of heroin (odds ratio (OR) = 0.50, 95% confidence interval (CI): 0.40– 0.72; p = .0001), methamphetamine (OR = 0.23, CI: 0.16– 0.35; p < .0001), and amphetamine (OR = 0.17, CI: 0.09– 0.34; p < .0001). Kratom initiation was also associated with reduction in regular HIV risk behaviors such as having sex with sex workers (OR = 0.20, CI: 0.12–0.32; p < .0001), using drugs before sexual intercourse (OR = 0.20, CI: 0.13– 0.31; p < .0001), injecting behaviors (OR = 0.10, CI: 0.04– 0.25; p < .0001), sharing of injection equipment (OR = 0.13, CI: 0.04– 0.43; p < .0001), and injecting with other injection drug users (IDUs) (OR = 0.07, CI: 0.02– 0.24; p < .0001).

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of 260 current kratom users among drug users in Malaysia; kratom dependence may be in the sample table but the abstract doesn't mention it.

**Решение:** =

---

### 177 · R2779

**Improved sexual functioning of long-term daily users of Mitragyna speciosa (Korth.)**

2020 · Journal of Herbal Medicine · article, review, journal article · en · https://doi.org/10.1016/j.hermed.2019.100293

Abstract Kratom leaves from Mitragyna speciosa (Korth.) trees are believed to have medicinal value, and have a long-history of folk medicine use for self-treatment of a broad range of indications. In Southeast Asia, traditional uses of kratom include as an aphrodisiac and a sexual performance enhancer. The study evaluated sexual functioning in a cohort of long-term male kratom users in the state of Penang, Malaysia. A field face-to-face survey, including the Malay version of the Brief Male Sexual Function Inventory (BMSFI) called Mal-BMSFI was conducted between January and December of 2017. The mean (SD) age of the cohort (N = 92) was 37.0 (11.2) years, and the mean (SD) duration of kratom use was 9.14 (5.5) years. All participants reported consuming kratom decoction, with an average amount of 1200 ml daily. Seventy-two participants (78%) reported using kratom to enhance sexual performance, and 71 of them (71/72, 99%) reported experiencing improved sexual performance. Of those who reported not using kratom to enhance sexual performance, 7/20 (35%) also experienced improved sexual performance after kratom use. The reported enhancements of sexual performance included: more energy during sex (75/92), delayed ejaculation (71/92), help to maintain erection (70/92), longer climax (51/92), increased sexual desire (44/92), and reduced sex organ sensitivity (43/92). The mean (SD) Mal-BMSFI score was 33.9 (7.1) and 78/92 (85%) reported overall high satisfaction with their sex life in the past 30 days. In conclusion long-term daily, male users of kratom decoction in Malaysia reported improved sexual functioning attributed to their kratom consumption.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Field survey of long-term daily kratom users in Malaysia; the abstract doesn't say if dependence was assessed, but it may be in the sample tables.

**Решение:** =

---

### 178 · R2782

**Long-Term Effects of Kratom ( Mitragyna speciosa ) Use**

2020 · Malaysian Journal of Medicine and Health Sciences · article

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title could be a review or a study of long-term users that measured dependence.

**Решение:** =

---

### 179 · R2785

**The Use of Benzodiazepines among Kratom (Mitragyna Speciosa Korth.) Users.**

2020 · Journal of psychoactive drugs · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1080/02791072.2019.1632505

ABSTRACT The leaves from Mitragyna speciosa (Korth.) trees, also known as kratom, are traditionally used in Southeast Asia as a mild psychotropic agent. We investigated the demographic characteristics of persons who used both kratom cocktail and benzodiazepines (BZO) in a sample drawn from a rural area in Penang, Malaysia, and the reasons for BZO use. Seventy-seven participants who currently use a kratom cocktail along with BZO were recruited through snowball sampling for this cross-sectional study. The participants were male, and the majority were Malays (99%, n = 76/77), single (57%, n = 44/77) and employed (91%, n = 70/77). BZO was used with kratom cocktail 1) to increase euphoria; 2) to reduce dependence on methamphetamine; 3) to promote sleep; 4) to ease methamphetamine-associated psychological symptoms and 5) to decrease the craving for kratom. There were no significant differences in the intake of kratom use (p = .751), BZO use duration (p = .259), frequency (p = .188) and quantity (p = .888) of BZO use in the last 7 days, and quantity of BZO use in the last 30 days (p = .337) between kratom users and kratom poly-drug users. An awareness of the health consequences of the co-use of kratom with BZO is needed to prevent untoward health incidents.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Cross-sectional survey of kratom cocktail users co-using benzodiazepines in Malaysia; abstract doesn't say whether kratom dependence was assessed.

**Решение:** =

---

### 180 · R2787

**Characterization of diverted buprenorphine use among adults entering corrections-based drug treatment in Kentucky.**

2020 · Drug and alcohol dependence · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.drugalcdep.2020.107837

Background: Illicit, medically unsupervised use of buprenorphine (i.e., “diverted use”) among vulnerable and underserved populations, such as corrections-involved adults, remains underexplored. Methods: Survey data (2016–2017) collected as part of a clinical assessment of incarcerated adults entering corrections-based substance use treatment in Kentucky were analyzed. For years examined, 12,915 completed the survey. Removing cases for participants who did not reside in Kentucky for > 6 months during the one-year pre-incarceration period (n = 908) resulted in a final sample size of 12,007. Results: Over a quarter of the sample reported past-year diverted buprenorphine use prior to incarceration and 21.8 % reported use during the 30-days prior to incarceration, using 6.5 months and 14.3 days on average, respectively. A greater proportion of participants who reported diverted buprenorphine use had previously been engaged with some substance use treatment (77.0 %) and reported greater perceived need for treatment (79.4 %) compared to those who did not report use. Use was more likely among participants who were younger, white, male, and who reported rural or Appalachian residence. Diverted buprenorphine users also evidenced extensive polydrug use and presented with greater substance use disorder severity. Non-medical prescription opioid, heroin, and diverted methadone use were associated with increased odds of diverted buprenorphine use while kratom was not. Diverted methadone use was associated with a 252.9 % increased likelihood of diverted buprenorphine use. Conclusions: Diverted buprenorphine use among participants in this sample was associated with concerning high-risk behaviors and may indicate barriers to accessing opioid agonist therapies for corrections-involved Kentucky residents, particularly those in rural Appalachia.

**ИИ:** разошлись — Opus ? (неясно, оценивали ли зависимость: Corrections treatment survey measured kratom use and SUD severity; unclear whether kratom-specific use disorder criteria were assessed.); Sonnet -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: Corrections treatment survey on diverted buprenorphine; kratom appears only as a use covariate, with no kratom dependence or use disorder measure indicated.)

**Решение:** ? опрос лиц в пенитенциарной системе: оценивалась тяжесть расстройств употребления

---

### 181 · R2808

**Kratom and Pain Tolerance: A Randomized, Placebo-Controlled, Double-Blind Study.**

2020 · The Yale journal of biology and medicine · article, journal article, randomized controlled trial · eng · https://pubmed.ncbi.nlm.nih.gov/32607084/

Background : Kratom has a long history of traditional medicine use in Southeast Asia. Consumption of kratom products has also been reported in the US and other regions of the world. Pain relief is among many self-reported kratom effects but have not been evaluated in controlled human subject research. Methods : Kratom effects on pain tolerance were assessed in a randomized, placebo-controlled, double-blind study. During a 1-day inpatient stay, participants received a randomized sequence of kratom and placebo decoctions matched for taste and appearance. Pain tolerance was measured objectively in a cold pressor task (CPT) as time (seconds) between the pain onset and the hand withdrawal from the ice bath. Health status, vital signs, objective, and subjective indicators of withdrawal symptoms, self-reported data on lifetime kratom use patterns, and assessments of blinding procedures were also evaluated. Results : Twenty-six males with the mean (SD) age 24.3 (3.4) years were enrolled. They reported the mean (SD) 6.1 (3.2) years of daily kratom consumption. Pain tolerance increased significantly 1 hour after kratom ingestion from the mean (SD) 11.2 (6.7) seconds immediately before to 24.9 (39.4) seconds 1 hour after kratom consumption (F(2,53.7)=4.33, p=0.02). Pain tolerance was unchanged after consuming placebo drinks: 15.0 (19.0) seconds immediately before and 12.0 (8.1) seconds 1 hour after consumption of placebo (F(2,52.8)=0.93, p=0.40). No discomfort or signs of withdrawal were reported or observed during 10-20 hours of kratom discontinuation. Conclusions : Kratom decoction demonstrated a substantial and statistically significant increase in pain tolerance. Further rigorous research on kratom pain-relieving properties and a safety profile is needed.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Lab RCT that recruited long-term daily kratom users and assessed withdrawal; unclear whether use disorder or dependence was measured.

**Решение:** =

---

### 182 · R2813

**Why People Use Kratom: Results from an Online Survey**

2020 · Journal watch · review, article · en · https://doi.org/10.1056/nejm-jw.na50943

Kratom is an Asian botanical, traditionally used for pain and purchasable over the internet. Its primary alkaloid is mitragynine, an atypical partial

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: Journal Watch summary of an online kratom survey, labelled a review; the original survey article should be screened separately.); Sonnet ? (неясно, оценивали ли зависимость: Journal Watch summary of an online survey of kratom users; the abstract is truncated and doesn't say whether dependence was assessed, so the underlying survey needs checking.)

**Решение:** - вторичный пересказ в Journal Watch, не первичное исследование

---

### 183 · R2844

**Socio-demographic Characteristics, Kratom Use and Quality of Life (QoL) of Regular Kratom (Mitragyna speciosa Korth.) Users**

2019 · Malaysian Journal of Medicine and Health Sciences · article, review

Introduction: Kratom which is a tropical plant use as traditional remedy in rural areas of Malaysia and Thailand has recently been a research focus worldwide due to its potential as substitution therapy for opioid addiction. However, data on its effect on the quality of life of kratom users is scarce. This study aimed to describe the socio-demographic and history of kratom use as well as assessing the quality of life and its associated factors in Malaysian kratom users. Methods: This cross-sectional survey recruited 150 kratom users and they were administered with socio-demograph- ic and substance history questionnaires, the World Health Organization Quality of Life- BREF (WHOQOL-BREF) to assess quality of life and the Kratom Dependence Scale (KDS) to assess severity of kratom dependence. Results: Respondents were all males with mean age of 34.4 years old (SD= 11.2). Sixty-percent of respondents use kratom > 6 years (mean duration = 8.5 years, SD= 5.3) while 55% (n=83/150) used >3 glasses of kratom daily. Duration of kratom use, quantity of kratom use and severity of kratom dependence were not associated with all the domains of quality of life except severe kratom dependence users had significant lower physical quality of life score when compared to that of users with mild to moderately severe kratom dependence. Conclusion: Based on our study, kra- tom consumption does not cause impairment in quality of life of kratom users except for severe kratom dependence which may cause deterioration in physical well-being of users

**ИИ:** + · обе модели · употребляющие + мера зависимости · Cross-sectional survey of 150 regular Malaysian kratom users that used the Kratom Dependence Scale to grade dependence severity.

**Решение:** =

---

### 184 · R2883

**Kratom as a substitute for opioids: Results from an online survey.**

2019 · Drug and alcohol dependence · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1016/j.drugalcdep.2019.05.005

Background Kratom is a South Eastern Asian tree whose leaves are used to make tea-like brews or swallowed in powdered form for various health and well-being reasons including to relieve pain and opioid withdrawal. It is important to learn more about the potential public health impact of kratom in the context of the opioid epidemic. Methods An anonymous online survey of kratom users (2867 current users and 157 former users) was conducted in September 2017 through the American Kratom Association and associated social media sites. Results Kratom was used primarily to relieve pain (endorsed by 48% of respondents), for anxiety, PTSD, or depression (22%), to increase energy or focus (10%) and to help cut down on opioid use and/or relieve withdrawal (10%). Over 90% of respondents who used it in place of opioids indicated that it was helpful to relieve pain, reduce opioid use, and relieve withdrawal. The reported incidence of bad adverse reactions was 13%, and reactions were overwhelmingly mild and self-managed. Conclusions Respondents reported using kratom for conditions which often require use of opioids, including pain and reduction of opioid use. The high self-reported efficacy and low incidence of adverse reactions associated with kratom use suggest that it may provide a potential alternative to opioids for some persons even though it has not been evaluated in multi-center clinical trials or approved for any therapeutic purpose. Further study of kratom, including systematic characterization of its safety and efficacy for various conditions is warranted.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Large online survey of kratom users; the abstract doesn't say whether dependence or use-disorder criteria were assessed.

**Решение:** =

---

### 185 · R2897

**Characteristics and physical outcomes of kratom users at a substance abuse treatment center**

2019 · Chulalongkorn Medical Journal · article, journalarticle, text/article · en · https://doi.org/10.58837/chula.cmj.63.3.6

Background: Despite many disadvantages such as physical and mental disorders, family disruption, crime, etc., substance use disorder is continuously reported worldwide. Twenty - nine million people were reported to suffer from substance abuse. In addition, the survey found that only 1/6 of substance abusers throughout the world were able to access medical services. Kratom (Mitragyna speciosa Korth) has been used not only as medicine, but also as psychedelic drug for a long time.Objective: To study behavioral and physical consequences of kratom use.Methods: One hundred and six kratom users were recruited into this study at the Princess Mother NationalInstitute on Drug Abuse Treatment (PMNIDAT). Collected data included1) general information,2) kratom use profile,3) side effects from using kratom,4) Naranjo’s algorithm, and5) Semi-structuredAssessment for Drug Dependence and Alcoholism (SSADDA) Section H. Statistics used to analyze these data were percentage, mean, standard deviation, independent t-test, Chi-square test, and Pearson’s correlation.Results: Kratom use was classified as either boiling (55.6%) or chewing (41.7%). A number of kratom users often took other substances. Although the boiling-pattern group took more other drugs, the chewing-pattern group significantly had more headaches, arthritis, nausea, or constipation when compared to the other.Conclusion: Kratom substance users frequently use other substances. There are multiple adverse effects fromboth patterns of kratom use.

**ИИ:** ? · обе модели · другое · Kratom users at a treatment centre were assessed with SSADDA for dependence; unclear whether they were recruited because of kratom problems.

**Решение:** =

---

### 186 · R2901

**Prevalence and Correlates of Electronic Cigarette Use Among a Clinical Sample of Polysubstance Users in Kentucky: Long Live the Cigarette?**

2019 · Substance use & misuse · article, journal article, journalarticle · eng · https://doi.org/10.1080/10826084.2018.1512629

Abstract Background: E-cigarette use has increased in the US, yet, in some regions rates of cigarette use remain high. Purpose: To describe the prevalence and features of lifetime and past-year e-cigarette use among a clinical sample of polysubstance users in Kentucky, and to determine significant associations of past-year e-cigarette use. Results: Of the final sample (N = 497), 83.5% reported having ever used e-cigarettes and 97.2% reported having ever used cigarettes. These rates surpass those found among Kentucky’s general population. Compared to those who did not report e-cigarette use, e-cigarette users were more likely to be younger ( = 33.4 vs. 43.6, p<.001) and White (88.2.1% vs. 62.5%, p = .001). E-cigarette users showed higher rates for lifetime incarceration (91.1% vs. 72.8%, p = .001) and past-year arrest (75.0% vs. 47.5%, p = .001). This group also presented with more severe substance use history and lower mean age for illicit drug use initiation ( = 13.8 vs. 16.4, p = .001). Approximately 65% of the sample reported past-year e-cigarette use and 96.6% reported past-year cigarette use. Logistic regression indicated that being younger (AOR = .973, p = .030), White (AOR = 1.92, .046), having a past-year arrest (AOR = 1.73, p = .047) and having used cigarettes (AOR = 8.93, p = .001) or kratom (AOR = 3.04, p = .025) within the past year were significantly associated with past-year e-cigarette use. Conclusions: E-cigarette use was related to more severe drug-using patterns. Rates of dual tobacco use among this sample are high, particularly among younger individuals. In ecological contexts where cigarette use remains normative, it is likely that dual use will persist for nicotine-dependent, polysubstance-using individuals.

**ИИ:** разошлись — Opus -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: E-cigarette study in polysubstance users; past-year kratom use appears only as a correlate, and no kratom dependence measure is indicated.); Sonnet ? (неясно, оценивали ли зависимость: Clinical polysubstance sample in Kentucky; kratom is only a correlate of e-cigarette use, and the abstract doesn't say whether kratom dependence was assessed.)

**Решение:** - исследование электронных сигарет, нет меры зависимости от кратома

---

### 187 · R2945

**The prevalence of psychotic symptoms in kratom (Mitragyna speciosa Korth.) Users in Malaysia.**

2019 · Asian journal of psychiatry · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.ajp.2019.07.008

Background Kratom is a traditional medicinal herb widely used in Malaysia and Thailand. Despite its widespread use and statements by regulatory agencies on the potential for kratom-associated psychosis, there is little data regarding the prevalence of psychotic symptoms among kratom users. This study investigated the prevalence of psychosis among kratom users, described psychotic symptomatology and severity, while examining associations between kratom use characteristics and the occurrence of psychotic symptoms. Methods This cross-sectional clinical survey recruited 150 regular kratom users. The Mini International Neuropsychiatric Interview (MINI) and Diagnostic and Statistical Manual of Mental Disorders 5 th Edition (DSM-V) diagnostic criteria were used to evaluate psychotic symptomatology among kratom users, and the Brief Psychiatric Rating Scale (BPRS) was used to assess the severity of psychiatric symptoms. Chi-square tests with Yate's correction were performed to determine the association between kratom use characteristics and the occurrence of psychotic symptoms among kratom users in this study. Results Six out of 150 kratom users (4%) presented with any psychotic symptoms. The psychotic symptoms reported were positive symptoms and thought alienation, with a mean BPRS score of 33 (i.e., mild severity). Variables related to kratom use (such as intake of kratom with diphenhydramine, duration of kratom use, and quantity and frequency of daily kratom use) were not associated with the occurrence of psychotic symptoms among kratom users. Conclusion Although psychotic symptoms could occur among regular kratom users, they were rare and not significantly associated with kratom use characteristics. We found no evidence of elevated psychosis among regular users.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of 150 regular kratom users using MINI and DSM-5; abstract mentions only psychosis, but kratom dependence may be in the sample table.

**Решение:** =

---

### 188 · R2964

**Distinct kratom user populations across the United States: A regional analysis based on an online survey.**

2019 · Human psychopharmacology · article, journal article, journalarticle · eng · https://doi.org/10.1002/hup.2709

Abstract Objective Kratom preparations have raised concerns of public health and safety in the United States. This paper analyzed the patterns and predictors of kratom use by four U.S. regions according to the U.S. Census. Method An anonymous cross‐sectional online survey yielded 8,049 valid responses. The data were categorised by regions (Northeast, South, Midwest, and West) and analyzed for the following predictors: age, gender, marital status, ethnicity, employment status, insurance coverage, education, and household income. Results After adjusting for state population, the survey response rates were highest from Oregon, Idaho, and Florida. Kratom use was significantly lower for both prescription drug dependency and acute or chronic pain in the Northeast region than the rest of the country. Multiple logistic regression models found that gender, employment, and education were significant on the regional level. Higher education was associated with lower kratom use for an illicit drug dependency ( p = .002) independent of region whereas men were less likely to use kratom for acute or chronic pain in the Northeast ( p &lt; .001) but more likely in the Midwest ( p = .041). Conclusions The regional pattern of kratom use differed from opioid use data in both demographics and trend direction warranting further investigation.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Large online survey of US kratom users analysing reasons for use by region; abstract doesn't say whether kratom dependence was assessed.

**Решение:** =

---

### 189 · R2988

**Poster Abstract: Detecting Kratom Intoxication in Wearable Biosensor Data**

2019 · IEEE/ACM Conference on Connected Health: Applications, Systems and Engineering Technologies · article, conference object, conference paper · en · https://doi.org/10.1109/chase48038.2019.00028

In the ongoing opioid addiction crisis, users who lack access to treatment have sought novel methods to relieve withdrawal symptoms. Among these is a psychoactive plant from South-East Asia popularly known as kratom. With its spreading consumption it would be valuable to automatically detect kratom use. Although wearable biosensors have been applied to detect substance use in the past, kratom's effects are not as well understood and can be paradoxical. In this paper, we perform supervised learning on a set of features extracted from streaming kratom data gathered from wrist-worn biosensors deployed on participants over a period of several days.We extract several time domain features, define a period of intoxication post-use based on the existing literature, and compare four classifiers based on their accuracy, sensitivity, and specificity. Our results show that kratom use can be detected with 95% accuracy using a random forest classifier in data collected from home use.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Wearable biosensor study of people using kratom at home; sample description might report use disorder, but the abstract doesn't mention dependence.

**Решение:** =

---

### 190 · R2995

**Self-reported prevalence and severity of opioid and kratom (Mitragyna speciosa korth.) side effects.**

2019 · Journal of ethnopharmacology · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.jep.2019.111876

Ethnopharmacological relevance Mitragyna speciosa (Korth.) is a traditional medicinal plant widely used in Southeast Asia for its opioid-like effects. Although kratom produces analgesia through binding of mitragynine and other alkaloids at the mu-opioid receptor (MOR), the association of long-term kratom use with adverse opioid-like effects remains unknown. Aim of the study To determine the self-reported prevalence and severity of opioid-related adverse effects after kratom initiation in a cohort of illicit opioid users. Materials and methods A total of 163 illicit opioid users with current kratom use history were recruited through convenience sampling from the northern states of Peninsular Malaysia. Face-to-face interviews were conducted using a semi-structured questionnaire. Results Respondents were all males, majority Malays (94%, n = 154/163), with a mean age of 37.10 years (SD = 10.9). Most were single (65%, n = 106/163), had 11 years of education (52%, n = 85/163) and employed (88%, n = 144/163). Half reported using kratom for over >6 years (50%, n = 81/163), and 41% consumed >3 glasses of kratom daily (n = 67/163). Results from Chi-square analysis showed kratom initiation was associated with decreased prevalence of respiratory depression, constipation, physical pain, insomnia, depression, loss of appetite, craving, decreased sexual performance, weight loss and fatigue. Conclusions Our findings indicate that kratom initiation (approximately 214.29 mg of mitragynine) was associated with significant decreases in the prevalence and severity of opioid adverse effects.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of 163 opioid users who currently use kratom; abstract doesn't say if kratom dependence was assessed, which similar Malaysian studies often do.

**Решение:** =

---

### 191 · R2996

**Kratom Use and High-Risk Substance Use Behaviors in the United States Non-Medical Use of Prescription Drugs National Survey**

2019 · Annals of Emergency Medicine · article, review, journal article · en · https://doi.org/10.1016/j.annemergmed.2019.08.292

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. This national survey of kratom users and high-risk substance use might report kratom dependence measures, so the full text is needed.

**Решение:** =

---

### 192 · R2999

**Effects of Kratom (Mitragyna Speciosa Korth.) Use in Regular Users.**

2019 · Substance use & misuse · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1080/10826084.2019.1645178

Background: Mitragyna speciosa (Korth.) or kratom is an indigenous medicinal plant of Southeast Asia. Kratom is widely reported to have dose-dependent effects based on available literature, but to our knowledge, this has not been established conclusively. Objective: This study sought to evaluate if kratom use produces dose-dependent effects, with a stimulant effect at low doses and a sedative effect at high doses, in a sample of regular kratom users. Methods: A total of 63 regular kratom users participated in this cross-sectional study. The Brief-Biphasic Alcohol Effects Scale (B-BAES) was used to determine subjects self-report kratom use experiences. Results: Almost all in the sample were male (98%, n = 62/63), and the majority of subjects were Malays (94%, n = 59/63). The mean age of the subjects in the sample was 43.8 years (SD = 12.1). Seventy-five percent (n = 47/63) have >5 years kratom use history, and 65% (n = 41/63) consumed >3 glasses of kratom daily. Results from first test showed no significant difference in the stimulant (t 61 =0.371, p 61 =502, p 3 glasses a day or less than this amount, regardless of duration of use. In the second test, no significant differences in the mean scores were found among those who consumed >3 glasses daily or less than this amount among short-term or long-term uses. Conclusions: Daily kratom use produced both stimulant and sedative effects but they were not statistically significantly associated with the dose consumed, both among short-term and long-term users in our sample.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Cross-sectional survey of 63 regular kratom users; the abstract doesn't say whether dependence was assessed, so the full text may.

**Решение:** =

---

### 193 · R3000

**Long-Term Cognitive Effects of Kratom (Mitragyna speciosa Korth.) Use.**

2019 · Journal of psychoactive drugs · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1080/02791072.2018.1555345

ABSTRACT Kratom or Mitragyna speciosa (Korth.) is a medicinal plant of Southeast Asia. As a result of its opioid-like effects, it remains unknown whether consumption of kratom tea is associated with impaired cognitive function. We assessed the cognitive function of 70 regular kratom users and 25 control participants using the Cambridge Neuropsychological Test Automated Battery. Participants performed six neuropsychological tasks that assessed motor, learning and memory, attention and executive function. Relative to control participants, higher consumption (>3 glasses daily or mitragynine doses between 72.5 mg and 74.9 mg) of kratom tea was selectively associated with impaired performance on the Paired Associates Learning task, reflecting deficits in visual episodic memory and new learning. Overall, the performance of kratom users compared to control participants, and the performance of high (>3 glasses per day) as well as low (≤3 glasses per day) kratom using groups, were comparable on all neuropsychological domains. Higher intake of kratom juice (>3 glasses daily) did not appear to impair motor, memory, attention or executive function of regular kratom users.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Study of 70 regular kratom users; the abstract doesn't say whether dependence was assessed, but sample tables in this research group's papers often report it.

**Решение:** =

---

### 194 · R3002

**Prevalence of Amphetamine-Type Stimulants (ATS) use among clients in primary and private Methadone Maintenance Treatment (MMT) program in Kuantan, Malaysia**

2019 · Journal of Substance Use · article · https://doi.org/10.1080/14659891.2019.1642409

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; Malaysian methadone clients' substance use may include kratom, but it is unclear whether kratom dependence was assessed.

**Решение:** =

---

### 195 · R3004

**Non-Prescribed Buprenorphine Use Mediates the Relationship between Heroin Use and Kratom Use among a Sample of Polysubstance Users.**

2019 · Journal of psychoactive drugs · article, journal article, research support, n.i.h., intramural · eng · https://doi.org/10.1080/02791072.2019.1597224

ABSTRACT In Asia, Mitragyna speciosa (e.g., “kratom”) has been used to mitigate alcohol and drug dependence. Some preliminary findings suggest kratom’s potential use as an informal harm-reduction method in the United States, such as an opioid substitute or as a means of lessening opioid withdrawal symptoms. To determine correlates of past-year kratom use among a sample of polysubstance users enrolled in residential recovery programs in Kentucky, an anonymous survey was completed by clients in April 2017. Logistic regression was used to identify significant associations with past-year kratom use. Of the final sample (N = 478), 10.4% reported past-year kratom use. Past-year heroin use, but not past-year prescription opioid (e.g., oxycodone, hydrocodone) use, was significantly associated with kratom use, such that individuals who reported past-year heroin use were 2.5 times more likely to also report past-year kratom use. Non-prescribed buprenorphine (i.e., Suboxone) use partially mediated the relationship between past-year heroin and kratom use by explaining 36% of the association between the two drugs. Though amphetamines were highly preferred, past-year use was negatively correlated with past-year kratom use. Rates of past-year kratom use were lower than rates of alcohol and illicit drug use. Kratom was not preferred over heroin or prescription opioids.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of polysubstance users in residential recovery reporting past-year kratom use; abstract doesn't say whether kratom dependence was assessed.

**Решение:** =

---

### 196 · R3046

**ปัจจัยส่วนบุคคล สังคมและระดับความรู้ที่มีความสัมพันธ์กับสาเหตุและพฤติกรรมการใช้ยาเสพติดชนิด 4X100 ของเด็กและเยาวชนในสถานพินิจ และคุ้มครองเด็กและเยาวชนเขต 8 และ 9**

2019 · Journal of Social Work and Social Administration · article · th

This research examines the Personal factors, society factors and knowledge level related to causes and behaviors of taking 4x100 drug type, among children and youth in The Venue of Youth Observation and Protection in Zone 8 and 9. The purpose of this research aimed to study personal factors, social factors and level of knowledge on the dangers of the 4x100 drug amongst the adolescent and young people; as well as to propose preventive measures for 4x100 drug problems in adolescents and young people. Employing purposive sampling method, the research limits target of study solely to the adolescent and young people who were punished by law for the use of Kratom drug in Observation and Protection Center Area 8 and 9 consisting of 14 centers in total. The research uses quota sampling system to study 200 samples, by distributing the quota proportionately to the population in each center. The results reveal that the majority of the sample group are of 16-17 years old (70.5%), have received primary school education (74.5%), have 2-3 siblings (64.5%), live with parents (76%) and have a monthly income less than 1,500 baht (31.5%).The majority of the group (51.7%) are aware of the dangers of 4x100 drug, while the other 48.3% are not aware of the dangers of the substance. The average frequency of 4x100 drug use is 3-4 times/week (35.5%) with moderate use (average 1.85, SD=1.137). The majority of the sample group are moderately self-responsible (average 2.36, SD=1.058), have a neutral relationship with their families (average 2.07, SD=1.097) and have been intensively disciplined by family (average 2.81, SD 1.045). Research suggestions (1) There should be an education program that provides knowledge on drugs for children and youth from early childhood, in order to prevent the use of drugs in children and youth. The research found that most children and youth who use drugs are 14 years old and above, which is the teenage period when there are many changes in self-development. However, if knowledge is given since childhood, it will result in lower drug consumption. (2) Student leaders should be appointed to help keep their friends, children, and youth away from drugs. (3) Provide knowledge on development of children and teenagers to parents and teachers, to observe changes in emotions, and behavior that need to be well taken care of. (4) Prevent media consumption such as television, magazine, radio, Internet, etc. and be aware strictly of social responsibility by controlling media that may influence the behavior of the sample group such as video of drug consumption on Facebook, or scenes of actors or actress taking drugs, etc. (5) Encourage parents to cultivate responsibility for the value of money and encourage children and youth to know how to save money since young. This is in order for children and youth to develop responsible money habits and not spend money in the wrong way.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of 200 detained youths who use 4x100 kratom cocktail; abstract gives use frequency but doesn't say whether dependence was assessed.

**Решение:** =

---

### 197 · R3074

**Kratom use, psychiatric comorbidity and the psychosocial correlates among FELDA settlers in northern Peninsular Malaysia / Al-Zilal Abdul Wahid**

2018 · University of Malaya Students Repository · dissertation, text · en · https://core.ac.uk/download/328341261.pdf

Kratom use, psychiatric comorbidity and the psychosocial correlates among FELDA settlers in Northern Peninsular Malaysia Introduction: Kratom (Mitragyna Speciosa, Korth) is an indigenous plant of South East Asia, particularly in Malaysia, Thailand, and Indonesia. For centuries people use Kratom as a traditional remedy to treat various ailments. Its inclusion into the New Psychoactive Substance (NPS) and extensive availability have brought about concerns regarding its current use, and potential harm. Despite the rising concerns, the prevalence of its use among rural settlers, its sociodemographic factors as well as the impact on mental illness of regular-users and quality of life is scarce. Objectives: The study aims at finding the prevalence of Kratom use among the rural settlers in a Felda settlement, located in the northern region of Malaysia. Its associating factors, as well as any psychiatric co-morbidities, is examined to ascertain the effects of Kratom use among the respondents. Method: The study recruited participants on a voluntary basis. The study chose the largest Felda settlement in Perlis. Its residents all originate from Perlis and have stayed at the site for generations. The study obtained the sociodemographic data, and trained individuals assessed all the respondents using the MINI, ASSIST-M, WHOQoL-Bref questionnaires. viii Results: The study recruited a total sample of 144 participants. The Kratom users were determine using the MINI, the ASSIST-M and the WHOQoL-BREF-Malay Version questionaire. The prevalence of Kratom use was 24.3% (n=35) among the participants. The univariate analysis found statistically significant association (p\u3c0.01) between the Kratom user and age, gender, marital status, education level, employment status, general illness, history of illicit substance use, the presence of family members abusing illicit substance, smoking and opioid dependency. The multiple logistic regression analysis identified a significant association between Kratom users with history of drug, and tobacco use. The participants with moderate and high tobacco use and past and present other substance usage are likely to be a Kratom-user. In the assessment of their quality of life, Kratom-users reported feeling physically healthier than the non-users. However, though close to 70% are employed, their average income is less than two thousand ringgits per month. Moreover, among the Kratom-users, almost all are smokers, smoking an average of 20 sticks per day (IQR=10) and they started smoking at a mean age of 15.4 years (SD=3.35). Conclusion: The study found a high prevalence of Kratom-use among the rural settlers. The study identified a robust association of Kratom use with tobacco and opioid usage. The participants with moderate and high tobacco use plus past and present other substance use are likely to be a Kratom-user. The study concludes the severity of the problem is chronic and worrying. The report should serve as a precursor for further researches in this area as well as possible health policy-making

**ИИ:** + · обе модели · опрос населения с ASSIST, DSM или ICD · Community survey of FELDA settlers used MINI and ASSIST-M; 35 kratom users, so kratom dependence or risk scores among users are likely reportable.

**Решение:** =

---

### 198 · R3076

**Trends in the use of illicit substances in Thailand: Results from national household surveys.**

2018 · Drug and alcohol review · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1111/dar.12689

Abstract Introduction and Aims Thailand borders some of the world’s largest methamphetamine and opioid producing countries and trafficking routes. Thailand’s ‘War on Drugs’ campaign was launched in 2003. This study reports trends in illicit substance use in Thailand over the period 2001–2011. Design and Methods National Household surveys on illicit drug use were conducted in 2001, 2003, 2007, 2008 and 2011. A stratified multi‐stage cluster random sampling technique was implemented for each survey. Provinces in four regions were systematically selected using a probability proportionate to the size of the targeted population. Participants were interviewed using structured questionnaires on their history of substance use. Results The prevalence of illicit drug use within the past drastically decreased from 4.5% in 2001 to 1.0% in 2003 ( P &lt; 0.05). Since 2003, the prevalence of illicit use within the past year varied between 1.0% and 1.3%. By 2011, it was estimated that 0.84% have used kratom (a substance derived from Mitragyna speciosa) within the past year. Around 0.20% and 0.19% reported using cannibis and yaba (metamphetamine tablet) within a year of the 2011 survey. Other types of illicit drugs were less commonly used in Thailand. Discussion and Conclusions There was a decrease in prevalence of illicit drug use within the past year between 2001 and 2003 in Thailand. Since 2003, the past year prelavence of illicit drug use has remained relatively stable. From 2001 to 2011, cannabis, kratom and yaba have remained the three most commonly reported types of illicit drugs used in Thailand.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Thai national household surveys measured kratom use; the abstract doesn't say whether dependence or use disorder was assessed among users.

**Решение:** =

---

### 199 · R3083

**Clusters of alcohol and drug use and other health-risk behaviors among Thai secondary school students: a latent class analysis.**

2018 · BMC public health · article, other literature type, journal article · eng · https://doi.org/10.1186/s12889-018-6205-z

La consommation d'alcool et de drogues et d'autres comportements à risque pour la santé ont tendance à se regrouper chez les adolescents et à causer beaucoup de dommages à eux-mêmes et aux autres. Cet article vise à caractériser les élèves du secondaire en fonction de leurs groupes de comportements à risque pour la santé et à identifier les facteurs déterminant l'appartenance de la classe à ces groupes de comportements. Les données d'une enquête scolaire nationale ont été utilisées pour identifier des grappes de consommation d'alcool et de drogues et d'autres comportements à risque pour la santé chez les élèves du secondaire âgés de 12 à 15 ans à l'aide d'un modèle de régression de classe latente. Un modèle de régression logistique multinomiale a été utilisé pour identifier les prédicteurs de l'appartenance au cluster. Au total, 25 566 élèves ont été inclus dans l'analyse, dont 88 % ont été classés comme ayant des comportements à faible risque signalant une consommation modérée d'alcool ; 11 % comme ayant des comportements à risque modéré, tels que conduire sous l'influence de l'alcool, se battre, porter une arme et consommer de l'alcool et du tabac ; et 0,6 % comme ayant des comportements à risque élevé, tels que la consommation de drogues illicites, en particulier le kratom et le cannabis. Les hommes, les élèves plus âgés, ceux ayant un mauvais rendement scolaire, ne vivant pas avec leurs parents, la consommation de drogues par les membres de la famille et les pairs, et ayant un faible niveau de mépris perçu de leurs amis s'ils consommaient des drogues étaient des facteurs de risque importants pour être dans les classes de comportement à risque modéré et élevé. La consommation d'alcool, de tabac et de drogues, ainsi que d'autres comportements à risque pour la santé tels que les combats, sont regroupés chez les élèves du secondaire thaïlandais. Ce résultat souligne l'importance de stratégies globales de prévention et d'éducation, en particulier pour les groupes à risque modéré à élevé. El consumo de alcohol y drogas y otras conductas de riesgo para la salud tienden a agruparse entre los adolescentes y contribuyen en gran medida a dañarse a sí mismos y a los demás. Este documento tiene como objetivo caracterizar a los estudiantes de secundaria en función de sus grupos de comportamientos de riesgo para la salud e identificar los factores que determinan la membresía de la clase a estos grupos de comportamiento. Los datos de una encuesta escolar nacional se utilizaron para identificar grupos de consumo de alcohol y drogas y otros comportamientos de riesgo para la salud entre estudiantes de secundaria de 12 a 15 años utilizando un modelo de regresión de clase latente. Se utilizó un modelo de regresión logística multinomial para identificar los predictores de la pertenencia al clúster. Un total de 25.566 estudiantes fueron incluidos en el análisis, de los cuales el 88% fueron clasificados como teniendo comportamientos de bajo riesgo reportando solo consumo moderado de alcohol; el 11% como teniendo comportamientos de riesgo moderado, como conducir bajo la influencia del alcohol, pelear, portar un arma y el consumo de alcohol y tabaco; y el 0,6% como teniendo comportamientos de alto riesgo, como el uso de drogas ilícitas, particularmente kratom y cannabis. Los hombres, los estudiantes mayores, aquellos con un bajo rendimiento escolar, que no viven con los padres, el uso de drogas por parte de familiares y compañeros, y tener un bajo nivel de desdén percibido de sus amigos si usaban drogas fueron factores de riesgo significativos para estar en las clases de comportamiento de riesgo moderado y alto. El consumo de alcohol, tabaco y drogas, así como otras conductas de riesgo para la salud, como las peleas, se agrupan en los estudiantes de secundaria tailandeses. Este resultado pone de relieve la importancia de las estrategias integrales de prevención y educación, en particular para los grupos de riesgo moderado a alto. Alcohol and drug use and other health-risk behaviors tend to cluster together among adolescents and contribute a large amount of harm to both themselves and to others. This paper aims to characterize secondary school students based on their clusters of health-risk behaviors and identify factors determining class membership to these behavior-clusters. Data from a national school survey was used to identify clusters of alcohol and drug use and other health-risk behaviors among secondary school students aged 12–15 years using a latent class regression model. A multinomial logistic regression model was used to identify predictors of the cluster membership. A total of 25,566 students were included in the analysis, of which 88% were classified as having low-risk behaviors reporting only moderate alcohol use; 11% as having moderate-risk behaviors, such as driving under the influence of alcohol, fighting, carrying a weapon, and alcohol and tobacco use; and 0.6% as having high-risk behaviors, such as use of illi

**ИИ:** разошлись — Opus ? (неясно, оценивали ли зависимость: National Thai school survey that measured kratom use; dependence seems unlikely but the abstract doesn't rule it out.); Sonnet -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: Thai school survey latent class analysis of risk behaviors; kratom only as part of illicit drug use cluster, no dependence or use disorder measure apparent.)

**Решение:** - опрос школьников в Таиланде: кластеры риска, нет меры зависимости от кратома

---

### 200 · R3133

**Neuroticism Is Associated with Chronic Severe Pain among Ex-Opioid Users on Methadone Maintenance Therapy**

2018 · International Medical Journal · article, text/journal article, research article · en · https://doi.org/10.5281/zenodo.2586234

{"references": ["Rosenblum A, Joseph H, Fong C, Kipnis S, Cleland C, Portenoy RK. Prevalence and characteristics of chronic pain among chemically dependent patients in methadone maintenance and residential treatment facilities. JAMA. 2003;289(18):2370-8.", "Peles E, Schreiber S, Gordon J, Adelson M. Significantly higher methadone dose for methadone maintenance treatment (MMT) patients with chronic pain. Pain. 2005;113(3):340-6.", "Barry DT, Beitel M, Garnet B, Joshi D, Rosenblum A, Schottenfeld RS. Relations among psychopathology, substance use, and physical pain experiences in methadone- maintained patients. J Clin Psychiatry. 2009;70(9):1213-8.", "Verhaak PFM, Kerssens JJ, Dekker J, Sorbi MJ, Bensing JM. Prevalence of chronic benign pain disorder among adults: a review of the literature. Pain. 1998;77(3):231-9.", "Portenoy RK, Ugarte C, Fuller I, Haas G. Population-based survey of pain in the United States: differences among white, African American, and Hispanic subjects. J Pain. 2004;5(6):317-28.", "Pud D, Zlotnick C, Lawental E. Pain depression and sleep disorders among methadone maintenance treatment patients. Addict Behav. 2012;37(11):1205-10.", "Barry DT, Bernard MJ, Beitel M, Moore BA, Kerns RD, Schottenfeld RS. Counselors' experiences treating methadone-maintained patients with chronic pain: a needs assessment study. J Addict Med. 2008;2(2):108-11.", "Othman Z, Gani FA. Attendance at counselling sessions predicts good treatment response in methadone maintenance therapy. Int Med J. 2017;24(1):21-3.", "Karasz A, Zallman L, Berg K, Gourevitch M, Selwyn P, Arnstein J. The experience of chronic severe pain in patients undergoing methadone maintenance treatment. J Pain Symptom Manage. 2004;28(5):517-25.", "Lahey BB. Public health significance of neuroticism. Am Psychol. 2009;64(4):241.", "Ormel J, Jeronimus BF, Kotov R, Riese H, Bos EH, Hankin B, et al. Neuroticism and common mental disorders: Meaning and utility of a complex relationship. Clin Psychol Rev. 2013;33(5):686-97.", "Goubert L, Crombez G, Van Damme S. The role of neuroticism, pain catastrophizing and pain-related fear in vigilance to pain: a structural equations approach. Pain. 2004;107(3):234-41.", "Lin EH, Katon W, Von Korff M, Tang L, Williams Jr JW, Kroenke K, et al. Effect of improving depression care on pain and functional outcomes among older adults with arthritis: a randomized controlled trial. JAMA. 2003;290(18):2428-9.", "Peles E, Schreiber S, Hetzroni T, Adelson M, Defrin R. The differential effect of methadone dose and of chronic pain on pain perception of former heroin addicts receiving methadone maintenance treatment. J Pain. 2011;12(1):41-50.", "Compton P, Canamar CP, Hillhouse M, Ling W. Hyperalgesia in heroin dependent patients and the effects of opioid substitution therapy. J Pain. 2012;13(4):401-9.", "White JM. Pleasure into pain: the consequences of long-term opioid use. Addict Behav. 2004;29(7):1311-24.", "Hassan Z, Muzaimi M, Navaratnam V, Yusoff NH, Suhaimi FW, Vadivelu R, et al. From kratom to mitragynine and its derivatives: physiological and behavioural effects related to use, abuse, and addiction. Neurosci Biobehav Rev. 2013;37(2):138-51.", "Shamima AR, Fakurazi S, Hidayat MT, Hairuszah I, Moklas MAM, Arulselvan P. Antinociceptive action of isolated mitragynine from Mitragyna speciosa through activation of opioid receptor system. Int J Mol Sci. 2012;13(9):11427-42.", "Vicknasingam B, Mahmud M. Malaysian drug treatment policy: An evolution from total abstinence to harm reduction. Jurnal Antidadah Malaysia. 2008;3:107-21.", "Tan G, Jensen MP, Thornby JI, Shanti BF. Validation of the Brief Pain Inventory for chronic nonmalignant pain. J Pain. 2004;5(2):133-7.", "Aisyaturridha A, Naing L, Nizar AJ. Validation of the Malay Brief Pain Inventory questionnaire to measure cancer pain. J Pain Symptom Manage. 2006;31(1):13-21.", "John OP, Srivastava S. The Big Five trait taxonomy: History, measurement, and theor e t i c a l p e r s p e c t i v e s . Handbook of p e r s o n a l i t y : Theory and r e s e a r c h . 1999;2(1999):102-38.", "John OP, Naumann LP, Soto CJ. Paradigm shift to the integrative big five trait taxonomy. Handbook of personality: Theory and research. 2008;3:114-58.", "Muhamad H. A cross-cultural validation of western constructs of spirituality, personality traits, and cognitive beliefs, and their interrelations in a Malaysian context: Monash University. Faculty of Education. Krongold Centre; 2013.", "Beck AT, Steer RA, Brown GK. Beck depression inventory-II. San Antonio, TX. 1996:78204-2498.", "Beck AT, Steer RA, Carbin MG. Psychometric properties of the Beck Depression Inventory: Twenty-five years of evaluation. Clin Psychol Rev. 1988;8(1):77-100.", "Oei TP, Mukhtar F. Exploratory and confirmatory factor validation and psychometric properties of the Automatic Thoughts Questionnaire for Malays (ATQ-Malay) in Malaysia. Hong Kong J Psychiatry. 2008;18(3):92-101.", "Mukhtar F, Zulkefly NS. The Beck Anxiety Inve

**ИИ:** ? · обе модели · нет аннотации · Only references available; Malaysian methadone sample citing kratom literature, so kratom use/dependence may have been assessed as a covariate.

**Решение:** =

---

### 201 · R3142

**Polydrug use among kratom users: Findings from the 2011 Thailand National Household Survey**

2018 · Journal of Substance Use · article, review, journal-article · en · https://doi.org/10.1080/14659891.2018.1436599

Despite the availability of numerous anecdotal reports of polydrug use in kratom users, few studies have been carried out in Thailand. This study aimed to explore the problem of polydrug use among Thai kratom users. A national household survey on the prevalence of substance use was conducted in 2011 using a multistage random sampling technique. Participants were interviewed using a structured questionnaire. The frequency of other substance use was compared between respondents with and without a history of kratom use. Of the total sample (18,457), 544 (2.9%) acknowledged kratom use. Eighty-nine (46.1%) used it almost every day. The mean age of users (SD) was 42.7 (12.8) years old, 459 (84.4%) were male, and 264 (48.5%) had used other illicit drugs in the past. Kratom users were significantly more likely to use heroin, ecstasy, and ice with adjusted odds ratios of 39.7, 30.5, and 29.1, respectively. Of 195 who acknowledged kratom use in the past 12 months, 22 (11.3%) concurrently used other illicit drugs, including cannabis, amphetamine-type stimulants (ATSs), and inhalants. Polydrug use is common in Thai kratom users who are more likely to use opiates and ATSs in their lifetime. Another drug concurrently used was cannabis. Health personnel need to be aware of polydrug use in this population.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Thai national household survey of kratom users; abstract covers polydrug use only, but the structured questionnaire may have assessed dependence.

**Решение:** =

---

### 202 · R3174

**Assessment of gonadotropins and testosterone hormone levels in regular Mitragyna speciosa (Korth.) users.**

2018 · Journal of ethnopharmacology · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.jep.2018.04.005

Ethnopharmacological relevance Mitragyna speciosa (Korth.) also known as kratom, is a native medicinal plant of Southeast Asia with opioid-like effects. Kratom tea/juice have been traditionally used as a folk remedy and for controlling opiate withdrawal in Malaysia. Long-term opioid use is associated with depletion in testosterone levels. Aim of the study Since kratom is reported to deform sperm morphology and reduce sperm motility, we aimed to clinically investigate the testosterone levels following long-term kratom tea/juice use in regular kratom users. Methods A total of 19 regular kratom users were recruited for this cross-sectional study. A full-blood test was conducted including determination of testosterone level, follicle stimulating hormone (FSH) and luteinizing hormone (LH) profile, as well as hematological and biochemical parameters of participants. Results We found long-term kratom tea/juice consumption with a daily mitragynine dose of 76.23-94.15 mg did not impair testosterone levels, or gonadotrophins, hematological and biochemical parameters in regular kratom users. Conclusion Regular kratom tea/juice consumption over prolonged periods (>2 years) was not associated with testosterone impairing effects in humans.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Clinical cross-sectional study of 19 regular kratom users; the abstract doesn't say whether dependence was assessed, but the sample table might report it.

**Решение:** =

---

### 203 · R3175

**Brain Magnetic Resonance Imaging of Regular Kratom (Mitragyna speciosa Korth.) Users:A preliminary study**

2018 · Monash University Research Portal (Monash University) · article, research article · en · https://core.ac.uk/download/700756412.pdf

Introduction: Mitragyna speciosa (Korth.) or kratom is a native medicinal plant of Southeast Asia. Commonly used by hard labours in harsh working environment, the ingestion of brewed kratom decoction is reported to produce dose-dependent stimulant and opioid-like effects. Kratom is also regularly consumed as a pain killer and as traditional cure for common maladies such as fever and cough. However, it remains unknown whether regular consumption of kratom decoction is associated with brain abnormalities in regular users in traditional settings. Methods: A total of 14 subjects (7 regular kratom users and 7 non-kratom users) voluntarily participated in this cross-sectional study. Face-to-face interviews were conducted with kratom users to determine history of kratom use and later these respondents underwent brain magnetic resonance imaging (MRI). Results: There were no significant differences (p&gt;0.05) in the intracranial volume (ICV), cortical volumes (frontal, parietal, temporal, occipital, or cingulate lobe), or subcortical volumes (striatum, hippocampus, or amygdala), as well as in the diffusion tensor imaging (DTI) metrics, fractional anisotropy (FA) and mean diffusivity (MD) between kratom users and the controls. Conclusion: This preliminary study showed long-term consumption of kratom decoction is not significantly associated with altered brain structures in regular kratom users in traditional settings. However, further study is needed to establish more data for kratom use and its effects.</p

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Small MRI study of regular kratom users; the abstract mentions interviews but doesn't say whether dependence was assessed.

**Решение:** =

---

### 204 · R3176

**Constipation prevalence and fatigue severity in regular kratom (Mitragyna speciosa Korth.) users**

2018 · Journal of Substance Use · article, journal article, journal-article · en · https://doi.org/10.1080/14659891.2018.1546340

ABSTRACT Background: User reports suggest that long-term kratom (Mitragyna speciosa Korth., Rubiaceae) consumption can be associated with negative effects like constipation and withdrawal symptoms such as fatigue. We aim to investigate constipation prevalence from kratom use and fatigue severity during kratom cessation in individuals who reported regular ingestion of kratom decoction. Methods: A total of 125 male regular-kratom users participated in this retrospective study. The Constipation Assessment Scale (CAS) was administered to assess effects during kratom use. The Fatigue Severity Scale (FSS) was used to assess fatigue during kratom withdrawal. Results: All respondents were males, the majority being Malays (97%, n = 121/125). Mean (SD) age was 34 years (11.2), and mean (SD) duration of kratom use was 8.5 years (5.5). A total of 57% had > 6 years kratom use history (n = 71/125), while 59% (n = 74/125) had used three or more glasses of kratom tea/juice daily. More than four-fifth (94%, n = 118/125) never experienced constipation; only 6% (n = 7/125) experienced constipation. As for fatigue, 86% (n = 108/125) reported fatigue during kratom cessation. Results from chi-square analysis showed that withdrawal from higher (three or more glasses daily) kratom intake was associated with severe fatigue during kratom cessation. Conclusions: Regular and higher (three or more glasses) consumption of kratom decoction did not appear to cause significant constipation problems, but users were prone to severe fatigue during kratom cessation.

**ИИ:** ? · обе модели · только абстиненция · Regular kratom users surveyed on constipation and withdrawal fatigue; abstract doesn't say if dependence was assessed, but the full text might.

**Решение:** =

---

### 205 · R3178

**Severity of Kratom (Mitragyna speciosa Korth.) Psychological Withdrawal Symptoms.**

2018 · Journal of psychoactive drugs · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1080/02791072.2018.1511879

ABSTRACT Kratom leaves (Mitragyna speciosa Korth.) are traditionally used in Southeast Asia for their medicinal value. Self-report studies suggest that cessation from chronic kratom tea consumption (freshly brewed kratom tea) was associated with unpleasant psychological symptoms. This study sought to assess the severity of anxiety and depression during kratom cessation. Regular kratom users (N = 150) were recruited from the northern state of Penang (Malaysia) for this retrospective study. The Beck Depression Inventory (BDI) and Beck Anxiety Inventory (BAI) scales were used to assess the severity of the symptoms of anxiety and depression. Most respondents (70%) experienced symptoms of mild anxiety, while 81% experienced symptoms of mild depression during kratom cessation. Those who consumed higher quantities of kratom tea daily (≥4 glasses) had higher odds of reporting longer duration of kratom use history (OR = 4.8, 95% CI 2.3 −10.1, p < 0.001), higher frequency of daily kratom use (≥4 times) (OR = 72, CI 9.5– 543.1, p < 0.001), and were more likely to experience moderate symptoms of depression (OR = 2.9, CI 1.1–7.3, p = 0.020) during kratom cessation than those who consumed between one and three glasses of kratom tea per day. Cessation from regular and long-term kratom tea consumption was not associated with symptoms of high anxiety or depression.

**ИИ:** ? · обе модели · только абстиненция · Regular kratom users in Malaysia; withdrawal anxiety and depression assessed, dependence measure not mentioned but may appear in sample description.

**Решение:** =

---

### 206 · R3179

**Severity of Pain and Sleep Problems during Kratom (Mitragyna speciosa Korth.) Cessation among Regular Kratom Users.**

2018 · Journal of psychoactive drugs · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1080/02791072.2018.1443234

Kratom (Mitragyna speciosa Korth.) is traditionally used in Southeast Asia for its medicinal value and psychoactive properties. Nonetheless, cessation from regular kratom use is reported to cause unpleasant dose-dependent withdrawal symptoms. This study aims to evaluate the severity of pain and sleep problems following the cessation of kratom tea/juice consumption among regular kratom users. A total of 170 regular users were recruited through snowball sampling for this cross-sectional study. The Brief Pain Inventory (BPI) and Pittsburgh Sleep Quality Index (PSQI) scales were administered to assess the severity of pain and sleep problems. Most participants experienced moderate pain intensity (84%) and moderate pain interference (70%) during kratom cessation; 46% experienced more sleep problems during kratom cessation. Individuals who consumed ≥4 glasses of kratom tea/juice (about 76-115 mg of mitragynine) daily had higher odds of reporting some pain interference (OR: 2.0; CI: 1.04-3.93: p < .028), and sleep problems during kratom cessation (OR: 2.0; CI: 1.08-3.68: p < .020), as compared to those who consumed 1-3 glasses of kratom tea/juice daily. However, the effects were still relatively mild. Cessation from regular kratom tea/juice consumption is not associated with prolonged pain and sleep problems, as compared to those reported for opioid analgesics.

**ИИ:** ? · обе модели · только абстиненция · Survey of 170 regular kratom users on pain and sleep during cessation; abstract does not say whether dependence was assessed.

**Решение:** =

---

### 207 · R3180

**Substance Use Disorder Related to Kratom (Mitragyna speciosa) Use in Malaysia**

2018 · Current Psychopharmacologye · article, other literature type, journal-article · en · https://doi.org/10.2174/2405461503666180420120649

Background: Kratom is a traditional medicinal herb with mild addictive properties. Nevertheless, current available data on substance use disorder related to kratom use is scarce. This study aims to clinically evaluate and identify factors that are associated with kratom use disorder among regular kratom tea/juice users in traditional settings in Malaysia. &lt;/P&gt;&lt;P&gt; Method: 150 regular kratom users were recruited through convenient sampling for this crosssectional study. They were interviewed with Mini International Neuropsychiatric Interview (M.I.N.I.) to diagnose substance use disorder related to kratom use, while the Ketum Dependence Scale (KDS) and Clinical Opioid Withdrawal Scale (COWS) were administered to evaluate kratom dependence and withdrawal severity. Results: All subjects were males with the majority being Malays (99%, n=148/150). More than half were single (n=84/150), had secondary education (91%, n=136/150), and were employed (93%, n=139/150). Almost all (99%) fulfilled the criteria for substance use disorder related to kratom use, 95% reported withdrawal symptoms on abstinence, 87% reported tolerance, and 93% craving for kratom. Results from Chi-square analysis indicated that higher quantity (&gt;3 glasses) of daily kratom tea/juice consumption was significantly associated with severe kratom dependence (OR: 2.1: 1.0-4.5: p&lt;.041) and moderate withdrawal (OR: 3.1: 1.5-6.3: p&lt;.002). Similarly, those who consumed &gt;3 glasses of brewed kratom tea daily had higher odds of reporting longer kratom use history (&gt;7 years) (OR: 4.4: 2.2-8.8: p&lt;.001) and higher frequency of daily kratom use (&gt;5 times) (p&lt;.001), compared to those who consumed less than three glasses of kratom daily. Conclusion: Our findings indicated that regular and chronic (&gt;3 glasses daily) kratom tea/juice consumption was associated with kratom use disorder, severe kratom dependence and moderate withdrawal.</jats:sec

**ИИ:** + · обе модели · употребляющие + мера зависимости · 150 regular kratom users in Malaysia were assessed with the MINI for kratom use disorder and with the KDS; 99% met SUD criteria.

**Решение:** =

---

### 208 · R3201

**The prevalence and associated factors of new psychoactive substance use: A 2016 Thailand national household survey**

2018 · Addictive Behaviors Reports · article · https://doi.org/10.1016/j.abrep.2017.11.001

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Thai national household survey on new psychoactive substances, likely mostly kratom; no abstract, so unclear whether dependence was measured.

**Решение:** =

---

### 209 · R3212

**新興影響精神物質－－卡痛（Kratom）對人體之生理危害**

2018 · article · ja

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: Chinese title, 'Emerging psychoactive substance kratom: physiological harms to the human body', reads like a narrative review; no abstract or sign of primary data.); Sonnet ? (нет аннотации: Chinese title on kratom's physiological harms; no abstract. Likely a review, but study type cannot be confirmed.)

**Решение:** - обзор на китайском языке о физиологическом вреде кратома

---

### 210 · R3242

**Prevalence and psycho-social determinants of Kratom (Mitragyna speciosa) juice cocktail consumption among youth in Surat Thani Province, Thailand**

2017 · Journal of Substance Use · article, journal-article · en · https://doi.org/10.1080/14659891.2017.1378735

The objective of this study was to explore the prevalence of Kratom juice cocktail (KJC) consumption among youth and psychosocial determinants using a cross-sectional community-based study design. A total of 468 adolescents in Surat Thani Province were selected using simple random sampling. Self-administered questionnaires were used, and multiple logistic regression was used to identify factors related to the KJC consumption. The findings suggest that the prevalence of KJC use was high (31.4%), while self-efficacy (AOR = 12.95, 95% CI = 1.64–102.35), attitude toward KJC (AOR = 30.14, 95% CI = 6.91–131.53), self-regulation (AOR = 23.80, 95% CI = 3.11–182.28), and existence of peers drinking KJC (AOR = 32.46, 95% CI = 4.86–216.58) were strongly associated with KJC drinking behavior of youth. Youth who drink alcohol (AOR = 5.23, 95% CI = 1.07–25.63), who are employed and have an income (AOR = 4.02, 95% CI = 1.07–15.13) were more likely to drink KJC. Increasing self-efficacy and developing better self-regulation skills to resist the urge to drink KJC in high-risk situations, formulating correct attitudes against drug use, and increasing surveillance of illegal drug use may drive down harmful drug use among youth. In addition, as friends influence KJC consumption, peer education can be used as a KJC consumption prevention strategy.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Youth survey of kratom cocktail use prevalence and determinants; unclear whether dependence was assessed among the users.

**Решение:** =

---

### 211 · R3265

**Patterns of Kratom use and health impact in the US-Results from an online survey.**

2017 · Drug and alcohol dependence · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.drugalcdep.2017.03.007

Background Kratom preparations have raised concerns of public health and safety in the US. Investigation into the demographics, perceived beneficial and detrimental effects of Kratom as well as common doses and purposes of its use are important to properly evaluate its potential health impact. Methods An anonymous cross-sectional online survey was conducted in October 2016 of 10,000 current Kratom users through available social media and online resources from the American Kratom Association. A total of 8049 respondents completed the survey. Results Kratom is primarily used by a middle-aged (31-50 years), middle-income ($35,000 and above) population for purposes of self-treating pain (68%) and emotional or mental conditions (66%). Kratom preparations present with a dose-dependent effect with negative effects, which were primarily gastrointestinal related including nausea and constipation, mainly presenting at high (5g or more/dose) and more frequent (22 or more doses/week) dosing. Conclusions Kratom shows a dose-dependent opioid-like effect providing self-reported perceived beneficial effects in alleviating pain and relieving mood disorders. Kratom was primarily used for self-treatment of pain, mood disorders, and withdrawal symptoms associated with prescription opioid use.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Large online survey of current kratom users; abstract doesn't say whether dependence or use disorder was assessed.

**Решение:** =

---

### 212 · R3267

**Clinical Toxicology**

2017 · https://doi.org/10.1016/b978-0-12-813213-5.00016-x

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · The title is only a journal name and there is no abstract. It may be a conference-abstract supplement that includes kratom data.

**Решение:** =

---

### 213 · R3285

**The association between chronic severe pain and neuroticism personality trait among patients on methadone maintenance therapy in Alor Star, Kedah**

2017 · review · https://core.ac.uk/download/199245605.pdf

Pain is very commonly reported among previous heroin users on methadone maintenance therapy (MMT) with the prevalence of chronic severe pain (CSP) of 37-48.2% being reported. The symptom causes distress and disability, and adversely affect patients’ quality of life, addiction treatment outcome and exacerbates their ambivalence towards MMT. In general, neuroticism personality trait has been shown by various studies to be associated with CSP, but similar association has yet been explored in MMT patients.Current study aim to assess the prevalence of CSP among patients on MMT, and to examine whether neuroticism is significantly associated with CSP in this group of patients.This is a cross-sectional study, utilizing validated Malay versions of Brief Pain Inventory (BPI) for pain measurement, Big Five Inventory (BFI) to measure neuroticism, Beck’s Depression Inventory (BDI) for measurement of depressive symptoms, and Beck’s Anxiety Inventory (BAI) for measurement of anxiety symptoms. All rating instruments mentioned are self-rated instruments. Sample size is determined using proper sample size calculation, and universal sampling method is applied for subject recruitment. Samples were collected from two MMT centres in Alor Star. By using Multiple Logistic Regression analyses, Neuroticism score (p<0.001), BAI score (p<0.012) and regular use of over-the-counter analgesics (p<0.016) were found to be statistically significant in association with CSP, with adjusted Odds Ratio of 1.60 (95% CI 1.27, 2.12), 1.44 (95% CI 1.08, 1.93), and 3.56 (95% CI 1.27, 10.01), respectively. Multicollinearity was not detected. However, interaction was noted between neuroticism score and BAI score (p=0.028). Hence, the interaction was included into the analysis of fitness of final model. The fitness of this final model was confirmed using Hosmer-Lemeshow test (p=0.282), classification table (overall correctly classified percentage= 83.4%), and area under the receiver operating characteristic (ROC) curve test (87.9%). It was interesting to note that the prevalent of daily usage of kratom product was over 40% in the sample. Neuroticism score is positively associated with CSP among patients on MMT, whereby with every one point increment in neuroticism score, there is 60% higher odds of having CSP. Though it is tempting to conclude that high neuroticism score predict CSP development among patient on MMT, the author recognizes the limitations of current cross-sectional study design in establishing the nature of the association. Other significant associative factors are BAI score and regular use of over-the-counter analgesics. For every one point increment in BAI score, there is 44% higher odds of patient having CSP; and if an MMT patient use OTC analgesics for at least 3 times a week, the odds of having CSP is 3.6 times compared to those not using OTC regularly. The results suggest that, firstly, addressing anxiety in patient might help to improve CSP, and unaddressed anxiety in patient with chronic pain might in fact adversely affect the efficacy of chronic pain intervention and MMT outcome. Besides, the strong association between OTC analgesics usage and CSP suggested that when CSP among this group of patients was not adequately addressed, patient resorted to OTC analgesics to relieve their pain. OTC use as a way of self-medication was reported by studies to be common, and the practice actually exposes the patients to adverse drug reactions, which is avoidable. In the case of MMT, drug-to-drug interaction of methadone with OTC analgesics could be fatal. Over 40% of the study subjects reported use of kratom product daily. Though its association with CSP was not statistically significant, its implication to our MMT patients cannot be ignored, as kratom has been increasingly reported locally, as well as globally, as an emerging illicit substance with high abuse potential

**ИИ:** разошлись — Opus -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: MMT pain study; instruments listed are BPI, BFI, BDI and BAI. Daily kratom use was reported, but no kratom dependence measure was mentioned.); Sonnet ? (неясно, оценивали ли зависимость: Cross-sectional study of methadone patients where over 40% used kratom daily; the abstract doesn't say whether kratom dependence was assessed, so check the full text.)

**Решение:** - пациенты метадоновой программы: фокус на боли и невротизме, нет меры зависимости от кратома

---

### 214 · R3299

**Outcome of Cure and Care Community Center (CCSC): A Community Based Treatment (CBTx) Program in Malaysia**

2017 · MOJ Addiction Medicine & Therapy · article · en · https://doi.org/10.15406/mojamt.2017.03.00051

In an effort to depart from the Compulsory Center for Drug Users (CCDU), Malaysia has initiated the Cure and Care Service Center program (CCSC) to provide a community based treatment program (CBTx) engaging a multitude of services related to drug and substance abuse, rehabilitation to drug users, dependents and recovering persons.The objective of this study is to identify the outcome of the CCSC service.The population of this study is the clients of CCSC during the span of its operation (2011-2012).A total of 10 CCSCs were randomly chosen with reference to its location in the 4 zones (North, South, East & Central) of Peninsular Malaysia.A total of 232 clients responded to the outcome study.The study found that the outcome of drug rehabilitation program at CCSC is generally positive.The main outcome is that clients' involvement in criminal activities has reduced significantly after they have completed their program at CCSC.The consumption of ketum leaves extracts, alcohol, drugs, and even drug injecting behavior have also reduced significantly.Almost 20% of the clients gained employment after their discharge from the program.Also, about a third of the clients have changed their lifestyle; they took care of their health, engaged in physical activities and exercises; played sports; took their medicine and maintained their leisure time.Some are involved in religious activities, and almost half of the clients have been seen to have made that change.Around 20% has started to renew relationships with their parents, siblings, and other family members.A smaller number got involved in intimate relationships and marriage.Many clients managed to obtain more permanent jobs, engaged in recreational, sports activities, and enhanced relationship with family.Overall the outcome of the CCSC program was found to be successful.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Outcome study of Malaysian drug treatment clients that measured ketum use; unclear whether kratom dependence (e.g., ASSIST) was assessed.

**Решение:** =

---

### 215 · R3300

**Outcome of cure and care community center (CCSC): a community based treatment (CBTX) program in Malaysia**

2017 · https://doi.org/10.15406/mojamt.2017.3.00051

In an effort to depart from the Compulsory Center for Drug Users (CCDU), Malaysia has initiated the Cure and Care Service Center program (CCSC) to provide a community based treatment program (CBTx) engaging a multitude of services related to drug and substance abuse, rehabilitation to drug users, dependents and recovering persons. The objective of this study is to identify the outcome of the CCSC service. The population of this study is the clients of CCSC during the span of its operation (2011-2012). A total of 10 CCSCs were randomly chosen with reference to its location in the 4 zones (North, South, East & Central) of Peninsular Malaysia. A total of 232 clients responded to the outcome study. The study found that the outcome of drug rehabilitation program at CCSC is generally positive. The main outcome is that clients’ involvement in criminal activities has reduced significantly after they have completed their program at CCSC. The consumption of ketum leaves extracts, alcohol, drugs, and even drug injecting behavior have also reduced significantly. Almost 20% of the clients gained employment after their discharge from the program. Also, about a third of the clients have changed their lifestyle; they took care of their health, engaged in physical activities and exercises; played sports; took their medicine and maintained their leisure time. Some are involved in religious activities, and almost half of the clients have been seen to have made that change. Around 20% has started to renew relationships with their parents, siblings, and other family members. A smaller number got involved in intimate relationships and marriage. Many clients managed to obtain more permanent jobs, engaged in recreational, sports activities, and enhanced relationship with family. Overall the outcome of the CCSC program was found to be successful.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Outcome study of Malaysian drug treatment clients reports ketum consumption; unclear whether ketum dependence was assessed among those using it.

**Решение:** =

---

### 216 · R3328

**Prevalence and motivations for kratom use in a sample of substance users enrolled in a residential treatment program.**

2017 · Drug and alcohol dependence · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.drugalcdep.2017.08.034

Kratom use in the West has increased recently, yet the prevalence and motives for use among individuals with a history of substance use disorder (SUD) have not been fully examined. Kratom has been documented as a means of treating chronic pain, mitigating drug dependence, and easing withdrawal symptoms, yet it is unclear if substance users are utilizing kratom as a self-medication. Abuse liability, side effects, and overall appeal of kratom remain uncertain. In April 2017, an anonymous survey regarding kratom use and motivations was completed by clients enrolled in a 12-Step-oriented residential program. 500 respondents with a self-reported history of SUD completed the survey. 20.8% of respondents endorsed lifetime kratom use and 10.2% reported past-12-month use. Kratom-users were younger (=32.1 vs. 35.9, p<0.001) and were more versatile substance users. A majority (68.9%) of kratom-users reported having used the drug as a means of reducing or abstaining from non-prescription opioids (NPO) and/or heroin, and 64.1% reported using kratom as a substitute for NPO/heroin. 18.4% of kratom-users reported using the drug due to a disability or chronic pain. One-third of kratom-users stated that kratom was a helpful substance and that they would try it again. However, kratom was not preferred and was indicated as having less appeal than NPO, heroin, amphetamines, and Suboxone. Among substance users, kratom use may be initiated for a variety of reasons, including as a novel form of harm-reduction or drug substitution, particularly in the context of dependence and withdrawal from other substances.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of residential SUD patients on kratom use and motives; abstract doesn't say whether kratom dependence was assessed.

**Решение:** =

---

### 217 · R3330

**ประมาณการจำนวนผู้ใช้ยาเสพติดในพื้นที่สามจังหวัดชายแดนใต้ ด้วยวิธี Multiplier และสุ่มตัวอย่างแบบ Respondent Driven Sampling**

2017 · Prince of Songkla University · thesis

Master of Science Program in Epidemiology, 2017Background: The Deep-south provinces of Thailand, the border area where the population is majority Malay ethnic, have faced armed-conflicts for the past decade and are a major route of drug trafficking. Several studies reported concerns about drug problems among people in the area but the prevalence of drug users has not been studied. ‘Kratom’ is an alkaloid and the traditional plant originates from South-East Asia. Historically it has been used for its herbal qualities. Presently it is used by adolescents for recreational purposes, and has been reported as the most popular substance in the region for the past decade. Objectives: This study aimed to estimate the size of drug using population in the Deep-south provinces of Thailand. The second objective aimed to compare factors associated with kratom use with and without other substances among kratom users. Design: A cross-sectional survey was conducted in 2016. Males age>18 years who had ever used any drugs including heroin, methamphetamine, cannabis and kratom in past six months were recruited. A respondent-driven sampling method was used to reach the target population. We used the multiplier method to estimate the size of the drug using population. For objective two, we excluded participants who were not currently Kratom users from the analysis. Result: The estimated number of drug users in 2016 in our study setting was 13,545 thus the prevalence of drug users among male population in the same age group was 50.2 per 1,000 population, twice as high as the national ix prevalence. Most drug users lived in Pattani (60.6%) followed by Narathiwat and Yala provinces. The most currently used drug among current drug users was kratom (85.2%) followed by methamphetamine (57.7%) and cannabis (29.2%). More than half (60.6%) of current users consumed more than one type of illicit drugs. Kratom and methamphetamines were the most common combination (25.6%). Use of kratom alone was reported by 38% of users; while kratom co-use use was reported by 62%. The most common combination was kratom and methamphetamines (54%). Being a heavy kratom user increased the odds of heavy methamphetamine use (OR= 4.19 95%CI=2.10-8.33). Five factors were statistically significantly associated with varying patterns of kratom use: living in Pattani province, use with peers, report of having been in treatment during last six months, having history of treatment from an ‘Other Health’ sector and having been in treatment for more than 1 episode, with adjusted ORs of 0.52, 0.39, 2.73, 2.25 and 3.36 respectively. The mean ASSIST score was highest for kratom (22.8) followed by methamphetamine (10.0). Conclusion: Kratom was found the most commonly used substance. The high prevalence of drug users should be considered by stakeholders. The results of this study are useful for policy makers to develop intervention to minimize and control kratom use. Polydrug use among kratom users was demonstrated to be a serious problem in southern Thailand. The combination of kratom and methamphetamine should be considered high risk

**ИИ:** + · обе модели · другая выборка, есть употребляющие и мера зависимости · RDS survey of drug users in Deep South Thailand, most of whom use kratom; ASSIST kratom scores reported, so risk-level counts are likely.

**Решение:** =

---

### 218 · R3348

**Kratomaddictionbehaviorofindividuals, groupsworkingin Krabi (พฤติกรรมการเสพใบกระท่อมของประชาชนกลุ่มวัยทำงาน ในจังหวัดกระบี่)**

2017 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Thai study of kratom use behaviour among working-age adults in Krabi; no abstract, likely a survey that may have assessed dependence.

**Решение:** =

---

### 219 · R3349

**ผลกระทบด้านร่างกาย จิตใจและพฤติกรรมของผู้ใช้ใบกระท่อมที่เข้ารับการบำบัดรักษาในสถานบำบัดรักษาสารเสพติด**

2017 · Chula Digiverse · doctoral thesis, dissertation · th · https://doi.org/10.58837/chula.the.2017.1560

ที่มาและความสำคัญ : กระท่อม (Mitragyna speciosa Korth.) ไม่เพียงแต่ใช้เป็นยารักษาโรคในการรักษาพื้นบ้านของไทย แต่ยังมีการนำมาใช้เป็นสารเสพติดมาเป็นระยะเวลานาน อย่างไรก็ตามกระท่อมถือเป็นสารเสพติดผิดกฎหมายในประเทศไทย วัตถุประสงค์ : เพื่อศึกษาผลกระทบด้านร่างกาย จิตใจและพฤติกรรมของผู้ใช้ใบกระท่อม เพื่อศึกษารูปแบบวิธีการใช้และปัจจัยที่สัมพันธ์กับรูปแบบการใช้ใบกระท่อม เพื่อศึกษาความผิดปกติด้านการใช้ใบกระท่อม วิธีการศึกษา : ผู้ใช้ใบกระท่อมที่มารับบริการที่สถาบันบำบัดรักษาและฟื้นฟูผู้ติดสารเสพติดแห่งชาติบรมราชชนนีอายุตั้งแต่ 18 ปีขึ้นไป เป็นผู้ที่เคยใช้พืชกระท่อมเป็นส่วนหนึ่งของสารเสพติดในช่วงชีวิตใดก็ได้หรือใน 1 เดือนที่ผ่านมา รวมทั้งสิ้น 106 ราย เครื่องมือที่ใช้เก็บรวบรวมข้อมูลคือ แบบสอบถามข้อมูลจำนวน 6 แบบสอบถาม สถิติที่ใช้ในการวิเคราะห์ข้อมูล ได้แก่ ร้อยละ ค่าเฉลี่ย ส่วนเบี่ยงเบนมาตรฐาน สถิติ Independent Samples t-Test, Chi-square และ Pearson's correlation ผลการศึกษา : พบผู้ใช้กระท่อมในรูปแบบน้ำต้มใบกระท่อมสี่คูณร้อยจำนวนเท่ากับร้อยละ 55.6 ประเภทเคี้ยวใบกระท่อม ร้อยละ 41.7 ผู้ใช้กระท่อมส่วนใหญ่ใช้สารเสพติดอื่น ๆ ร่วมด้วย ถึงแม้ว่าผู้ใช้กระท่อมแบบต้มใช้สารเสพติดอื่นร่วมมากกว่าผู้ใช้กระท่อมแบบเคี้ยวอย่างมีนัยสำคัญทางสถิติ (p = 0.001) แต่ผู้ใช้แบบเคี้ยวจะมีอาการปวดศีรษะ อาการข้ออักเสบ คลื่นไส้ ท้องผูก หรืออุจจาระแข็งมากกว่าการใช้แบบอื่นๆอย่างมีนัยสำคัญ สรุปผลการศึกษา : การศึกษานี้พบผู้ใช้กระท่อมส่วนใหญ่ใช้สารเสพติดอื่น ๆ ร่วม และพบอาการข้างเคียงจากการใช้กระท่อมทั้งแบบเคี้ยวและแบบน้ำต้มสี่คูณร้อย

**ИИ:** разошлись — Opus ? (другое: Drug-treatment patients with lifetime kratom use; kratom use disorder assessed, but unclear whether they were treated for kratom itself.); Sonnet + (употребляющие + мера зависимости: Thai thesis of 106 kratom users at a national drug treatment institute; an explicit aim is studying kratom use disorder, so a count of disorder is likely.)

**Решение:** - выборка набрана по обращению за лечением кратома

---

### 220 · R3369

**Kratom use, abuse and addiction**

2016 · article · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. The title sounds like a review, but it could also report original data on kratom addiction.

**Решение:** =

---

### 221 · R3375

**Novel Psychoactive Substances: Kratom**

2016 · article · eng · https://hdl.handle.net/11572/371770

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title sounds like a narrative overview, but a primary study can't be ruled out without the full text.

**Решение:** =

---

### 222 · R3440

**Factor Analytical Investigation of Krathom (Mitragyna speciosa Korth.) Withdrawal Syndrome in Thailand.**

2016 · Journal of psychoactive drugs · article, journal article, journalarticle · eng · https://doi.org/10.1080/02791072.2016.1156791

Krathom (Mitragyna speciosa Korth.) is an addictive and illicit substance used in Thailand and other Southeast Asian countries. It has become the most commonly used substance among villagers. The study aimed to explore the factor structure of the krathom withdrawal syndrome based on the findings of an earlier qualitative study. The current study was divided into two stages. Cross-sectional data collections were employed in both phases. The samples comprised, respectively, 196 and 330 krathom users aged over 25 years. The characteristics of krathom withdrawal symptoms and signs were identified and the factor structure examined using exploratory factor analysis (EFA). Confirmatory Factor Analysis (CFA) was used to examine the construct validity and multivariate linear regression was used to identify factors predicting the intensity of krathom withdrawal symptoms. The final scale comprised 20 items with four factors: craving-fatigue syndrome; musculoskeletal system and insomnia; mood symptoms; and autonomic nervous system/physical sickness. Symptoms and signs of krathom withdrawal similar to those of the withdrawal syndrome of opioid substances appear to be present in regular krathom users. The krathom withdrawal intensity is predicted by duration of krathom use, frequency, and daily amount of krathom use.

**ИИ:** ? · обе модели · только абстиненция · Survey of krathom users developing a withdrawal scale; dependence measures possibly reported in the full text but not mentioned in the abstract.

**Решение:** =

---

### 223 · R3442

**Relationship between family attachment and resilience among secondary school students abusing mitragyna speciosa (Ketum, Kratom or Kratum)**

2016 · Man in India · article

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; quantitative study of students using kratom may have assessed dependence; full text needed.

**Решение:** =

---

### 224 · R3502

**Kajian penyalahgunaan daun ketum dalam kalangan pelajar sekolah menengah di negeri Kedah dan Perlis**

2015 · Universiti Utara Malaysia Institutional Repository (Universiti Utara Malaysia) · book, review · ms · https://core.ac.uk/download/83552850.pdf

Pokok Ketum, juga dikenali sebagai Pokok Biak (bahasa Inggeris: Kratom), ialah sejenis tumbuhan daripada famili Rubiaceae yang banyak terdapat di Afrika, di utara dan tengah Semenanjung Malaysia serta di selatan Thailand. Di Thailand, pokok ini dipanggil Kakuam, Ithang atau Thom, di Amerika Syarikat pula sebagai Kratom. Nama botaninya Mitragyna speciosa korth (Karl & Colin, 1988). Daun Ketum telah lama menjadi bahan perubatan tradisional sebagai minuman pemulih tenaga bagi wanita yang baru lepas bersalin. Daun ini direbus dan airnya diminum sebagai pemulih tenaga, juga bagi rawatan mengeluarkan angin dalam badan dan bagi merawat sakit belakang.Bagaimanapun air rebusan daun ketum telah disalahgunakan dan mula dijual secara meluas kepada pengguna biasa. Penagihan air ketum juga telah menular di kalangan pelajar sekolah di Kedah dan Perlis di mana gejala ketagihan air ketum berleluasa hingga kini (Noorazura, 2014).Bengkel pemurnian resolusi yang dijalankan oleh AADK bersama-sama agensi-agensi terlibat peringkat negeri Kedah menunjukkan terdapat 16 resolusi yang telah dicapai dalam pemantapan untuk mengatasi masalah penagihan air ketum di mana ianya merangkumi 3 sub program (pencegahan, rawatan, pemulihan serta penguatkuasaan).Salah satu sub program yang ditekankan adalah pencegahan yang merangkumi pendedahan maklumat yang tepat mengenai penyalahgunaan air ketum diberikan kepada semua kaunselor sekolah di negeri Kedah.Hasil daripada resolusi tentang perlunya langkah-langkah pencegahan dilakukan bermula dari peringkat sekolah lagi maka kajian ini telah dirangka sebagai peringkat permulaan untuk mengenal pasti tentang pengetahuan, kefahaman dan kesedaran pelajar-pelajar sekolah menengah tentang bahaya penyalahgunaan air daun ketum dalam kalangan masyarakat pada hari ini.Semua pandangan yang diberikan melalui soal selidik ini akan mantapkan dengan temu bual berstruktur dengan beberapa kumpulan guru, JKK kampung serta ahli masyarakat setempat dan ibu bapa dalam mengesahkan jawapan yang diberikan oleh pelajar-pelajar sekolah menengah bagi daerah yang dijadikan sampel kajian. Data yang didapati ini akan menjadi bukti tentang tahap pengetahuan, kefahaman dan kesedaran penyalahgunaan daun ketum dalam kalangan pelajar sekolah menengah di negeri Kedah dan Perlis.

**ИИ:** разошлись — Opus -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: Student survey on knowledge, understanding and awareness of ketum misuse dangers; no kratom dependence or use-disorder measure is indicated.); Sonnet ? (неясно, оценивали ли зависимость: Questionnaire survey of Malaysian secondary students on ketum knowledge and awareness; unclear whether use or dependence among users was measured, likely knowledge-focused.)

**Решение:** - опрос школьников в Кедахе: знания и мотивы, без клинической меры зависимости

---

### 225 · R3506

**Reasons to Use Red Vein Kratom Powder**

2015

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -7 (другое — напишите почему: The title reads like a promotional or marketing web article rather than a study of people. There is no abstract or venue.); Sonnet ? (нет аннотации: No abstract; title suggests motives for kratom use, possibly a promotional web article rather than a study. Cannot tell if dependence was assessed.)

**Решение:** - рекламный / промо-материал о красном кратоме

---

### 226 · R3541

**Social Functioning of Kratom (Mitragyna speciosa) Users in Malaysia.**

2015 · Journal of psychoactive drugs · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1080/02791072.2015.1012610

Kratom (Mitragyna speciosa) is an indigenous plant known for its traditional medicinal use, and for its addiction potential, in Southeast Asia. In recent years, kratom and its major alkaloid, mitragynine, spread worldwide with largely unknown effects on behavior and mental health. Recent studies show that kratom use can lead to dependence and that mitragynine works as an addictive drug in animal studies. Nevertheless, kratom preparations were also suggested as a less harmful substitute in opiate withdrawal. Potential side-effects of prolonged kratom use, however, are currently unclear. The aim of this study was to investigate the social functioning of regular kratom users in Malaysia. A cross-sectional survey was carried out in three northern states of Peninsular Malaysia investigating 293 regular kratom consumers using the Addiction Severity Index in a snowball sampling technique. Findings showed that regular kratom users do not experience major impairments in their social functioning, despite being dependent on kratom for prolonged periods. Our findings suggest that chronic kratom administration does not significantly impair social functioning of users in a natural context in Malaysia.

**ИИ:** + · обе модели · употребляющие + мера зависимости · Survey of 293 regular kratom users in Malaysia; the abstract says users were dependent, so it likely reports dependence status.

**Решение:** =

---

### 227 · R3549

**Prevalence, patterns, associated factors and severity of substance use among psychotic patients in southern Thailand**

2015 · Asian Journal of Psychiatry · article · https://doi.org/10.1016/j.ajp.2014.11.006

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. Substance use severity among psychotic patients in southern Thailand likely covers kratom and may use ASSIST or dependence criteria.

**Решение:** =

---

### 228 · R3551

**Pharmacokinetics of mitragynine in man.**

2015 · Drug design, development and therapy · article, journal article, journalarticle · eng · https://doi.org/10.2147/dddt.s79658

Satariya Trakulsrichai,1,2 Korbtham Sathirakul,3,4 Saranya Auparakkitanon,5 Jatupon Krongvorakul,5 Jetjamnong Sueajai,5 Nantida Noumjad,5 Chonlaphat Sukasem,5 Winai Wananukul2,6 1Department of Emergency Medicine, Faculty of Medicine Ramathibodi Hospital, 2Ramathibodi Poison Center, Faculty of Medicine Ramathibodi Hospital, 3Department of Pharmacy, Faculty of Pharmacy, Mahidol University, Bangkok, Thailand; 4Center for Drug Research Discovery and Development, Thammasat Univerisity, Prathumthani, Thailand; 5Department of Pathology, Faculty of Medicine Ramathibodi Hospital, 6Department of Medicine, Faculty of Medicine Ramathibodi Hospital, Mahidol University, Bangkok, Thailand Background: Kratom, known botanically as Mitragyna speciosa (Korth.), is an indigenous tree in Southeast Asia. Kratom is currently easily available worldwide via special shops and the Internet to use as a drug of abuse, opioid alternative, or pain killer. So far, the pharmacokinetics of this plant has been studied only in animals, and there is no such study in humans. The major abundant active alkaloid in Kratom, mitragynine, is one of the promising new chemical substances to be developed as a new drug. The aim of this study was to examine the pharmacokinetics of mitragynine and assess the linearity in pharmacokinetics in chronic users.Methods: Since Kratom is illegal in Thailand, studies in healthy subjects would be unethical. We therefore conducted a prospective study by enrolling ten chronic, regular, healthy users. We adjusted the steady state in each subject by giving a known amount of Kratom tea for 7 days before commencement of the experiment. We admitted and gave different oral doses to subjects to confirm linearity in pharmacokinetics. The mitragynine blood concentrations at 17 times points and the urine concentrations during the 24-hour period were collected and measured by liquid chromatography-tandem mass spectrometry method. Results: Ten male subjects completed the study without adverse reactions. The median duration of abuse was 1.75 years. We analyzed one subject separately due to the abnormal behavior of blood concentration. From data of nine subjects, the pharmacokinetic parameters established were time to reach the maximum plasma concentration (0.83&plusmn;0.35 hour), terminal half-life (23.24&plusmn;16.07 hours), and the apparent volume of distribution (38.04&plusmn;24.32 L/kg). The urine excretion of unchanged form was 0.14%. The pharmacokinetics were observed to be oral two-compartment model. Conclusion: This was the first pharmacokinetic study in humans, which demonstrated linearity and was consistent with the oral two-compartment model with a terminal half-life of about 1 day. The pharmacokinetic linearity and parameters reported are necessary pharmacological information of Kratom, and there is a possibility for it to be developed medically as a pain killer or better opioid substitute in the future. Keywords: kratom, human, pharmacokinetic

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Pharmacokinetic study of ten chronic regular kratom users; the abstract doesn't say whether dependence was assessed.

**Решение:** =

---

### 229 · R3595

**Suicide risk among Thai illicit drug users with and without mental/alcohol use disorders.**

2014 · Neuropsychiatric disease and treatment · article, journal article, journalarticle · eng · https://doi.org/10.2147/ndt.s56441

BACKGROUND: It is not yet known if the increased risk of suicide in substance abusers is caused by the causal and/or coexisting relationship between substance use and psychiatric disorders. This study was designed to estimate the suicide risk among individuals with illicit drug use alone, illicit drug users with mental disorders, and illicit drug users with alcohol use disorders. METHODS: Subjects were participants of the 2008 Thai National Mental Health Survey. They were asked for their illicit drug use in the past year. The Mini International Neuropsychiatric Interview (MINI), current suicidality (1 month prior to assessment), mood episodes, anxiety disorders, psychotic disorders, and alcohol use disorders were used for assessing mental/alcohol use disorders. A score of 1 or more for the MINI-Suicidality module was defined as the presence of suicide risk. RESULTS: Of the total 17,140 respondents, 537 currently used illicit drugs, while 1,194 respondents had a suicide risk. Common illicit drugs were kratom (59%) and (meth)amphetamine (24%). Compared with 16,603 Thais without illicit drug use, the illicit drug users with or without mental/alcohol use disorders (n=537) had an increased risk of suicide (adjusted odds ratio [OR], 95% confidence interval [CI] =2.09, 1.55-2.81). While those who used illicit drugs alone (no mental/alcohol use disorder) (n=348) had no increased risk of suicide (adjusted OR, 95% CI =1.04, 0.66-1.65), the illicit drug users with mental or alcohol use disorders (n=27 and n=162, respectively) had significantly increased risk of suicide (adjusted ORs, 95% CIs =14.06, 6.50-30.3 and 3.14, 1.98-4.99, respectively). CONCLUSION: A key limitation of this study was the combined suicidal behaviors as a suicidality risk. Mental or alcohol use disorders found in this population actually increased the suicide risk. These findings support the coexisting relationship that mental and alcohol use disorders play a vital role in increasing the suicide risk in illicit drug users.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · National survey used the MINI and kratom was the most common drug, but only alcohol use disorders are mentioned; kratom dependence may not have been assessed.

**Решение:** =

---

### 230 · R3598

**Significance of Using Kratom Leaves in Heroine Withdrawals**

2014

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; might be a survey of heroin users who use kratom that assessed kratom dependence, or might be a review.

**Решение:** =

---

### 231 · R3609

**Positive outcomes of Cure and Care Community Centres (CCSC): a community based treatment programme in Malaysia**

2014 · International Journal of Prevention and Treatment of Substance Use Disorders · article, other literature type · und · https://doi.org/10.4038/ijptsud.v1i2.7700

In an effort to depart from the Compulsory Centre for Drug Users (CCDU), Malaysia has initiated the Cure and Care Service Centre (CCSC) programme to provide a community based treatment programme that provides a multitude of services related to drug and substance abuse rehabilitation to drug users, dependents and recovering persons. The objective of this study is to identify the outcomes of the CCSC service. The population of this study is the clients of CCSCs during the period of its operation (2011-2012). Ten CCSCs were randomly chosen with reference to their location in the four zones (North, South, East and Central) in the Malaysia Peninsular. A total of 232 clients responded to the study. The study found that the outcome of drug rehabilitation programmes at CCSCs was generally positive. The main out come was that clients’ involvement in criminal activities had reduced significantly after they had completed their CCSC programmes. The consumption of ketum leaves extracts, alcohol, drugs and even drug injecting behaviour had also reduced significantly. Almost 20% of the clients gained employment after being discharged from the programme. Also about one third of the clients have changed their lifestyles: they took care of their health, engaged in physical activities and exercises; played sports; took their medicine and relaxed sufficiently. Some were involved in religious activities, and almost half were seen to have made that change. Around 20% has started to renew relationships with their parents, siblings and other family members. A smaller number got involved in intimate relationships and even marriage. Many clients managed to obtain more permanent jobs, engaged in recreational sports activities and enhanced relationships with their families. Overall the outcome of the CCSC programme was successful. DOI: http://dx.doi.org/10.4038/ijptsud.v1i2.7700 International Journal of Prevention and Treatment of Substance Use Disorders 2014;1(2):71-83

**ИИ:** разошлись — Opus ? (неясно, оценивали ли зависимость: Malaysian drug-treatment clients whose ketum use was measured; the abstract doesn't say whether kratom dependence was assessed.); Sonnet -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: Outcome evaluation of Malaysian drug treatment centres. Ketum use is only a reduced-consumption outcome, with no kratom dependence or use disorder measure apparent.)

**Решение:** ? опрос клиентов реабилитационных центров Cure and Care в Малайзии

---

### 232 · R3634

**OR03-1 * EFFECT OF KRATHOM (MITRAGYNA SPECIOSA KORTH.) USE AMONG TRADITIONAL USERS IN SOUTHERN THAILAND**

2014 · Alcohol and Alcoholism · article, review, conference-abstract · en · https://doi.org/10.1093/alcalc/agu053.11

Background. Krathom (mitragyna speciosa, Korth.), a plant based narcotic, has been controlled for more than 70 years in Thailand and evidence regarding its effects on mental and physical health is scarce. This study aimed to examine the effect of krathom use among krathom users. Methods. Two cross-sectional surveys were conducted in 2011 and in 2012 among 523 and 595 male villagers aged over 25 years who were regular users, occasional users, ex-users, and non-users of krathom. A follow-up interview was done among 200 of the 523 subjects and a medical record review among 214 in 2013. Results. Health problems in the past year commonly reported by 526 krathom users at baseline were rain panic (35%), lost appetite (24%), constipation (18%) and gastritis (2%). At follow-up five users had died (two with cancer and others cause unknown), two ex-heavy users had stomach mass of accumulated krathom fibre and four had severe chronic illnesses, i.e. renal failure, paraplegia and headache. Based on their medical records, users were less likely to have health problems e.g. common cold, work-related fatigue, insomnia, diabetes and hypertension than were non-users. Conclusions. Most krathom users were still healthy and had no serious health problems despite prolonged use, except those who swallowed its fibre.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Surveys of Thai village krathom users on health effects; abstract does not state whether dependence criteria were assessed.

**Решение:** =

---

### 233 · R3635

**Validation of Krathom (Mitragyna speciosa Korth.) Dependence Scale (KDS): a dependence screen for internationally emerging psychoactive substance.**

2014 · Substance abuse · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1080/08897077.2014.924464

BACKGROUND: Krathom (Mitragyna speciosa Korth.) is the most commonly used illicit substance in Thailand, and its use has become widespread internationally. Studies on krathom dependence and its health impact are scarce, as there has been no instrument to measure its dependence syndrome and classify krathom users. This study aimed to develop and explore the factor structure, reliability, and validity of a Krathom Dependence Scale (KDS). METHODS: This study comprised 2 phases. First, cross-sectional surveys were conducted with 523 (Phase I) and 595 (Phase II) male villagers aged >25 years who were regular, occasional, ex-, or nonusers of krathom. Scale construction was based on the qualitative results from users and previous literature. Exploratory factor analysis (EFA) using maximum likelihood extraction with oblimin rotation was conducted in Phase I and confirmatory factor analysis (CFA) in Phase II to confirm the construct of the scale. Internal consistency of the KDS was assessed using Cronbach's alpha coefficient. Discriminative validity was examined by checking its ability to differentiate between regular and occasional users and patterns of krathom use and its concurrent validity by comparing its levels of score with the Fagerstrom Test for Nicotine Dependence (FTND). The KDS contains 16 items on a 0-3 (never-always) rating scale, making a total score of 0-48. RESULTS: Phase I EFA revealed a single-factor solution for the scale, which was confirmed by the CFA in Phase II, with an alpha coefficient of .98. The KDS discriminates regular from occasional users reasonably well and is highly correlated with the FTND score. Two cutoffs were suggested: 34/35 for distinguishing moderate from high dependence and 13/14 for low from moderate. CONCLUSIONS: The KDS appears to capture key theoretical constructs and correlates with indices of drug dependence by standard criteria. It should be useful in early intervention for those with krathom use disorders in community and primary care settings.

**ИИ:** + · обе модели · валидация шкалы · KDS validation study in Thai villagers who use kratom, with dependence cutoffs; could report how many users were dependent.

**Решение:** =

---

### 234 · R3639

**Kratom (Mitragyna speciosa) dependence, withdrawal symptoms and craving in regular users.**

2014 · Drug and alcohol dependence · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1016/j.drugalcdep.2014.03.017

Background Kratom (Mitragyna speciosa) preparations have been traditionally used in Southeast Asia for its medicinal properties. Lately, Kratom use has spread to Europe and the US, where abuse potential and health hazards increasingly emerge. This study is the first to measure systematically Kratom dependence, withdrawal symptoms, and drug craving in regular Kratom users in Malaysia. Methods A cross-sectional survey of 293 regular Kratom users was conducted in the community across three northern peninsular states of Malaysia. The Leeds Dependence Questionnaire, Marijuana Withdrawal Checklist, and Marijuana Craving Questionnaire-Short Form were used to measure Kratom dependence, withdrawal and craving. Results More than half of the regular users (>6 month of use) developed severe Kratom dependence problems, while 45% showed a moderate Kratom dependence. Physical withdrawal symptoms commonly experienced include muscle spasms and pain, sleeping difficulty, watery eyes/nose, hot flashes, fever, decreased appetite, and diarrhoea. Psychological withdrawal symptoms commonly reported were restlessness, tension, anger, sadness, and nervousness. The average amount of the psychoactive compound, mitragynine, in a single dose of a Kratom drink was 79mg, suggesting an average daily intake of 276.5mg. Regular users who consumed ≥3 glasses Kratom per day, had higher odds of developing severe Kratom dependence, withdrawal symptoms, and inability to control Kratom craving. Conclusions The findings from this study show that regular Kratom use is associated with drug dependency, development of withdrawal symptoms, and craving. These symptoms become more severe with prolonged use and suggest a stronger control of the drug.

**ИИ:** + · обе модели · употребляющие + мера зависимости · Community survey of 293 regular kratom users in Malaysia; used the Leeds Dependence Questionnaire and reports the share with severe or moderate dependence.

**Решение:** =

---

### 235 · R3640

**Mitragyna speciosa ) dependence , withdrawal symptoms and raving in regular users**

2014 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · обе модели · употребляющие + мера зависимости · Title matches Singh et al. 2014, a survey of regular kratom users in Malaysia that assessed dependence. Labelled 'Review' but appears to be primary data.

**Решение:** =

---

### 236 · R3682

**Pattern and the cause circle of offence related to addictive substance use in juvenile observation and protection centers, Thailand**

2013 · https://doi.org/10.4038/ijptsud.v1i1.5910

This cross-sectional study examines the pattern and cause circle of offence occurrences related to addictive substance use among 1002 juvenile participants (quantitative) and 52 participants (qualitative) in six juvenile observation and protection centers. The results indicated that males were more likely to use cannabis, kratom, Yaba, ecstasy, ketamine, and ice during their lifetime (p Juveniles who had entered the justice system after such experiences will have high risk of drug relapse and re-offence. Finding the pattern and the cause circle of offence occurrences may be beneficial to delivering interventions to resolve the gap of the cause circle before returning them to the community. DOI: http://dx.doi.org/10.4038/ijptsud.v1i1.5910 International Journal of Prevention and Treatment of Substance Use Disorder Vol.1(1) 2013: 38-50

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Thai juvenile detention survey assessed lifetime kratom use; truncated abstract does not say whether kratom dependence or use disorder was measured.

**Решение:** =

---

### 237 · R3754

**Measuring Dependence Severity Of Ketum (Mitragyna Speciosa) Use Among Ketum Leaf Users In Malysia**

2013 · review · https://core.ac.uk/download/199245856.pdf

Ketum or M.speciosa is an indigenous psychotropic plant commonly used for its medicinal value. Studies on ketum use is still scarce, hence further research is needed\ud to elucidate its prolonged use risk in humans. Study aim to determine the sociodemographic characteristics, measure ketum dependence severity, ketum withdrawal severity, ketum craving intensity and analyze the social functioning of ketum leaf users. A total of 293 ketum users were surveyed from three northern states of peninsular Malaysia (Penang, Kedah and Perlis). A cross-sectional study design using non-probability sampling techniques (purposive and quota) was used to collect data. Four study instruments specifically the Leeds Dependence Questionnaire, Marijuana Withdrawal Checklist, Marijuana Craving Questionnaire- Short Form, and Addiction Severity Index were used to measure ketum dependence severity among ketum leaf users. Respondents were all male, majority of Malay ethnicity. Eighty-five percent were employed, 46% were between the ages of 18-25 years, 41% were married, while three-fifths had completed eleven years (SPM) of education. Seventy-nine percent reported that they need to use ketum daily, 83% reported ketum can cause addiction if used regularly, 64% encountered sleeping problems, 67% became nervous, 72% were unable to control ketum desire and 90% had better social-functioning

**ИИ:** + · обе модели · употребляющие + мера зависимости · Survey of 293 ketum users in Malaysia that measured dependence severity with the Leeds Dependence Questionnaire; it is primary data even though it is labelled a review.

**Решение:** =

---

### 238 · R3771

**Neurocognitive Functioning In Ketum (Mitragyna Speciosa Korth) Leaf Users In Northern Parts Of Peninsular Malaysia**

2012 · review · https://core.ac.uk/download/225563166.pdf

Abuse of ketum (Mitragyna speciosa Korth) has increased recently in Malaysia. While there are extensive pharmacological studies of ketum effects on animals, human studies on patterns of neuropsychological function of ketum leaf users are limited. To measure the neurocognitive function of ketum users in the northern parts of peninsular Malaysia and compare it with that of healthy non-drug users (control group) and heroin dependents, also to compare the neurocognitive function of long term and short term ketum users

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Quantitative comparison of ketum users with controls and heroin dependents; abstract doesn't say whether ketum dependence was assessed.

**Решение:** =

---

### 239 · R3818

**The Development and validation of krathom dependence screening test and krathom withdrawal rating scale**

2012 · PSU Knowledge Bank (Prince of Songkla University) · dissertation, thesis · en

Thesis (Ph.D., (Epidemiology))--Prince of Songkla University, 2012

**ИИ:** + · обе модели · валидация шкалы · PhD thesis that developed and validated a krathom dependence screening test, so it likely reports dependence among users.

**Решение:** =

---

### 240 · R3870

**A survey of Mitragyna speciosa use at the border town of Kedah and Perlis.**

2011 · review

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Survey of kratom users in Malaysian border towns, no abstract; it may have assessed dependence despite the 'Review' record type.

**Решение:** =

---

### 241 · R3893

**Respondent-driven sampling: reaching male youth with drug use experience in Thailand**

2011 · Journal of Population and Social Studies · article · en

Respondent-Driven Sampling (RDS) was developed and has been widely used for recruiting sample from hard-to-reach populations such as populations at risk of HIV, injection drug users, males who have sex with males, and commercial sex workers. This article reports on the use of RDS technique in a research among Thai male youth aged 15-24 years who ever used drugs. Beginning with seventeen respondents who were used as initial seeds for recruiting more eligible subjects, the research was able to include 749 male youth with drug use experience in the sample. Majority of the recruited youth (41.3%) reported amphetamine as their first drug, followed by those who used mitragyna speciosa (20.1%), marijuana (17.2%), and inhalant (13.7%). Distribution of the sample youth recruited by this technique was found to be relatively normal which suggested that RDS was a reliable strategy for recruiting a sample of hard-to-reach populations. It is believed that this sampling technique can also be useful for the study of general hidden populations.

**ИИ:** разошлись — Opus ? (неясно, оценивали ли зависимость: RDS methods paper on Thai male youth who use drugs, including kratom users; abstract doesn't say whether kratom dependence was assessed.); Sonnet -3 (нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки: RDS methods paper on Thai male youth with drug experience; kratom only as first drug used, no dependence or use-disorder measure evident.)

**Решение:** - методологическая статья по выборке RDS, нет меры зависимости от кратома

---

### 242 · R3904

**Anxiety and depression among daun ketum users in northern peninsular Malaysia**

2010

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · There is no abstract. The title describes a survey of ketum users in Malaysia, which may have assessed dependence; the full text is needed.

**Решение:** =

---

### 243 · R3946

**The informal use of ketum (Mitragyna speciosa) for opioid withdrawal in the northern states of peninsular Malaysia and implications for drug substitution therapy.**

2010 · The International journal on drug policy · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1016/j.drugpo.2009.12.003

Background Ketum (krathom) has been mentioned in the literature as a traditional alternative to manage drug withdrawal symptoms though there are no studies indicating its widespread use for this purpose. This study examines the reasons for ketum consumption in the northern areas of peninsular Malaysia where it is widely used. Methods A cross-sectional survey of 136 active users was conducted in the northern states of Kedah and Penang in Malaysia. On-site urine screening was done for other substance use. Findings Ketum users were relatively older (mean 38.7 years) than the larger substance using group. Nearly 77% (104 subjects) had previous drug use history, whilst urine screening confirmed 62 subjects were also using other substances. Longer-term users (use >2 years) had higher odds of being married, of consuming more than the average three glasses of ketum a day and reporting better appetite. Short-term users had higher odds of having ever used heroin, testing positive for heroin and of using ketum to reduce addiction to other drugs. Both groups used ketum to reduce their intake of more expensive opiates, to manage withdrawal symptoms and because it was cheaper than heroin. These findings differ from those in neighbouring Thailand where ketum was used primarily to increase physical endurance. Conclusions No previous study has shown the use of ketum to manage opioid withdrawal symptoms except for a single case reported in the US. Ketum was described as affordable, easily available and having no serious side effects despite prolonged use. It also permitted self-treatment that avoids stigmatisation as a drug dependent. The claims of so many subjects on the benefits of ketum merits serious scientific investigation. If prolonged use is safe, the potential for widening the scope and reach of substitution therapy and lowering its cost are tremendous, particularly in developing countries.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Cross-sectional survey of 136 active ketum users; the abstract doesn't say whether dependence or use-disorder criteria were assessed.

**Решение:** =

---

### 244 · R4247

**A study of kratom eaters in Thailand.**

1975 · Bulletin on narcotics · article, case reports, journal article · eng · https://pubmed.ncbi.nlm.nih.gov/1041694/

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; classic Suwanlert study of a group of kratom users, tagged case report, may report dependence counts.

**Решение:** =

---

### 245 · R4381

**ความชุกและปัจจัยที่มีอิทธิพลต่อการใช้สารเสพติดของวัยรุ่นที่มีความหลากหลาย ทางชาติพันธุ์ในพื้นที่ภาคเหนือตอนบนประเทศไทย**

Disease Control Journal · article · th · https://doi.org/10.14456/dcj.2026.13

In contemporary society, characterized by cultural diversity and varying living environments, adolescents face heightened risks of substance use. This cross-sectional analytical study aimed to investigate the prevalence and factors influencing substance use. Participants included 238 adolescents (aged 15-17 years) recruited via simple random sampling. Research data were gathered through questionnaires between December 2024 and February 2025. Data was analyzed using descriptive statistics and logistic regression analysis. The findings revealed that alcohol consumption was the most prevalent form of substance use among adolescents (56.3%), followed by kratom use (18.5%), tobacco product use (13.9%), and cannabis use (7.1%). Tobacco use was significantly associated with being male (AOR=5.8; 95% CI: 2.39-14.39), alcohol consumption (AOR=33.1; 95% CI: 3.06-192.84), and kratom use (AOR=3.1; 95% CI: 1.40-8.58). Alcohol consumption was associated with depression (AOR=2.3; 95% CI: 1.25-4.34) family and peer factors (AOR=0.4; 95% CI: 0.23-0.89) tobacco use (AOR=22.2; 95% CI: 2.80-176.16) and kratom use (AOR=17.2; 95% CI: 3.83-77.31). Cannabis use was associated with being male (AOR=46.6; 95% CI: 6.14-403.02) and kratom use (AOR=65.6; 95% CI: 9.54-452.43). Kratom use was associated with tobacco use (AOR=2.8; 95% CI: 1.09-7.50), alcohol consumption (AOR=14.4; 95% CI: 3.19-65.80), and cannabis use (AOR=25.5; 95% CI: 4.49-145.01). The findings reveal a rising trend in substance use prevalence, particularly polydrug use. It recommended that rigorous and sustained policies be established to control and prevent access to alcohol and kratom among the adolescent population.

**ИИ:** ? · обе модели · неясно, оценивали ли зависимость · Survey of Thai adolescents reports kratom use prevalence; abstract doesn't say whether dependence was measured, but Thai questionnaires often use ASSIST.

**Решение:** =

---

### 246 · R0542

**Akuamma Seed (Picralima nitida) Use in the U.S.: Findings from a Web-Based Survey.**

2026 · Journal of psychoactive drugs · article, journal article, journalarticle · eng · https://doi.org/10.1080/02791072.2026.2618033

Indigenous to West Africa, akuamma seed (Picralima nitida) is used in traditional medicine and demonstrates opioidergic activity. Little is known about its role in management of pain or other ailments among people in the United States. This study presents findings from a web-based survey conducted between December 2023 and July 2024. Summary statistics characterized individuals reporting lifetime akuamma seed use, including demographics, substance use history, pain severity, and motivations. Between-group comparisons were conducted for those with and without lifetime akuamma seed use. Among 369 participants, 28 (7.6%) reported lifetime akuamma seed use. Those with lifetime akuamma seed use were older (44.7 years, p = .04), females (64.3%, p = .004), or currently disabled (32.1%, p < .001). They reported less alcohol (p = .033), more kava (78.6%, p = .001) and Delta-8 THC (71.4%, p < .001) use; all had tried kratom. Those who had tried akuamma seed indicated greater pain severity and reported use for pain management and opioid substitution; 60.7% reported pain relief from akuamma seed. No participants met DSM-5 criteria for akuamma seed-related substance use disorder modified. Akuamma seed may be used in the United States alongside other unscheduled psychoactive substances, particularly, psychoactive botanical-derived products. Additional research is needed to evaluate safety, efficacy, and health outcomes associated with akuamma seed.

**Ваша слепая метка (калибровка):** -6 не про кратом: веб-опрос потребителей семян акуаммы (Picralima nitida)

**ИИ:** ? · обе модели · другое · Akuamma-focused web survey that applied modified DSM-5 SUD criteria; sample includes kratom users, and kratom SUD may also have been assessed.

**Решение:** - не про кратом: веб-опрос потребителей семян акуаммы (Picralima nitida)

---

### 247 · R0807

**Concurrent polydrug use patterns of people who use illicit drugs in Austria: A latent class analysis**

2025 · OSF Registries · studyregistration/pre-registration, text/project, preprint · en · https://doi.org/10.17605/osf.io/qjyeu

We aim to investigate what concurrent polydrug use patterns among people who use illicit drugs (PWUiD) in Austria can be identified using data collected via web survey. Participants indicated which substances they had used in the last 30 days, in the last 12 months, and over their lifetime. We will examine substance-use groups separately for each of these timeframes. We will analyze all collection rounds of the survey done in Austria (2017, 2021, 2024), which will give us information on the stability of the identified groups. Based on findings from Eggerth et al. (2005) and Hannemann et al. (2017), we expect to identify distinct classes of substance use in Austria. Specifically, we expect the emergence of: (a) a cannabis use class, primarily characterized by cannabis use; (b) a classical party drug use class, characterized by the use of stimulants (i.e., cocaine, ecstasy/MDMA, amphetamine); (c) an extensive polydrug use class, characterized by the use of a wide range of substances; (d) a psychedelics use class, characterized by the predominant use of LSD, magic mushrooms, truffles, and other hallucinogens. And based on our own theoretical considerations we specified: (e) a downer user class, characterized by the use of heroin, synthetic opioids, kratom, other opioids than heroin (e.g., methadone, buprenorphine, fentanyl without prescription), and benzodiazepines. We further expect that these classes will differ in sociodemographic characteristics (e.g., age, income), without making specific assumptions about the direction of these differences. We also expect that the concurrent substance-use patterns captured in the 2021 survey may differ from previous years due to the impact of the COVID-19 pandemic. References Eggerth, A., Keller-Ressel, M., Lachout, S., &amp; Schmid, R. (2005). Konsumtypen bei Freizeitdrogenkonsumenten in Österreich. SUCHT, 51(2), 88–96. https://doi.org/10.1024/2005.02.04 Hannemann, T. V., Kraus, L., &amp; Piontek, D. (2017). Consumption patterns of nightlife attendees in Munich: A latent-class analysis. Substance Use &amp; Misuse, 52(11), 1511–1521. https://doi.org/10.1080/10826084.2017.1290115

**Ваша слепая метка (калибровка):** ? пререгистрация анализа опросов потребителей ПАВ в Австрии: зависимость может быть в анкете

**ИИ:** -3 · обе модели · нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки · Pre-registered latent class analysis of polydrug use timeframes; kratom use only, no kratom dependence or use-disorder measure described.

**Решение:** - пререгистрация анализа опросов в Австрии: только временные интервалы употребления, без шкалы зависимости

---

### 248 · R1290

**Kratom survey: Most daily users wanted more energy**

2024 · Alcoholism & Drug Abuse Weekly · article, journalarticle, review · en · https://doi.org/10.1002/adaw.34022

A survey of kratom users found that most used it in a problematic way, and that when it did become a problem, it was because they were trying to stop but couldn't because of withdrawal. Avoidance of withdrawal was, therefore, a motivator. This sounds a lot like the theory of George Koob, Ph.D., National Institute on Alcohol Abuse and Alcoholish director, of hyperkatifeia as the reason why people keep drinking (see “COVID‐19 experience reinforces theory that negative emotions drive alcohol use,” ADAW Nov. 9, 2020; https://onlinelibrary.wiley.com/doi/10.1002/adaw.32887 ).

**Ваша слепая метка (калибровка):** -1 новостная заметка / вторичный пересказ опроса потребителей кратома

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: A trade newsletter news item summarising someone else's kratom survey, not a primary study; the original survey should be screened instead.); Sonnet ? (неясно, оценивали ли зависимость: News summary of a survey of kratom users reporting problematic use and withdrawal; unclear whether use disorder or dependence was measured, so check the underlying study.)

**Решение:** - новостная заметка в Alcoholism & Drug Abuse Weekly о чужом опросе

---

### 249 · R2269

**Attitudes towards Kratom use, decriminalization and the development of a community-based Kratom control mechanism in Southern Thailand.**

2021 · The International journal on drug policy · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1016/j.drugpo.2021.103197

Kratom (Mitragyna speciosa Korth.) is an indigenous plant of Southeast Asia, which has been used in traditional medicine for centuries. Despite local communities in Southern Thailand viewing Kratom as a traditional remedy and not as an illicit drug, Thailand criminalized Kratom in 1943 which has led to tensions between government authorities and local communities. This study employed a mixed-method design to explore alternative ways to decriminalize Kratom, using a Participatory Action Research framework to develop a community charter to better manage Kratom in Tambon Namphu, a rural sub-district in Southern Thailand. Quantitative data consisted of face-to-face surveys with 457 Tambon Namphu residents, 104 students and teachers and on-line self-complete surveys conducted with 1,058 people outside Tambon Namphu. Qualitative data were collected using focus groups, in-depth interviews and through public forums conducted with Tambon Namphu residents. Survey results indicate that most participants agreed with decriminalization of both Kratom cultivation and consumption and typically reported positive attitudes towards people who use Kratom. The most common reasons for supporting Kratom decriminalization were Kratom's perceived benefits for work productivity and health. People had more positive attitudes towards the consumption of fresh Kratom leaves than Kratom decoctions which were deemed more harmful. Participatory action research methods were used to pilot the development of a community consensus framework for Kratom control in Donsai, a village of 127 households. Following successful piloting, the community consensus framework on Kratom control was adopted in Donsai, adapted across Tambon Namphu and then extended to cover 135 villages across Thailand.

**Ваша слепая метка (калибровка):** ? опрос жителей в Южном Таиланде (n=457): среди них есть потребители, зависимость может быть в таблицах

**ИИ:** -3 · обе модели · нет меры зависимости или расстройства для кратома: только доля употребления, мотивы, эффекты, установки · Mixed-methods survey of residents' attitudes toward kratom decriminalization; the abstract describes no kratom dependence or use-disorder measure.

**Решение:** - опрос в провинции Нампху посвящен декриминализации, нет клинической меры зависимости

---

### 250 · R2414

**A DRUG ADDICT'S KRYPTONITE**

2021 · CHEST Journal · article · en · https://doi.org/10.1016/j.chest.2021.07.650

_Аннотации нет — решайте по названию или ставьте `?`._

**Ваша слепая метка (калибровка):** -4 клинический случай токсичности кратома (CHEST Journal, poster/case)

**ИИ:** разошлись — Opus -4 (клинический случай или серия случаев; данные токсикологии, отравлений, смертей без опроса людей: No abstract; catchy-titled CHEST 2021 meeting abstracts are almost always single-patient case reports, not surveys of kratom users.); Sonnet ? (нет аннотации: No abstract. "Kryptonite" is slang for kratom, but this CHEST item is probably a case report. Full-text check needed to confirm.)

**Решение:** - постерный клинический случай в CHEST Journal

---

### 251 · R3404

**Addiction in Thailand**

2016 · Elsevier eBooks · book chapter, book-chapter · en · https://doi.org/10.1016/b978-0-12-800212-4.00101-1

_Аннотации нет — решайте по названию или ставьте `?`._

**Ваша слепая метка (калибровка):** -1 глава книги о зависимостях в Таиланде (без эмпирических данных)

**ИИ:** разошлись — Opus -1 (обзор, комментарий, теоретическая, правовая или регуляторная работа: A book chapter giving a broad overview of addiction in Thailand, most likely a narrative review rather than a primary study of kratom users.); Sonnet ? (нет аннотации: Book chapter on addiction in Thailand with no abstract; likely a review, but could cover kratom use data, so full text check is warranted.)

**Решение:** - глава книги о наркоситуации в Таиланде, без первичных данных
