---
description: Quiz the learner from the supplied material - N questions, answers withheld until the learner answers, then feedback with where to read
argument-hint: <topic> [n:5] [format:mcq|short|scenario|mixed] and drop or paste the approved material
---

Run the learning-coach skill in **quiz** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules. Read dropped material with the document-reader skill and keep page and section references. If no material is supplied, ask for it; do not quiz from general knowledge.
2. Use `references/quiz-formats.md` to choose the format (default: mixed, five questions, difficulty rising) and write questions that each test one idea from the material and record the source section for the feedback.
3. Output the QUIZ template: QUIZ (topic, N questions, format, source document), then Q1 to QN with no answers shown, then the line "Answer in any order; say 'reveal' for a hint, 'reveal all' for the answers after you have attempted them."
4. Do not print answers, an answer key or explanations until the learner has attempted the questions. When they answer, respond with the FEEDBACK template per question: YOUR ANSWER, VERDICT (correct / partly / incorrect), WHY, WHERE TO READ (section or page), then SCORE and REVISE NEXT (the ideas to revisit, with spaced-repetition timing from `references/coaching-method.md`).
5. If the learner asks for the answers before attempting, give a hint ladder step instead; reveal in full only after an attempt or an explicit second request, and say so.
