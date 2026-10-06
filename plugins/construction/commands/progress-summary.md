---
description: Write a PROGRESS SUMMARY for the period - completed, in progress, blocked, next week, risks - from contractor updates and site reports
argument-hint: <paste the period's updates, site reports and counts; state the period if not obvious>
---

Run the construction-copilot skill in **progress-summary** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules. Identify the period from the input or ask; never assume the current week.
2. Sort every item in the input into COMPLETED, IN PROGRESS, BLOCKED, NEXT WEEK. Quantities (pits, metres of conduit, metres of cable, splices, premises passed) are copied with their units and source line; do not total figures unless the input gives the components.
3. Use the PROGRESS SUMMARY template in `references/contractor-instruction-template.md` (section "Progress summary"). RISKS come from BLOCKED items and from `references/defect-priority-matrix.md` triggers (weather, access, permits, materials, resources).
4. Output:
```
PROGRESS SUMMARY
PERIOD: <from> to <to>   PROJECT: <name/stage>   PREPARED FROM: <site reports, contractor update of <date>>

COMPLETED
- <item> (<qty unit>) - <source>

IN PROGRESS
- <item> - <% or qty if given> - <expected finish if given>

BLOCKED
- <item> - <blocker> - <owner> - <since>

NEXT WEEK
- <item> - <who>

RISKS
- <risk> - <likelihood: likely | possible> - <impact on milestone> - <mitigation if stated>

NOT STATED IN INPUT
<what a reader will ask for that the input did not give: premises passed to date, programme variance, safety incidents>
```
5. Keep it to one page. Short lines, no narrative. Facts only from the input; mark any inference "(inferred)".
6. Input missing: if no updates were given, output the empty template with the period line and a request for the site reports.
