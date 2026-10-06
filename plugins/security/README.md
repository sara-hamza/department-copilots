# security - Security Analyst

Paste what you can see (firewall log lines, authentication logs, an alert, a config fragment) and get back a severity call with the evidence behind it, a numbered investigation plan, what you cannot yet conclude, and containment options for a human to decide on.

| Command | Use when |
|---|---|
| `/security:triage <paste logs, alert or config>` | New alert or odd log: SEVERITY / OBSERVATIONS / INVESTIGATION / DO NOT CONCLUDE YET / CONTAINMENT OPTIONS |
| `/security:investigate <alert type or paste>` | Investigation checklist tailored to the alert type (auth anomaly, scanning, malware indicator, misconfiguration) |
| `/security:remediate <finding or paste>` | Remediation steps with the risk of each step and how to verify it worked |

Requires `copilot-common`. Defensive analysis only: the analyst never writes exploits, scanners, payloads or evasion, and never states that a system is compromised without evidence from the input.

Reference knowledge lives in `skills/security-analyst/references/`. Escalation contacts, severity definitions and the incident process are marked `CUSTOMISE`.
