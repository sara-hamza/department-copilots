---
description: One-page executive brief from multiple reports, notes and spreadsheets - going well, needs attention, key risks, decisions required, likely impact - every point traced to a source
argument-hint: <drop or paste the reports, notes and spreadsheets for the period; say who the brief is for and the period>
---

Run the executive-briefing skill in **brief** mode on:

$ARGUMENTS

Steps:
1. Read every source supplied. PDFs and DOCX through the copilot-common document-reader (keep page and section references); CSV/XLSX through the spreadsheet-reader (run its profile_sheet.py profiler first and compute any figure with a short Python snippet; show results, not code); pasted notes as supplied. Build the SOURCES list first, numbered, with document name, date and author if shown.
2. Follow `references/brief-structure.md` for selection and ordering, and `references/source-tracing-rules.md` for citations: every point ends with `[S<n> p.<x>]` or `[S<n> §<section>]` or `[S<n> sheet <name>]`.
3. Produce the EXECUTIVE BRIEF template from SKILL.md: PERIOD AND SOURCES, GOING WELL (3), REQUIRING ATTENTION (3), KEY RISKS, DECISIONS REQUIRED (one line each; full framing lives in the decisions mode), LIKELY IMPACT, NOT COVERED BY THE SOURCES.
4. One page: about 350 words excluding the sources list. Each point one or two sentences, number first where there is one, then why it matters.
5. If the sources contradict each other, say so in the point and cite both. If a point cannot be traced to a source, it does not go in the brief.
6. If fewer than three items qualify for a section, list what qualifies and write "only <n> items supported by the sources" rather than padding.
