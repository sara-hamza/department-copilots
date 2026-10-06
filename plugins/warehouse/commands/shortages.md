---
description: Which items are low, zero or negative against minimum levels or usage - shortages only
argument-hint: <drop the stock export (CSV/XLSX); give minimum levels or usage if the export lacks them>
allowed-tools: ["Bash"]
---

Run the warehouse-assistant skill in **shortages** mode on:

$ARGUMENTS

Steps:
1. If a CSV/XLSX is provided, apply the copilot-common spreadsheet-reader skill (run its profile_sheet.py profiler first), identify on-hand, minimum, on-order and usage columns, then compute with a short Python snippet. Show results, not code.
2. Follow the LOW STOCK rules in `references/stock-analysis-method.md`: negative first, then zero, then below minimum, then below days-of-cover threshold where usage is supplied.
3. Output only the LOW STOCK section of the template in SKILL.md plus a one-line BASIS and an ASSUMPTIONS list. Columns: Item, Description, On hand, On order, Minimum (or cover rule), Shortfall, Days of cover (if usage known), Flag (NEGATIVE / ZERO / BELOW MIN / LOW COVER).
4. Sort by severity then by shortfall descending. Negative stock is a data issue as much as a shortage; say so.
5. If the export contains locations, show the shortage per location only when the employee asks; otherwise pool and say so.
