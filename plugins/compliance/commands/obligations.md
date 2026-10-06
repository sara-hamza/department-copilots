---
description: Build an obligations register table from a contract, policy or procedure - Clause, Obligation, Owner, Due/Trigger, Evidence
argument-hint: <paste the document text or drop the PDF/DOCX; optionally say which party is the company>
---

Run the compliance-reviewer skill in **obligations** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules. Read dropped files with the document-reader skill and keep clause and page references.
2. Use `references/obligations-register-template.md`: extract every "shall", "must", "will", "is responsible for", "agrees to" and "may not" statement, classify it (one-off, recurring, triggered, ongoing), and identify which party it binds.
3. Output the OBLIGATIONS REGISTER table: Ref | Clause | Obligation (short, active voice) | Binds (company / counterparty / both) | Owner (role, `TBC` if unknown) | Due or Trigger | Evidence of compliance | Status. Then OBLIGATIONS ON THE COUNTERPARTY as a shorter table, and NOTES (obligations that depend on undefined terms or missing schedules).
4. Owners are roles, not names. Do not assign an owner the document does not support; write `owner: TBC` and list it under NOTES for the compliance lead to allocate.
5. Close with: "This is not legal advice. Outputs are for review by qualified staff."
