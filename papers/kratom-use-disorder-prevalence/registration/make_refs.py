"""Reference list of the protocol from Crossref (every reference is checked by DOI; nothing typed from memory).

Writes registration/references.md (APA-like) and prints first author and year for each DOI, so the in-text citations
can be checked against Crossref. Run: .venv/Scripts/python.exe papers/kratom-use-disorder-prevalence/registration/make_refs.py
"""
import html
import re
import time
from pathlib import Path

import httpx

HERE = Path(__file__).resolve().parent
DOIS = """
10.1186/2046-4053-4-1
10.1136/bmj.g7647
10.1186/s13643-023-02281-7
10.1080/15332640.2026.2706579
10.1159/000539338
10.1080/00952990.2025.2609965
10.1097/adm.0000000000000986
10.1097/adm.0000000000001290
10.2174/2405461503666180420120649
10.1016/j.drugalcdep.2014.03.017
10.1016/j.drugalcdep.2024.111329
10.1016/j.drugalcdep.2017.10.012
10.1080/02791072.2018.1562133
10.1080/02791072.2025.2465797
10.1080/10826084.2026.2697988
10.1097/XEB.0000000000000054
10.15171/ijhpm.2014.71
10.1186/s13643-020-01542-z
10.1348/000711006X126600
10.1186/s12874-019-0782-0
10.1001/jamanetworkopen.2024.20496
10.7326/M19-0891
10.1016/j.drugalcdep.2013.02.036
10.1111/j.1360-0443.2007.02114.x
10.1080/08897077.2014.924464
10.1046/j.1360-0443.1995.9056072.x
10.1176/appi.books.9780890425596
10.1002/sim.4040
10.1002/jrsm.1348
10.1097/EDE.0000000000001232
10.1136/bmjopen-2015-010247
10.1002/jrsm.1547
10.3758/s13428-012-0261-6
10.1007/s11121-021-01246-3
10.1016/j.jclinepi.2014.03.003
10.1136/bmj.h870
""".split()


def name(a):
    if a.get("family"):
        ini = " ".join(p[0] + "." for p in re.split(r"[\s-]+", a.get("given") or "") if p)
        return f"{a['family']}, {ini}".strip().rstrip(",")
    return a.get("name", "")


def fmt(m):
    au = m.get("author") or []
    names = [name(a) for a in au]
    if len(names) > 20:
        names = names[:19] + ["…", names[-1]]
    if len(names) > 1:
        auth = ", ".join(names[:-1]) + ", & " + names[-1]
    else:
        auth = names[0] if names else (m.get("publisher") or "")
    yr = (m.get("issued", {}).get("date-parts") or [[None]])[0][0]
    title = html.unescape(re.sub(r"<[^>]+>", "", " ".join(m.get("title") or []))).strip()
    title = re.sub(r"\s+", " ", title)
    cont = html.unescape(" ".join(m.get("container-title") or []))
    vol, iss, pg = m.get("volume"), m.get("issue"), m.get("page") or m.get("article-number")
    src = f"*{cont}*" if cont else ""
    if vol:
        src += f", *{vol}*" + (f"({iss})" if iss else "")
    if pg:
        src += f", {pg}"
    return f"- {auth} ({yr}). {title}. {src}. https://doi.org/{m['DOI']}".replace(". .", ".").replace(".. ", ". ")


def main():
    c = httpx.Client(timeout=40)
    out = []
    for d in DOIS:
        for i in range(4):
            r = c.get(f"https://api.crossref.org/works/{d}", params={"mailto": "mrexert@gmail.com"})
            if r.status_code == 200:
                break
            time.sleep(2 * (i + 1))
        if r.status_code != 200:
            print("FAILED", d, r.status_code)
            continue
        m = r.json()["message"]
        au = m.get("author") or [{}]
        print(d, "|", au[0].get("family") or au[0].get("name"), len(m.get("author") or []),
              (m.get("issued", {}).get("date-parts") or [[None]])[0][0])
        out.append(fmt(m))
        time.sleep(0.3)
    out.sort(key=lambda s: s.lower())
    (HERE / "references.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(len(out), "references")


if __name__ == "__main__":
    main()
