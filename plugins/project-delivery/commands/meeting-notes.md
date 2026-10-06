---
description: Turn raw meeting notes into DECISIONS / ACTIONS / OPEN QUESTIONS / PARKING LOT that paste cleanly into the project channel
argument-hint: <paste raw notes> [meeting:<name> date:<date> attendees:<list>]
---

Run the project-copilot skill in **meeting-notes** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules. Remove phone numbers and personal remarks that are not needed by the wider readership of the notes.
2. Use `references/raid-method.md` (section "Finding actions in prose") to separate decisions (something was agreed), actions (owner + deliverable), open questions (asked, not answered) and parking lot (raised, deliberately deferred). Use writing-helper for tone: terse, factual, chronological inside each section.
3. Produce exactly this template:

```
MEETING NOTES: <meeting> | <date> | attendees: <list or "not stated">

PURPOSE
<one line>

DECISIONS
1. <decision> | by whom | rationale if stated

ACTIONS
# | Owner | Action | Due
1 | <name> | <verb + deliverable> | <date or "not stated">

OPEN QUESTIONS
1. <question> | who can answer | needed by

PARKING LOT
- <topic> | why deferred | revisit when

RISKS OR ISSUES RAISED (for the RAID log)
- <item> | type: Risk/Issue/Dependency | owner if named

NEXT MEETING
<date and purpose if stated>
```

4. Keep every item traceable: if the employee asks, show the source fragment. Do not add decisions that were only discussed; "we talked about X" is not a decision.
5. Offer (one line) to run raid mode on the RISKS OR ISSUES RAISED section.
6. If no input is given, ask for the raw notes and the meeting name and date.
