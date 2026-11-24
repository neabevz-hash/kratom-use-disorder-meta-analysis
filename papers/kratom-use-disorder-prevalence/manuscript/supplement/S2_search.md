**Supplementary File S2.** Search strategies, dates and results per source (PRISMA-S)

Final search started 2026-11-21 15:04:44 (UTC) with the frozen code of protocol v1.0 (git tag `kratom-prereg-v1.0`). Concept A (kratom) was searched in every source without date or language limits; concept B (people who use kratom, or dependence) was applied afterwards to titles and abstracts by `search/dedup.py`, identically for all sources (terms in protocol §8).

**Kratom terms.** kratom; kratoms; krathom; kratum; ketum; kakuam; biak-biak; Mitragyna speciosa; mitragynine; 7-hydroxymitragynine; mitragynine pseudoindoxyl.

**Non-English terms (OpenAlex).** กระท่อม; ใบกระท่อม; кратом; митрагинин; クラトム; ミトラガイニン; 卡痛; 帽柱木; 크라톰; daun ketum; air ketum; daun kratom.

| Source | Interface and query form | Searched (UTC) | Records |
| --- | --- | --- | --- |
| PubMed | NCBI E-utilities; kratom terms in title or abstract ([tiab]) and the MeSH term Mitragyna | 2026-11-21T15:05:12+00:00 | 1,203 |
| Europe PMC | REST API; TITLE_ABS phrases | 2026-11-21T15:05:23+00:00 | 1,213 |
| OpenAlex | API; title_and_abstract.search, phrases joined by OR | 2026-11-21T15:05:43+00:00 | 2,903 |
| OpenAlex, other languages | API; one phrase per query (Thai, Malay, Russian, Japanese, Chinese, Korean) | 2026-11-21T15:05:52+00:00 | 72 |
| Semantic Scholar | Graph API, bulk search, phrases joined by OR | 2026-11-21T15:06:01+00:00 | 2,430 |
| Scopus | Scopus Search API; TITLE-ABS-KEY | 2026-11-21T15:18:47+00:00 | 1,778 |
| Crossref | REST API, query.bibliographic; records kept only with a kratom term in title or abstract | 2026-11-21T15:06:43+00:00 | 2,165 |
| DataCite | REST API; titles and descriptions | 2026-11-21T15:20:14+00:00 | 817 |
| OpenAIRE Graph | API; research products of type publication | 2026-11-21T15:08:20+00:00 | 2,447 |
| CORE | API v3 (authenticated); title or abstract phrases | 2026-11-21T15:17:36+00:00 | 2,308 |
| Reference lists of seven syntheses | OpenAlex referenced_works; records with a kratom term | 2026-11-21T15:18:55+00:00 | 190 |

**Query strings as sent** (from `search/runs/2026-11-21/search_log.json`):

- PubMed: `"kratom"[tiab] OR "kratoms"[tiab] OR "krathom"[tiab] OR "kratum"[tiab] OR "ketum"[tiab] OR "kakuam"[tiab] OR "biak-biak"[tiab] OR "Mitragyna speciosa"[tiab] OR "mitragynine"[tiab] OR "7-hydroxymitragynine"[tiab] OR "mitragynine pseudoindoxyl"[tiab] OR "Mitragyna"[Mesh] OR kratom*[tiab]`
- Scopus: `TITLE-ABS-KEY(kratom OR krathom OR kratum OR ketum OR kakuam OR "biak-biak" OR "mitragyna speciosa" OR mitragynine OR "7-hydroxymitragynine")`
- Europe PMC: `TITLE_ABS:"kratom" OR TITLE_ABS:"kratoms" OR TITLE_ABS:"krathom" OR TITLE_ABS:"kratum" OR TITLE_ABS:"ketum" OR TITLE_ABS:"kakuam" OR TITLE_ABS:"biak-biak" OR TITLE_ABS:"Mitragyna speciosa" OR TITLE_ABS:"mitragynine" OR TITLE_ABS:"7-hydroxymitragynine" OR TITLE_ABS:"mitragynine pseudoindoxyl"`
- Semantic Scholar: `"kratom" / "kratoms" / "krathom" / "kratum" / "ketum" / "kakuam" / "biak-biak" / "Mitragyna speciosa" / "mitragynine" / "7-hydroxymitragynine" / "mitragynine pseudoindoxyl"`
- DataCite: `titles.title:("kratom" OR "kratoms" OR "krathom" OR "kratum" OR "ketum" OR "kakuam" OR "biak-biak" OR "Mitragyna speciosa" OR "mitragynine" OR "7-hydroxymitragynine" OR "mitragynine pseudoindoxyl") OR descriptions.description:("kratom" OR "kratoms" OR "krathom" OR "kratum" OR "ketum" OR "kakuam" OR "biak-biak" OR "Mitragyna speciosa" OR "mitragynine" OR "7-hydroxymitragynine" OR "mitragynine pseudoindoxyl") OR subjects.subject:("kratom" OR "kratoms" OR "krathom" OR "kratum" OR "ketum" OR "kakuam" OR "biak-biak" OR "Mitragyna speciosa" OR "mitragynine" OR "7-hydroxymitragynine" OR "mitragynine pseudoindoxyl")`
- OpenAlex: `title_and_abstract.search:"kratom"/"kratoms"/"krathom"/"kratum"/"ketum"/"kakuam"/"biak-biak"/"Mitragyna speciosa"/"mitragynine"/"7-hydroxymitragynine"/"mitragynine pseudoindoxyl"`
- Crossref: "kratom" (scanned 1,316, kept 1,292); "kratom use" (scanned 3,000, kept 0); "kratom users" (scanned 3,000, kept 0); "kratom dependence" (scanned 3,000, kept 0); "kratom use disorder" (scanned 3,000, kept 0); "ketum" (scanned 32, kept 18); "krathom" (scanned 6, kept 6); "Mitragyna speciosa" (scanned 3,000, kept 586); "mitragynine" (scanned 459, kept 263)
- OpenAIRE: `"kratom" OR "krathom" OR "ketum" OR "Mitragyna speciosa" OR "mitragynine"` (2447)
- CORE: `title:"kratom" OR abstract:"kratom"` (1400); `title:"krathom" OR abstract:"krathom"` (5); `title:"ketum" OR abstract:"ketum"` (277); `title:"Mitragyna speciosa" OR abstract:"Mitragyna speciosa"` (1035); `title:"mitragynine" OR abstract:"mitragynine"` (826)
- Reference lists of seven syntheses (DOIs): 10.1080/15332640.2026.2706579; 10.1159/000539338; 10.1080/00952990.2025.2609965; 10.1080/02791072.2025.2465797; 10.1080/10826084.2026.2697988; 10.1016/j.drugalcdep.2017.10.012; 10.1080/02791072.2018.1562133.

**De-duplication and removal by rule** (`search/dedup.py`):

- Records identified: 17,526; unique after de-duplication on DOI, PMID and normalized title: 4,383 (13,143 duplicates).
- Removed by rule: 118 records typed as non-study by every source, 33 vendor advertisements, and records without a concept B term.
- Records screened: 2,304.

**Benchmark recall.** 9 studies of people who use kratom that assessed use disorder or dependence, from the reference lists of earlier reviews: 9 of 9 were in the screening list.

**Citation searching of the included reports** (after full-text screening; `search/citations_included.py`): 18 included reports (15 found in OpenAlex): 708 records in their reference lists or citing them, 161 not found by the main search, 0 with a kratom term.
