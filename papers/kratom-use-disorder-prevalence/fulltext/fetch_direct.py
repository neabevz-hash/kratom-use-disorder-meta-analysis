"""Fourth pass (protocol §11b): open-access copies at known direct links that the generic passes missed.

Each link below is a legal open-access copy listed by OpenAlex (repository PDF, Zenodo record, publisher's open PDF,
OJS galley) or the open article that a data deposit belongs to. Same PDF-to-text conversion as fetch_oa.py; pages that
answer with a bot check are recorded as blocked. retrieval_log.csv is updated in place.

Run: .venv/Scripts/python.exe -I papers/kratom-use-disorder-prevalence/fulltext/fetch_direct.py
"""
from __future__ import annotations

import csv
import hashlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fetch_oa as fo  # noqa: E402

LINKS = {
    "R0815": ["https://digitalcommons.library.tmc.edu/context/baylor_docs/article/9467/viewcontent/At_least_four_groups_of_kratom_consumers_in_the_United_States__latent_class_analysis_of_motivations_for_kratom_use_compressed.pdf"],
    "R0126": ["https://harmreductionjournal.biomedcentral.com/counter/pdf/10.1186/s12954-026-01534-7.pdf"],
    "R2897": ["https://digital.car.chula.ac.th/cgi/viewcontent.cgi?article=4732&context=clmjournal"],
    "R0842": ["https://papers.iafor.org/wp-content/uploads/papers/pce2025/PCE2025_95162.pdf"],
    "R1604": ["https://academic.oup.com/jsm/article-pdf/20/Supplement_1/qdad060.178/50414092/qdad060.178.pdf"],
    "R0105": ["https://gut.bmj.com/content/gutjnl/75/Suppl_2/A330.2.full.pdf"],
    "R0235": ["https://www.jpsmjournal.com/article/S0885-3924(26)00575-0/pdf"],
}


def zenodo_pdf(record: str) -> list[str]:
    r = fo.get(f"https://zenodo.org/api/records/{record}")
    if r is None:
        return []
    return [f["links"]["self"] for f in r.json().get("files", []) if f.get("key", "").lower().endswith(".pdf")]


def main():
    LINKS["R1683"] = zenodo_pdf("7312543")
    rows = list(csv.DictReader(fo.LOG.open(encoding="utf-8-sig")))
    fields = list(rows[0].keys())
    for row in rows:
        rid = row["rec_id"]
        if row["status"] == "retrieved" or rid not in LINKS:
            continue
        for url in LINKS[rid]:
            data, status = fo.fetch_pdf(url)
            row["tried"] = (row["tried"] + f";direct:{status}").strip(";")
            if not data:
                print(f"{rid}: {status} {url[:80]}", flush=True)
                continue
            text, pages = fo.pdf_to_text(data)
            if len(text) < 1500:
                print(f"{rid}: too short ({len(text)} chars)", flush=True)
                continue
            (fo.PDF / f"{rid}.pdf").write_bytes(data)
            row.update({"status": "retrieved", "source": "pdf_direct", "url": url, "chars": str(len(text)),
                        "pages": str(pages), "sha256": hashlib.sha256(data).hexdigest(), "at_utc": fo.utcnow()})
            header = f"REC_ID: {rid}\nSOURCE: pdf_direct\nURL: {url}\nRETRIEVED_UTC: {row['at_utc']}\n\n"
            (fo.TEXT / f"{rid}.txt").write_text(header + text, encoding="utf-8")
            print(f"{rid}: retrieved ({pages} pages, {len(text):,} chars)", flush=True)
            break
    with fo.LOG.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"retrieved {sum(1 for r in rows if r['status'] == 'retrieved')} of {len(rows)}")


if __name__ == "__main__":
    main()
