---
description: Only the checklist of what is still needed to progress the case - dates, service state, prior attempts, RSP, address confirmed
argument-hint: <paste the case text or notes>
---

Run the customer-case-assistant skill in **missing-info** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules.
2. Walk the "Information needed to progress" table in `references/case-triage-checklist.md` for the case type you identify. Mark each item present (quote it briefly) or missing.
3. Produce exactly this template and nothing else:

```
MISSING INFORMATION: <case ref or short label> | case type: <type>

HAVE
- <item>: <value or brief quote>

NEED
1. <item> | why it matters | who can supply it (customer / RSP / NOC / field)
2. ...

ASK THE CUSTOMER (ready to paste)
<two to four plain-English questions in customer tone, no acronyms>

ASK THE RSP (if applicable)
<numbered, specific, evidence-led questions>
```

4. Order NEED by what unblocks the case fastest (address and service identifier first, then service state, then dates, then prior attempts, then RSP details).
5. Do not list items that are irrelevant to the case type (no appointment questions for a billing dispute that belongs to the RSP).
6. If no input is given, output the generic checklist for a service fault case and say that is what it is.
