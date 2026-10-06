---
description: Profile a CSV/XLSX export - columns, types, fill rates, keys - and report data quality problems (missing, duplicates, impossible values)
argument-hint: <drop the export (CSV/XLSX); say what the rows represent if the file name does not make it obvious>
allowed-tools: ["Bash"]
---

Run the data-analyst skill in **profile** mode on:

$ARGUMENTS

Steps:
1. Apply the copilot-common spreadsheet-reader skill: run its profile_sheet.py profiler first on the file (every sheet), then compute any extra checks with a short Python snippet. Show results, not code.
2. Walk `references/data-quality-checklist.md`: completeness, uniqueness, validity (ranges, dates, categories), consistency across columns, and structural problems (merged headers, subtotal rows, trailing notes).
3. Produce the DATA PROFILE and DATA QUALITY templates from SKILL.md: shape (rows, columns, sheets), one line per column (type, fill, distinct, range or top values, key candidate), what the rows appear to represent and the grain, then the quality table (Issue, Column, Count, Example rows, Effect on analysis).
4. State interpretations as interpretations: "Appears to be one row per service order" rather than "This is".
5. If the file cannot be profiled (legacy .xls, password protected, image of a table), say what to export instead.
6. End with READY FOR: one line on which analyses the data supports (anomalies, trends) and which it does not and why.
