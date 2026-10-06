---
description: Extract an ACTIONS table (who / what / when / source line) from meeting minutes or notes
argument-hint: <paste minutes or notes> [meeting:<name> date:<date>]
---

Run the project-copilot skill in **actions** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules. If a PDF or DOCX of minutes is named, apply document-reader and keep page references.
2. Use the action-recognition rules in `references/raid-method.md` (section "Finding actions in prose"): an action has a verb, an owner and a deliverable. "We should look at X" with no owner is an OPEN QUESTION, not an action, unless the chair assigned it.
3. Produce exactly this template:

```
ACTIONS from <meeting> (<date>)

# | Owner | Action | Due | Status | Source line
1 | <name or role> | <verb + deliverable> | <date or "not stated"> | Open | "<quoted fragment>"
2 | ...

UNOWNED (need an owner before they are real actions)
- <action> | source line

DECISIONS NOTED IN PASSING
- <decision> | source line

MISSING INFORMATION
<owners or dates the minutes did not state>
```

4. Quote the source fragment for every row so the employee can verify it. Never assign an owner the minutes did not name; use the role if the minutes used a role.
5. Dates: convert relative dates ("by Friday", "next sprint") to a calendar date only if the meeting date is known; otherwise keep the relative wording and flag it.
6. If no input is given, ask for the minutes and offer to also run meeting-notes mode on the same paste.
