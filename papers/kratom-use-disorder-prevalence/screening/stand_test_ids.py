"""Records for the stand test of the screener prompt (protocol §10): one per decision type, chosen by DOI or title
before any screening. Prints the rec_ids for llm_screen.py --ids and the expected label of each record.

Run: .venv/Scripts/python.exe papers/kratom-use-disorder-prevalence/screening/stand_test_ids.py --run 2026-11-21-check
"""
import argparse
import csv
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
# (DOI or title regex, expected label, why)
PICKS = [
    ("10.1097/adm.0000000000001290", "include", "seed: DSM-5 KUD among US consumers"),
    ("10.2174/2405461503666180420120649", "include", "seed: MINI and KDS among Malaysian regular users"),
    ("10.3390/healthcare10040746", "include", "seed: methadone patients who use ketum, KDS"),
    ("10.1097/adm.0000000000001637", "unsure|exclude", "NSDUH prevalence of kratom use (no KUD module)"),
    ("10.1016/j.drugalcdep.2017.10.012", "exclude", "systematic review"),
    ("10.3389/fphar.2024.1412397", "exclude", "Reddit analysis (qualitative)"),
    ("10.1080/15563650.2019.1569236", "exclude", "poison-centre exposures"),
    ("10.1097/adm.0000000000001259", "unsure|include", "laboratory study of people who use kratom regularly"),
    ("10.1080/15504263.2023.2289456", "unsure|include", "psychiatric inpatients who use kratom"),
    (r"(?i)case report", "exclude", "case report (first by title)"),
    (r"(?i)\bmice\b.*withdraw|withdraw.*\bmice\b|\brats?\b.*withdraw", "exclude", "animal withdrawal study"),
    ("NOABSTRACT", "unsure|exclude", "record without abstract"),
    ("THAI", "any", "Thai-language record"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()
    rows = list(csv.DictReader((HERE.parent / "search" / "runs" / a.run / "screening.csv").open(encoding="utf-8-sig")))
    chosen = []
    for key, exp, why in PICKS:
        if key == "NOABSTRACT":
            hit = next((r for r in rows if len(r["abstract"]) < 50 and re.search(r"(?i)\buse|users?", r["title"])), None)
        elif key == "THAI":
            hit = next((r for r in rows if re.search(r"[฀-๿]", r["title"] + r["abstract"])), None)
        elif key.startswith("10."):
            hit = next((r for r in rows if r["doi"].lower() == key), None)
        else:
            hit = next((r for r in rows if re.search(key, r["title"])), None)
        print(f"{hit['rec_id'] if hit else 'MISSING':7} expected {exp:15} {why} | {hit['title'][:80] if hit else ''}")
        if hit:
            chosen.append(hit["rec_id"])
    print(",".join(chosen))


if __name__ == "__main__":
    main()
