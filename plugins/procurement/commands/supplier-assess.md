---
description: Structured supplier assessment from supplied information - capability, risk, compliance documents present and missing
argument-hint: <paste or drop the supplier's capability statement, certificates, insurances, references, financial information, and the scope you need them for>
---

Run the procurement-assistant skill in **supplier-assess** mode on:

$ARGUMENTS

Steps:
1. Read what was supplied (document-reader for PDFs; keep page references). List every document received under DOCUMENTS RECEIVED with its date and expiry where shown.
2. Walk `references/supplier-assessment-checklist.md` section by section. For each item mark Present (with reference), Missing, or Expired/Out of date. Do not infer that a document exists because the supplier says it does.
3. Produce the SUPPLIER ASSESSMENT template from SKILL.md: SUPPLIER AND SCOPE, DOCUMENTS RECEIVED, CAPABILITY (against the scope), COMPLIANCE DOCUMENTS (table: Requirement, Status, Reference, Expiry), RISK OBSERVATIONS (each with the evidence and a likelihood word), MISSING BEFORE ONBOARDING, QUESTIONS FOR THE SUPPLIER.
4. Risks are observations for a human to weigh: "single director, two years trading, likely higher continuity risk for a multi-year supply". No scores unless the employee's own scoring sheet is supplied.
5. If the scope is not stated, ask for it in one line at the top and assess only the generic compliance items.
6. Never recommend approving or rejecting the supplier. State readiness: "all mandatory documents present" or "not ready: <n> mandatory items missing".
