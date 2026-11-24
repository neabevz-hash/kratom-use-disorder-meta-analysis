"""Check the public OSF registration against registration/osf.md (text fields) and registration/osf_package/ (files).

Run: .venv/Scripts/python.exe papers/kratom-use-disorder-prevalence/registration/verify_osf.py 6d7n3
Writes registration/osf_check.json.
"""
import hashlib
import html
import json
import re
import sys
from pathlib import Path

import httpx

HERE = Path(__file__).resolve().parent
GUID = sys.argv[1] if len(sys.argv) > 1 else "6d7n3"
C = httpx.Client(timeout=120, follow_redirects=True)


def norm(t: str) -> str:
    t = html.unescape(html.unescape(str(t)))
    t = re.sub(r"[*`]", "", t)
    return re.sub(r"\s+", " ", t).strip().lower()


def md_fields() -> dict[str, str]:
    md = (HERE / "osf.md").read_text(encoding="utf-8")
    body = md.split("## Review Methods", 1)[1]
    out, cur, buf = {}, None, []
    for line in body.splitlines():
        m = re.match(r"^\*\*(.+?)\*\*\s*$", line)
        if m:
            if cur:
                out[cur] = "\n".join(buf).strip()
            cur, buf = m.group(1), []
        elif line.startswith("## ") or line.startswith("---"):
            continue
        elif cur:
            buf.append(line)
    if cur:
        out[cur] = "\n".join(buf).strip()
    return out


def main():
    reg = C.get(f"https://api.osf.io/v2/registrations/{GUID}/").json()["data"]
    a = reg["attributes"]
    resp = a.get("registration_responses") or {}
    texts = {k: v for k, v in resp.items() if isinstance(v, str)}
    files = {k: v for k, v in resp.items() if isinstance(v, list)}
    fields = md_fields()
    rtexts = {norm(v): k for k, v in texts.items()}
    res = {"guid": GUID, "date_registered": a.get("date_registered"), "public": a.get("public"),
           "fields_in_osf_md": len(fields), "text_responses": len(texts), "matched": [], "not_matched": []}
    for name, val in fields.items():
        if norm(val) in rtexts:
            res["matched"].append(name)
        else:
            # closest response by shared words, to show the difference
            nv = set(norm(val).split())
            best = max(texts.items(), key=lambda kv: len(nv & set(norm(kv[1]).split())), default=(None, ""))
            res["not_matched"].append({"field": name, "closest_key": best[0],
                                       "osf_text_start": str(best[1])[:200], "md_text_start": val[:200]})
    # files
    pkg = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (HERE / "osf_package").iterdir() if p.is_file()}
    res["files"] = []
    for key, lst in files.items():
        for f in lst:
            name = f.get("file_name") or f.get("name")
            fid = f.get("file_id") or f.get("id")
            url = (f.get("file_urls") or {}).get("download") or (f"https://osf.io/download/{fid}/" if fid else None)
            sha = None
            if url:
                r = C.get(url)
                if r.status_code == 200:
                    sha = hashlib.sha256(r.content).hexdigest()
            res["files"].append({"field": key, "name": name, "sha256": sha, "package_sha256": pkg.get(name),
                                 "same": sha is not None and sha == pkg.get(name)})
    (HERE / "osf_check.json").write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"registered {res['date_registered']} public={res['public']}; text fields matched "
          f"{len(res['matched'])} of {len(fields)} (OSF has {len(texts)} text responses)")
    for nm in res["not_matched"]:
        print("  NOT MATCHED:", nm["field"], "| closest:", nm["closest_key"])
    for f in res["files"]:
        print("  file", f["field"], f["name"], "same as package" if f["same"] else f"DIFFERENT/unknown ({f['sha256']})")


if __name__ == "__main__":
    main()
