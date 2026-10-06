# Plain-English findings template

Findings are for readers who will not open the spreadsheet. Each finding stands on its own, carries its evidence, and is honest about confidence and limits.

## Structure of one finding

```
<n>. <One sentence that a manager could repeat in a meeting.>
   Evidence: <the figure, its basis (column, filter, period) and the comparison that makes it meaningful>
   Confidence: <confirmed by the data | likely | possible>
   Caveat: <the one thing that could make this misleading>
```

Rules:
- The statement names the thing, the direction and the size. "Restore times at Riverbend are more than double the network median" beats "Riverbend has issues".
- The evidence gives the number and the comparison. A number without a comparison is not a finding.
- Confidence words: "confirmed by the data" (arithmetic fact, complete data), "likely" (robust across methods, minor gaps), "possible" (one method, small sample, or data quality issues).
- Caveat is mandatory. If there is genuinely none, write "Caveat: none identified; data complete for the period".

## Ordering

1. What the reader asked about.
2. Largest financial or service impact.
3. Anything that would change a decision this week.
4. Data quality issues that affect the above (one finding, not ten).
5. Everything else in one "Also noted" line.

Eight findings at most. More than that is a report, not findings.

## Glossing statistical terms

| Term | Gloss to use the first time |
|---|---|
| median | the middle value; half are above and half below |
| outlier | a value outside the normal range for this data (above the 75th percentile plus 1.5 times the spread) |
| IQR | the spread of the middle half of the values |
| z-score | how many standard deviations from the average |
| correlation | the two measures move together; it does not mean one causes the other |
| week over week | this week compared with the week before |
| rolling average | the average of the last n periods, which smooths out single-week noise |
| concentration | a large share of the total sits in a few values |
| grain | what one row in the data represents |

## Words to avoid

| Avoid | Use instead |
|---|---|
| caused by, because of, due to | is associated with, coincides with, at the same time as |
| proves | shows, indicates |
| significant (unless a test was run) | large, notable, above the threshold |
| always, never | in every row of this extract, in no row of this extract |
| massive, huge, tiny | the number and the comparison |
| trend (for two points) | change between <period> and <period> |

## Worked example

```
FINDINGS
SCOPE
Fault tickets export, 2,140 tickets, 1 Jan to 28 Sep 2026, one row per ticket, reader: Head of Service Delivery.

1. Tickets at Riverbend take more than twice as long to restore as the network as a whole.
   Evidence: median time to restore 14.8 hours (184 tickets, column time_to_restore_h) against 6.2 hours across all 2,140 tickets.
   Confidence: likely
   Caveat: 11 Riverbend tickets have no closed date and are excluded; if they are long-running, the gap is larger, not smaller.

2. Ticket volume jumped by half in the week of 14 September.
   Evidence: 92 tickets opened in ISO week 38 against 61 in week 37 (+31, +50.8%); the 4-week rolling average before the jump was 64.
   Confidence: confirmed by the data
   Caveat: week 39 is partial and excluded, so it is not yet known whether the volume stayed high.

3. One RSP accounts for 38% of all tickets.
   Evidence: 813 of 2,140 tickets, column rsp.
   Confidence: confirmed by the data
   Caveat: without the number of active services per RSP it is not possible to say whether this is above their share of the base.

Also noted: 17 exact duplicate rows removed; 4 tickets have a closed date before the opened date and were excluded from time-to-restore.

WHAT THIS DOES NOT SHOW
- Why Riverbend restore times are longer; the extract has no fault-cause or field-visit columns.
- Whether the week 38 jump continued.

SUGGESTED NEXT QUESTIONS
1. Was there a known event at Riverbend in September? An outage log for the estate would test this.
2. Does the top RSP's ticket share match its service share? A services-by-RSP count would test this.

FIGURES USED
Figure | Value | Column | Filter | Period
Median restore, Riverbend | 14.8 h | time_to_restore_h | estate = Riverbend, closed_date present | Jan-Sep 2026
Median restore, all | 6.2 h | time_to_restore_h | closed_date present | Jan-Sep 2026
Tickets week 38 | 92 | opened_date | ISO week 38 | 2026
Tickets week 37 | 61 | opened_date | ISO week 37 | 2026
Top RSP share | 38% (813/2,140) | rsp | none | Jan-Sep 2026
```

## CUSTOMISE

- Default reader when none is stated: `department manager, non-analyst` (verify)
- Maximum findings: `8` (verify)
- House glossary additions (company-specific terms readers already know and need no gloss): `ONT, RSP, PON, estate, premises passed, premises connected` (verify)
