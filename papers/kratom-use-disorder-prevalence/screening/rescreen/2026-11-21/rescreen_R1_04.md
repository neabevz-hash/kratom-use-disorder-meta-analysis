# Отбор вслепую по правилу защиты, часть 4

Записи 451–600 из 1154: записи, которые исключили обе модели (вне калибровочной выборки). Отбор вслепую по правилу защиты (протокол, §11b). **Меток ИИ здесь нет** — решайте по тем же критериям, что и в калибровке; в сомнениях — `?`. Порядок случайный (зерно 20261122).

**Быстрый режим:** достаточно одного символа — `+`, `?` или просто `-` (исключить, причина не нужна).

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

### 451 · R0488

**Uji Efektivitas Ekstrak Daun Kratom (Mitragyna speciosa Korth) dalam Menekan Bakteri Ralstonia syzygii subsp. indonesiensis secara In Vitro**

2026 · JURNAL PROTEKSI TANAMAN TROPIKA · article, journalarticle, journal-article · id · https://doi.org/10.20527/jptt.v9i1.3665

Pisang termasuk dalam komoditas hortikultura utama yang memberikan kontribusi ekonomi signifikan di Indonesia. Namun demikian, produktivitas tanaman ini menurun secara drastis akibat infeksi penyakit darah yang disebabkan oleh Blood Disease Bacterium (BDB). Salah satu jenis bakteri patogen dalam kelompok BDB adalah Ralstonia syzygii subsp. indonesiensis, yang diketahui bersifat sangat agresif dan mudah menyebar. Upaya pengendalian penyakit ini umumnya masih mengandalkan penggunaan bakterisida sintetis yang berisiko menimbulkan pencemaran lingkungan serta menyebabkan resistensi pada patogen. Oleh sebab itu, diperlukan alternatif pengendalian yang lebih aman dan berkelanjutan, seperti pemanfaatan pestisida nabati dari tumbuhan lokal. Penelitian ini bertujuan untuk mengevaluasi aktivitas antibakteri dari ekstrak daun kratom (Mitragyna speciosa Korth) terhadap pertumbuhan R. syzygii subsp. indonesiensis. Ekstrak daun kratom diperoleh melalui metode maserasi menggunakan pelarut etanol 96%, dan uji antibakteri dilakukan dengan teknik difusi agar menggunakan cakram kertas. Konsentrasi ekstrak yang diuji mencakup 5%, 10%, 15%, 20% dan 25%. Hasil penelitian menunjukkan bahwa pemberian ekstrak daun kratom (Mitragyna speciosa) pada berbagai konsentrasi mampu menghambat pertumbuhan bakteri Ralstonia syzygii subsp. indonesiensis secara in vitro. Rata-rata diameter zona hambat yang diamati berturut-turut untuk konsentrasi 5%, 10%, 15%, 20%, dan 25% adalah 4,15 mm; 6,71 mm; 7,75 mm; 8,39 mm; dan 10,00 mm, sedangkan kontrol (0%) tidak menunjukkan aktivitas antibakteri (0 mm). Hasil uji lanjut DMRT pada taraf 5% menunjukkan adanya perbedaan yang signifikan antar perlakuan. Hal ini mengindikasikan bahwa ekstrak daun kratom memiliki potensi sebagai agen antibakteri dengan efektivitas tertinggi diperoleh pada konsentrasi 25%.

**Решение:** -

---

### 452 · R3789

**Development of transcriptomic resources for interrogating the biosynthesis of monoterpene indole alkaloids in medicinal plant species.**

2012 · PloS one · article, journal article, research support, n.i.h., extramural · eng · https://doi.org/10.1371/journal.pone.0052506

The natural diversity of plant metabolism has long been a source for human medicines. One group of plant-derived compounds, the monoterpene indole alkaloids (MIAs), includes well-documented therapeutic agents used in the treatment of cancer (vinblastine, vincristine, camptothecin), hypertension (reserpine, ajmalicine), malaria (quinine), and as analgesics (7-hydroxymitragynine). Our understanding of the biochemical pathways that synthesize these commercially relevant compounds is incomplete due in part to a lack of molecular, genetic, and genomic resources for the identification of the genes involved in these specialized metabolic pathways. To address these limitations, we generated large-scale transcriptome sequence and expression profiles for three species of Asterids that produce medicinally important MIAs: Camptotheca acuminata, Catharanthus roseus, and Rauvolfia serpentina. Using next generation sequencing technology, we sampled the transcriptomes of these species across a diverse set of developmental tissues, and in the case of C. roseus, in cultured cells and roots following elicitor treatment. Through an iterative assembly process, we generated robust transcriptome assemblies for all three species with a substantial number of the assembled transcripts being full or near-full length. The majority of transcripts had a related sequence in either UniRef100, the Arabidopsis thaliana predicted proteome, or the Pfam protein domain database; however, we also identified transcripts that lacked similarity with entries in either database and thereby lack a known function. Representation of known genes within the MIA biosynthetic pathway was robust. As a diverse set of tissues and treatments were surveyed, expression abundances of transcripts in the three species could be estimated to reveal transcripts associated with development and response to elicitor treatment. Together, these transcriptomes and expression abundance matrices provide a rich resource for understanding plant specialized metabolism, and promotes realization of innovative production systems for plant-derived pharmaceuticals.

**Решение:** -

---

### 453 · R3049

**因妊娠期使用卡痛（Kratom）造成新生兒戒斷症候群**

2019 · article · zh

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 454 · R4219

**แอลคาลอยด์จากใบสดของต้นกระท่อม**

1990 · Chulalongkorn University

Thesis (M.Sc. in Pharm)--Chulalongkorn University, 1990The fresh leaves of Mitragyna speciosa (Korth.) Havil. Were examined for their alkaloids. Altogether nine alkaloids were isolated, six of which being heteroyohimbine alkaloids identified as mitragynine, paynantheine, speciogynine, mitraciliatine, ajmalicine, and tetrahydroalstonine. The other three being oxindole alkaloids identified as isopteropodine, isomitraphylline, and mitraphylline. Tetrahydroalstonine and isopteropodine have never been reported from this species before. The physical and chemical properties of these alkaloids were studies.สามารถแยกได้แอลคาลอยด์ 2 ประเภท คือ heteroyohimbines และ oxindoles จากใบสดของต้นกระท่อม Mitragyna speciosa (Korth.) Havil., heteroyohimbines ที่แยกได้มี 6 ชนิด คือ mitragynine, paynantheine, speciogynine, mitraciliatine, ajmalicine และ tetrahydroalstonine ส่วน oxindoles ที่แยกได้มี 3 ชนิด คือ isopteropodine, isomitraphylline และ mitraphylline แอลคาลอยด์ tetrahydroalstonine และ isopteropodine ยังไม่เคยมีรายงานว่าพบในพืชชนิดนี้มาก่อน พร้อมทั้งได้ศึกษาคุณสมบัติทาเคมีและกายภาพของแอลคาลอยด์ทั้ง 9 ชนิ

**Решение:** -

---

### 455 · R1127

**Testing for Kratom alkaloids in fingernail clippings - not only mitragynine.**

2024 · Journal of pharmaceutical and biomedical analysis · article, journal article, journalarticle · eng · https://doi.org/10.1016/j.jpba.2024.116078

Kratom (Mitragyna speciosa) is a species of large tree that grows in Southeast Asia and is part of the Rubiaceae family. Its fresh leaves are harvested for their medicinal properties and used for their psychoactive effects. Kratom contains many biologically active alkaloids, including mitragynine and 7-OH-mitragynine, which are considered the two most important psychoactive components and constitute approximately 66% and 2% of the total alkaloid content. Other alkaloids are present in the plant, such as speciogynine, speciociliatine and paynantheine, but have less psychoactive activity. Over the past decade, the sale of kratom powder has increased on the Internet. This led to a significant increase in forensic cases. Given the lack of data existing in the literature, and the total absence of data in nails, the authors report a study to determine the best target alkaloids for documenting kratom consumption in this matrix. Fingernail clippings from a supposed kratom powder user were analyzed after liquid-liquid extraction, chromatography separation using a HSS C18 column and performed on an ultra-high performance liquid chromatography coupled to a tandem mass spectrometer. In the specimen, mitragynine was quantified at 229 pg/mg, speciogynine and paynantheine were both quantified at 2 pg/mg, and speciociliatine was quantified at 19 pg/mg. 7-OH-mitragynine was not detected. The interpretation of these concentrations is complex, since there is currently no reference in the literature, as this is the first identification of mitragynine and other kratom alkaloids in nails. Nevertheless, in view of the high concentration of mitragynine, the subject seems to be a repetitive user of kratom. According to the measured concentrations, it seems that mitragynine remains the best target to document kratom consumption, but the identification of the other alkaloids would enhance the specificity of the test.

**Решение:** -

---

### 456 · R0752

**Abstract TAC132: Racial/Ethnic Disparities in Life’s Essential 8 Outcomes Among Women of Reproductive Age in Baltimore and Washington D.C.**

2025 · Hypertension · article · eng · https://doi.org/10.1161/hyp.82.suppl_1.tac132

Introduction: Cardiovascular disease (CVD) remains a leading cause of morbidity and mortality among women in the United States, with risks increasingly emerging in the reproductive years. Life’s Essential 8 (LE8) captures key health behaviors and factors influencing cardiovascular health. However, racial and ethnic disparities in LE8 components remain underexplored among women of reproductive age, particularly in community-based settings. Methods: We analyzed cross-sectional data from women aged 18–50 years enrolled in the SAFE HEART Study in Baltimore and Washington, D.C. Participants self-identified race and ethnicity and were categorized into four mutually exclusive groups: Non-Hispanic White, Non-Hispanic Black, Non-Hispanic Asian, and Hispanic (of any race). LE8 outcomes—including hypertension, hyperlipidemia, diabetes, BMI, diet, physical activity, sleep, and smoking—were based on self-report. Multivariable logistic regression models estimated adjusted odds ratios (ORs) and 95% confidence intervals (CIs) for each LE8 metric by racial/ethnic group, adjusting for age, education, income, insurance, and employment. Non-Hispanic White women served as the reference group. Results: The mean age of the sample was 30.86 ± 6.66 years. The sample was racially diverse: 47.8% identified as Non-Hispanic Black, 21.1% as Non-Hispanic White, 24.4% as Hispanic, and 3.1% as Asian. Most participants had some college education or higher (79.7%), were insured (79.4%), and employed (86.9%), though 68.1% reported financial strain. Significant disparities emerged across several LE8 metrics. Compared to Non-Hispanic White women, Non-Hispanic Black women had significantly higher odds of hypertension (OR=2.75, 95% CI: 1.45–5.23), hyperlipidemia (OR=2.41, 95% CI: 1.24–4.71), diabetes (OR=4.21, 95% CI: 2.04–8.72), and smoking (OR=4.70, 95% CI: 2.12–10.42). Hispanic women also had elevated odds of hypertension (OR=2.64, 95% CI: 1.27–5.46) and hyperlipidemia (OR=2.55, 95% CI: 1.19–5.49). No Asian participants reported hypertension or hyperlipidemia. Differences in sleep, diet, and physical activity were not statistically significant. Conclusion: Women of reproductive age in this urban sample face high burdens of cardiovascular risk, with pronounced disparities by race and ethnicity, particularly among Non-Hispanic Black and Hispanic women. Findings underscore the urgent need for culturally tailored prevention strategies that address both clinical and social drivers of cardiovascular health.

**Решение:** -

---

### 457 · R0324

**Drug problems in adolescents**

2026 · Digital Repository (National Repository of Grey Literature) · dissertation · cs

This thesis examines the issue of kratom use among adolescents from a social work perspective. The theoretical section focuses on substance use issues during adolescence, risk and protective factors, the legal context, and the specific characteristics of kratom. The empirical section is based on qualitative research conducted through semi-structured interviews with adolescents who have experience using kratom. The aim of the research was to understand the reasons that lead adolescents to use kratom and to capture the meanings and functions they attribute to this substance. The results show that kratom use is primarily linked to efforts to cope with schoolwork, psychological stress, and the daily demands of adolescence. At the same time, they highlight the importance of peer groups, family, and the online environment in shaping attitudes toward kratom use. The study emphasizes the importance of social work in the areas of prevention and support for adolescents and their families.

**Решение:** -

---

### 458 · R1352

**Mapování potřeb školních metodiků prevence v oblasti nových návykových látek**

2024 · bachelor thesis · ces/cze · http://www.nusl.cz/ntk/nusl-621977

Background: Nowadays, psychoactive substances are sold that are not subject to any control or regulation. Examples include kratom, HHC, CBD. In the short time of their existence, the effects and consequences of the use of these addictive substances have not been sufficiently studied, and their unlimited availability can be dangerous for the child population. Objectives: The aim of my work is to map the needs of school prevention workers at the level of primary education for prevention programs related to n addictive substances and to analyze the most significant obstacles in the performance of the function, requirements in the field of education and the own organization of programs, the change of which would lead to more effective planning of prevention programs. Methods: As part of the research, the so-called mixed-method was used, i.e. a combination of an online questionnaire study with school prevention workers from the Prague 5 district and individual semi-structured interviews, which were attended by 2 prevention workers who had previously filled out the questionnaire. Part of the questions in the questionnaire is taken from the questions of the SEPA preventive activities reporting system and part is based on research questions. The range of topics in the semi-structured interview is based on...

**Решение:** -

---

### 459 · R1702

**An evaluation of adverse drug reactions and outcomes attributed to kratom in the US Food and Drug Administration Adverse Event Reporting System from January 2004 through September 2021.**

2023 · Clinical and translational science · article, journal article, research support, n.i.h., extramural · eng · https://doi.org/10.1111/cts.13505

Abstract Kratom is a widely used Asian botanical that has gained popularity in the United States due to a perception that it can treat pain, anxiety, and opioid withdrawal symptoms. The American Kratom Association estimates 10–16 million people use kratom. Kratom‐associated adverse drug reactions (ADRs) continue to be reported and raise concerns about the safety profile of kratom. However, studies are lacking that describe the overall pattern of kratom‐associated adverse events and quantify the association between kratom and adverse events. ADRs reported to the US Food and Drug Administration Adverse Event Reporting System from January 2004 through September 2021 were used to address these knowledge gaps. Descriptive analysis was conducted to analyze kratom‐related adverse reactions. Conservative pharmacovigilance signals based on observed‐to‐expected ratios with shrinkage were estimated by comparing kratom to all other natural products and drugs. Based on 489 deduplicated kratom‐related ADR reports, users were young (mean age 35.5 years), and more often male (67.5%) than female patients (23.5%). Cases were predominantly reported since 2018 (94.2%). Fifty‐two disproportionate reporting signals in 17 system‐organ‐class categories were generated. The observed/reported number of kratom‐related accidental death reports was 63‐fold greater than expected. There were eight strong signals related to addiction or drug withdrawal. An excess proportion of ADR reports were about kratom‐related drug complaints, toxicity to various agents, and seizures. Although further research is needed to assess the safety of kratom, clinicians and consumers should be aware that real‐world evidence points to potential safety threats.

**Решение:** -

---

### 460 · R0421

**ACMT Highlights Episode 73 - Western Use of Kratom Products and Associated Challenges**

2026 · LVHN Scholarly Works · text

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 461 · R3873

**Metabolism studies of the Kratom alkaloid speciociliatine, a diastereomer of the main alkaloid mitragynine, in rat and human urine using liquid chromatography-linear ion trap mass spectrometry.**

2011 · Analytical and bioanalytical chemistry · article, evaluation study, journal article · eng · https://doi.org/10.1007/s00216-011-4660-9

Mitragyna speciosa (Kratom) is currently used as a drug of abuse. When monitoring its abuse in urine, several alkaloids and their metabolites must be considered. In former studies, mitragynine (MG), its diastereomer speciogynine (SG), and paynantheine and their metabolites could be identified in rat and human urine using LC-MS(n). In Kratom users' urines, besides MG and SG, further isomeric compounds were detected. To elucidate whether the MG and SG diastereomer speciociliatine (SC) and its metabolites represent further compounds, the phase I and II metabolites of SC were identified first in rat urine after the administration of the pure alkaloid. Then, the identified rat metabolites were screened for in the urine of Kratom users using the above-mentioned LC-MS(n) procedure. Considering the mass spectra and retention times, it could be confirmed that SC and its metabolites are so far the unidentified isomers in human urine. In conclusion, SC and its metabolites can be used as further markers for Kratom use, especially by consumption of raw material or products that contain a high amount of fruits of the Malaysian plant M. speciosa.

**Решение:** -

---

### 462 · R1438

**New Psychoactive Substances Discharged at Rest Areas along Interstate Highway in Kentucky - Wastewater Analysis**

2024 · Emerging Trends in Drugs Addictions and Health · article · en · https://doi.org/10.1016/j.etdah.2023.100123

Introduction: New psychoactive substances (NPS) such as synthetic opioids, synthetic cannabinoids, synthetic cathinones, and piperazines are intermittently introduced in the illicit drug supply chain. To monitor this ever-changing landscape of NPS, wastewater-based epidemiology offers a comprehensive, non-invasive, cost-effective, and time-efficient approach. Methods: Twenty-three forensically identified NPS were simultaneously analyzed in wastewater samples collected from rest areas along the interstate highway in Kentucky over twelve months using solid phase extraction and ultra-performance liquid chromatography coupled with tandem mass spectrometry. Results: Para-hydroxy methamphetamine and 1-(3-chlorophenyl) piperazine were the most frequently detected NPS (detection frequency, df = 100%). The mean mass load of para-hydroxy methamphetamine (methamphetamine corrected 85.9 mg/d/1000 people) and MAB- CHMINACA (9.06 mg/d/1000 people) were among the highest. Mitragynine and 4-methyl pentedrone have recently been associated with overdose deaths. In wastewater samples, mitragynine and 4-methyl pentedrone were detected (df ≥ 98%) at 36.4 and 28.5 mg/d/1000 people, respectively. Conclusions: This study shows that wastewater surveillance at the rest areas can potentially complement the existing forensic surveillance, such as components of the National Drug Early Warning System, in detecting NPS outbreaks.

**Решение:** -

---

### 463 · R0117

**Assessment of Abuse Potential-Related Effects of Oral Dried Kratom Leaf Powder in Healthy Normal Participants Following Single and Multiple Daily Doses.**

2026 · Drug testing and analysis · article, journal article, randomized controlled trial · eng · https://doi.org/10.1002/dta.70089

ABSTRACT Kratom is increasingly used in the United States for energy and self‐management of pain and mood. While its active alkaloid, mitragynine, has partial μ‐opioid receptor agonist activity, clinical data on its abuse potential remain limited. This study evaluated abuse‐related outcomes following single and multiple doses of dried kratom leaf powder in healthy kratom‐naive adults in a randomized, double‐blind, placebo‐controlled study. Healthy participants ( n = 116) received a single oral dose or 15 consecutive daily doses of Mitra‐Leaf kratom capsules (4 cohorts: 500–4000 mg dried leaf powder; equivalent to 6.65–53.2 mg mitragynine; n = 12–13 per cohort, n = 49 total) or placebo ( n = 67). Subjective effects were assessed using the Drug Effects Questionnaire (DEQ). Opioid withdrawal symptoms were evaluated using the Subjective Opioid Withdrawal Scale (SOWS) and Clinical Opiate Withdrawal Scale (COWS). Abuse‐related treatment‐emergent adverse events (ARTEAEs) were recorded. DEQ responses were dose‐related, except between the middle two dose levels with statistically significant increases in maximum effect and area‐under‐the‐curve compared to placebo observed only at the highest single dose. DEQ responses decreased following repeated dosing. No participants met the threshold for clinically meaningful opioid withdrawal based on COWS or SOWS. ARTEAEs occurred more frequently at higher doses but were generally mild and resolved without sequelae. No serious adverse events or deaths were reported. Oral administration of kratom at tested doses was well tolerated and associated with modest, dose‐related subjective effects, minimal withdrawal symptoms, and low ARTEAE rates. Findings support further research on kratom's safety and therapeutic potential, while emphasizing the importance of dose control and product standardization.

**Решение:** -

---

### 464 · R1781

**A UNIQUE PRESENTATION OF BRUGADA SYNDROME UNMASKED BY CHRONIC KRATOM USE**

2023 · CHEST Journal · article, journalarticle, journal-article · en · https://doi.org/10.1016/j.chest.2023.07.336

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 465 · R2992

**เภสัชจลนศาสตร์ของโคเดอีนในหนูขาวใหญ่ที่ได้รับมิตรากัยนึน**

2019 · Prince of Songkla University · thesis

Master of Science (Pharmacology), 2019Kratom (Mitragyna speciosa (Korth.) Havil.) belonging to the family Rubiaceae is the native plant in Southern Thailand. Mitragynine is the major alkaloid from kratom leaves. It has many pharmacological activities such as analgesic, antidiarrheal as well as anti-inflammatory effects. However, it has been reported as CYP450 enzymes inhibitors, especially CYP2D6. CYP2D6 is an enzyme which plays a role in the codeine metabolism to morphine. The combination use of kratom leaves and codeine may alter the pharmacokinetics of codeine. The objective of this study is to investigate the effect of mitragynine on the pharmacokinetics of codeine in mitragynine-pretreated rats. Rats were divided into two groups (n=13 per group). The first was the control group, rats were orally pretreated with the vehicle and another group was pretreated once a day with 15 mg/kg of mitragynine for seven consecutive days. After mitragynine or vehicle pretreatments, rats were administered single oral dose of codeine (25 mg/kg). Blood was collected from the tail vein at 0 before, and after 5, 10, 15, 30, 45, 60, 90, 120, 180, and 240 min of codeine administration. The plasma concentration versus time profile of codeine and morphine were analyzed by non-compartment pharmacokinetics model. Compared with the control group, the result showed that plasma concentration of codeine was significant increase in mitragynine pretreatment group. The relevant pharmacokinetic parameters were as follow: Cmax from 1.76 to 8.44 μg/mL, AUC4h from 193.74 to 774.87 μg min/mL and AUC0→∞ from 306.08 to 993.93 μg min/mL (p<0.05). Whereas the plasma concentration of morphine was significant decrease with Cmax from 2.32 to 0.45 μg/mL and AUC from 415.42 to 58.03 ug·h/mL (p<0.05). This study suggested that mitragynine was altered the pharmacokinetics of codeine in rats by increase codeine absorption and decrease codeinemetabolism to morphine. The inhibition of CYP2D6 isoenzyme by mitragynine postulated, which needs to further confirm this evidence.2017 The scholarship for Teacher Assistant from Faculty of Science, Prince of Songkla University 2019 Award for Academic Oral Presentation in National Academic Conference“สานพลังการก้าวข้ามขีดจํากัด เพื่อภาคใต้แห่งความสุข”พืชกระท่อม (Mitragyna speciosa (Korth.) Havil.) วงศ์ Rubiaceae เป็นพืชท้องถิ่นที่พบได้มากทางภาคใต้ของประเทศไทย มีสารกลุ่มอัลคาลอยด์ที่สําคัญ ได้แก่ สารมิตราภัยนั้น มีฤทธิ์ทาง เภสัชวิทยาในการระงับปวด แก้ท้องเสีย และยับยั้งการอักเสบ เป็นต้น แต่อย่างไรก็ตาม สารมิตรากัยนีน ในใบกระท่อม ยังมีฤทธิ์ในการยับยั้งการทํางานของเอนไซม์ไซโทโครม พี450 โดยเฉพาะอย่างยิ่ง CYP2D6 ซึ่งเป็นเอนไซม์ที่มีบทบาทในการเมแทบอลิซึมยาโคเดอีน เป็นมอร์ฟีน การได้รับพืชกระท่อม ร่วมกับยาโคเดอีน อาจทําให้เกิดการเปลี่ยนแปลงเภสัชจลนศาสตร์ของยาโคเดอีนได้ ดังนั้นการศึกษานี้ จึงมีวัตถุประสงค์ เพื่อศึกษาเภสัชจลนศาสตร์ของโคเดอีนในหนูขาวใหญ่ ภายหลังการได้รับมิตรา กัยนีน ทําการศึกษาโดยแบ่งหนูขาวออกเป็นสองกลุ่ม กลุ่มละ 13 ตัว หนูกลุ่มควบคุม จะได้รับการ เหนี่ยวนําด้วยตัวทําละลาย และหนูกลุ่มทดลองจะได้รับการเหนี่ยวนําด้วยมิตราภัยนั้น ขนาด 15 mg/kg โดยการป้อนทางปาก วันละหนึ่งครั้ง ต่อเนื่องเป็นระยะเวลา 7 วัน ภายหลังจากนั้น หนูขาวทั้งสองกลุ่ม จะได้รับยาโคเดอีน โดยการป้อนทางปาก ขนาด 25 mg/kg ทําการเก็บเลือดจากเส้นเลือดดําบริเวณปลายหาง ที่เวลา 0, 5, 10, 15, 30, 45, 60, 90, 120, 180 และ 240 นาที วิเคราะห์พารามิเตอร์ทางเภสัช จลนศาสตร์ด้วยแบบจําลองแบบไม่แบ่งส่วน ผลการศึกษาพบว่าหนูขาวกลุ่มที่ได้รับการเหนี่ยวนําด้วย มิตรากัยนั้น มีความเข้มข้นของโคเดอีนในเลือดสูงกว่ากลุ่มควบคุม อย่างมีนัยสําคัญทางสถิติ โดยมีค่าC เพิ่มขึ้นจาก 1.76 เป็น 8.44 ug/mL ค่า AUC และ AUC-2 เพิ่มขึ้นจาก 193.74 เป็น 774.87 ugmin/mL และ 306.08 เป็น 993.93 แg-min/mL ตามลําดับ ในขณะที่ความเข้มข้นของมอร์ฟีนกลุ่ม ทดลองต่ํากว่ากลุ่มควบคุม อย่างมีนัยสําคัญทางสถิติ (p<0.05) โดยมีค่า C ลดลงจาก 2.32 เป็น 0.45 ug/mL และ AUC ลดลงจาก 415.42 เป็น 58.03 4g-min/mL ดังนั้นผลการทดลองนี้จึงสามารถสรุปได้ ว่า สารมิตรากัยนั้นสามารถเปลี่ยนแปลงเภสัชจลนศาสตร์ของโคเดอีนไปจากเดิม โดยเพิ่มการดูดซึม โคเดอีน และลดการแปรรูปเป็นมอร์ฟีน ซึ่งการเปลี่ยนแปลงสันนิษฐานว่าอาจผ่านการยับยั้งการทํางาน ของเอนไซม์ CYP2D6 ภายในตับ ดังนั้นจึงจําเป็นที่จะต้องทําการศึกษากลไกการยับยั้งต่อไปในอนาค

**Решение:** -

---

### 466 · R0874

**Higher accumulation of mitragynine in Mitragyna speciosa (kratom) leaves affected by insect attack.**

2025 · PloS one · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1371/journal.pone.0320941

Kratom leaves are widely consumed by locals to increase their stamina for working longer hours in the field. However, insect damage to the leaves can lead to significant loss of leaf harvest. Despite this, there remains considerable uncertainty regarding how herbivory attack affects the chemical composition of kratom's leaf metabolome. In this study, we investigated the effect of insect herbivory on the secondary metabolites (SMs) of kratom leaves, using untargeted metabolomics as well as the effect on the accumulation of mitragynine and relation to leaf traits. The presence of diverse herbivore species were observed on the kratom leaves as indicated by three orders of insects including Coleoptera (beetles), Lepidoptera (butterflies and moths) and Hemiptera (true bug). A higher accumulation of mitragynine was observed as a defense mechanism against herbivores, with the study also finding a correspondence between increased mitragynine levels and elevated leaf acidity. A significant difference in the presence of three key metabolites (cearoin, 8-hydroxy-8-(3-octyloxiran-2-yl) octanoic acid, and 2,3,5,7-tetramethoxy-9,10-dihydrophenanthrene) that have interesting therapeutic usage, between insect and non-insect leaves, indicated the influence of interaction with insect herbivory. In conclusion, these findings highlight the potential to manage insect herbivory to modulate alkaloid accumulation in kratom, offering a sustainable approach that preserves insect biodiversity while naturally boosting the plant's chemical defense.

**Решение:** -

---

### 467 · R1180

**Detection of ADB-4en-PINACA Metabolite, 2-Methylmethcathinone and 3-Methylmethcathinone in Authentic Urine Samples**

2024 · Emerging Trends in Drugs Addictions and Health · article · en · https://doi.org/10.1016/j.etdah.2023.100079

Introduction: In Singapore, new psychoactive substances (NPS) continued to be prevalent with synthetic cannabinoids (SC), synthetic cathinones and mitragynine being detected. In early 2023, ADB-4enPINACA metabolite and the positional isomers of 4-methylmethcathinone (4-MMC), i.e., 2-MMC and 3-MMC were detected in drug users’ urine samples. To the best of our knowledge, ADB-4en-PINACA metabolite was the first time being identified in authentic urine sample. Methods: 0.5 mL of urine samples were incubated with β-glucuronidase enzyme and extracted. The extracted samples were screened using LC-Orbitrap MS method followed by confirmation using LC-QToF MS method. Results: ADB-4en-PINACA dihydrodiol metabolite was detected in two authentic urine samples, which was consistent to the result of the metabolic study.1 The identity was confirmed with the reference standard in both HRMS methods. Other SC metabolites such as MDMB-4en-PINACA metabolites, ADBBUTINACA metabolite and/or ADB-PINACA metabolite were also detected in the samples. In addition, 2-MMC and 3-MMC were recently detected in a few drug users’ urine samples. Using the sensitive and selective LC-QToF method, the three positional isomers of methylmethcathinone were chromatography separated and specifically identified with the reference standards. Conclusions: New NPS constantly enters the drug market with structural diversity and rapid development of the new derivatives, therefore, NPS continues to pose challenge for the drug detection in urine testing. The laboratory applies various techniques to comprehensively identify the new NPS and their positional isomers to cater for the rapid change.

**Решение:** -

---

### 468 · R3239

**Current Opiate and Opioid Hazards in Children and Adolescents**

2017 · Clinical Pediatric Emergency Medicine · article · en · https://doi.org/10.1016/j.cpem.2017.07.006

Abstract The use of opiates and opioids by both adults and children is a growing problem in the United States. With the increased prevalence of prescription opioid misuse, efforts have been aimed to control the spread of this epidemic. Prescription opioids, however, only represent a portion of the opiate-like products available through prescription or illicit means. We describe the hazards and increased use of opioid-related products such as heroin, fentanyl, and buprenorphine as well as emerging products of abuse such as Kratom, loperamide, and carfentanil.

**Решение:** -

---

### 469 · R0089

**Evaluating the Inhibitory Potential of Kratom Alkaloids on Cytrochrome P450**

2026 · ScholarWorks (Boise State University) · article, text · en

U.S. consumption of kratom (Mitragyna speciosa) has increased to nearly two million users as of 2022. The popularity of kratom products is attributed to their dose-dependent effects, where low doses are excitatory, and high doses are sedative. Individuals addicted to opioids who can no longer obtain them through a physician are increasingly turning to kratom as an accessible alternative. Despite being marketed as safe, kratom use is perilous, resulting in adverse events – including death – especially in poly-substance use with opioids or benzodiazepines. Between 2016 and 2017, the Centers for Disease Control (CDC) investigated 152 deaths involving kratom. Of these, 60% were determined to be caused by kratom, with only 7 instances of kratom detected as the sole substance in postmortem toxicology. Kratom is a natural substance that is federally unregulated; therefore, quality control evaluation of commercial products is not required. Although mitragynine and 7-hydroxymitragynine have been extensively studied, several other bioactive alkaloids remain underexplored. There is a critical need to understand the pharmacokinetic properties of other alkaloids in kratom. The current study addresses this by using in vitro cytochrome P450 assays to assess the potential for drug-herb interactions. The result of this investigation will inform regulatory bodies with the data needed to inform consumer safety guidelines.

**Решение:** -

---

### 470 · R2411

**Kratom use for depression/anxiety self-management: challenges during the COVID-19 pandemic - A case report.**

2021 · Heliyon · article, case reports, journal article · eng · https://doi.org/10.1016/j.heliyon.2021.e07039

BACKGROUND: Kratom is a psychoactive plant preparation originating from Southeast Asia. It has been used as a recreational and performance drug in Southeast Asia, and is now increasingly used in Europe and the U.S. CASE REPORT: We describe the case of a 63-year-old man who presented for treatment after his long-term Kratom use failed as a self-management for persistent major depression (ICD 10: F33.2) and a generalized anxiety disorder (ICD-10: F41.1). The failure coincided with emerging stress at the beginning of the COVID-19 pandemic. The patient suffered from childhood on from ruminative thinking and depressive mood, which was treated in several settings during his life. He started to use alcohol to control his depression, but developed an alcohol addiction. This was successfully treated and the patient remained abstinent for more than 25 years afterwards. About 7 years ago, he started to use Kratom 3-4 times daily on a regular, but constant rate. Kratom use worked efficiently as a self-management of his depression with no escalation of dosing. It was also very effective in reducing Morbus Menière symptoms of tinnitus and sudden hearing loss, which eventually allowed regular performance as a caregiver in a demanding job on shift-work. During recently increased stress load in the work environment and the COVID-19 pandemic, the established Kratom doses failed to control hyperarousal and mental nervousness. The patient was treatment seeking and subsequently detoxified from Kratom. Anxiety- and depression management was shifted to treatment attempts with Lorazepam, Venlafaxine, Opipramol, Mirtazapine and psychotherapy. CONCLUSION: Kratom instrumentalization for self-management of depression and anxiety may effectively work without causing escalation of drug use and addiction, but may be limited by a temporary increase in psychological stress load and a relapse into major depression and generalized anxiety disorder.

**Решение:** -

---

### 471 · R2599

**A New Data Repository for Pharmacokinetic Natural Product-Drug Interactions: From Chemical Characterization to Clinical Studies.**

2020 · Drug metabolism and disposition: the biological fate of chemicals · article, journal article, research support, n.i.h., extramural · eng · https://doi.org/10.1124/dmd.120.000054

There are many gaps in scientific knowledge about the clinical significance of pharmacokinetic natural product-drug interactions (NPDIs) in which the natural product (NP) is the precipitant and a conventional drug is the object. The National Center for Complimentary and Integrative Health created the Center of Excellence for NPDI Research (NaPDI Center) (www.napdi.org) to provide leadership and guidance on the study of pharmacokinetic NPDIs. A key contribution of the Center is the first user-friendly online repository that stores and links pharmacokinetic NPDI data across chemical characterization, metabolomics analyses, and pharmacokinetic in vitro and clinical experiments (repo.napdi.org). The design is expected to help researchers more easily arrive at a complete understanding of pharmacokinetic NPDI research on a particular NP. The repository will also facilitate multidisciplinary collaborations, as the repository links all of the experimental data for a given NP across the study types. The current work describes the design of the repository, standard operating procedures used to enter data, and pharmacokinetic NPDI data that have been entered to date. To illustrate the usefulness of the NaPDI Center repository, more details on two high-priority NPs, cannabis and kratom, are provided as case studies. SIGNIFICANCE STATEMENT: The data and knowledge resulting from natural product-drug interaction (NPDI) studies is distributed across a variety of information sources, rendering difficulties to find, access, and reuse. The Center of Excellence for NPDI Research addressed these difficulties by developing the first user-friendly online repository that stores data from in vitro and clinical pharmacokinetic NPDI experiments and links them with study data from chemical characterization and metabolomics analyses of natural products that are also stored in the repository.

**Решение:** -

---

### 472 · R0490

**7-OH and kratom vaping products: an emerging public health threat.**

2026 · Toxicological sciences : an official journal of the Society of Toxicology · article, editorial, journal article · eng · https://doi.org/10.1093/toxsci/kfaf169

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 473 · R3167

**Histologic Characterization of Kratom Use-Associated Liver Injury.**

2018 · Gastroenterology research · article, case reports, journal article · eng · https://doi.org/10.14740/gr990e

Kratom is an herbal product derived from the leaves of Southeast Asian Mitragyna speciosa trees. It has traditionally been used by indigenous people to relieve fatigue and manage pain, diarrhea, or opioid withdrawal. The use of kratom has become more commonplace in the United States for similar purposes. Only rare reports of kratom liver toxicity exist in the literature but without histologic characterization. Herein, we report one case of kratom use-associated liver toxicity in a 38-year-old patient. The patient complained of dark colored urine and light colored stools after using kratom. He had unremarkable physical examination. Laboratory testing at presentation revealed elevated alanine aminotransferase (389 U/L), aspartate aminotransferase (220 U/L), total bilirubin (5.1 mg/dL), and alkaline phosphatase (304 U/L). There was no serology evidence of viral hepatitis A, B, and C. The acetaminophen level at presentation was below detectable limits. Ultrasound examination of the right upper quadrant revealed normal echogenicity and contour of the liver without bile ductal dilatation or disease of the gallbladder. The patient underwent liver biopsy 4 days after the initial presentation which revealed a pattern of acute cholestatic liver injury including zone 3 hepatocellular and canalicular cholestasis, focal hepatocyte dropout, mild portal inflammation, and bile duct injury. Kratom was stopped, the patient improved clinically and biochemically and was discharged 8 days after the initial presentation. To our best knowledge, this is the first case report detailing the histology of kratom use-associated liver injury.

**Решение:** -

---

### 474 · R2597

**Kratom Dependence and Treatment Options: A Comprehensive Review of the Literature.**

2020 · Current drug targets · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.2174/1389450121666200719011653

Kratom, or Mitragyna speciosa Korth., is a tropical plant prevalent in Southeast Asia, and it is utilized as a traditional remedy for symptomatic relief of various illnesses. It has been labeled as an atypical opioid with significant narcotic-like properties, capable of inducing kratom dependence among those who misuse or abuse it. The prevalence of kratom use has drastically increased worldwide, raising concerns among healthcare providers, particularly regarding the availability of efficacious treatment options for kratom dependence. This manuscript provides a comprehensive narrative review of literature focusing on the psychoactive alkaloids of kratom, the possible neurobiological and pathophysiological models underlying the occurrence of kratom dependence, and the clinical presentations and effective treatment options available for kratom dependence. The psychoactive alkaloids of kratom, such as mitragynine (MG) and 7-hydroxymitragynine (7-HMG), act as partial mu opioid agonists and induce kratom dependence. As a result, regular kratom use leads to withdrawal symptoms on abstinence, along with craving, tolerance, and cross-tolerance to morphine. The psychological withdrawal symptoms reported include depressed mood, anxiety, restlessness, irritability, and feeling tense, while the physical withdrawal symptoms are myalgia and body ache, joint pain, lacrimation, running nose, yawning, insomnia, diarrhea, feverish sensation, loss of appetite, tremors, itching over the body, loss of concentration, and chills. Neonatal withdrawal symptoms, such as oral intolerance, restlessness, irritability, and vomiting, are also reported in newborns of women who are on regular kratom use. Sublingual buprenorphine-naloxone (Suboxone) is reported as a promising treatment for detoxification and maintenance replacement therapy for kratom-dependent users. Alternative treatments for in-patient detoxification include intravenous clonidine and a combination of oral dihydrocodeine and lofexidine. We conclude by adding a note on the research gap concerning kratom dependence, which future studies should focus on.

**Решение:** -

---

### 475 · R0997

**ฤทธิ์ต้านเชื้อแบคทีเรียของสารสกัดไมทราไจน่า สเปซิโอซาต่อเชื้อสเตรปโตค็อกคัส มิวแทนส์**

2025 · Khon Kaen University Dental Journal · article · en

Objective: The purpose of this study aimed to evaluate the antibacterial effect of Mitragyna speciosa Korth. (Kratom) extract on Streptococcus mutans. Materials and Methods: Crude extracts of kratom leaves were prepared using four extraction methods: maceration with 95% ethanol, maceration with 50% ethanol, decoction, and squeezing. S. mutans cultured in Mueller Hinton Broth was plated on Mitis Salivarius Agar. Paper discs containing kratom extracts from the four different extraction methods, and 0.12% chlorhexidine (as a positive control) were placed on agar plates. The inhibition zones were measured in millimeters, with clear zones indicating bacterial growth inhibition. The experiments were performed in triplicate. Data were recorded numerically and supplemented with images for analysis. Results: The experiments indicated a similar clear zone area in shape and size. A clear inhibition zone was seen around the filter disc soaked in 0.12% chlorhexidine, indicating its antibacterial activity against S. mutans, while discs soaked in other extracts allowed normal bacterial growth. Red and white kratom extracts were unable to inhibit bacterial growth regardless of the extraction method used (maceration with 95% or 50% ethanol, decoction, or squeezing). However, reduced clear zones were observed around paper discs soaked with extracts from white kratom (squeezing method) and red kratom (maceration with 95% ethanol), which exhibited a slight tendency to inhibit bacterial growth. Conclusion: Despite previous reports of antibacterial properties, kratom extracts obtained by the extraction methods in this study probably had a slight or no effect on S. mutans. Further investigation will provide more information on the effect of kratom on S. mutans.

**Решение:** -

---

### 476 · R3866

**Intrahepatic cholestasis following abuse of powdered kratom (Mitragyna speciosa).**

2011 · Journal of medical toxicology : official journal of the American College of Medical Toxicology · article, case reports, journal article · eng · https://doi.org/10.1007/s13181-011-0155-5

Introduction Kratom (Mitragyna speciosa) is a common medical plant in Thailand and is known to contain mitragynine as the main alkaloid. According to an increase in published reports and calls at German poison control centers, it has been used more frequently as a drug of abuse in the western hemisphere during the last couple of years. Despite this increase, reports of severe toxicity are rare within the literature. Case report We describe a case of a young man who presented with jaundice and pruritus after intake of kratom for 2 weeks in the absence of any other causative agent. Alkaloids of M. speciosa were detected in the urine. Conclusion While M. speciosa is gaining in popularity among illicit drug users, its adverse effects remain poorly understood. This is the first published case of intrahepatic cholestasis after kratom abuse.

**Решение:** -

---

### 477 · R4019

**違法ドラッグ市場に流通するKratom(Mitragyna speciosa)の基原種鑑別について**

2008

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 478 · R1528

**Effect of Red and Green Kratom on fat accumulation in 3T3-L1 cells.**

2023 · https://doi.org/10.1371/journal.pone.0291738.g005

After 72 hours, lipid accumulation in 3T3-L1 cells treated with Red and Green Kratom (0–10 μg/mL) was determined using Oil Red O staining (A). Lipid accumulation at each concentration was assessed in triplicate experiments and determined by measuring the absorbance of Oil Red O at 500 nm (B). The asterisk (*) indicates a statistically significant decrease in fat accumulation compared to 0 μM of each test inhibitor (p < 0.05, Student’s t-test). The experiments were done in triplicate.</p

**Решение:** -

---

### 479 · R3305

**Eksplorasi Penggunaan Ketum dalam Kalangan Belia di Negeri Kedah**

2017 · Jurnal Pembangunan Sosial · article, other literature type, journal-article · en · https://doi.org/10.32890/jps.20.2017.11549

Ketum atau nama saintifiknya Mitragyna Speciosa telah lama digunakan dalam amalan perubatan tradisional untuk merawat penyakit tertentu. Namun sejak akhir-akhir ini, ketum telah digunakan secara berleluasa sebagai bahan khayal bagi menggantikan dadah. Daun ketum direbus untuk menghasilkan air ketum dan dicampur dengan bahan-bahan lain seperti paracetamol, serbuk ubat nyamuk, dan air soda. Campuran air ketum bersama bahan tersebut boleh memberi kesan yang hampir sama dengan dadah dan menyebabkan pengamalnya ketagihan air ketum. Masalah ini berleluasa terutamanya di negeri-negeri Utara Semenanjung Malaysia. Sehubungan dengan itu, kajian ini bertujuan mengeksplorasi amalan penggunaan air ketum dalam kalangan belia di negeri Kedah. Hasil temu bual dengan tujuh informan kajian mendapati amalan penggunaan ketum adalah bagi tujuan kesihatan tubuh badan, dan sebagai alternatif kepada dadah. Selain itu, informan kajian sedar bahawa amalan pengambilan air ketum yang berlebihan dan air ketum campuran boleh membawa kepada kemudaratan termasuk kematian. Dapatan kajian ini adalah penting kepada profesion bantuan seperti pekerja sosial dan kaunselor dalam memahami amalan penggunaan ketum, seterusnya memberi input tentang intervensi dan program yang bersesuaian dalam menangani masalah ketum khususnya dalam kalangan belia

**Решение:** -

---

### 480 · R2141

**Kratom Use Among U.S. Adolescents: Analyses of the 2019 National Survey on Drug Use and Health.**

2022 · The Journal of adolescent health : official publication of the Society for Adolescent Medicine · article, journal article, research support, n.i.h., extramural · eng · https://doi.org/10.1016/j.jadohealth.2021.10.009

Background: Kratom (Mitragyna speciosa) is an opioid-like psychoactive substance not approved by the U.S. Food and Drug Administration that could be used due to its euphoric, stimulant, and analgesic effects. Kratom is gaining popularity in the U.S. and becoming a reason of concern among pediatricians. Methods: Data from the 2019 National Survey on Drug Use and Health were analyzed to estimate the prevalence and identify correlates of lifetime and past 12-month kratom use among 13,397 U.S. adolescents. Multivariable logistic regression models were conducted to assess the associations of interest. Results: Lifetime and past 12-month prevalence of kratom use was .44% (95% confidence interval [CI] .32–.60) and .27% (95% CI .18–.40), respectively. Past 12-month cigarette use was associated with lifetime kratom use (adjusted odds ratio 2.60, 95% CI 1.07–6.35). Past 12-month cannabis use was associated with past 12-month kratom use (adjusted odds ratio 2.48, 95% CI 1.15–5.35). Conclusions: This first report on the epidemiology of adolescent kratom use provides a baseline to assess kratom use trends in future years and identify potential correlates of use among adolescents.

**Решение:** -

---

### 481 · R1937

**Long-term buprenorphine treatment for kratom use disorder: A case series.**

2022 · Substance abuse · article, casereport, journalarticle · eng · https://doi.org/10.1080/08897077.2021.2010250

Background: Opioid agonist therapy with buprenorphine is an effective, evidence-based treatment for opioid use disorder. However, there has been increasing use of alternative substances which can still produce opioid-like effects. One of these substances is the herbal supplement kratom. The chemical composition of kratom, specifically mitragynine and 7-hydroxymitragynine, has partial mu-opioid receptor agonist and antagonist effects at the kappa- and delta-opioid receptors. Due to its addictive potential, accessibility, and legal status, there have been increasing cases of kratom use disorder (KUD). Thus, it is important to consider effective treatment options for this nontraditional substance. Methods: Twenty-eight patients self-identified kratom as their primary substance of use. Length of kratom use ranged between 1 month and 25 years, with an average daily kratom dose of 92 g/d. Nine patients were inducted on a buprenorphine/naloxone dose between 1 and 6 mg, 18 patients between 8 and 16 mg, and 1 patient at 20 mg. Three patients were stabilized on a dose at 4 mg, 23 patients between 8 and 16 mg, 1 patient at 18 mg, and 1 patient at 20 mg. Results: There was no correlation between stabilizing dose of buprenorphine/naloxone and past daily dose of kratom. As of March 2020, 20 of the 28 patients were still receiving outpatient buprenorphine/naloxone treatment. Six patients were lost to follow-up due to missed appointments, 1 tapered down to 0.25 mg of buprenorphine/naloxone and self-discharged, and 1 moved out of town. The rest have remained in treatment from 5 to 22 months, with an average duration of 11 months. Of the 28 patients, 68%, 82%, and 82% had negative test results for mitragynine at 4, 8, and 12 weeks of treatment, respectively. Conclusions: To our knowledge, this is the largest case series exploring long-term buprenorphine/naloxone treatment for KUD. Our findings suggest buprenorphine/naloxone can be used as an effective treatment option for KUD.

**Решение:** -

---

### 482 · R2002

**In vitro and in vivo pharmacology of kratom.**

2022 · Advances in pharmacology (San Diego, Calif.) · article, part of book or chapter of book, book chapter · eng · https://doi.org/10.1016/bs.apha.2021.10.001

Kratom products have been historically and anecdotally used in south Asian countries for centuries to manage pain and opioid withdrawal. The use of kratom products has dramatically increased in the United States. More than 45 kratom alkaloids have been isolated, yet the overall pharmacology of the individual alkaloids is still not well characterized. The purpose of this chapter is to summarize in vitro and in vivo opioid activities of the primary kratom alkaloid mitragynine and its more potent metabolite 7-hydroxymitragynine. Following are experimental procedures described to characterize opioid receptor activity; receptor binding and functional assays, antinociceptive assays, operant conditioning assays, and respiratory plethysmography. The capacity of kratom alkaloids to confer tolerance and physical dependence as well as their pharmacokinetic properties are also summarized. The data reviewed here suggest that kratom products and mitragynine possess low efficacy agonist activity at the mu-opioid receptor in vivo. In addition, kratom products and mitragynine have been demonstrated to antagonize the effects of high efficacy mu-opioid agonists. The data further suggest that 7-hydroxymitragynine formed in vivo by metabolism of mitragynine may be minimally involved in the overall behavioral profile of mitragynine and kratom, whereas 7-hydroxymitragynine itself, at sufficiently high doses administered exogenously, shares many of the same abuse- and dependence-related behavioral effects associated with traditional opioid agonists. The apparent low efficacy of kratom products and mitragynine at mu-opioid receptors supports the development of these ligands as effective and potentially safe medications for opioid use disorder.

**Решение:** -

---

### 483 · R3163

**กระท่อม: สมุนไพรหรือยาเสพติด**

2018 · Journal of Thai Traditional and Alternative Medicine · article · th

Kratom (Mitragyna speciosa Korth.) is an endemic plant species of Southeast Asia. The main constituents in kratom leaves are alkaloids, especially mytragynine and its derivatives, which possess psychological activities as well as nociceptive activities similar to those of morphine. This plant has been widely used throughout Southeast Asian countries asa herbal drug for decades. Kratom has been incorporated into many Thai traditional recipes for the treatment of diarrhea, cough, fever, muscle aches, opium withdrawal, diabetes and hypertension. It is also found in materia medica of Thai traditional medicine. In Thailand, kratom is used in men to combat fatigue and enhance tolerance to hard work under the scorching sun. Recently, there have been reports of kratom abuse, where kratom is mixed with other psychoactive substances, known as a kratom cocktail, 4x100. Thus, many countries have classified kratom and its constituents as controlled substances and narcotic drugs and imposed strict regulations on the production, utilization and distribution of this plant and its products. Nevertheless, the additional pharmacological and toxicological properties, methods of extraction with higher yield and the development of new pharmaceutical products of kratom and its constituents are continuously explored in many countries. Therefore, Thailand should review the role, regulation, and value of kratom especially in terms of herbal medicine.

**Решение:** -

---

### 484 · R0266

**Kava-potentiated Withdrawal in Persons Using Multiple Substances: A Case Series of Kava and Kratom Co-ingestion.**

2026 · Journal of addiction medicine · article, journal article, journalarticle · eng · https://doi.org/10.1097/adm.0000000000001678

Objectives: Kava ( Piper methysticum ) is indigenous to Pacific Island nations and has a long history of use in traditional medicine and ceremonies. Kava has effects similar to benzodiazepines, but its detailed mechanisms are uncertain. Although legal across the United States, kava is not without side effects. Currently, there are many kava and kratom blends accessible at stores and online. Recent case reports have emerged describing patient experiences with kava withdrawal when co-ingesting kava and kratom together; however, research remains scarce. This case series aims to add to the limited literature on kava withdrawal in co-ingestion of kava-kratom. Methods: Publications before July 2025 were searched using the Ovid Medline, PubMed, and Google Scholar databases using the terms “kava”, “kratom”, “withdrawal”, and “case report”. The 2 case reports were found describing kava withdrawal symptoms and treatment when co-ingesting with kratom. This case series presents 2 additional cases from our institutions. Results: All 4 patients were male with underlying histories of psychiatric illness and alcohol use disorder. All consumed more than the recommended amounts of the kava and kratom. Kava withdrawal symptoms were similar to sedative withdrawal. The onset of these symptoms varied considerably in relation to the last dose. Paradoxically, symptoms of kava withdrawal were observed in some cases despite sedatives still being present in the patients’ systems; however, the involvement of polysubstance complexes the exact etiology of symptoms. All patients improved with phenobarbital and/or benzodiazepines. Conclusions: Exact kava mechanism is complex and not fully understood. Further research is warranted.

**Решение:** -

---

### 485 · R1949

**Living Systematic Review on Cannabis and Other Plant-Based Treatments for Chronic Pain: Surveillance Report 1, September 2022**

2022 · review · https://doi.org/10.23970/ahrqepccer250.2022updatesr1

Overview This is the first surveillance report since the annual update of a living systematic review on cannabis and other plant-based treatments for chronic pain. The systematic review synthesizes evidence on the benefits and harms of plant-based compounds (PBCs), such as cannabinoids and kratom, used to treat chronic pain, and addresses concerns about severe adverse effects, abuse, misuse, dependence, and addiction. The purpose of this surveillance report is to describe new studies identified since the last search (April 2022) and provide a synthesis of the accumulated evidence. Surveillance update reports are planned on a quarterly basis, and the systematic review will be updated annually. The systematic review is available on the Agency for Healthcare Research and Quality (AHRQ) website (https://effectivehealthcare.ahrq.gov/products/plant-based-chronic-pain-treatment/livingreview). Table 1 provides a summary of the version history.

**Решение:** -

---

### 486 · R1630

**"Tianeptine abuse via novel, extended-release, star-shaped, drug delivery device".**

2023 · Toxicology reports · article, case reports, journal article · eng · https://doi.org/10.1016/j.toxrep.2023.07.006

We report a rare domestic case of exposure to tianeptine and use of a novel, extended-release, six-armed, star-shaped, drug delivery capsule. A 40-year-old male with a history of depression, anxiety, ethanol, opioid, cannabis, and tobacco use disorders presented to the emergency department (ED) from a substance abuse residential recovery treatment program after developing hypertension, tachycardia, and tremor for two day. He used an extended-release, six-armed, star-shaped, drug delivery device he purchased online, filling each arm with 15 mg of tianeptine (90 mg total). His intention was to mitigate the symptoms of kratom/opioid withdrawal through this extended-release method while simultaneously undergoing formal treatment for ethanol withdrawal. Tianeptine is an atypical tricyclic antidepressant that exerts complex mechanisms of action including serotonin (5-HT) neuromodulation as well as full μ-opioid and ∂-opioid receptor agonism. The capsule itself is made of caprolactone, which is a bioabsorbable material similar to absorbable sutures, initially developed as a long-term enteral antimalarial delivery method and is not FDA approved for human use. Over the course of the patients two day hospitalization course he developed symptoms consistent with uncomplicated ethanol withdrawal, which were treated with as-needed phenobarbital. No clinical manifestations of opioid or serotonin toxicity developed. Serial EKGs and telemetry monitoring remained unchanged. The patient was then medically cleared and discharged back to the residential recovery treatment program.

**Решение:** -

---

### 487 · R4184

**Serious drug reaction due to long continued use of ketoprofen gel (Ketum®)**

1997 · Nouvelles Dermatologiques · conference paper

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 488 · R1116

**Metamfetamine/Mitragyna-speciosa: Various toxicities, drug abuse and intentional drug misuse**

2024 · Reactions Weekly · article, journalarticle, journal-article · en · https://doi.org/10.1007/s40278-024-62768-9

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 489 · R0600

**AI-Assisted Thematic Analysis of 7-Hydroxymitragynine (7-OH) Discussion Across Reddit Communities: Surveillance Study Reveals Dependence Signals (Preprint)**

2026 · JMIR Publications Inc. · article, preprint · en · https://doi.org/10.2196/preprints.105386

BACKGROUND 7-Hydroxymitragynine (7-OH) is a potent μ-opioid receptor agonist found in trace amounts in Mitragyna speciosa (kratom) and increasingly marketed in concentrated, "enhanced" products that may expose consumers to a substantially stronger opioid than conventional botanical kratom. Because such products are emerging faster than traditional surveillance systems can track, naturalistic online discussion offers a potential early-warning window, but manual thematic coding of large post volumes is resource-intensive, and unconstrained use of large language models (LLMs) risks introducing unsupported content. OBJECTIVE This study applied a schema-guided, LLM-assisted extraction pipeline to characterize patterns of 7-OH use and dependence-relevant signals across dedicated Reddit communities, while directly benchmarking model coding against blinded human coding to determine which variables could be reliably automated. METHODS We collected 1,671 publicly available posts from five 7-OH–focused subreddits from community founding (2017–2024) through October 2024. A codebook developed with substance-use experts defined nine coding items spanning dependence indicators (quitting, withdrawal, tolerance, addiction language), consumption practices (route, reason for use), kratom comparisons, and physical and psychological side effects. A 100-post validation subset was coded by two blinded human coders and by GPT-3.5 Turbo. Interrater reliability was computed using Gwet's AC1, and items were retained for full-corpus analysis only when AI–human agreement fell within 0.05 of human–human agreement and exceeded 0.50. Descriptive prevalence and co-occurrence statistics were then computed across the full corpus. RESULTS Eight of nine primary items met reliability criteria; for two (kratom comparisons, physical side-effect presence) AI–human agreement exceeded human–human agreement. Only "reason for use" failed, reflecting low human–human agreement (AC1=0.20) on an item requiring clinical judgment. Tolerance was the most frequently discussed dependence indicator (17.6%, n=294), followed by quitting (6.0%) and withdrawal (5.3%); addiction language appeared in 4.2% of posts. Two or more dependence indicators co-occurred in 7.1% of posts; among posts using addiction language, 70% also mentioned tolerance and 54.3% mentioned quitting. Physical side effects were reported in 9.8% of posts (most commonly insomnia, 6.7%) and psychological side effects in 3.7% (anxiety, 3.2%). CONCLUSIONS Across 1,671 posts, frequently co-occurring discussion of tolerance, withdrawal, addiction, and quitting—alongside opioid-consistent side effects—suggests 7-OH may carry meaningful abuse liability distinct from botanical kratom. Methodologically, a hybrid design in which LLM coding is retained only after item-level reliability benchmarking achieved human-comparable performance for most, but not all, variables, supporting validated LLM assistance as a scalable tool for surveillance of emerging substances.

**Решение:** -

---

### 490 · R0033

**Fentanylization of Kratom: A narrative mini-review of escalating potency, access, and psychiatric complications**

2026 · World Journal of Psychiatry · journalarticle, review, journal article · en · https://doi.org/10.5498/wjp.126485

Recreational substance use in the United States trends towards increasingly concentrated products, including fentanyl, cannabis oils, and nicotine-salts.Concentrated and semi-synthetic alkaloids derived from the Mitragyna speciosa (Kratom) plant represent emerging substances of misuse due to accessibility and limited regulation.Available evidence suggests potential drug-drug interactions between Kratom alkaloids and psychiatric medications, as well as associations with psychiatric symptoms, withdrawal, dependence, and overdose.This review synthesizes the United States regulatory and market landscape and the psychiatric clinical, pharmacologic, and pharmacokinetic evidence regarding recreational Kratom alkaloid use.It introduces the term "fentanylization" as a framework for understanding how the escalating potency of Kratom products mirrors that of other concerning substances of misuse.We completed a narrative mini-review of PubMed, Google Scholar, and relevant United States government databases in September, 2026.Core adverse-outcome and pharmacology terms included "Kratom alkaloids", "7hydroxymitragynine", "mitragynine pseudoindoxyl", "Kratom drug interactions", "Kratom serotonin syndrome", "mitragynine CYP450", "Kratom psychosis", and "Kratom toxicity".To balance the search, additional pertinent terms were included, such as "Kratom therapeutic use", "Kratom pharmacokinetics", "mitragynine whole leaf", "Kratom epidemiology", and "Kratom opioid use disorder treatment".Limitations of narrative mini-reviews include author selection bias, nonreproducibility, and limited scope compared to traditional narrative reviews.Our search identified 400 scientific articles published between 2021 and 2026, compared with 244 publications from 1985 through 2020.Pharmacokinetic and pharmacologic research indicates Kratom, Kratom alkaloid extracts, and semi-synthetic alkaloids may carry health implications for consumers, including activity at mu-opioid receptors and inhibition or modulation of cytochrome P450 enzymes.Case reports describe Kratom-associated serotonin toxicity, psychosis, and mania, as well as risk for withdrawal, dependence, and overdose, though causation remains ill defined.The use of concentrated and semi-synthetic Kratom alkaloids poses a potential risk to consumers, particularly those with psychiatric disorders, though evidence of this risk is low quality and primarily focused on in vitro, animal, and case studies.These substances appear to follow a pattern of increasingly potent products that are easily available for consumer purchase.Clinicians should screen for and consider patients' Kratom usage when evaluating new symptoms and changing medications in psychiatric settings.

**Решение:** -

---

### 491 · R2201

**Adolescent kratom exposure affects cognitive behaviours and brain metabolite profiles in Sprague-Dawley rats.**

2022 · Frontiers in pharmacology · article, journal article, journalarticle · eng · https://doi.org/10.3389/fphar.2022.1057423

Adolescence is a critical developmental period during which exposure to psychoactive substances like kratom ( Mitragyna speciosa ) can cause long-lasting deleterious effects. Here, we evaluated the effects of mitragynine, the main alkaloid of kratom, and lyophilised kratom decoction (LKD) on cognitive behaviours and brain metabolite profiles in adolescent rats. Male Sprague-Dawley rats (Postnatal day, PND31) were given vehicle, morphine (5 mg/kg), mitragynine (3, 10, or 30 mg/kg), or LKD (equivalent dose of 30 mg/kg mitragynine) for 15 consecutive days. Later, a battery of behavioural testing was conducted, brain was extracted and metabolomic analysis was performed using LCMS-QTOF. The results showed that mitragynine did not affect the recognition memory in the novel object recognition task. In the social interaction task, morphine, mitragynine, and LKD caused a marked deficit in social behaviour, while in Morris water maze task, mitragynine and LKD only affected reference memory. Metabolomic analysis revealed distinct metabolite profiles of animals with different treatments. Several pathways that may be involved in the effects of kratom exposure include arachidonic acid, pantothenate and CoA, and tryptophan pathways, with several potential biomarkers identified . These findings suggest that adolescent kratom exposure can cause cognitive behavioural deficits that may be associated with changes in the brain metabolite profiles.

**Решение:** -

---

### 492 · R1485

**Kratom Use and Health Literacy of Kratom for User: A Narrative Review**

2024 · THE BANGKOK MEDICAL JOURNAL · article, review, journalarticle · en · https://doi.org/10.31524/bkkmedj.2024.13.001

Kratom is a tropical plant native to Southeast Asia. The delisting of kratom as a narcotic in many countries has significantly increased its accessibility, leading to greater experimentation with its usage. The kratom has the potential for pain relief, euphoria, and addiction to opioids. However, misuse, especially through potent mixtures like 4×100, can lead to adverse effects such as nausea, vomiting, and dizziness. Responsible use and health literacy are crucial for addressing concerns and preventing misuse, emphasizing the need for accurate information on kratom’s traditional and modern applications. This review aims to provide a comprehensive perspective on the effects of kratom use, usage patterns, clinical care guidelines for kratom users, and health literacy related to kratom use. A searched Pubmed, ScienceDirect, Google scholar, Scopus, and Thailand journal citation index center databases using appropriate search strategies for each database. After the screening, all relevant studies were included. Improper usage of kratom can detrimentally impact users’ health, manifesting side effects akin to both stimulant and opioid consumption, such as tachycardia, blushing, anxiety, agitation, loss of appetite, and polyuria. Therefore, promoting health literacy is essential for individuals using kratom responsibly to ensure a better understanding of its potential risks and benefits.

**Решение:** -

---

### 493 · R3364

**Notes from the Field: Kratom (Mitragyna speciosa) Exposures Reported to Poison Centers - United States, 2010-2015.**

2016 · MMWR. Morbidity and mortality weekly report · article, journal article, journalarticle · eng · https://doi.org/10.15585/mmwr.mm6529a4

Kratom (Mitragyna speciosa) is a plant consumed throughout the world for its stimulant effects and as an opioid substitute (1). It is typically brewed into a tea, chewed, smoked, or ingested in capsules (2). It is also known as Thang, Kakuam, Thom, Ketum, and Biak (3). The Drug Enforcement Administration includes kratom on its Drugs of Concern list (substances that are not currently regulated by the Controlled Substances Act, but that pose risks to persons who abuse them), and the National Institute of Drug Abuse has identified kratom as an emerging drug of abuse (3,4). Published case reports have associated kratom exposure with psychosis, seizures, and deaths (5,6). Because deaths have been attributed to kratom in the United States (7), some jurisdictions have passed or are considering legislation to make kratom use a felony (8). CDC characterized kratom exposures that were reported to poison centers and uploaded to the National Poison Data System (NPDS) during January 2010-December 2015. The NPDS is a national database of information logged by the country's regional poison centers serving all 50 United States, the District of Columbia, and Puerto Rico and is maintained by the American Association of Poison Control Centers. NPDS case records are the result of call reports made by the public and health care providers.

**Решение:** -

---

### 494 · R1939

**Kratom Induced Acute Tubular Necrosis**

2022 · Journal of the American Society of Nephrology · article, journalarticle, conference-abstract · en · https://doi.org/10.1681/asn.20223311s1355c

Introduction: Kratom (Mitragyna speciosa) is part of the coffee plant family (Rubiceae). Its use has been linked to rural workers in Indonesia and Malaysia but recently has gained popularity in the Western world. The active compounds are indole alkaloids (mitragynine) which act as partial opioid agonists. Its effects are described as a stimulant, analgesics and muscle relaxants. The potential drug to drug interactions, cross contamination and direct kidney injury makes it important for Nephrologists to recognize. This case highlights acute kidney injury in a young patient with daily use of Kratom. Case Description: A 28 y/o Caucasian man with history of DM type 1 and Psoriasis presented with one week of nausea, vomit and decreased urine output. Medication list included an insulin pump, Enbrel and Valtrex. He reported increased use of daily Kratom pills in the last week for anxiety. On physical exam, his VS were normal but was found to be hypovolemic. BUN was 44 mg/dl, Cr 9.53 mg/dl. Electrolytes, LFT’s CK were normal. Serologies were negative. U/A showed pyuria, 1+ eosinophils, no granular casts, no rbc’s and no crystals. A 24-hr urine had 2 gm of proteinuria. Urine toxicology was negative. Renal U/S had normal kidneys with no hydronephrosis. His kidney function became worse despite adequate intravascular volume expansion; therefore, a kidney biopsy was done and was consistent with acute tubular necrosis. His Cr peaked at 13 mg/dl and kidney function gradually improved without the need of any kidney replacement therapy. Discussion: Kratom consumption in the United States is unregulated and mostly available at herbal stores. The FDA has recommended to classify as Schedule I substance. We presented a case of oliguric AKI in a patient with Kratom consumption. Drug-todrug interaction and cross contamination are the main safety concern of this substance. Rhabdomyolysis, acute hepatic and kidney injury have been reported. It is important for the practicing Nephrologist and general clinicians to be aware of such herbal supplements and their presentations. More studies are needed to establish the exact pathogenesis and relation to causality.

**Решение:** -

---

### 495 · R2533

**วิจัยสร้างสรรค์ การแสดงชุด “มรดกถิ่นเสียงสำเนียงโทนโคราช”**

2021 · Humanities and Social Sciences Journal, Chiang Mai Rajabhat University · article · th

This creative research aimed to study the history of the Korat’s tone drum and to create a set of performances called “Moradok Thin Siang Samniang Tone Korat” (Local Heritage of Korat’s Tone Drum). The research was conducted through a qualitative research methodology. The research tools used for data collection consisted of both observation and interview forms, as well as the recording of the focus group’s dialogues and experts commentaries. The research results were then presented through descriptive analysis. The research found that the Korat’s tone is an imitation of the Khmer’s tone. It is used as an instrument for performing Korat’s traditional music. The tone itself is crafted from clay of the village in Dan Kwian. The tone’s face is made of snakeskin or lizard skin, which are fully stretched. The snake skin provides a soprano tune, whereas the lizard skin provides an alto pitch. The underlying objective of this research was to publicize, preserve and promote the Korat’s tone. The performance’s title represents the tone of Korat. The melody for the show is Korat’s folk music combined with Isan’s folk music. The dance movements are based on both Isan’s and Korats’ prototypical dance. In total, the performance consists of 15 movements, which can be further performed in 15 variations in rows. The dress styles consist of tank-sleeve shirts and loincloths. The thirteen female performers wear gold jewelry, beautiful makeup and “Kratum Thad Dok Sathorn” hairstyles. The instruments in the show are small Korat’s tones. This performance can therefore be held during general auspicious ceremonies and demonstrations along with other instructional activities.

**Решение:** -

---

### 496 · R1163

**Status Epilepticus Mimic: Severe Encephalopathy and Abnormal Movements Associated with Kratom Toxicity (P9-4.003)**

2024 · Neurology · article, journalarticle, journal-article · en · https://doi.org/10.1212/wnl.0000000000204770

Objective: To describe a case of recurrent encephalopathy and abnormal movements associated with chronic kratom use. Background: Kratom is an herbal substance which acts on mu-opioid receptors to produce opioid and stimulant-like effects. Originating in Southeast Asia, kratom use has increased in the United States over recent years. Case reports have established that kratom is associated with neurologic toxicity, including seizure and coma. We describe a case of recurrent severe encephalopathy and abnormal movements initially thought to be status epilepticus in a chronic user of kratom. Design/Methods: Case report Results: A 42-year-old man with a history of traumatic brain injury and Krabbe disease carrier status arrived at our hospital intubated and sedated on propofol and midazolam infusions for presumed status epilepticus. Family reported several days of intermittent convulsion and involuntary movements. Continuous EEG revealed frontal intermittent rhythmic delta activity without epileptiform discharges or seizures. MRI brain showed minor gliosis of the left inferior frontal lobe. Routine labs including toxicology screens were normal. After extubation, he was agitated and impulsive. He left the hospital against medical advice when this spontaneously resolved. He returned with encephalopathy and abnormal movements two weeks later. On examination, he was lethargic and had asynchronous brief losses of postural tone of the bilateral upper extremities. Continuous EEG revealed generalized periodic discharges of triphasic morphology. Urinalysis, urine drug screen, and autoimmune encephalopathy panel were unrevealing. On day 3, his mentation returned to baseline. He reported kratom use for the last year combined with the recent addition of a supplement for restless legs. He was counseled on drug cessation and discharged in stable condition. Conclusions: Kratom use has been associated with provoked seizures, agitation, and other neurologic sequelae. Because kratom is not detectable on standard urine drug screening, it is necessary for clinicians to inquire about use in cases of encephalopathy without identified etiology. Disclosure: Mr. Bluntson has nothing to disclose. Dr. Cothern has nothing to disclose. Dr. Willis has received personal compensation in the range of $10,000-$49,999 for serving as a Consultant for Alexion, Biogen. Dr. Willis has received personal compensation in the range of $10,000-$49,999 for serving on a Speakers Bureau for Alexion, Biogen.

**Решение:** -

---

### 497 · R2518

**Risk society and the fight for kratom use**

2021 · Colorado State University. Libraries · article, other literature type, other/text · en · https://doi.org/10.25675/3.03756

2021 Spring.Includes bibliographical references.This research argues that the rise of alternative medicine and health supplements is best understood within the context of the 'risk society'. The dual pressures of deregulation in the health sector of the economy and the dominance of Big Pharma, has the consequences of proliferating the use of non-sanctioned forms of health care. The Southeast Asian plant Kratom is one such illustration of this phenomenon. Drawing from over 200 Reddit posts on r/Kratom, this research analyzes the reaction of the kratom community to attempts by the Food and Drug Administration and Drug Enforcement Administration to restrict access to the botanical. Ulrich Beck's work on 'risk society' is combined with the recent literature on neoliberalism to analyze the narratives emerging from the community of kratom users. Using theme-based coding, the findings revealed tent-pole sentiments of 1) A desire for treatment agency and personal liberty, 2) Fear of regression or return to risk, and 3) Disdain and distrust of regulatory agencies and the pharmaceutical industry. Parallels to Beck's risk society were extant in the thematically related passages, including 1) the commonality of anxiety, 2) the loss of monopoly on knowledge from authoritative institutions, 3) the transition from patient ignorance versus being their own auxiliary doctor in the modern era, and 4) the power of corporatocracy overshadowing the traditional preeminence of the state. These arguments indicate a more nuanced understanding of neoliberalism is required. While typically seen as a way of freeing up capitalist markets for the benefit of large corporations such as Big Pharma, neoliberalism's emphasis on self-reliance and entrepreneurialism also provides a frame of resistance for those non-corporate actors threatened by State regulation. These findings enhance our understanding of the role of States and sub-community resistance in Ulrich Beck's theory of 'risk society'. In the context of risk society, the kratom community's experience with mainstream medicine and subsequently the pharmaceutical industry has made them distrusting of the state due to its failings to properly police such institutions and would rather be left to their own devices to decide what is and isn't appropriate for their respective conditions

**Решение:** -

---

### 498 · R1767

**Reversible Neuroimaging findings associated with Kratom use. (P12-5.021)**

2023 · Neurology · article, journal-article · en · https://doi.org/10.1212/wnl.0000000000203577

Objective: To report a case of reversible ischemic changes on MRI associated with chronic kratom use in a patient presenting with encephalopathy and seizures Background: Mitragyna speciosa, or kratom, is a psychoactive substance that targets multiple opioid receptors and has been an unregulated and under-reported substance of abuse. Its use has been reported to cause liver toxicity, respiratory depression, neuropsychiatric issues and even death. Its neurological side effects at this time are not well established. Design/Methods: We report a case of a 23-year-old male with a medical history significant for polysubstance abuse who presented for acute encephalopathy and seizure-like episode, requiring ICU admission and intubation for airway protection. Results: Patient initially presented with hypotension, leukocytosis, and lactic acidosis concerning sepsis. He was started on broad spectrum antibiotics for meningitis coverage and Keppra to prevent further seizures. Urine toxicology screen was negative. Once examined off sedation, the patient was noted to have right upper extremity weakness with babinski reflex on right concerning stroke therefore an MRI was obtained. It revealed small areas of confluent juxtacortical white matter abnormality high in the posterior frontal lobes bilaterally with some true diffusion restriction on the left suggestive of acute infarct. However, the appearance was unusual for a stroke. Further history from the family revealed that the patient uses Kratom on a daily basis for a number of years to help with anxiety. He had no further seizures and his mental status improved during the remainder of his hospitalization. Repeat MRI Brain 2 months after initial presentation showed resolution of the abnormalities. Conclusions: Kratom has been reported in the past to cause neurological issues like seizures or PRES. This case shows reversible ischemic neuroimaging findings of Kratom use in a patient with a stroke-like presentation. Disclosure: Dr. Pisati has nothing to disclose. Dr. Shah has nothing to disclose. Dr. Thaliath has nothing to disclose. Dr. Maryala has nothing to disclose. Dr. Allam has nothing to disclose.

**Решение:** -

---

### 499 · R1173

**ความหลากหลายทางสัณฐานวิทยาของกระท่อม (Mitragyna speciosa (Korth) Havil) ระดับประชากรในภาคใต้ของประเทศไทย**

2024 · วารสารวิทยาศาสตร์และเทคโนโลยี มหาวิทยาลัยมหาสารคาม (Journal of Science and Technology Mahasarakham University) · article · th

The objective of this research was to study the diversity of kratom subpopulation in the Southern Thailand using morphological characteristics for classification. Study on kratom specimens in 9 provinces in the area of Southern Thailand: Surat Thani, Nakhon Si Thammarat, Trang, Phatthalung, Krabi, Phang Nga, Chumphon, Prachuap Khiri Khan and Ranong. Record of ecosystem and morphological characteristics. Data were analyzed and a dendrogram using the UPGMA technique. It was found that kratom can be divided into 2 large groups: 1) Group of green petiole includes green, yellow-green and green-yellow colors 2) group of red petiole includes red, red-orange, pink-orange colors. Leaf shape can be classified into 3 types: lanceolate, obvate and obovate. Leaf base can be classified into 3 types: cuneate, obtuse and cordate. Leaf apex can be classified into 2 types: cuminate and cuspidate. Leaf margin can be classified into 2 types: entire and dentate. Stipule color can be classified into 3 groups: green and yellow-green group, orange-pink and pink-orange group and red-orange and red group. Therefore, it can be indicated that the Southern Thailand has a wide variety of kratom population with morphological differences.

**Решение:** -

---

### 500 · R1002

**Nanogel Formulations of Kratom (Mitragyna speciosa) Extract: A Promising Antibiofilm agent for Diabetic Ulcer Infections**

2025 · Research Journal of Pharmacy and Technology · article, journalarticle, journal-article · en · https://doi.org/10.52711/0974-360x.2025.00752

Diabetic ulcer infections present a substantial obstacle to wound management due to the prevalence of persistent bacterial biofilms that are impervious to conventional antibiotic therapies. Nanomaterials have emerged as a revolutionary platform for addressing the challenges of antibiotic resistance and biofilm-associated infections. Researchers have the potential to employ Kratom in the development of antibiofilm medicines specifically designed to combat diabetic ulcer infections. This is due to its capacity to impede bacterial quorum sensing and disrupt the process of biofilm development. Objective of this study is to determine the antibiofilm properties of the nanogel derived from kratom extract in diabetic ulcer infections. The study was carried out on a 96-well flat-bottom polystyrene microtiter plate using various doses of test chemicals (1%, 0.5%, 0.25%, 0.125% w/v) to identify their effects on S. aureus. The concentration of extract in nanogel used was 10, 20, and 30% to test antibiofilm in the mid-phase, maturation, and eradication phases. In the mid-phase biofilm, Kratom-derived nanogel extract (KDNE) at a concentration of 30% w/v exhibited significant antibiofilm efficacy against Staphylococcus aureus (SA), with an inhibition percentage of 79.21% ± 0.08; maturation phase of 74.12% ± 0,101; and eradication of 67.25% ± 0.046. KDNE compounds have shown efficacy against Staphylococcus aureus, suggesting their potential as natural antibacterial and antibiofilm agents.

**Решение:** -

---

### 501 · R1296

**Botanical-induced toxicity: Liver injury and botanical-drug interactions. A report on a society of Toxicology Annual Meeting symposium.**

2024 · Regulatory toxicology and pharmacology : RTP · conference paper, conference proceedings · eng · https://doi.org/10.1016/j.yrtph.2024.105708

Botanical supplements and herbal products are widely used by consumers for various purported health benefits, and their popularity is increasing. Some of these natural products can have adverse effects on liver function and/or interact with prescription and over-the-counter (OTC) medications. Ensuring the safety of these readily available products is a crucial public health concern; however, not all regulatory authorities require premarket safety review and/or testing. To address and discuss these and other emerging needs related to botanical safety, a symposium was held at the Society of Toxicology Annual Meeting in Salt Lake City (UT) on March 11, 2024. The symposium addressed the latest research on botanical-induced liver toxicity and botanical-drug interactions, including new approach methods to screen for toxicity, challenges in assessing the safety of botanicals, and relating human adverse events to specific products. The presentations and robust panel discussion between the speakers and audience highlighted the need for further research and collaboration to improve the safety of botanical supplements and herbal products, with the ultimate goal of protecting consumer health. Although utility of many of the modern tools presented in the symposium requires further study, the synergistic efforts of diverse experts hold promise for effective prediction and evaluation of botanical-induced hepatotoxicity and botanical-drug interaction potential.

**Решение:** -

---

### 502 · R1202

**Sex differences among patients with intentional poisoning presenting to the emergency Department at a Tertiary Care Centre in Beirut, Lebanon**

2024 · Basic and Clinical Pharmacology and Toxicology · article · https://doi.org/10.1111/bcpt.14039

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 503 · R1324

**An update on the clinical pharmacology of kratom: uses, abuse potential, and future considerations.**

2024 · Expert review of clinical pharmacology · article, journal article, review · eng · https://doi.org/10.1080/17512433.2024.2305798

ABSTRACT Introduction Kratom (Mitragyna speciosa) has generated substantial clinical and scientific interest as a complex natural product. Its predominant alkaloid mitragynine and several stereoisomers have been studied for activity in opioid, adrenergic, and serotonin receptors. While awaiting clinical trial results, the pre-clinical evidence suggests a range of potential therapeutic applications for kratom with careful consideration of potential adverse effects. Areas covered The focus of this review is on the pharmacology, pharmacokinetics, and potential drug–drug interactions of kratom and its individual alkaloids. A discussion on the clinical pharmacology and toxicology of kratom is followed by a summary of user surveys and the evolving concepts of tolerance, dependence, and withdrawal associated with kratom use disorder. Expert opinion With the increasing use of kratom in clinical practice, clinicians should be aware of the potential benefits and adverse effects associated with kratom. While many patients may benefit from kratom use with few or no reported adverse effects, escalating dose and increased use frequency raise the risk for toxic events in the setting of polysubstance use or development of a use disorder.

**Решение:** -

---

### 504 · R0508

**Complicating Factors Surrounding Concurrent Use of Kratom and a Novel 7-hydroxymitragynine Product Among a Participant Enrolled in a Kratom Clinical Trial.**

2026 · Journal of addiction medicine · article, journal article, case reports · eng · https://doi.org/10.1097/adm.0000000000001604

BACKGROUND: 7-Hydroxymitragynine (7-OH) is a highly selective mu opioid receptor agonist with binding affinity greater than morphine. Although trace amounts of 7-OH are found in kratom, it is formed by metabolism in humans after kratom ingestion. Novel semi-synthetic 7-OH products are manufactured by mono-oxidation of kratom's primary alkaloid, mitragynine. Formulations include sublingual tablets, powders, and liquid shots. We report a case of a study participant with self-reported 7-OH use. CASE PRESENTATION: A 23-year-old man using kratom for 3 years was enrolled into a clinical trial evaluating kratom pharmacokinetics, behavioral pharmacology, and withdrawal. He typically used 1.5-2g of kratom whole-leaf powder 6 times/day. Following scheduled kratom product self-administration during the study, several outcomes were atypical, including blunted subjective kratom effects. He reported recent initiation of a "new kratom product" ("Opia") identified as semi-synthetic 7-OH; he was using 20 mg 3 times/day for 4 days before study admission. Mitragynine (29.7 ng/mL) plasma concentration peaked at 1.5 hours post kratom self-administration, while 7-OH C max (11.7 ng/mL) occurred before self-administration, confirming prior ingestion of 7-OH. The participant reported withdrawal symptoms and requested early discharge from the study, but refused the study protocol kratom "rescue dose," stating he preferred to take his "stronger" product. DISCUSSION: Clinicians must obtain detailed self-reports from patients who report any kratom use. As 7-OH products are misleadingly marketed as kratom, and as both long-time kratom consumers and kratom-naive individuals may experiment with these novel products, improved assessment methods are urgently needed in the absence of real-time confirmatory testing.

**Решение:** -

---

### 505 · R2979

**Kratom exposures reported to United States poison control centers: 2011-2017.**

2019 · Clinical toxicology (Philadelphia, Pa.) · article, journal article, journalarticle · eng · https://doi.org/10.1080/15563650.2019.1569236

Abstract Context: Kratom, or Mitragyna speciosa, is a plant indigenous to Southeast Asia that has gained national attention in the United States for its increased use in the self-management of opioid withdrawal and pain, as well as for concerns about its safety. Methods: This study analyzes exposures to kratom reported to poison control centers (PCCs) in the United States during 2011–2017 from the National Poison Data System (NPDS). Discussion: From 2011 through 2017, 1807 kratom exposures were reported to United States PCCs. Almost two-thirds (65.0%) of these exposures occurred during 2016–2017. Most exposures occurred among adults ≥20 years (88.9%), males (70.8%), at a residence (86.1%), and were intentional (74.3%). Among first-ranked kratom exposures, 31.8% resulted in admission to a health care facility (HCF) and 51.9% in a serious medical outcome. Multiple-substance exposures were associated with greater odds of admission to a HCF (OR: 2.80; 95% CI: 2.21–3.55) and a serious medical outcome (OR: 2.25; 95% CI: 1.77–2.85) compared with single-substance exposures. There were 11 deaths associated with kratom exposure, including two that occurred after exposure to kratom only. Among kratom-only exposures, 86.1% resulted in one or more clinical effects. The most common clinical effects were agitation/irritability (22.9%) and tachycardia (21.4%). There were seven neonatal exposures, including five experiencing withdrawal. Conclusions: Kratom is associated with a variety of serious medical outcomes, especially when used with other substances. More research is needed to define the human response to kratom. Increased regulation of kratom products would help guarantee product quality and safety. Individuals who choose to use kratom should be educated about its potential risks, including the dangers of using it in combination with other substances.

**Решение:** -

---

### 506 · R2054

**(PO-154) Impact of COVID-19 Pandemic on the Quality of Psychiatric Consultation-Liaison Work**

2022 · Journal of the Academy of Consultation-Liaison Psychiatry · article · en · https://doi.org/10.1016/j.jaclp.2022.03.147

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 507 · R4097

**Energy drinks consumption in male construction workers, Chonburi province.**

2004 · Journal of the Medical Association of Thailand = Chotmaihet thangphaet · article, journal article, journalarticle · eng · https://pubmed.ncbi.nlm.nih.gov/15822540/

This unmatched case-control study aimed to determine the relationship among caffeine drinks consumption known as "energy drinks consumption", drug dependence and related factors in male construction workers in Chonburi Province. It was conducted during December 15, 2001 and February 15, 2002. Data were collected using interview questionnaires. The logistic regression was used to control possible confounding factors. The subjects consisted of 186 cases who had consumed energy drinks for more than 3 months and 186 controls who had given up for more than 3 months. They were frequency/group matched by age group. There was statistically significant association among energy drinks consumption and overtime work, motivation from advertisements, positive attitude of energy drinks consumption, alcohol drinks, smoking and ex-taking Kratom behavior. Multivariate analyses revealed that only 5 factors were related to energy drinks consumption: marital status (OR = 1.88, 95%CI: 1.14, 3.11), overtime work (OR = 2.84, 95%CI: 1.73, 4.64), motivation from advertisements (OR = 2.72, 95%CI: 1.67, 4.42), positive attitude of energy drinks consumption (OR = 4.06, 95%CI: 1.65, 10.01) and ex-taking Kratom behavior (OR = 2.77, 95%CI: 1.19, 6.44). As a result, construction workers should be provided with the knowledge of energy drinks consumption, the effect of drug dependence behavior, and the advantages of safe and healthy food that is cheap, readily available, and rich in nutrients.

**Решение:** -

---

### 508 · R2727

**The Therapeutic Prospects of Naturally Occurring and Synthetic Indole Alkaloids for Depression and Anxiety Disorders**

2020 · Evidence Based Complementary and Alternative Medicine · review · https://doi.org/10.1155/2020/8836983

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 509 · R3993

**Focus group discussion on HIV/AIDS risk behaviors in a fishermen's community of east coast, Malaysia**

2008 · Springer

There is a need to examine risk factors contributing to the high prevalence of HIV/AIDS in the fishermen's communities. A qualitative study by using focus group discussion method was conducted in one of the fishermen's village of East Coast, Malaysia. A total of thirty-five people were recruited and five focus group discussions of 6-9 people were conducted over a period of 7 months. The selection of participants was based on villagers that were able to give the best information about the topic being discussed. Structured open ended questionnaires were used to ensure consistency approach between facilitators. All sessions were video-taped with respondent's consent. The discussions were transcribed per verbatim and several contentious themes were developed. Every respondent agreed that HIV/AIDS is an immense problem in the village. Many of the villagers were involved in HIV/AIDS risk behaviors. Multiple sex partners, smoking, alcohol abuse, glue sniffing, intravenous drug abusing and ketum leaves addictions were being practiced freely in the village. Children start to smoke and glue sniff as early as eight years old. Easy accessibility of all the substances in the village and lack of support and supervision from parents and ignorance and lack of recreational and religious activities instigated them to involve in high risk behaviors. Negative stigma towards drug abusers hindered them from involvement in behaviors in the community which are interrelated to each other and lead to high HIV/AIDS prevalence in the community. For effective HIV/AIDS preventive and control measures in the fishermen's community, the researchers recommended integrated approach of actions by various group of people and agencies

**Решение:** -

---

### 510 · R0332

**Method optimization foriIdentification and quantitation of mitragynine in commercial beverage products via GC-MS**

2026 · OpenBU (Boston University) · dissertation, thesis · en

As of April 2026, 48 states have pending legislation on the regulation of kratom. Several states have taken the initiative to ban kratom and kratom-related products. This has come to include Feel Free® and Happy Hippo products, which contain both kratom and kava. Prior to 2026, kratom/kava products were available in gas stations, wellness stores, and smoke shops across the country, easily acquired with a single transaction. The availability of kratom has led to a significant increase in exposure, addiction, and overdose on these substances, spanning almost every age demographic from pre-teens to the elderly. The addictiveness of these products is highlighted by mitragynine, the main alkaloid of kratom, and its higher binding affinity to the mu receptor than morphine. As mitragynine is metabolized, the compound is converted into 7-hydroxymitragynine, a naturally present alkaloid found at low levels within kratom, which is even more potent than mitragynine. This increased potency of 7-hydroxymitragynine is often exploited by users and abused on its own in other commercial products. It was important for this research to optimize a GC-MS method for the detection and quantitation of mitragynine in Feel Free® and Happy Hippo products. Through the optimization of the Yulikawanti et al. method, a GC-MS method was developed. The quantitation of the original bottles of Feel Free® and Happy Hippo were calculated to be 34.573 mg and 78.942 mg, respectively, compared to the supplement labels' reported 40 mg and 50 mg.

**Решение:** -

---

### 511 · R2565

**Medicinal plants utilized in Thai Traditional Medicine for diabetes treatment: Ethnobotanical surveys, scientific evidence and phytochemicals**

2020 · Journal of Ethnopharmacology · review · https://doi.org/10.1016/j.jep.2020.113177

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 512 · R1080

**Insights into the alteration of vaginal microbiota and metabolites in pregnant woman with preterm delivery: prospective cohort study.**

2025 · Frontiers in cellular and infection microbiology · article, journal article, journalarticle · eng · https://doi.org/10.3389/fcimb.2025.1580801

Disruptions in vaginal microbiota and metabolites during pregnancy may be the most important risk factor for preterm delivery, thus the difference in vaginal microbiota and metabolites between women who subsequently delivered at term and who eventually experienced preterm birth. In this study, 63 participants were enrolled before the cervical cerclage surgery (namely pre-cerclage), comprising women who subsequently delivered at term and who eventually experienced preterm birth. The cervical-vaginal fluid (CVF) was collected two days prior to the cervical cerclage surgery. Compared with the term birth groups (PrTG), the proportion of beneficial bacteria (Lactobacillus, Prevotella, Trichococcus, Neisseria and Gemella) in the preterm birth group (PrPG) were significantly reduced (p < 0.05), while the proportion of harmful bacteria (Thauera, Ochrobactrum, Gardnerella, Massilia, Phyllobacteriaceae and Atopobium) were significantly increased (p < 0.05). In addition, vaginal metabolomics-based LC-Orbitrap-MS/MS revealed that the contents of 2-Piperidone, Melphalan, N-acetylputrescine, Obatoclax, Eurostoside, Pregnanediol 3-O-glucuronide, O-Phospho-L-serine, 1-Kestose and N-arachidonylglycine were significantly decreased in the PrPG group compared with the PrTG group, while Acenocoumarol, Isopyrazam, Pentosidine, hexose, 7-Hydroxymitragynine, PE, Tamoxifen and 1-Deoxynojirimycin contents were significantly increased. These results suggest that specific bacterial species and metabolites may serve as potential biomarkers for preterm birth prediction, and approve the theoretical basis for the intervention of preterm birth.

**Решение:** -

---

### 513 · R0099

**Elevated 7-Hydroxymitragynine Levels Found in Products Misbranded as Kratom.**

2026 · Journal of AOAC International · article, journal article, journalarticle · eng · https://doi.org/10.1093/jaoacint/qsaf094

Abstract Background The leaves of Mitragyna speciosa, commonly called kratom, have been consumed for centuries for their energizing and analgesic properties. Kratom has gained popularity in North America, with an estimated 16 million American consumers. Recently, a new product has emerged, labeled “kratom extract” but purportedly composed of high concentrations of 7-hydroxymitragynine, an oxidation product of mitragynine, the primary alkaloid found in kratom. Objective 7-hydroxymitragynine, a potent mu-agonist, may pose a serious public health risk. Commercial products labeled as containing 7-hydroxymitragynine were evaluated to determine whether the constituent was present and in what concentration. Method The concentrations of 7-hydroxymitragynine and mitragynine were determined by a previously validated HPLC-DAD method, AOAC Official MethodSM 2017.14. The chromatographic profiles of products were also compared to authentic kratom leaf. Results All products were described on their label as containing “kratom extracts.” The concentration of mitragynine ranged from 2.0 to 6.0 mg/g dry weight, substantially lower than typically found in kratom leaves or extracts. 7-hydroxymitragynine was determined at 22–75 mg/g dry weight, 5–28% higher than the label claims. The chromatographic profiles of all products were inconsistent with kratom leaf, having exceptional levels of 7-hydroxymitragynine, lacking the other major naturally occurring alkaloids, and exhibiting peaks not observed in leaf. Conclusions The products were verified to contain very high levels of 7-hydroxymitragynine, achievable only by synthetic means. These products differ significantly from authentic native kratom leaf and are not kratom extracts, as labeled, but rather synthetic derivatives that constitute unapproved new drugs being unlawfully marketed. There is an urgent need to differentiate kratom, which has been safely consumed for centuries, from 7-hydroxymitragynine, which may pose a significant risk to public health. Highlights Traditional kratom leaf is distinguished from products found to contain high concentrations of 7-hydroxymitragynine, only achievable by synthetic means. These unapproved new drugs contained other unidentified constituents, also not present in the native kratom leaf. The presence of concentrated 7-hydroxymitragynine products in the market masquerading as kratom is misleading, unlawful, and potentially dangerous to the public.

**Решение:** -

---

### 514 · R3849

**Evaluation of the effect of Mitragyna speciosa alkaloid on cytochrome P450 enzymes using a novel high throughput assay**

2011

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 515 · R0679

**Evaluation of the unregulated online kratom market in two east-central European countries: test purchase and analysis of potential toxicological consequences.**

2025 · Harm reduction journal · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1186/s12954-025-01363-0

BACKGROUND: As interest in human enhancement continues to rise in Europe, kratom (Mitragyna speciosa) products have raised significant public health concerns. Kratom, which is used for its dose-dependent stimulant and sedative effects, has grown in popularity to enhance mood and self-manage pain or opioid withdrawal symptoms. This study aimed to assess the East-Central European online kratom market, evaluate product quality, and analyze potential toxicological risks to inform evidence-based harm reduction strategies. METHODS: A comprehensive approach was employed, including online market surveillance, detailed content analysis of vendor websites, test purchase of products, followed by chemical analysis. Google search engine results were used to identify vendors shipping to Hungary. A total of 59 web shops were identified, and 25 distributors were selected for further analysis. Eight online sellers were included in test purchases. Mitragynine content was analyzed using supercritical fluid chromatography coupled with tandem mass spectrometry (SFC-MS/MS) and high-performance liquid chromatography with diode-array detection (HPLC-DAD). Toxicovigilance data were extracted from the United States Food and Drug Administration Adverse Event Reporting System (FAERS) and the Center for Food Safety and Applied Nutrition Adverse Event Reporting System (CAERS). RESULTS: The online kratom market in East-Central Europe is extensive and accessible, with many sellers identified in Hungary, the Czech Republic, Slovakia, and the Netherlands. While 68% (n/N = 17/25) of the evaluated web shops promoted enhancement effects, only 32% (n/N = 8/25) presented any information on potential adverse effects. Analysis of the products revealed highly variable mitragynine content, with mean concentrations ranging between 14.16 and 18.41 mg/g in powder form, and 42.60-210.20 µg/mL in prepared teas. Vigilance databases revealed 1090 cases in FAERS and 630 in CAERS associated with kratom use, with high rates of serious outcomes, including 592 deaths reported in FAERS. CONCLUSIONS: The online kratom market in East-Central Europe poses a significant public health threat, particularly to individuals seeking its enhancement effects. The significant variability in the mitragynine content, combined with the lack of safety information creates a high-risk environment. Toxicological data revealed a high incidence of serious adverse reactions, particularly in cases of polysubstance use. These findings highlight the urgent need for regulatory oversight and harm reduction strategies.

**Решение:** -

---

### 516 · R4175

**Neuropharmacological studies on mitragynine and mitragynine Pseudoindoxyl,compounds related to a Thai folk medicine Mitragyna speciosa: Elucidation of opium-like properties(タイ伝承民間薬Mitragyna speciosaの活性成分mitragynineとその関連化合物mitragynine Pseudoindoxylに関する神経薬理学的研究: オピオイド作用の解明)**

1998 · 千葉大学 · book, dissertation · ja · https://doi.org/10.11501/3135935

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 517 · R1363

**การพัฒนารูปแบบการป้องกันปัญหายาเสพติดของนักเรียน ในหลักสูตรการศึกษานอกระบบ จังหวัดพะเยา**

2024 · Journal of Roi Kaensarn Academi · article · th

This research and development endeavor aims to investigate drug addiction issues, devise a prevention model, and assess its efficacy among students in alternative education programs in Phayao province. The study involves a sample group comprising public health officers, community leaders, teachers, and high school students, totaling 360 individuals. The research unfolds in three phases: 1) probing drug addiction issues, 2) formulating a prevention model, and 3) gauging the model's effectiveness. Research instruments include questionnaires with tool reliability scores ranging from 0.86 to 0.97. Statistical analyses encompass descriptive statistics and paired t-tests. The results showed that: 1) prevailing substance abuse among students stands at 35.83%, with alcohol being the most commonly abused substance at 37.45%, followed by cigarette/electronic cigarette smoking at 34.26%, marijuana at 14.74%, kratom at 11.95%, and methamphetamine at 1.59%. Statistically significant correlations (p-value < 0.05) were noted between substance abuse and variables such as average monthly income, pre-existing medical conditions, living arrangements, perception of substance abuse, supportive factors, and reinforcing factors. 2) The prevention model comprises five operational strategies: (1) Establishing student support systems, (2) Enhancing social immunity, (3) Implementing the "To Be Number One" project, (4) Preventing and addressing substance abuse issues (alcohol/cigarettes), and (5) Developing information dissemination systems, documents, and media related to substance abuse. 3) Evaluation outcomes indicate significant enhancements in life skills, perception of substance abuse, and preventive behaviors among the sample group post-program completion (p < 0.001). Notable reductions in cigarette/electronic cigarette smoking and alcohol consumption behaviors were observed. Hence, it is recommended to extend the program's reach to other areas through ongoing collaboration among teachers, parents, students, community leaders, and public health officials to sustain efforts in substance abuse prevention and intervention.

**Решение:** -

---

### 518 · R3108

**Examining the Therapeutic Potential of Kratom Within the American Drug Regulatory System**

2018 · Springer eBooks · book chapter, other literature type, part of book or chapter of book · en · https://doi.org/10.1007/978-3-319-76720-8_5

Kratom is a plant native to Southeast Asia. It has been used for hundreds, if not thousands, of years in traditional medicine within that region. Kratom is a rare substance, due to it having both stimulant and narcotic properties. Kratom use has spread to regions outside of its native geographic range, and these countries are simultaneously considering both the benefits kratom could hold for patients and the misuse that could occur among drug users. Within the United States, after reports of increasing kratom use, the Drug Enforcement Administration (DEA) announced its intention to regulate the plant on an emergency basis. After considerable public and legislative backlash, the DEA backed off of this decision. To date, no federal regulation exists within the United States, and only a few states have regulations. This chapter discusses kratom use within Southeast Asia and the growing body of research documenting the potential medical benefits as well as the abuse liability of kratom. It concludes by discussing the drug regulation system within the United States and the potential hurdles kratom might face before becoming a recognized part of American pharmacopeia.

**Решение:** -

---

### 519 · R1948

**Living Systematic Review on Cannabis and Other Plant-Based Treatments for Chronic Pain: 2022 Update**

2022 · Living Systematic Review on Cannabis and Other Plant-Based Treatments for Chronic Pain: 2022 Update · book chapter, report, review · eng · https://doi.org/10.23970/ahrqepccer250update2022

Objectives. To update the evidence on benefits and harms of cannabinoids and similar plant-based compounds to treat chronic pain using a living systematic review approach. Data sources. Ovid® MEDLINE®, PsycINFO®, Embase®, the Cochrane Library, and SCOPUS® databases; reference lists of included studies; and submissions received after Federal Register request were searched to April 4, 2022. Review methods. Using dual review, we screened search results for randomized controlled trials (RCTs) and observational studies of patients with chronic pain evaluating cannabis, kratom, and similar compounds with any comparison group and at least 1 month of treatment or followup. Dual review was used to abstract study data, assess study-level risk of bias, and rate the strength of evidence (SOE). Prioritized outcomes included pain, overall function, and adverse events. We grouped studies that assessed tetrahydrocannabinol (THC) and/or cannabidiol (CBD) based on their THC to CBD ratio and categorized them as comparable THC to CBD ratio, high-THC to CBD ratio, and low-THC to CBD ratio. We also grouped studies by whether the product was a whole-plant product (cannabis), cannabinoids extracted or purified from a whole plant, or a synthetic product. We conducted meta-analyses using the profile likelihood random effects model and assessed between-study heterogeneity using Cochran’s Q statistic chi square test and the I2 statistic. Magnitude of benefit was categorized as no effect or small, moderate, and large effects. Results. From 3,283 abstracts, 21 RCTs (N=1,905) and 8 observational studies (N=13,769) assessing different cannabinoids were included; none evaluated kratom. Studies were primarily short term, and 59 percent enrolled patients with neuropathic pain. Comparators were primarily placebo or usual care. The SOE was low unless otherwise noted. Compared with placebo, comparable THC to CBD ratio oral spray was associated with a small benefit in change in pain severity (7 RCTs, N=632, 0 to10 scale, mean difference [MD] −0.54, 95% confidence interval [CI] −0.95 to −0.19, I2=39%; SOE: moderate) and overall function (6 RCTs, N=616, 0 to 10 scale, MD −0.42, 95% CI −0.73 to −0.16, I2=32%). There was no effect on study withdrawals due to adverse events. There was a large increased risk of dizziness and sedation, and a moderate increased risk of nausea (dizziness: 6 RCTs, N=866, 31.0% vs. 8.0%, relative risk [RR] 3.57, 95% CI 2.42 to 5.60, I2=0%; sedation: 6 RCTs, N=866, 8.0% vs. 1.2%, RR 5.04, 95% CI 2.10 to 11.89, I2=0%; and nausea: 6 RCTs, N=866, 13% vs. 7.5%, RR 1.79, 95% CI 1.19 to 2.77, I2=0%). Synthetic products with high-THC to CBD ratios were associated with a moderate improvement in pain severity, a moderate increase in sedation, and a large increase in nausea (pain: 6 RCTs, N=390, 0 to 10 scale, MD −1.15, 95% CI −1.99 to −0.54, I2=48%; sedation: 3 RCTs, N=335, 19% vs. 10%, RR 1.73, 95% CI 1.03 to 4.63, I2=28%; nausea: 2 RCTs, N=302, 12.3% vs. 6.1%, RR 2.19, 95% CI 0.77 to 5.39; I²=0%). We also found moderate SOE for a large increased risk of dizziness (2 RCTs, 32% vs. 11%, RR 2.74, 95% CI 1.47 to 6.86, I2=40%). Extracted whole-plant products with high-THC to CBD ratios (oral) were associated with a large increased risk of study withdrawal due to adverse events (1 RCT, 13.9% vs. 5.7%, RR 3.12, 95% CI 1.54 to 6.33) and dizziness (1 RCT, 62.2% vs. 7.5%, RR 8.34, 95% CI 4.53 to 15.34); outcomes assessing benefit were not reported or insufficient. We observed a moderate improvement in pain severity when combining all studies of high-THC to CBD ratio (8 RCTs, N=684, MD −1.25, 95% CI −2.09 to −0.71, I2=58%; SOE: moderate). Evidence (including observational studies) on whole-plant cannabis, topical or oral CBD, low-THC to CBD, other cannabinoids, comparisons with active products or between cannabis-related products, and impact on use of opioids was insufficient to draw conclusions. Other important harms (psychosis, cannabis use disorder, and cognitive effects) were not reported. Conclusions. Low to moderate strength evidence suggests small to moderate improvements in pain (mostly neuropathic), and moderate to large increases in common adverse events (dizziness, sedation, nausea) with high- and comparable THC to CBD ratio extracted cannabinoids and synthetic products during short-term treatment (1 to 6 months); high-THC to CBD ratio products were also associated with increased risk of withdrawal due to adverse events. Evidence for whole-plant cannabis and other comparisons, outcomes, and plant-based compounds was unavailable or insufficient to draw conclusions. Small sample sizes, lack of evidence for moderate and long-term use and other key outcomes, such as other adverse events and impact on use of opioids during treatment, indicate that more research is needed.

**Решение:** -

---

### 520 · R0145

**Exploring perceived drivers of occupational stress and coping strategies among nurses in the Buea Health District, Cameroon: a qualitative study**

2026 · BMC Public Health · article · eng · https://doi.org/10.1186/s12889-026-29629-7

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 521 · R3483

**A Comparison of Mitragyna Speciosa and Mitragynine Against Opioids on Thermal Nociception in Rats**

2015 · eGrove · dissertation, text · en · https://core.ac.uk/download/148695039.pdf

The purpose of this experiment is to compare Mitragyna speciosa (M. speciosa) and its active component, mitragynine, a known µ-opioid receptor (MOR) agonist, against well-known and commonly abused opioids, morphine and oxycodone. Another goal of this research is to determine if these compounds are also active when administered orally as is typical in human users. Male Sprague-Dawley rats were administered M. speciosa and mitragynine both intraperitoneally (IP) and orally and their antinociceptive effects were evaluated on the hotplate. Mitragynine exhibited antinociceptive effects similar to oxycodone when administered both IP and orally. M. speciosa exhibited a trend towards antinociceptive effects when administered both IP and orally. This research demonstrates that M. speciosa possesses properties like oxycodone and raises the possibility of an abuse liability which might warrant consideration for restrictions on the consumer marketplace.

**Решение:** -

---

### 522 · R4065

**Pharmacological studies on 7-hydroxymitragynine, isolated from the Thai herbal medicine Mitragyna speciosa : discovery of an orally active opioid analgesic**

2006 · Institutional Repositories DataBase (IRDB) · thesis, dissertation · en · https://opac.ll.chiba-u.jp/da/curator/900034443/

研究科: 千葉大学大学院医学薬学府 修了年:2006 千大院医薬博乙第薬2号

**Решение:** -

---

### 523 · R2387

**สารเสพติดที่ใช้ร่วมในผู้ป่วยเสพติดกระท่อม**

2021 · Journal of The Department of Medical Services · article · th

Background: Thai teenagers like to boil kratom leaves as a base for a cocktail pattern including cough syrup, cola and other substance. These kratom decoction can produce addictive effect in addition to kratom leaves and also cause harms from other substances in the decoction.Objective: This research aimed to identify the types of drugs or substances found in kratom decoction and kratom dependent patients’ urine.Method: The samples were 69 kratom addicts who met the DSM-IV-TR and they are treated at Princess Mother National Institute on Drug Abuse Treatment (PMNIDAT), Thanyarak Songkhla Hospital, and Thanyarak Pattani Hospital. Age of samples were 18 years and older and they had willing to participate in the research. The data were collected by kratom use questionnaire which consisting of demographic data , drug use information and urine test record form. The validity kratom use questionnaire, each item has the Index of Item-Objective Congruence between 0.67-1.00. The data were analyzed by descriptive statistics such as frequency, percentage, mean and standard deviation.Result: Most kratom dependent patients put substances other than kratom leaves in kratom decoction. They mixed cola and cough syrup in kratom decoction. The top 5 substances that found in the kratom dependent patients’ urine were nicotine, mitragynine, caffeine, methamphetamine, and diphenhydramine ranging 86.95, 85.51, 62.32, 56.52 and 42.03 percent respectively.Conclusion: The substances that found in the urine were either substances that are mixed or use with kratom and contamination from food and other. Some substances may be able to cause more danger to the health of the Kratom addicts

**Решение:** -

---

### 524 · R2405

**Effets hépatobiliaires des substances utilisées par les usagers de drogues : revue de la littérature**

2021 · CCSD · thesis

Introduction: The use of psychoactive substances (PAS) has diversified over the past several years, with a heterogeneous user population and a variety of products consumed. If the use disorder and the psychiatric disorders related to the consumption are known, the somatic complications are less known. Method: We conducted a review of the literature to analyze the hepatotoxic potential of the main PAS, apart from infectious hepatic complications related to injections. Results: Among the substances we studied, those most known to cause liver damage are MDMA (also known as ecstasy), cocaine, kratom and khat. MDMA and cocaine are substances that are increasingly used, particularly by young people, unlike khat and kratom, whose use remains more exceptional in France. Conclusion: somatic complications related to the use of PAS contribute to their dangerousness and can have a warning value. It is important that health professionals report to the addictovigilance center the complications related to the use of PAS in order to reduce the risks and adapt prevention programs.Introduction : L’usage de substances psychoactives (SPA) s’est diversifié depuis plusieurs années, avec une population de consommation hétérogène, et des produits consommés variés. Si le trouble de l'usage et les troubles psychiatriques liés à la consommation sont connus, les complications somatiques le sont moins. Méthode : Nous avons réalisé une revue de la littérature pour analyser le potentiel hépatotoxique des principales SPA, en dehors des complications hépatiques infectieuses liées aux injections. Résultats : Parmi les substances que nous avons étudiées, celles qui sont les plus connues pour être à l’origine d’atteintes hépatiques sont la MDMA (également connue sous le nom d’ecstasy), la cocaïne, le Kratom et le khat. La MDMA et la cocaïne sont des substances de plus en plus consommées en particulier par les jeunes, contrairement au khat et kratom dont la consommation reste plus exceptionnelle en France. Conclusion : les complications somatiques liées à l’usage des SPA participent à leur dangerosité et peuvent avoir une valeur d’alerte. Il est important que les professionnels de santé signalent au centre d’addictovigilance les complications liées à l’usage de SPA afin de réduire les risques et adapter des programmes de prévention

**Решение:** -

---

### 525 · R4174

**Antinociception and physical dependence in mice induced by mitragynine, an indole alkaloid isolated from Thai medicinal plant Mitragyna speciosa**

1998 · The Japanese Journal of Pharmacology · article, journal article, journal-article · en · https://doi.org/10.1016/s0021-5198(19)40733-6

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 526 · R0258

**Mitragynine reduces methamphetamine self-administration in rats without disrupting food-maintained responding.**

2026 · Psychopharmacology · article, journal article, journalarticle · eng · https://doi.org/10.1007/s00213-026-07124-6

Abstract Rationale Kratom ( Mitragyna speciosa ), a plant native to Southeast Asia, has become popular in the United States for its reported ability to treat substance use disorders (SUD). Mitragynine (MG) is the most abundant alkaloid found in kratom. Objectives The present studies evaluated whether MG decreases methamphetamine self-administration under both fixed-ratio (FR) and progressive-ratio (PR) schedules. In a separate cohort we examined whether MG would alter food-maintained responding. Methods Three separate experiments were conducted in male and female adult Sprague–Dawley rats. In Experiment 1, rats self-administered methamphetamine (0.032 mg/kg/infusion, intravenous) under a fixed-ratio (FR) schedule. In Experiment 2, a separate group received food pellets under a FR schedule. In Experiment 3, a different group received methamphetamine (0.032 mg/kg/infusion) under a progressive-ratio (PR) schedule. In all experiments rats received pretreatment with MG (10–56 mg/kg, intraperitoneal) or vehicle 30 min before testing. Behavioral measures included active and inactive lever presses, response rates, and in the case of PR, breakpoints. Results MG dose-dependently reduced methamphetamine delivery under both the FR and PR schedules, with significant decreases in active lever presses, and breakpoints at 32 and 56 mg/kg. Effects were generally comparable in males and females, without significant sex × treatment interaction detected. Conclusions MG decreased methamphetamine-maintained responding at doses that did not affect food-maintained responding, indicating a selective effect on methamphetamine reinforcement relative to natural reward. These findings identify MG as a compound with robust effects on methamphetamine-maintained behavior and support its continued evaluation in preclinical models of methamphetamine use disorder.

**Решение:** -

---

### 527 · R0024

**Oleogels, Bigels, and Emulgels**

2026 · MDPI eBooks · book · en · https://doi.org/10.3390/books978-3-7258-6375-4

Oleogels, Bigels, and Emulgels: Fabrication, Application and Research Trends compiles research and reviews from the Gels journal, highlighting recent advances and current knowledge in the study of different types of gels in the food and cosmetics industries, dentistry, and water management. The main subjects covered in this reprint were the development and evaluation of 3D-printable food systems; investigation of cooling effect on oleogels properties; evaluation of the potential of oleogels as substitutes for solid fats in cookies; investigations of gels for sustained root canal disinfection; development and evaluation of hydrogel and Kratom nanoparticle-loaded gels for skincare systems; investigations into the use of gels in water management; preparation and utilization of bigels in the food industry; and examination of oleogels potential to enhance the textural and sensory qualities of sausages. This reprint is especially recommended for researchers, students, and industry professionals, as it offers new perspectives on the manufacturing and use of gels.

**Решение:** -

---

### 528 · R3846

**Insecticidal and wormicidal plants from Aravalli hill range of India.**

2011 · Journal of ethnopharmacology · journal article · eng · https://doi.org/10.1016/j.jep.2011.04.013

Various plants are being used as ethnomedicines against insects and worms in Aravalli hill range of India. In this study, we are focusing upon intellectual traditional ecological knowledge with an objective of revaluation of ethnomedicinal data processing for the plants being utilized against insects and worms. These plants can be explored for drug discovery program against insects and worms. An ethnobotanical survey was carried out to raise the information on plants against insects and worms from ethnic tribes. The information about the plant part used, dose & mode of administration was collected and verified by interviewing at different times, tribes and places within the study area. 67 remedies with 49 plants species belonging to 29 families are identified and reported with taxonomic description. Mitragyna parvifolia (Roxb.) Korth. is first time reported with ethnomedicinal claims (against insects and worms). These plants may specially be selected for the drug discovery program against insects and worms. Active ingredients from these plants may serve as novel drug molecules. Beside conservation efforts to these plants there is an urgent need to document the ethnomedicinal knowledge. The survey provides a veritable source of information for traditional medical practitioners and medicinal plant researchers and help in developing strategies for future conservation.

**Решение:** -

---

### 529 · R0820

**Mapping and analysis of marketing communication of selected kratom distributors**

2025 · Digital Repository (National Repository of Grey Literature) · dissertation, thesis · cs · https://core.ac.uk/download/651300433.pdf

Background: Kratom is a natural substance with psychoactive effects similar to some opioids. Kratom use is becoming more common in the Czech population, particularly among adolescents. Kratom is often classified as a "collectible" on the Czech market and its distribution and marketing are not regulated. There are efforts to regulate the market internally by kratom vendors, but the marketing promotion of kratom remains unregulated. Marketing communication by kratom vendors has not been mapped in the Czech Republic yet. Aims: The main aim of the research was to analyse the marketing communication of kratom in selected communication channels: e-shop website, advertisement on the Internet, newsletter and product packaging. The secondary aim was to map the promotion of kratom in selected retail stores, convenience stores and vending machines in Prague. Methods: The research set consisted of communication channels of 30 selected kratom distributors. Selected communication channels were analysed: e-shop websites, advertising areas on the Internet, newsletters and direct sales points of kratom. The data was collected from April to October 2024. Promotional material was analysed under the following categories: visual audit, verbal audit, thematic analysis, sales promotion methods, contact point analysis,...Východiska: Kratom je přírodní látka s psychoaktivními účinky podobnými některým opioidům. Míra užívání kratomu v české populaci se zvyšuje, a to zejména mezi mladistvými. Kratom bývá na českém trhu řazen do kategorie "sběratelský předmět," jeho distribuce a marketing nejsou regulovány. Objevuje se snaha o interní regulaci trhu ze strany distributorů kratomu, marketingová propagace kratomu však nadále zůstává neregulována. Marketingová komunikace distributorů kratomu dosud v ČR nebyla zmapována. Cíle: Hlavním cílem výzkumu bylo analyzovat marketingovou komunikaci kratomu ve vybraných komunikačních kanálech: webové stránky e-shopu, inzertní plochy na internetu, newsletter a obal produktu. Sekundárním cílem bylo mapovat propagaci kratomu ve vybraných kamenných prodejnách, večerkách a prodejních automatech na území Prahy. Metody: Marketingová komunikace distributorů kratomu byla analyzována metodou kvalitativní obsahové analýzy. Výzkumný soubor tvořily komunikační kanály vybraných 30 distributorů kratomu. Analýzovány byly vybrané komunikační kanály: webové stránky e-shopu, inzertní plochy na internetu, newsletter a místa přímého prodeje kratomu. Sběr dat probíhal od dubna do října 2024. Propagační materiál byl analyzován v kategoriích: vizuální audit, verbální audit, tematická analýza, metody podpory...Klinika adiktologie 1. LF UK a VFNDepartment of Addictology First Faculty of Medicine Charles University and General University Hospital in Prague1. lékařská fakultaFirst Faculty of Medicin

**Решение:** -

---

### 530 · R2613

**LEGALITAS PENYITAAN TERHADAP DAUN KRATOM YANG BELUM DILARANG OLEH UNDANG-UNDANG NARKOTIKA**

2020 · JLR - Jurnal Legal Reasoning · article, journalarticle, journal-article · id · https://doi.org/10.35814/jlr.v3i1.2229

Kratom merupakan tanaman yang mengandung alkaloid mitragynine yang dalam dosis tinggi, sehingga mengakibatkan efek 13 kali lebih kuat dari morfin, dapat menimbulkan adiksi, depresi, gangguan pernapasan hingga kematian. UNODC pada tahun 2013, menggolongkan kratom sebagai New Psychoactive Subtances, kemudian Badan Pengawas Obat dan Makanan mengeluarkan Surat Edaran Nomor tahun 2016 tentang Pelarangan Penggunaan Mitraguna Speciosa (kratom) dalam Obat Tradisional dan Suplemen Makanan yang kemudian didukung oleh Badan Narkotika Nasional dengan menetapkan 5 tahun (2017-2022) masa transisi terhadap masyarakat yang masih memperjualbelikan dan menggunakan daun kratom agar bisa menyesuaikan terhadap larangan daun kratom pada tahun 2022. Artinya daun kratom masih belum dilarang hingga 2022. Tetapi pada 14 oktober 2019 kepolisian Resor Palangka Raya melakukan penyitaan terhadap 12 ton daun kratom kering. Penelitian ini berusaha meneliti legalitas penyitaan 12 ton daun kratom yang dilakukan Polres Palangka Raya dan mencari tahu dapatkah kepolisian melakukan penyitaan terhadap benda yang tidak terikat suatu tindak pidana. Penelitian ini menggunakan metode penelitian yuridis normative, mengumpulkan data-data sekunder dengan menggunakan studi kepustakaan dan diteliti dengan pendekatan wacana. Hasil penelitian ini adalah kepolisian tidak dapat melakukan penyitaan terhadap benda yang tidak terikat oleh suatu tindak pidana. Sehingga penyitaan yang dilakukan oleh kepolisian resor palangkaraya merupakan perbuatan yang melanggar asas legalitas. Karena hingga saat ini belum ada aturan yang mengatur secara jelas dan rinci mengenai penyalahgunaan dan peredaran daun kratom.

**Решение:** -

---

### 531 · R3759

**Mixture Models for Estimating the Number of Drug Users in Thailand 2005-2007**

2013 · Applied Mathematics · article, review · en · https://doi.org/10.4236/am.2013.49168

It is difficult to measure the sizes of illegal drug user populations directly by using the survey method because of many “hidden drug addicts” and the difficulty of receiving a true response. Systematic and routine information on treatment episodes of drug users is adopted to estimate the population size in this study. Mixture models of zero-truncated Poisson distributions using the nonparametric maximum likelihood estimators (NPMLE) by means of capture-recapture repeated count data were used to project the number of drug users. The method was applied to surveillance data of drug users identified by treatment episodes in over 1140 health treatment centers in Thailand from the Bureau of Health Service System Development, Ministry of Public Health. We presented how this mixture model could be utilized to construct the unobserved frequency of drug users with no treatment episode and further estimated the total population size of drug users in the country from 2005 to 2007. The result of simulation was confirmed that mixture model is suitable when population is large. By means of mixture models, the estimations for the number of drug users were fitted with excellent goodness-of-fit values and we were also compared to the conventional Chao estimates. The NPMLE for the total number of drug users in Thailand 2005, 2006, and 2007 were 184,045 (95% CI: 181,297-86,793), 230,665 (95% CI: 226,611-234,719), 299,670 (95% CI: 294,217-305,123), respectively, also 125,265 (95% CI: 123,092-127,142), 166,287 (95% CI: 163,222-169,352), 228,898 (95% CI: 224,766 - 233,030) for the number of methamphetamine (Yaba) users, and 11,559 (95% CI: 10,234-12,884), 11,333 (95% CI: 9276-13,390), 8953 (95% CI: 7878-10,028) for the number of heroin users, respectively. The numbers of marijuana, kratom-plant, opium, and inhalant users were underestimated because their symptoms were mild and not severe enough to remedy in health treatment centers which led to the smaller size of the total number of drug users. The well-estimated sizes of heroin and methamphetamine addicts are high reliable because they are based on clearly evident count with a severe addiction problem to health treatment centers. The estimation by means of mixture models can be recommended to monitor drug demand trend and drug health service routinely; it is easy to calculate via the available programs MIXTP based on request.

**Решение:** -

---

### 532 · R2754

**Time to treatment initiation and retrospective analysis of antiretroviral therapy outcomes among hiv-positive methadone maintenance therapy clients in primary health-care centers, Kuantan, Pahang**

2020 · Journal of Pharmacy and Bioallied Sciences · article · https://doi.org/10.4103/jpbs.jpbs_3_20

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 533 · R3125

**Pharmacokinetic modeling of single dose Kratom (mitragynine) in rats**

2018 · Frontiers in Pharmacology · article, journal article, journal-article · de · https://doi.org/10.3389/conf.fphar.2018.63.00087

Event Abstract Back to Event Pharmacokinetic modeling of single dose Kratom (mitragynine) in rats Yuvenesan Jagabalan1, Hadzliana Zainal1*, Ammar Imad Hazim Al Ganaby2, Vikneswaran Murugaiyah1 and Surash Ramanathan2 1 School of Pharmaceutical Sciences, University of Science Malaysia, Malaysia 2 Center for drug research, University of Science, Malaysia, Malaysia Background Mitragynine the principal alkaloid of M. speciosa leaf has been reported to be responsible for most of its pharmacological effects. Earlier studies have reported the pharmacokinetic properties of mitragynine (MG) following single oral dose administration. However, the selection of MG doses employed in these studies was derived empirically without proper scientific basis. In view of this, the present study was undertaken to determine MG dose-proportionality properties after repeated oral administration in rats. Methods In this study, eighteen rats were randomly assigned into three experimental groups (n = 6, each). The first group rats were orally treated with a single dose of 20 mg/kg MG. The second group was given a single oral dose of 40 mg/kg MG whereas the third group of rats received the 80 mg/kg MG dose orally. Blood was collected from the tail vein before the dosing and thereafter at specific time-points after drug administration. Blood samples were centrifuged and separated plasma samples were frozen prior to analysis using HPLC. Results The pharmacokinetics was best described by two-compartment distribution models with first order absorption. Estimated typical clearance (CL/F) value was 2.21 L.h-1 , absorption rate (Ka) of of 0.82 h-1 and volume of distribution (Vd) of 30.8 L. The stability of the model and predicted performance were confirmed by bootstrap method and numerical predictive check. Conclusion Based on the single dosing experimental rat data, the model provides a useful tool to quantify the pharmacokinetic parameters to propose an optimal dosing regimen in rats. Subsequently, the pharmacokinetic parameter can be modeled to the pharmacodynamics of MG for extrapolation into human use. Keywords: mitragynine, single dosing study, Two-compartment, Pharmacodynamic (PD), pharmacokinetic Conference: International Conference on Drug Discovery and Translational Medicine 2018 (ICDDTM '18) “Seizing Opportunities and Addressing Challenges of Precision Medicine”, Putrajaya, Malaysia, 3 Dec - 5 Feb, 2019. Presentation Type: Poster Presentation Topic: Miscellaneous Citation: Jagabalan Y, Zainal H, Al Ganaby A, Murugaiyah V and Ramanathan S (2019). Pharmacokinetic modeling of single dose Kratom (mitragynine) in rats. Front. Pharmacol. Conference Abstract: International Conference on Drug Discovery and Translational Medicine 2018 (ICDDTM '18) “Seizing Opportunities and Addressing Challenges of Precision Medicine”. doi: 10.3389/conf.fphar.2018.63.00087 Copyright: The abstracts in this collection have not been subject to any Frontiers peer review or checks, and are not endorsed by Frontiers. They are made available through the Frontiers publishing platform as a service to conference organizers and presenters. The copyright in the individual abstracts is owned by the author of each abstract or his/her employer unless otherwise stated. Each abstract, as well as the collection of abstracts, are published under a Creative Commons CC-BY 4.0 (attribution) licence (https://creativecommons.org/licenses/by/4.0/) and may thus be reproduced, translated, adapted and be the subject of derivative works provided the authors and Frontiers are attributed. For Frontiers’ terms and conditions please see https://www.frontiersin.org/legal/terms-and-conditions. Received: 10 Oct 2018; Published Online: 17 Jan 2019. * Correspondence: PhD. Hadzliana Zainal, School of Pharmaceutical Sciences, University of Science Malaysia, Penang, 11700, Malaysia, hadz@usm.my Login Required This action requires you to be registered with Frontiers and logged in. To register or login click here. Abstract Info Abstract The Authors in Frontiers Yuvenesan Jagabalan Hadzliana Zainal Ammar Imad Hazim Al Ganaby Vikneswaran Murugaiyah Surash Ramanathan Google Yuvenesan Jagabalan Hadzliana Zainal Ammar Imad Hazim Al Ganaby Vikneswaran Murugaiyah Surash Ramanathan Google Scholar Yuvenesan Jagabalan Hadzliana Zainal Ammar Imad Hazim Al Ganaby Vikneswaran Murugaiyah Surash Ramanathan PubMed Yuvenesan Jagabalan Hadzliana Zainal Ammar Imad Hazim Al Ganaby Vikneswaran Murugaiyah Surash Ramanathan Related Article in Frontiers Google Scholar PubMed Abstract Close Back to top Javascript is disabled. Please enable Javascript in your browser settings in order to see all the content on this page.

**Решение:** -

---

### 534 · R0240

**Mitragynine reduces symptoms of alcohol use disorder (and tinnitus) in a self-medication of rodents**

2026 · bioRxiv · preprint, posted-content · en · https://doi.org/10.64898/2026.11.19.767795

Alcohol use disorder (AUD) is a major psychiatric disease. Available pharmacotherapies show rather modest compliance and efficacy. Tinnitus is a highly aversive hearing problem, that may arise from the same unsolved problems as AUD. Based on a patient report of Kratom, a Southeast Asian plant preparation, efficacy in the self-medication of AUD and tinnitus, we tested the main active Kratom alkaloid, mitragynine, for its therapeutic action in AUD mouse models covering various symptoms of the disease. We found that experimenter administered mitragynine (i.p.) inhibits well-established ongoing alcohol consumption in a social setting when alcohol is permanently available. Mitragynine also inhibits alcohol consumption in a non-social, isolated setting. While mitragynine did not work for prophylaxis during abstinence, it markedly attenuated the relapse to binge drinking with alcohol availability restricted to a limited time. Furthermore, mitragynine reduced alcohol seeking behaviour during its establishment as well as during retrieval from memory. It was also effective to attenuate its re-establishment after extinction. We found significant antidepressive effects of mitragynine, during alcohol withdrawal. To address the compliance problem for pharmacotherapies, we established a test that can monitor this and found that mice after a short training, learned to orally self-administer mitragynine hydrochloride leading to a strong reduction in voluntary alcohol drinking. In parallel, mitragynine reduced tinnitus after a noise trauma in a gerbil model. Together, these findings suggest that mitragynine may be used as a pharmacotherapy for AUD and tinnitus with an expected high compliance rate.

**Решение:** -

---

### 535 · R3373

**Quantitative and Qualitative Analysis of Mitragynine in Kratom (Mitragyna Speciosa) by GC-MS, LC-MS/MS and UPLC-PDA**

2016 · Journal of Regulatory Science · article, other literature type, journalarticle · en · https://doi.org/10.21423/jrs-v03n02p001

In 2011, emergency rooms on theWest Coast had patients showing up with opiate/heroin withdrawal symptoms from Kratom. Mitragyna speciosa, or Korth (Thai name Kratom; Rubiaceae) is a medical plant native to Thailand and other Southeast Asian countries and is presently illegal in Thailand and other European countries [1]. In the United States, Kratom is readily available via the internet and local retail stores.The leaves of Mitragyna speciosa consist of two primary active alkaloids: Mitragynine 66.2%, and 7 -hydroxy-7H-mitragynine 2.0%, and three indole alkaloids: Paynantheine 8.6%, Speciogynine 6.6%, and Speciociliatine 0.8%. Since mitragynine is one of the major constituent of Kratom, mitragynine is used as the marker compound for the identification and quantitation of Kratom in a variety of products.This study describes methodology for the qualitative identification and quantitation of Kratom in dierent types of products such as but not limited to: powders, liquids, and spent-leaf materials. A quick methanolic based extraction procedure was used in combination with two instrument techniques: 1) GC/MS and/or LC-MS/MS for the initial screening and spectral confirmation of mitragynine in Kratom and quantitation via UPLC/PAD; 2) LC-MS/MS. Two dierent mass spectrometry systems were employed for confirmation/quantitation to permit flexibility within the regulatory laboratory for sample analysis.A mitragynine solvent standard was used for the comparative identification of Kratom and quantitation was reported based on the level of mitragynine in the product tested. Due to the low concentration of the mitragynine stock standard (100 mug/mL) and the high level of mitragynine in the products tested, traditional spiking of the standard via a wet/dry spike into a negative control was not feasible. Solvent based calibrationcurves were used for the quantitation of mitragynine in Kratom by UPLC/PDA and LC-MS/MS. Validation was performed by characterizing a Kratom product purchased via the internet. This positive control was extracted seven times over three days and analyzed by all three analytical techniques: GC/MS, LC-MS/MS and UPLC/PDA. The UPLC/PDA data demonstrated a mean value of 1.041% (n=21, 4.2%) and the LC-MS/MS 1.140% (n=14, 6.81%) for mitragynine in the positive control. This positive control was extracted and analyzed in duplicate with every analytical batch.https://doi.org/10.21423/jrs-v03n02p001 (DOI assigned 8/7/2019)

**Решение:** -

---

### 536 · R3745

**Pattern and consequences of krathom (Mitragyna speciosa Korth.) use among male villagers in southern Thailand: a qualitative study.**

2013 · The International journal on drug policy · article, journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1016/j.drugpo.2012.09.004

Background Krathom is currently the most popular illicit substance in use in southern Thailand. Research regarding its effects and health impacts is scarce. This study explored the pattern of krathom use and users' perceptions of the consequences of its use. Methods An in-depth qualitative interview. A group of 34 self-identified regular users, occasional users, non-users and ex-users of krathom was used in this study. Health volunteer as a key-contact person helped the researcher to invite villagers to participate in the study using snowballing technique. The process of data analysis was guided by Strauss and Corbin's grounded theory. Results The core category, 'Understanding krathom use', was generated from three inter-related categories: (i) reasons for continuing krathom use, (ii) the way of applying krathom, and (iii) perceiving positive and realizing the negative effects of krathom use and their 18 subcategories. Conclusions The study findings reveal the importance of considering krathom use from the perspective and belief of the villagers. Krathom is addictive with its own characteristic symptoms and signs. The results provide support for policy interventions to control the availability of krathom according to the community context. In addition, krathom misuse by adolescents must be considered.

**Решение:** -

---

### 537 · R2896

**Kratom Linked to Seizures, Altered Heart Rhythms**

2019 · Psychiatric News · article, other literature type, journal article · en · https://doi.org/10.1176/appi.pn.2019.5a2

Back to table of contents Previous article Next article Clinical and Research NewsFull AccessKratom Linked to Seizures, Altered Heart RhythmsTerri D’ArrigoTerri D’ArrigoSearch for more papers by this authorPublished Online:30 Apr 2019https://doi.org/10.1176/appi.pn.2019.5a2AbstractIn recent years, there has been a jump in calls to poison control centers as kratom’s popularity grows, with nearly a third of kratom exposures resulting in admission to a health care facility.Kratom, a plant touted as a “natural opiate” and available legally in most parts of the United States, has gained popularity in recent years for its alleged ability to help with pain and the symptoms of opioid withdrawal. But those who use it may be taking a serious risk with their health, suggests a study in Clinical Toxicology.“Taking kratom in addition to SSRIs may be like double dosing.” —Henry A. Spiller, M.S., D.A.B.A.T.Researchers who analyzed data from the National Poison Data System (NPDS) found that there were 1,807 kratom-related calls to U.S. poison control centers between 2011 and 2017, with 65% occurring in 2016 and 2017. Nearly a third of kratom exposures resulted in admission to a health care facility, and 11 deaths were associated with kratom use.About 65% of the calls were regarding people who had taken kratom only. Among these single-substance exposures, 51.9% resulted in serious medical outcomes such as seizures, respiratory depression, coma, liver problems, bradycardia (slowed heart rate), and cardiac arrest. Other common side effects were agitation and irritability, tachycardia (fast heart rate), and high blood pressure. Five of the calls were for infants experiencing withdrawal after exposure to kratom in utero. The results suggest that kratom is not the benign supplement its promoters claim it to be, and it does not act like a typical opioid, said study researcher Henry A. Spiller, M.S., D.A.B.A.T., director of the Central Ohio Poison Center and an assistant professor at the Ohio State University College of Medicine.CDC, FDA Warn of Kratom’s DangersNearly 100 Americans in 27 states died of kratom overdose between July 2016 and December 2017, according to research published in the April 12 edition of the Centers for Disease Control and Prevention’s Morbidity and Mortality Weekly Report.Researchers studied data about overdose deaths entered into the State Unintentional Drug Overdose Reporting System and found that toxicology reports for 152 of those who died were positive for kratom. Furthermore, medical examiners or coroners noted kratom as a cause of death in 91 of these cases. Approximately 80% of those who died had a history of substance use, and approximately 90% had no evidence that they were currently receiving medically supervised treatment for pain.Also in April, the Food and Drug Administration released the results of laboratory testing that found heavy metals in approximately 30 kratom products and warned that long-term kratom users could potentially develop heavy metal poisoning, which could include nervous system or kidney damage, anemia, high blood pressure, or increased risk of certain cancers.“Notes From the Field: Unintentional Drug Overdose Deaths With Kratom Detected—27 States, July 2016–December 2017” can be accessed here here. “Laboratory Analysis of Kratom Products for Heavy Metals” is available here.“What we found, especially with adverse events like tachycardia and hypertension, is that it’s more like tramadol, for which one mechanism of action is serotonin and norepinephrine reuptake inhibition. That’s why you see the agitation and the seizures,” Spiller said. Spiller added that kratom works like an opioid only at higher doses, when it can cause respiratory depression.“We’re not the DEA [Drug Enforcement Administration], but people need to know there are risks to this,” Spiller added. “Natural doesn’t necessarily mean safe. Just because kratom is a plant, that doesn’t mean it can’t have adverse effects.”Petros Levounis, M.D., M.A., an addiction psychiatrist who has treated people who use kratom, said that kratom overdose may be difficult to treat.“Because of kratom’s complex neurotransmitter profile, naloxone may not be as effective in reversing an overdose,” said Levounis, who is a professor and chair of the Department of Psychiatry at Rutgers New Jersey Medical School.Spiller noted a second challenge to kratom’s neurotransmitter profile. “We don’t know how many people [currently] taking kratom are taking other things like SSRIs [selective serotonin reuptake inhibitors]. If they are taking SSRIs, taking kratom may be like double dosing,” Spiller said.In their study, Spiller and his coauthors called for more government oversight of kratom.“The high proportions of [health care facility] admissions and serious medical outcomes highlight the need for kratom regulation by the FDA [Food and Drug Administration] to ensure quality and safety, as well as the need for more research on the effects of kratom in humans,” they wrote.Naloxone may not be as effective in reversing kratom overdose as it is for other opioid overdoses because of kratom’s neurotransmitter profile, says Petros Levounis, M.D., M.A.The DEA is considering listing kratom as a Schedule I drug on par with heroin or LSD, a move recommended by the Department of Health and Human Services but met with public outcry. Listing kratom as Schedule I would pose problems for research because those wishing to study it would have to register and obtain approval through the DEA, Levounis said.“The debate about research has been around for a while. Schedule I exists to protect people from something dangerous, but the other side is that it limits access for research on it,” Levounis said. “If kratom does have some medical promise, then it should go through classic FDA approval pathways. Like cannabis, we’re far from having confidence for recommending this to patients before the research has completed its course.”The American Association of Poison Control Centers provided the NPDS data for the study. ■“Kratom Exposures Reported to United States Poison Control Centers: 2011–2017” can be accessed here. ISSUES NewArchived

**Решение:** -

---

### 538 · R2395

**Living Systematic Review on Cannabis and Other Plant-Based Treatments for Chronic Pain: May 2021 Update**

2021 · Agency for Healthcare Research and Quality (AHRQ) · other literature type, report, review · en · https://doi.org/10.23970/ahrqepccerplantpain3

Overview This is the third quarterly progress report for an ongoing living systematic review on cannabis and other plant-based treatments for chronic pain. The first progress report was published in January 2021 and the second in March 2021. The draft systematic review was available for public comment from May 19 through June 15, 2021, on the Agency for Healthcare Research and Quality (AHRQ) Effective Health Care website. The systematic review synthesizes evidence on the benefits and harms of plant-based compounds (PBCs), such as cannabinoids and kratom, used to treat chronic pain, addressing concerns about severe adverse effects, abuse, misuse, dependence, and addiction. The purpose of this progress report is to describe the cumulative literature identified thus far. This report will be periodically updated with new studies as they are published and identified, culminating in an annual systematic review that provides a synthesis of the accumulated evidence. Main Points In patients with chronic (mainly neuropathic) pain with short-term treatment (4 weeks to &lt;6 months): • Studies of cannabis-related products were grouped based on their tetrahydrocannabinol (THC) to cannabidiol (CBD) ratio using the following categories: high THC to CBD, comparable THC to CBD, and low THC to CBD. • Comparable THC to CBD ratio oral spray is probably associated with small improvements in pain severity and may be associated with small improvements in function. There was no effect in pain interference or serious adverse events. There may be a large increased risk of dizziness and sedation, and a moderate increased risk of nausea. • Synthetic THC (high THC to CBD) may be associated with moderate improvement in pain severity and increased risk of sedation, and large increased risk of nausea. Synthetic THC is probably associated with a large increased risk of dizziness. • Extracted whole-plant high THC to CBD ratio products may be associated with large increases in risk of withdrawal due to adverse events and dizziness. • Evidence on whole-plant cannabis, low THC to CBD ratio products (topical CBD), other cannabinoids (cannabidivarin), and comparisons with other active interventions was insufficient to draw conclusions. • Other key adverse event outcomes (psychosis, cannabis use disorder, cognitive deficits) and outcomes on the impact on opioid use were not reported. • No evidence on other plant-based compounds, such as kratom, met criteria for this review.

**Решение:** -

---

### 539 · R2431

**The Protective Effect of Kratom (Mitragyna speciosa Korth.) Leaves Extract on Pancreas of Mice Exposed to Alcoholic Drinks**

2021 · Tropical Journal of Natural Product Research · article, journal article, journal-article · en · https://doi.org/10.26538/tjnpr/v5i7.11

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 540 · R0461

**Abstract TU271: Sleep Duration and Mental Health Among Women: Evidence from the SAFE HEART Study Supporting Life’s Essential 8**

2026 · Circulation · article · eng · https://doi.org/10.1161/cir.153.suppl_1.tu271

Background: Sleep, a key component of the American Heart Association’s Life’s Essential 8 (LE8), influences both cardiovascular and mental health. However, its relationship with stress, depression, and anxiety among women remains uncertain. Objective: Examine associations between subjective sleep duration and mental health outcomes in adult women. Hypothesis: We hypothesized that both short and long sleep would be linked to poorer mental health. Methods: We conducted a cross-sectional analysis of 711 women aged ≥18 years enrolled in the SAFE HEART Study. Participants were recruited from community sites in Baltimore and Washington Counties (MD) and through the American Heart Association’s Research Goes Red registry. Sleep duration was categorized as short (&lt;7 h), optimal (7–9 h), or long (≥9 h). Mental health was assessed using the Perceived Stress Scale (PSS-4), Patient Health Questionnaire (PHQ-2), and Generalized Anxiety Disorder scale (GAD-2). Logistic regression models estimated odds ratios (ORs) and 95% confidence intervals (CIs) using optimal sleep as referent: Model A unadjusted; Model B adjusted for sociodemographic factors (age, race, education, employment, marital status); Model C further adjusted for cardiovascular risk factors (smoking, physical inactivity, hypertension, diabetes, obesity). Results: Among 711 participants (mean age 40.2 ± 14.9 years), 29% were Black, 47.8% White, and 18.6% Hispanic. Over one-third reported short sleep (37.9%), 55.1% optimal, and 7.0% long sleep. Women with short or long sleep were more likely to have lower education, be unmarried or unemployed, and exhibit higher physical inactivity, smoking, hypertension, high cholesterol, and diabetes (all p &lt; 0.05). Overall, 73.8% had high perceived stress, 20.0% screened positive for depression, and 25.9% for anxiety. Long sleep (≥9 h) was associated with higher odds of depression in unadjusted models (OR 3.99; 95% CI 2.16–7.37) and showed borderline, non-significant association after full adjustment (OR 2.02; p = 0.06). It was also related to greater anxiety risk in unadjusted analyses (OR 2.21, 95% CI 1.20–4.07), though this attenuated after adjustment. While not statistically significant, the consistency and magnitude of these findings suggest that longer sleep may be linked to poorer mental health. Short sleep (&lt;7 h) was not associated with stress, depression, or anxiety. Conclusion: Longer sleep may signal poorer mental health, emphasizing sleep's role in women's CVH.

**Решение:** -

---

### 541 · R1756

**Increasing prevalence of designer benzodiazepines in impaired driving: A 5-year analysis from 2017 to 2021**

2023 · Journal of Analytical Toxicology · article · https://doi.org/10.1093/jat/bkad036

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 542 · R1882

**Mitragyna speciosa overdose: Exacerbation of Fanconi syndrome following Mitragyna speciosa abuse: case report**

2022 · Reactions Weekly · article, journal article, journal-article · en · https://doi.org/10.1007/s40278-022-22676-x

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 543 · R2770

**Kratom use in the United States: Response to Grundmann et al .**

2020 · Addiction · article, letter, comment · eng · https://doi.org/10.1111/add.15170

We thank Grundmann et al. for their comments [1]. As pointed out, the cross-sectional study design is not intended to infer a causal relationship between kratom use and substance use disorders or risks of drug abuse [2]. Our study found that 21% of kratom users self-report behaviors classified as substantial or severe on the Drug Abuse Screening Test (DAST-10), a validated tool to assess these behaviors. Grundmann et al. accurately characterize prior studies as finding that a subset of kratom users report their reason for use as self-treatment of opioid drug dependence; however, the authors erroneously suggest that these reports are inconsistent with our finding of high DAST-10 scores in a portion of users. Reasons for use and general drug abuse behaviors are distinct, and while investigating reasons for kratom use is invaluable, it does not necessarily predict drug abuse behaviors. A survey by Garcia-Romeu et al. found that < 3% of users met moderate or severe DSM-5 criteria for kratom-related substance use disorder; however, as stated in the article's limitations, recruitment through websites of interest to kratom users probably resulted in selection bias that emphasized users ‘positively inclined towards kratom’ [3]. These results differ significantly from ours, but given the different drug abuse assessment scales and sampling methods, the prevalence of substance abuse behaviors and substance use disorders among kratom users requires further study. Grundmann et al. incorrectly characterize our survey as sampling only non-medical users. The Non-Medical Use of Prescription Drugs (NMURx) program samples the population of adults aged 18 years and older in the United States. Further, it is incorrect to suggest that prior surveys on websites frequented by kratom users are capable of estimating use in a general population, particularly in the absence of statistical controls. Estimates of prevalence must use appropriate sampling methods and statistical adjustments to account for non-probabilistic elements of on-line recruitment. The NMURx program has shown results congruent with national probability surveys [4]. Estimates of national prevalence by additional survey programs will further illuminate kratom's popularity. We strongly agree that further studies are warranted to clarify potential benefits and risks of use. Discourse is crucial regarding kratom's potential efficacy as a harm reduction drug and the decision for federal scheduling, but it is important to recognize that this discussion is currently based on retrospective and cross-sectional data. Furthermore, much of the current data were funded or obtained by the American Kratom Association, a group advocating for continued unrestricted access. Our article did not address possible safety profile differences between kratom and classical opioids. Rather, our intent was to provide the first estimates of prevalence at the national level, contextualized with additional data on demographics and drug abuse profiles, to further inform the national discussion. None.

**Решение:** -

---

### 544 · R1816

**Kratom ( Mitragyna speciosa ): Pharmacology and Use of a Naturally Occurring Atypical Opioid**

2023 · Oxford University Press eBooks · book chapter, part of book or chapter of book, book-chapter · en · https://doi.org/10.1093/oxfordhb/9780197618431.013.15

Abstract Kratom (Mitragyna speciosa) is a tree in the coffee family, indigenous to Southeast Asia (SEA), whose leaves have historically been used as a natural remedy and for its purported stimulating and analgesic properties. Kratom has gained popularity in recent years in the United States, where internet-based sales have driven growing numbers of people to experiment with kratom products. Kratom contains over 40 unique alkaloids displaying complex pharmacological properties including opioid- and non-opioid-receptor mediated effects. Data from animal research indicates therapeutic potential of kratom; for instance, as an analgesic agent or in mitigating opioid and alcohol withdrawal symptoms. Some adverse effects and risks are also attributable to kratom and its alkaloids, including possible liver damage and potential for dependence, particularly in the context of high dosage and/or chronic administration. However, in comparison to commonly used opioid medications, these risks are generally lower for kratom, consistent with human observational data from SEA and the US. Prevalence of kratom use remains difficult to conclusively assess, with estimates ranging between 1.8 to 15.6 million kratom-using adults in the US alone. The limited human data, comprised of survey and case report, suggest kratom may be effective for pain relief, to address mood and anxiety symptoms, and as a potential future aid in the treatment of substance use disorders and drug withdrawal. Overall, limited data indicate kratom and its alkaloids warrant a significant investment of rigorous basic and clinical research to better characterize its pharmacology, potential risks, and therapeutic benefits.

**Решение:** -

---

### 545 · R1164

**Acute Liver Injury and Kratom Use: A Case Report**

2024 · Elsevier BV · posted-content · https://doi.org/10.2139/ssrn.4965127

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 546 · R2656

**G protein-biased kratom-alkaloids and synthetic carfentanil-amide opioids as potential treatments for alcohol use disorder.**

2020 · British journal of pharmacology · article, journal article, research support, n.i.h., extramural · eng · https://doi.org/10.1111/bph.14913

BACKGROUND AND PURPOSE: Mitragyna speciosa, more commonly known as kratom, is a plant that contains opioidergic alkaloids but is unregulated in most countries. Kratom is used in the self-medication of chronic pain and to reduce illicit and prescription opioid dependence. Kratom may be less dangerous than typical opioids because of the stronger preference of kratom alkaloids to induce receptor interaction with G proteins over β-arrestin proteins. We hypothesized that kratom (alkaloids) can also reduce alcohol intake. EXPERIMENTAL APPROACH: We pharmacologically characterized kratom extracts, kratom alkaloids (mitragynine, 7-hydroxymitragynine, paynantheine, and speciogynine) and synthetic carfentanil-amide opioids for their ability to interact with G proteins and β-arrestin at μ, δ, and κ opioid receptors in vitro. We used C57BL/6 mice to assess to which degree these opioids could reduce alcohol intake and whether they had rewarding properties. KEY RESULTS: Kratom alkaloids were strongly G protein-biased at all three opioid receptors and reduced alcohol intake, but kratom and 7-hydroxymitragynine were rewarding. Several results indicated a key role for δ opioid receptors, including that the synthetic carfentanil-amide opioid MP102-a G protein-biased agonist with modest selectivity for δ opioid receptors-reduced alcohol intake, whereas the G protein-biased μ opioid agonist TRV130 did not. CONCLUSION AND IMPLICATIONS: Our results suggest that kratom extracts can decrease alcohol intake but still carry significant risk upon prolonged use. Development of more δ opioid-selective synthetic opioids may provide a safer option than kratom to treat alcohol use disorder with fewer side effects.

**Решение:** -

---

### 547 · R0787

**From Kratom to Semi-Synthetic Opioids: The Rise and Risks of MGM-15.**

2025 · Drug testing and analysis · article, journal article, journalarticle · eng · https://doi.org/10.1002/dta.3952

ABSTRACT Kratom ( Mitragyna speciosa ), a plant native to Southeast Asia, has long been used for its stimulant and analgesic properties. 7‐Hydroxymitragynine (7‐HMG) is a potent and selective opioid agonist in vitro and demonstrates a potent opioid effect in living subjects, reversible by naloxone. It has been semi‐synthesized into products that are readily available in retail and virtual shops. It is known that 7‐HMG has earned the nickname “legal morphine,” and has gained popularity among users seeking pain relief and/or a “high” comparable with prescription opioids. Medicinal chemistry efforts have led to synthetic 7‐HMG derivatives such as MGM‐15, where stereospecific saturation of the imine N(1)–C(2) double bond increases opioid receptor affinity and activity. Despite its higher in vitro opioid potency, MGM‐15 is currently sold in the US for human consumption as a “research chemical” in tablet form, even though there is an absence of this being studied in humans and obviously no FDA approval. In this study, we analyzed commercially available MGM‐labeled tablets using UPLC–MS/MS and subsequently evaluated the binding affinities of purified MGM‐15 across multiple opioid receptors. Tablets contained an average of 10.9 ± 0.2 mg (10.7 to 11.2 mg) of MGM‐15, with no naturally occurring kratom alkaloids or illicit substances detected. MGM‐15 shows greater hMOR and hDOR binding affinities than 7‐HMG, indicating the potential for higher opioid effects and risks, emphasizing the urgent need for more research to advise regulation and hopefully prevent misuse and harm.

**Решение:** -

---

### 548 · R3592

**Poster #S269 DEXTROMETHORPHAN AND PSYCHIATRIC MORBIDITY: A SINGAPORE PERSPECTIVE**

2014 · Schizophrenia Research · article · en · https://doi.org/10.1016/s0920-9964(14)70548-1

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 549 · R3719

**Mitragyna Speciosa (Kratom)-Induced Cholestatic Hepatitis**

2013 · The American Journal of Gastroenterology · article, journal article, journal-article · en · https://doi.org/10.14309/00000434-201310001-00470

Purpose:Mitragyna speciosa Korth (vernacular name: kratom) is a tall, leafy tree in the family Rubiaceae. Kratom leaves have long been used as a narcotic and central nervous system stimulant. Herein, we report the first case of cholestatic hepatitis due to kratom use. Methods: A 34-year-old female with no significant past medical history was referred for evaluation of her extreme fatigue, pruritus, and jaundice. She was well until two weeks prior, when she started having back aches, for which she took a half-spoon of kratom for two consecutive days. Within a week, she started feeling fatigued, which subsequently worsened, and extreme pruritus ensued. The patient also noticed dark-colored urine and clay-colored stools. She denied any abdominal pain, fever, nausea, vomiting, chills, melena, rashes, confusion, excessive alcohol drinking, recent travel, intravenous drug abuse, or recent antibiotic use. She endorsed taking less than 2 grams of acetaminophen daily for the last three days. On examination, she was oriented to person, place, and time, with scleral icterus and multiple excoriation marks. No stigmata of chronic liver disease were noticed. Abdominal and neurological examinations were unremarkable. Upon presentation, liver biochemistries revealed alanine aminotransferase (ALT) 93 U/L [range: 12-78 U/L], aspartate aminotransferase (AST) 61 U/L [range: 15-37 U/L], alkaline phosphatase (ALP) 298 U/L [range: 50-136 U/L), and total bilirubin: 10.6 mg/dl [range: 0.2- 1.0 mg/dl]. No evidence of coagulopathy was noted. Serological tests for Hepatitis A, B, C, Epstein-Barr virus, cytomegalovirus, and auto immune hepatitis were negative. Her urine toxicology was negative, and alcohol level was normal. Wilson's disease, alpha 1 antitrypsin deficiency, primary biliary cirrhosis, and hemochromatosis were ruled out by appropriate testing. The patient was initially started on N-Acetylcysteine (NAC) protocol for potential acetaminophen toxicity. Abdominal ultrasound and hepatobiliary scan revealed no evidence of common bile duct obstruction. She was started on ursodiol 10 mg/kg/day and hydroxyzine for pruritus. Liver biopsy was preformed, which revealed cholestasis, lobular inflammation, and increased eosinophils within sinusoids, consistent with drug-induced liver injury. Given the absence of coagulopathy or encephalopathy, she was discharged home with follow-up. An appointment 40 days later revealed complete normalization of liver function tests and resolution of clinical symptoms. Conclusion: To our knowledge, this is the first reported case of kratom-induced cholestatic hepatitis. This case highlights the need for physicians to consider widely available substances, especially herbal supplements, when evaluating cholestatic liver injury.

**Решение:** -

---

### 550 · R1964

**Sex- and Dose-Dependent Differences in the Development of an Addiction-Like Phenotype Following Extended-Access Fentanyl Self-Administration**

2022 · Frontiers in Pharmacology · article · und · https://doi.org/10.3389/fphar.2022.841873

Opioid use disorder (OUD) is a major epidemic in the United States, and fentanyl is a major culprit. The National Institute on Drug Abuse has highlighted an urgent need for research on the risks and outcomes of OUD with fentanyl; a better understanding of sex/gender differences is also critically needed given that the opioid epidemic has been particularly impactful on women. In response to this need, we developed a rat model of OUD with fentanyl and showed that sex impacts relapse vulnerability following extended-access self-administration under a low fentanyl dose. Here, our goal was to determine sex differences across a broad dose range, including high doses expected to maximize the expression of addiction-like features (e.g., vulnerability to relapse and physical dependence). Male and female rats were assigned to self-administer one of four fentanyl doses (0.25, 0.75, 1.5, and 3.0 µg/kg/infusion), and once they acquired, they were given extended (24-h/day), intermittent access (2, 5 min trials/h, fixed-ratio 1) to fentanyl for 10 days. Physical dependence (spontaneous weight loss) was assessed during early withdrawal, and relapse vulnerability was assessed on withdrawal day 15 using an extinction/cue-induced reinstatement procedure. Despite markedly higher intake in the high- versus low-dose groups, each group responded similarly during relapse testing (extinction and cue-induced reinstatement). However, number of infusions, or frequency of use, during extended access was predictive of later vulnerability to relapse, whereas total intake impacted physical dependence given that weight loss only occurred following the discontinuation of fentanyl self-administration at the three highest doses. Females self-administered more fentanyl each day and within each binge (active trial), and had longer lasting weight loss during withdrawal than males. Relapse vulnerability was also higher in females than males and highest in females tested during estrus. These findings indicate that sex is an important risk factor for patterns and levels of fentanyl intake, relapse, and physical dependence, and while fentanyl intake predicts physical dependence, frequency of use predicts relapse.

**Решение:** -

---

### 551 · R0734

**The Hidden Perils of Kratom: A Case of Drug-Induced Psychosis Successfully Treated With a Second-Generation Antipsychotic.**

2025 · The primary care companion for CNS disorders · article, journal article, journalarticle · eng · https://doi.org/10.4088/pcc.25cr03935

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 552 · R2407

**Medical Kratom Laws: New Perspective from Thailand**

2021 · Indian Journal of Health and Medical Law · article · en

Kratom is an important tropical plant that has a possible medical usefulness. However, it can cause addiction in the user and classified as a narcotic. Kraom addiction is accepted as an additive substance disorder. Worldwide, kratom is usually controlled by narcotics drug laws. In the present day, the legalization of medical kratom is a new aspect. In Thailand, the medical kratom laws is launched and become the interesting issue for further discussion. In the present article, the authors discuss on the medical kratom, with special focus on the new perspective from Thailand.

**Решение:** -

---

### 553 · R0451

**Safety and Efficacy of Monoamine Oxidase Inhibitors in Patients Who Use Psychoactive Substances: Potential Drug Interactions and Substance Use Disorder Treatment Data**

2026 · CNS Drugs · review · https://doi.org/10.1007/s40263-025-01256-7

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 554 · R1329

**Effects of Itraconazole on Pharmacokinetics of Mitragynine and 7-Hydroxymitragynine in Healthy Volunteers.**

2024 · ACS pharmacology & translational science · article, journal article, journalarticle · eng · https://doi.org/10.1021/acsptsci.3c00335

CYP3A4-mediated metabolic conversion of mitragynine to 7-hydroxymitragynine (7OH) has been demonstrated in human liver microsomes, and in rodents. Pharmacokinetics (PK) of mitragynine and 7OH in humans is still limited. We aimed to examine the pharmacokinetics of mitragynine and the formation of 7OH in healthy volunteers. To elucidate involvement of CYP3A4 in 7OH formation, inhibition by itraconazole was implemented. Two study periods with PK study of mitragynine alone in period 1, followed by period 2 including itraconazole pretreatment was conducted. Freshly prepared kratom tea consisting of 23.6 mg of mitragynine was given to participants in both study periods. Serial blood samplings were performed for 72 hours, and analyzed using a validated LCMS in multiple reaction monitoring mode. The median Cmax for mitragynine of 159.12 ± 8.68 ng/mL was attained in 0.84 h. While median Cmax for 7OH of 12.81 ± 3.39 ng/mL was observed at 1.77 h. In period 1, Cmax and AUC 0-inf of 7OH accounted for 9% and 20 %, respectively, of those parameters for mitragynine. The geometric mean ratio of AUC0-72 for 7OH/mitragynine (metabolic ratio, MR) was 13.25 ± 1.07. Co-administration of itraconazole 200 mg per day orally for 4 days (period 2) decreased 7OH exposure by 56% for Cmax and 43% for AUC0-72 after a single oral dose of kratom tea. While the Cmax of mitragynine increased by 1.5 folds without a significant change in Tmax. The geometric mean metabolic ratio was 3.30 ± 1.23 (period 2), indicating the attenuation for the formation of 7OH by the pretreatment with itraconazole. This suggested the CYP3A4-mediated formation of 7OH from mitragynine in healthy volunteers. This study provides the first evidence of metabolic conversion of mitragynine to 7OH in humans.

**Решение:** -

---

### 555 · R1038

**Exploring the cognitive effects of kratom: A review.**

2025 · Behavioural brain research · article, journal article, review · eng · https://doi.org/10.1016/j.bbr.2024.115387

Despite the strict kratom regulation in some regions, the demand for kratom products is still increasing worldwide. Kratom products are commonly consumed for their pain-relieving effect or as a self-treatment for opioid use disorder. Kratom is also taken as a recreational drug among youth and adults. Since substance abuse can cause cognitive impairment, many studies investigated the effects of kratom on cognition. The interaction of some kratom alkaloids with various receptors such as opioid, serotonergic, and adrenergic receptors further sparks the interest to investigate the effects of kratom on cognitive function. Hence, this review aims to provide an overview of the effects of kratom on cognitive behaviours and their underlying changes in neurobiological mechanisms. In conclusion, kratom, particularly its main alkaloid, mitragynine may adversely affect cognitive performances that may be attributed to the disruption in synaptic plasticity, brain activity as well as various proteins involved in synaptic transmission. The impact of kratom on cognitive functions could also shed light on its safety profile, which is essential for the therapeutic development of kratom, including its potential use in opioid substitution therapy.

**Решение:** -

---

### 556 · R2504

**Case Report: Treatment of Kratom Use Disorder With a Classical Tricyclic Antidepressant.**

2021 · Frontiers in psychiatry · article, case reports, journal article · eng · https://doi.org/10.3389/fpsyt.2021.640218

Kratom or Mitragyna speciosa (Korth.) is an evergreen tree of the coffee family native to South-East Asia and Australasia. It is used by locals recreationally to induce stimulant and sedative effects and medically to soothe pain and opiate withdrawal. Its leaves are smoked, chewed, or infused, or ground to yield powders or extracts for use as liquids. It contains more than 40 alkaloids; among these, mitragynine and 7-hydroxymitragynine are endowed with variable mu, delta, and kappa opioid stimulating properties (with 7-hydroxymitragynine having a more balanced affinity), rhynchophylline, which is a non-competitive NMDA glutamate receptor antagonist, but is present in negligible quantities, and raubasine, which inhibits α 1 -adrenceptors preferentially over α 2 -adrenceptors, while the latter are bound by 7-hydroxymitragynine, while mitragynine counters 5-HT 2A receptors. This complexity of neurochemical mechanisms may account for kratom's sedative-analgesic and stimulant effects. It is commonly held that kratom at low doses is stimulant and at higher doses sedative, but no cut-off has been possible to define. Long-term use of kratom may produce physical and psychological effects that are very similar to its withdrawal syndrome, that is, anxiety, irritability, mood, eating, and sleep disorders, other than physical symptoms resembling opiate withdrawal. Kratom's regulatory status varies across countries; in Italy, both mitragynine and the entire tree and its parts are included among regulated substances. We describe the case of a patient who developed anxiety and dysphoric mood and insomnia while using kratom, with these symptoms persisting after withdrawal. He did not respond to a variety of antidepressant combinations and tramadol for various months, and responded after 1 month of clomipramine. Well-being persisted after discontinuing tramadol.

**Решение:** -

---

### 557 · R1966

**Natural Products for the Treatment of Post-stroke Depression**

2022 · Frontiers in Pharmacology · review · https://doi.org/10.3389/fphar.2022.918531

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 558 · R0435

**Position paper- Semi-synthetic products based on 7-hydroxymitragynine: a public health emergency**

2026 · article · en · https://doi.org/10.13140/rg.2.2.32018.62400

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 559 · R0548

**Increases in Kratom-Related Reports to Poison Centers - National Poison Data System, United States, 2015-2025.**

2026 · MMWR. Morbidity and mortality weekly report · article, journal article, journalarticle · eng · https://doi.org/10.15585/mmwr.mm7511a1

Kratom, the leaves of a tropical evergreen tree (Mitragyna speciosa), is traditionally consumed in Southeast Asia for pain relief, mood enhancement, and to relieve symptoms of opioid withdrawal. Kratom contains psychoactive compounds that interact with opioid receptors and is widely available in various forms in the United States. Its evolution from natural leaf to high-potency alkaloid products has raised concerns about toxicity. Data on kratom-related use that resulted in a report to the National Poison Data System (NPDS) (i.e., kratom exposure report) during 2015-2025 were analyzed to assess trends by exposure report type, demographic characteristics of persons exposed, and outcomes. During the past 11 years, poison centers received a total of 14,449 kratom exposure reports; the record high 3,434 reports in 2025 represent an increase of approximately 1,200% compared with the 258 reports in 2015. Most reports involved males and young adults aged 20-39 years, but reports among adults aged 40-59 years increased most sharply, with rates nearly overlapping with those among young adults by 2025. Although single-substance exposure reports accounted for most reports (62%), multiple-substance reports occurred at higher rates (range = 467-5,442 per 1 million multiple-substance drug exposure reports versus 388-4,045 per 1 million single-substance drug exposure reports), were associated with more hospitalizations (44%-56% versus 24%-29% annually) and serious (life threatening, pronounced, prolonged, or systemic) outcomes (57%-66% versus 41%-49% annually), and accounted for the vast majority of kratom-associated deaths during the study period (184 of 233; 79%). NPDS data indicate that kratom-related reports to poison centers are increasing and expanding among demographic groups, underscoring the value of ongoing surveillance to identify high-risk patterns of kratom use and guide strategies to reduce risks from multiple-substance exposure reports.

**Решение:** -

---

### 560 · R2062

**Kratom (Mitragyna speciosa) Validation: Quantitative Analysis of Indole and Oxindole Alkaloids Reveals Chemotypes of Plants and Products.**

2022 · Planta medica · article, journal article, journal-article · eng · https://doi.org/10.1055/a-1795-5876

Abstract Many consumers are turning to kratom (Mitragyna speciosa) to self-manage pain and opioid addiction. In the United States, an array of capsules, powders, and loose-leaf kratom products are readily available. Additionally, several online sites supply live kratom plants. A prerequisite to establishing quality control and quality assurance standards for the kratom industry, or understanding how alkaloid levels effect clinical outcomes, is the identification and quantitation of major and minor alkaloid constituents within available products and preparations. To this end, an ultra-high performance liquid chromatography-high resolution mass spectrometry method was developed for the analysis of 8 indole alkaloids (7-hydroxymitragynine, ajmalicine, paynantheine, mitragynine, speciogynine, isopaynantheine, speciociliatine, and mitraciliatine) and 6 oxindole alkaloids (isomitraphylline, isospeciofoleine, speciofoline, corynoxine A, corynoxeine, and rhynchophylline) in US-grown kratom plants and commercial products. These commercial products shared a qualitatively similar alkaloid profile, with 12 – 13 detected alkaloids and high levels of the indole alkaloid mitragynine (13.9 ± 1.1 – 270 ± 24 mg/g). The levels of the other major alkaloids (paynantheine, speciociliatine, speciogynine, mitraciliatine, and isopaynantheine) and the minor alkaloids varied in concentration from product to product. The alkaloid profile of US-grown M. speciosa “Rifat” showed high levels of the indole alkaloid speciogynine (7.94 ± 0.83 – 11.55 ± 0.18 mg/g) and quantifiable levels of isomitraphylline (0.943 ± 0.033 – 1.47 ± 0.18 mg/g). Notably, the alkaloid profile of a US-grown M. speciosa seedling was comparable to the commercial products with a high level of mitragynine (15.01 ± 0.20 mg/g). This work suggests that there are several M. speciosa chemotypes.

**Решение:** -

---

### 561 · R3211

**การดำรงลักษณ์ทางชาติพันธุ์และวัฒนธรรมมอญกระทุ่มมืด อำเภอไทรน้อย ตำบลไทรใหญ่ จังหวัดนนทบุรี: ภาคปฏิบัติการทางวาทกรรมสู่ความยั่งยืนของชุมชน**

2018 · Journal of Humanities and Social Sciences Thonburi University · article · en

บทคัดย่อ การวิจัยครั้งนี้มีวัตถุประสงค์เพื่อศึกษาถึงการดำรงอัตลักษณ์ทางชาติพันธุ์และวัฒนธรรมมอญกระทุ่มมืด สู่ความยั่งยืนของชุมชน อำเภอไทรน้อย ตำบลไทรใหญ่ จังหวัดนนทบุรี ด้วยการวิเคราะห์วาทกรรมด้านตัวบท ภาคปฏิบัติการทางวาทกรรม และภาคปฏิบัติทางสังคม ว่ามีกระบวนการอย่างไร การวิจัยครั้งนี้เป็นการวิจัยเชิงคุณภาพโดยใช้วิธีการวิเคราะห์วาทกรรมตามแนวทางของแฟร์คลาฟ ด้วยการสัมภาษณ์เชิงลึกของคนในชุมชน ผู้นำชุมชน หัวหน้าส่วนราชการในชุมชนบ้านกระทุ่มมืด อำเภอไทรน้อย ตำบลไทรใหญ่ จังหวัดนนทบุรี จำนวน 15 คน ผลการศึกษาพบว่า ตัวบทการดำรงอัตลักษณ์ทางชาติพันธุ์และวัฒนธรรมชาวมอญกระทุ่มมืด ประกอบด้วย 4 ด้าน คือ ด้านวัฒนธรรมและประเพณี ด้านการแต่งกาย ด้านการดำรงชีพ ด้านภาษาและการสื่อสาร เป็นความเชื่อที่ถูกถ่ายทอดมาจากบรรพบุรุษ ซึ่งความเชื่อส่วนใหญ่จะเป็นความเชื่อที่เกี่ยวกับโชคลาภที่สัมพันธ์กับการดำรงชีวิตตั้งแต่เกิดจนถึงตาย ผลการวิเคราะห์ภาคปฏิบัติการทางวาทกรรมการดำรงอัตลักษณ์ทางชาติพันธุ์และวัฒนธรรมมอญกระทุ่มมืด พบว่าชาวมอญกระทุ่มมืดให้ความสำคัญกับวัฒนธรรมและประเพณีที่สืบทอดมาจากบรรพบุรุษเป็นอย่างมากโดยถือปฏิบัติกันสืบต่อมาจากรุ่นสู่รุ่นรวมถึงด้านการแต่งกาย การดำรงชีพ ด้านภาษาและการสื่อสาร ทั้งนี้เพื่อดำรงอัตลักษณ์ของชาวมอญกระทุ่มมืดและเพื่อสนับสนุนการผลิตซ้ำ ซึ่งการผลิตซ้ำในชุมชนมอญกระทุ่มมืดเกิดขึ้นจากการสนับสนุนจากผู้นำชุมชนและผู้สูงอายุหรือผู้หลักผู้ใหญ่ในชุมชนที่เข้ามาผลักดันให้เกิดการอนุรักษ์และส่ง เสริมให้คนในชุมชนเห็นความสําคัญของวัฒนธรรมและอัตลักษณ์ของชาวมอญกระทุ่มมืด คำสำคัญ: การวิเคราะห์วาทกรรม, อัตลักษณ์, มอญกระทุ่มมืด, ความยั่งยืนของชุมชน Abstract This research is qualitative research with a methodology to discourse analyze. The purpose of the research is to study the way ethnic and cultural identity Mon Katum meut. Sustainability of community Amphoe Sai Noi , Sai Yai , Nonthaburi : The discourse analysis chapter. Practical mathematical discourse and social practice that process. This research is qualitative research using discourse analysis methods based on the guidelines of Norman Fairclough. With in-depth interviews of community leaders to community members, The head of Government in the community Ban Katum meut Amphoe Sai Noi, Sai Yai, Nonthaburi. The number of 15 persons to gather information on the above discourse analysis. The study found that the chapter on the ethnic and cultural identities Mon Katum meut. Contains 4 aspects: cultural traditions and aspects of living side dress. Language and communication is being transmitted from the ancestors for many generations, from past to present. The most is the belief about the fortune associated with living since was ordained to the death. The practical working maintenance of ethnic identity and cultural discourse Mon Krathum meut. Mon Krathum meut to focus on the culture and tradition of the elders is a very common practice by holding the tradition from generation to generation, dressing, living language and communication. In order to establish the identity of the Mon Kratum Muet to support reproduction. Which is reproduced in the Mon Kratum muet place with the support of community leaders and the elderly or adult in the community who are pushing for conservation and encouraged people in the community see the importance of the culture and identity of the Mon Krutum muet. Keyword: Discourse analysis, identity, Mon Kratum muet, Sustainable communities

**Решение:** -

---

### 562 · R1064

**การศึกษาการอบแห้งใบกระท่อมด้วยวิธีฟูลอิดไดซ์เบด**

2025 · PSRU Journal of Science and Technology · article · th

Kratom leaves are used to treat intestinal infections, diarrhea, muscle pain, and to reduce fever. In 2021, the Thai government lifted the restriction on using kratom in food, allowing it to be legally incorporated into food products. At present, kratom is processed into dried leaves and powder, which are used in various products such as kratom-infused beverages and instant tea. This research studied the drying process of green-stem kratom leaves (Tangkwa variety) using a fluidized bed dryer. The system consists of a blower fan that pushes hot air through a heater into the drying chamber at a flow rate of 38 cubic feet per minute (CFM). Kratom leaves weighing 1 kilograms, 2 kilograms, and 3 kilograms were cut into pieces of 3–5 centimeters in size. The experiments were conducted at temperatures of 40°C, 50°C, 60°C, and 70°C, with moisture content recorded every 10 minutes to determine the effects of temperature and leaf weight on moisture ratio, specific energy consumption, and mitragynine content. The results showed that moisture was reduced more quickly at higher temperatures, while drying time increased with greater weight of kratom leaves. Specific energy consumption decreased by up to 9.10% as the drying temperature increased. The mitragynine content in kratom leaves decreased linearly with increasing drying temperature, with the lowest level of 25.93% observed at 70°C. Based on the experimental results, considering energy use and drying time, a drying temperature of 60°C was found to be the most appropriate for this study. However, if retaining the highest mitragynine content is the priority, drying should be conducted at 40°C. The findings from this research can be applied to the development of food and beverage products from kratom leaves, adding value to agricultural products, recommending appropriate drying temperatures to reduce energy consumption, and supporting the production of Thai traditional herbal medicines with controlled active compounds.

**Решение:** -

---

### 563 · R3022

**Use of Buprenorphine-Naloxone in the Treatment of Tianeptine Use Disorder**

2019 · Journal of Addiction Medicine · article · https://doi.org/10.1097/adm.0000000000000490

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 564 · R0131

**Counseling Pregnant Patients About Cannabis and Kratom**

2026 · Psychiatric News · journalarticle, journal article, journal-article · en · https://doi.org/10.1176/appi.pn.2026.10.10.7

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 565 · R3290

**Assessment of the abuse potential and benefits of kratom and its mitragynine alkaloids: Implications for regulation**

2017 · Drug and Alcohol Dependence · article, journal-article · en · https://doi.org/10.1016/j.drugalcdep.2016.08.317

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 566 · R3749

**The challenge of new psychoactive substances. A report from the Global SMART Programme.**

2013 · United Nations Office on Drugs and Crime · review · https://core.ac.uk/download/34719377.pdf

1. INTRODUCTION p.1 1.1 Emergence of new psychoactive substances 1.2 Definition and categories of new psychoactive substances 2. MAIN NEW PSYCHOACTIVE SUBSTANCES ENCOUNTERED IN ILLICIT MARKETS AND THEIR EFFECTS p.3 2.1 Synthetic cannabinoids 2.2 Synthetic cathinones 2.3 Ketamine 2.4 Phenethylamines 2.5 Piperazines 2.6 Plant-based substances 2.6.1 Khat 2.6.2 Kratom 2.6.3 Salvia divinorum 2.7 Miscellaneous substances 2.7.1 Aminoindanes 2.7.2 Phencyclidine-type substances 2.7.3 Tryptamines 3. GLOBAL SPREAD OF NEW PSYCHOACTIVE SUBSTANCES p.19 3.1 Emergence of new psychoactive substances 3.2 Legal situation 3.2.1 The international drug control system 3.2.2 Regional responses: the European Union 3.2.3 National responses to new psychoactive substances 3.2.4 Other regulatory frameworks 4. USE OF NEW PSYCHOACTIVE SUBSTANCES p.33 4.1 Global use estimates 4.2 Regional use estimates 4.3 National use estimates 4.4 National treatment data estimates 4.5 Internet surveys on the use of new psychoactive substances 5. SOURCES OF NEW PSYCHOACTIVE SUBSTANCES p.43 5.1 Countries reporting seizures of new psychoactive substances 5.2 Number of new psychoactive substances in global markets 5.3 Perceived sources of new psychoactive substances and the role of internet 5.4 Identification of new psychoactive substances ANNEXES p.57 • New psychoactive substances reported in 2012 • Synthetic cannabinoids • Synthetic cathinones • Ketamine • Phenethylamines • Piperazines • Plant-based substances • Aminoindanes • Phencyclidine-type substances • Tryptamines • Others • Reference

**Решение:** -

---

### 567 · R0091

**Defining kratom: evidence-based policy guidelines for a rapidly evolving market.**

2026 · Frontiers in pharmacology · article, journal article, journalarticle · eng · https://doi.org/10.3389/fphar.2026.1925809

The leaves of Mitragyna speciosa, commonly called kratom, have been consumed for centuries in Southeast Asia for their energizing and analgesic properties. Over the last decade kratom has gained popularity in the United States, with an estimated 10-16 million consumers, and a wide variety of products have become available in the marketplace. Along with a plethora of product formulations that contain various concentrations of kratom alkaloids, new products have emerged, labelled as "kratom", but comprised of highly concentrated synthetic alkaloids. Consumers and regulators alike struggle to differentiate the spectrum of products that range from those similar in composition to traditional kratom to those that are illegally marketed, unapproved novel drugs. With significant implications to public health policy and safety, there is a need to clearly define and differentiate kratom, kratom-derived, and synthetic products. Herein we offer guidance to support standardization of the terminology used in the manufacture and labelling of kratom and kratom-derived products in the United States. This is intended to be a reference tool for use by industry and federal, state, and other jurisdictions that oversee the kratom industry to encourage clear and consistent communication.

**Решение:** -

---

### 568 · R2207

**In case you haven&t heard…**

2021 · Alcoholism & Drug Abuse Weekly · article · en · https://doi.org/10.1002/adaw.33154

It's probably not unusual for patients to seek help for kratom addiction, but we don't hear about it very often. Still, “I got in trouble with kratom — I was getting it online; could I have some of that buprenorphine?” is not an unprecedented question for physicians to hear. Recently a case in which such treatment was successful was posted in a medical journal. For the case study, go to https://journals.sagepub.com/doi/full/10.1177/20503245211021193 . This was, as Peter Grinspoon, M.D., observed, quite a large dose of kratom the patient was taking, and trying to withdraw on her own by using kratom tea probably would not have been effective. The episode occurred during the pandemic, when it would have been very difficult to find other treatment, and patients self‐treating all kinds of problems were falling between the cracks as COVID‐19 took precedence.

**Решение:** -

---

### 569 · R1233

**A comprehensive update in herbal and dietary supplement–induced liver injury**

2024 · Clinical Liver Disease · article · en · https://doi.org/10.1097/cld.0000000000000185

INTRODUCTION In the United States, over 100,000 over-the-counter herbal and dietary supplements (HDS) are available both in stores and online, contributing to the potential for HDS-induced liver injury (HILI).1 HDS includes a diverse spectrum of constituents like vitamins, minerals, proteins, herbs, and botanical essences and is now a well-recognized potential cause of both acute and chronic liver injury.1–3 Unlike conventional medicines, HDS products are sometimes contaminated with unclear safety profiles due to adulteration and mislabeling.4 Cases of HILI reported to the US Drug-Induced Liver Injury Network have increased from 7% of all DILI cases in 2005 to 20% in 2014.2,5 Diagnosing HILI is challenging due to scarce assessment tools, unclear injury patterns, and uncertainty about the culprit ingredients that cause liver damage. The aim of this review is to provide clinical insights and updates on the diagnosis and management of HILI. CURRENT TRENDS IN HERBAL AND DIETARY SUPPLEMENT–INDUCED LIVER INJURY The incidence of severe liver injury from HDS, as per the Acute Liver Failure (ALF) Study Group database, rose from 12.4% (1998–2007) to 21.1% (2007–2015).6 Despite a lower rate of comorbid conditions, patients with HDS-related ALF exhibit higher transplantation and mortality rates than cases due to prescription medication.6 Similarly, in a 2015 population study, over 18% of ALF cases were attributed to HDS, with 50% resulting in death or liver transplant.7 In the prospective study of DILI from the NIH-funded Drug-Induced Liver Injury Network, liver injury attributable to HDS increased from 7% in 2004–2005 to 20% by 2013–2014.3,5 In Europe, studies also show a growing tendency for HDS use.3 Notably, despite widespread HDS usage in Asia, the incidence varies significantly, ranging from as high as 70% in Singapore8 to 2.5% in India.9 Amid the COVID-19 pandemic, interest in HDS spiked, propelling US sales to over $10 billion in 2020, a 17.3% surge from the prior year—the highest in 2 decades. Recent statistical data reveal that more than 50% of US adults use HDS daily.10 Use is more prevalent among females, non-Hispanic Asian and non-Hispanic White, individuals aged 70 or older, and those with conditions like stroke, obesity, arthritis, and respiratory problems.5,11,12 Interestingly, use increases with income and education among adults.5,11,12 In the United States, HDS is regulated by the Food and Drug Administration (FDA)’s Center for Food Safety and Applied Nutrition through the Dietary Supplement Health and Education Act of 1994. Per the Dietary Supplement Health and Education Act, HDS products are not subject to the same stringent premarket safety and efficacy testing as pharmaceuticals.13 Additionally, HDS products are exempt from mandatory investigational clinical trials for efficacy documentation. Federal law mandates HDS manufacturers to provide a comprehensive list of dietary ingredients. Regardless, many HDS products have been withdrawn from the market due to discrepancies between the listed dietary ingredients and the actual product formulation. Recent research has revealed a 51% mislabeling rate for dietary ingredients, notably suggesting that mislabeled HDS products could harbor undisclosed ingredients while omitting listed substances.4 At times, these products were found to be contaminated with heavy metals and pesticides.14 The FDA prohibits making explicit claims about the treatment or prevention of specific diseases. Nevertheless, manufacturers frequently draw consumer interest by using unsubstantiated statements and consumers may not understand the level of regulatory supervision imposed on HDS. NAVIGATING CLINICAL CONUNDRUMS AND INSIGHTS IN DIAGNOSING HEPATIC INJURY FROM HERBAL AND DIETARY SUPPLEMENTS There is no specific serum marker to aid in diagnosing HILI. The skill of history-taking holds paramount importance and entails obtaining information on supplement usage, initiation and cessation dates, dosage alterations, data pertaining to recovery after discontinuation (dechallange), and re-exposure (rechallenge)1 (Figure 1).FIGURE 1: A stepwise approach to diagnosis of herbal and dietary supplement–induced liver injury. Adapted from Navarro et al3 and Fontana et al.15 Abbreviations: ALT, alanine amniotransferase; ALP, alkaline phosphatase; AST, aspartate aminotransferase; HDS, herbal and dietary supplements; INR, international normalised ratio; ULN, upper limit normal.Causality assessment methods have been developed to evaluate the probability that a particular drug or HDS is responsible for liver injury1 (Table 1). However, use is rather limited in HILI due to the use of multi-ingredient HDS, adulteration, mislabeling, and simultaneous intake of pharmaceuticals and other over-the-counter medications.1 Detailed review of clinical data remains the gold standard for diagnosis and causality assessment. TABLE 1 - Causality assessment instruments16–19 RUCAM (Roussel Uclaf Causality Assessment Method RECAM (Revised Electronic Causality Assessment Method The Maria‐Victorino (CDS) The Digestive Disease Week–Japan 2004 (DDW‐ J) Criteria Time to onset from the beginning of the drug/herbCourse of ALT after cessation of the drug/herb Percentage difference between ALT peak and ULNRisk factorsConcomitant drug(s)/herb(s)Exclusion of Alternative CausesPrevious hepatotoxicity of the drug/herbResponse to unintentional re-exposure Onset after drug start and onset after drug stopDechallange or washoutLiterature supporting liver injuryExclusion of competing diagnoses Temporal relationship between drug intake and onset of clinical pictureExclusion of alternative causesExtrahepatic manifestationsIntentional or accidental re-exposure to the drugPrevious report in the literature of cases of DILI associated with drug The score is a modification of the RUCAM with the inclusion of DLST results and peripheral eosinophilia. Total score and resulting causality grading ≤ 0, excluded;1–2, unlikely;3–5, possible;6–8, probable;≥ 9, highly probable 17 definite; ≤ 0, excluded;1–2, unlikely;3–4, possible;5–8, probable;> 17 definite; Specific operational information Prospective use, retrospective use is less accurate;Calculated individually for each co-administered product;For idiosyncratic, not for intrinsic reactions;Applicable only for acute liver injury, not for pre-existing chronic liver disease;Used in HDS-HILI; Better than RUCAM at diagnostic extremesHas not been validated in HILI Not used widely in clinical practice because it was shown to be inferior to the RUCAM Not currently used outside of Japan because of the lack of widely available and reproducible DLST assays. Abbreviations: ALT, alanine aminotransferase; CDS, Clinical Diagnostic Scale; DLST, drug‐lymphocyte stimulation test; HDS, herbal and dietary supplements; HILI, HDS-induced liver injury; ULN, upper limit normal. LiverTox, created in 2012 by the National Institute of Diabetes and Digestive and Kidney Diseases, is a great resource and tool for physicians, researchers, and patients. It offers up-to-date insights into the potential hepatoxicity of over 1000 medications and HDS with likelihood scales for liver injury.20 LiverTox incorporates the Drug-Induced Liver Injury Network’s 5-point categorization as “likelihood scores” as part of its comprehensive approach to assess the likelihood of HILI. This classification relies heavily on published literature, making it more precise for medications that have been used widely but less so for newer drugs or herbals with limited use. Several in vitro assessment tools have been developed to help aid in the diagnosis of DILI21 (Table 2). Genetic and immunologic susceptibility plays an important role in the development of HILI.1 A strong link has been observed between liver injury related to green tea extract consumption and the HLA allele B*35:01.22 This allele was identified in 72% of the patients with HILI due to green tea extract and in over 90% of those in whom the injury was categorized as highly probable or certain.22 Allele carriers are younger at presentations and have shorter latency periods, higher median alanine aminotransferase values, and more severe presentations.22 Notably, HLA-B*35:01 has also been linked to the liver injury induced by Polygonum multiflorum,23 Garcinia cambogia,24 and Turmeric.25 A missense variant (rs2476601) in PTPN22, which has been correlated with various autoimmune disorders, poses a risk factor for all-cause DILI in diverse racial and ethnic populations.26,27 TABLE 2 - Investigational in vitro assessment tools to help aid in the diagnosis of HILI In vitro test Process Comment LTT PBMCs are incubated with questionable hepatotoxin. Lymphocyte proliferation is measured by interferon-gamma release or 3H-thymidine Low sensitivity and specificity;Has not been standardized or validated;Integral component of DDW-J 2004 scale Cluster of differentiation 69 (CD69) Incubated with implicated hepatotoxin.CD69 expression monitored Validation studies not published Monocyte-derived hepatocyte-like cells Incubating MH cells with questionable hepatotoxin. Toxicity is analyzed by measuring the release of lactate dehydrogenase 92.3% sensitivity and 100% specificity;Has not been externally validated; Note: Weber S et al.21Abbreviations: LLT, lymphocyte transformation test; PBMC, peripheral blood mononuclear cells. EXPLORING THE COMMON HEPATOTOXIC CULPRITS: HERBAL AND DIETARY SUPPLEMENTS UNVEILED THROUGH PATTERNS OF LIVER INJURY HDS generally falls into 2 categories: single ingredient (Table 3), involving 1 plant product, or multi-ingredient formulations (Table 4). Multi-ingredient HDS poses diagnostic challenges due to complex mixtures, nuanced pharmacology with potential synergies, high rate of mislabeling, adulteration, substance omission, and even pesticide contamination, all contributing to diverse host risks.4,14 Green tea, an ancient drink, has a good safety profile when consumed as a beverage but may pose a risk for liver injury when consumed in the extract form.28 The primary component, epigallocatechin gallate, is known to cause potential hepatotoxicity, especially with prolonged use, fasting intake, and doses exceeding 800 mg.28 The use of organic solvents in extraction, like methanol or chloroform, adds another layer of risk.28 Even caffeine, commonly found in weight loss or performance-enhancing supplements, can amplify the hepatotoxicity of stimulants.28 Yohimbine extract, prevalent in weight loss supplements, has been linked to a higher incidence of severe outcomes.28 This caution extends beyond individual components, emphasizing the potential synergistic toxicity of additives. TABLE 3 - Commonly used hepatotoxic HDS in the market Ingredient Chemical structure Plant and region Marketed Use Purported benefit Latency Adverse effects Pattern of liver injury outcome DILIN Class Ashwagandha, “Indian ginseng” Steroidal lactone WithaniaSomniferaIndia and Southeast Asia Energy enhancement Adaptogen, anxiolytic, anti-diabetic, anti-inflammatory, aphrodisiac and anti-aging; 2–12 wk Gastrointestinal upset, diarrhea, nausea, and vomiting Cholestatic or mixed pattern of injury, jaundice, and pruritus No deaths or transplants Category C likelihood score Black cohosh Triterpenes glycosides and polyphenols Actaea racemosa/Cimicifuga racemoseNorth America Menopause symptom relief Malaise, gynecological disorders, kidney disorders, malaria, rheumatism, and sore throat; 2–12 wk Hypotension, bradycardia, central nervous system effects, nausea, and vomiting Hepatocellular, autoimmune hepatitis Liver failure, transplant, and death reported Category A likelihood score Curcumin/Turmeric Polyphenol Curcuma longaIndiaSouthern Asia and Central America Indigestion Anti-inflammatory, antioxidant, antimicrobial, and even antineoplastic effects; 4–12 wk Dermatitis and gastrointestinal upset Hepatocellular or mixed or autoimmune hepatitis Death reported Category B likelihood score Garcinia cambogia/Garcinia gummi-gutta (−)−Hydroxycitric acid Malabar tamarind treeIndia, Nepal and Sri Lanka Weight loss Anti-inflammatory and appetite suppressant; 12–48 wk Serotonin syndrome, rhabdomyolysis Mostly hepatocellular pattern, rarely mixed Liver failure, transplant, death, chronic HILI reported Category B likelihood score GTE epigallocatechin-3-gallate (EGCG) Catechin-Polyphenol Camellia sinensis South and Southeast Asia Weight loss Chemoprotective antiproliferative and antioxidant; 1–64 wk Headache, dizziness and nausea Hepatocellular Most recovery, Liver failure, transplant, and death reported Category A likelihood score Kratom Tetracyclic indole and pentacyclic oxindole alkaloids Mitragyna speciosia, Southeast Asia (Thailand, Myanmar, and Malaysia) Analgesic Anxiolytic, antitussive, antidiarrheal, stimulant, analgesic, opiate withdrawal; 1–8 wk Respiratory depression, aggression, hallucinations, delusions, insomnia, vomiting, severe withdrawal, hypertension, dyspnea, confusion, seizure, coma, death Mixed or cholestatic injury No deaths from acute liver failure or transplants Category B likelihood score Note: DILIN class, that is, likelihood of causing clinically significant liver injury and the pattern of resultant liver injury. The likelihood score was obtained from the DILI Network LiverTox database. It is a 5‐point scale (A–E) that estimates whether a medication is a cause of liver injury: A = well‐known cause; B = highly likely cause; C = probable cause; D = possible cause; E = unlikely cause; E* = suspected but unproven cause; X = unknown.Abbreviations: GTE, green tea extract; HILI, HDS-induced liver injury. TABLE 4 - Commonly encountered hepatotoxic multi-ingredient HDS Supplement Marketed Use Latency Suspected hepatotoxins Pattern of liver injury Likelihood score Herbalife Weight loss, digestive health, boosting immunity, heart health, energy and fitness 8-36w Saw palmettoGreen tea extract Hepatocellular (most common), mixed, cholestatic, sinusoidal obstruction syndrome(rare) A OxyELITE Pro Weight loss, body building, performance enhancement aid 2-20w Aegeline Hepatocellular, submassive or massive necrosis, autoimmune hepatitis-like A Hydroxycut Weight loss, body building “fat burning” 2-12w AshwagandhaEphedraGreen tea extract Hepatocellular, submassive or massive necrosis, cholestatic or mixed hepatitis(rarely) B Slimquick Weight loss 3-12w Green tea extract, Turmeric Hepatocellular C DILIN class, i.e., likelihood of causing clinically significant liver injury; and the pattern of resultant liver injury. Likelihood score obtained from the DILI Network LiverTox database.It is a 5‐point scale (A to E) that estimates whether a medication is a cause of liver injury: It is a 5-point scale (A to E) that estimates whether a medication is a cause of liver injury: A = well‐known cause; B = highly likely cause; C = probable cause; D = possible cause; E = unlikely cause; E* = suspected but unproven cause; X = unknown. Multi-ingredient supplements like OxyELITE-pro, OxyELITE-Pro New Formula (OxyELITE-pro-NF), and Hydroxycut led to a myriad of complications that mandated their removal from the market. Chemical analysis often identified potentially hepatotoxic ingredients like caffeine and yohimbine, alongside green tea extract and Garcinia cambogia, as potential culprits.28 Significantly, notwithstanding the removal of original Hydroxycut formulations from the market in 2009, reformulations are presently available. New, albeit rare, cases of liver injury linked to Hydroxycut are still reported, leading to cholestatic liver injury and even vanishing bile duct syndrome.28 STRATEGIES OF MANAGEMENT AND PROGNOSIS OF HERBAL AND DIETARY SUPPLEMENT–INDUCED LIVER INJURY HILI is typically idiosyncratic in nature, with a latency period of 2–24 weeks.1,15,29 The pattern of liver injury is more commonly hepatocellular and depends on the interplay between host, environmental factors, and culprit ingredients.1,15,29 Suspected agents should be promptly discontinued and reported through the FDA’s medical product safety reporting program (MedWatch https://www.fda.gov/safety/medwatch-fda-safety-information-and-adverse-event-reporting-program). Approximately 80% of patients fully recover without long-term sequelae.1,15 However, patients with ALF characterized by coagulopathy and encephalopathy require urgent referral to a liver transplant center due to their limited likelihood (~25%) of spontaneous recovery. Alarmingly, despite similar disease severity (Model for End-Stage Liver Disease scores), patients with HDS-induced ALF show lower transplant-free survival and higher transplantation rates at 21 days compared to allopathic medicine–induced ALF cases.30 Patients with pre-existing liver disease, lower serum albumin levels upon presentation, and higher total bilirubin and INR levels are at increased risk of adverse hepatic outcomes.1 Conversely, patients exhibiting granulomas and eosinophil infiltrates on biopsy tend to have a higher likelihood of spontaneous recovery.1 General supportive care is the standard of care for HILI. In cases of ALF with early-stage encephalopathy, a 3-day N-acetylcysteine regimen has been shown to significantly improve transplant-free survival from 27% to 58% in adults.1 Corticosteroids for 1–3 months may benefit patients with autoimmune phenotype and plasma cell predominance on biopsy, but empirical use is discouraged, especially in those with cholestatic liver injury patterns, as it may cause harm.1 Like idiosyncratic DILI, there is no specific antidote for liver injury caused by HDS. SUMMARY HILI accounts for 20% of DILI cases in the United States. Identifying and preventing HILI poses substantial challenges due to diverse presentations, diagnostic complexities, ingredient identification hurdles, limited treatment options, and lack of regulatory oversight of HDS products to confirm ingredients and ensure safety. Further advances in the identification of at-risk genetic phenotypes, greater oversight from regulatory organizations, and specific treatments for HILI are needed.

**Решение:** -

---

### 570 · R1597

**Living Systematic Review on Cannabis and Other Plant-Based Treatments for Chronic Pain: 2022 Update—Surveillance Report 3**

2023 · casereport, review · https://doi.org/10.23970/ahrqepccer250.2022updatesr3

Overview This is the third surveillance report since the annual update of a living systematic review on cannabis and other plant-based treatments for chronic pain. Since the last surveillance report, inclusion criteria were expanded to also address subacute pain (4 to 12 weeks’ duration) and pain in adolescents.1 The systematic review synthesizes evidence on the benefits and harms of plant-based compounds (PBCs), such as cannabinoids and kratom, used to treat chronic or subacute pain, and addresses concerns about severe adverse effects, abuse, misuse, dependence, and addiction. The purpose of this surveillance report is to describe new studies identified since the last search (mid-October 2022) and provide a synthesis of the accumulated evidence. Surveillance update reports are planned on a quarterly basis, and the systematic review will be updated annually. The systematic review is available on the Agency for Healthcare Research and Quality (AHRQ) website (https://effectivehealthcare.ahrq.gov/products/plant-based-chronic-paintreatment/living-review). Table 1 provides a summary of the version history.

**Решение:** -

---

### 571 · R1156

**Untargeted High-Resolution Mass Spectrometry for Detection of Natural Products and Confiscated Powders and Pills.**

2024 · Methods in molecular biology (Clifton, N.J.) · book chapter, journal article · eng · https://doi.org/10.1007/978-1-0716-3541-4_18

Drug testing for clinical toxicology purposes is difficult given the variety of drugs and substances that can be abused. High-resolution mass spectrometry is a powerful tool for the qualitative identification of compounds in the blood and urine of exposed individuals. The interpretation of results can be greatly improved if caregivers and/or laboratorians are able to communicate with patients, family members, friends, or law enforcement (where appropriate), in order to obtain and test the drugs, plants, herbals, or chemicals that were taken. Methods are needed for the extraction, purification, and untargeted mass spectral analysis of drugs from the donated or seized materials.

**Решение:** -

---

### 572 · R1519

**What is kratom.org?**

2023 · https://doi.org/10.6084/m9.figshare.21992513.v1

kratom.org is an advocacy group dedicated to protecting consumers from governmental and corporate threats, improving the safety of kratom and spreading awareness of kratom's many benefits. It also offers educational materials, a newsletter and website to inform consumers of the facts about kratom which is considered as one of the best resources to fight misinformation about kratom. kratom.org is a nonprofit organization that has been active in the kratom community since it was founded in 2014. Their mission is to protect consumers from unwarranted legal decisions and to provide reliable information on kratom. They work to bring about a better understanding of kratom's benefits, safety, and potential to help people around the world. kratom.org is comprised of a team of volunteers who are passionate about safe and effective kratom use. As such, the group regularly updates its website with new facts and figures about kratom. This information is useful to kratom users and can serve as a basis for a conversation about kratom. In addition to providing kratom information, kratom.org website includes an email newsletter and a form to contact Congress. Those interested in joining kratom.org can sign up for an email newsletter, which is a surprisingly easy process. Similarly, kratom.org hosts focus forums on specific topics such as kratom safety, legality, and consumer protection. kratom.org has a comprehensive GMP Program to ensure that kratom is handled properly. Suppliers that comply with the program are able to sell quality products and improve the safety of consumers. Manufacturers must pass an official audit and adhere to specific manufacturing guidelines. In addition, kratom.org offers an in-depth educational program. This educational program aims to educate lawmakers, government agencies, and kratom vendors about kratom's benefits. Additionally, kratom.org offers scientific research on the kratom plant, including its biology and pharmacology. Another good way to promote kratom is to donate to kratom.org, either for its education program or for its legal defense. These donations help cover costs of promotion and scientific research. You can even donate a one-time sum or set up a monthly or yearly contribution. Unlike some other kratom advocacy groups, kratom.org is a Virginia-registered organization, which means it is exempt from paying taxes. But this does not mean the group is free from the IRS. Peter Candland, the Executive Director, is responsible for overseeing all aspects of kratom.org's daily tasks. He is a former lawmaker from Arizona who has spent a decade working in government. His experience in state and federal legislature has helped shape the organization's goals. kratom.org has made a strong impact in the world of kratom. They have helped bring about positive change in the United States and have shown that kratom is safe, effective and legal. kratom.org has also worked with governments in other countries to bring about favorable policies for the kratom industry. Although kratom.org is not the only group advocating for kratom, it is certainly one of the most important. By promoting kratom's many edifying benefits, they are demonstrating that kratom is an appropriate and safe alternative to narcotics and conventional painkillers.</p

**Решение:** -

---

### 573 · R1257

**Survey of U.S. Residents and Their Usage of Electronic Cigarettes with Drugs Other Than Nicotine.**

2024 · Journal of psychoactive drugs · article, journal article, research support, n.i.h., extramural · eng · https://doi.org/10.1080/02791072.2023.2250353

ABSTRACT Electronic cigarettes (e-cigs), originally intended to be used as cigarette substitutes, have evolved into discreet devices for consuming drugs other than nicotine (DOTNs). Presented are the results of an exploratory survey in which information regarding demographics, e-cig device type, DOTN use, frequency and context of use was collected. The average reported age of respondents was 27.4 years of age (SD = 12.0), and respondents predominantly identified as male (73%). Vape pens (disposable or refillable) were the most reported device across all DOTN classes. Cannabinoids were the most reported class of DOTN used, for both lifetime and past 30-day use. Other DOTNs reported included herbal supplements, amphetamines, caffeine, kratom, vitamins, opiates, DMT, fentanyl, and ketamine. Combinations of DOTNs used in e-cigs and trends in poly-substance use were reported. The most commonly reported context was vaping alone, followed by with friends, at home, and at social events; less commonly reported contexts included when driving, at work, and at school. Results from this study are useful for developing future national surveys to consider a comprehensive substance use-focused strategy that includes vaping, building awareness of DOTN e-cig use, and highlighting public safety issues in driving impairment, crime scene investigations, and death investigations.

**Решение:** -

---

### 574 · R3088

**Healthcare Reform. Opioid Crisis.**

2018 · Issue brief (Health Policy Tracking Service) · journal article · eng · https://pubmed.ncbi.nlm.nih.gov/30681792/

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 575 · R3738

**Medical Toxicology of Drug Abuse**

2013 · Journal of Emergency Medicine · article · en · https://doi.org/10.1016/j.jemermed.2012.11.059

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 576 · R2817

**A Case of Kratom Overdose in a Pediatric Patient.**

2020 · Case reports in psychiatry · article, case reports, journal article · eng · https://doi.org/10.1155/2020/8818095

Kratom is a synthetic opioid that is federally unregulated and thus available for purchase through online retail and smoke shops in most states. Due to its availability, there is concern for misuse in the pediatric population. There is existing literature describing toxicity of kratom in adults; yet, to the best of our knowledge, there are no cases describing kratom toxicity in the pediatric population. Thus, we present the case of kratom overdose in a pediatric patient.

**Решение:** -

---

### 577 · R2766

**การบริหารจัดการอย่างยั่งยืนของประชาชนเครือข่ายชุมชนอนุรักษ์และฟื้นฟู ป่าภูถ้ำภูกระแต อำเภอแวงน้อย จังหวัดขอนแก่น**

2020 · Modern Management Frontier Journal · article · th

The objectives of this research were 1) to study the sustainable management of people in Phu Tham Phu Kratae Forest Conservation and Rehabilitation Community Network, Waeng Noi District, Khon Kaen Province. 2) to compare opinions on sustainable management of people in the conservation community network And rehabilitation of Phu Tham Phu Kratae Forest, Waeng Noi District, Khon Kaen Province, classified by gender, age, educational level and occupation, and 3) to find suggestions for sustainable management development of the people of Phu Tham Phu Kratae Forest Conservation and Rehabilitation Community Network, Waeng Noi District, Khon Kaen Province This is a mixed methods research, consisting of 146 people, 8 primary informants. By using the concept of prevention, correction, conservation And environmental rehabilitation in 8 areas, determining statistical significance at the level of .05 Questionnaire 5 rating scales with statistical methods used in data analysis, frequency, percentage, mean, standard deviation, t-test and F-test, one way ANOVA And qualitative research It is an In-Depth Interview and Descriptive Analysis. The research found the follows : 1) Sustainable management conditions Of the Phu Tham Phu Kratae Forest Conservation and Rehabilitation Community Network, Waeng Noi District, Khon Kaen Province, found that the overall picture was at a high level. 2) The comparison of opinions towards the sustainable management of the people of the Phu Tham Phu Kratae Forest Conservation and Rehabilitation Community Group, Waeng Noi District, Khon Kaen Province, found that classified by gender, education level and occupation, in general, there is no difference in opinions. And classified according to age, found that, in general, opinions were significantly different at the level of 0.05 and. 3) Have guidelines for the development of sustainable management of the people, the community network for conservation and restoration of Phu Tham Phu Kratae forest, Waeng Noi District, Khon Kaen Province Regarding prevention, it was found that there should be a process to promote and create participation of people in the communities in the area. Build a team of forest protection volunteers and increase surveillance to prevent forest encroachment. Regarding correction and rehabilitation, it was found that training should be provided to members. There is additional forest plantations in the deteriorated forest areas. To create a new forest instead. Conservation aspect, it is found that the forest area should be surveyed and the rules for preserving the sustainable forest boundary, the use of resources found that there should be clear control and supervision of the rules and regulations for the use of forest resources. As for the storage, it is found that the rules for conservation, storage and maintenance should be considered. Deforestation Do not seek benefits With a sign indicating the conservation area for treatment, found that conservation activities should be organized Preserving and rehabilitating forests Have sustainable forest fire prevention activities In the aspect of development, it was found that the information system development plan should be planned. There is development, creating new developmental ideas. "Bring the forest to the forest" as if creating a forest in the house, in the community and in the area of zoning, it should be found that the control zoning should be planned Hunting area Hunting-free zone, sanctuary, and natural resource and environment group of Phu Tham, Phu Kratum Into a clear proportion.

**Решение:** -

---

### 578 · R0547

**Increase in Poison Center Reports Linked to Kratom-Containing Kava Products - National Poison Data System, United States, 2000-2025.**

2026 · MMWR. Morbidity and mortality weekly report · article, journal article, journalarticle · eng · https://doi.org/10.15585/mmwr.mm7512a1

Kava (Piper methysticum), a central nervous system depressant derived from a plant in the pepper family native to the Pacific Islands, is traditionally consumed in religious, cultural, political, and social ceremonies. In the United States, kava emerged in the late 1990s and has experienced renewed growth and product diversification since the 2010s, with increasing availability of concentrated extracts and ready-to-drink beverages. These commercial products are commonly marketed as healthy alternatives to alcohol, sold near college campuses, and increasingly being combined with kratom, a psychoactive botanical with opioid-like effects, raising safety concerns. Data on kava-related use during January 2000-December 2025 that resulted in a report to the National Poison Data System (i.e., kava exposure report) were analyzed to assess trends by users' demographic characteristics, exposure type, and outcomes. Kava-related exposure reports declined sharply after a 2002 Food and Drug Administration advisory on kava-associated severe liver injury but have risen steadily since 2011, reaching 203 reported exposures in 2025. Reports primarily involved adults aged ≥20 years, but demographic characteristics have changed over time. During 2000-2001, reports primarily involved females and included more children aged ≤12 years, whereas exposure reports since 2013 have predominantly involved men; reports involving children have been rare. Since 2017, reports involving combined use of kava and kratom have increased, reaching 30% (61) of all kava reports in 2025. These increases have coincided with higher rates of serious reported clinical outcomes in recent years (32% in 2025 compared with 12% in 2000). These data indicate a resurgence of overall kava exposure reports to poison centers, as well as an increase in kratom-related kava reports, which has coincided with higher rates of serious clinical outcomes. The findings in this report suggest the need for enhanced surveillance for, clinical awareness of, and public education regarding commercial products containing kava.

**Решение:** -

---

### 579 · R0900

**Abstract 4371369: Joint Associations of Social and Psychological Health Risk and Life’s Essential 8 among Women of Reproductive Age**

2025 · Circulation · article · eng · https://doi.org/10.1161/circ.152.suppl_3.4371369

Background: Cardiovascular risk factors are increasing among women of reproductive age, yet limited evidence exists on how co-occurring social and psychological burdens influence cardiovascular health (CVH). Understanding these joint effects is critical for guiding early prevention strategies that improve both maternal and long-term CVH. Methods: We conducted a cross-sectional analysis using 2013–2023 National Health and Nutrition Examination Survey data among women aged 18–49. Social burden was calculated as a cumulative score (range 0–5) based on poverty status, education, marital status, insurance, and employment, with high burden defined as scores ≥ the sample median. Psychological burden was assessed using the PHQ-9; scores ≥15 indicated moderate-to-severe depression. Women were categorized into four groups: (1) dual burden (high social and psychological burden), (2) psychological burden only, (3) social burden only, and (4) no burden. Multinomial logistic regression models adjusted for age, race/ethnicity, and Life’s Essential 8 (LE8) metrics, estimated associations between burden group and low (CVH score 0–49) and moderate (50–74) CVH compared to high CVH (≥75) scores. CVH was evaluated using LE8 metrics: diet, physical activity, smoking, sleep, BMI, blood pressure, glucose, cholesterol, and the overall LE8 score. Results: Among 6,279 women (weighted population ~74 million, mean age 35.0 ± 8.7 years), 25.5% had no burden, 67.9% had social burden only, 0.6% had psychological burden only, and 6.0% had dual burden. Dual burden was significantly associated with low CVH across several domains: smoking (aRRR=2.47; 95% CI: 1.84–3.31), sleep (1.81; 1.33–2.46), glucose (1.89; 1.33–2.70), and blood pressure (1.28; 1.01–1.62). High social burden alone was consistently associated with low CVH, including smoking (7.92; 5.29–11.86), sleep (6.22; 4.24–9.12), physical activity (1.72; 1.27–2.33), glucose (2.00; 1.09–3.67), cholesterol (1.95; 1.17–2.32), BMI (1.49; 1.02–2.18), and blood pressure (1.56; 1.01–2.39). Psychological burden alone was only significantly associated with smoking (4.26; 1.75–10.36). Conclusion: Women of reproductive age with co-occurring social and psychological burden face heightened risk for suboptimal cardiovascular health, especially in modifiable behaviors. These findings underscore the need for targeted screening and prevention during the reproductive years to reduce both maternal morbidity and long-term cardiovascular disease risk.

**Решение:** -

---

### 580 · R0665

**Community Economic Empowerment Through Processing Sapat Leaves into Masiraan Villageâ€™s Special Herbal Tea Products**

2025 · Antasari Conference on Islamic Economics and BusinessÂ (ACIEB) · research article

This study aims to analyze the process and impact of community economic empowerment through the processing of daun sapat (Mitragyna speciosa) into herbal tea products as part of a local creative economy initiative in Masiraan Village, Pandawan District, Hulu Sungai Tengah Regency. Using the Asset-Based Community Development (ABCD) approach, this research emphasizes community participation, local asset utilization, and capacity building for sustainable economic development. The participatory qualitative method involved 15 participants (housewives, youth, and community leaders) for two months (Juneâ€“August 2025). Data were collected through observation, interviews, focus group discussions (FGD), and documentation. Quantitative descriptive analysis using a 5-point Likert scale was applied to measure changes in skills, motivation, and participation. Results show significant improvement in community skills, from an average of 2.0 (pre-training) to 4.6 (post-training), with increased entrepreneurial motivation and active collaboration. The value of daun sapat increased from IDR 2,000/kg (raw) to IDR 50,000/kg (finished herbal tea). The findings indicate that the ABCD approach effectively transforms local natural resources into high-value products while reinforcing Islamic economic principles, particularly á¸¥ifáº“ al-mÄl (protection of wealth). This study contributes to the literature on Islamic community empowerment and provides a replicable model for sustainable village-based creative economy development

**Решение:** -

---

### 581 · R2167

**พืชกระท่อมกับการดูแลสุขภาพของคนไทย**

2022 · Journal of Health Research and Innovation · article · th

Thai people have been using Kratom for a long time, especially in the South of Thailand. In 2021, the government of Thailand, amendment to the narcotic act. An amendment to remove Kratom from the list of harmful drugs and eliminate all penalties related to Kratom. The studies show Kratom has more benefits than harm. It is difficult to addictive if used properly. The purpose of this academic article was to present the botanical characteristics and chemical composition of Kratom, Kratom and drug laws, toxicology of Kratom, and Kratom and health care among Thais. The data from literature show the important substances in Kratom are alkaloids such as mitragynine which is found only in Kratom. It acts like opioids. The 7-hydroxymitragynine act as pain control like morphine, while limiting the negative side effects. It does not suppress the respiratory system. Kratom is also composed of a few other alkaloids which have the benefit of reducing pain and anti-inflammatory. Kratom leaves can be used to treat diarrhea symptoms, loss of weight, anti-oxidant, peptic ulcer, cough relief, anti-depression, stress relief, anti-depressive, and muscle relaxant. However, the determination of safe dosage has not been established for the treatment and the medical research on using Kratom was not been widely published. Moreover, if used improperly, it may cause toxic effects on the body. Therefore, the dosage of Kratom in the treatment of different symptoms should be studied to get more clear on its use to promote health care among Thais. This will promote confidence for people in using Kratom to take care of their health.

**Решение:** -

---

### 582 · R0624

**Mitragyna speciosa/Quetiapine: Mania and psychotic symptoms following drug misuse and Sedation: case report**

2025 · Reactions Weekly · article, journalarticle, journal-article · en · https://doi.org/10.1007/s40278-025-75083-3

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 583 · R0771

**Kratom-Induced Seizures: An Emerging Public Health Crisis (P6-9.015)**

2025 · Neurology · article, journalarticle, journal-article · en · https://doi.org/10.1212/wnl.0000000000210320

Objective: To determine the incidence of Kratom-induced seizures to help propose methods for better evaluation of these patients. Background: Kratom ( Mitragyna speciosa ) is a widely-legalized substance that has both stimulant- and opioid-like effects. Reasons for Kratom use ranges from pain relief to euphoria. Although the American Kratom Association claims that use is benign, there have been many reported adverse effects. One insidious effect is seizures. To date, there have only been a few case reports on Kratom-induced seizures. Design/Methods: A literature search was conducted in both PubMed and Scopus to find Kratom-induced seizure case reports/series. The search string consisted of a derivative of “Kratom” and “adverse effect” and “seizure.” General Kratom review articles were read for any other potential references not included in the search. A total of 77 articles were retrieved, and 11 articles with 23 unique patients were analyzed. Results: Our analysis showed that Kratom-associated adverse effects, including seizures, are becoming more common. For each patient reviewed, initial differentials did not include Kratom. No routine urinalysis detected Kratom-metabolites; therefore, patients underwent numerous additional tests. On average, patients spent 4 days hospitalized and received at least one type of imaging. Additionally, users tend to share characteristics: male, middle-aged, college educated, and middle class. Conclusions: Kratom-induced seizures are underreported in the literature. Analysis of Poison Control Center calls from 2011–2017 yielded 113 reported seizures from 1174 Kratom exposures, significantly more than published reports. Kratom is not detected by urinalysis. Untargeted chromatography-mass spectrometry can detect Kratom, but this instrument is expensive. Similarly, there is not a hospital-grade disposable test for Kratom detection. In conclusion, developing a positive predictive algorithm using the characteristics of Kratom users can help suggest Kratom as a source for seizures. Creating a rapid test for Kratom or an algorithm would save hospitals money and shorten patients’ hospitalizations. Disclaimer: Abstracts were not reviewed by Neurology® and do not reflect the views of Neurology® editors or staff. Disclosure: Mr. Fletcher has nothing to disclose. Dr. Dhyani has nothing to disclose.

**Решение:** -

---

### 584 · R4087

**麻薬性タイ国伝承民間薬 Mitragyna speciosa からのオピオイド活性成分の発見とその構造活性相関**

2005 · 応用薬理 · article · ja

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 585 · R1567

**Successful Management of Kratom Use Disorder With Buprenorphine and Naloxone.**

2023 · Cureus · article, case reports, journal article · eng · https://doi.org/10.7759/cureus.41146

Kratom is an unregulated herbal supplement that is growing in popularity in the United States. Its primary active ingredients, mitragynine, and 7-hydroxymitragynine, are partial agonists that act on mu- and delta-opioid receptors in the central nervous system, producing analgesia and a sense of euphoria. Kratom use can lead to addiction and adverse side effects, such as seizures, hallucinations, and coma. This case report presents a male in his 40s with a history of kratom use, who presented to the clinic seeking help for his addiction. The patient had been using kratom for several years to self-medicate for his anxiety and depression and gradually developed a kratom addiction. The patient was successfully treated with buprenorphine/naloxone, which helped alleviate his withdrawal symptoms and allowed him to abstain from kratom. This case underscores the growing issue of kratom addiction in the United States and the critical need for physician awareness in treating withdrawal.

**Решение:** -

---

### 586 · R1217

**A broad-spectrum LC-MS/MS method for screening and quantification of 100 analytes in clinical and autopsy blood samples**

2024 · Journal of Chromatography B Analytical Technologies in the Biomedical and Life Sciences · article · https://doi.org/10.1016/j.jchromb.2024.124323

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 587 · R3029

**Kratom and General Anesthesia: A Case Report and Review of the Literature.**

2019 · A&A practice · article, other literature type, case reports · eng · https://doi.org/10.1213/xaa.0000000000000857

Kratom is a botanical substance derived from the Mitragyna speciosa plant, which grows naturally in Southeast Asia. Its active compounds include alkaloids with psychoactive and opioid properties. Low doses act as a stimulant, while higher doses cause analgesia and euphoria. As a drug of abuse, there are reports of seizure, acute psychosis, and death. Both the US Food and Drug Administration and the Drug Enforcement Agency warn against the use of kratom. Here is the first reported case of an anesthetic in a patient using kratom for chronic pain.

**Решение:** -

---

### 588 · R2761

**Pain and Addiction**

2020 · Pain Care Essentials and Innovations · book chapter · https://doi.org/10.1016/b978-0-323-72216-2.00009-0

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 589 · R1729

**Receptor Selectivity and Therapeutic Potential of Kratom in Substance Use Disorders**

2023 · Current Addiction Reports · article, review, journal article · en · https://doi.org/10.1007/s40429-023-00472-9

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 590 · R0938

**Kratom-Induced Acute Liver Failure in a Healthy Adult**

2025 · The American Journal of Gastroenterology · article, journalarticle, conference-abstract · en · https://doi.org/10.14309/01.ajg.0001150016.15318.9b

Introduction: Kratom is a popular, unregulated herbal supplement used for its psychotropic and opioid-like effects. Despite its widespread perception as safe, Kratom has been increasingly implicated in drug-induced liver injury (DILI), with rare reports of acute liver failure (ALF). We present a case of ALF in a previously healthy individual following Kratom use. Case Description/Methods: A 43-year-old woman with a past medical history of plaque psoriasis presented to the emergency room with confusion, nausea, and jaundice for the past week. She reported drinking multiple bottles of Kratom daily for chronic back pain for the past 5 months. She denied any prior liver disease, alcohol, or illicit substance use. She started drinking Kratom 5 months prior for her chronic back pain. Liver function tests (LFTs) were notable for a bilirubin of 23 mg/dL, alkaline phosphatase 1,436 U/L, aspartate aminotransferase 644 U/L, alanine aminotransferase 115 U/L, and international normalized ratio 1.18. Physical exam was notable for jaundice with no asterixis. Ultrasound showed a non-specific finding of coarsened hepatic echotexture. MRI MRCP showed no evidence of biliary tree pathology. Liver biopsy showed severe portal and lobular hepatitis with small bile duct injury and a predominantly lymphocytic infiltrate containing plasma cells, neutrophils, and eosinophils. Liver serological workup was unremarkable for alternative etiologies of elevated liver enzymes. She was started on empiric N-acetylcysteine for 3 days and Budesonide 9 mg daily for one week, with improvement in LFTs. Strict stoppage of Kratom was advised. At the 2-month follow-up, LFTs showed continued improvement, with bilirubin levels down to 3.9 mg/dL. Discussion: Acute liver failure from Kratom is a rare but serious side effect. As there are over 40 metabolites in Kratom, the exact mechanism of liver injury is unclear. Unlike most reported cases with a 1–8 week latency, our patient developed peak bilirubin levels after 5 months, suggesting that Kratom-induced injury may follow a prolonged or subclinical course. Biopsy findings were consistent with resolving drug-induced liver injury. Notably, the patient recovered without transplantation, highlighting the potential for reversibility with early recognition. Given Kratom’s wide availability and perceived safety, clinicians should maintain a high index of suspicion, especially in younger patients presenting with unexplained liver injury and no traditional risk factors.

**Решение:** -

---

### 591 · R0802

**The psychotropic botanicals Kratom and hemp induce select cytochrome P450 enzymes in human hepatocytes: Inhibition is not the only game in town**

2025 · Drug Metabolism and Pharmacokinetics · article, journalarticle, journal-article · en · https://doi.org/10.1016/j.dmpk.2025.101251

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 592 · R3264

**Herbal Highs: Review on Psychoactive Effects and Neuropharmacology.**

2017 · Current neuropharmacology · journal article, review, journalarticle · eng · https://doi.org/10.2174/1570159x14666161031144427

BACKGROUND: A new trend among users of new psychoactive substances' the consumption of "herbal highs": plant parts containing psychoactive substances. Most of the substances extracted from herbs, in old centuries were at the centre of religious ceremonies of ancient civilizations. Currently, these herbal products are mainly sold by internet web sites and easily obtained since some of them have no legal restriction. OBJECTIVE: We reviewed psychoactive effects and neuropharmacology of the most used "herbal highs" with characterized active principles, with studies reporting mechanisms of action, pharmacological and subjective effects, eventual secondary effects including intoxications and/or fatalities Method: The PubMed database was searched using the following key.words: herbal highs, Argyreia nervosa, Ipomoea violacea and Rivea corymbosa; Catha edulis; Datura stramonium; Piper methysticum; Mitragyna speciosa. RESULTS: Psychoactive plants here reviewed have been known and used from ancient times, even if for some of them limited information still exist regarding subjective and neuropharmacological effects and consequent eventual toxicity when plants are used alone or in combination with "classical" drugs of abuse. CONCLUSION: Some "herbal highs" should be classified as harmful drugs since chronic administration has been linked with addiction and cognitive impairment; for some others taking into consideration only the recent trends of abuse, studies investigating these aspects are lacking.

**Решение:** -

---

### 593 · R0515

**การพยาบาลผู้ป่วยจิตเภทที่ก่อพฤติกรรมรุนแรงจากการเสพสารเสพติดแอมเฟตามีน : กรณีศึกษา**

2026 · Krabi Medical Journal · article · th

Objective : To compare the nursing care provided to two case studies of schizophrenic patients exhibiting violent behavior resulting from amphetamine use, and to utilize the findings as a clinical guideline for enhancing the efficiency of nursing interventions for this patient population. Methodology : This study is a comparative case study of two schizophrenic patients with violent behavior induced by amphetamine use, who were admitted to the Ruam Jai Ward at Krabi Hospital between October 2023 and September 2024. Data were collected from medical records and analyzed by comparing the two cases through the application of the nursing process. Results : The first case was a 29-year-old Thai male with a 6-year history of schizophrenia, complicated by methamphetamine and kratom use. Following methamphetamine consumption, he exhibited aggression, auditory hallucinations, and delirium, leading to the assault of a neighbor and destruction of property. After receiving care based on the clinical nursing practice guidelines for Serious Mental Illness with High Risk of Violence (SMI-V), there was no recurrence of violent behavior or complications from substance and psychiatric medication use, and his psychotic symptoms improved. The second case was a 39-year-old Thai male with a 15-year history of schizophrenia, co-occurring with the use of methamphetamine, kratom, and cannabis. Post-methamphetamine use, he presented with delirium, agitation, hallucinations, and a hostile gaze, leading to the assault of his brother-in-law and property damage. While managed under the SMI-V guidelines, he experienced complications from long-term substance abuse, including rhabdomyolysis, and developed acute dystonia due to the central nervous system depressant effects of multiple psychiatric medications, alongside amphetamine withdrawal. These conditions required intensive physical and mental health care, resulting in a prolonged hospital stay. Although both cases presented with psychiatric emergencies and violent behavior induced by amphetamine use, they differed significantly in disease severity, complications, and the complexity of problems, necessitating distinct nursing interventions. Conclusion : Medical treatment combined with holistic nursing care ensured that both cases received individualized crisis management across all phases, including admission for aggressive behavior, stabilization, and pre-discharge. The care was guided by the protocols for Serious Mental Illness with High Risk of Violence (SMI-V) induced by amphetamine use. Discharge planning involved active caregiver participation to facilitate the patients' successful reintegration into their families and communities. Effective nursing processes were implemented, ranging from risk assessment and timely crisis intervention to rehabilitation aimed at preventing relapse. This included proactive care, close monitoring of vital signs and complications, and functional rehabilitation to enhance self-care abilities. Family readiness was prioritized through humanized counseling, emphasizing compassion and love. Caregivers played a vital role in ensuring treatment adherence, reducing aggressive behaviors, and preventing re-hospitalization. Furthermore, a multidisciplinary approach and community involvement were essential in providing continuous and sustainable care.

**Решение:** -

---

### 594 · R0862

**A Numerical Simulation of the Kratom Plant Growth Model While Treated by a Specific Nutrient Using an Explicit Finite Difference Method**

2025 · Iaeng International Journal of Applied Mathematics · article

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 595 · R2314

**Pharmacological Characterization of Synthetic Kratom Alkaloids for Improved Alcohol Use Disorder Therapeutics**

2021 · The FASEB Journal · article, conference-abstract, journal article · en · https://doi.org/10.1096/fasebj.2021.35.s1.02465

Background Kratom is an opioid‐containing plant and currently a federally unscheduled substance within the U.S. that is used to self‐medicate chronic pain and opioid dependence, serving as a substitute for illicit and prescription opioids. Similarly, some individuals with Alcohol Use Disorder (AUD) find kratom helpful in reducing AUD dependence and withdrawal symptoms. We have previously shown that the kratom alkaloids can dose‐dependently decrease alcohol consumption in mice, and that this activity is dependent on delta opioid receptor (DOR) expression. However, the most potent of the alkaloids 7‐OH mitragynine, exhibited rewarding properties, presumably due to its mu opioid receptor (MOR) pharmacology. We hypothesized that reduction of MOR potency relative to potency at DOR would lead to an improved therapeutic window with respect to reward liability and alcohol consumption. Methods A series of kratom analogs were pharmacologically characterized for their ability to bind to opioid receptors and elicit G‐protein and beta‐arrestin signaling using radioligand binding and cellular signaling assays. Using the 2‐bottle choice assay of 10% alcohol consumption, wildtype and DOR knockout (DOR KO) mice were used to assess to what degree the kratom alkaloids could reduce alcohol use, and whether any effects were DOR‐mediated. Drug reward was also assessed through conditioned place preference experiments. Results Kratom analogs are G‐protein‐biased at the opioid receptors, similar to their parent compounds. Kratom analog #2 showed the most favorable pharmacology with similar DOR potency but greatly reduced MOR potency compared to 7‐OH mitragynine, and was capable of significantly decreasing ethanol consumption in wildtype mice at a dose of 10 mg/kg. CPP experiments and experiments with DOR KO mice are currently being completed for kratom analog #2 and will be useful in confirming DOR‐mediated effects and whether the improved pharmacological profile of the analogs confers therapeutic benefits. Discussion Our results indicate that the development of potent, DOR‐selective opioids could provide a pathway to treat alcohol use without being significantly rewarding, and that the kratom alkaloids provide useful scaffolds to jumpstart these efforts.

**Решение:** -

---

### 596 · R0058

**Kratom Use and Severe Health Outcomes Surge in the US.**

2026 · JAMA · article, journal article, journalarticle · eng · https://doi.org/10.1001/jama.2026.2131

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 597 · R0426

**The Unregulated Rise of Kratom Drinks: Emerging Challenges and Policy Recommendations**

2026 · Public Health Reports · article, journal article, journalarticle · eng · https://doi.org/10.1177/00333549251403378

The opioid epidemic left the US health system with devastating questions.How did a profit-driven pharmaceutical company fuel a crisis that claimed hundreds of thousands of lives?One answer lies in the unchecked influence of commercial interests on product marketing and regulation, a failure that enabled the rise of OxyContin and, more recently, Juul.Given the immense harm caused by these products, it is critical to monitor emerging industries whose products carry a risk of addiction for similar warning signs.We identify kratom drinks as one such product, arguing that lax regulation, aggressive marketing, and consumer confusion make them a looming public health threat.

**Решение:** -

---

### 598 · R3753

**Psychoactive plant species - Actual list of plants prohibited in Poland**

2013 · Psychiatria Polska · article · https://pubmed.ncbi.nlm.nih.gov/23885543/

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 599 · R1381

**A Preliminary Inventory of Kratom (Mitragyna Speciosa) Products and Vendors on the Darknet and Cryptomarkets.**

2024 · Journal of psychoactive drugs · article, journal article, journalarticle · eng · https://doi.org/10.1080/02791072.2023.2242361

ABSTRACT In recent years, the online sale of kratom (Mitragyna speciosa), a Southeast Asian plant with both medicinal and psychoactive properties, has raised health concerns mainly due to the uncontrolled diffusion of adulterated kratom-related products. This exploratory study provides, for the first time, a snapshot of the availability of kratom products on the darknet which has been further validated by data searches on the surface web. A total of 231 listings of kratom across 23 darknet marketplaces were identified between March 2020 and October 2021. Among these, 40 were found actively sold across five markets by thirteen vendors. Listed items were mainly advertised as “safe” substitutes for medicinal products for the self-management of pain and other health conditions and offered in various forms (e.g., dry leaf powder, pills, capsules). Purchases were made using cryptocurrencies, with some vendors offering Pretty Good Privacy, and were shipped from Europe, Australia, the United States, and the United Kingdom. Goods sold by the same sellers also included illicit drugs and fraud-related products. Our study discovered a previously unknown diffusion of kratom products on the darknet mainly for self-treating a variety of medical conditions, suggesting the need for further research and immediate interventions to safeguard the well-being and health of kratom consumers.

**Решение:** -

---

### 600 · R0079

**Clinical presentation and treatment in kratom withdrawal: a narrative review of case studies**

2026 · Journal of Education Health and Sport · article, journalarticle, review · en · https://doi.org/10.12775/jehs.2026.88.69728

Background. Kratom (Mitragyna speciosa) use is increasing internationally and case reports describe a range of withdrawal syndromes. Clinical guidance for recognizing and managing kratom withdrawal is limited. This narrative review of case reports synthesizes clinical features, management strategies, and outcomes among published patient cases. Aim. To characterize the clinical features, management strategies, and outcomes reported in published cases of kratom withdrawal. Additionally, identify common patterns in presentation and treatment that may inform preliminary clinical guidance for recognition and management. Methods. Article databases were searched for case studies related to kratom withdrawal. After screening titles/abstracts and full texts, 12 reports describing 16 individual patients were included. Data was extracted and findings were narratively synthesized across demographics/use characteristics, clinical presentation, pharmacological management, and outcomes. Results. Reported reasons for kratom use included self-treatment of opioid use disorder, pain, and psychiatric symptoms. Presentation varied from mild autonomic and gastrointestinal symptoms to severe, atypical syndromes. Opioid-like features of mild severity relative to usual opioid use predominated. Pharmacological management most commonly involved buprenorphine/naloxone. Clonidine and benzodiazepines were common adjuncts. Conclusions. Case-level evidence and existing literature indicates that kratom withdrawal most often presents as an opioid-like syndrome and that buprenorphine, with symptom-driven, conservative induction, was the most consistently effective treatment in reported cases. Interpretation is limited by small numbers, heterogeneous and incomplete reporting (dose/formulation/duration). Prospective, standardized reporting of exposure and outcomes and kratom-specific validation of withdrawal assessment tools are needed to inform evidence-based management.

**Решение:** -
