---
description: Draft a technically accurate, neutral, evidence-led reply to the RSP - SUMMARY, ACCESS NETWORK FINDINGS, WHAT THIS INDICATES, REQUESTED FROM RSP, NEXT STEP
argument-hint: <paste the RSP ticket or email and the evidence we hold>
---

Run the rsp-assistant skill in **draft-response** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules and the writing-helper RSP tone: precise, technical, neutral, evidence-led; no speculation about the RSP's network, no emotional language, no internal remarks.
2. Choose the matching template in `references/response-templates.md` (fault accepted on access side, fault not found on access side, awaiting RSP evidence, planned works, repeat fault). Use `references/wholesale-demarcation.md` for the correct demarcation wording.
3. Before writing WHAT THIS INDICATES, run the evidence-check rule from SKILL.md on each sentence: every claim must be supported by a fact in ACCESS NETWORK FINDINGS. If not supported, reword as a question or drop it.
4. Output:
```
DRAFT RESPONSE TO RSP
SUBJECT: <ticket ref> - <service id> - <one-line status>

SUMMARY
<two lines: what was reported, what we found>

ACCESS NETWORK FINDINGS
<facts with values, times and zone; bottom-up: optical, ONT/UNI, L2, session discovery, aggregation/NNI>

WHAT THIS INDICATES
<neutral interpretation; "the access path to the UNI is operating within specification" not "the fault is yours">

REQUESTED FROM RSP
1. <numbered, specific>

NEXT STEP
<what the network operator will do and when, and what will trigger it>

INTERNAL NOTES (not to send)
<anything removed from the draft, confidence, who to copy>
```
5. Never state or imply the RSP is at fault. State what the access network shows and what remains to be established. Do not quote SLA restoration times unless the employee gave them.
6. Input missing: if the evidence is too thin to state findings, output the "awaiting RSP evidence" template with the questions from `references/rsp-question-bank.md` and say under INTERNAL NOTES which access checks should be done first.
