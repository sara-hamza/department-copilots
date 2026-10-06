# Response templates for RSP replies

All plain text. Precise, neutral, evidence-led (writing-helper RSP tone). No end-customer personal data; use the service identifier. Every fact in ACCESS NETWORK FINDINGS carries a value and a time with zone. WHAT THIS INDICATES says only what the findings support. SLA wording is a placeholder unless supplied.

## Common frame

```
DRAFT RESPONSE TO RSP
SUBJECT: <ticket ref> - <service id> - <status in four words>

SUMMARY
<what the RSP reported, in one line; what the network operator found, in one line>

ACCESS NETWORK FINDINGS
<bottom-up, one fact per line, with value, time and zone>

WHAT THIS INDICATES
<neutral interpretation>

REQUESTED FROM RSP
1. <numbered>

NEXT STEP
<what the network operator will do and the trigger; or "ticket held pending the above">

INTERNAL NOTES (not to send)
<confidence, what was removed, who to copy, what to check next on our side>
```

## Template 1: fault found on the access side

```
SUMMARY
Reported: no service since <time>. Found: ONT offline with loss of signal; fault located on the access path.

ACCESS NETWORK FINDINGS
ONT <serial last 4>: offline since 04 Oct 2026 21:14 ACDT, last-down reason LOS (no dying gasp).
ONT RX at last reading: -30.1 dBm (1490 nm) at 21:10 ACDT; previous day -17.8 dBm.
OLT port <id>: operational; 30 of 31 ONTs on the same splitter online.
No planned works on this PON.

WHAT THIS INDICATES
A fault on the access path serving this premises only, most likely the drop or lead-in. This is within the company's responsibility.

REQUESTED FROM RSP
1. Confirm the end customer's availability for a field visit (date and window).
2. Confirm the ONT has power and the LOS indicator is lit (customer observation).

NEXT STEP
Field visit to be scheduled on confirmation of access. We will update this ticket on completion with the remediation and the post-repair RX reading. [SLA wording from wholesale agreement]
```

## Template 2: no fault found on the access side (session or traffic issue)

```
SUMMARY
Reported: PPP session established, no internet. Found: access path operating within specification to the UNI and the NNI.

ACCESS NETWORK FINDINGS
ONT <serial last 4>: online since 02 Oct 2026 08:02 ACDT, no active alarms.
ONT RX: -18.4 dBm (1490 nm) at 06 Oct 2026 10:05 ACDT. OLT RX from ONT: -22.1 dBm.
UNI: up, 1000/full, no errors in the last 24 h.
MAC <last 4> learned on C-VLAN <n>; service port mapped to S-VLAN <n> toward NNI <id>.
NNI <id>: LAG up, all members active; S-VLAN <n> counters incrementing in both directions at 10:05 ACDT.
Service port counters: <n> packets in, <n> packets out in the last 15 minutes at 10:05 ACDT.

WHAT THIS INDICATES
Traffic is passing the UNI and the NNI for this service. The access path is operating within specification. To locate where the session loses connectivity we need the BNG-side details below.

REQUESTED FROM RSP
1. Is the PPPoE session currently established on the BNG? Session start time and BNG id.
2. IP address assigned, pool type (public, CGNAT, quarantine).
3. Subscriber traffic seen at the BNG in and out over the last 15 minutes.
4. Default route or routing for this subscriber; any policy, quota or suspension applied.
5. Session details: MTU, VLAN tags seen, RADIUS attributes returned.

NEXT STEP
Ticket held pending the above. On receipt the network operator will correlate the BNG session times with the access counters and advise within <time> [confirm].
```

## Template 3: awaiting RSP evidence (thin input)

```
SUMMARY
Reported: <symptom>. We have checked the access path and requires the information below to proceed.

ACCESS NETWORK FINDINGS
<what has been checked, with values and times; if a check is outstanding, omit it here and note it internally>

WHAT THIS INDICATES
No fault has been identified on the access path from the checks listed. Further checks depend on the session details held by the RSP.

REQUESTED FROM RSP
<numbered questions from the question bank for the symptom>

NEXT STEP
Ticket held pending the above.

INTERNAL NOTES (not to send)
Access checks still outstanding on our side: <list>. Do these before chasing the RSP.
```

## Template 4: planned works or known incident

```
SUMMARY
Reported: <symptom> for <n> services. Found: the services are within the scope of <planned works ref | incident ref>.

ACCESS NETWORK FINDINGS
<OLT or PON affected, start time, current state, services affected count>

WHAT THIS INDICATES
The reported impact is consistent with the <works | incident>. No separate fault is indicated for the listed services.

REQUESTED FROM RSP
1. Any service in the list that remains affected after the restoration time, with its symptom.

NEXT STEP
Restoration notice will be issued via the standard channel. We will confirm per-service status on request after restoration.
```

## Template 5: repeat fault

```
SUMMARY
Reported: recurrence of <symptom>, previous ticket <ref>. Found: <current access state>.

ACCESS NETWORK FINDINGS
Previous remediation on <date>: <action>, post-repair RX <value>.
Current: <values and times>.
Alarm history since previous closure: <count and types>.

WHAT THIS INDICATES
<if degraded again: access path degraded; field visit required. If stable: access path stable since remediation; the current symptom is not explained by the access evidence>

REQUESTED FROM RSP
<per symptom block>

NEXT STEP
<field visit with trigger; or held pending>
```

## Phrase bank

| Situation | Phrase |
|---|---|
| Access clean | "The access path to the UNI is operating within specification." |
| L2 clean | "A MAC is learned on the expected VLAN and the service port is mapped to the NNI; counters are incrementing in both directions." |
| PADI seen, no PADO | "Discovery frames from the customer MAC are observed at the OLT; no offer has been observed from the NNI side." |
| Nothing from the CPE | "No frames have been observed from the UNI since <time>. Please confirm the CPE WAN state." |
| Optical fault | "Optical receive level at the ONT is below the operating range; a fault on the access path is indicated." |
| Cannot determine | "The available evidence does not establish where the session is lost. The items below will allow this to be determined." |
| Decline to speculate | "We are not able to comment on the BNG or CPE state from the access network; the RSP's session records are required." |

## Pre-send checklist

1. Every finding has a value, a unit and a time with zone.
2. Nothing in WHAT THIS INDICATES goes beyond ACCESS NETWORK FINDINGS (run evidence-check).
3. No end-customer personal data.
4. No SLA, credit or restoration promise unless supplied.
5. REQUESTED FROM RSP is numbered and answerable.
6. INTERNAL NOTES removed before pasting.

## CUSTOMISE: company reply conventions

- Ticket subject format: `<fill in>`
- Standard sign-off and wholesale support role name: `<fill in>`
- Agreed turnaround to quote in NEXT STEP: `<fill in>`
- Channel for restoration notices: `<fill in>`
