---
description: Draft a numbered instruction to the contractor with due dates, evidence required and acceptance criteria, per the writing-helper template
argument-hint: <paste the defects, blockers or scope, and the contractor and site names>
---

Run the construction-copilot skill in **contractor-instruction** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules. Remove internal-only remarks (opinions about the contractor, commercial notes, other contractors' names) from the instruction; keep them under INTERNAL NOTES after the draft.
2. Use the Instruction to contractor template in `references/contractor-instruction-template.md`, which follows the copilot-common writing-helper structure: context (one line), numbered actions with due dates, evidence required, acceptance criteria, contact.
3. Each action is one outcome, at one location, with one due date and one evidence item. Split compound requests. Order safety items first.
4. Use the default rectification timeframes from `references/defect-priority-matrix.md` where the employee gave none, and mark them "(default)". Acceptance criteria reference `references/construction-qa-checklist.md` items by name.
5. Output: INSTRUCTION TO CONTRACTOR (ready to paste) then INTERNAL NOTES (not to send) then MISSING BEFORE SENDING (contract reference, site id, due dates not confirmed, contact name).
6. Input missing: if there is nothing to instruct, say so and ask for the defect, blocker or scope item.
