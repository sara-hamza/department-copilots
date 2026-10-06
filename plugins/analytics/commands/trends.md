---
description: Period-over-period comparison (week, month, quarter) with the basis stated and a chart-ready table
argument-hint: <drop the export (CSV/XLSX); say the date column, the measure, the period (week/month/quarter) and any dimension to split by>
allowed-tools: ["Bash"]
---

Run the data-analyst skill in **trends** mode on:

$ARGUMENTS

Steps:
1. Apply the copilot-common spreadsheet-reader skill (run its profile_sheet.py profiler first) to confirm the date column, the measure and any split dimension, then aggregate with a short Python snippet. Show results, not code.
2. Follow the period rules in `references/anomaly-detection-method.md` (section "Period-over-period changes"): complete periods only (flag the partial current period), ISO weeks or calendar months stated, change in absolute and percent, and a rolling average where there are at least six periods.
3. Produce the TRENDS template from SKILL.md: BASIS, HEADLINE (latest complete period vs prior and vs same period last year if available), the CHART-READY TABLE (Period, Value, Change, Change %, Rolling avg, plus one column per split value if a dimension is given), NOTABLE PERIODS (largest rises and falls with dates), CAVEATS.
4. The chart-ready table is plain pipe-separated columns with ISO dates or period labels in the first column so it pastes into Excel without editing. No merged cells, no footnotes inside the table.
5. If the date column has gaps, list the missing periods rather than interpolating. If the measure is a count, say whether blank rows were counted.
6. A trend is a description of the series, not a forecast. Do not extrapolate unless asked, and then label it "simple projection, assumes the recent rate continues".
