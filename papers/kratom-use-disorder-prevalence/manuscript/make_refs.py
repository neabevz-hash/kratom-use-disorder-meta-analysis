"""Manuscript reference list from Crossref (every DOI checked; theses without DOI are added from the search records).
Writes manuscript/references.md and prints first author / year per DOI to check in-text citations.
Run: .venv/Scripts/python.exe -I papers/kratom-use-disorder-prevalence/manuscript/make_refs.py"""
import sys, time
from pathlib import Path
import httpx
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "registration"))
from make_refs import fmt  # noqa: E402
DOIS = """10.1080/15332640.2026.2706579 10.1159/000539338 10.1080/00952990.2025.2609965 10.1016/j.addbeh.2020.106479
10.1016/j.drugalcdep.2024.111263 10.1016/j.drugalcdep.2013.02.036 10.1080/08897077.2014.924464 10.1111/j.1360-0443.2007.02114.x
10.1046/j.1360-0443.1995.9056072.x 10.1111/j.1360-0443.1994.tb03332.x 10.31584/jhsmr.2023932 10.1176/appi.books.9780890425596
10.1136/bmj.n71 10.15171/ijhpm.2014.71 10.1097/XEB.0000000000000054 10.1002/sim.4040 10.1002/jrsm.1348
10.1136/bmjopen-2015-010247 10.1136/bmj.h870 10.1186/s12874-019-0782-0 10.1001/jamanetworkopen.2024.20496
10.1007/s40429-026-00811-6 10.35118/apjmbb.2026.034.3.14 10.1016/j.dadr.2025.100394 10.58837/chula.jmbs.7.1.7
10.1371/journal.pone.0287466 10.1016/j.drugalcdep.2024.111329 10.1097/adm.0000000000000986 10.1016/j.drugalcdep.2020.107849
10.1097/adm.0000000000001290 10.1016/j.drugalcdep.2014.03.017
10.1007/s40429-026-00755-x 10.1097/adm.0000000000001785 10.1097/adm.0000000000001637 10.1016/j.amepre.2021.02.004
10.1097/adm.0000000000001728 10.1186/s13643-020-01542-z 10.18637/jss.v036.i03 10.18637/jss.v067.i01""".split()
MANUAL = [   # included reports without a DOI: details checked on the title pages of the texts read (fulltext/text/)
    "- Kanchanasim, P. (2026). Prevalence of substance use and quality of life among support personnel in a tertiary care "
    "hospital in Bangkok. *Journal of Medical Bioscience*. [Data extracted from the thesis version of the same study, "
    "Chulalongkorn University, Faculty of Medicine, 2024; in Thai.]",
    "- Koktavá, K. (2024). *Míra a vzorce užívání kratomu v dospělé populaci a riziko ztráty kontroly v průběhu užívání "
    "kratomu: dotazníková průřezová studie* [Prevalence and patterns of kratom use in the Czech population and risk of loss "
    "of controlled use over time: Cross-sectional questionnaire survey] [Bachelor's thesis, Charles University, First "
    "Faculty of Medicine]. https://core.ac.uk/download/619650299.pdf",
    "- Kunová, V. (2022). *Vzorce užívání kratomu u pravidelných uživatelů: kvalitativní analýza* [Patterns of kratom use "
    "among regular users: Qualitative analysis] [Master's thesis, Charles University, First Faculty of Medicine]. "
    "https://core.ac.uk/download/534449169.pdf",
    "- Leong Bin Abdullah, M. F. I., Singh, D., Narayanan, S., Abdul Rahim, A., & Vicknasingam, B. (2019). "
    "Socio-demographic characteristics, kratom use and quality of life (QoL) of regular kratom (*Mitragyna speciosa* "
    "Korth.) users. *Malaysian Journal of Medicine and Health Sciences*, *15*(3), 4-9.",
    "- Saengmolee, W. (2022). *Characterization of physiological biomarkers in long-term kratom (Mitragyna speciosa Korth.) "
    "users: A preliminary study* [Doctoral dissertation, Prince of Songkla University]. "
    "https://core.ac.uk/download/597595552.pdf",
]
def main():
    sys.stdout.reconfigure(encoding="utf-8")
    c = httpx.Client(timeout=40)
    out = []
    for d in DOIS:
        r = c.get(f"https://api.crossref.org/works/{d}", params={"mailto": "mrexert@gmail.com"})
        if r.status_code != 200:
            print("FAILED", d, r.status_code); continue
        m = r.json()["message"]; au = m.get("author") or [{}]
        print(d, "|", au[0].get("family") or au[0].get("name"), (m.get("issued", {}).get("date-parts") or [[None]])[0][0])
        out.append(fmt(m)); time.sleep(0.3)
    out += MANUAL
    out.sort(key=lambda s: s.lower())
    (HERE / "references.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(len(out), "references")
if __name__ == "__main__":
    main()
