"""Tables of the manuscript from the analysis results (analysis/results/*.csv, analysis/data/primary.csv, forms/samples.csv).

Writes manuscript/tables.md: Table 1 (characteristics of the 14 samples), Table 2 (pooled prevalence by level and subgroup),
Table 3 (moderators and post hoc contrasts), Table 4 (GRADE summary of findings, rules in deviations.md C2), and
Table S1 (all sensitivity analyses) for the supplement. Template: papers/sports-betting-prevalence/manuscript/make_tables.py.
Run: .venv/Scripts/python.exe -I papers/kratom-use-disorder-prevalence/manuscript/make_tables.py
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
RES = PAPER / "analysis" / "results"
COUNTRY = {"USA": "USA", "MYS": "Malaysia", "THA": "Thailand", "CZE": "Czechia"}
SAMPLE = {"S01": "Daily users, community", "S02": "Adults who use kava or kratom, online", "S03": "Military conscripts",
          "S04": "Regular users, community", "S05": "Adults who used kratom, online", "S06": "Regular users, online",
          "S07": "Regular users, community", "S08": "Long-term users, community",
          "S09": "Adults with lifetime use, online (mTurk)", "S10": "Kratom users, online", "S11": "Current consumers, online",
          "S12": "Regular users, community", "S13": "Hospital support staff", "S14": "Regular users, community"}
REGULAR = {"S01": "daily, ≥ 1 year", "S04": "daily, 12 months", "S06": "≥ 3 times a week, ≥ 4 weeks", "S07": "weekly",
           "S08": "≥ 2 years", "S12": "≥ 2 times a day, > 1 year", "S14": "≥ 6 months"}
AUTHOR = {"S12": "Leong Bin Abdullah"}   # first author as printed (samples.csv keeps the short form)
STUDY = {"S09": "Smith et al. (2022)", "S11": "Hill et al. (2024)"}


def rows(name: str, folder: Path = RES) -> list[dict]:
    return list(csv.DictReader((folder / name).open(encoding="utf-8")))


def fm(x) -> str:
    return f"{float(x):.1f}"


def ci(r: dict) -> str:
    return "not pooled (k < 3)" if r["prev"] in ("", "NA") else f"{fm(r['prev'])} ({fm(r['lo'])}–{fm(r['hi'])})"


def pi(r: dict) -> str:
    return "" if r["pi_lo"] in ("", "NA") else f"{fm(r['pi_lo'])}–{fm(r['pi_hi'])}"


def line(label: str, r: dict) -> str:
    i2 = "" if r["I2"] in ("", "NA") else r["I2"]
    return f"| {label} | {r['k']} | {int(float(r['n'])):,} | {ci(r)} | {pi(r)} | {i2} |"


def orci(r: dict, a="OR", lo="lo", hi="hi") -> str:
    return f"{r[a]} ({r[lo]}–{r[hi]})"


def table1(samples: list[dict], est: dict) -> list[str]:
    L = ["**Table 1.** Characteristics of the included samples and their estimates.", "",
         "| Study | Country (data years) | Sample; recruitment | n | Regular use required | Instrument | L1/L2/L3, % | JBI 2/6/9 |",
         "|---|---|---|---|---|---|---|---|"]
    yn = {"yes": "Y", "no": "N", "unclear": "U"}

    def p(sid, lv):
        r = est.get((sid, lv))
        if not r:
            return "–"
        return r["pct"] + {"L2-scale": "†", "L2-screen": "‡"}.get(r["code"], "")

    for s in sorted(samples, key=lambda s: (s["region"] != "North America", s["region"], s["year"])):
        sid = s["sample_id"]
        ins = sorted({est[(sid, lv)]["instrument"] for lv in ("L1", "L2", "L3") if (sid, lv) in est}) or ["KDS"]
        rc = s["recruitment_channel"]
        rec = "advocacy or vendor channels" if rc == "advocacy or vendor channels" else ("not stated" if rc == "NR" else "general")
        dy = s["data_years"] if s["data_years"] not in ("", "NR") else "NR"
        jbi = "/".join(yn.get(s[f"jbi_{i}"], s[f"jbi_{i}"]) for i in (2, 6, 9))
        L.append(f"| {AUTHOR.get(sid, s['first_author'])} ({s['year']}) | {COUNTRY[s['country']]} ({dy}) | {SAMPLE[sid]}; {rec} | "
                 f"{int(float(s['n_users'])):,} | {REGULAR.get(sid, 'no')} | {', '.join(ins)} | "
                 f"{p(sid, 'L1')}/{p(sid, 'L2')}/{p(sid, 'L3')} | {jbi} |")
    L += ["", "L1, any use disorder (DSM-5 ≥ 2 criteria); L2, moderate-to-severe use disorder (DSM-5 ≥ 4) or dependence; "
          "† dependence scale (KDS ≥ 14, SDS or LDQ at the authors' cut-off); ‡ ASSIST ≥ 27; L3, severe use disorder "
          "(DSM-5 ≥ 6). Leong Bin Abdullah (2019) reported only KDS ≥ 35 beside a merged 0–34 band (43/150, 28.7%), which fits "
          "no level; it is described but not pooled. JBI items: 2, participants sampled appropriately; 6, valid methods for "
          "identifying the condition; 9, adequate response rate (Y, yes; N, no; U, unclear). ASSIST, Alcohol, Smoking and "
          "Substance Involvement Screening Test; DSM-5-SUD, DSM-5 substance use disorder checklist; KDS, Kratom Dependence "
          "Scale; LDQ, Leeds Dependence Questionnaire; SDS, Severity of Dependence Scale; SUDST, Substance Use Disorder "
          "Screening Test (DSM-5 checklist); NR, not reported.", ""]
    return L


def table2() -> list[str]:
    pooled = {r["analysis"]: r for r in rows("pooled.csv")}
    sens = {r["analysis"].split(" ")[0]: r for r in rows("sensitivity.csv") if not r["analysis"].startswith("10")}
    L = ["**Table 2.** Pooled prevalence of kratom use disorder and dependence among people who use kratom.", "",
         "| Analysis | k | n | % (95% CI) | 95% PI | I², % |", "|---|---|---|---|---|---|"]
    order = [("All samples", None), ("L1 any use disorder", "L1 any use disorder"),
             ("L2 moderate-to-severe or dependence (primary)", "L2 moderate-to-severe or dependence (primary)"),
             ("L3 severe use disorder", "L3 severe use disorder"), ("North America", None),
             ("L1 any use disorder", "L1, North America"), ("L2 moderate-to-severe", "L2, North America"),
             ("L3 severe", "L3, North America"),
             ("Southeast Asia", None), ("L2 moderate-to-severe or dependence", "L2, Southeast Asia"),
             ("Europe", None), ("L2 dependence (SDS, LDQ)", "L2, Europe"),
             ("L2 by sample type", None), ("Online consumers", "L2, online consumers"),
             ("Community users", "L2, community users")]
    for label, key in order:
        L.append(f"| **{label}** | | | | | |" if key is None else line(label, pooled[key]))
    L += ["| **L2 by case definition** | | | | | |", line("DSM-5 criteria or interview only", sens["1"]),
          "", "Binomial–normal generalized linear mixed models with a logit link. The Southeast Asia model did not "
          "converge in metafor and was fitted with lme4 (Wald CI; prediction interval from τ). PI, prediction interval. "
          "All sensitivity analyses: Table S1.", ""]
    return L


def table3() -> list[str]:
    m = {r["term"]: r for r in rows("multilevel_prespecified.csv")}
    reg = rows("subgroup_tests.csv")[0]
    tr = rows("posthoc_frequency_trend.csv")[0]
    mb = rows("meta_bias.csv")
    sea, eur = m["region3Southeast Asia"], m["region3Europe"]
    L = ["**Table 3.** Moderators of prevalence and post hoc within-study contrasts.", "",
         "| Analysis | Contrast | OR (95% CI) | p |", "|---|---|---|---|",
         f"| Pre-specified multilevel model, all estimates (13 samples) | L2 vs L1 | {orci(m['level3L2'])} | < 0.001 |",
         f"| | L3 vs L1 | {orci(m['level3L3'])} | < 0.001 |",
         f"| | Regular use required vs not | {orci(m['regularyes'])} | {float(m['regularyes']['p']):.3f} |",
         f"| | Southeast Asia vs North America | {orci(sea)} | {float(sea['p']):.2f} |",
         f"| | Europe vs North America | {orci(eur)} | {float(eur['p']):.2f} |",
         f"| Region, L2 only (GLMM, k = 12) | Southeast Asia vs North America | "
         f"{orci(reg, 'OR_SEA_vs_NA', 'OR_SEA_lo', 'OR_SEA_hi')} | {float(reg['p']):.2f} (omnibus) |",
         f"| Post hoc: dosing frequency, Hill et al. (2024), n = {int(float(tr['n'])):,} | per additional daily dose (1–6); "
         f"any use disorder {tr['pct_1_dose']}% at 1 vs {tr['pct_5_6_doses']}% at 5–6 doses a day | "
         f"{tr['OR_per_dose']} ({tr['lo']}–{tr['hi']}) | < 0.001 |"]
    for r in rows("posthoc_sex.csv"):
        L.append(f"| Post hoc: sex, {STUDY.get(r['sample_id'], r['sample_id'])} | men vs women, any use disorder "
                 f"({fm(r['pct_male'])}% vs {fm(r['pct_female'])}%) | {orci(r)} | |")
    L += [f"| Small-study effects, L2 | logit prevalence on 1/√n (REML, Hartung–Knapp) | slope {mb[0]['estimate']} | {float(mb[0]['p']):.2f} |",
          f"| Publication status, L2 | journal vs grey literature (GLMM) | log-OR {mb[1]['estimate']} | {float(mb[1]['p']):.2f} |",
          "", "The multilevel model nests estimates (L1, L2, L3) within samples (binomial GLMM, lme4, Wald CI). Regular use "
          "required: the sample was restricted to people using kratom at least weekly or daily, or for a minimum period "
          "(Table 1).", ""]
    return L


def table4() -> list[str]:
    L = ["**Table 4.** GRADE summary of findings (event rates; rules fixed before rating, deviations C2).", "",
         "| Outcome | k | Prevalence, % (95% CI) | Risk of bias | Inconsistency | Imprecision | Indirectness | Publication bias | Certainty |",
         "|---|---|---|---|---|---|---|---|---|"]
    for r in rows("grade.csv"):
        L.append(f"| {r['outcome']} | {r['k']} | {r['prevalence'].replace('-', '–')} | {r['risk_of_bias']} | "
                 f"{r['inconsistency']} | {r['imprecision']} | {r['indirectness']} | {r['publication_bias']} | **{r['certainty']}** |")
    L += ["", "Start: high (prevalence in the target population). One level down for each serious concern (two for very "
          "serious inconsistency). Indirectness: most participants came from samples recruited through advocacy or vendor "
          "channels or restricted to regular use.", ""]
    return L


def table_s1() -> list[str]:
    pooled = {r["analysis"]: r for r in rows("pooled.csv")}
    L = ["**Table S1.** Sensitivity analyses of the primary outcome (L2).", "",
         "| Analysis | k | n | % (95% CI) | 95% PI | I², % |", "|---|---|---|---|---|---|",
         line("Primary analysis", pooled["L2 moderate-to-severe or dependence (primary)"])]
    for r in rows("sensitivity.csv"):
        L.append(line(r["analysis"], r))
    return L + [""]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    samples = rows("samples.csv", PAPER / "forms")
    est = {(r["sample_id"], r["level"]): r for r in rows("primary.csv", PAPER / "analysis" / "data")}
    L = ["# Tables (generated by make_tables.py; do not edit by hand)", ""]
    L += table1(samples, est) + table2() + table3() + table4() + table_s1()
    (HERE / "tables.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    main()
