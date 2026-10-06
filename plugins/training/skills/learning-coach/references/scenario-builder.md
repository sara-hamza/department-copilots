# Scenario builder

Scenarios are turn-based fault or process exercises built from the supplied material. The learner sees a starting situation, chooses checks, and receives one result per check. The cause stays hidden until the debrief. All names, addresses and identifiers are fictional.

## Building a scenario (coach's private preparation)

1. Choose the type and difficulty.
2. Pick a cause the material covers (its fault table, procedure or case type).
3. Write the hidden facts: the cause, and the result every plausible check would return. Use thresholds and alarm names exactly as the material states them. Where the material gives ranges, pick realistic values inside them.
4. Write the model path: the order of checks the material's procedure requires, with references.
5. Write the starting situation: only what the learner would see first (ticket text, alarm, customer words, first reading).
6. List the tools: the checks the learner may ask for, in the material's terms.
7. Decide reveal rules: each check reveals only its own result; some checks are "unavailable" if the material says so (for example, no field reading until field attends).

## Scenario card (private to the coach)

```
TITLE:
TYPE: gpon-fault | provisioning | customer-case | custom
DIFFICULTY: easy | medium | hard
SOURCE: <document, sections used>
HIDDEN CAUSE:
HIDDEN FACTS (check -> result):
  <check 1> -> <result>
  <check 2> -> <result>
  ...
MODEL PATH: <ordered checks with references>
DISTRACTORS: <facts that look relevant but are not>
DEBRIEF POINTS: <three things to remember>
```

## Difficulty levers

| Lever | Easy | Medium | Hard |
|---|---|---|---|
| Evidence at start | Clear, consistent | One ambiguous value | Misleading first evidence (historical alarm, stale reading) |
| Number of plausible causes | 1 to 2 | 3 | 4 or more, two with similar signatures |
| Distractors | None | One | Several, including a second unrelated minor issue |
| Information availability | All checks available | One check delayed (field required) | Key check unavailable; learner must reason around it |
| Pressure | None | Customer waiting | Multiple tickets; must prioritise |
| Communication | Not required | One update to write | RSP response and ticket note to write, reviewed against the material |

## Template: GPON fault (NOC or field)

Starting situation elements:
- Ticket text as an RSP or customer would write it (symptom, since when, what they tried)
- Service type (residential FTTP, business)
- Any alarm visible initially (per the material's alarm names)
- Whether adjacent services are mentioned (usually not; the learner must ask)

Tools (phrase in the material's terms):
- ONT status and last-down reason
- ONT RX and TX; OLT RX from the ONT
- Adjacent ONT status on the same splitter or PON
- Alarm history for the PON and OLT
- UNI or Ethernet port state
- MAC learned and VLAN mapping
- Session state (PPPoE or DHCP) as visible from the access side
- Planned works or outages
- Customer confirmation (ONT lights, power, cabling)
- Field tests (power meter at the premises and pit, connector inspection, OTDR) available only after dispatch

Hidden-cause library (choose causes the material covers; examples):

| Cause family | Typical signature in a scenario | Trap for the learner |
|---|---|---|
| Premises power | Dying gasp then offline; customer says ONT lights off | Dispatching field before asking about power |
| Drop or lead-in fibre | LOS, no dying gasp, ONT RX none, adjacent ONTs online | Concluding distribution fault without adjacent status |
| Distribution or splitter | Several ONTs on one splitter down together | Treating as single-premise |
| OLT port or SFP | Whole PON down; OLT TX out of range | Not checking the OLT side |
| Degraded optical | RX in the warning band, intermittent registration, FEC errors | Calling it "in range, no fault" |
| Customer cabling or CPE | ONT online, UNI down or no MAC | Escalating to RSP too early |
| Provisioning mismatch | UNI up, no MAC on expected VLAN; profile mismatch | Looking only at optical |
| RSP side | MAC learned, VLAN correct, no PPPoE session; other customers of same RSP affected | Blaming the access network |

Worked example (medium):

```
SCENARIO: No internet after storm, medium, from <SOP title>

SITUATION
RSP ticket 10:42 ACDT: "Customer at Lot 18 Example Estate reports no internet since last night. Modem shows red light. Customer has rebooted. Please investigate."
NMS shows: ONT offline. Last alarm: LOS 22:17 ACDT previous night.

YOUR TOOLS
ONT status and last-down reason; optical readings; adjacent ONT status; PON alarm history; planned works; customer confirmation; field tests after dispatch.

What do you check first, and why?
```
Hidden facts: last-down reason LOS (no dying gasp); ONT RX none; OLT RX from ONT none; adjacent four ONTs on the same splitter online with normal RX; no planned works; customer confirms ONT power light on, PON light red; field power meter at the premises: no light; at the pit: reading within the material's normal range. Hidden cause: drop fibre damaged (storm). Model path per the SOP: last-down reason, adjacent ONT status, optical readings, planned works, customer confirmation, dispatch field with the right test. Distractor: the "red light" is consistent with both power and fibre issues until the alarm type is read.

## Template: provisioning

Starting situation: a new service order or a change order with the details as the material's order form shows them; a symptom after activation (no service, wrong speed, wrong VLAN). Tools: order details, ONT serial and registration state, profile applied, service port and VLAN mapping, UNI state, MAC learned, session state. Causes the material may cover: wrong ONT serial, profile mismatch, VLAN mapping error, ONT not registered, order not completed, speed profile wrong. Hard variant: two errors, one masking the other.

## Template: customer case

Starting situation: a complaint as the customer wrote or said it, with emotion and missing facts; prior correspondence summary. Tools: ask the customer a question (the coach answers in character from hidden facts), check the case history, check service state as the material allows, consult the material's process. Learner outputs: a case summary and a reply drafted per the material's tone and wholesale rules (the retail relationship is with the RSP). Causes: delayed activation, repeated faults, missed appointment, misdirected complaint that belongs with the RSP. Debrief checks the reply against the material: acknowledgement, what was found, next step and when, who to contact, nothing promised that the material does not allow.

## Running the scenario

- One result per check. If the learner asks for two things, give the first and ask them to choose again.
- Unnecessary checks are allowed; note them for the debrief rather than blocking them.
- If the learner asks for something the material does not provide, answer `NOT COVERED BY THE SUPPLIED MATERIAL` and offer the nearest documented check.
- If the learner concludes early, ask "What evidence supports that?" once; if they confirm, proceed to the debrief.
- Track the move list for the debrief.

## Debrief rules

- WHAT HAPPENED states the hidden cause plainly.
- YOUR PATH marks each move: efficient (on the model path, in a sensible order), unnecessary (did not change the conclusion), missed (required by the material and not done).
- THE MODEL PATH cites the material section for each step.
- WHAT TO REMEMBER is three points, each tied to a mistake or a success in this run.
- NEXT SCENARIO is a variant one lever harder, or the same cause family with a different signature.

## CUSTOMISE: company scenario inputs

- Approved SOPs and fault tables to build from: `<list>`
- Alarm names and thresholds as they appear in the NMS and the standard (so scenarios use the real vocabulary): `<fill in or reference the document>`
- Platforms in use (OLT vendor, ONT models) and typical readings: `<fill in>`
- Estate naming convention for fictional sites: `<e.g. "Example Estate", "Sample Rise">`
- Customer-case process and tone rules document: `<fill in>`
