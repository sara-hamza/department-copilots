# Stock analysis method (low stock and slow movers)

## Preparation

1. Run the profiler. Identify item code, description, unit, on hand, minimum, on order, last movement, usage and cost columns. Record the assumption for any abbreviated header.
2. Remove subtotal rows, repeated headers and blank rows. Count them.
3. Check units. A line with on hand 2 and unit "drum" may be 4,000 m; a line with unit "m" and on hand 4,000 may be the same stock under another code. Note unit variants for the duplicate pass.
4. Check for multiple locations. Pool unless told otherwise; say which.
5. Check the stock date and the usage period. Usage from last year against stock as at today gives a weak days-of-cover figure; say so.

## Low stock: severity order

| Flag | Rule | Meaning |
|---|---|---|
| NEGATIVE | on hand < 0 | data issue: unrecorded receipt, issue booked twice, wrong unit, or a stocktake not posted. List first; the figure cannot be used for cover |
| ZERO | on hand = 0 and (minimum > 0 or usage > 0) | stocked out; if on order > 0 show the on-order qty |
| BELOW MIN | 0 < on hand < minimum | below the system minimum; shortfall = minimum minus on hand |
| LOW COVER | days of cover < lead time + safety days (CUSTOMISE) where usage is known | will run out before a replenishment could land |

Days of cover = (on hand + on order) / average daily usage. Average daily usage = total issued in the period / days in the period. State the period.

If there is no minimum column and no usage, only NEGATIVE and ZERO can be flagged. Say so.

Sort: NEGATIVE, ZERO, BELOW MIN, LOW COVER; within each, largest shortfall first.

Items with zero usage and zero minimum but zero stock are not shortages; omit them and count them under ASSUMPTIONS.

## Slow movers

Window: default six months (CUSTOMISE). An item is a slow mover when on hand > 0 and there is no issue transaction (or the last movement date is older than the window).

Separate two groups:
- **Never moved**: no issue in the whole history supplied, or last movement is the receipt itself. Often over-purchased or project leftovers.
- **Stopped moving**: issued before the window, nothing since. Often superseded items or completed projects.

For each: on hand, unit, last movement date, months idle, value at cost if a cost column exists (on hand x unit cost; say the cost basis).

Cautions to state in ASSUMPTIONS:
- Critical spares (OLT cards, SFPs, FDH components, test equipment) are expected to be slow movers. Do not recommend disposal; list them with "critical spare?" for the storeperson.
- Seasonal or project items may move again when the next stage starts.
- A receipt within the window without an issue does not make an item active.

## Presenting value

- Value at cost = on hand x unit cost from the cost column. If the column is total value, use it directly and say so.
- Totals per section and overall. Percent of total stock value if the total is known.
- Round to dollars for stock value; cents are noise at this level.

## Data quality checks to report

| Check | Why it matters |
|---|---|
| Items with on hand > 0 but no description | cannot be identified on the shelf |
| Items with usage but on hand blank | stock not tracked for that code |
| Duplicate item codes in the export | the export double counts; dedupe before summing |
| Last movement date in the future | keyed wrongly |
| Unit of measure blank | cover and duplicate checks unreliable |
| Minimum level higher than any stock ever held | minimum set wrongly; flag, do not plan from it |

## CUSTOMISE

Defaults to replace with the company's inventory policy:

- Slow-mover window: `6 months` (verify)
- Low-cover threshold: `lead time + 14 days`; default lead time `21 days` when unknown (verify)
- Critical spares list (never recommend disposal): `OLT line cards, OLT SFPs/transceivers, FDH splitter modules, power supplies, OTDR and power-meter kits` (verify)
- Stock locations that count as issued rather than on hand: `technician vans, site containers` (verify)
- Cost basis: `average cost` or `last purchase price` (verify which the export uses)
