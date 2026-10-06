---
description: Produce review questions only for a contract, policy or procedure, grouped by topic, for the drafter, counterparty or legal
argument-hint: <paste the document text or drop the PDF/DOCX> [for:drafter|counterparty|legal]
---

Run the compliance-reviewer skill in **questions** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules. Read dropped files with the document-reader skill and keep clause and page references.
2. Walk the relevant checklist (`references/contract-review-checklist.md` or `references/policy-review-checklist.md`). For every item that is absent, unclear, internally inconsistent or unusually one-sided, write one specific, answerable question.
3. Output REVIEW QUESTIONS grouped by topic (Term and termination, Liability and indemnity, Service levels, Data and privacy, Assignment and change of control, Notices, Payment, Definitions, Operational, Other), each question numbered with its clause or page reference, and a final MOST IMPORTANT TO RESOLVE list of the three to five questions that most affect risk.
4. Match the audience from the `for:` token: drafter (why was this drafted this way), counterparty (neutral, commercial wording per writing-helper), legal (precise, references the clause and the concern). Default to legal.
5. Questions only: no review conclusions, no risk ratings, no recommendation to sign or not. Close with: "This is not legal advice. Outputs are for review by qualified staff."
