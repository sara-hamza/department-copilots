# Alert triage matrix

Classify the pattern, weigh the benign and malicious explanations, rate severity by asset and evidence strength, and name the check that separates the two. Every rating carries "possible" or "likely" until the input shows the event.

## Severity scale (defaults; CUSTOMISE below)

| Severity | Meaning | Typical examples |
|---|---|---|
| Critical | Likely active compromise of a high-impact asset or identity, or confirmed data access | Confirmed unauthorised admin login to NMS or OLT management; ransomware behaviour on a server; valid credentials used from an unexpected country followed by privilege changes |
| High | Likely malicious activity with a plausible path to impact, or a confirmed vulnerability on an exposed asset | Successful login after a password-spray pattern; malware indicator with execution evidence; management interface exposed to the internet |
| Medium | Suspicious activity without evidence of success, or a misconfiguration with limited exposure | Sustained failed logins without a success; internal scan from an unexpected host; overly permissive firewall rule on an internal segment |
| Low | Likely benign or noise, but worth recording | Scanner traffic blocked at the perimeter; single failed login; expired certificate warning |
| Informational | No action; context for later | Routine admin activity confirmed with owner |

Severity is impact x confidence. Raise impact for: identity providers, VPN gateways, jump hosts, NMS and OLT management, aggregation routers, domain controllers, backup systems, finance and HR systems, anything internet-facing. Raise confidence only with corroborating evidence from more than one source.

## Matrix

### Authentication anomalies

| Pattern | Benign explanation | Malicious explanation | Distinguishing check | Default severity |
|---|---|---|---|---|
| Many failed logins, one account, one source, short window | User mistyping, cached old password on a device or script after rotation | Brute force against one account | Did any success follow? Does the source belong to the user? Was the password changed recently? | Low to Medium (possible) |
| Few failed logins each across many accounts, one or few sources | Misconfigured service account across hosts; SSO outage | Password spraying | Account list looks like a directory dump? Sources external? Any success? | Medium (possible), High if any success |
| Success from a new country or ASN | Travel, VPN, mobile carrier NAT | Credential theft | Confirm with the user; check device and MFA method; compare with prior login history | Medium (possible), High if followed by changes |
| Impossible travel (two locations too far apart in the interval) | Split tunnelling, cloud proxies, mobile roaming | Session or credential theft | Both sessions from known devices? Same user-agent? | Medium (possible) |
| MFA fatigue (repeated push prompts, then accept) | User fumbling a new phone | Attacker with the password pushing prompts | Timing between prompts; source of the auth attempts; user confirmation | High (likely if user denies initiating) |
| Login outside hours to a management system | On-call work, maintenance window | Unauthorised access | Change ticket or on-call roster; confirm with the person | Medium (possible), High for NMS/OLT |
| Service account interactive login | Admin troubleshooting | Credential misuse | Owner confirmation; which host; what followed | Medium (possible) |
| New admin account, group change, MFA method change | Approved change | Persistence | Change ticket; who made it; from where | High (possible) until ticket found |
| Account lockouts across many users | Password policy change, AD replication issue, expired service password | Spray causing lockouts | Pattern of sources; timing versus any change | Medium |

### Scanning and reconnaissance

| Pattern | Benign explanation | Malicious explanation | Distinguishing check | Default severity |
|---|---|---|---|---|
| Many destination ports, one source, perimeter denies | Internet background noise, research scanners | Reconnaissance | Any allows among the denies? Source reputation from the input? Target an exposed service? | Low |
| Many internal hosts contacted on one port from one internal host | Vulnerability scanner, monitoring, asset discovery | Internal reconnaissance or worm | Is the source a known scanner or monitoring host? Scheduled? | Medium (possible), High if unknown host |
| Sequential probing of management ports (22, 23, 161, 443, 830) toward network devices | NMS discovery | Targeting the network management plane | Source is the NMS? Authenticated? | High if not the NMS |
| DNS queries for many internal hostnames from one client | Software inventory, backup agent | Discovery | Which process on the host; timing | Medium (possible) |

### Malware and endpoint indicators

| Pattern | Benign explanation | Malicious explanation | Distinguishing check | Default severity |
|---|---|---|---|---|
| EDR alert, detection only, quarantined | True positive handled; or false positive on admin tooling | Initial access attempt | Was the file executed before quarantine? Parent process? User action (email attachment)? | Medium (possible), High if executed |
| Outbound connection to a flagged domain or IP | Stale threat list; CDN overlap; ad network | Command and control | Process, periodicity (beaconing), volume, other hosts contacting it | Medium (possible), High if periodic and persistent |
| Office document spawning a shell or script host | Macro-based automation (rare, should be known) | Macro malware | Which user, which document, where from | High (likely) |
| Mass file renames or encryption-like behaviour | Backup or archive job | Ransomware | Process, rate, extension pattern, ransom note presence | Critical (likely) |
| Unexpected scheduled task, service or run key | Software install | Persistence | Change ticket; binary path; signer | High (possible) |
| Large outbound transfer from a server | Backup to cloud, replication | Exfiltration | Destination ownership; schedule; data type | High (possible) until destination confirmed |

### Misconfiguration and exposure

| Pattern | Benign explanation | Malicious explanation | Distinguishing check | Default severity |
|---|---|---|---|---|
| Firewall rule any/any or broad source to a management port | Temporary troubleshooting rule left in place | Deliberate backdoor | Change history; who added; when | High if internet-facing, Medium internal |
| Management interface reachable from the internet | Misconfigured NAT or ACL | Exposure being exploited | Auth logs on that interface; who connected | High (confirmed exposure); Critical if foreign logins succeeded |
| Default or shared credentials in a config fragment | Legacy device | Trivial access path | Device role; reachability | High for network devices |
| Telnet, HTTP or SNMPv1/v2c enabled on network devices | Legacy monitoring | Credential sniffing path | Which segment; who uses it | Medium |
| Logging disabled or log source silent | Agent crash, disk full | Log tampering | When did it stop; host state; correlate with other events | Medium (possible), High if coincides with other indicators |
| Certificate expired or self-signed on an internal service | Oversight | Interception | None usually; hygiene item | Low |

### Email and user reports

| Pattern | Benign explanation | Malicious explanation | Distinguishing check | Default severity |
|---|---|---|---|---|
| User reports suspicious email, not clicked | Spam | Phishing campaign | Headers (SPF/DKIM/DMARC results in the input), sender domain, link domain, other recipients | Low to Medium |
| User clicked and entered credentials | Legitimate site misremembered | Credential harvest | Which site; reset status; subsequent logins for that user | High (likely) |
| Invoice or payment detail change request by email | Genuine supplier change | Business email compromise | Verify by phone on a known number; header analysis; route to finance process | High (possible) |

## Common false positives (check before rating)

- Monitoring and vulnerability scanners generating scan-like traffic on schedule.
- Service accounts failing after password rotation on one forgotten host.
- Cloud provider and CDN IP ranges tripping geo-based rules.
- Time-zone mismatches making activity look "out of hours".
- SSO or identity provider outages causing waves of failures.
- Backup, replication and sync jobs producing large transfers.
- Admin tooling (remote management, scripting hosts) flagged by EDR heuristics.
- Internet background radiation hitting the perimeter and being denied.

## Escalation triggers (defaults; CUSTOMISE below)

Escalate immediately when the input shows any of: successful unauthorised access to NMS, OLT, aggregation or identity systems; ransomware behaviour; confirmed credential harvest for a privileged user; management interface exposed with foreign successful logins; evidence of data leaving to an unknown destination; any event the employee believes may involve personal information (route also to compliance for notification assessment).

## CUSTOMISE: company incident process

Replace with the approved process:

| Severity | Notify | Within | Channel |
|---|---|---|---|
| Critical | Security lead, CIO or equivalent, on-call network engineering, incident manager | 15 minutes | `<phone / Teams bridge>` |
| High | Security lead, system owner | 1 hour | `<channel>` |
| Medium | Security queue, system owner | Same business day | `<ticket queue>` |
| Low / Informational | Security queue | Weekly review | `<ticket queue>` |

- Security lead: `<name, role, phone, email>`
- Incident manager / duty manager: `<...>`
- Network engineering on-call: `<...>`
- Privacy and compliance contact for notification assessment: `<...>`
- External incident response retainer (if any): `<...>`
- Incident ticket category and template: `<...>`
- Evidence preservation location: `<...>`
