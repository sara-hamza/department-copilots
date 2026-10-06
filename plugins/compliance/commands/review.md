---
description: Full compliance review of a contract, policy or procedure - obligations, risks, dates, responsibilities, ambiguities, missing information, questions for legal, each with a clause or page reference
argument-hint: <paste the document text or drop the PDF/DOCX; say whether it is a contract, policy or procedure if not obvious>
---

Run the compliance-reviewer skill in **review** mode on this input:

$ARGUMENTS

Steps:
1. Apply `copilot-common` privacy rules. If a PDF or DOCX is provided, read it with the document-reader skill and build a DOCUMENT MAP (headings, clause numbers, pages, schedules) before reviewing.
2. Identify the document type. For contracts use `references/contract-review-checklist.md`; for policies and procedures use `references/policy-review-checklist.md`. Walk every item in the checklist and record present, absent or unclear.
3. Output the full COMPLIANCE REVIEW template: DOCUMENT, OBLIGATIONS, RISKS (High/Med/Low with why), DATES, RESPONSIBILITIES, AMBIGUITIES, MISSING INFORMATION, QUESTIONS FOR LEGAL. Every item cites a clause, section or page (`cl. 12.3`, `p.7`, `Sched. 2`).
4. Open and close with: "This is not legal advice. Outputs are for review by qualified staff."
5. If a referenced schedule, annexure, defined-terms section or standard is not supplied, list it under MISSING INFORMATION and do not infer its contents. If the document is a partial extract, say so in the DOCUMENT line.
