---
description: Defensive triage of pasted firewall logs, auth logs, alerts or config fragments - severity, observations, investigation steps, what not to conclude yet, containment options
argument-hint: <paste the log lines, alert text or config fragment; say what prompted the look if known>
---

Run the security-analyst skill in **triage** mode on this input:

$ARGUMENTS

Steps:
1. Apply `copilot-common` privacy rules. Usernames, IP addresses and hostnames in the input are evidence; keep them in the triage but do not add any not in the input. If a screenshot is provided, transcribe it first (screenshot-reader).
2. Read the input with `references/log-reading-guide.md` to identify the source, the fields that matter and the time window, then classify the pattern with `references/alert-triage-matrix.md`.
3. Output the TRIAGE template: SEVERITY (with "possible" or "likely" and why), OBSERVATIONS (facts from the input with timestamps, counts and sources), INVESTIGATION (numbered, each step saying what it would confirm or rule out), DO NOT CONCLUDE YET (what the evidence does not establish), CONTAINMENT OPTIONS (for human decision, each with its impact), ESCALATE IF.
4. Check the false-positive list for the pattern before rating. If the pattern matches a known benign cause (scanner, monitoring, service account rotation), say so and list the check that would confirm it.
5. If the input is too thin to classify (no timestamps, no source, a single line), say DO NOT CONCLUDE YET and name the single most useful piece of evidence to collect next. Never state compromise, exfiltration or attacker intent unless the input shows it.
