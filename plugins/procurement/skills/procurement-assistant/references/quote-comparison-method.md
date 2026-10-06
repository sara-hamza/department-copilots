# Quote comparison method

A quote is comparable only after it has been normalised. Compare normalised figures; show the as-quoted figures beside them so the officer can trace the adjustment.

## Step 1: extract from each quote

| Field | Where to look | If absent |
|---|---|---|
| Supplier legal entity and ABN | letterhead, footer | note "entity not stated" |
| Quote number, date, validity | header | validity missing: flag; expired: not comparable |
| Items, part numbers, descriptions | line table | match on description with care |
| Quantity and unit of measure | line table | unit missing: ask |
| Unit price and extended price | line table | check qty x rate = extension |
| Currency | header or line | assume AUD only if the supplier is Australian and nothing says otherwise; state it |
| GST | subtotal lines | "plus GST", "incl GST" or silent; silent: assume ex GST and flag |
| Delivery terms | terms section | ex works, DAP site, "delivered", FIS; silent: assume ex works and flag |
| Freight | separate line or note | if "to be advised": treat as excluded |
| Lead time | terms or per line | "ex stock", "4-6 weeks from PO"; take the longer figure |
| Warranty | terms | period and scope (parts only, parts and labour, on site) |
| Payment terms | terms | 30 days from invoice, deposit required, progress payments |
| Standards and compliance | item descriptions, attachments | cited standard numbers, test reports, certificates |
| Exclusions and assumptions | terms, notes | commissioning, installation, training, packaging, site access |
| Minimum order quantity, pack sizes | line notes | a 500 m MOQ changes the real cost for 320 m |

## Step 2: normalise

Apply these in order and list each one applied in the BASIS section.

1. **Units**: convert everything to the unit the scope uses. Cable in metres (1 drum = stated drum length); connectors and pigtails each; enclosures each; splitters each. Show the conversion factor.
2. **Quantity**: compare at the scope quantity. If a supplier quotes a different quantity (pack size, MOQ), compute the cost of the quantity actually required plus any forced over-purchase, and show both.
3. **Currency**: convert only with a rate supplied by the employee. Otherwise present in quoted currency and say the comparison is incomplete.
4. **GST**: bring all to ex GST. If a quote is incl GST, divide by 1.1 (standard Australian GST) and say so.
5. **Delivery**: add freight to ex works quotes if a freight figure is supplied or quoted; otherwise mark "freight excluded, not comparable on delivered basis".
6. **Scope gaps**: if one quote includes commissioning and another excludes it, either add the excluded item from a supplied price or compare with the item removed from both; say which.
7. **Validity**: an expired quote is shown but marked not comparable until revalidated.

## Step 3: compare on criteria

| Criterion | How to judge | Weighting note |
|---|---|---|
| Total normalised cost | lowest wins on price alone | only one of several criteria |
| Unit cost | for repeat buys and future call-offs | matters more for framework agreements |
| Lead time | against the required-by date | a cheaper quote that misses the date is not cheaper |
| Warranty | period, scope, who pays freight for returns | parts-only warranty on active equipment is weaker |
| Quantity offered | full scope or partial | partial quotes need a second supplier |
| Compliance | standard cited and evidence supplied | "complies" without evidence is a claim |
| Exclusions | what the officer will still have to buy | add estimated cost if known |
| Validity | days remaining | short validity may force a decision before evaluation ends |
| Payment terms | cash flow impact; deposits increase risk | note, do not price |
| Supplier risk | from the supplier assessment if done | reference it, do not repeat |

## Step 4: recommendation basis

Write it as: "On the stated criteria, <Supplier> best meets the requirement because <criterion>. <Other supplier> is $<x> (<y>%) lower on normalised cost but <trade-off>. Confidence: <likely | possible>, limited by <missing items>."

Never write "award to". The officer decides, often with a panel.

## Matching items across documents (used by compare-bom)

1. Part number or SKU exact match after normalisation (uppercase, strip spaces and punctuation).
2. Manufacturer part number where the supplier uses its own code.
3. Normalised description plus unit: lowercase, collapse spaces, strip pack sizes and colours, keep fibre count and connector type (`12F SMOF loose tube` and `cable, 12 fibre, loose tube, single mode` are the same item; `SC/APC` and `SC/UPC` are not).
4. Anything else is unmatched. Do not force a match on a partial description.

Quantity comparison only after converting units. Price comparison only on the same unit and GST basis.

## Common traps

| Trap | Effect | Handling |
|---|---|---|
| Drum lengths differ (2 km vs 4 km) | per-metre price looks similar, waste differs | compute drums required for the scope and the over-purchase |
| "Price valid for full quantity" | partial orders cost more | note the condition |
| Freight "TBA" | cheapest quote becomes dearest delivered | mark not comparable on delivered basis |
| Alternate item offered | different spec, maybe different standard | list as alternate, compare separately, flag compliance |
| Quote in USD with "subject to exchange" | cost moves after PO | flag; ask for a fixed AUD price |
| Lead time "subject to stock" | no commitment | ask for a committed date |

## CUSTOMISE

Defaults to replace with the company's procurement policy:

- Minimum number of quotes by value: `1 under $5,000; 2 from $5,000; 3 from $25,000; formal tender above $<x>` (verify)
- Preferred delivery basis for comparison: `delivered to our warehouse, ex GST` (verify)
- Mandatory standards for passive fibre plant: `cite the relevant AS/CA or the company engineering standard` (fill in)
- Approved product list: `compare against the current approved product list if supplied` (fill in)
- Evaluation weighting if one is used: `cost 50 / lead time 20 / compliance 20 / warranty 10` (verify or remove)
