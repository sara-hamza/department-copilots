# Invoice vs PO check method

Work line by line before looking at totals. A matching total can hide two offsetting errors.

## Step 0: identify the documents

| Check | Invoice | PO | Note if different |
|---|---|---|---|
| Supplier legal name and ABN | | | Different entity to the PO supplier is a document issue |
| PO number quoted on invoice | | | No PO number: cannot match automatically; ask the supplier |
| Invoice number and date | | | Date before PO date is unusual; note it |
| Currency | | | Convert only if a rate is supplied; otherwise flag |
| GST treatment (inclusive / exclusive / mixed) | | | State the assumption used |
| Delivery or service period | | | Period outside PO validity: flag |
| Payment terms | | | Terms on invoice shorter than contract terms: flag |

## Step 1: match lines

Match keys in order of reliability:
1. PO line number quoted on the invoice.
2. Item or part code.
3. Normalised description (trim, lowercase, collapse spaces, strip pack sizes) plus unit price.
4. Description similarity as a last resort; mark these matches "probable".

Outcomes per invoice line: matched, matched with difference, not on PO. Outcomes per PO line: invoiced in full, partly invoiced, not yet invoiced.

## Step 2: compare each matched line

| Compare | Formula | Flag when |
|---|---|---|
| Quantity | invoice qty minus PO qty (or remaining qty after prior invoices) | any over-delivery; under-delivery is noted, not flagged |
| Unit rate | invoice rate minus PO rate | any difference; even cents matter on high-volume lines |
| Unit of measure | each vs box vs metre vs drum | mismatch; a drum of 2 km cable invoiced "per metre" changes the extension |
| Extension | qty x rate vs extended amount shown | difference greater than $0.01 rounding |
| Discount | PO discount applied? | discount missing or smaller |

Rate difference in $ for the line = (invoice rate minus PO rate) x invoice qty. Quantity difference in $ = (invoice qty minus PO qty) x PO rate. The two together plus any extension error equal the line variance. Present them so the reviewer can see which one drives it.

## Step 3: totals

```
Sum of matched line differences
+ lines invoiced not on PO
- PO lines not invoiced (only if comparing to the full PO value)
+ freight / handling / surcharges not on the PO
= invoice total minus PO total (ex GST)
```

Variance % = variance / PO total, one decimal place. Say whether the comparison is to the full PO or to the remaining PO balance after prior invoices.

Worked example of the headline block:

```
Invoice INV-20441 dated 28 Sep 2026 from <supplier>   $128,400.00 incl GST
PO 4500018822                                          $116,000.00 incl GST
Variance                                               +$12,400.00 / +10.7%
```

## Step 4: GST sanity

- GST = 10% of the taxable subtotal. Compare the GST shown with 10% of (subtotal minus GST-free lines).
- Total = subtotal + GST. Check it.
- A "tax invoice" must say so and show the supplier ABN when the total is $82.50 or more (ATO rule; confirm with finance policy).
- GST on a GST-free item (some exports, some insurance components) is a query, not an arithmetic error.

## Step 5: duplicates and repeats

Check against any prior invoices supplied:
- Same invoice number: duplicate.
- Same supplier, same amount, within 7 days, different invoice number: possible duplicate; ask.
- Same PO lines already invoiced in full: repeat billing.
- Invoice number sequence gap or re-use: note only.

If no prior invoices are supplied, write "no prior invoices supplied; duplicate check limited to this document".

## Step 6: what to write back to the supplier

Neutral, numbered, answerable:
1. "Line 4 is invoiced at $412.00 per unit; PO 4500018822 line 4 is $380.00. Please confirm the applicable rate or issue a credit."
2. "Line 9 (freight, $1,240.00) is not on the PO. Please advise the authority for this charge."
3. "Quantity on line 2 is 120; the PO balance is 100. Please confirm the delivery docket reference."

## Common causes of variance (for the Reason column)

| Pattern | Usual cause |
|---|---|
| Rate up on every line by the same % | Price rise not reflected in PO, or CPI clause |
| One line much higher | Wrong unit of measure or wrong item |
| Extra lines at the bottom | Freight, surcharge, variation claimed without a PO amendment |
| Quantity over PO | Over-delivery, or a second delivery against a closed line |
| Total matches, lines differ | Offsetting errors; still needs correction for the ledger |
| Credit expected but absent | Prior short delivery or returned goods |

## CUSTOMISE

Defaults to replace with the company's AP policy:

- Tolerance before a query is raised: `$50 or 2% per line, whichever is greater` (verify)
- Rate tolerance: `none; any rate difference is queried` (verify)
- Freight accepted without a PO line: `up to $250 if PO says "plus freight"` (verify)
- Invoices without a PO number: `return to supplier` (verify)
- Delegations: review by `AP officer`, approval by `cost centre owner within delegation`, above `$<x>` by `<role>` (fill in)
- Three-way match required (PO, goods receipt, invoice): `yes for stock items` (verify)
