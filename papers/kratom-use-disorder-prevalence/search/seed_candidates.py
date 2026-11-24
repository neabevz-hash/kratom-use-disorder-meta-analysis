"""Seed-set candidates: kratom studies cited by reviews and key KUD papers (OpenAlex referenced_works).
Prints candidates with a dependence/disorder term; the seed set itself (seed_set.csv) is chosen by hand from them."""
import json, re, sys, httpx
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
ENV = {k.strip(): v.strip() for k, v in (l.split("=", 1) for l in (ROOT / ".env").read_text(encoding="utf-8").splitlines() if "=" in l and not l.startswith("#"))}
K = ENV["OPENALEX_API_KEY"]
C = httpx.Client(timeout=60)
SOURCES = ["10.1097/adm.0000000000001290", "10.1159/000539338", "10.1080/15332640.2026.2706579",
           "10.1080/00952990.2025.2609965", "10.1016/j.drugalcdep.2024.111329", "10.1097/adm.0000000000000986",
           "10.1080/02791072.2025.2465797", "10.1080/10826084.2026.2697988"]
def inv(ix):
    if not ix: return ""
    pos = {i: w for w, idxs in ix.items() for i in idxs}; return " ".join(pos[i] for i in sorted(pos))
refs = {}
for d in SOURCES:
    w = C.get(f"https://api.openalex.org/works/doi:{d}", params={"api_key": K, "select": "id,referenced_works"}).json()
    for r in w.get("referenced_works") or []:
        refs.setdefault(r.split("/")[-1], []).append(d)
ids = list(refs)
out = []
for i in range(0, len(ids), 50):
    ch = ids[i:i+50]
    d = C.get("https://api.openalex.org/works", params={"filter": "openalex:" + "|".join(ch), "per_page": 50, "api_key": K,
              "select": "id,doi,title,publication_year,abstract_inverted_index,type"}).json()
    out += d["results"]
D = re.compile(r"depend|use disorder|\bDSM|addict|withdraw|problematic", re.I)
rows = []
for w in out:
    t = w.get("title") or ""; ab = inv(w.get("abstract_inverted_index"))
    if re.search(r"kratom|mitragyn|ketum|krathom", t + ab, re.I) and D.search(t + " " + ab) and w.get("type") != "review":
        m = re.findall(r"[^.]*(?:depend|disorder|DSM)[^.]*\d+(?:\.\d+)?\s?%[^.]*\.", ab)
        rows.append((w.get("publication_year"), (w.get("doi") or "").replace("https://doi.org/", ""), t, len(refs[w["id"].split("/")[-1]]), m[:2]))
rows.sort()
for r in rows:
    print(r[0], "|", r[1], "| cited by", r[3], "|", r[2][:120]); [print("     >>", s.strip()[:260]) for s in r[4]]
print(len(out), "refs;", len(rows), "candidates")
