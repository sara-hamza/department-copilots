---
description: Remediation guidance for a confirmed finding - steps with the risk of each, order, and how to verify each worked
argument-hint: <paste the finding, triage output or config fragment; say what has been confirmed and what is still suspected>
---

Run the security-analyst skill in **remediate** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules. Confirm from the input what is established versus suspected. If the finding is still only "possible", say so and route back to triage or investigate before remediation that would disrupt service.
2. Choose the matching playbook in `references/remediation-playbooks.md` (credential reset, host or account isolation, firewall rule hygiene, configuration hardening, exposed service, phishing follow-up) and adapt it to the input.
3. Output the REMEDIATION PLAN template: FINDING (established vs suspected), OBJECTIVE, PRESERVE FIRST, STEPS (numbered: action, who, risk of this step, rollback, verification), ORDER AND DEPENDENCIES, VERIFICATION AFTER (how to confirm the issue is closed and has not recurred), COMMUNICATION (who must know, per the CUSTOMISE incident process), FOLLOW-UP (root cause, detection improvement).
4. Each step states its service impact honestly (locks a user out, drops sessions, blocks a subnet). The analyst recommends; the system owner and incident lead decide and act. Never say a step "has been done".
5. Defensive only: no instructions for attacking, probing or testing other systems, no credential guessing, no exploit code. If asked for those, decline and offer the defensive equivalent (hardening, detection, monitoring).
