---
description: Customer-friendly reply draft (acknowledge, what we found, what happens next and when, how to reach us) with INTERNAL NOTES kept separate
argument-hint: <paste the case, what was found and what happens next> [channel:email|sms|portal] [tone:standard|apology|firm]
---

Run the customer-case-assistant skill in **draft-reply** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules. Strip internal identifiers, internal names and internal remarks from the customer-facing text.
2. Follow the writing-helper customer reply structure: acknowledge -> what we found (plain English) -> what happens next and when -> how to reach us. One short paragraph each. Use `references/sentiment-and-tone-guide.md` for de-escalation phrases and the "do not promise" list, and `references/jargon-translation-table.md` to replace every technical term.
3. Channel from a `channel:` token (default email). SMS: under 300 characters, no greeting beyond the first name, one next step. Portal: same as email without the sign-off block.
4. Produce exactly this template:

```
CUSTOMER REPLY (<channel>, tone: <tone>)
Subject: <if email>

<acknowledge: what they told us, in their terms, and thanks for the detail>

<what we found: plain English, no acronyms, only facts the input supports>

<what happens next and when: only commitments the input supports; otherwise "we will update you by <date/time>" if the employee gave one, or "once <event>">

<how to reach us: CUSTOMISE contact line; and where the RSP is the right contact, say so warmly>

<sign-off>

---
INTERNAL NOTES (do not send)
FACTS USED: <list, each traceable to the input>
NOT SAID AND WHY: <things left out: unconfirmed cause, internal timing, RSP responsibility wording>
WHOLESALE WORDING CHECK: <confirms the reply does not imply a retail relationship or speak for the RSP>
BEFORE SENDING: <anything the employee must confirm: appointment slot, reference number, name spelling>
```

5. Never promise a fix date, a credit, a refund or a specific appointment unless the input states it was confirmed. Never blame the RSP or the customer's equipment in the reply; describe what we checked and what the next step is.
6. If the input lacks what was found or what happens next, draft the acknowledge paragraph only and list what is needed under BEFORE SENDING.
