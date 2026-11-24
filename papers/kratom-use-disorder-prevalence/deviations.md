# Deviations from the registered protocol (v1.0)

Every change after registration is dated, justified and reported in the registration and in the paper (protocol §4).

## D1. Registration files not attached (2026-11-22)

- **Protocol (§2):** the OSF registration carries the frozen protocol and the registration package.
- **What happened:** the registration (https://osf.io/6d7n3, registered 2026-11-21 at 15:02:37 UTC, public) was submitted with both file fields empty: OSF no longer creates projects (since 2026-11-16), files have to be uploaded into the form's file fields, and they were not. OSF does not allow files to be added after submission.
- **What the registration does hold:** all 61 text fields. Checked through the OSF API (`registration/verify_osf.py` → `registration/osf_check.json`): 59 of 60 fields in `registration/osf.md` match verbatim; in "Query strings" OSF removed the text `<term>` inside angle brackets (as in the sports-betting registration); the exact strings are in the protocol and `search/runs/2026-11-21/search_log.json`.
- **The package:** built from the tag `kratom-prereg-v1.0` (commit 6fbbde0) before the registration. SHA-256: `Rekhert_kratom_protocol_v1.0.pdf` aefc3816324918df7589404c895482f654518cc852e55414ff20e80dfb6eb631; `kratom-prereg-v1.0.zip` 61348e6a87bbd13bc8ad5f673c4a69ff016b9fafcaf7a64978011646d1216295; `llm_screener_prompt.md` 9cdeef328dfda32953e55e2326434b8711c21aa0280a420bee4ddbe5c72a80a9; `extraction_codebook.md` e8ab5b503f2743bc6a872acbebae8dd564585c4949ea5f25a59c9a68e3c69bbf. The same files are released unchanged with the data (GitHub, Zenodo) at submission.
- **Effect on the review:** none on the methods; the order registration → final search (15:04:44 UTC) → screening is kept.

## D2. AI passes interrupted and resumed (2026-11-21/22)

- The two AI passes started on 2026-11-21 stopped after 441 (Opus) and 448 (Sonnet) records when the desktop application restarted; 9 and 16 calls had failed to start (Windows status 0xC0000142) and are retried on resume. The runner resumes from the label file (records already labelled are not sent again), with the same prompt, models and seeded order; concurrency 3 instead of 4. No record has two labels (checked).

## C1. Levels table completed before extraction (clarification, 2026-11-22)

Protocol §13: the levels table is completed for every instrument found in the included studies before extraction, from development and validation papers; logged as a clarification, not a change of rule. Instruments in the 14 included reports: DSM-5 checklists, KDS, SDS, LDQ, the Thai SUDST and ASSIST (`forms/instrument_thresholds.csv`).
- **KDS:** the score system of Saingam et al. (2014; 16 items, 0–48) — bands 0–13 low or mild, 14–34 moderate, 35–48 high or severe — as applied and cited in two included reports (R0060; R2129, which prints the moderate band as 13–34). The development paper is not open access; its abstract gives the same cut-offs ("Two cutoffs were suggested: 34/35 for distinguishing moderate from high dependence and 13/14 for low from moderate", Saingam et al., 2014, 10.1080/08897077.2014.924464; checked 2026-11-22). The lowest band includes a score of 0 and is not a case; **L2-scale = moderate or high band (≥ 14)**. The high band is not L3, which stays DSM-5 severe only.
- **SDS:** no cut-off validated in people who use kratom was found; the authors' fixed cut-off is used and coded L2-scale (R1294: share scoring ≥ 6).
- **LDQ:** no validated kratom bands were found; L2-scale = the authors' medium or moderate band or higher; a count for the high band alone is not levelled (listed only).
- **SUDST** (Saengduenchai et al., 2023, 10.31584/jhsmr.2023932): 11 yes/no items, one per DSM-5 criterion; 2–3 low, 4–5 moderate, ≥ 6 high. Treated as a DSM-5 criteria checklist: L1 ≥ 2, L2 ≥ 4, L3 ≥ 6.
- **ASSIST:** as registered (high risk ≥ 27 = L2-screen; moderate 4–26 recorded, not pooled).

## D3. Closed full texts requested from authors (2026-11-22)

- **Protocol (§11b):** open-access full texts only; authors are not contacted.
- **Change (R1's decision, 2026-11-22):** only 80 of 235 reports sought were open access, and the closed ones include the largest US study of kratom use disorder and the core Malaysian and Thai studies (31 of the 44 records R1 had labelled include at title and abstract). R1 requests copies of 15 closed reports from their authors (e-mail or ResearchGate full-text requests) and downloads by hand 5 open copies that the scripts could not reach (`fulltext/REQUESTS.md`).
- **Rules fixed before any copy arrives:** copies received by 2026-12-06 go through the same full-text procedure (the frozen AI proposal prompt, R1's decision, extraction and verification); the rest stay "reports not retrieved". Reports obtained this way are flagged (`source = author copy`) and tested in a sensitivity analysis (excluding them). The search, the screening decisions and the analysis plan do not change.
- **What was done (2026-11-23):** R1 downloaded 7 reports by hand (author-posted or repository copies found through Google Scholar and ResearchGate, and one repository thesis); 4 were eligible (R1255, R3639, R2844, R0243). R1 then decided not to e-mail authors, so no requests were sent and the cut-off of 2026-12-06 no longer applies. The 4 reports are flagged `manual_pdf` in `fulltext/retrieval_log.csv`; sensitivity analysis without them is reported.
- **Extraction corrections by R1 (2026-11-23):** ST13 (R2844) severe KDS band set to not_levelled, because mild and moderate were reported together and the share at KDS ≥ 14 cannot be built (C1); ST14 (R0243) leaf users set as the whole sample.
- **Analysis note:** with a 0% (ST14, ASSIST high risk 0/80) and a 100% sample (ST15, LDQ moderate or severe 293/293), `rma.glmm` did not converge for the Southeast Asia subgroup; the same binomial–normal model was fitted with `lme4::glmer` (bobyqa), as written in `analysis/analysis.R`.

## C2. GRADE rules (clarification, 2026-11-23)

Protocol §17 names the domains; the thresholds were fixed in `analysis/grade.py` before rating: start high; downgrade one level for risk of bias (more than half of the samples "no" on JBI 2, 6 or 9), inconsistency (prediction interval wider than 20 percentage points; two levels if wider than 50), imprecision (CI half-width above 5 points), indirectness (more than half of the participants from advocacy- or vendor-recruited samples or samples selected for regular use) and publication bias (small-study association p < 0.10). Results: `analysis/results/grade.csv`.

## D4. Post hoc analyses (2026-11-23)

Not in the protocol, labelled post hoc in the paper (`analysis/posthoc.R`): (1) within-study frequency gradient — any use disorder by daily dosing frequency in the largest sample (S11, Hill et al. 2024; logistic regression on 1–6 doses per day); (2) sex — odds ratio (male vs female) for any use disorder in the two samples that report it, not pooled (k < 3); (3) comparison with published pooled prevalences of cannabis use disorder among people who use cannabis (Leung et al., 2020; Dawson et al., 2024), descriptive only.
