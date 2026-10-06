---
description: Meeting preparation pack - agenda, objectives, likely questions with our answers, and materials to bring
argument-hint: <paste account notes, meeting purpose, attendees and anything the developer has sent> [meeting:<type: intro|site|commercial|contract|review>]
---

Run the bd-copilot skill in **meeting-prep** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules.
2. Determine the meeting type from a `meeting:` token or from context (intro, site visit, commercial, contract, project review). Use `references/developer-opportunity-qualification.md` to find the gaps the meeting should close and `references/objection-handling.md` for likely questions and our answers. Use `references/proposal-structure.md` to decide which materials are relevant.
3. Produce exactly this template:

```
MEETING PREP: <developer> | <meeting type> | <date/time if known> | attendees: <ours / theirs>

OBJECTIVES (ours, in priority order)
1. <outcome we want from this meeting>

AGENDA (<n> minutes)
1. <item> | <minutes> | <who leads>

WHAT WE KNOW / WHAT WE NEED TO FIND OUT
Know: <facts with source>
Find out: <qualification gaps, phrased as the question to ask>

LIKELY QUESTIONS FROM THEM AND OUR ANSWERS
Q: <question>
A: <answer outline; "CONFIRM BEFORE MEETING" where a fact or figure is not in the input>

LIKELY OBJECTIONS
<objection> | response outline | proof we can bring

MATERIALS TO BRING
- <item> | why | ready: yes / needs preparing

CLOSE: what we ask for at the end
<the specific next step we want them to agree to>

MISSING INFORMATION
<things to confirm internally before the meeting>
```

4. Never put a price, timeframe or capability in an answer unless the input provides it; write `CONFIRM BEFORE MEETING`.
5. If no input is given, ask for the meeting purpose and whatever account notes exist, and produce a generic intro-meeting agenda marked as such.
