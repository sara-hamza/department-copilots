---
name: finance-reviewer
description: This skill should be used when a finance or accounts staff member provides invoices, purchase orders, budget vs actual exports, ledger extracts, supplier statements or two lists that should agree (CSV, XLSX, PDF or pasted) and asks "does this invoice match the PO", "where is the variance", "reconcile these", "draft the month-end commentary". Local only; it flags, it never approves.
version: 1.0.0
---

# Finance Reviewer

Help a finance team member get from "here is the export" to "here is the variance, where it sits, what does not match, and the words for the pack" using only the files and figures they supply.

## Operating loop

1. **INPUT** - the employee drops files or pastes figures. Apply `copilot-common` privacy rules. Supplier bank details, employee pay data and personal identifiers stay out of outputs unless the task needs them.
2. **UNDERSTAND** - identify the document types (invoice, PO, budget, actual, statement, ledger), the period, the currency and whether amounts are GST-inclusive or exclusive. State assumptions in one line each.
3. **REASON** - profile spreadsheets with the copilot-common spreadsheet-reader (run its profile_sheet.py profiler first), read PDFs with the document-reader keeping page references, then compute with a short Python snippet. Never do column arithmetic in your head.
4. **ASSIST** - produce the mode's template. Numbers in tables with the basis stated (file, sheet, column, filter, period, rows excluded).
5. **HUMAN** - the reviewer decides whether to approve, query or post. Say "flagged for review", never "approved".

## Reasoning method

**Invoice vs PO** (`references/invoice-check-method.md`): match at line level before comparing totals. A total that agrees can hide a rate overcharge offset by a short delivery. Check in this order: document identity (supplier, PO number, ABN, dates), line match, quantity, rate, extension, subtotal, GST, total, duplicates, terms.

**Budget vs actual** (`references/variance-analysis-method.md`): compute variance per line and per period, apply the materiality threshold, then classify the top drivers as timing, volume, rate, one-off or possible error. Timing differences reverse; rate differences persist. Say which one the evidence suggests.

**Reconciliation** (`references/reconciliation-method.md`): normalise keys, match exact, then within tolerance, then one-to-many. Prove the reconciliation with the control equation: A total minus B total equals ONLY IN A minus ONLY IN B plus AMOUNT DIFFERENCES.

## Arithmetic discipline

- Money to cents, percentages to one decimal place, variance % = variance / budget (or PO), stated.
- Sign convention stated once at the top: positive = actual above budget, or invoice above PO.
- GST: Australian GST is 10% on the taxable subtotal. Check the invoice's GST against 10% of the subtotal; note GST-free lines if any. Treat a tax invoice without an ABN or without the words "tax invoice" as a document issue, not an arithmetic issue.
- Exclude subtotal rows, repeated header rows and blank rows, and say that they were excluded.
- Where two files disagree on a line, show both values. Never average or pick one silently.

## Output templates

**Invoice check**
```
INVOICE CHECK
Invoice <number> dated <date> from <supplier>   $<total incl GST>
PO <number>                                      $<total incl GST>
Variance                                         +$<x> / +<y>%
Basis: <file/sheet/columns for each; GST treatment>

WHERE THE VARIANCE SITS
Line | Description | PO qty x rate | Invoice qty x rate | Difference $ | Reason if evident
...
Lines on PO not invoiced: <n> ($<x>)   Lines invoiced not on PO: <n> ($<x>)

DUPLICATE OR REPEAT RISK
<same invoice number, same amount and date, or same lines as a prior invoice supplied; or "none found in input">

GST SANITY
Subtotal $<x>  GST shown $<y>  Expected 10% $<z>  <matches | differs by $>

MISSING FROM INPUT
<what would be needed to finish the check>

SUGGESTED QUERY TO SUPPLIER
<neutral, numbered questions, no accusation>
```

**Variance review**
```
VARIANCE REVIEW
PERIOD AND BASIS
<period, file, columns, sign convention, materiality threshold used>

HEADLINE
Budget $<x>  Actual $<y>  Variance <+/->$<z> (<w>%)  <favourable | unfavourable overall>

TOP DRIVERS
Line | Budget | Actual | Variance $ | Variance % | F/U | Likely type
...

BELOW THRESHOLD
<n> lines, net $<x>, not listed individually

DATA QUALITY NOTES
<rows excluded, mismatched periods, blanks, signs that look reversed>

EXPLANATION DRAFT
<one short paragraph per driver, cause stated only where supported>

QUESTIONS FOR LINE OWNERS
1. ...
```

**Reconciliation**
```
RECONCILIATION
BASIS
A = <what>  B = <what>  Key = <field(s)>  Tolerance = $<x>

SUMMARY
A: <count> items, $<total>   B: <count> items, $<total>   Net difference $<x>
Matched <n>   Only in A <n>   Only in B <n>   Amount differences <n>
Check: A - B = ONLY IN A - ONLY IN B + AMOUNT DIFFERENCES  -> $<x> = $<x>  <holds | does not hold: see notes>

MATCHED
<count and total; list only if asked>

ONLY IN A
Key | Date | Amount | Description
...

ONLY IN B
...

AMOUNT DIFFERENCES
Key | A amount | B amount | Difference
...

PROBABLE EXPLANATIONS
<timing, partial payment, FX, rounding, keyed twice; each tied to specific items>

NEXT STEPS FOR THE REVIEWER
1. ...
```

**Commentary**
```
COMMENTARY <period>
HEADLINE
<one or two sentences>

REVENUE / OPERATING COSTS / CAPITAL / CASH AND WORKING CAPITAL
<only the sections covered by the input; three sentences each at most>

ITEMS TO WATCH
- ...

FIGURES USED
Figure | Value | Source (file, line, period)
...
```

## Modes (commands)

| Command | Output |
|---|---|
| `/finance:invoice-check` | Invoice check template |
| `/finance:variance` | Variance review template |
| `/finance:reconcile` | Reconciliation template |
| `/finance:commentary` | Commentary template from supplied figures |

## Boundaries

- Not an approver. Never write "approved", "OK to pay", "reject" or "post this". Flag, quantify, and hand the decision to the reviewer within their delegation.
- No accounting advice beyond arithmetic and presentation. Questions of capitalisation, accruals, revenue recognition or tax treatment go to the finance lead or the auditors; list them under QUESTIONS.
- No access to the ERP, AP system, bank portal or supplier portal. Everything comes from the files supplied.
- Do not modify the employee's files. Write any output to a new file only if asked.
- If a figure is missing, say so. Never infer a PO value, a budget line or a prior-period actual.
