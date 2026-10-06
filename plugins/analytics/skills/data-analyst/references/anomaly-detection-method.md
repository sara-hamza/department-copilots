# Anomaly detection method

Every anomaly reported must carry its method and threshold so the reader can judge it. Run more than one method where possible and say where they agree.

## Outliers in a numeric column

**IQR fence** (robust to skew; preferred default)
- Q1 = 25th percentile, Q3 = 75th percentile, IQR = Q3 - Q1.
- Lower fence = Q1 - 1.5 x IQR; upper fence = Q3 + 1.5 x IQR.
- Extreme fence (optional): 3 x IQR.
- Report values outside the fence with the fence values shown.

**z-score** (assumes roughly symmetric data)
- z = (value - mean) / standard deviation (sample SD).
- Threshold 3 by default; 2.5 for small or noisy data if the employee agrees.
- Weak when the data is skewed (costs, durations); say so if the mean and median differ by more than 20%.

**Report**: a value flagged by both methods is "likely outlier"; by one only is "possible outlier". Always show the median and the fence or threshold beside the value.

**Minimum rows**: 30 for either method. Below that, report only impossible values and the largest absolute differences, and say the fences are weak.

**Group-wise outliers**: when the data has a natural group (estate, RSP, technician, item), compute fences within the group as well as overall. A value normal overall may be extreme for its group, and the reverse.

## Concentration

- Share of total for each value of a dimension: value total / grand total.
- Top-1 share, top-3 share, and the count of values making up 80% of the total.
- Flag when top-1 share exceeds the threshold (default 40%) or when fewer than 3 values make up 80%.
- Use the right measure: count of rows for events (tickets, faults), sum for amounts (cost, quantity).
- Concentration is only unusual relative to expectation: 40% of tickets from the largest estate may be proportional to its premises. Say "compare with the premises or volume base if available".

## Period-over-period changes

- Choose the period from the date column density: daily data with 8 or more weeks -> weekly; otherwise monthly; quarterly for multi-year data.
- Weeks are ISO weeks (Monday start) unless the employee uses another convention; say which.
- Exclude the partial current period. Label it as excluded.
- Change = current - prior; change % = change / prior (n/a if prior is zero).
- Flag when |change %| exceeds the threshold (default 25% week over week, 15% month over month) and the absolute change is above a floor (so a move from 2 to 3 is not "50% up" in the headline).
- Rolling average: 4 periods for weekly, 3 for monthly, when at least 6 periods exist.
- Same period last year: report if the data covers it.
- Gaps: list missing periods; never interpolate.

## Correlation

- Pearson r between two numeric columns on rows where both are present.
- Report only when rows >= 30 and |r| >= 0.5. Mention |r| between 0.3 and 0.5 as "weak association" only if the employee asked about those columns.
- Always add "association, not cause". Check for a shared driver (both grow with volume) before treating it as interesting.
- Spearman rank correlation is a better choice when either column is skewed or has outliers; use it and say so if the IQR step flagged many outliers.

## Impossible or suspicious values

Take the list from `data-quality-checklist.md` and report counts and example rows. These are anomalies of data entry, not of the business, and must be separated from business anomalies.

## Duplicates as anomalies

- Exact duplicate rows: count and examples; usually an export artefact.
- Duplicate keys with different values: more serious; list them.
- Near-duplicates (same date, same amount, different reference): possible double entry; list under "possible".

## Ranking "what to check first"

Order by: (1) impossible values that would corrupt totals, (2) outliers flagged by both methods on the measure the reader cares about, (3) period changes beyond threshold in the latest complete period, (4) concentrations without an obvious proportional base, (5) correlations. For each, give the one check that would confirm or dismiss it.

## Worked example

Fault tickets export, 2,140 rows, one per ticket, Jan to Sep. Measure: time to restore (hours). Overall median 6.2 h, Q1 3.1, Q3 11.4, IQR 8.3, upper fence 23.9 h. 61 tickets above the fence; 38 of those also have z > 3 (likely outliers). Group-wise: estate "Riverbend" median 14.8 h against 6.2 overall; 22 of the 61 are Riverbend. Week over week: ISO week 38 count 92 vs week 37 count 61, +50.8%, above the 25% threshold, absolute +31. Concentration: top RSP 38% of tickets (below the 40% flag). What to check first: whether Riverbend's restore times coincide with a known event in weeks 37-38 (hypothesis, not conclusion).

## CUSTOMISE

Defaults to replace with the team's own conventions:

- IQR multiplier: `1.5` (extreme `3`) (verify)
- z-score threshold: `3` (verify)
- Concentration flag: top-1 share above `40%`, or fewer than `3` values making 80% (verify)
- Week-over-week flag: `25%` with absolute floor `10` (verify); month-over-month `15%` with floor `20` (verify)
- Week convention: `ISO, Monday start` (verify)
- Correlation reporting: `|r| >= 0.5 and n >= 30` (verify)
- Minimum rows for statistical fences: `30` (verify)
