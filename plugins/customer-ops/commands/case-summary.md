---
description: Structured case summary from a complaint, call notes or email thread - issue, timeline, sentiment, done so far, missing information, recommended response, internal next step
argument-hint: <paste the complaint, call notes or thread; drop a screenshot or PDF if that is what you have>
---

Run the customer-case-assistant skill in **case-summary** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules. If a screenshot is provided, transcribe it first (screenshot-reader) into a READ FROM IMAGE block; if a PDF, apply document-reader.
2. Triage with `references/case-triage-checklist.md` (case type, service state, wholesale boundary, urgency signals). Read sentiment with `references/sentiment-and-tone-guide.md` and quote the words that justify the sentiment call.
3. Produce exactly this template:

```
CASE SUMMARY: <ref if given> | <case type> | <estate/area if stated>

CUSTOMER ISSUE
<one or two lines in the customer's terms>

TIMELINE (from the text)
<date/time> | <event> | source: <who said it>

CUSTOMER SENTIMENT
<calm | frustrated | angry | distressed | threatening escalation> - evidence: "<quoted words>"
Vulnerability or urgency signals: <medical, safety, working from home, none stated>

WHAT HAS BEEN DONE
- <action, by whom, when, outcome> (only what the text states)

MISSING INFORMATION
- <item from the triage checklist that is not in the text>

RECOMMENDED RESPONSE
<approach in two or three lines: tone, what we can say, what sits with the RSP, what to promise and not promise>

INTERNAL NEXT STEP
1. <owner> | <action> | <by when>

WHOLESALE BOUNDARY
<what in this case is the company's (access network, ONT, lead-in, appointment) and what is the RSP's (plan, billing, modem, PPP, credit)>
```

4. Timeline entries come only from the text. Never state a check was done unless the text says so. Mark inferred dates as "approx".
5. If the paste is too short to summarise, output the MISSING INFORMATION section only and ask for the thread or call notes.
