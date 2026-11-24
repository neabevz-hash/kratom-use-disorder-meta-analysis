# Check run of the v1.0 search code (2026-11-21)

Run before freezing the protocol, to test the code, the seed-set recall and concept B. Not the final search: the final search runs with the frozen code after the OSF registration.

- `search_log.json` — query strings, record counts and timings per source (`search/search.py`).
- `dedup_report.json` — de-duplication and removals before screening (`search/dedup.py`): 17,528 records → 4,385 unique → 2,304 to screen (118 non-study records, 33 vendor advertisements, 1,930 outside concept B).
- `recall_seed_set.json` — recall on the seed set: 9 of 9 (`search/recall.py`).
- Raw exports (`raw/`), `records_unique.jsonl`, `screening.csv` and `screening.ris` stay local (git-ignored); they are reproduced by the scripts.
- After the first de-duplication, use and dependence terms in Czech, Polish, German, Spanish, Portuguese and French were added to concept B (Czech theses on kratom use had been removed); the numbers above are after that change.
- Stand test of the screener prompt on 13 records of this run: `screening/stand_test_ids.py`, `screening/llm/stand_test_2026-11-21-check_*.jsonl`.
