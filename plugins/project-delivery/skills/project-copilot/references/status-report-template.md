# Status report template and RAG rules

One page. Decisions and asks are what the reader acts on; everything else supports them. Follow the writing-helper status structure: status word first, three bullets of progress, blockers, asks.

## RAG definitions (CUSTOMISE to the company PMO)

| Colour | Schedule | Cost | Scope | Risk |
|---|---|---|---|---|
| GREEN | All milestones forecast on or before baseline, or within float | Forecast within approved budget | No uncontrolled change | No open risk scored 6 or above without mitigation |
| AMBER | A milestone forecast to slip but RFS and contractual dates hold; recovery plan exists | Forecast over budget by up to the tolerance (default 5%) with a plan | Change requests raised, awaiting approval | A risk scored 6 or above with mitigation under way |
| RED | RFS or a contractual date will move, or no recovery plan | Over tolerance or no plan | Unapproved scope being delivered | A risk scored 9 with no mitigation, or a realised risk affecting RFS |

Rules:
- OVERALL is the worst of the four unless the employee states a reason to differ; record the reason.
- Never set COST without cost figures in the input. Write `not assessed`.
- A RAG change from the previous report must be explained in the OVERALL line ("AMBER from GREEN: civil handover forecast 12 days late").
- Do not use "GREEN" to mean "nothing happened". If no progress is evidenced, say so.

## The template

```
PROJECT STATUS: <project / estate / stage> | period ending <date> | prepared from <minutes date, schedule export date, RAID date>

OVERALL: <GREEN|AMBER|RED> - <one line: the single fact that drives the colour>
SCHEDULE: <G|A|R>   COST: <G|A|R|not assessed>   SCOPE: <G|A|R>   RISK: <G|A|R>

PROGRESS THIS PERIOD
- <completed item with evidence: "Stage 2 haul complete, 1,840 m, as per contractor report 2 Oct">
- <completed item>
- <completed item>

MILESTONES
Milestone                 | Baseline    | Forecast    | Status      | Comment
Civil handover Stage 3    | 14 Nov 2026 | 26 Nov 2026 | Slipping    | Developer contractor not yet appointed
Haul complete Stage 2     | 2 Oct 2026  | 2 Oct 2026  | Achieved    |
RFS Stage 2               | 18 Dec 2026 | 18 Dec 2026 | On track    | Testing booked wk of 7 Dec

BLOCKERS
<blocker> | impact: <milestone, premises> | owner | since <date> | needed to clear: <specific thing>

ASKS (decisions or help needed from the reader)
1. <ask> | from <whom> | by <date> | if not: <consequence>

NEXT PERIOD
- <planned work with dates>

RISKS TO WATCH (top 3)
<risk> | L x I | mitigation | owner

MISSING INFORMATION
<what the report could not assess from the input>
```

## Audience variants

| Audience | Lead with | Include | Leave out |
|---|---|---|---|
| PMO (default) | OVERALL and MILESTONES | Full template | Day-to-day task detail |
| Steerco | ASKS and OVERALL | Milestones, blockers, top 3 risks | NEXT PERIOD detail, minor progress |
| Team | PROGRESS and NEXT PERIOD | Everything plus the actions table | Nothing; this is the working view |
| Developer (external) | Milestones and what we need from them | Milestones, dependencies on them, next steps | Internal blockers, cost, internal names and RAG |

For the developer variant apply the writing-helper "Developer / property client" tone: professional, outcome-focused, no internal process detail, no internal RAG colours.

## Progress bullets: what counts as evidence

| Acceptable | Not acceptable |
|---|---|
| "Splicing complete at FDH 02, 96 fibres, test results received 1 Oct" | "Good progress on splicing" |
| "Design rev C approved by developer 29 Sep" | "Design nearly there" |
| "14 of 22 pits inspected, 2 defects raised" | "Pit inspections under way" |

If the input only supports the right-hand column, write the bullet from the right-hand column and add the gap to MISSING INFORMATION ("quantities for splicing progress not stated").

## Common delivery blockers (recognise these in the input)

| Blocker as it appears | Usual impact |
|---|---|
| Civil handover not accepted, defects outstanding | Haul cannot start; RFS exposed |
| Comms room or FDH site not ready, no power | Active equipment cannot be commissioned |
| Design not approved by developer or internal design | Procurement and construction wait |
| Contractor capacity, crews reassigned | Haul and splice dates move |
| Lot access, locked sites, landscaping over pits | Drop installs and testing blocked |
| Title or stage registration delayed by the developer | Addresses not available; provisioning and RSP onboarding wait |
| RSP not onboarded for the estate | Residents cannot order even after RFS |

## CUSTOMISE

- Cost tolerance for AMBER: 5% (confirm).
- Report cadence: weekly, period ending Friday (confirm).
- Milestone names: align with the list in attention-triage-rules.md.
- Distribution: delivery manager, PMO, head of delivery (confirm). External developer version only after the delivery manager reviews it.
