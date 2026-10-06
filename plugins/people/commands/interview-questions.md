---
description: Build a structured, competency-based interview question set for a role with what good answers cover
argument-hint: <role title or paste the JD> [stage:screen|panel|technical] [competencies:...]
---

Run the people-assistant skill in **interview-questions** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules. Do not use any candidate detail in the question set; the same questions go to every candidate.
2. Use `references/structured-interview-method.md`: pick five to seven competencies from the JD or the role family table, then write questions in the past-behaviour or situational form with the probe follow-ups and the WHAT A GOOD ANSWER COVERS notes.
3. Output the INTERVIEW QUESTION SET template: ROLE, STAGE, COMPETENCIES ASSESSED, then per competency: QUESTION, PROBES, WHAT A GOOD ANSWER COVERS, RATING ANCHORS (1 to 4), then LOGISTICS (time per question, who asks what) and QUESTIONS TO AVOID (protected attributes, with the lawful alternative).
4. If no role or JD is given, ask for the role title, level and the three outcomes the role must deliver in year one before writing questions.
5. Never include questions that touch age, family plans, health, religion, nationality or other protected attributes, and say so if the hiring manager's input asked for them.
