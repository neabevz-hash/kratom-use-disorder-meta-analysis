"""Third pass for open-access full texts (protocol §11b): PMC author manuscripts and PMC articles through NCBI E-utilities.

pmc.ncbi.nlm.nih.gov answers bots with a challenge page and Europe PMC's REST full text returns errors for NIH author
manuscripts, but the official NCBI API (efetch, db=pmc) serves their JATS XML. For every report in retrieval_log.csv
with status "not retrieved": PMCID from the NCBI ID converter (by DOI or PMID) → efetch db=pmc → jats_to_text (same
converter as fetch_oa.py) → fulltext/text/<rec_id>.txt with SOURCE pmc_efetch; retrieval_log.csv is updated in place.
A text counts only if it has a body (more than an abstract).

Run: .venv/Scripts/python.exe -I papers/kratom-use-disorder-prevalence/fulltext/fetch_pmc.py --run 2026-11-21
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fetch_oa as fo  # noqa: E402

E = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"


def pmcid_for(doi: str, pmid: str) -> str:
    for ident in (doi, pmid):
        if not ident:
            continue
        r = fo.get("https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/", params={"ids": ident, "format": "json",
                                                                                     "tool": "kratom-review", "email": fo.EMAIL})
        if r is not None:
            for rec in r.json().get("records", []):
                if rec.get("pmcid"):
                    return rec["pmcid"]
        time.sleep(0.4)
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()
    recs = {json.loads(l)["rec_id"]: json.loads(l) for l in
            (fo.PAPER / "search" / "runs" / a.run / "records_unique.jsonl").open(encoding="utf-8")}
    rows = list(csv.DictReader(fo.LOG.open(encoding="utf-8-sig")))
    fields = list(rows[0].keys())
    got = 0
    for row in rows:
        if row["status"] == "retrieved":
            continue
        rid = row["rec_id"]
        pmcid = pmcid_for(row["doi"], recs[rid].get("pmid") or "")
        if not pmcid:
            continue
        r = fo.get(E + "efetch.fcgi", params={"db": "pmc", "id": pmcid.replace("PMC", ""), "retmode": "xml",
                                              "tool": "kratom-review", "email": fo.EMAIL})
        time.sleep(0.4)
        if r is None or b"<body" not in r.content:
            row["tried"] = (row["tried"] + f";pmc_efetch:{pmcid}:no body").strip(";")
            print(f"{rid} {pmcid}: no body", flush=True)
            continue
        text = fo.jats_to_text(r.content)
        url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/"
        row.update({"status": "retrieved", "source": "pmc_efetch", "url": url, "chars": str(len(text)), "pages": "",
                    "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(), "at_utc": fo.utcnow(),
                    "tried": (row["tried"] + f";pmc_efetch:{pmcid}").strip(";")})
        header = f"REC_ID: {rid}\nSOURCE: pmc_efetch\nURL: {url}\nRETRIEVED_UTC: {row['at_utc']}\n\n"
        (fo.TEXT / f"{rid}.txt").write_text(header + text, encoding="utf-8")
        got += 1
        print(f"{rid} {pmcid}: retrieved ({len(text):,} chars)", flush=True)
    with fo.LOG.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    total = sum(1 for r in rows if r["status"] == "retrieved")
    print(f"pmc_efetch: {got} new; retrieved {total} of {len(rows)}")


if __name__ == "__main__":
    main()
