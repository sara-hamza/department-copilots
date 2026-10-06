---
description: Project requirements summary for a development - premises, staging, dates, constraints, open items, questions for the developer, risks
argument-hint: <paste development plan details, project notes, developer emails; name a plan PDF or lot schedule if you have one>
---

Run the developer-assistant skill in **requirements** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules. If a development plan or drawing PDF is named, apply document-reader and cite pages. If a lot schedule or stage programme spreadsheet is named, apply spreadsheet-reader and state which columns were used for lot, stage, dwelling type and dates.
2. Walk `references/development-intake-checklist.md` field by field. Mark each as known (with source), partly known, or missing. Missing fields become QUESTIONS FOR DEVELOPER using the wording in `references/developer-question-bank.md`.
3. Produce exactly this template:

```
PROJECT REQUIREMENTS: <development> | <developer> | <location> | as of <date>

PREMISES
<total lots/dwellings, by type and stage, with source>

STAGING
Stage | Lots | Civil start | Civil handover | Title registration | First settlement | Source

DATES THAT DRIVE US
<the earliest settlement per stage and the implied latest civil handover (CUSTOMISE lead times), labelled "derived">

CONSTRAINTS
- <design, civil, siting, access, planning or commercial constraint> | source

OPEN ITEMS
# | Item | Owner (ours / developer) | Needed by | Status
(comms room, power, civil handover date, easements, specification acceptance, as-builts ...)

QUESTIONS FOR DEVELOPER
<grouped by topic, numbered, from the question bank>

RISKS
<risk: cause -> event -> impact> | likelihood | what we do

MISSING INFORMATION
<intake fields with no source in the input>
```

4. Derived dates are labelled "derived" and show the lead time used. Never present a derived date as the developer's date.
5. If no input is given, output the intake checklist as a blank form and ask for the development plan and the developer's latest programme.
