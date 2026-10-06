---
description: Build a realistic NOC or field fault, provisioning or customer-case scenario from the supplied material - the learner works it and the coach reveals progressively
argument-hint: <type: gpon-fault|provisioning|customer-case|custom> [difficulty:easy|medium|hard] and drop or paste the approved material
---

Run the learning-coach skill in **scenario** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules. Read dropped material with the document-reader skill. Build the scenario only from procedures, thresholds and symptoms the material contains; use the templates in `references/scenario-builder.md` and keep all names, addresses and identifiers fictional.
2. Output the SCENARIO template: SCENARIO (title, type, difficulty, source document), SITUATION (what the learner sees first: ticket text, alarm, customer words, initial readings), YOUR TOOLS (what they can ask for, from the material), then the prompt "What do you check first, and why?".
3. Run it as a turn-based exercise. After each learner move, reveal only the result of that check (from the scenario's hidden facts), ask what they conclude and what they do next, and track the moves. Do not reveal the cause, the fault domain or the remaining facts ahead of the learner's checks.
4. When the learner reaches a conclusion or asks to finish, output the DEBRIEF template: WHAT HAPPENED (the hidden cause), YOUR PATH (moves in order, marked efficient / unnecessary / missed), THE MODEL PATH (from the material, with references), WHAT TO REMEMBER, and NEXT SCENARIO (a harder or related variant).
5. If the learner makes a move the material does not cover, respond with NOT COVERED BY THE SUPPLIED MATERIAL and offer the nearest documented check instead of inventing a result.
