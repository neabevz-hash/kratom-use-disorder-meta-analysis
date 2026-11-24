"""GRADE for event rates (protocol §17; Iorio et al. 2015), rules fixed in deviations.md C2 before rating.

Start: high (prevalence from observational studies of the target population). Downgrade by one level for each:
- risk of bias: more than half of the samples rated "no" on JBI item 2, 6 or 9;
- inconsistency: 95% prediction interval wider than 20 percentage points (two levels if wider than 50);
- imprecision: 95% CI half-width above 5 percentage points;
- indirectness: more than half of the participants come from samples recruited through kratom advocacy or vendor
  channels or selected for regular use (not all people who use kratom);
- publication bias: small-study association (logit prevalence on 1/sqrt(n)) with p < 0.10.
Writes analysis/results/grade.csv.
Run: .venv/Scripts/python.exe -I papers/kratom-use-disorder-prevalence/analysis/grade.py
"""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEVELS = ["very low", "low", "moderate", "high"]
ROWS = {"L2 moderate-to-severe or dependence (primary)": "L2", "L1 any use disorder": "L1",
        "L3 severe use disorder": "L3", "L2, North America": "L2", "L1, North America": "L1",
        "L3, North America": "L3"}


def main():
    pooled = {r["analysis"]: r for r in csv.DictReader((HERE / "results" / "pooled.csv").open(encoding="utf-8"))}
    prim = list(csv.DictReader((HERE / "data" / "primary.csv").open(encoding="utf-8")))
    mb = {r["test"]: r for r in csv.DictReader((HERE / "results" / "meta_bias.csv").open(encoding="utf-8"))}
    smallstudy_p = float(next(v["p"] for k, v in mb.items() if k.startswith("logit")))
    out = []
    for name, level in ROWS.items():
        p = pooled[name]
        d = [r for r in prim if r["level"] == level and (", North America" not in name or r["region"] == "North America")]
        rob = sum(1 for r in d if "no" in (r["jbi_2"], r["jbi_6"], r["jbi_9"])) > len(d) / 2
        piw = float(p["pi_hi"]) - float(p["pi_lo"])
        inc = 2 if piw > 50 else (1 if piw > 20 else 0)
        imp = (float(p["hi"]) - float(p["lo"])) / 2 > 5
        n_sel = sum(float(r["n"]) for r in d if r["recruitment_channel"] == "advocacy or vendor channels"
                    or r["regular_use_required"].lower() not in ("no", "nr", "na", ""))
        ind = n_sel > sum(float(r["n"]) for r in d) / 2
        pub = smallstudy_p < 0.10
        down = int(rob) + inc + int(imp) + int(ind) + int(pub)
        out.append({"outcome": name, "k": p["k"], "prevalence": f"{p['prev']} ({p['lo']}-{p['hi']})",
                    "risk_of_bias": "serious" if rob else "not serious",
                    "inconsistency": ["not serious", "serious", "very serious"][inc] + f" (PI width {piw:.0f} pp)",
                    "imprecision": "serious" if imp else "not serious", "indirectness": "serious" if ind else "not serious",
                    "publication_bias": "suspected" if pub else "not detected",
                    "certainty": LEVELS[max(0, 3 - down)]})
    with (HERE / "results" / "grade.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    for r in out:
        print(r["outcome"], "|", r["prevalence"], "|", r["certainty"], "|", r["risk_of_bias"], r["inconsistency"],
              r["imprecision"], r["indirectness"], r["publication_bias"])


if __name__ == "__main__":
    main()
