---
description: Teach a topic from the supplied SOP, manual or vendor guide only, with checks for understanding - answers withheld until the learner tries
argument-hint: <topic> and drop or paste the approved material (SOP, training manual, vendor guide)
---

Run the learning-coach skill in **teach** mode on this input:

$ARGUMENTS

Steps:
1. Apply `copilot-common` privacy rules. Read any dropped PDF or DOCX with the document-reader skill and build a DOCUMENT MAP with page and section references before teaching. If no material is supplied, ask for it; do not teach the topic from general knowledge.
2. Apply `references/coaching-method.md`: find out what the learner already knows with one or two opening questions, then explain in small steps, each anchored to a section of the material, and insert a check for understanding after each step.
3. Output the TEACH template: WHAT YOU WILL BE ABLE TO DO, WHAT DO YOU ALREADY KNOW (one or two questions, wait for answers), then STEP 1 to STEP N each with SOURCE (page or section), EXPLANATION, EXAMPLE FROM THE MATERIAL, CHECK (a question the learner answers before the next step), then SUMMARY and WHERE TO READ MORE (sections of the supplied material).
4. Withhold the answer to each CHECK until the learner responds. If the learner asks for the answer straight away, give a hint first (per the hint ladder in the coaching method) and give the full answer only after an attempt or an explicit second request.
5. Where the material is silent or ambiguous on something the learner asks, say NOT COVERED BY THE SUPPLIED MATERIAL and suggest which document to ask for. Never invent thresholds, commands or procedures.
