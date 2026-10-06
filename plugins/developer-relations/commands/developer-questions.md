---
description: Clear question list for the developer, grouped by topic (civil, staging, pit and pipe, comms room, power, easements, titles and dates), ready to paste into an email
argument-hint: <paste what you know about the development and what you still need> [format:email|list]
---

Run the developer-assistant skill in **developer-questions** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules.
2. Compare the input with `references/development-intake-checklist.md` to find the gaps. For each gap pick or adapt the question from `references/developer-question-bank.md`. Do not ask what the input already answers; cite it under ALREADY KNOWN so the developer is not asked twice.
3. Use writing-helper developer tone: professional, confident, no internal process detail. Explain in one clause why each question matters when it is not obvious.
4. Produce exactly this template:

```
QUESTIONS FOR <developer>: <development> | <date>

<one-line opener for the email if format:email>

CIVIL AND PIT AND PIPE
1. <question> (<why, one clause>)

STAGING AND PROGRAMME
...

COMMS ROOM, FDH SITE AND POWER
...

EASEMENTS, TENURE AND ACCESS
...

TITLES, DATES AND SETTLEMENTS
...

DESIGN AND LOT INFORMATION
...

COMMERCIAL AND AGREEMENT (only if relevant)
...

<closing line with the date we need answers by, if the employee gave one>

---
ALREADY KNOWN (not asked)
<field> | <value> | source

PRIORITY (if they only answer three)
1. <question number> | why
```

5. Keep each question answerable in one line or with one document. Split compound questions.
6. If no input is given, output the full question bank grouped by topic and say it is the generic set.
