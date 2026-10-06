# rsp - RSP Assistant

Paste the RSP's email or ticket, the fault evidence you hold and any logs. Get back the questions to send the RSP, a neutral evidence-led reply, or a check that the evidence really supports what you are about to say.

| Command | Use when |
|---|---|
| `/rsp:questions <RSP claim and our evidence>` | Work out EVIDENCE WE HOLD, EVIDENCE WE NEED FROM RSP (numbered questions), WHAT WE WILL DO WHEN ANSWERED |
| `/rsp:draft-response <ticket and evidence>` | Draft the reply: SUMMARY, ACCESS NETWORK FINDINGS, WHAT THIS INDICATES, REQUESTED FROM RSP, NEXT STEP |
| `/rsp:evidence-check <what we plan to say and the evidence>` | Before sending: CLAIM, SUPPORTED BY, NOT SUPPORTED, REWORD AS |

Requires `copilot-common` (writing-helper RSP tone). Works with `sticky-notes` for carrying ticket context between replies.

Reference knowledge lives in `skills/rsp-assistant/references/`. The demarcation table, SLA references and wholesale contact roles there are sensible defaults marked `CUSTOMISE`; align them with the company's wholesale agreement and operations manual.
