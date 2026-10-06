---
description: Full stock analysis from a stock export - low stock, slow movers, duplicate candidates, replenishment recommendation, assumptions
argument-hint: <drop the stock export (CSV/XLSX) and, if available, the movement or usage history; say the period and any minimum levels>
allowed-tools: ["Bash"]
---

Run the warehouse-assistant skill in **stock-analysis** mode on:

$ARGUMENTS

Steps:
1. If a CSV/XLSX is provided, apply the copilot-common spreadsheet-reader skill (run its profile_sheet.py profiler first) to identify item code, description, unit, on-hand, minimum or reorder level, on-order, last movement date and usage columns, then compute with a short Python snippet. Show results, not code. State any column meaning assumed (`Assuming SOH = stock on hand`).
2. Follow `references/stock-analysis-method.md` for low stock and slow movers, `references/duplicate-detection-rules.md` for duplicate candidates and `references/replenishment-method.md` for the recommendation.
3. Produce the full STOCK ANALYSIS template from SKILL.md: BASIS, LOW STOCK, SLOW MOVERS, DUPLICATE CANDIDATES, REPLENISHMENT RECOMMENDATION, ASSUMPTIONS. Each table carries the basis line (file, sheet, columns, filter, period).
4. If there is no usage or movement history, produce LOW STOCK against minimum levels only, say that SLOW MOVERS and REPLENISHMENT cannot be computed, and list what export would allow it.
5. If there are no minimum levels, use the CUSTOMISE default rule (days of cover from usage) and say so; if neither usage nor minimums exist, list zero and negative stock only.
6. Never write "adjusted", "merged" or "ordered". Recommend; the storeperson and procurement act.
