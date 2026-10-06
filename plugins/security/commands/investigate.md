---
description: Investigation checklist tailored to an alert type - authentication anomaly, scanning, malware indicator, misconfiguration, data movement
argument-hint: <alert type or paste the alert; include what systems and log sources exist if known>
---

Run the security-analyst skill in **investigate** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules. Everything comes from the paste; the analyst never queries a SIEM, firewall, identity provider or endpoint tool itself.
2. Identify the alert type using `references/alert-triage-matrix.md`. Build the checklist from that row's investigation steps and from the field guidance in `references/log-reading-guide.md`.
3. Output the INVESTIGATION CHECKLIST template: ALERT TYPE, HYPOTHESES (benign and malicious, side by side), EVIDENCE TO COLLECT (numbered: source, what to look for, time window, what it would show), QUESTIONS FOR THE SYSTEM OWNER, DECISION POINTS (if evidence shows X then Y), PRESERVE (what to keep before anyone changes anything), ESCALATE IF.
4. Every evidence step must be read-only and defensive: exports, log queries, reviews, confirmations with owners. Do not include steps that run tools against other systems, test credentials, or probe hosts.
5. If the alert type is unclear, list the two or three closest types and the evidence that would distinguish them, then stop. Do not assume the worst case.
