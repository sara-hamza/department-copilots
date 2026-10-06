# RAID method: classifying and normalising project items

RAID = Risks, Assumptions, Issues, Dependencies. The point of the register is not the list; it is that every item has an owner, a date and a next move. Normalise first, then flag what is missing.

## Classification decision table

| The line says | Type | Test |
|---|---|---|
| "might", "could", "if ... then", "there is a chance" | Risk | Has it happened? No. Could it? Yes. |
| "we are assuming", "on the basis that", "should be", "expected to" with no evidence | Assumption | Being treated as true without confirmation |
| "is", "has", "currently", "blocked", "failed", "late" | Issue | It is happening now and has an impact now |
| "waiting on", "need X from Y", "Y needs X from us", "subject to", "once X delivers" | Dependency | Progress depends on another party or workstream |
| Verb + named person + deliverable | Action | Someone will do something specific |
| "agreed", "decided", "approved", "confirmed" | Decision | Something was settled; record who and the rationale |
| Question mark, "unclear", "TBC", "need to find out" | Open question | Asked, not answered, no one assigned |
| Background, history, restating known facts | Noise | Context only; do not register |

Edge cases:
- A risk that has occurred becomes an issue. Close the risk with "realised, see ISS-n" and open the issue.
- A dependency that is overdue is also an issue. Keep the dependency row and open an issue row that references it.
- An assumption that fails becomes a risk or an issue depending on whether the impact has landed.
- "Developer may not finish civil by March" is a risk until March; after March with civil unfinished it is an issue and an overdue dependency.

## Writing a risk properly

Use cause -> event -> impact so the mitigation is obvious:

`Because <cause>, <event> may occur, leading to <impact on milestone, premises, cost>.`

Example: `Because the developer's civil contractor has not been appointed, pit and pipe for Stage 3 may not be ready by the planned handover of 14 Nov, leading to the RFS milestone slipping past the developer's settlement date and first residents having no service.`

Rate likelihood and impact on the scale below (CUSTOMISE to the company's PMO scale if it differs).

| Scale | Likelihood | Impact |
|---|---|---|
| 1 Low | Unlikely in this project (< 20%) | Absorbed within float; no milestone moves |
| 2 Medium | Could go either way (20 to 60%) | A milestone moves but RFS holds |
| 3 High | More likely than not (> 60%) | RFS, a contractual date or premises count affected |

Score = likelihood x impact. 6 or 9 needs a named mitigation and an owner this week.

## Required fields per register

| Register | Mandatory | Flag if missing |
|---|---|---|
| Risk | ID, statement, likelihood, impact, mitigation, owner, review-by date, status | OWNERLESS, NO DATE |
| Assumption | ID, statement, how it will be validated, owner, validate-by date, status | OWNERLESS, NO DATE |
| Issue | ID, statement, impact now, action, owner, due, status | OWNERLESS, NO DATE |
| Dependency | ID, what, from/to whom, needed-by date, owner on our side, status | OWNERLESS, NO DATE |

Status vocabulary: Open, Monitoring, Mitigating, Escalated, Closed, Realised (risk became issue), Validated or Failed (assumptions).

## Staleness and duplicates

- STALE: no update in the last 14 days, or review/validate-by date has passed (CUSTOMISE in attention-triage-rules.md).
- DUPLICATE candidates: same milestone and same cause with different wording; same dependency logged by two workstreams. List the IDs and suggest which to keep; do not merge without the employee.
- Items with status Closed but a future due date are inconsistent; flag as CHECK STATUS.

## Finding actions in prose

An action needs all three: a verb, an owner, a deliverable. Date is strongly preferred.

| Minutes say | Treat as |
|---|---|
| "Sarah to send the revised BOM to the developer by Thursday" | Action: Sarah, send revised BOM, Thursday (convert if meeting date known) |
| "We need to send the revised BOM" | Unowned action; list under UNOWNED |
| "Should we revisit the splitter ratio?" | Open question |
| "Agreed to go with 1:32 across Stage 2" | Decision |
| "Civil handover now looking like late Nov" | Slip signal; record under SLIPPING or as a dependency with a new forecast |
| "Parking the comms room fit-out discussion until the developer confirms the building" | Parking lot with a trigger |

Quote the fragment that produced each action so the employee can check it. Do not infer owners from who usually does the work.

## Blank register (paste-ready)

```
RISKS
ID | Risk (cause -> event -> impact) | L | I | Mitigation | Owner | Review by | Status

ASSUMPTIONS
ID | Assumption | Validated by | Owner | Validate by | Status

ISSUES
ID | Issue | Impact now | Action | Owner | Due | Status

DEPENDENCIES
ID | We need / They need | From / To | Needed by | Owner | Status
```

## CUSTOMISE

- ID prefixes in use: `R-`, `A-`, `I-`, `D-` (confirm against the PMO register).
- Likelihood and impact scales: 3-point above; replace with the PMO 5-point scale if used.
- Review cadence: risks fortnightly, issues weekly, dependencies at every project meeting (confirm).
- Escalation: score 9, or any issue affecting RFS or a developer contractual date, goes to the delivery manager (confirm name and channel).
