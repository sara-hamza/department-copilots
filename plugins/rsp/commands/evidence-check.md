---
description: Check that our evidence actually supports what we are about to tell the RSP - CLAIM, SUPPORTED BY, NOT SUPPORTED, REWORD AS
argument-hint: <paste the draft reply or the statements you plan to make, plus the evidence>
---

Run the rsp-assistant skill in **evidence-check** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules.
2. Split the draft into individual claims (one per sentence that asserts a fact, a cause or a responsibility). Number them.
3. For each claim, find the evidence line that supports it. Use `references/wholesale-demarcation.md` to decide whether the claim is about something the network operator can actually see; a claim about the RSP side (BNG, RADIUS, IP, CPE) is NOT SUPPORTED unless the RSP supplied the evidence.
4. Output:
```
EVIDENCE CHECK
CLAIM 1: <sentence>
SUPPORTED BY: <evidence line with value and time> | none
NOT SUPPORTED: <the part that goes beyond the evidence>
REWORD AS: <neutral wording that only says what the evidence shows, or a question to the RSP>

CLAIM 2: ...

VERDICT
<ready to send | send after rewording claims n, m | do not send: findings not established>
```
5. Watch for these patterns: "the fault is on your side" (never supported; reword to what the access path shows); "the ONT is fine" (supported only if RX, UNI state and MAC learning are all in evidence); "no issues found" (reword to list what was checked); "PPPoE is working" (supported only by PADI/PADO/PADR/PADS evidence or an RSP-confirmed session); "customer CPE is faulty" (never provable from the access side).
6. Input missing: if there is no draft, ask for the statements to check; if there is no evidence, mark every claim NOT SUPPORTED and say so.
