---
description: Translate technical ticket or field text into customer-friendly wording, side by side TECHNICAL / CUSTOMER WORDING
argument-hint: <paste the technical note, NOC ticket text or field report>
---

Run the customer-case-assistant skill in **plain-english** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules. Keep internal identifiers (PON, OLT, port numbers, ticket IDs) out of the customer column.
2. Use `references/jargon-translation-table.md` for every term. Where a term is not in the table, translate by describing what the customer would notice (lights, connection, speed) rather than the mechanism.
3. Produce exactly this template:

```
PLAIN ENGLISH TRANSLATION

TECHNICAL                                   | CUSTOMER WORDING
<sentence or fragment from the input>       | <what to say to the customer>
...

TERMS REPLACED
<term> -> <customer phrase>

DO NOT SAY TO THE CUSTOMER
- <internal detail, blame, unconfirmed cause, RSP-side speculation> | why

WHOLESALE CHECK
<anything in the technical text that belongs to the RSP's domain (PPP, IP, modem, plan) and how the customer wording hands that back to the RSP without blame>
```

4. Keep the customer column factual and calm. "Appears" and "we are checking" for anything not confirmed. No percentages or dBm values; describe the effect.
5. Split long technical sentences into one row per fact so the employee can pick which rows to use.
6. If no input is given, ask for the technical text and show three example rows from the table.
