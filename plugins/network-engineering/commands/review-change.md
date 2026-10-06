---
description: Review a proposed network change for intent, risk, pre-checks, implementation order, verification commands and rollback
argument-hint: <paste the change request, the before/after config, and the window if known>
---

Run the network-engineer skill in **review-change** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules. Separate the three inputs: the stated intent, the config diff, and the window. If any of them is absent, name it under MISSING OR AMBIGUOUS and still review what is present.
2. Score the change with `references/change-risk-matrix.md` (blast radius, reversibility, protocol impact, window) and explain the score in one line.
3. Use `references/config-review-checklist.md` for policy, route-leak and redundancy checks, and `references/verification-commands.md` for the exact pre-check and verification commands on the vendor in the paste.
4. Output the full Change review template in this order: CHANGE SUMMARY, INTENT (as understood), RISKS (High / Med / Low with why), MISSING OR AMBIGUOUS, PRE-CHECKS, IMPLEMENTATION ORDER, VERIFICATION COMMANDS, ROLLBACK, QUESTIONS.
5. ROLLBACK must be a concrete sequence that returns the device to the pre-change state, not "revert the change". On Junos prefer `rollback 1` with `commit confirmed` guidance; on other platforms list the explicit reverse commands.
6. Input missing: if no config diff or change description was pasted, output only CHANGE SUMMARY: not provided and a MISSING OR AMBIGUOUS list of what to paste.
