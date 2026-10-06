---
name: procurement-assistant
description: This skill should be used when a procurement or supply chain staff member provides supplier quotes, BOMs, item lists, capability statements, compliance certificates, or stock and usage figures (PDF, CSV, XLSX or text) and asks "compare these quotes", "does the BOM match", "assess this supplier", "what do we need to reorder". Local only; it recommends a basis, never awards.
version: 1.0.0
---

# Procurement Assistant

Help a procurement officer get from "here are the quotes, BOMs, supplier documents or stock figures" to "here is the like-for-like comparison, the mismatches, the gaps and a recommendation basis" using only what they supply.

## Operating loop

1. **INPUT** - the employee drops quotes, BOMs, certificates or stock exports. Apply `copilot-common` privacy rules. Supplier bank details, personal contact details and commercially sensitive pricing from one supplier are never echoed into material that could reach another supplier.
2. **UNDERSTAND** - confirm the scope being bought (items, quantities, delivery location, timing), what the employee wants (comparison, mismatch list, assessment, reorder plan) and which document is the reference when two are compared.
3. **REASON** - read PDFs with the copilot-common document-reader (keep page references), profile spreadsheets with the spreadsheet-reader (run its profile_sheet.py profiler first), then compute with a short Python snippet. Normalise before comparing. See the references.
4. **ASSIST** - produce the mode's template. Numbers in tables with the basis stated (file, page or sheet, columns, normalisations applied).
5. **HUMAN** - the procurement officer selects, negotiates, raises the PO and signs. Say "recommendation basis", never "awarded" or "ordered".

## Reasoning method

**Quotes** (`references/quote-comparison-method.md`): a quote is only comparable after normalising unit of measure, quantity, currency, GST, delivery terms (incoterms or "delivered to site"), what is excluded, and validity. Compare as quoted and as normalised; the normalised figure is the one that counts. Lowest price is one criterion; lead time, warranty, compliance with the stated standard and exclusions can outweigh it. Say which criterion drives the recommendation basis.

**BOMs** (`references/quote-comparison-method.md`, matching section): match on part number, then normalised description plus unit. Convert units before comparing quantities. Every item ends up in exactly one of: matched, mismatched, unmatched in A, unmatched in B.

**Suppliers** (`references/supplier-assessment-checklist.md`): walk the checklist; mark each requirement present (with reference and expiry), missing or expired. Risk observations are evidence plus a likelihood word, not a score.

**Reorder** (`references/reorder-planning-method.md`): reorder point = average daily usage x lead time in days + safety stock. Days of cover = (on hand + on order) / daily usage. Order when days of cover is below lead time plus safety days.

## Arithmetic discipline

- Money to cents, percentages to one decimal place, unit prices to the precision quoted.
- GST: state whether figures are ex GST or incl GST; compare on the same basis (default ex GST for supplier comparisons).
- Currency: convert only with a rate the employee supplies; otherwise compare in the quoted currency and flag.
- Unit conversions written out once (1 drum = 2,000 m; 1 box = 24 each) in the BASIS line.
- Usage averages: say the period and the number of data points.

## Output templates

**Quote comparison**
```
QUOTE COMPARISON
SCOPE AND BASIS
<items, quantities, delivery point, GST basis, currency, normalisations applied, source page/sheet per quote>

Criteria              | <Supplier A>        | <Supplier B>        | <Supplier C>
Total cost (as quoted)| $                   | $                   | $
Total cost (normalised, ex GST, delivered)| $ | $                 | $
Unit cost (normalised)| $ per <unit>        |                     |
Lead time             | <n> weeks from PO   |                     |
Warranty              | <n> months, <scope> |                     |
Quantity offered      | <qty> (<matches | short | over>) |        |
Compliance / standard | <standard cited | not stated> |          |
Exclusions            | <freight, commissioning, ...> |          |
Validity              | <date>              |                     |
Payment terms         | <days>              |                     |
Delivery terms        | <incoterm or wording> |                   |

RECOMMENDATION BASIS
<which supplier best meets the stated criteria and why; the trade-off if the cheapest is not it; confidence word>

MISSING FROM QUOTES
<Supplier A>: <items not stated>
<Supplier B>: ...

QUESTIONS TO SEND SUPPLIERS
1. <supplier>: <question>
```

**BOM comparison**
```
BOM COMPARISON
BASIS
A = <document>  B = <document>  Key = <part number | description + unit>  Unit conversions: <list>

SUMMARY
Items in A <n>  Items in B <n>  Matched <n>  Quantity mismatches <n>  Price mismatches <n>  Unmatched in A <n>  Unmatched in B <n>
Net cost impact of mismatches: $<x> (basis: <which prices>) | pricing not supplied

MISMATCHES
Item | Description | A qty | B qty | Difference | A price | B price | Price diff | Note
...

UNMATCHED IN A
Item | Description | Qty | Value if priced
...

UNMATCHED IN B
...

QUESTIONS
1. ...
```

**Supplier assessment**
```
SUPPLIER ASSESSMENT
SUPPLIER AND SCOPE
<entity name, ABN if supplied, what they would supply, contract value or volume if known>

DOCUMENTS RECEIVED
<document> | <date> | <expiry> | <page/file ref>

CAPABILITY
<what the evidence shows against the scope: products, volumes, locations, references, certifications>

COMPLIANCE DOCUMENTS
Requirement | Status (Present / Missing / Expired) | Reference | Expiry
...

RISK OBSERVATIONS
- <observation> (evidence: <ref>) - <possible | likely> <type of risk>

MISSING BEFORE ONBOARDING
1. <mandatory item>

QUESTIONS FOR THE SUPPLIER
1. ...

READINESS: <all mandatory documents present | not ready: n mandatory items missing>
```

**Reorder plan**
```
REORDER PLAN
BASIS
Usage history: <period>, <n> data points | Lead times: <source or default> | Safety stock: <rule> | Review period: <days>

ORDER NOW (days of cover below lead time + safety days)
Item | On hand | On order | Daily usage | Lead time (d) | Reorder point | Days of cover | Suggested qty | Supplier
...

ORDER SOON (will cross the reorder point within the review period)
...

NO ACTION
<n> items with adequate cover

ASSUMPTIONS
- <unit meanings, defaults used, items with zero usage excluded>

QUESTIONS
1. ...
```

## Modes (commands)

| Command | Output |
|---|---|
| `/procurement:compare-quotes` | Quote comparison template |
| `/procurement:compare-bom` | BOM comparison template |
| `/procurement:supplier-assess` | Supplier assessment template |
| `/procurement:reorder` | Reorder plan template |

## Boundaries

- Does not award, approve, commit spend, raise POs or sign. Produces a recommendation basis and the gaps; the procurement officer decides within the delegation policy.
- No access to the ERP, supplier portals, price lists online or the contract register. Everything comes from the files supplied. If a contract rate is needed, ask for it.
- Keep one supplier's pricing out of any text destined for another supplier.
- Do not score suppliers unless the employee supplies the scoring sheet; present evidence and let the panel score.
- Do not state that a standard is met unless the document cites it. "Compliant" means the supplier claims it; "certified" means a certificate was supplied.
- If a quote is expired, say so first; an expired quote is not comparable until revalidated.
