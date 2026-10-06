---
description: Compare the learner's answer to the supplied material - CORRECT / MISSING / INCORRECT / WHERE TO READ
argument-hint: <paste your answer> [to: the question or scenario] and drop or paste the approved material
---

Run the learning-coach skill in **review-answer** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules. Read dropped material with the document-reader skill and keep page and section references. If the question the learner answered is not stated, ask for it before reviewing.
2. Compare the answer against the material only, using the review method in `references/coaching-method.md`: list what the material says the answer should contain, then map each point of the learner's answer to it.
3. Output the ANSWER REVIEW template: QUESTION, CORRECT (points the learner got right, each with the section that confirms it), MISSING (points the material requires that the answer left out, with where to read), INCORRECT (points that contradict the material, quoting the material), WHERE TO READ (ordered list of sections or pages), ONE THING TO FIX FIRST, and TRY AGAIN (a reworded version of the question or a closely related one for a second attempt).
4. Do not write the model answer out in full unless the learner has attempted at least once and asks for it; coach towards it with the MISSING and WHERE TO READ sections.
5. If the material does not cover part of the learner's answer, mark it NOT COVERED BY THE SUPPLIED MATERIAL rather than judging it right or wrong from general knowledge.
