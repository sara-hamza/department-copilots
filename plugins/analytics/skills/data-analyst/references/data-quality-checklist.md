# Data quality checklist

Run this on every export before analysis. Report each issue with the column, the count, example rows and the effect it has on the analyses requested.

## 1. Structure

| Check | How to detect | Effect |
|---|---|---|
| Header row not on row 1 (title rows above) | profiler shows `col1, col2` names or a first row of mostly blanks | re-read with the correct header row |
| Repeated header rows mid-sheet | a text column whose top value equals the header name | exclude and count |
| Subtotal and total rows | rows where the key is blank and the measure is a sum of the rows above; descriptions like "Total", "Subtotal" | exclude; they double count |
| Merged cells or multi-row headers | blank cells below a header, split column names | reconstruct the header; state the mapping |
| Trailing notes or signatures | last rows with text in one column only | exclude |
| Multiple tables on one sheet | a blank row then a new header pattern | split and profile separately |
| Wide vs long layout | one column per month vs one row per month | reshape before trends; say which |
| Units in the header (`Cost ($000)`, `Length (km)`) | header text | state the unit; convert if comparing |

## 2. Completeness

| Check | Threshold | Effect |
|---|---|---|
| Column fill rate | below 95%: note; below 60%: unreliable for analysis | exclude from trends; count blanks as a category only if meaningful |
| Blank rows | any | exclude and count |
| Missing key (ticket number, order ID) | any | cannot deduplicate; report count |
| Missing date on a dated extract | any | exclude from trends; count |
| Blank meaning | is blank "zero", "unknown" or "not applicable"? | state the assumption; never treat blank as zero silently |

## 3. Uniqueness

| Check | Effect |
|---|---|
| Exact duplicate rows | export artefact; exclude after counting |
| Duplicate keys with different values | report; do not sum until the employee says which to keep |
| Key candidate from profiler that is not actually unique | the grain is not what it appears; re-state the grain |
| Near-duplicates (same date, amount, counterparty; different reference) | list under possible double entry |

## 4. Validity

| Check | Rule |
|---|---|
| Negative counts or quantities | impossible unless credits or returns are expected; list |
| Negative durations | end before start; list |
| Percentages above 100 or below 0 | list |
| Dates in the future | beyond today or beyond the extract date; list |
| Dates before the business existed or before the system went live | list (often 1900-01-01 or 1970-01-01 defaults) |
| Dates stored as text | profiler shows type text with date-like values; parse and state the format assumed (DD/MM/YYYY in Australia) |
| Numbers stored as text (`$1,200`, `12%`) | profiler handles common cases; check for stray spaces or footnote markers |
| Out-of-range values | postcode length, fibre count not in {2,4,12,24,48,72,96,144,288}, RX power outside -40 to +10 dBm, speed tier not in the product list |
| Category values outside the expected set | status values other than the known states; list the unexpected ones with counts |

## 5. Consistency

| Check | Example | Handling |
|---|---|---|
| Case and spacing variants | `NSW`, `nsw`, `New South Wales` | normalise for grouping; report the variants |
| Mixed units in one column | metres and kilometres, hours and minutes | detect by magnitude; ask or state the assumption |
| Mixed date formats | `03/04/2026` and `2026-04-03` | parse both; flag ambiguous day/month |
| Start after end | timestamps reversed | exclude from durations; count |
| Status contradicts dates | `Closed` with no closed date, `Open` with a closed date | list |
| Totals column disagrees with components | `Total` not equal to the sum of parts | report the count and largest differences |
| Codes with inconsistent length | leading zeros stripped by Excel | normalise; state it |

## 6. Grain and period

- Say what one row appears to represent and how you decided (key column, distinct counts).
- Say the period covered and whether the first and last periods are complete.
- Say whether the extract is a snapshot (stock as at a date) or a transaction log (movements over a period); the two support different analyses.

## Reporting format

```
DATA QUALITY
Issue | Column | Count | Example rows | Effect on analysis
Blank values | closed_date | 212 (9.9%) | 14, 88, 301 | excluded from time-to-restore
Duplicate rows | all | 17 | 455-456 | excluded
Negative quantity | qty_issued | 4 | 1021, 1402 | listed under impossible values; excluded from usage
Category variants | state | 3 variants of NSW | 12, 77 | normalised to NSW
```

## CUSTOMISE

Defaults to replace with company data conventions:

- Known status sets: tickets `<list>`, orders `<list>`, services `<list>` (fill in)
- Valid fibre counts in use: `2, 4, 12, 24, 48, 72, 96, 144, 288` (verify)
- Valid speed tiers: `<list>` (fill in)
- Date format on exports: `DD/MM/YYYY` (verify per system)
- System go-live dates (earliest valid date per system): `<system>: <date>` (fill in)
- Fill-rate thresholds: note below `95%`, unreliable below `60%` (verify)
