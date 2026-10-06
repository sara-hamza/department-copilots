# Remediation playbooks

Defensive playbooks for findings that have been established by evidence. Each step states who acts, the risk of the step, how to roll it back and how to verify it worked. The analyst recommends; the system owner and incident lead decide and act. Preserve evidence before changing anything.

## Universal preamble

PRESERVE FIRST (before any step below)
1. Export the relevant logs for the window plus margin (security lead; no risk; verify export opened and hashed or stored in the evidence location).
2. Record the timeline with time zone and who observed what.
3. Screenshot or export current state of the affected object (account settings, firewall rule, config) before modifying it.
4. Open the incident ticket per the CUSTOMISE process and record the severity call with its confidence word.

Communication rule: tell the system owner before acting on their system; tell affected users plainly and without blame; route possible personal-information exposure to the privacy and compliance contact for notification assessment.

## Playbook 1: Credential reset (suspected or confirmed credential compromise)

| Step | Who | Risk | Rollback | Verify |
|---|---|---|---|---|
| 1. Confirm scope: which accounts, which systems they can reach, whether privileged | Security lead with system owner | None | n/a | List written |
| 2. Revoke active sessions and tokens for the account | Identity admin | User loses current sessions; automated jobs using the account fail | Re-issue | Session list empty; user re-authenticates |
| 3. Reset password out of band (not via email to the possibly compromised mailbox) | Identity admin with user by phone or in person | User locked out until contacted | n/a | Login with new credential succeeds for the user only |
| 4. Re-enrol MFA if the method may be attacker-controlled; remove unknown methods and devices | Identity admin | User needs device access | Re-add known device | Only known methods remain |
| 5. Review and remove mailbox rules, forwarding, app consents, API keys and recovery addresses created in the window | Mail and identity admin | Legitimate rules removed if not checked with user | Restore from export | Rule list matches user's expectation |
| 6. Check what the account did in the window (logins, changes, data access) and feed back into scope | Security lead | None | n/a | Timeline updated |
| 7. For privileged or service accounts: rotate dependent secrets, update stored credentials in systems that use them | System owners | Service outage if a dependency is missed | Restore previous secret temporarily | All dependent services healthy |
| 8. Monitor the account for 14 days for new locations, devices and rule changes | Security | None | n/a | Daily check logged |

Do not: reset by sending a link to the affected mailbox; reuse a pattern-based password; skip service account dependencies.

## Playbook 2: Isolation of a host or account

| Step | Who | Risk | Rollback | Verify |
|---|---|---|---|---|
| 1. Decide the isolation level: network quarantine via EDR, switch port disable, VLAN move, or account disable | Incident lead with system owner | Service loss for the user or the role of that host; evidence loss if the host is powered off | Reverse the change | Decision and impact recorded |
| 2. Capture volatile evidence first if the capability exists (process list, network connections, memory if tooling available) | Security | Delay | n/a | Captured to evidence location |
| 3. Apply isolation (prefer EDR quarantine that keeps management channel; avoid powering off) | Endpoint or network admin | Host unreachable for user; may alert an intruder | Release quarantine | Host cannot reach anything but the management channel |
| 4. Disable the associated account if credential misuse is suspected (Playbook 1) | Identity admin | User locked out | Enable | Login fails |
| 5. Identify what the host talked to in the window; assess those hosts | Security | None | n/a | List and assessment written |
| 6. Remediate the host: reimage preferred over cleaning for confirmed malware; patch and harden before return | Endpoint admin | Data on host lost if not backed up | n/a | Clean build verified, EDR healthy |
| 7. Return to network in stages; monitor for 14 days | Endpoint admin, security | Recurrence | Re-isolate | No alerts; expected traffic only |

Do not: power off a server if memory evidence matters and the capability to capture exists; isolate a network device without engineering on-call present; isolate an OLT or aggregation node without assessing RSP customer impact and following the change process.

## Playbook 3: Firewall rule hygiene (overly broad, temporary or unexplained rules)

| Step | Who | Risk | Rollback | Verify |
|---|---|---|---|---|
| 1. Export the current rule base and change history | Network admin | None | n/a | Export stored |
| 2. List rules that are any/any, broad source to management ports, disabled-but-present, expired temporary, or without description or owner | Security with network admin | None | n/a | List with rule IDs |
| 3. For each, identify owner and purpose; check hit counts over 90 days | Network admin | None | n/a | Table: rule, owner, purpose, hits |
| 4. For rules with no owner, no hits, or purpose expired: disable (do not delete) in a change window | Network admin via change process | Breaks an unknown dependency | Re-enable | Monitor for failures for 7 days |
| 5. For needed-but-broad rules: narrow to specific sources, destinations, ports; add description, owner, expiry | Network admin via change process | Breaks access if narrowed too far | Restore previous rule | Owner confirms access works |
| 6. Delete disabled rules after the monitoring period | Network admin via change process | Low | Recreate from export | Rule base matches intended state |
| 7. Add a standard: every rule has description, owner, ticket, expiry for temporary rules; review quarterly | Security lead | None | n/a | Standard published |

Order: management-plane exposure first (anything allowing internet or broad internal sources to NMS, OLT, jump hosts, identity), then internet-facing services, then internal segmentation.

## Playbook 4: Configuration hardening (network devices and servers)

| Area | Steps | Risk | Verify |
|---|---|---|---|
| Management access | Restrict to management subnet and jump hosts; SSH only, disable Telnet and HTTP; SNMPv3 with auth and privacy, remove v1/v2c communities; session timeouts | Lockout if the restriction excludes the admin source; apply with console or out-of-band access available | Login from outside the allowed range fails; from inside succeeds |
| Authentication | Central AAA (TACACS or RADIUS) with per-user accounts and MFA where supported; local fallback account with strong unique credential stored in the vault; remove default and shared accounts | Loss of access if AAA misconfigured | AAA logs show per-user logins; local account only used on AAA failure |
| Logging | Syslog to the central platform with correct time zone and NTP; log config changes and logins; alert on logging target changes | Minimal | Test event appears in SIEM with correct time |
| Services | Disable unused services and interfaces; update firmware per vendor advisories with change control | Service impact; test in lab first for network devices | Service inventory matches intent |
| Control plane | ACLs on management and control-plane traffic; rate limits; disable unneeded protocols on customer-facing ports | Can affect legitimate protocols if too tight | Monitor protocol health after change |
| Servers | Patch cadence; least-privilege service accounts; host firewall; EDR present; disable legacy protocols (SMBv1, NTLMv1, TLS 1.0/1.1) | Legacy clients break | Compatibility checked, then disabled |
| Backups | Offline or immutable copies; test restore; separate credentials | Cost | Restore test documented |

Apply through the change process with pre-checks, a maintenance window where RSP services could be affected, and a rollback plan. Verify each change with a read-only check, not by probing from outside.

## Playbook 5: Exposed service (management interface or service reachable from the internet)

1. Confirm exposure from the input (firewall rule, NAT, external scan report supplied by the employee); do not probe to confirm.
2. Check auth logs on that interface for the exposure period; any success from unknown sources escalates to Playbook 1 and 2.
3. Remove the exposure: delete or narrow the NAT or rule via emergency change; prefer VPN or jump-host access.
4. Rotate credentials for that interface and any accounts that logged in during the period.
5. Review the device config for changes in the period (compare to last known good backup).
6. Add a detection: alert on any new rule allowing internet sources to management ports.

## Playbook 6: Phishing follow-up

1. Scope: who received it (gateway search by subject, sender, URL hash), who clicked, who submitted credentials (from proxy logs or user reports).
2. Block the sender domain, URL and attachment hash at the gateway and proxy; purge from mailboxes if the platform supports it.
3. For users who submitted credentials: Playbook 1.
4. For users who opened an attachment: EDR review of the host; Playbook 2 if indicators are present.
5. Notify recipients with a short factual message and what to do; no blame.
6. Record indicators for detection; feed into awareness training.

## Verification after remediation (all playbooks)

- The specific indicator no longer appears over a defined period (24 hours, 7 days, 14 days depending on severity).
- Logging from the affected system is flowing and complete.
- No new accounts, rules, tasks, forwarding or consents created since the incident.
- Owner confirms service is normal.
- Root cause written: how it happened, why it was not prevented, why it was or was not detected, what changes.

## CUSTOMISE: company remediation specifics

- Change process reference and emergency change path: `<fill in>`
- Evidence preservation location and hashing procedure: `<fill in>`
- Credential vault and rotation procedure: `<fill in>`
- Identity provider and MFA re-enrolment procedure: `<fill in>`
- EDR quarantine capability and who may trigger it: `<fill in>`
- Maintenance window rules for network devices affecting RSP services: `<fill in>`
- User notification template owner: `<fill in>`
- Privacy breach assessment contact: `<name, role, email>`
