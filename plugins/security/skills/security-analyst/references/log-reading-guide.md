# Log reading guide

Read the fields that carry meaning, establish the time window and zone first, and separate what the log says from what it suggests. A log line is an observation; the story around it is inference.

## First five questions for any paste

1. What produced this (firewall, VPN, identity provider, OS, EDR, web server, mail gateway, network device)?
2. What is the time zone, and is the clock trusted? Note it beside every finding.
3. What is the window? First and last timestamp, and whether this is a sample or the full set.
4. Who or what are the actors: source, destination, account, host, process?
5. What prompted the look? An alert rule, a user, a routine review. The rule's logic matters as much as the log.

## Firewall and perimeter logs

| Field | Why it matters | Watch for |
|---|---|---|
| Action (allow, deny, drop, reset) | Denies show attempts; allows show exposure | Allows among a sea of denies from the same source |
| Source IP and port | Who; ephemeral ports change, fixed source ports suggest tooling | Internal source doing external-style scanning |
| Destination IP and port | What was targeted; management ports (22, 23, 161, 443, 830, 3389, 5900, 8443) are high value | Destination is a network device, jump host or NMS |
| Rule name or ID | Which policy matched; "default deny" vs a broad allow | Rules named temp, test, any, or with no description |
| Direction and zone | Inbound from internet vs lateral | Lateral traffic between segments that should not talk |
| Bytes and duration | Volume and persistence | Long sessions with steady small volume (beaconing) or large outbound bursts |
| NAT details | Which internal host was really involved | Mapping errors exposing the wrong host |
| Counts per minute | Rate separates scanning from use | Even, machine-like intervals |

Read order: group by source, then by destination port, then look at allows. Denies alone are usually noise; allows that follow denies from the same source are the finding.

## Authentication, VPN and identity logs

| Field | Why it matters | Watch for |
|---|---|---|
| Result (success, failure, locked, MFA denied) | The one field that matters most | Success after a run of failures |
| Failure reason (bad password, no such user, expired, MFA timeout) | Separates spraying (many "no such user" or one failure per user) from brute force (many on one user) | "No such user" with directory-like usernames |
| Account | Privileged accounts, service accounts, shared accounts | Service account interactive logins |
| Source IP, geo, ASN | New locations and hosting providers | Hosting or VPN provider ranges, countries with no staff |
| Device, user agent, client | Known device vs new | Scripted clients, outdated agents, mismatch with the user's usual device |
| MFA method and outcome | Push accepted after many prompts; method changes | Number of prompts before accept; new method registered |
| Session details (duration, logoff) | Unusual length or persistence | Sessions overlapping from different locations |
| Target application or system | Where they went after login | Admin consoles, NMS, mail rules |

Read order: find successes; for each success check what preceded it from the same source and account; then look at what the session did.

## Operating system and endpoint logs

| Field | Why it matters | Watch for |
|---|---|---|
| Event type (logon, process create, service install, scheduled task, privilege use) | What happened | Process creation with a script host or shell as the child of an office or browser process |
| Parent and child process, command line | Behaviour chain | Encoded or obfuscated command lines; downloads via scripting tools |
| User context and integrity level | Who ran it | System or admin context from a user action |
| File path and signer | Where it ran from | Temp, downloads, user profile paths; unsigned binaries |
| Network connections from the process | Where it talked | Periodic connections to one external host |
| Persistence artefacts (run keys, services, tasks, startup folders) | Survives reboot | New entries with no change ticket |
| EDR verdict and action | Detected only vs blocked | "Detected" with no block means it may have run |

## Network device logs (OLT, aggregation, routers, switches)

| Field | Why it matters | Watch for |
|---|---|---|
| Login source and protocol (SSH, Telnet, HTTP, console, SNMP) | Who manages it and how | Telnet or HTTP in use; logins not from the jump host or NMS range |
| Config change events and commit diffs | What changed | Changes outside maintenance windows; user accounts, ACLs, SNMP communities, logging targets modified |
| AAA results | Central auth working or fallback to local | Local account use when TACACS or RADIUS should be in play |
| Interface and session alarms | Operational context | Correlate with change times to separate ops events from security events |
| Logging destination changes | Visibility | Syslog or SNMP trap targets removed or changed |

## Email headers and mail gateway logs

| Field | Why it matters | Watch for |
|---|---|---|
| Return-path, From, Reply-To | Who it claims to be from | Display name matches a known person, address does not; Reply-To differs |
| Authentication-Results (SPF, DKIM, DMARC) | Did the sending domain authorise it | Fail or none on a domain that normally passes |
| Received chain | Path taken | Unexpected relays; internal server appearing in an external message |
| URL and attachment details | Payload | Newly registered domains, lookalike domains, archive attachments |
| Recipients and delivery result | Scope | Many internal recipients; delivered vs quarantined |
| Mailbox rules created | Persistence after compromise | Forwarding to external addresses; rules that delete or move security mail |

## Working method

1. Normalise timestamps to one zone and sort.
2. Build a short timeline: first event, pivots (first success, first change, first outbound), last event.
3. Count: how many sources, accounts, hosts, ports. Numbers change the story.
4. For each candidate finding write: OBSERVED (line and value), INFERRED (what it suggests), UNKNOWN (what you would need).
5. Check the false-positive list in `alert-triage-matrix.md`.
6. Name the single most discriminating piece of evidence to collect next.

## Evidence quality notes

- A log excerpt chosen by a human is a sample; say so and ask for the full window if it matters.
- Clock skew between sources can invert cause and effect; compare against a trusted source.
- Absence of a log entry is not evidence of absence; check that the source was logging during the window.
- Screenshots are transcriptions; mark values read visually.
- Threat-intelligence verdicts on IPs and domains age quickly; treat a listing as a prompt, not proof.

## CUSTOMISE: company log sources

Document the real sources so the analyst recognises formats and knows what exists:

- Perimeter firewalls: `<vendor, log format, retention, where to export>`
- VPN and remote access: `<...>`
- Identity provider and directory: `<...>`
- EDR: `<...>`
- Email gateway: `<...>`
- Network device syslog and AAA (OLT, aggregation, core): `<...>`
- NMS audit logs: `<...>`
- SIEM or log platform and query language: `<...>`
- Known scanner and monitoring source ranges (to recognise benign scan-like traffic): `<...>`
- Jump host and management subnet ranges: `<...>`
