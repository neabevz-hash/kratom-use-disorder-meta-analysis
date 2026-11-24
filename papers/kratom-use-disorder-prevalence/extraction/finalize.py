"""Final extraction tables (protocol §11c): R1-verified drafts -> forms/samples.csv and forms/estimates.csv.

Input: extraction/decisions/samples_R1.csv and estimates_R1.csv (verify_md.py parse), extraction/study_map.csv and the
search records (first author, year, DOI of the main report). Samples R1 dropped are left out. IDs: S01…, E001….
Run: .venv/Scripts/python.exe -I papers/kratom-use-disorder-prevalence/extraction/finalize.py --run 2026-11-21
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
sys.path.insert(0, str(HERE))
from common import load_records  # noqa: E402

SAMPLE_COLS = ["sample_id", "study_id", "report_ids", "first_author", "year", "doi", "label", "pub_status", "language",
               "country", "region", "data_years", "design", "sample_type", "sampling", "recruitment_channel", "use_period",
               "regular_use_required", "product_form", "n_users", "response_rate", "age_mean", "age_sd", "pct_male",
               "pct_other_opioid_use", "instruments", "industry_funding", "funding_coi",
               "jbi_1", "jbi_2", "jbi_3", "jbi_4", "jbi_5", "jbi_6", "jbi_7", "jbi_8", "jbi_9", "sample_key"]
EST_COLS = ["estimate_id", "sample_id", "subgroup", "instrument", "threshold", "cumulative", "threshold_source",
            "author_label", "level", "table_rule", "time_frame", "cases", "n", "derived", "derivation",
            "primary_for_authors", "location", "note"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()
    recs = load_records(a.run)
    dec = HERE / "decisions"
    samples = [r for r in csv.DictReader((dec / "samples_R1.csv").open(encoding="utf-8")) if not r["dropped"]]
    ests = list(csv.DictReader((dec / "estimates_R1.csv").open(encoding="utf-8")))
    smap = {}
    for r in csv.DictReader((HERE / "study_map.csv").open(encoding="utf-8")):
        smap.setdefault(r["study_id"], []).append(r)
    out_s, out_e, ids = [], [], {}
    for k, s in enumerate(sorted(samples, key=lambda r: r["sample_key"]), 1):
        sid = f"S{k:02d}"
        ids[s["sample_key"]] = sid
        main = next(r for r in smap[s["study_id"]] if r["role"].startswith("main"))
        u = recs[main["rec_id"]]
        out_s.append({**{c: s.get(c, "") for c in SAMPLE_COLS}, "sample_id": sid,
                      "report_ids": ";".join(r["rec_id"] for r in smap[s["study_id"]]),
                      "first_author": u.get("first_author", ""), "year": u.get("year", ""), "doi": u.get("doi", "")})
    n = 0
    for e in ests:
        if e["sample_key"] not in ids:
            continue
        n += 1
        out_e.append({**{c: e.get(c, "") for c in EST_COLS}, "estimate_id": f"E{n:03d}", "sample_id": ids[e["sample_key"]]})
    for name, cols, rows in (("samples.csv", SAMPLE_COLS, out_s), ("estimates.csv", EST_COLS, out_e)):
        with (PAPER / "forms" / name).open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
    print(f"forms/samples.csv: {len(out_s)} samples; forms/estimates.csv: {len(out_e)} estimates")


if __name__ == "__main__":
    main()
