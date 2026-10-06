---
description: Prioritise a defect list or site photos into a DEFECT REGISTER review with severity, standard breached, rectification and evidence needed
argument-hint: <paste the defect list or QA report, or drop photos with locations>
---

Run the construction-copilot skill in **defects** mode on:

$ARGUMENTS

Steps:
1. Apply `copilot-common` privacy rules. If photos were supplied, describe each with screenshot-reader site-photo rules first and use "appears" wording for anything judged from an image.
2. Classify every defect with `references/defect-priority-matrix.md`: safety first, then service-affecting, then compliance, then cosmetic; civil and fibre defects use their own rows. Use `references/construction-qa-checklist.md` to name the requirement breached where the defect maps to a checklist item.
3. Output the DEFECT REGISTER review: a prioritised table with columns Severity | Location | Defect | Standard breached (if known) | Required rectification | Evidence needed, sorted P1 first, then a SUMMARY line (count per severity), then DUPLICATES OR MERGED (defects that are the same item), then QUESTIONS (defects that cannot be classified without more information).
4. Standard breached: name the clause or checklist item only if it is known from the input or the QA checklist; otherwise write "to confirm" rather than inventing a clause number.
5. Required rectification states the outcome and the default timeframe for that severity; it does not instruct the contractor directly (use contractor-instruction for that).
6. Input missing: if no defects were supplied, say so and list what a usable defect entry needs (location id, description, photo, who found it, date).
