---
description: What stock will probably be required next month, from the usage history and current stock supplied
argument-hint: <drop the usage or issue history and current stock (CSV/XLSX); say the month to forecast and any known upcoming builds>
allowed-tools: ["Bash"]
---

Run the warehouse-assistant skill in **forecast** mode on:

$ARGUMENTS

Steps:
1. If a CSV/XLSX is provided, apply the copilot-common spreadsheet-reader skill (run its profile_sheet.py profiler first) to identify item, date, quantity issued and location columns, then compute with a short Python snippet. Show results, not code.
2. Follow `references/replenishment-method.md`: monthly usage from the history, trend check on the last 30 days, known build programme adjustments only if the employee supplies them, then requirement = forecast usage + safety stock minus (on hand + on order).
3. Output the REPLENISHMENT RECOMMENDATION section of the template in SKILL.md plus BASIS and ASSUMPTIONS: Item, Description, Avg monthly usage, Last-month usage, Forecast next month, On hand, On order, Requirement, Priority (ORDER NOW / ORDER THIS MONTH / COVERED).
4. State the method for every forecast (average of n months, trend-adjusted, or build-driven). Items with no usage in the period are excluded and counted under ASSUMPTIONS.
5. If the history covers fewer than three months, say that the forecast is weak and show it as a range (last month to average) rather than one figure.
6. A forecast is a recommendation for procurement to act on; do not write "ordered".
