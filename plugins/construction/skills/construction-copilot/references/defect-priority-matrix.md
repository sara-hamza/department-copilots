# Defect priority matrix

Order of severity: safety > service-affecting > compliance > cosmetic. Classify by the highest row the defect matches. Civil and fibre defects have separate rows because the same description carries different consequences. Timeframes are defaults; replace from the contract (see CUSTOMISE).

## Severity definitions

| Severity | Meaning | Default rectification | Default evidence to close |
|---|---|---|---|
| P1 Safety | Immediate risk to the public, workers or property | Make safe within 2 hours, rectify within 24 hours | Photo of the made-safe state, then photo of the rectified state, both time-stamped |
| P2 Service-affecting | Prevents a service from being delivered or will fail in service; blocks a milestone | Rectify within 5 working days or before the milestone, whichever is sooner | Photo plus test result (OTDR, power meter, mandrel or rodding) as applicable |
| P3 Compliance | Breaches the specification or standard but service works; will be rejected at handover | Rectify within 10 working days or before handover | Photo and, where a count or measurement is involved, the corrected record |
| P4 Cosmetic | Appearance, tidiness or minor documentation; no functional effect | Rectify before practical completion | Photo or corrected document |

## Civil defects

| Defect as described | Severity | Why | Required rectification |
|---|---|---|---|
| Open pit or trench without barrier or cover in a public area | P1 | Fall or traffic hazard | Barrier or cover now; lid fitted |
| Pit lid missing, broken, or wrong class in a trafficable area | P1 in trafficable areas, P3 elsewhere | Collapse under load | Correct class lid fitted |
| Trench not reinstated, trip hazard on footpath | P1 | Public injury | Temporary reinstatement now; permanent within 24 h |
| Shared trench with power without required separation | P1 | Electrical and future-works hazard | Stop work on that section; rectify separation; record |
| Services struck or damaged (water, gas, power, comms) | P1 | Immediate hazard and outage | Notify the utility; make safe; incident report |
| Conduit crushed, deformed or failed mandrel | P2 | Cable cannot be hauled or will be damaged | Replace section; re-prove with mandrel |
| Pit undersized for closure or cable count | P2 | Closure cannot be installed correctly; bend radius will fail | Replace with correct pit size |
| Conduit not continuous between pits, no draw rope | P2 | Haul cannot proceed | Rod and rope; repair the break |
| Depth of cover below minimum (default 450 mm footpath, 600 mm road, 300 mm private property) | P3, P2 if under a road | Future damage | Re-lay or add mechanical protection per the spec |
| Pit position differs from design by more than tolerance (default 1 m) and not recorded | P3 | As-built and future access | Record on as-built; relocate if it affects a lot's lead-in |
| Marker tape or marker posts missing | P3 | Future strike risk | Install |
| Pit interior with silt, water or debris over cables | P3, P2 if cables submerged in a closure pit | Closure and cable damage over time | Clean; fix drainage or seal |
| Bedding or backfill material incorrect | P3 | Conduit damage over time | Re-lay affected section |
| Reinstatement surface finish poor, cosmetic only | P4 | Appearance | Re-finish |
| Site left untidy, offcuts, spoil | P4 | Appearance and developer relations | Clean |

## Fibre defects

| Defect as described | Severity | Why | Required rectification |
|---|---|---|---|
| Bare fibre or cable exposed above ground in a public area | P1 | Laser exposure and public contact | Secure and cover now; terminate or protect |
| Splice loss above threshold (default 0.1 dB average, 0.3 dB maximum) | P2 | Budget failure, service fault later | Re-splice; retest |
| Link loss above budget or OTDR event above threshold | P2 | Service cannot be delivered | Locate and rectify; retest both directions |
| Fibre allocated to wrong port or lot (port schedule mismatch) | P2 | Wrong premises connected; rework at activation | Repatch or re-splice per schedule; update records |
| Closure unsealed, ports open, gland loose | P2 | Water ingress; outage within months | Reseal; inspect tray for moisture |
| Splice protection sleeve missing, fibre unsupported in tray | P2 | Fibre break in service | Re-dress tray with protection |
| Bend radius below minimum at pit, closure or FDH | P2 if loss shown, P3 if not | Macrobend loss and long-term failure | Re-dress; retest at 1550 nm |
| Cable not labelled, or label does not match schedule | P3 | Cannot be maintained; handover rejected | Label per standard |
| FDH door seal damaged, unused ports uncapped, patch cords strained | P3 | Contamination and failure later | Rectify; clean connectors |
| Cable slack not stored per spec (default 5 m at pits, 10 m at closures) | P3 | Future repairs impossible | Re-coil or replace section |
| Test results missing, one direction only, or not matched to fibre ids | P3 (P2 at handover) | Cannot accept | Retest; resubmit |
| As-built markup missing changes seen on site | P3 | Records wrong; future faults longer | Correct as-built |
| Minor label legibility, faded tray markings | P4 | Appearance | Replace label |

## Blocker priority

| Priority | Definition | Examples |
|---|---|---|
| HIGH | Stops a milestone, or stops work for more than one stage or more than 50 premises (default) | No permit for the road crossing on the feeder route; developer has not handed over the civil corridor; FDH not delivered; power to an active cabinet not available |
| MED | Delays one stage that still has float, or fewer than 50 premises | Pit and pipe not proven on one street; splicing crew unavailable for a week; wet ground on one section |
| LOW | Nuisance with a workaround | Access gate key; material delivery split; minor design query |

Common blocker owners and what clears them:

| Owner | Typical blocker | What clears it |
|---|---|---|
| Developer | Civil corridor not ready; lot boundaries changed; shared trench not open | Written handover of the corridor; revised plan |
| Council or road authority | Permit, road opening, traffic management | Permit issued with conditions |
| Utility | Power connection, clearance from assets | Connection date; clearance letter |
| Network operator design | Design change, missing detail, port schedule | Revised IFC sheet |
| Network operator supply | FDH, splitters, cable, pits not delivered | Delivery date with tracking |
| Contractor | Crew, equipment, subcontractor, QA records | Resource plan; records submitted |
| Weather and ground | Wet, flood, rock | Dry days; revised method |

## Risk triggers for progress summaries

Flag a RISK when the input shows: more than two days of weather delay in the period; a permit expiring; a milestone within two weeks with blocked predecessors; materials with no delivery date; the same blocker reported in two consecutive periods; any P1 defect open; test results not submitted for a completed section.

## CUSTOMISE: company contract and specification values

- Rectification timeframes per severity from the contract: `<fill in>`
- Depth of cover minimums: `<fill in from spec>`
- Splice and link loss acceptance: `<fill in>`
- Slack storage lengths: `<fill in>`
- Pit position tolerance: `<fill in>`
- Premises threshold for HIGH blockers: `50` (verify)
- Specification document name and revision: `<fill in>`
