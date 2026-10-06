# Reorder planning method

Inputs: on-hand stock, on-order stock, usage history, supplier lead time, minimum order quantity, review period. Output: what to order now, what to order soon, and the arithmetic.

## Definitions

| Term | Formula or meaning |
|---|---|
| Daily usage (D) | total issued in the period / days in the period; state the period and the data points |
| Lead time (L) | days from PO to goods receipt; use the supplier's committed figure, else the CUSTOMISE default |
| Safety stock (SS) | buffer for demand and lead-time variability; see rules below |
| Reorder point (ROP) | D x L + SS |
| Days of cover | (on hand + on order) / D |
| Review period (R) | days between reorder reviews (weekly, fortnightly) |
| Order quantity (Q) | enough to cover D x (L + R) + SS minus (on hand + on order), rounded up to MOQ or pack size |
| Projected stock-out date | today + days of cover (if nothing is ordered) |

## Safety stock rules

Choose one and state it:

1. **Days of usage** (simplest): SS = D x safety days. Default safety days in CUSTOMISE.
2. **Demand variability**: SS = z x standard deviation of daily usage x square root of L. Use z = 1.65 for about 95% service level. Only if the usage history has enough points (at least 12 periods).
3. **Project-driven items**: for items consumed by scheduled builds (drop cable, ONTs, splitters), SS is the next build's requirement rather than a statistical buffer; ask for the build programme.

## Decision bands

| Condition | Band | Action |
|---|---|---|
| on hand + on order <= ROP | ORDER NOW | raise PO for Q |
| days of cover <= L + R but above ROP | ORDER SOON | order at next review; include in plan with a date |
| days of cover > L + R | NO ACTION | count only |
| on hand < 0 | DATA ISSUE | negative stock: list under ASSUMPTIONS, do not plan from it |
| D = 0 in period | NOT FORECAST | list under ASSUMPTIONS; may be obsolete or seasonal |

## Worked example

Drop cable 2-fibre, 500 m reels. On hand 18 reels, on order 0. Issued 96 reels in the last 90 days: D = 1.07 reels/day. Lead time 28 days. Safety days 14: SS = 15 reels. ROP = 1.07 x 28 + 15 = 45 reels. Days of cover = 18 / 1.07 = 17 days. Band: ORDER NOW. Review period 14 days: requirement to next review plus lead time = 1.07 x 42 + 15 = 60 reels; minus 18 on hand = 42 reels; MOQ 10 reels: order 50.

## Usage history handling

- Use issues (stock out to jobs), not receipts.
- Exclude returns and adjustments unless they reflect genuine consumption; say what was excluded.
- If the period includes a known abnormal event (a large build, a stocktake adjustment), say so and offer the figure with and without it.
- Seasonality: if the history is long enough, compare the same months last year; otherwise note the limitation.
- Trend: if the last 30 days are more than 30% above the period average, show both and plan on the higher figure with the reason stated.

## Multi-location stock

If the export has locations (warehouse, vans, site containers), compute per location only if the employee says each replenishes separately. Otherwise pool on-hand across locations and say so; van stock often counts as issued.

## Output notes

- ORDER NOW sorted by days of cover ascending (soonest stock-out first).
- Show the reorder point and days of cover for every ORDER NOW and ORDER SOON item so the officer can check the arithmetic.
- Where the supplier is known from the input, include it; otherwise leave blank rather than guessing.

## CUSTOMISE

Defaults to replace with the company's inventory policy:

- Default lead time when not supplied: `21 days` domestic, `70 days` imported (verify)
- Safety days: `14` for consumables, `28` for active equipment (ONTs, OLT cards, SFPs) (verify)
- Review period: `7 days` (verify)
- Service level target for statistical safety stock: `95%` (z = 1.65) (verify)
- Minimum usage history before planning: `90 days` (verify)
- Critical items that must never stock out (plan on the higher of trend or average): `ONTs, drop cable, SC/APC pigtails, splitters, FDH spares` (verify)
