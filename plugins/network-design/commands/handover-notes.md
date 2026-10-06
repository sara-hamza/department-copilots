---
description: Check a design handover pack against the handover checklist - present, missing, and what to chase
argument-hint: <drop or list the pack contents: drawings, as-builts, test results, splice plans, BOM, notes>
---

Run the design-reviewer skill in **handover-notes** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules. Build an inventory of what was supplied (file names, sheet titles, revision numbers, dates) before judging it.
2. Walk `references/handover-pack-checklist.md` item by item. Mark each PRESENT (cite the file or sheet), MISSING, or PARTIAL (say what is incomplete).
3. Output the HANDOVER PACK template: PACK SUMMARY (project, stage, revision, date), CHECKLIST (table: Item | Status | Where | Note), MISSING OR PARTIAL (numbered, with who usually supplies it), REVISION AND CONSISTENCY ISSUES (drawings referencing superseded revisions, dates out of order), READY FOR HANDOVER (Yes / No, with the single blocking item if No).
4. Do not mark an item PRESENT because its name appears in a transmittal; the content must be in the pack.
5. Input missing: if nothing was supplied, output the full checklist with every item MISSING and say that this is the target list, not a review.
