---
description: Check an invoice against its PO - totals, variance $ and %, line differences, duplicates, missing PO lines, rate differences, GST sanity
argument-hint: <drop invoice and PO files (CSV/XLSX/PDF) or paste both, plus any contract rates>
allowed-tools: ["Bash"]
---

Run the finance-reviewer skill in **invoice-check** mode on:

$ARGUMENTS

Steps:
1. If a CSV/XLSX is provided, apply the copilot-common spreadsheet-reader skill (run its profile_sheet.py profiler first) to learn the columns, then compute totals, line joins and differences with a short Python snippet. Show results, not code. PDFs go through the copilot-common document-reader; note the page for every figure taken from a PDF.
2. Follow `references/invoice-check-method.md`: match lines on PO line number, item code or description; compare quantity, rate and extended amount per line; check GST on the invoice total; look for duplicates against any prior invoices supplied.
3. Produce the INVOICE CHECK template from SKILL.md: the headline block (Invoice / PO / Variance $ / Variance %), then WHERE THE VARIANCE SITS as a table (Line, Description, PO qty x rate, Invoice qty x rate, Difference $, Reason if evident), then DUPLICATE OR REPEAT RISK, GST SANITY, MISSING FROM INPUT and SUGGESTED QUERY TO SUPPLIER.
4. State the basis under every table: which file, which sheet, which columns, which rows were excluded (subtotals, blanks, freight if separated).
5. If only the invoice is supplied, or only the PO, say so under MISSING FROM INPUT, produce what can be checked (arithmetic, GST, internal duplicates) and stop. Do not infer PO values.
6. Never write "approved", "OK to pay" or "reject". Write what matches, what does not, and what a reviewer should confirm.
