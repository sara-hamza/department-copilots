# Case triage checklist

Identify the case type, confirm the service state, draw the wholesale line, then list what is needed to progress. Work through it in that order every time.

## Step 1: case type

| Customer says | Case type | Usually sits with |
|---|---|---|
| "No internet", "lights are red", "LOS light", "box is off" | No service | Network operator access network, unless the modem is the only thing down |
| "Drops out", "keeps disconnecting", "works some of the time" | Intermittent | Could be either; needs ONT history from NOC and session history from RSP |
| "Slow", "not getting the speed I pay for" | Slow or speed | RSP plan and modem first; the network operator if the ONT port or optical level is the cause |
| "Waiting for connection", "technician did not show", "no one has contacted me" | New connection or appointment | Network operator field scheduling if the appointment is ours; RSP if the order has not been placed with us |
| "Damaged my driveway", "pit lid broken", "cable hanging" | Damage or property | Network operator (or the construction contractor); safety first |
| "Rude technician", "no one called back", "been passed around" | Conduct or process complaint | Network operator if about our staff or contractors; note it even if the root issue is RSP |
| "Bill is wrong", "want to change plan", "cancel" | Billing or plan | RSP. We do not bill residents |
| "Which providers can I use", "when will my estate be ready" | Information request | Network operator (availability, RSP list) |

If more than one type applies, record the primary one and note the others; a conduct complaint on top of a no-service case changes the tone, not the technical steps.

## Step 2: service state

Establish from the text, or mark missing:
- Is the service active now, never worked, or stopped working? Since when?
- ONT lights as described by the customer (power, PON, LOS, LAN) and whether the ONT has power.
- Is the modem or router the RSP's or the customer's, and has it been restarted?
- Has anything changed: moved house, new modem, building work, storm, power outage?
- Are neighbours affected (customer may know)?
- What has the RSP told the customer, and when?

## Step 3: the wholesale line

| Network operator owns | RSP owns |
|---|---|
| Lead-in and premises fibre, ONT (the connection box), wall outlet | Modem or router, Wi-Fi, home cabling beyond the ONT |
| PON, splitter, FDH, OLT, aggregation to the RSP NNI | PPP/DHCP session, authentication, IP address |
| Field appointments on the access network | Plan, speed tier, billing, credits, contract |
| Estate readiness, RSP availability list | Customer relationship, order placement with the network operator |

Write the boundary for this case in one or two lines. It drives who is asked for what and what the reply can commit to.

## Step 4: urgency and vulnerability signals

Raise under CUSTOMER SENTIMENT and treat as priority (CUSTOMISE: link to the priority assistance process if one exists):
- Medical equipment, medical alarm, carer dependency.
- Safety: exposed cable, open pit, damaged structure, electrical concern.
- Working from home with income impact, exams, moving date.
- Elderly or isolated resident, language barrier noted.
- Threat to go to the ombudsman, media or social media (not vulnerability, but changes handling and escalation).
- Repeat contact: third or more contact on the same issue.

## Step 5: information needed to progress

| Item | Why it matters | Usually from | Needed for case types |
|---|---|---|---|
| Service address, confirmed (lot and street, estate) | Everything keys off it; wrong address wastes a truck | Customer | All |
| Service or ONT identifier (serial, service ID the RSP uses) | Lets NOC look at the right ONT | RSP, customer (sticker on ONT) | No service, intermittent, slow |
| RSP name | Determines who we talk to and what we can say | Customer | All technical |
| RSP ticket or reference | Links our case to theirs | Customer or RSP | All technical |
| Date and time the problem started | Correlates with outages, works, weather | Customer | No service, intermittent, slow |
| ONT light state and power | First split between power, fibre and session | Customer | No service, intermittent |
| What the customer has already tried (restart modem, restart ONT, different device) | Avoids repeating steps, shows what remains | Customer | Technical |
| What the RSP has already done (session check, modem swap, raised to us) | Decides whether the case should be with us at all | Customer, RSP | Technical |
| Appointment details (date, window, reference, who booked it) | Needed to find and fix a missed or wrong appointment | Customer, field scheduling | Appointment |
| Photos and exact location | Damage and safety cases | Customer | Damage, safety |
| Preferred contact method and hours | So the next update lands | Customer | All |
| Consent to discuss with the RSP or a third party on their behalf | Privacy | Customer | When we will contact the RSP about their service (CUSTOMISE) |

## Step 6: what "progress" looks like per type

| Case type | Progress means |
|---|---|
| No service | NOC has ONT status and optical levels; adjacent ONT status known; field booked if access-side |
| Intermittent | ONT history (drops, LOS events) from NOC; session history from RSP; pattern identified (time of day, weather) |
| Slow | RSP confirms plan and modem test; NOC confirms port speed and optical; customer has done a wired test |
| New connection or appointment | Order located; appointment confirmed or rebooked; customer told the window |
| Damage or property | Made safe; location and photos logged; contractor or field instructed; customer told the rectification timing |
| Conduct or process | Facts logged; acknowledged to the customer; internal review owner named |
| Billing or plan | Customer referred to RSP with a clear explanation; nothing more for us |

## CUSTOMISE

- Case reference format and where it is recorded.
- Priority assistance or vulnerable customer process and who to escalate to.
- Response-time commitments: acknowledge within 1 business day, update every 2 business days (verify).
- Complaints process steps and the external body referenced in final responses (verify wording with compliance).
- Standard RSP contact points for case coordination.
