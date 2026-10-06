---
description: From an RSP claim and our evidence, work out what we hold, what to ask the RSP (numbered), and what we will do when answered
argument-hint: <paste the RSP claim or ticket and the access-network evidence we hold>
---

Run the rsp-assistant skill in **questions** mode on:

$ARGUMENTS

Steps:
1. Apply `copilot-common` privacy rules. Keep the end customer's name, phone and full address out of the output; use the service identifier the RSP uses.
2. Place the symptom on the demarcation map in `references/wholesale-demarcation.md`: which elements are the company's (ONT, PON, OLT, aggregation to NNI) and which are the RSP's (BNG, authentication, IP, CPE, customer relationship), and what each side can see.
3. Pick the matching symptom block in `references/rsp-question-bank.md` and tailor the questions to the evidence already provided. Drop any question the paste already answers.
4. Output:
```
RSP CLAIM (as understood)
<one line>

EVIDENCE WE HOLD
✓ <access-network fact with value, time and zone>
✗ <failed fact>
? <access-side check not yet done; list as our own next check, not an RSP question>

EVIDENCE WE NEED FROM RSP
1. <question, answerable with a value or yes/no>
2. ...

WHAT WE WILL DO WHEN ANSWERED
If <answer A> then <our action>. If <answer B> then <our action>.
```
5. For "customer has PPP session but no internet" the questions must cover: session established on the BNG (time, BNG id); IP assigned (and whether it is public, CGNAT or wrong pool); traffic seen from the subscriber at the BNG; default route or routing for that subscriber; BNG session details (MTU, VLAN tags seen, RADIUS attributes, any policy or quota applied).
6. Input missing: if no RSP claim was given, ask for it; if no access evidence was given, list the access checks to run first (ONT state and RX, UNI state, MAC learned on the service port, PPPoE discovery counters, aggregation and NNI state).
