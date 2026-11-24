**Supplementary File S4.** Use of generative AI

Models: Claude Opus 5.5 (`claude-opus-5-5`) and Claude Sonnet 5.5 (`claude-sonnet-5-5`), Anthropic, run headless through Claude Code 2.1.289; the model and version were stored with every output. Runs: title-and-abstract passes 21–22 November 2026 (2,304 records × 2 passes); full-text proposals 22–23 November 2026; extraction and risk-of-bias drafts 22–23 November 2026.

| Task | Prompt file | Frozen under git tag | SHA-256 |
| --- | --- | --- | --- |
| Title-and-abstract screening | `screening/llm_screener_prompt.md` | `kratom-prereg-v1.0 (registered)` | `9cdeef328dfda329…` |
| Full-text eligibility proposals | `fulltext/ft_prompt.md` | `kratom-ft-prompt-v1.0` | `448c0a79f29bb1b0…` |
| Extraction and JBI drafts | `extraction/extract_prompt.md` | `kratom-extraction-prompt-v1.0` | `9778d2c1d55e0347…` |

**Calibration** (300 random records, the author blind to the model labels; labels sealed with SHA-256 before unblinding). Rule "full text unless both passes exclude": sensitivity 0.94 (33/35), specificity 0.98 (261/265), κ = 0.91. Agreement between passes: κ = 0.92. Records missed by the rule: 2; safeguard triggered.

**Safeguard.** 1,154 double exclusions with a term for people or without an abstract re-screened blind by the author: 0 moved to full text; 605 double exclusions without such terms not re-screened.

**Records retained by at least one pass.** 245 decided by the author with the model labels shown; 235 reports sought in total.

**Extraction.** 14 samples, 98 estimates, 1,596 drafted values verified by the author against the sources; 4 corrected (0.25%). Model quotations found verbatim in the source: 86% of estimates and 94% of key fields (the rest were paraphrased tables or text broken by PDF conversion; each value was checked by the author regardless).

**Manuscript.** Claude Code wrote the search, screening and analysis code and drafted the text from the author's analysis outline; the author revised and approved the text.
