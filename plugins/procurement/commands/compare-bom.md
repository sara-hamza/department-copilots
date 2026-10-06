---
description: Compare a BOM against another BOM or a supplier quote - quantity, item and price mismatches with unmatched items on each side
argument-hint: <drop both files (CSV/XLSX/PDF) or paste both lists; say which is the reference (design BOM, contractor claim, quote)>
allowed-tools: ["Bash"]
---

Run the procurement-assistant skill in **compare-bom** mode on:

$ARGUMENTS

Steps:
1. If a CSV/XLSX is provided, apply the copilot-common spreadsheet-reader skill (run its profile_sheet.py profiler first) on each file to find the item code, description, unit, quantity and price columns, then match and compare with a short Python snippet. Show results, not code.
2. Follow the matching rules in `references/quote-comparison-method.md` (section "Matching items across documents"): match on part number first, then normalised description plus unit; convert units before comparing quantities (metres vs drums, each vs packs).
3. Produce the BOM COMPARISON template from SKILL.md: BASIS (which document is A, which is B, key used, unit conversions applied), SUMMARY counts, the MISMATCHES table (Item, A qty, B qty, Difference, A price, B price, Price difference, Note), UNMATCHED IN A, UNMATCHED IN B, and QUESTIONS.
4. State the cost impact of quantity mismatches using the price from the quote or contract rates if supplied; otherwise show quantities only and say pricing was not supplied.
5. If one document has no quantities (a pick list of items only), compare presence only and say so.
