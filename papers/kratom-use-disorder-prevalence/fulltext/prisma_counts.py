"""PRISMA 2020 counts for the database and register search (protocol §11; citation searching is counted separately).

Inputs: search/runs/<run>/dedup_report.json, screening/decisions/tiab_summary.json, fulltext/retrieval_log.csv,
fulltext/linked_components.csv (figures, supplements and data deposits of a retrieved report: linked to it and
counted as duplicates, E6), fulltext/decisions/ft_R1.csv. Writes fulltext/prisma_counts.json.

Run: .venv/Scripts/python.exe papers/kratom-use-disorder-prevalence/fulltext/prisma_counts.py --run 2026-11-21
"""
import argparse
import csv
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
REASON_LABEL = {"E5_design": "design (review, qualitative without counts, case series, preclinical)",
                "E1_selected_sample": "sample recruited because of kratom problems",
                "E7_not_kratom_users": "not people who use kratom",
                "E4_no_dependence_measure": "no use-disorder or dependence measure for kratom",
                "E2_no_kratom_user_estimate": "no estimate for people who use kratom",
                "E3_distribution_cutoff": "cut-off from the sample's own distribution",
                "no_extractable_counts": "no extractable counts", "E6_duplicate": "duplicate or component of another report",
                "other": "other"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()
    dd = json.loads((PAPER / "search" / "runs" / a.run / "dedup_report.json").read_text(encoding="utf-8"))
    ts = json.loads((PAPER / "screening" / "decisions" / "tiab_summary.json").read_text(encoding="utf-8"))
    log = list(csv.DictReader((HERE / "retrieval_log.csv").open(encoding="utf-8-sig")))
    linked = {r["rec_id"]: r for r in csv.DictReader((HERE / "linked_components.csv").open(encoding="utf-8"))}
    ft = {r["rec_id"]: r for r in csv.DictReader((HERE / "decisions" / "ft_R1.csv").open(encoding="utf-8-sig"))}
    retrieved = [r for r in log if r["status"] == "retrieved"]
    not_ret = [r for r in log if r["status"] != "retrieved" and r["rec_id"] not in linked]
    excl = Counter(r["reason"] for r in ft.values() if r["decision"] != "eligible")
    excl["E6_duplicate"] += len(linked)
    out = {
        "identification": {"records_per_source": dd["records_per_source"], "records_total": dd["records_total"],
                           "duplicates_removed": dd["duplicates_removed"],
                           "removed_before_screening": {"non_study_records": dd["auto_removed_non_study_records"],
                                                        "vendor_advertising": dd["auto_removed_vendor_advertising"],
                                                        "outside_concept_b": dd["removed_outside_concept_b"]}},
        "screening": {"records_screened": ts["records_screened"], "records_excluded": ts["excluded_title_abstract"],
                      "reports_sought": len(log),
                      "reports_not_retrieved": len(not_ret),
                      "reports_assessed": len(retrieved) + len(linked),
                      "reports_excluded": {REASON_LABEL.get(k, k): v for k, v in excl.most_common()},
                      "reports_included": sum(1 for r in ft.values() if r["decision"] == "eligible")},
        "check": {"retrieved_with_r1_decision": sum(1 for r in retrieved if r["rec_id"] in ft),
                  "retrieved": len(retrieved), "linked_components": len(linked)},
    }
    (HERE / "prisma_counts.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
