---
description: Turn interview notes into a structured summary by competency with quoted evidence - no hire or no-hire verdict
argument-hint: <paste interview notes; name the role and the competencies if known>
---

Run the people-assistant skill in **interview-summary** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules. Refer to the candidate by initials or "the candidate". Remove any note that references a protected attribute and do not carry it into the summary.
2. Use the summary method in `references/structured-interview-method.md`: map every note to a competency, quote the evidence as the interviewer wrote it, and separate OBSERVED from INTERPRETED.
3. Output the INTERVIEW SUMMARY template: ROLE AND STAGE, COMPETENCIES, then per competency: EVIDENCE (quoted), STRENGTH SHOWN, GAP OR UNCLEAR, FOLLOW-UP QUESTION; then NOT ASSESSED, INTERVIEWER CONSISTENCY NOTES (where interviewers disagree) and NEXT STEP FOR THE PANEL.
4. Do not produce a score, a ranking against other candidates, or an overall hire or no-hire recommendation, even if asked. State once: "Rating and decision are for the panel."
5. If the notes are too thin to summarise a competency, write `NOT ENOUGH EVIDENCE` under that competency rather than filling the gap.
