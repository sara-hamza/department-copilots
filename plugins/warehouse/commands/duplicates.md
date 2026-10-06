---
description: Find items that appear to be the same thing under different codes, descriptions or units
argument-hint: <drop the stock export or item master (CSV/XLSX)>
allowed-tools: ["Bash"]
---

Run the warehouse-assistant skill in **duplicates** mode on:

$ARGUMENTS

Steps:
1. If a CSV/XLSX is provided, apply the copilot-common spreadsheet-reader skill (run its profile_sheet.py profiler first) to identify item code, description, unit, manufacturer part number and barcode columns, then group with a short Python snippet. Show results, not code.
2. Follow `references/duplicate-detection-rules.md`: exact duplicate codes first, then same manufacturer part number or barcode, then normalised description, then description plus unit variants (each vs box of 24, metre vs drum).
3. Output only the DUPLICATE CANDIDATES section of the template in SKILL.md plus BASIS and ASSUMPTIONS. For each group: Group, Items (code and description), On hand each, Unit each, Match rule, Confidence (certain / likely / possible), Suggested action for the storeperson to consider.
4. Confidence rules: same code or barcode is certain; same normalised description and unit is likely; description similarity only is possible. Never merge "possible" into the certain count.
5. Items that differ on connector type, fibre count, length or colour are not duplicates; list them under NOT DUPLICATES (LOOK-ALIKES) if the employee would reasonably ask.
