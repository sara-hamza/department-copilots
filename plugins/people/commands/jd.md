---
description: Improve a job description - structure, inclusive language, clear requirements vs nice-to-haves
argument-hint: <paste the JD or rough role notes; optionally say the level and team>
---

Run the people-assistant skill in **jd** mode on this input:

$ARGUMENTS

Steps:
1. Apply `copilot-common` privacy rules. Strip any personal data about current or former incumbents from the output.
2. Read `references/jd-structure-and-language.md` and apply the section order, the inclusive-language table and the requirements test (would a strong candidate be excluded by this line?).
3. Output the IMPROVED JOB DESCRIPTION template: ROLE SUMMARY, WHAT YOU WILL DO, WHAT YOU NEED (essential), NICE TO HAVE, HOW WE WORK, ABOUT THE TEAM, then CHANGES MADE (numbered, each with the reason) and QUESTIONS FOR THE HIRING MANAGER.
4. Do not invent salary, reporting line, location or hours. If they are missing, leave a `[CONFIRM: ...]` placeholder and list it under QUESTIONS FOR THE HIRING MANAGER.
5. If the input is only a title with no content, produce a skeleton with placeholders and ask the five intake questions from the reference instead of guessing the role.
