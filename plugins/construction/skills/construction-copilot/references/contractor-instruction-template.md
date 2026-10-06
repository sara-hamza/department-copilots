# Contractor instruction and progress summary templates

Both follow the copilot-common writing-helper: direct, numbered, dated, with acceptance criteria. No vague "please action ASAP". No internal opinions in anything sent.

## Instruction to contractor

```
INSTRUCTION TO CONTRACTOR
TO: <contractor, site contact>   FROM: <our role>   DATE: <date>
PROJECT: <estate, stage>   REF: <instruction number / contract clause if used>

CONTEXT
<one line: what was found, where, when, by whom>

ACTIONS
1. <location id> - <outcome required> - due <date> (default: <severity timeframe>)
2. ...

EVIDENCE REQUIRED
- <per action: time-stamped photo before and after; OTDR file by fibre id; mandrel record; corrected as-built sheet>

ACCEPTANCE CRITERIA
- <per action: the QA checklist item it must meet, in one line, e.g. "splice loss average 0.1 dB, max 0.3 dB, bidirectional">

SAFETY
<if any P1 item: make-safe instruction and the time it is required by>

CONTACT
<name, role, phone or email for the contractor to confirm completion>
```

Rules:
- One action per line: one location, one outcome, one due date.
- Order: P1 safety first, then items blocking the next milestone, then the rest.
- Default timeframes from `defect-priority-matrix.md` are marked "(default)" so the manager can replace them with contract terms.
- No commercial statements (back-charges, liquidated damages, variation acceptance) unless the employee supplies the wording; put a placeholder `[commercial wording from contract manager]`.
- Keep the contractor's workers' names out. Address the contractor company and site contact only.

After the instruction, append two blocks that are not sent:

```
INTERNAL NOTES (not to send)
<opinions, history, commercial notes, other contractors, what to watch>

MISSING BEFORE SENDING
<contract reference, confirmed due dates, contact name, photo numbers, anything marked default>
```

## Worked example

```
INSTRUCTION TO CONTRACTOR
TO: Northline Civil, J. Park (site supervisor)   FROM: Construction Manager   DATE: 6 Oct 2026
PROJECT: Riverlea Stage 3   REF: CI-031

CONTEXT
QA inspection on 5 Oct 2026 of Pits P3-040 to P3-058 (Bower Street) found the items below.

ACTIONS
1. P3-044 - open pit with no cover on the footpath. Make safe immediately; fit the correct class lid - due 6 Oct 2026 by 12:00 (P1).
2. P3-047 to P3-049 - P100 feeder conduit failed mandrel between P3-047 and P3-048. Replace the damaged section and re-prove - due 13 Oct 2026 (default 5 working days).
3. P3-052 - pit interior holds water over the distribution cable coil. Clean, identify the ingress point and seal - due 20 Oct 2026 (default 10 working days).
4. Bower Street, lots 40 to 58 - lead-in conduits have no end seals at the boundary points. Fit seals - due 20 Oct 2026 (default).
5. Bower Street - marker tape not observed in the open section at P3-050 during backfill. Confirm tape installed with photos; expose and install where absent - due 13 Oct 2026.

EVIDENCE REQUIRED
- Actions 1, 3, 4: time-stamped photos before and after, pit id visible.
- Action 2: mandrel proving record for P3-047 to P3-048 after replacement.
- Action 5: photos of tape in trench at three points between P3-049 and P3-051.

ACCEPTANCE CRITERIA
- Action 1: lid class suits footpath, fitted level (QA checklist 1, Lid).
- Action 2: mandrel passes full length; draw rope installed (QA checklist 2, Continuity and proving).
- Action 3: pit dry at re-inspection; cables coiled on brackets (QA checklist 1, Interior).
- Action 4: every lead-in end sealed; location recorded on the lot schedule (QA checklist 2, Lead-ins).
- Action 5: marker tape continuous above conduit (QA checklist 2, Marker tape).

SAFETY
Action 1 is a P1 safety item. Barrier or cover the pit now and confirm by phone when done.

CONTACT
<name>, Construction Manager, <phone>. Reply with evidence to this instruction reference.
```

```
INTERNAL NOTES (not to send)
Third open-pit finding on this crew this month; raise at the weekly meeting. Water in P3-052 may be the stormwater connection the developer changed; check with developer before accepting a claim.

MISSING BEFORE SENDING
Contract clause reference for CI numbering; confirm whether the P1 lid timeframe in the contract is 2 h or 4 h; contact phone number.
```

## Progress summary

```
PROGRESS SUMMARY
PERIOD: <from> to <to>   PROJECT: <estate, stage>   PREPARED FROM: <sources with dates>

COMPLETED
- <activity> - <qty unit> - <section or street> - <source>

IN PROGRESS
- <activity> - <qty or % if given> - <expected finish if given> - <source>

BLOCKED
- <activity> - <blocker> - <owner> - <since> - <source>

NEXT WEEK
- <activity> - <who> - <precondition>

RISKS
- <risk> - <likely | possible> - <milestone affected> - <mitigation if stated>

NOT STATED IN INPUT
- <what the reader will ask for that the input did not give>
```

Rules:
- One page. Bullets, not paragraphs.
- Quantities exactly as given with units; do not total unless components are itemised in the input.
- If the input gives cumulative figures (premises passed to date), show them with "to date" and the date.
- RISKS come from BLOCKED items plus the triggers in `defect-priority-matrix.md`.
- Mark inferences "(inferred)". Never invent a programme date or variance.

## CUSTOMISE: company instruction and reporting conventions

- Instruction numbering and the contract clause it is issued under: `<fill in>`
- Who signs instructions (role): `<fill in>`
- Standard progress reporting day and recipients (roles only): `<fill in>`
- Quantities tracked each week (for example premises passed, pits installed, m conduit, m cable, splices, tests complete): `<fill in>`
