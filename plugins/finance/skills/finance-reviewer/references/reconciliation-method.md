# Reconciliation method (two lists that should agree)

Typical pairs: supplier statement vs AP ledger; PO lines vs invoices received; bank statement vs cashbook; intercompany A vs B; fixed asset register vs GL; contractor claim schedule vs certified amounts.

## Step 1: understand both lists

From the profiler output for each list record: the candidate key columns, the amount column, the date column, sign convention (are credits negative or in a separate column?), and whether amounts include GST. Both lists must be on the same GST basis before matching; convert one side and say so.

## Step 2: choose and normalise the key

Preference order:
1. A shared reference (invoice number, PO number, payment reference, transaction ID).
2. A composite key (supplier plus invoice number; date plus amount).
3. Date plus amount alone (last resort; false matches are possible; mark them "probable").

Normalise before matching: trim, uppercase, strip leading zeros and punctuation (`INV-0001234` and `inv 1234` should match), remove "INV", "TAX INVOICE" prefixes if one side adds them, standardise dates to ISO.

## Step 3: match in passes

| Pass | Rule | Result label |
|---|---|---|
| 1 Exact | key equal and amount equal within $0.01 | MATCHED |
| 2 Key only | key equal, amount differs | AMOUNT DIFFERENCE |
| 3 Tolerance | key equal, amount within tolerance (rounding, FX) | MATCHED (tolerance) with the difference listed |
| 4 One-to-many | one item on A equals the sum of several on B with related keys (partial payments, split invoices) | MATCHED (combined) listing the components |
| 5 Unmatched | anything left | ONLY IN A or ONLY IN B |

Never match the same item twice. Remove matched items from the pool after each pass.

## Step 4: prove it

```
Total A - Total B = sum(ONLY IN A) - sum(ONLY IN B) + sum(AMOUNT DIFFERENCES, A minus B)
```

If the equation does not hold, a matched item was counted twice or an item was dropped. Find it before presenting.

## Step 5: explain the unmatched items

| Pattern | Probable explanation | Reviewer action |
|---|---|---|
| In supplier statement, not in ledger, recent date | Invoice not yet received or not yet entered | Request copy, check AP inbox |
| In ledger, not on statement | Supplier has not applied the payment, or credit not raised | Send remittance advice, request credit note |
| Amount difference equals 10% or 1/11 | GST basis differs | Align basis, re-run |
| Amount difference small and even cents | Rounding or FX | Accept within tolerance, note |
| Amount difference equals a prior item | Payment applied to the wrong invoice | Ask supplier to reallocate |
| Same key twice on one side | Duplicate entry | Reverse one after confirming |
| Date differs by one to three days, amount equal | Timing (bank clearance, period cut-off) | Accept, note the date |

## Presentation rules

- Lists sorted by amount descending within each section.
- Show counts and totals for every section; the reviewer should be able to foot the summary.
- Keep MATCHED to count and total unless the employee asks for the full list.
- Give each unmatched item enough to find it: key, date, amount, description or counterparty.

## CUSTOMISE

Defaults to replace with the company's finance procedures:

- Matching tolerance: `$1.00` or `0.5%`, whichever is smaller (verify)
- Date tolerance for bank items: `3 business days` (verify)
- Ageing buckets for unmatched statement items: `0-30, 31-60, 61-90, 90+ days` (verify)
- Supplier statement reconciliation frequency: `monthly for top 20 suppliers` (verify)
- Who signs off a reconciliation: `preparer and independent reviewer` (verify)
