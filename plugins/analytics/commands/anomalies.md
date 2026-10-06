---
description: Find anything unusual - outliers, concentrations, week-over-week changes and correlations - with the detection method stated for each
argument-hint: <drop the export (CSV/XLSX); name the measure and date columns if you know them, and what "unusual" means for this data>
allowed-tools: ["Bash"]
---

Run the data-analyst skill in **anomalies** mode on:

$ARGUMENTS

Steps:
1. Apply the copilot-common spreadsheet-reader skill (run its profile_sheet.py profiler first) to find numeric measures, date columns and categorical dimensions, then compute with a short Python snippet. Show results, not code.
2. Follow `references/anomaly-detection-method.md`: IQR fence and z-score for outliers (both, report where they agree), top-N share for concentration, week-over-week or period-over-period change against the threshold, Pearson correlation only between numeric columns with enough rows, impossible values from the data-quality checklist.
3. Produce the ANOMALIES template from SKILL.md: BASIS, then one block per finding type (OUTLIERS, CONCENTRATIONS, PERIOD CHANGES, CORRELATIONS, IMPOSSIBLE VALUES) each with a table and a Method line stating the rule and threshold used, then WHAT TO CHECK FIRST (ranked) and CAVEATS.
4. Each anomaly row carries the identifying columns (date, site, item, RSP, whatever the grain is) so the reader can find it in the source.
5. Where the data has fewer than 30 rows for a measure, say that statistical fences are weak and report only impossible values and the largest absolute differences.
6. Describe, do not explain. "Tickets for estate X are 3.4x the median" is a finding; "because of a splitter fault" is a hypothesis and belongs under WHAT TO CHECK FIRST.
