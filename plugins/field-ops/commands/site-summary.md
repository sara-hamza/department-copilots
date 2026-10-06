---
description: Turn rough site notes into a SITE VISIT SUMMARY - Issue, Testing, Findings, Remediation, Further action - without inventing tests
argument-hint: <paste rough notes, times, readings and what you did>
---

Run the field-assistant skill in **site-summary** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules. Keep customer name, phone and full address out of the summary unless the technician clearly wants them in; a lot number or service reference is enough.
2. Use the SITE VISIT SUMMARY template in `references/site-closeout-template.md`: ISSUE, TESTING, FINDINGS, REMEDIATION, FURTHER ACTION, plus TIME ON SITE and MATERIALS USED when given.
3. Keep only tests, readings and actions the technician wrote down. Do not add tests they did not mention. If an expected test is absent, append one line after the summary: `SUGGESTED (not done): ...`.
4. Readings with units and the point measured. Times with zone (ask only if ambiguous; default ACDT/ACST for Adelaide).
5. FURTHER ACTION names an owner (Field, NOC, Construction, RSP, Customer) and a trigger or date; write `owner: TBC` rather than guessing.
6. Input missing: if the notes contain no readings or actions, produce the ISSUE line only and list under MISSING INFORMATION what to add before closing the ticket.
