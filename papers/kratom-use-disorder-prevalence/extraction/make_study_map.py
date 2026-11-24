"""Study map and extraction jobs (protocol §11b, linking reports): 14 included reports → 11 studies.

Links are judged from site, years of data collection and sample size (the AI full-text proposals flagged them; R1 sees
them in the verification files). Writes extraction/study_map.csv and extraction/jobs.json.
Run: .venv/Scripts/python.exe -I papers/kratom-use-disorder-prevalence/extraction/make_study_map.py --run 2026-11-21
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from common import eligible_reports, load_records  # noqa: E402

# study_id: (main, attached, link_reason, samples instruction)
STUDIES = {
    "ST01": ("R0060", [], "", "One sample: 100 daily male kratom users, Penang community, 2024-2025."),
    "ST02": ("R0816", [], "", "One sample: the kratom users of the US online survey of kava and kratom users (2023-2024); "
             "kava-only users are not part of it. If people who use both are reported separately, keep all kratom users as the sample."),
    "ST03": ("R0922", [], "", "One sample: the conscripts who used kratom (state the reference period used for the "
             "denominator: lifetime, past 12 months or current). Extract SUDST and ASSIST estimates for them."),
    "ST04": ("R1857", ["R1161"], "Same Penang case-control sample of 60 regular kratom users (USM/AMDI, recruited 2019-2020): "
             "R1857 (PLOS ONE 2023) and R1161 (PhD thesis, 2024)",
             "One sample: the 60 regular kratom users (controls are not part of it). R1857 gives the DSM-5 assessment by a "
             "psychiatrist; R1161 (attached) gives KDS results if reported."),
    "ST05": ("R1294", [], "", "One sample: the adults who used kratom (state whether lifetime or past-30-day users are the "
             "denominator of the SDS estimate)."),
    "ST06": ("R1402", ["R1425"], "Same NIDA nationwide remote EMA study of US adults who use kratom regularly (enrolled "
             "July-November 2022, n = 395 surveyed): R1402 (baseline DSM-5 KUD by severity) and R1425 (EMA paper)",
             "One sample: the 395 surveyed at baseline. Use R1402 for the DSM-5 estimates; R1425 (attached) only for "
             "values R1402 does not give."),
    "ST07": ("R2039", [], "", "One sample: 10 regular kratom users interviewed in Czechia (LDQ scores)."),
    "ST08": ("R2129", [], "", "One sample: the long-term kratom users (controls are not part of it); KDS bands."),
    "ST09": ("R2149", ["R2153"], "Same US mTurk re-contact survey of adults with lifetime kratom use (April-May 2021, "
             "n = 129 evaluable): R2149 (KUD and withdrawal) and R2153 (dose-effect paper)",
             "One sample: the 129 evaluable respondents (or the denominator R2149 uses for KUD). Use R2149; R2153 "
             "(attached) only for values R2149 does not give."),
    "ST10": ("R2648", [], "", "One sample: the Johns Hopkins online survey of kratom users (2017)."),
    # ST11 (R3754 alone) was replaced on 2026-11-23 by ST15, after the article of the same sample arrived (D3)
    "ST12": ("R1255", [], "", "One sample: the current US kratom consumers of the 2023 online survey (n = 2,061)."),
    "ST13": ("R2844", [], "", "One sample: 150 regular kratom users in Malaysia (KDS, Malay version)."),
    "ST14": ("R0243", [], "", "One sample: the hospital support staff who used kratom (state whether lifetime leaf users, "
             "kratom cocktail users or both are the denominator); ASSIST risk bands for kratom."),
    "ST15": ("R3639", ["R3754"], "Same sample of 293 regular male kratom users in Penang, Kedah and Perlis: R3639 (Singh, "
             "Müller & Vicknasingam 2014, Drug and Alcohol Dependence) and R3754 (thesis, USM; incomplete text)",
             "One sample: the 293 regular kratom users. Use R3639 (LDQ categories); R3754 (attached) only for values "
             "R3639 does not give."),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()
    recs = load_records(a.run)
    elig = set(eligible_reports())
    used = {m for m, *_ in STUDIES.values()} | {x for _, att, *_ in STUDIES.values() for x in att}
    assert used == elig, (sorted(elig - used), sorted(used - elig))
    rows, jobs = [], []
    for st, (main, att, why, samples) in STUDIES.items():
        for rid, role in [(main, f"main of job {main}"), *[(x, f"attached to job {main}") for x in att]]:
            u = recs[rid]
            rows.append({"study_id": st, "rec_id": rid, "role": role, "first_author": u.get("first_author", ""),
                         "year": u.get("year", ""), "doi": u.get("doi", ""), "title": u["title"], "link_reason": why,
                         "possible_overlap": ""})
        jobs.append({"job_id": main, "study_id": st, "main": main, "attached": att, "listed_only": [],
                     "link_reason": why, "samples": samples, "job_notes": "", "possible_overlap": []})
    with (HERE / "study_map.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    (HERE / "jobs.json").write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(elig)} reports -> {len(STUDIES)} studies, {len(jobs)} jobs")


if __name__ == "__main__":
    main()
