"""Backward and forward citation searching of the included reports (protocol §9), through OpenAlex.

For every report R1 included at full text (fulltext/decisions/ft_R1.csv, decision eligible): its reference list
(referenced_works) and the works citing it. Records already in the final search (search/runs/<run>/records_unique.jsonl,
by DOI or normalised title) are dropped; of the new ones, only records with a kratom term in title or abstract are kept
(the others cannot be about people who use kratom). The kept records get IDs C001… and go through the same screening:
two AI passes with the frozen prompt, then R1 (screening/llm_screen.py with --list).

Output: search/runs/<run>-citations/records.jsonl, screening.csv, log.json.
Run: .venv/Scripts/python.exe papers/kratom-use-disorder-prevalence/search/citations_included.py --run 2026-11-21
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import search as S
from dedup import norm_title

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
KRATOM = re.compile(r"kratom|krathom|kratum|\bketum|kakuam|biak-biak|mitragyn|กระท่อม|кратом|クラトム|卡痛|크라톰", re.I)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()
    run = HERE / "runs" / a.run
    recs = {json.loads(l)["rec_id"]: json.loads(l) for l in (run / "records_unique.jsonl").open(encoding="utf-8")}
    known_doi = {d for u in recs.values() for d in (u.get("all_dois") or "").lower().split(";") if d}
    known_title = {norm_title(u["title"]) for u in recs.values()}
    ft = [r for r in csv.DictReader((PAPER / "fulltext" / "decisions" / "ft_R1.csv").open(encoding="utf-8-sig"))
          if r["decision"] == "eligible"]
    key = {"api_key": S.ENV["OPENALEX_API_KEY"]}
    seeds, found, per_seed = [], {}, {}
    for r in ft:
        u = recs[r["rec_id"]]
        w = None
        if u.get("doi"):
            resp = S.client.get(f"https://api.openalex.org/works/doi:{u['doi']}", params={**key, "select": "id,referenced_works"})
            w = resp.json() if resp.status_code == 200 else None
        if w is None:
            oid = next((s for s in u["source_ids"].split(";") if re.match(r"^W\d+$", s)), None)
            if oid:
                resp = S.client.get(f"https://api.openalex.org/works/{oid}", params={**key, "select": "id,referenced_works"})
                w = resp.json() if resp.status_code == 200 else None
        if w is None:
            per_seed[r["rec_id"]] = "not in OpenAlex"
            continue
        wid = w["id"].split("/")[-1]
        seeds.append(wid)
        refs = [x.split("/")[-1] for x in w.get("referenced_works") or []]
        got = []
        for ch in S.chunks(refs, 50):
            got += [(x, "reference of " + r["rec_id"]) for x in S._openalex_page("openalex:" + "|".join(ch))]
        got += [(x, "cites " + r["rec_id"]) for x in S._openalex_page(f"cites:{wid}")]
        per_seed[r["rec_id"]] = {"openalex": wid, "references": len(refs), "citing": sum(1 for _, how in got if how.startswith("cites"))}
        for x, how in got:
            rec = S._openalex_rec(x, "citations_included", {"cites": how})
            k = rec["source_id"]
            if k in found:
                found[k]["cites"] += "; " + how
            else:
                found[k] = rec
    new = [r for r in found.values() if r["doi"] not in known_doi and norm_title(r["title"]) not in known_title]
    kept = [r for r in new if KRATOM.search(f"{r['title']} {r['abstract']}")]
    kept.sort(key=lambda r: (-(int(r["year"]) if str(r["year"]).isdigit() else 0), r["title"].lower()))
    out = HERE / "runs" / f"{a.run}-citations"
    out.mkdir(parents=True, exist_ok=True)
    with (out / "records.jsonl").open("w", encoding="utf-8") as f:
        for i, r in enumerate(kept, 1):
            r["rec_id"] = f"C{i:03d}"
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    cols = ["rec_id", "title", "abstract", "year", "first_author", "venue", "doi", "pmid", "link", "language", "types",
            "sources", "cites"]
    with (out / "screening.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in kept:
            w.writerow({**r, "link": f"https://doi.org/{r['doi']}" if r["doi"] else "", "types": f"openalex:{r['type']}",
                        "sources": "citations_included"})
    log = {"run_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "included_reports": len(ft),
           "seeds_in_openalex": len(seeds), "per_report": per_seed, "unique_records_found": len(found),
           "new_not_in_search": len(new), "new_with_kratom_term": len(kept)}
    (out / "log.json").write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in log.items() if k != "per_report"}, indent=2))


if __name__ == "__main__":
    main()
