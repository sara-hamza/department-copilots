# Variance analysis method (budget vs actual)

## Definitions

- Variance $ = Actual minus Budget. State this once; some packs use Budget minus Actual.
- Variance % = Variance $ / Budget. If Budget is zero, show "n/a" and the $ only.
- Favourable (F): revenue above budget, or cost below budget. Unfavourable (U): the reverse.
- Period: month, quarter, YTD, full year. Compare like with like. A month actual against a YTD budget is not a variance.

## Step 1: shape the data

From the profiler output, identify: line or account column, cost centre or project column (if any), budget column(s), actual column(s), period columns. Decide whether the sheet is wide (one column per month) or long (one row per line per period). Reshape in the Python snippet if needed.

Exclude: subtotal and total rows (they double count), rows with no account, repeated headers. Say how many rows were excluded.

## Step 2: compute

Per line and per period: variance $, variance %, F/U. Then roll up to the total and prove it: the sum of line variances equals total actual minus total budget.

## Step 3: materiality

Report individually any line where either test is met; roll up the rest into BELOW THRESHOLD.

| Test | Default |
|---|---|
| Absolute | variance $ at or above the threshold in the CUSTOMISE section |
| Relative | variance % at or above the threshold AND variance $ above a floor (avoids $30 on a $100 budget) |

Rank the reported lines by absolute variance $, largest first.

## Step 4: classify each driver

| Type | What the evidence looks like | Will it reverse? |
|---|---|---|
| Timing | Budget phased evenly, actual lumpy; invoice arrived early/late; accrual missing | Yes, in a later period |
| Volume | More or fewer units, premises, lots, tickets than planned; rate per unit unchanged | No, unless demand changes |
| Rate | Same volume, higher unit price, wage rate, contractor rate, FX | No; persists |
| One-off | Single invoice, write-off, settlement, project close-out | No, but does not recur |
| Possible error | Posted to the wrong account or period, sign reversed, duplicate posting | Yes, once corrected |

Write "cause not evident from input" when the data gives no basis. Never infer a cause from the account name alone.

## Step 5: explanation draft

One short paragraph per driver:
1. The line and the variance ($ and %).
2. The type and the evidence for it.
3. Whether it reverses, and any action (reforecast, accrual, PO amendment, query).

Example: "Contractor splicing costs are $84,200 (18.3%) above budget for September. The volume of premises passed was 1,210 against 980 planned, so this appears to be volume driven; the average cost per premises is within 1% of budget. Not expected to reverse; the full-year forecast should be revisited if the acceleration continues."

## Commentary structure

For the monthly pack (used by the commentary command):

```
HEADLINE        One or two sentences: the overall result and the single biggest reason.
REVENUE         Result vs budget, main drivers, outlook if supported.
OPERATING COSTS Result vs budget, top two or three drivers, timing vs permanent.
CAPITAL         Spend vs plan, projects ahead or behind, commitments if given.
CASH            Balance, movement, working capital points if given.
ITEMS TO WATCH  Short bullets; things that could become material next period.
```

Rules: point first, number second, cause third. No adjectives without a number. No forecast unless the input contains one. Every number in the prose must appear in the FIGURES USED table with its source.

## Common data problems

| Symptom in profiler output | Likely issue | Handling |
|---|---|---|
| Budget column sum much larger than actual sum | Budget is full year, actual is YTD or month | Compare to phased budget or say the comparison is invalid |
| Negative costs | Credits, reversals, or sign convention differs by column | Show them; do not net silently |
| Fill rate well below 1 on account column | Subtotal rows or blank spacer rows | Exclude and count them |
| Same account appears twice | Two cost centres or duplicated rows | Group by account plus cost centre; flag if identical rows |
| Actual exactly equals budget on many lines | Accruals booked at budget | Note as "accrued at budget; true variance unknown" |

## CUSTOMISE

Defaults to replace with the company's management reporting policy:

- Materiality, absolute: `$10,000` per line per month (verify)
- Materiality, relative: `10%` with a `$2,000` floor (verify)
- Capital projects materiality: `$25,000` or `5%` of approved budget (verify)
- Favourable/unfavourable convention for revenue and cost lines: as above (verify against the pack)
- Period convention: `month and YTD both reported` (verify)
- Commentary audience and length: `CFO pack, one page` (verify)
