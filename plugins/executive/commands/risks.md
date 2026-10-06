---
description: Consolidated risk view across multiple reports and registers with likelihood and impact as the sources state them, duplicates merged, gaps flagged
argument-hint: <drop or paste the risk registers, reports and notes; say the audience and whether an existing risk scale applies>
---

Run the executive-briefing skill in **risks** mode on:

$ARGUMENTS

Steps:
1. Read every source (document-reader for PDFs and DOCX with page references; spreadsheet-reader for CSV/XLSX risk registers, running its profile_sheet.py profiler first; pasted notes as supplied). Build the numbered SOURCES list.
2. Extract every risk, issue stated as a risk, and "watch item". Keep the source's own likelihood and impact wording or rating; map it to the common scale in the CUSTOMISE section of `references/brief-structure.md` only where the source's scale is stated, and show both.
3. Merge duplicates across sources (the same risk reported by two departments) into one row citing both; note where the sources rate it differently.
4. Produce the CONSOLIDATED RISK VIEW template from SKILL.md: BASIS AND SCALE, the risk table (Ref, Risk, Likelihood, Impact, Rating, Trend if stated, Owner, Mitigation in place, Source), TOP RISKS (the five highest with why), NEW SINCE LAST PERIOD (if a prior view is supplied), RISKS WITHOUT OWNER OR MITIGATION, GAPS (areas the sources do not cover), and the source citations per `references/source-tracing-rules.md`.
5. Do not add risks the sources do not mention and do not re-rate a risk on the briefing's own judgement. Where a rating looks inconsistent with the narrative in the same source, flag it under a "possible inconsistency" note with both references.
6. Issues (already happened) are listed separately from risks (might happen) if the sources mix them.
