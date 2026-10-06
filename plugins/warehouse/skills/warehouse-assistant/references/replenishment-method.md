# Replenishment method (next-month requirement)

Answer "what stock will probably be required next month" from the usage history supplied, then compare with what is on hand and on order.

## Inputs

| Input | Source | If missing |
|---|---|---|
| Issue history by item and date | movements export | cannot forecast; say what export is needed |
| On hand and on order | stock export | requirement cannot be netted; show gross forecast only |
| Lead times | supplier data or CUSTOMISE default | use default and state it |
| Build programme (premises to be connected, estates starting) | employee | forecast from history only; note that build timing is not reflected |
| Bill of materials per premises or per stage | employee or design | needed only for build-driven forecasting |

## Step 1: monthly usage per item

Sum issues per item per calendar month. Returns and adjustments excluded unless the employee says they are genuine consumption. State the number of months with data.

## Step 2: pick the forecasting method per item

| Method | When | Forecast |
|---|---|---|
| Average | at least 3 months of history, no strong trend | mean monthly usage |
| Trend-adjusted | last month more than 30% above or below the average | state both; plan on the higher for critical items, on the average otherwise, and say why |
| Build-driven | employee supplies next month's premises or stages and a BOM per premises | premises x BOM quantity per item, plus a small consumables allowance |
| Range | fewer than 3 months of history | low = smallest month, high = largest month; present as a range, not a point |

Say the method beside every item or group of items.

## Step 3: requirement

```
Requirement = Forecast usage + Safety stock - (On hand + On order)
```

Safety stock default: half a month of usage for consumables, one month for active equipment (CUSTOMISE). If requirement is zero or negative, the item is COVERED.

## Step 4: priority

| Priority | Rule |
|---|---|
| ORDER NOW | days of cover < lead time, or on hand is zero with forecast usage > 0 |
| ORDER THIS MONTH | requirement > 0 and days of cover >= lead time |
| COVERED | requirement <= 0 |

Days of cover = (on hand + on order) / (forecast usage / 30).

## Worked example

SC/APC pigtails: issues Jul 420, Aug 460, Sep 610 (3 months, avg 497). Last month is 23% above average: below the 30% trend trigger, so method = average. Forecast Oct = 497. Safety stock half a month = 249. On hand 380, on order 500. Requirement = 497 + 249 - 880 = negative 134: COVERED. Days of cover = 880 / (497/30) = 53 days.

ONTs: issues Jul 210, Aug 240, Sep 390 (avg 280). Last month is 39% above average: trend-adjusted; critical item, so plan on 390. Safety stock one month = 390. On hand 150, on order 0. Requirement = 390 + 390 - 150 = 630. Days of cover = 150 / 13 = 11.5 days, lead time 42 days: ORDER NOW.

## Presenting the forecast

- One row per item with forecast usage > 0 or on hand > 0.
- Columns: item, description, average monthly usage, last month, forecast, method, on hand, on order, requirement, priority.
- Sort by priority then days of cover ascending.
- Totals: items ORDER NOW, items ORDER THIS MONTH, items COVERED.
- A short ASSUMPTIONS list: months of history, safety stock rule, lead times used, items excluded (no usage), whether build programme was supplied.

## Known limitations to state

- History reflects past builds; a new estate starting next month will not show in the average. Ask for the build programme.
- Stocktake adjustments inside the window distort usage; exclude them and say so.
- Van stock issued but not consumed appears as usage; forecast may be high by the van buffer.
- Items issued in packs but counted in each (or the reverse) produce impossible usage; check the unit before trusting the number.

## CUSTOMISE

Defaults to replace with the company's inventory policy:

- Safety stock: `0.5 month` consumables, `1 month` active equipment (verify)
- Trend trigger: `30%` above or below average (verify)
- Default lead time: `21 days` domestic, `70 days` imported (verify)
- Critical items planned on the higher of trend or average: `ONTs, drop cable, SC/APC pigtails, splitters, FDH spares, OLT SFPs` (verify)
- Typical per-premises BOM for build-driven forecasts: `1 ONT, 1 drop cable run, 2 SC/APC pigtails, 1 wall outlet, 1 premises connection device` (fill in from design standard)
