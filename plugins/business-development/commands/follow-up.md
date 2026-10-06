---
description: Follow-up email to the developer plus an internal action plan after a meeting
argument-hint: <paste the meeting notes, who attended, what was agreed and what was asked> [tone:standard|warm|formal]
---

Run the bd-copilot skill in **follow-up** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules. Strip internal remarks, internal names the developer does not know, and any commercial figures that were not stated in the meeting from the external email.
2. Use writing-helper developer tone and the follow-up structure in `references/proposal-structure.md` (section "Follow-up email"). Use `references/developer-opportunity-qualification.md` to spot gaps the meeting left open and turn them into internal actions or polite questions.
3. Produce exactly this template:

```
FOLLOW-UP EMAIL (to <developer contact>, tone: <tone>)
Subject: <estate / project> - follow-up from <date> meeting

<thanks and one-line summary of the purpose>

What we discussed
- <point agreed or discussed, as stated in the notes>

What we will do
- <our action> | by <date, only if stated or agreed>

What we need from you
- <their action or information> | by <date if agreed>

Next step
<the specific next meeting, document or decision, with a proposed date>

<sign-off>

---
INTERNAL ACTION PLAN (do not send)
# | Owner | Action | Due | Depends on
1 | ...

OPEN QUALIFICATION GAPS
<field from the qualification checklist> | how we will close it

RISKS NOTED IN THE MEETING
<risk> | likelihood | what we do about it

NOT SAID IN THE EMAIL AND WHY
<commercial figures, internal timing, competitor remarks, unconfirmed capabilities>
```

4. The email states only what the notes say was agreed. Do not add commitments, dates or figures that were not in the meeting. Where the notes are ambiguous about who agreed what, list it under the internal plan as "confirm with <attendee>".
5. If no input is given, ask for the meeting notes and the developer contact, and output the empty template.
