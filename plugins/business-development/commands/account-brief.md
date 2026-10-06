---
description: Account brief for a developer or estate opportunity - opportunity, likely priorities, potential objections, questions to ask, proposal differentiators, follow-up actions
argument-hint: <paste developer notes, estate details, prior correspondence; name a development plan PDF if you have one>
---

Run the bd-copilot skill in **account-brief** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules. If a development plan or proposal PDF is named, apply document-reader and keep page references. If a lot schedule spreadsheet is named, apply spreadsheet-reader.
2. Qualify the opportunity with `references/developer-opportunity-qualification.md` (lot count, staging, timing, competing networks, power and comms room, contract status). Anticipate objections with `references/objection-handling.md`.
3. Produce exactly this template:

```
ACCOUNT BRIEF: <developer> | <estate / project> | <location> | prepared <date>

OPPORTUNITY
<what it is: lots, dwelling types, stages, timing, status of any agreement; each fact with its source>
Qualification: <strong | moderate | weak | insufficient information> - <why, citing the qualification table>

LIKELY PRIORITIES (for this developer)
1. <priority> | evidence from input or "inferred from developer type"

POTENTIAL OBJECTIONS
<objection> | likelihood | our response outline (from objection-handling.md) | evidence we would need

QUESTIONS TO ASK
1. <question> | why it matters | which qualification gap it closes

PROPOSAL DIFFERENTIATORS
- <differentiator relevant to this developer> | why it matters to them

FOLLOW-UP ACTIONS
# | Owner | Action | By when

MISSING INFORMATION
<qualification fields not in the input>
```

4. Mark every inference as "inferred"; mark facts with their source. Do not invent lot counts, dates, competitor names or commercial terms.
5. If no input is given, ask for the developer name, estate, lot count, stage timing and any correspondence, and show the qualification checklist so the employee knows what to gather.
