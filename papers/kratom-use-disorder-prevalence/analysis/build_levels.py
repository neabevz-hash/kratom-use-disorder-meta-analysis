"""Cumulative case-definition levels from the verified estimates (protocol §13; levels table with C1).

Extraction keeps every category as printed. Here, for every sample, instrument and time frame (whole sample only):
- L1 (any use disorder): a direct ">=2" estimate; else n minus the "below" category (none, 0-1 criteria); else the sum
  of the L1, L2 and L3 bands;
- L2 (moderate-to-severe disorder or dependence): a direct cumulative L2 estimate (">=4", "SDS>=6", "ASSIST>=27");
  else the sum of the bands at L2 or above (moderate + severe; KDS moderate + high; LDQ medium + high, C1);
- L3 (severe disorder): a direct ">=6" estimate.
Codes: L2 from DSM-5-SUD, SUDST or interview = "L2"; from KDS, SDS, LDQ = "L2-scale"; from ASSIST = "L2-screen".

One estimate per sample and level for the pooled analyses (protocol §13): instrument priority interview > DSM-5-SUD,
SUDST > DSM-IV, ICD > KDS, SDS, LDQ > ASSIST; time frame past 12 months > current > lifetime > NR.
Writes analysis/data/level_estimates.csv (all rows) and analysis/data/primary.csv (one row per sample and level).
Run: .venv/Scripts/python.exe -I papers/kratom-use-disorder-prevalence/analysis/build_levels.py
"""
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
PRIORITY = {"interview": 0, "DSM-5-SUD": 1, "SUDST": 1, "DSM-IV": 2, "ICD-10": 2, "ICD-11": 2, "KDS": 3, "SDS": 3,
            "LDQ": 3, "ASSIST": 4}
TF = {"past 12 months": 0, "current": 1, "lifetime": 2, "NR": 3, "past week": 3}
SCALE = {"KDS", "SDS", "LDQ"}


def num(v):
    try:
        return float(str(v).replace(",", ""))
    except ValueError:
        return None


def code_l2(ins: str) -> str:
    return "L2-scale" if ins in SCALE else ("L2-screen" if ins == "ASSIST" else "L2")


def main():
    samples = {s["sample_id"]: s for s in csv.DictReader((PAPER / "forms" / "samples.csv").open(encoding="utf-8"))}
    ests = [e for e in csv.DictReader((PAPER / "forms" / "estimates.csv").open(encoding="utf-8"))
            if e["subgroup"].strip().lower() == "all" and num(e["cases"]) is not None and num(e["n"]) is not None]
    groups = defaultdict(list)
    for e in ests:
        groups[(e["sample_id"], e["instrument"], e["time_frame"], e["n"])].append(e)
    rows = []
    for (sid, ins, tf, n), es in groups.items():
        n = num(n)
        lv = lambda e: e["level"]  # noqa: E731
        direct = {}
        for e in es:
            if e["cumulative"] == "yes" and lv(e) in ("L1", "L2", "L2-scale", "L2-screen", "L3"):
                key = "L2" if lv(e).startswith("L2") else lv(e)
                direct.setdefault(key, e)
        bands = [e for e in es if e["cumulative"] == "no"]
        below = [e for e in es if lv(e) == "below"]
        # LDQ high band coded not_levelled while the medium band is given: part of L2-scale (C1)
        l2bands = [e for e in bands if lv(e).startswith("L2") or lv(e) == "L3"]
        if ins == "LDQ" and any(b["level"] == "L2-scale" for b in es):   # C1: the high band joins the medium band
            l2bands = [e for e in es if e["level"] in ("L2-scale", "not_levelled")]
        if ins == "ASSIST":
            l2bands = []
        out = {}
        if "L1" in direct:
            out["L1"] = (num(direct["L1"]["cases"]), "direct", [direct["L1"]])
        elif below and ins in ("DSM-5-SUD", "SUDST", "interview"):
            out["L1"] = (n - sum(num(b["cases"]) for b in below), "n minus below", below)
        elif ins in ("DSM-5-SUD", "SUDST", "interview") and any(lv(e) == "L1" for e in bands):
            bb = [e for e in bands if lv(e) in ("L1", "L2", "L3")]
            out["L1"] = (sum(num(b["cases"]) for b in bb), "sum of bands", bb)
        if "L2" in direct:
            out["L2"] = (num(direct["L2"]["cases"]), "direct", [direct["L2"]])
        elif l2bands:
            top = [e for e in es if e["cumulative"] == "yes" and lv(e) == "L3"]
            parts = l2bands + [t for t in top if t not in l2bands]
            out["L2"] = (sum(num(b["cases"]) for b in parts), "sum of bands", parts)
        if "L3" in direct:
            out["L3"] = (num(direct["L3"]["cases"]), "direct", [direct["L3"]])
        for level, (cases, how, src) in out.items():
            rows.append({"sample_id": sid, "level": level, "code": code_l2(ins) if level == "L2" else level,
                         "instrument": ins, "time_frame": tf, "cases": f"{cases:g}", "n": f"{n:g}",
                         "pct": f"{100 * cases / n:.1f}", "how": how, "estimate_ids": "+".join(x["estimate_id"] for x in src)})
    rows.sort(key=lambda r: (r["sample_id"], r["level"], PRIORITY.get(r["instrument"], 9), TF.get(r["time_frame"], 9)))
    best = {}
    for r in rows:
        best.setdefault((r["sample_id"], r["level"]), r)
    s_cols = ["first_author", "year", "country", "region", "sample_type", "sampling", "recruitment_channel", "use_period",
              "regular_use_required", "product_form", "n_users", "pub_status", "pct_other_opioid_use",
              "jbi_2", "jbi_6", "jbi_9"]
    (HERE / "data").mkdir(exist_ok=True)
    for name, data in (("level_estimates.csv", rows), ("primary.csv", list(best.values()))):
        with (HERE / "data" / name).open("w", encoding="utf-8", newline="") as f:
            cols = list(data[0]) + s_cols
            w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
            w.writeheader()
            for r in data:
                w.writerow({**r, **{c: samples[r["sample_id"]][c] for c in s_cols}})
    for r in best.values():
        s = samples[r["sample_id"]]
        print(f"{r['sample_id']} {s['first_author'][:12]:12} {s['region'][:13]:13} {r['level']} {r['code']:9} "
              f"{r['instrument']:9} {r['time_frame'][:9]:9} {r['cases']:>4}/{r['n']:<5} {r['pct']:>5}% {r['how']}")


if __name__ == "__main__":
    main()
