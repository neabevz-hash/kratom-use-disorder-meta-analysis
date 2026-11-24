"""Supplementary files built from the logs and the verified tables, so that every number matches the record of the work.

S1_deviations.md  - changes after registration (D1-D4) and clarifications (C1-C2), from deviations.md
S2_search.md      - search strategies, dates and counts per source (PRISMA-S), de-duplication, benchmark recall
S3_levels.md      - instruments, thresholds and case-definition levels (forms/instrument_thresholds.csv)
S4_ai.md          - generative AI: roles, models, version, prompts and their hashes, calibration, verification
S5_excluded.md    - reports excluded at full text with the reason, and linked components
S6_samples.md     - included studies, their reports and samples
S7_estimates.md   - every verified estimate (forms/estimates.csv)
S8_rob.md         - JBI risk-of-bias ratings per sample
S9_analyses.md    - Table S1 (sensitivity analyses, leave-one-out) and estimates not used in the analyses
Template: papers/sports-betting-prevalence/manuscript/make_supplement.py.
Run: .venv/Scripts/python.exe -I papers/kratom-use-disorder-prevalence/manuscript/make_supplement.py
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
OUT = HERE / "supplement"
RUN = PAPER / "search" / "runs" / "2026-11-21"
RES = PAPER / "analysis" / "results"
SOURCES = {"pubmed": ("PubMed", "NCBI E-utilities; kratom terms in title or abstract ([tiab]) and the MeSH term Mitragyna"),
           "europepmc": ("Europe PMC", "REST API; TITLE_ABS phrases"),
           "openalex": ("OpenAlex", "API; title_and_abstract.search, phrases joined by OR"),
           "openalex_non_en": ("OpenAlex, other languages", "API; one phrase per query (Thai, Malay, Russian, Japanese, Chinese, Korean)"),
           "s2": ("Semantic Scholar", "Graph API, bulk search, phrases joined by OR"),
           "scopus": ("Scopus", "Scopus Search API; TITLE-ABS-KEY"),
           "crossref": ("Crossref", "REST API, query.bibliographic; records kept only with a kratom term in title or abstract"),
           "datacite": ("DataCite", "REST API; titles and descriptions"),
           "openaire": ("OpenAIRE Graph", "API; research products of type publication"),
           "core": ("CORE", "API v3 (authenticated); title or abstract phrases"),
           "citations": ("Reference lists of seven syntheses", "OpenAlex referenced_works; records with a kratom term")}
REASONS = {"E4_no_dependence_measure": "No use-disorder or dependence measure for kratom",
           "E5_design": "Design (review, qualitative without counts, case series, preclinical)",
           "no_extractable_counts": "No extractable counts", "E2_no_kratom_user_estimate": "No estimate for people who use kratom",
           "E1_selected_sample": "Sample recruited because of kratom problems"}


def fmt(n) -> str:
    return f"{int(n):,}"


def cell(x, n: int | None = None) -> str:
    s = str(x or "").replace("|", "/").replace("\n", " ").strip()
    return s if n is None or len(s) <= n else s[: n - 1] + "…"


def rows(path: Path) -> list[dict]:
    return list(csv.DictReader(path.open(encoding="utf-8-sig")))


def records() -> dict[str, dict]:
    return {json.loads(l)["rec_id"]: json.loads(l) for l in (RUN / "records_unique.jsonl").open(encoding="utf-8")}


def s1() -> str:
    t = (PAPER / "deviations.md").read_text(encoding="utf-8")
    t = re.sub(r"(?m)^# .*\n", "", t)
    t = re.sub(r"(?m)^## (.+)$", r"**\1**", t)
    return ("**Supplementary File S1.** Changes after registration (D1–D4) and clarifications (C1–C2), as recorded in "
            "`deviations.md`\n\n" + t.strip() + "\n")


def s2() -> str:
    log = json.loads((RUN / "search_log.json").read_text(encoding="utf-8"))
    dd = json.loads((RUN / "dedup_report.json").read_text(encoding="utf-8"))
    rc = json.loads((RUN / "recall_seed_set.json").read_text(encoding="utf-8"))
    started = (RUN / "started_utc.txt").read_text(encoding="utf-8").split()[0].replace("T", " ").rstrip("Z")
    ps = log["_phrase_sets"]
    L = ["**Supplementary File S2.** Search strategies, dates and results per source (PRISMA-S)", "",
         f"Final search started {started} (UTC) with the frozen code of protocol v1.0 (git tag `kratom-prereg-v1.0`). "
         "Concept A (kratom) was searched in every source without date or language limits; concept B (people who use "
         "kratom, or dependence) was applied afterwards to titles and abstracts by `search/dedup.py`, identically for all "
         "sources (terms in protocol §8).", "",
         "**Kratom terms.** " + "; ".join(ps["kratom_terms"]) + ".", "",
         "**Non-English terms (OpenAlex).** " + "; ".join(ps["non_en"]) + ".", "",
         "| Source | Interface and query form | Searched (UTC) | Records |", "| --- | --- | --- | --- |"]
    for k, (name, how) in SOURCES.items():
        v = log.get(k, {})
        L.append(f"| {name} | {how} | {cell(v.get('searched_at_utc', ''))} | {fmt(v['records']) if 'records' in v else 'not searched'} |")
    L += ["", "**Query strings as sent** (from `search/runs/2026-11-21/search_log.json`):", "",
          f"- PubMed: `{cell(ps['pubmed_query'])}`", f"- Scopus: `{cell(ps['scopus_query'])}`"]
    for k in ("europepmc", "s2", "datacite"):
        for q in log[k]["meta"].get("queries", [])[:2]:
            L.append(f"- {SOURCES[k][0]}: `{cell(q.get('query'))}`")
    for f in log["openalex"]["meta"].get("filters", [])[:2]:
        L.append(f"- OpenAlex: `{cell(f.get('filter'))}`")
    cq = log["crossref"]["meta"].get("queries", {})
    L.append("- Crossref: " + "; ".join(f"\"{q}\" (scanned {fmt(v['scanned'])}, kept {fmt(v['kept_new'])})" for q, v in cq.items()))
    oq = log["openaire"]["meta"].get("queries", {})
    L.append("- OpenAIRE: " + "; ".join(f"`{cell(q)}` ({v.get('numFound', '')})" for q, v in oq.items()))
    L.append("- CORE: " + "; ".join(f"`{cell(q)}` ({v.get('totalHits', '')})" for q, v in log["core"]["meta"]["queries"].items()))
    L.append("- Reference lists of seven syntheses (DOIs): " + "; ".join(ps["syntheses_cited"]) + ".")
    L += ["", "**De-duplication and removal by rule** (`search/dedup.py`):", "",
          f"- Records identified: {fmt(dd['records_total'])}; unique after de-duplication on DOI, PMID and normalized title: "
          f"{fmt(dd['unique_records'])} ({fmt(dd['duplicates_removed'])} duplicates).",
          f"- Removed by rule: {fmt(dd['auto_removed_non_study_records'])} records typed as non-study by every source, "
          f"{fmt(dd['auto_removed_vendor_advertising'])} vendor advertisements, and records without a concept B term.",
          f"- Records screened: {fmt(dd['records_to_screen'])}.", "",
          f"**Benchmark recall.** {rc['seed_studies']} studies of people who use kratom that assessed use disorder or "
          "dependence, from the reference lists of earlier reviews: "
          f"{rc['in_screening_list']} of {rc['seed_studies']} were in the screening list.", "",
          "**Citation searching of the included reports** (after full-text screening; `search/citations_included.py`): "
          + citations_line(), ""]
    return "\n".join(L)


def citations_line() -> str:
    lg = json.loads((PAPER / "search" / "runs" / "2026-11-21-citations" / "log.json").read_text(encoding="utf-8"))
    return (f"{lg['included_reports']} included reports ({lg['seeds_in_openalex']} found in OpenAlex): "
            f"{fmt(lg['unique_records_found'])} records in their reference lists or citing them, "
            f"{fmt(lg['new_not_in_search'])} not found by the main search, {lg['new_with_kratom_term']} with a kratom term.")


def s3() -> str:
    L = ["**Supplementary File S3.** Instruments, thresholds and case-definition levels (protocol §13; completed before "
         "extraction, clarification C1)", "",
         "| Instrument | Full name | L1 | L2 | L3 | Code at L2 | Source of the thresholds | Notes |",
         "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in rows(PAPER / "forms" / "instrument_thresholds.csv"):
        L.append(f"| {r['instrument']} | {cell(r['full_name'])} | {r['L1_rule'] or '—'} | {r['L2_rule'] or '—'} | "
                 f"{r['L3_rule'] or '—'} | {r['code_at_L2']} | {cell(r['threshold_source'])} | {cell(r['notes'])} |")
    L += ["", "Levels are cumulative. Categories were extracted as printed and cumulative levels were built at analysis "
          "from contiguous categories (`analysis/build_levels.py`).", ""]
    return "\n".join(L)


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def s4() -> str:
    cal = json.loads((PAPER / "screening" / "decisions" / "calibration_stats.json").read_text(encoding="utf-8"))
    tiab = json.loads((PAPER / "screening" / "decisions" / "tiab_summary.json").read_text(encoding="utf-8"))
    corr = json.loads((PAPER / "extraction" / "decisions" / "correction_stats.json").read_text(encoding="utf-8"))
    qc = json.loads((PAPER / "extraction" / "decisions" / "quote_check.json").read_text(encoding="utf-8"))
    rule = cal["ai_rule_full_text_unless_both_exclude"]
    c = rule["counts"]
    prompts = [("Title-and-abstract screening", PAPER / "screening" / "llm_screener_prompt.md", "kratom-prereg-v1.0 (registered)"),
               ("Full-text eligibility proposals", PAPER / "fulltext" / "ft_prompt.md", "kratom-ft-prompt-v1.0"),
               ("Extraction and JBI drafts", PAPER / "extraction" / "extract_prompt.md", "kratom-extraction-prompt-v1.0")]
    L = ["**Supplementary File S4.** Use of generative AI", "",
         "Models: Claude Opus 5.5 (`claude-opus-5-5`) and Claude Sonnet 5.5 (`claude-sonnet-5-5`), Anthropic, run headless "
         "through Claude Code 2.1.289; the model and version were stored with every output. Runs: title-and-abstract passes "
         "21–22 November 2026 (2,304 records × 2 passes); full-text proposals 22–23 November 2026; extraction and risk-of-bias "
         "drafts 22–23 November 2026.", "",
         "| Task | Prompt file | Frozen under git tag | SHA-256 |", "| --- | --- | --- | --- |"]
    for task, p, tag in prompts:
        L.append(f"| {task} | `{p.relative_to(PAPER).as_posix()}` | `{tag}` | `{sha(p)[:16]}…` |")
    L += ["", f"**Calibration** (300 random records, the author blind to the model labels; labels sealed with SHA-256 before "
          f"unblinding). Rule \"full text unless both passes exclude\": sensitivity {rule['sensitivity']:.2f} "
          f"({c['tp']}/{c['tp'] + c['fn']}), specificity {rule['specificity']:.2f} ({c['tn']}/{c['tn'] + c['fp']}), "
          f"κ = {rule['kappa']:.2f}. Agreement between passes: κ = {cal['passes_agreement_full_text_vs_exclude']['kappa']:.2f}. "
          f"Records missed by the rule: {len(cal['rule_false_negatives'])}; safeguard triggered.", "",
          f"**Safeguard.** {fmt(tiab['safeguard']['re_screened'])} double exclusions with a term for people or without an "
          f"abstract re-screened blind by the author: {tiab['safeguard']['moved_to_full_text']} moved to full text; "
          f"{fmt(tiab['safeguard']['not_re_screened'])} double exclusions without such terms not re-screened.", "",
          f"**Records retained by at least one pass.** {tiab['verification']['records']} decided by the author with the "
          f"model labels shown; {tiab['to_full_text']} reports sought in total.", "",
          f"**Extraction.** {corr['verified_samples']} samples, {corr['drafted_estimates']} estimates, "
          f"{fmt(corr['drafted_values'])} drafted values verified by the author against the sources; "
          f"{corr['values_corrected']} corrected ({100 * corr['share_corrected']:.2f}%). Model quotations found verbatim in "
          f"the source: {100 * qc['estimates']['share_found']:.0f}% of estimates and {100 * qc['key_fields']['share_found']:.0f}% "
          "of key fields (the rest were paraphrased tables or text broken by PDF conversion; each value was checked by the "
          "author regardless).", "",
          "**Manuscript.** Claude Code wrote the search, screening and analysis code and drafted the text from the author's "
          "analysis outline; the author revised and approved the text.", ""]
    return "\n".join(L)


def s5() -> str:
    recs = records()
    ft = [r for r in rows(PAPER / "fulltext" / "decisions" / "ft_R1.csv") if r["decision"] == "not_eligible"]
    L = ["**Supplementary File S5.** Reports excluded at full text", "",
         "| Record | First author (year) | Title | DOI | Reason |", "| --- | --- | --- | --- | --- |"]
    for r in sorted(ft, key=lambda r: (REASONS.get(r["reason"], r["reason"]), r["rec_id"])):
        u = recs.get(r["rec_id"], {})
        L.append(f"| {r['rec_id']} | {cell(u.get('first_author'))} ({u.get('year', '')}) | {cell(u.get('title'), 120)} | "
                 f"{u.get('doi', '') or '—'} | {REASONS.get(r['reason'], r['reason'])} |")
    L += ["", "**Duplicates or components of another report** (supplementary files, conference abstracts and versions of "
          "an included or assessed report):", "", "| Record | Component of | Why |", "| --- | --- | --- |"]
    for r in rows(PAPER / "fulltext" / "linked_components.csv"):
        L.append(f"| {r['rec_id']} | {r['component_of']} | {cell(r['why'])} |")
    return "\n".join(L) + "\n"


def s6() -> str:
    L = ["**Supplementary File S6.** Included studies, their reports and samples", "",
         "| Study | Record | Role | First author (year) | DOI | Title | Link between reports |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for r in rows(PAPER / "extraction" / "study_map.csv"):
        L.append(f"| {r['study_id']} | {r['rec_id']} | {'main' if r['role'].startswith('main') else 'attached'} | "
                 f"{cell(r['first_author'])} ({r['year']}) | {r['doi'] or '—'} | {cell(r['title'], 110)} | {cell(r['link_reason'], 160) or '—'} |")
    L += ["", "| Sample | Study | First author (year) | Country | Data years | Sample type | Sampling | Recruitment | Use period "
          "| Regular use required | Product | n | Mean age | Male, % | Instruments |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for s in rows(PAPER / "forms" / "samples.csv"):
        L.append(f"| {s['sample_id']} | {s['study_id']} | {cell(s['first_author'])} ({s['year']}) | {s['country']} | "
                 f"{s['data_years']} | {s['sample_type']} | {s['sampling']} | {s['recruitment_channel']} | {s['use_period']} | "
                 f"{cell(s['regular_use_required'], 80)} | {s['product_form']} | {s['n_users']} | {s['age_mean']} | "
                 f"{s['pct_male']} | {cell(s['instruments'], 140)} |")
    return "\n".join(L) + "\n"


def s7() -> str:
    L = ["**Supplementary File S7.** Verified estimates (every category as published; `forms/estimates.csv`)", "",
         "| Estimate | Sample | Subgroup | Instrument | Threshold | Cumulative | Level | Time frame | Cases | n | Location |",
         "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for e in rows(PAPER / "forms" / "estimates.csv"):
        L.append(f"| {e['estimate_id']} | {e['sample_id']} | {cell(e['subgroup'], 50)} | {e['instrument']} | "
                 f"{cell(e['threshold'], 60)} | {e['cumulative']} | {e['level']} | {e['time_frame']} | {e['cases']} | "
                 f"{e['n']} | {cell(e['location'], 60)} |")
    return "\n".join(L) + "\n"


def s8() -> str:
    items = ["Sample frame appropriate", "Participants sampled appropriately", "Sample size adequate",
             "Subjects and setting described", "Coverage of the sample adequate", "Valid methods to identify the condition",
             "Condition measured reliably and in the same way", "Appropriate statistical analysis", "Response rate adequate"]
    L = ["**Supplementary File S8.** Risk of bias: JBI Critical Appraisal Checklist for Prevalence Studies (drafted by the "
         "model with quotations, verified by the author)", "",
         "Items: " + "; ".join(f"{i}. {t}" for i, t in enumerate(items, 1)) + ".", "",
         "| Sample | First author (year) | " + " | ".join(str(i) for i in range(1, 10)) + " |",
         "| --- | --- | " + " | ".join("---" for _ in range(9)) + " |"]
    for s in rows(PAPER / "forms" / "samples.csv"):
        L.append(f"| {s['sample_id']} | {cell(s['first_author'])} ({s['year']}) | "
                 + " | ".join(s[f"jbi_{i}"] for i in range(1, 10)) + " |")
    return "\n".join(L) + "\n"


def s9() -> str:
    t = (HERE / "tables.md").read_text(encoding="utf-8")
    ts1 = t[t.index("**Table S1.**"):].strip()
    L = ["**Supplementary File S9.** Additional analyses", "", ts1, "",
         "**Estimates not used in the pooled analyses** (a higher-priority estimate of the same sample and level was used):", "",
         "| Sample | Level | Code | Instrument | Time frame | Cases | n | % |", "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in rows(RES / "estimates_not_used.csv"):
        L.append(f"| {r['sample_id']} | {r['level']} | {r['code']} | {r['instrument']} | {r['time_frame']} | {r['cases']} | "
                 f"{r['n']} | {r['pct']} |")
    return "\n".join(L) + "\n"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.mkdir(exist_ok=True)
    parts = {"S1_deviations.md": s1, "S2_search.md": s2, "S3_levels.md": s3, "S4_ai.md": s4, "S5_excluded.md": s5,
             "S6_samples.md": s6, "S7_estimates.md": s7, "S8_rob.md": s8, "S9_analyses.md": s9}
    for name, fn in parts.items():
        text = fn()
        (OUT / name).write_text(text, encoding="utf-8", newline="\n")
        print(f"{name}: {len(text):,} chars")


if __name__ == "__main__":
    main()
