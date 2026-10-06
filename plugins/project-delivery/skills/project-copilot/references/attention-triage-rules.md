# Attention triage rules: ranking what needs the delivery lead today

Everything in the input gets a rank. The output lists only what the rank says matters today, puts the rest under WAITING ON, DECISIONS REQUIRED, SLIPPING or NOTHING NEEDED, and names the rule that placed each item.

## Ranking order

| Rank | Rule | Why it comes first |
|---|---|---|
| 1 | **Blocked milestone**: a milestone (civil handover, haul complete, RFS, first connection) cannot proceed because of an open issue or unmet dependency | Every day lost here moves the end date and the developer's settlement commitments |
| 2 | **Overdue dependency**: something we need from the developer, contractor, design, power authority or council is past its needed-by date | The slip is already happening; a chase today is cheaper than a replan next week |
| 3 | **Unowned decision**: a decision is required, nobody owns it, or the owner is not named | Nothing will happen until someone is asked; the lead is the default owner |
| 4 | **Stale item**: a risk, issue or dependency with no update beyond the threshold, or a passed review date | Either it is resolved and should be closed, or it is being ignored |
| 5 | **Overdue action**: a named action past its due date | Someone owes something; a reminder today keeps it from becoming an issue |
| 6 | **Decision with a deadline inside 5 working days** | Needs scheduling now to meet the date |
| 7 | **New risk with score 6 or 9** | Needs a mitigation and owner assigned this week |
| 8 | Everything else | Monitoring only |

Tie-breakers, in order: more days overdue first; more premises or lots affected first; items touching RFS or a contractual date first; then input order.

## Where each rank lands in the template

| Rank | Section |
|---|---|
| 1, 2, 3 | TODAY (numbered, highest first) |
| 4, 5 | TODAY if the lead is the owner or chaser; otherwise WAITING ON |
| 6 | DECISIONS REQUIRED |
| 7 | TODAY only if no owner; otherwise RISKS section of the status report |
| 8 | NOTHING NEEDED, with a revisit date |
| Any item with forecast later than baseline | Also listed under SLIPPING |

TODAY should rarely exceed seven items. If more than seven rank 1 to 3, list them all but mark items 8 onward as "TODAY (overflow)" so the lead can see the load.

## WAITING ON rules

- Each row needs: who, what, since when, chase-by date. The chase-by date is the needed-by date minus the lead time the item requires; if unknown, use needed-by minus 5 working days and say so.
- Group by party (developer, civil contractor, design, internal engineering, power authority, council) so one message can cover several items.
- If the "since" date is unknown, use the date of the input that first mentions it and mark it `since (first seen)`.

## DECISIONS REQUIRED rules

- State the decision as a question with the options if the input gives them.
- Name the owner if stated; otherwise `owner: TBC (lead to assign)`.
- Needed-by date: the date after which a milestone moves. If not stated, say so.
- Do not recommend an option unless the employee asks; list consequences of each if the input supports them.

## SLIPPING rules

- A slip exists only when both a baseline and a forecast (or an actual later than baseline) are in the input. Otherwise write `late, no baseline stated`.
- Show the number of calendar days.
- Name the cause only if the input states it; otherwise `cause: not stated`.
- Flag the downstream milestone most likely affected (civil handover -> haul -> RFS), marked as "likely" since the schedule logic is not in the paste.

## NOTHING NEEDED rules

Only items that are explicitly parked, closed, on track with a future date, or delegated with an owner and date belong here. State why it can wait and the date to look again. Do not use this section to hide items that are merely unclear; those go to MISSING INFORMATION.

## Reading a schedule export

When the input is a schedule CSV/XLSX (profiled with spreadsheet-reader), the columns that matter are: task name, baseline start/finish, forecast or current start/finish, actual finish, % complete, owner/resource, predecessor, milestone flag. Rules:
- A task with % complete < 100, forecast finish earlier than today and no actual finish is overdue.
- A milestone row with forecast later than baseline is SLIPPING.
- A task whose predecessor is overdue is at risk of slipping even if its own dates look fine; list it as "exposed" under SLIPPING.
- Summary rows (level 1 or rolled-up) are context; rank leaf tasks and milestones.

## Reading minutes

Minutes rarely have dates and owners on every line. Apply the decision table in raid-method.md, then rank. Unowned and undated items are findings in their own right; list them once under MISSING INFORMATION rather than repeating "not stated" on every row.

## CUSTOMISE

- Stale threshold: 14 days without update (adjust to the PMO cadence).
- Decision horizon: 5 working days.
- Milestone names used in company delivery (confirm and add): Developer agreement executed, Design approved, Civil handover accepted, Haul complete, Splicing complete, FDH commissioned, Testing complete, RFS declared, First connection.
- Working calendar: Monday to Friday, Australian public holidays for the state of the estate.
- Who the lead escalates blocked milestones to: delivery manager (confirm name and channel).
