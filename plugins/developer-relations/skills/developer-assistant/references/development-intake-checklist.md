# Development intake checklist

Walk every field. Mark known (with source), partial, or missing. Missing fields become questions; owed fields become open items. Lead times and specification names are defaults marked CUSTOMISE.

## Intake fields

| Topic | Field | Why delivery needs it | Typical source |
|---|---|---|---|
| Development | Name, location, local government area, developer entity | Agreement, addressing, council liaison | Developer, plan title block |
| Development | Type: greenfield detached, townhouse, MDU/apartments, mixed, retirement, commercial | Design architecture (FDH vs in-building), ONT type | Plan |
| Premises | Total lots or dwellings; by stage; by dwelling type | Splitter and fibre count design, equipment order | Lot schedule, plan |
| Premises | Future stages or adjacent land the developer controls | Capacity planning at the FDH and feeder | Developer |
| Staging | Number of stages, sequence, lots per stage | Design sequencing, staged RFS | Stage plan |
| Staging | Civil start and civil completion per stage | Haul cannot start until civil handover is accepted | Developer programme |
| Dates | Title registration date per stage | Addresses and lot identifiers for provisioning | Developer, surveyor |
| Dates | First settlement date per stage | Sets the RFS target and the latest civil handover | Developer sales |
| Dates | Builder handover or occupancy certificate dates (MDU) | In-building commissioning | Developer, builder |
| Civil | Who designs and builds pit and pipe; contractor appointed | Specification compliance, acceptance inspection scheduling | Developer |
| Civil | Specification they are building to (CUSTOMISE: company civil specification name and version) | Rework risk | Developer, civil consultant |
| Civil | Civil drawings received (version, date, format) | Design input | Civil consultant |
| Civil | Lead-in conduit to each lot boundary included; property entry point requirements passed to builders | Premises connection at move-in | Developer, builder pack |
| Civil | Shared trenching with power, water, gas: alignment and separation | Design and access | Civil consultant |
| Siting | FDH site or comms room location, size, which stage it sits in | Must be available before Stage 1 RFS | Plan, developer |
| Siting | Power supply to the FDH or comms room: who arranges, when, metering | Active equipment cannot run without it | Developer, power authority |
| Siting | Tenure: easement, lease, licence over the site; access rights | Legal access for operation and maintenance | Developer, legal |
| Siting | Backhaul or feeder route into the estate: entry point, existing company network nearby, third-party conduits | Connectivity to the wider network | Internal engineering, developer |
| Easements | Service easements on lots; road reserve dedication timing | Where fibre can legally run | Plan, surveyor |
| Access | Site access rules, inductions, contact for site entry | Field crews | Developer site manager |
| Design | Lot layout with lot numbers; street names approved; addressing | Design and provisioning | Surveyor, council |
| Design | Any special requirements: gated community, bulk services, CCTV or estate Wi-Fi, commercial tenancies | Architecture and commercial | Developer |
| Commercial | Agreement status (none, draft, signed), date, term | What we are obliged to do and by when | BD, legal |
| Commercial | Commitments made to the developer (dates, scope, contributions) and by whom | Delivery must honour or renegotiate | BD notes |
| Commercial | Developer's commitments to buyers (speed, RSP, move-in readiness) | Expectation management | Developer marketing |
| Contacts | Developer roles: development manager, project manager, civil consultant, sales, site manager | Who to ask what | Developer |
| Contacts | Internal roles: BD owner, delivery lead, design lead | Handover | Internal |

## Derived dates (CUSTOMISE lead times)

| From | Derive | Default lead time |
|---|---|---|
| First settlement per stage | RFS target = settlement minus 4 weeks (RSP onboarding and first connections) | 4 weeks |
| RFS target | Latest civil handover = RFS minus 10 to 14 weeks (haul, splice, FDH, test) | 12 weeks |
| Latest civil handover | Latest civil drawings final = civil handover minus 8 weeks (design lead time) | 8 weeks |
| Stage 1 RFS | FDH site and power must be available = Stage 1 RFS minus 6 weeks | 6 weeks |

Show every derived date as `derived: <settlement> minus <n> weeks = <date>`. If the developer's civil programme is later than the derived latest civil handover, raise a RISK with the gap in weeks.

## What counts as an open item

An open item is something a named side owes before a field can be marked known or a milestone reached. Tests:
- Is there a deliverable (document, decision, date, site, approval)? If not, it is a question, not an open item.
- Who owes it: us, the developer, or a third party (power authority, council, surveyor)?
- By when: the date the dependent milestone needs it, derived if necessary and labelled.

Typical open items: civil drawings final; pit and pipe specification acceptance; FDH site confirmed and power applied for; easement documents; title registration date confirmed; builder pack issued with entry-point requirements; agreement executed; site induction arranged.

Flags: STALE (no update in 14 days, CUSTOMISE), OVERDUE (needed-by passed), OWNERLESS, NO DATE.

## Risks to recognise in the input

| Signal | Risk |
|---|---|
| Civil handover inside 12 weeks of first settlement | RFS slips past settlement; residents move in without service |
| FDH or comms room in a later stage than the first settlements | Active equipment cannot be commissioned for Stage 1 |
| Pit and pipe built to another specification or without inspection | Rework, acceptance dispute |
| No power application lodged for the FDH site | Long lead with the power authority; RFS exposed |
| Developer promised a named RSP not on the network | Resident complaints at move-in |
| Title registration delayed | Addresses unavailable; provisioning and RSP onboarding wait |
| Lead-in conduits not included in builder pack | Premises connections delayed at move-in |

## CUSTOMISE

- Civil specification name and version; who performs acceptance inspections.
- Lead times above; replace with the delivery team's current figures.
- Siting requirements document (cabinet footprint, clearances, power rating).
- Stale threshold (14 days default).
- Internal role names for BD owner, delivery lead, design lead.
