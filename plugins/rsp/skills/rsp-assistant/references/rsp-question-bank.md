# RSP question bank, by symptom

Pick the block that matches the RSP's claim. Drop any question the paste already answers. Every question must be answerable with a value, a state or yes/no. Numbered so the RSP can reply by number.

## Standard header questions (every ticket)

1. Service identifier (company format) and the address or lot reference the RSP holds for it, to confirm we are looking at the same service.
2. Time the fault was first reported by the end customer and the time it was first observed by the RSP (with zone).
3. Is the fault continuous or intermittent? If intermittent, times of the last three occurrences.
4. Has anything changed on the RSP side for this service in the last 7 days (plan change, re-provision, CPE swap, credentials reset)?

## A. "Customer has PPP session but no internet"

Access side first: ONT online and RX; UNI up; MAC learned; PADI and PADO seen; traffic counters on the service port both directions.

1. Is the PPPoE session currently established on the BNG for this service? Session start time, BNG hostname or id.
2. Which IP address was assigned to the session, and from which pool? Is it public, CGNAT or a walled-garden or quarantine pool?
3. Does the BNG see traffic from the subscriber (packets or bytes in, over the last 15 minutes)? Does it see traffic to the subscriber?
4. Is a default route or the expected routing present for that subscriber? Any policy, filter, quota or suspension applied to the session?
5. BNG session details: MTU negotiated, VLAN tags seen (S-VLAN and C-VLAN), RADIUS attributes returned (framed IP, framed route, service policy), any accounting stop or interim anomalies.
6. Does the CPE show the WAN as up with the same IP? Can the CPE ping the BNG gateway? DNS resolution tested from the CPE?
7. Has the same customer MAC or credential been seen on another session (duplicate session, session not cleared)?

## B. "ONT online but no PPPoE session"

Access side first: UNI state and speed; MAC learned on the correct VLAN; PADI seen at the OLT; PADO seen from the NNI; service-port and S-VLAN mapping.

1. Does the BNG log a discovery (PADI) from the customer MAC in the last hour? Time of the last PADI seen.
2. If PADI was seen, did the BNG send PADO? If PADR arrived, what was the RADIUS result (accept or reject) and the reject reason?
3. Which S-VLAN and C-VLAN does the BNG expect for this service, and which did it see?
4. Credentials: were they recently reset or re-issued? Is the username in the expected realm?
5. Is the BNG serving this S-VLAN healthy (other sessions on the same S-VLAN and NNI establishing normally)?
6. CPE: WAN mode set to PPPoE with the correct VLAN tag (or untagged, as per the service)? CPE log shows PADI sent?

## C. "No sync / ONT offline / LOS" (reported by the RSP)

Access side: ONT state, RX, last-down reason, adjacent ONTs. This is the company's segment; questions to the RSP are limited.

1. Has the customer confirmed the ONT has power and which LEDs are lit (power, PON, LOS)?
2. Has anything been moved, renovated or disconnected at the premises recently?
3. Preferred contact window for a field visit if required (the RSP arranges with the customer).

## D. DHCP / IPoE no lease

1. Does the DHCP server or relay log a discover from the customer MAC? Time and relay agent information (option 82) seen.
2. Was an offer sent? Pool and address. Pool utilisation on that scope.
3. Expected VLAN for DHCP for this service.
4. CPE WAN mode set to DHCP? CPE log shows discover sent?

## E. Slow speed

Access side: bandwidth profile on the ONT or service port vs sold tier; PON utilisation; UNI speed; errors and discards on UNI and service port.

1. What tier is the customer sold, and what tier does the RSP have provisioned toward the network operator for this service?
2. Test method and results: wired to the CPE or Wi-Fi; which speed test server; times; three samples.
3. BNG shaping or policy applied to the session (rate limit, burst, quota state).
4. Upstream utilisation on the RSP side of the NNI at the time of the tests.
5. CPE model and whether it can forward the sold tier (WAN port speed, CPU).
6. Results of a test with a different device wired directly to the ONT UNI, if the RSP can arrange it.

## F. Intermittent drops

Access side: ONT uptime and last-down reasons, RX history, alarms, error counters, PON-wide events.

1. Session start and stop times on the BNG for the last 48 hours, with termination cause (LCP timeout, PADT from CPE, admin reset, BNG reload).
2. Does the drop correlate with any BNG, RADIUS or core event on the RSP side?
3. CPE uptime at the time of the last drop (did the CPE reboot?).
4. Does the customer experience it on wired and Wi-Fi alike?

## G. Voice

1. Where is the voice service hosted: ONT voice port (the network operator-provisioned profile) or RSP ATA or CPE?
2. SIP registration state and last registration time on the RSP platform.
3. Symptom: no registration, one-way audio, no dial tone, call drops? Which direction for one-way audio?
4. NAT or ALG settings on the CPE.

## H. IPTV / multicast

1. Multicast VLAN and groups expected for this service.
2. Does the middleware show the set-top box authenticated?
3. Symptom: no channels, specific channels, pixelation; time pattern.

## I. Multiple services affected

1. List of affected service identifiers with first-observed time for each.
2. Are the affected services on the same BNG, the same S-VLAN or NNI, or spread?
3. Any RSP-side change or event at the onset time?
4. Are unaffected services on the same NNI establishing normally right now?

## WHAT WE WILL DO WHEN ANSWERED: standard branches

| RSP answer | Network operator action |
|---|---|
| Session established, IP assigned, no subscriber traffic at BNG | Check service-port and UNI traffic counters; if traffic leaves the UNI but does not reach the NNI, investigate aggregation; if no traffic at the UNI, raise CPE or LAN with the RSP |
| Session established, traffic both ways at BNG | Access path carrying traffic; remaining issue is routing, policy or DNS on the RSP side; close the access ticket pending RSP confirmation |
| PADI not seen at BNG, but seen at OLT | Investigate S-VLAN mapping and NNI on our side; compare with other sessions on the same S-VLAN |
| PADI seen at BNG, RADIUS reject | Access path confirmed; credentials or RADIUS on the RSP side; close pending RSP |
| PADI not seen at the OLT either | CPE not sending or UNI issue; request CPE check; offer field visit if UNI suspected |
| No answer within the agreed time | Follow up once; then place the ticket in "awaiting RSP" and record the time |

## CUSTOMISE: company wholesale ticket rules

- Agreed response time for RSP information requests: `<e.g. 4 business hours>` (verify)
- Required fields in a wholesale ticket: `<fill in>`
- Where PPPoE discovery can be observed on the company's side: `<fill in>`
