# Kratom use disorder among people who use kratom: data and code

This repository contains the records, decisions, extracted data and analysis code for

> Rekhert, M. (2026). *How common is kratom use disorder among people who use kratom? A systematic review and meta-analysis* [Manuscript submitted for publication]. Preprint: https://doi.org/10.5281/zenodo.24512208

- Protocol (OSF Registries, registered 21 November 2026 before the final search and screening): https://doi.org/10.17605/OSF.IO/6D7N3
- Archived release (Zenodo): forthcoming
- Author: Martin Rekhert, Higher School of Psychology, Turan University, Almaty, Kazakhstan (ORCID [0009-0001-2402-2031](https://orcid.org/0009-0001-2402-2031))

## The review in brief

- **Question.** What proportion of people who use kratom meet criteria for kratom use disorder (KUD) or dependence at three levels — any KUD (L1, DSM-5 ≥ 2 criteria), moderate-to-severe KUD or dependence (L2, DSM-5 ≥ 4, DSM-IV/ICD dependence or a dependence-scale cut-off; primary), severe KUD (L3, DSM-5 ≥ 6) — and how do region, sampling and measurement shape the estimates?
- **Search.** 21 November 2026: PubMed, Europe PMC, OpenAlex (also Thai, Malay, Russian, Japanese, Chinese and Korean queries), Semantic Scholar, Scopus, Crossref, DataCite, OpenAIRE, CORE and the reference lists of seven syntheses; no date or language limits; 17,526 records, 2,304 screened; benchmark recall 9/9.
- **Selection.** One reviewer (the author) decided every record kept by the AI passes and every full text. Two AI passes (Claude Opus 5.5 and Claude Sonnet 5.5 through Claude Code 2.1.289, fixed prompt registered with the protocol) labelled titles and abstracts; a blind calibration of 300 records triggered the pre-specified safeguard (blind re-screening of 1,154 double exclusions; none moved). Full texts from open-access sources plus seven reports obtained by hand (deviation D3); 94 assessed with AI proposals, every decision by the reviewer. The AI drafted the extraction and risk-of-bias forms; the reviewer verified every value (4 of 1,596 corrected).
- **Included.** 18 reports, 14 studies, 14 samples (6,859 people who use kratom; USA, Malaysia, Thailand, Czechia); 13 samples in the meta-analyses.
- **Analysis.** Binomial–normal GLMMs on the logit scale (`metafor`, with `lme4` when `metafor` did not converge), a multilevel binomial GLMM over all estimates (`lme4`), GRADE for event rates.
- **Main results.** Any KUD 30.8% (95% CI 22.5–40.7; k = 7), L2 29.1% (6.9–69.4; k = 12; sample estimates 0–100%), severe KUD 5.1% (2.7–9.3; k = 5). US consumers (DSM-5): any 28.6%, moderate-to-severe 10.2%, severe 6.5%. Samples restricted to regular users: OR 23.7 (2.0–282); region not associated after adjustment. DSM-5 criteria or interviews only: L2 10.5%. Low to very low certainty of evidence.

## Repository layout

All study files are under `papers/kratom-use-disorder-prevalence/`.

| Path | Contents |
| --- | --- |
| `protocol.md` | Protocol v1.0 (frozen 21 November 2026, git tag `kratom-prereg-v1.0` in the working repository; registered on OSF) |
| `deviations.md` | Every change and clarification after registration, dated (D1–D4, C1–C2; Supplementary File S1) |
| `registration/` | The OSF registration form text, the scripts that built and checked the registration |
| `search/` | Search, de-duplication and recall scripts; `runs/2026-11-21/`: search log with every query, raw exports (zip; Scopus records not redistributed), unique records, screening list (CSV, RIS), recall on the benchmark set; `runs/2026-11-21-citations/`: citation searching of the included reports |
| `screening/` | AI screening prompt and runner, both AI passes with the SHA-256 of the label files, blind calibration, safeguard re-screening, verification worksheets and final decisions (`decisions/tiab_final.csv`) |
| `fulltext/` | Retrieval scripts and log, the full-text prompt and AI proposals (`llm/`), the reviewer's worksheets and decisions (`decisions/ft_R1.csv`), linked components, PRISMA counts |
| `extraction/` | Study map (reports → studies), extraction prompt and runner, AI drafts (`draft/`), the reviewer's verification worksheets (`verify/`) and verified values (`decisions/`), quote and correction audits, `finalize.py` |
| `forms/` | Extraction codebook, levels table (`instrument_thresholds.csv`), risk-of-bias rules, and the analysis tables `samples.csv` and `estimates.csv` |
| `analysis/` | `build_levels.py` (cumulative levels from the extracted categories), `analysis.R` (all pre-specified analyses), `posthoc.R` (deviation D4), `grade.py`, `prisma.R`; `data/`, `results/` and `figures/` as reported |
| `manuscript/` | Scripts for Tables 1–4 (`make_tables.py` → `tables.md`), Supplementary Files S1–S9 (`make_supplement.py` → `supplement/`) and the reference list (`make_refs.py` → `references.md`) |
| `harness/` | `llmaudit`: the Claude Code runner used for the AI drafts, agreement statistics (κ, AC1) |

Reviewer worksheets (`*.md` under `screening/`, `fulltext/decisions/`, `extraction/verify/`) have instructions in Russian, the reviewer's working language; records, AI drafts and decisions are in English, and every decision is also in a CSV file.

Not included: full texts and PDFs of the reports (copyright), raw Scopus records (licence terms), API keys.

## Reproducing the analysis

The analysis runs from the released files and needs no API access. Tested with Python 3.12 and R 4.6.1 (metafor, lme4, dplyr, readr, tidyr, ggplot2, jsonlite).

```bash
# verified extraction -> analysis tables (forms/samples.csv, forms/estimates.csv)
python papers/kratom-use-disorder-prevalence/extraction/finalize.py --run 2026-11-21
# cumulative levels from the extracted categories
python papers/kratom-use-disorder-prevalence/analysis/build_levels.py
# meta-analysis -> analysis/results/, analysis/figures/
Rscript papers/kratom-use-disorder-prevalence/analysis/analysis.R
Rscript papers/kratom-use-disorder-prevalence/analysis/posthoc.R
python papers/kratom-use-disorder-prevalence/analysis/grade.py
Rscript papers/kratom-use-disorder-prevalence/analysis/prisma.R
# Tables 1-4 and Supplementary Files S1-S9
python papers/kratom-use-disorder-prevalence/manuscript/make_tables.py
python papers/kratom-use-disorder-prevalence/manuscript/make_supplement.py
```

Run the commands from the repository root. The release was checked by running them in a clean copy: the analysis tables, the level estimates, all result files, Tables 1–4 and Supplementary Files S1–S9 came out identical (line endings aside).

Re-running the search, retrieval or the AI drafts needs network access and keys (`.env.example`): `OPENALEX_API_KEY`, `CORE_API_KEY` and `ELSEVIER_API_KEY` for the search, and `CLAUDE_CODE_OAUTH_TOKEN` (output of `claude setup-token`) for the Claude Code runs. Python packages for those steps: `httpx`, `lxml`, `pyyaml`, `jsonschema`, `pymupdf` (`pip install -e harness`).

## Licenses and citation

Code (`*.py`, `*.R`, `harness/`): MIT (`LICENSE`). Data and documents: CC BY 4.0 (`LICENSE-DATA.md`); bibliographic records, abstracts and quotations from the included reports remain with their copyright holders. Please cite the article and this repository (`CITATION.cff`).
