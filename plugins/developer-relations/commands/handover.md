---
description: Internal handover pack from BD or developer relations to the delivery team, with every item marked present or missing
argument-hint: <paste the account notes, agreement status, requirements and open items; name plans, lot schedules or agreements if you have them>
---

Run the developer-assistant skill in **handover** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules. Apply document-reader to named PDFs and spreadsheet-reader to named lot schedules; cite pages and rows.
2. Fill `references/handover-to-delivery-template.md` section by section. For every checklist item write present (with source), partial, or MISSING. Do not fill a gap with an assumption.
3. Produce the pack in this structure:

```
HANDOVER TO DELIVERY: <development> | <developer> | handed over by <name/role> | <date>

1. PROJECT SNAPSHOT            (what, where, how big, status of agreement)
2. KEY CONTACTS                (developer side roles; internal roles) - names only as the employee provided them
3. COMMERCIAL AND AGREEMENT    (status, key obligations and dates, anything unusual) - figures only if in the input
4. PREMISES AND STAGING        (table per stage)
5. DATES AND COMMITMENTS       (what we promised the developer, what they promised us, with sources)
6. CIVIL STATUS                (pit and pipe, specification, acceptance, as-builts, defects)
7. SITING AND POWER            (FDH / comms room, power, tenure)
8. DESIGN INPUTS RECEIVED      (drawings, lot layouts, revisions)
9. OPEN ITEMS AND RISKS        (table with owner and due)
10. HISTORY AND SENSITIVITIES  (what has gone wrong, what the developer cares about, what not to re-ask)
11. DOCUMENTS ATTACHED         (list; present / MISSING)

HANDOVER CHECKLIST
Item | Present / Partial / MISSING | Source or what is needed

READINESS
<ready for delivery kickoff | ready with gaps listed | not ready> - <why>

MISSING INFORMATION
<items delivery will need before design kickoff>
```

4. Section 10 is written from the notes only; no speculation about the developer's motives beyond what the employee wrote.
5. If no input is given, output the checklist with everything marked MISSING and ask for the account notes and agreement status.
