---
description: Budget vs actual variance by line and period with top drivers and an explanation draft
argument-hint: <drop the budget vs actual export (CSV/XLSX) or paste the table; say the period and the materiality threshold if known>
allowed-tools: ["Bash"]
---

Run the finance-reviewer skill in **variance** mode on:

$ARGUMENTS

Steps:
1. If a CSV/XLSX is provided, apply the copilot-common spreadsheet-reader skill (run its profile_sheet.py profiler first), identify the budget, actual, period and line/account columns, then compute variances with a short Python snippet. Show results, not code.
2. Follow `references/variance-analysis-method.md`: variance = actual minus budget; sign convention stated; favourable/unfavourable depends on whether the line is revenue or cost; apply the materiality threshold from the CUSTOMISE section unless the employee gives one.
3. Produce the VARIANCE REVIEW template from SKILL.md: PERIOD AND BASIS, HEADLINE (total budget, total actual, variance $ and %), TOP DRIVERS table (Line, Budget, Actual, Variance $, Variance %, F/U, Likely type: timing / volume / rate / one-off / error), BELOW THRESHOLD (count and total only), DATA QUALITY NOTES, EXPLANATION DRAFT and QUESTIONS FOR LINE OWNERS.
4. Classify each driver as timing, volume, rate, one-off or possible error only where the input supports it; otherwise write "cause not evident from input".
5. If no budget column exists, or periods do not line up (YTD vs month), say so under DATA QUALITY NOTES and compute only what is valid.
