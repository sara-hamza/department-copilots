---
description: Compare two or more supplier quotes for the same scope - normalised Criteria x Supplier table, recommendation basis, what is missing from each quote
argument-hint: <drop the quotes (PDF/CSV/XLSX) or paste them; state the scope, quantities required and any must-have criteria>
allowed-tools: ["Bash"]
---

Run the procurement-assistant skill in **compare-quotes** mode on:

$ARGUMENTS

Steps:
1. Read each quote. PDFs go through the copilot-common document-reader (keep page references). If a CSV/XLSX is provided, apply the copilot-common spreadsheet-reader skill (run its profile_sheet.py profiler first), then compute line totals and normalised unit prices with a short Python snippet. Show results, not code.
2. Follow `references/quote-comparison-method.md`: normalise every quote to the same unit of measure, quantity, currency, GST basis and delivery terms before comparing. State each normalisation made.
3. Produce the QUOTE COMPARISON template from SKILL.md: SCOPE AND BASIS, the Criteria x Supplier table (Total cost normalised, Unit cost, Lead time, Warranty, Quantity offered, Compliance and standards, Exclusions, Validity, Payment terms, Delivery terms), then RECOMMENDATION BASIS with reasoning, MISSING FROM QUOTES per supplier, and QUESTIONS TO SEND SUPPLIERS.
4. Where a quote excludes something another includes (freight, commissioning, GST), show the comparison both as quoted and as normalised, and say which figure is comparable.
5. If only one quote is supplied, produce the normalised single-quote summary and the MISSING FROM QUOTES list; say that no comparison is possible yet.
6. The recommendation is a basis for the procurement officer's decision, not an award. Write "lowest comparable cost is", "best meets the stated criteria", never "award to".
