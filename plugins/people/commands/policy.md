---
description: Explain a policy in plain English, with the caveat that the policy document governs
argument-hint: <paste the policy text or drop the PDF; optionally the question the employee asked>
---

Run the people-assistant skill in **policy** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules. If a PDF or DOCX is provided, read it with the document-reader skill and keep section and page references.
2. Output the POLICY IN PLAIN ENGLISH template: WHAT THIS POLICY COVERS, WHO IT APPLIES TO, THE KEY RULES (numbered, each with a section reference), WHAT YOU NEED TO DO, WHAT HAPPENS IF (consequences and process, as the policy states them), WHO TO ASK, and ANSWER TO YOUR QUESTION if the employee asked one.
3. Start and end with the line: "This is a summary. The policy document governs; check it or ask People for anything that matters."
4. Explain only what the policy says. Where the policy is silent or ambiguous on the employee's question, say so under NOT COVERED BY THE POLICY and name who can answer (People team contact per `references/onboarding-plan-template.md` CUSTOMISE section, or the policy owner named in the document).
5. If no policy text is supplied, do not explain from memory. Ask the employee to paste the current version or drop the file.
