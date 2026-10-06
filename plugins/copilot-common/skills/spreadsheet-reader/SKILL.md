---
name: spreadsheet-reader
description: This skill should be used when an employee provides a CSV, XLSX or XLS export (stock lists, budgets, invoices, POs, pick lists, schedules, RAID logs, data extracts, BOMs, quotes) and wants it profiled, checked, compared, reconciled or analysed. It explains how to profile the sheet locally with the bundled script and how to present numeric findings.
version: 1.0.0
---

# Spreadsheet Reader

Profile employee-supplied spreadsheets locally before analysing them. Never guess column meanings; look.

## Step 1: profile the file

Run the bundled profiler (stdlib only; uses `openpyxl` for .xlsx if installed, otherwise asks for a CSV export):

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/spreadsheet-reader/scripts/profile_sheet.py" "FILE.xlsx"
```

If that path does not resolve (for example when another plugin's command invokes this skill), locate the script and run it from there:

```bash
P=$(find "$HOME/.claude/plugins" -path '*copilot-common*' -name profile_sheet.py 2>/dev/null | head -1); python3 "$P" "FILE.xlsx"
```

Options: `--sheet NAME`, `--rows 10` (sample rows), `--json`.

It prints, per sheet: row/column counts, each column's inferred type, fill rate, distinct count, min/max/sum for numbers, top values for text, and candidate key columns (high distinct ratio). Use this to decide which columns matter before reading data.

## Step 2: confirm meaning with the employee only when ambiguous

If a column header is cryptic (`QOH`, `SOH`, `Amt1`), state the assumption in the output (`Assuming QOH = quantity on hand`) rather than stopping to ask, unless the whole answer hinges on it.

## Step 3: analyse with small scripts, not mental arithmetic

For sums, variances, joins and duplicate detection, write a short Python snippet (csv module or openpyxl) and run it. Show the result, not the code, unless asked. Round money to cents and percentages to one decimal place.

## Common analyses

| Need | Approach |
|---|---|
| Variance (invoice vs PO, budget vs actual) | Join on line item / code, compute delta and % per line, then total; list the top contributors |
| Duplicates | Normalise text (trim, lowercase, collapse spaces), group by the natural key, report groups with count > 1 |
| Shortages / low stock | Compare on-hand vs minimum/reorder level; flag negatives and zeros separately |
| Slow movers | Last movement date older than N months, or zero issues in the period |
| Anomalies | Values outside mean ± 3σ or outside the IQR fence, impossible values (negative quantities, future dates), sudden week-over-week changes |
| Concentration | Top-N share of total (suppliers, SKUs, customers) |

## Presenting numbers

- Put figures in a short table or on their own line, never buried in prose.
- Always state the basis: which column, which filter, which period.
- Say what was excluded (blank rows, subtotal rows, header rows repeated mid-sheet).

## Boundaries

Local files only. Do not open links inside spreadsheets. Do not modify the employee's file; write any output to a new file if a file is wanted.
