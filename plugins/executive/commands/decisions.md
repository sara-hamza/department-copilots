---
description: Decisions required from the sources, each framed with options, recommendation basis, deadline and owner
argument-hint: <drop or paste the reports, papers and notes; say the decision-maker and the meeting date if there is one>
---

Run the executive-briefing skill in **decisions** mode on:

$ARGUMENTS

Steps:
1. Read every source (document-reader for PDFs and DOCX with page references; spreadsheet-reader for CSV/XLSX, running its profile_sheet.py profiler first; pasted notes as supplied). Build the numbered SOURCES list.
2. Extract every explicit ask ("seeks approval", "decision required", "recommend that") and every implicit one (a blocked item waiting on a choice, a deadline that forces a choice, two documents proposing different courses). Mark implicit ones as "implied by".
3. Follow `references/decision-framing-method.md`: for each decision state the question in one sentence, the options actually available (including "do nothing" where real), the trade-offs the sources describe, reversibility, what the sources recommend and on what basis, the deadline and what happens if it passes, and the owner.
4. Produce the DECISIONS REQUIRED template from SKILL.md, ordered by deadline then impact. Every field cites its source per `references/source-tracing-rules.md`; fields the sources do not support are written "not stated in sources".
5. Recommendation basis is the source's recommendation and its stated reasoning, not the briefing's own view. If no source recommends, write "no recommendation in sources" and list what would be needed to form one.
6. The decision belongs to the executive. Never write "approved" or "decided"; write "decision required by".
