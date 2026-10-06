# Field test sequence: decision tree from the premises to the FDH

Cheapest test first. Each node gives one test and the branches. Do not skip a node because a later test seems more decisive; the cheap tests also protect against wasted pit entries.

## Node 0: before leaving the vehicle

1. What does the NOC or ticket say: ONT state (LOS, dying gasp, offline, online with no service), last RX, adjacent ONT status, OLT port state, any planned works.
2. If adjacent ONTs on the same splitter are down, go to Node 6 (FDH) and tell the NOC; do not start at the premises.
3. If the ticket says dying gasp, start at Node 1 and expect a power issue.
4. If ONT is online with no service, the fault is likely not optical: check the ONT RX once at Node 1, then report to the NOC for session and provisioning checks.

## Node 1: ONT, power and patch lead (premises)

Test: observe LEDs (power, PON, LOS, LAN); read RX at the ONT if the ONT or a meter on the ONT port gives it.

| Result | Next |
|---|---|
| No power LED | Power supply, outlet, customer power. Fix or report; stop fibre testing |
| Power on, PON steady, LOS off, RX in range | Optical path is fine. Report to NOC: session, provisioning or CPE. Stop |
| LOS on or PON flashing, RX below range or no light | Clean and inspect the ONT port and patch lead connectors; reseat; reread |
| Reading improves to range after cleaning | Dirty connector was the fault. Record before and after. Close with a connector clean |
| Still below range or no light | Node 2 |

## Node 2: premises fibre (wall outlet to boundary point)

Test: power meter at the wall outlet (network side of the patch lead), then at the boundary point or external termination.

| Result | Next |
|---|---|
| Outlet reading in range but ONT port reading was not | Patch lead. Replace, remeasure, close |
| Outlet reading below range, boundary reading in range | Premises fibre or outlet. VFL from the outlet to find the bend or break; inspect wall outlet bends and cable ties |
| Both below range or no light | Node 3 |
| No boundary point accessible | Node 3 from the pit side |

## Node 3: drop / lead-in (boundary to pit)

Test: power meter at the pit end of the drop (unmate at the multiport or closure if the design allows), 1490 nm.

| Result | Next |
|---|---|
| Pit end in range, boundary end not | Loss is in the drop or lead-in. VFL from the pit end; look for crush, tight bend in the conduit, water in the boundary pit. OTDR from the pit end at 1310 and 1550 if the VFL finds nothing |
| Pit end below range or no light, adjacent drops at the same pit in range | The drop's port or pigtail at the multiport or closure. Clean, inspect, reseat; then OTDR |
| Pit end below range and adjacent drops also low | Node 4 |
| Cannot unmate without affecting others | OTDR from the premises end with a launch lead, then Node 4 if the trace is clean to the pit |

## Node 4: distribution (pit to FDH)

Test: OTDR from the distribution pit toward the FDH on the affected fibre (with NOC agreement if the OLT is live, or on a spare fibre to prove the cable); check adjacent ONTs on the same distribution cable.

| Result | Next |
|---|---|
| Adjacent ONTs on this cable online, OTDR clean | Fault is in this fibre only: the splice for this fibre in the closure. Open the closure, inspect the tray, re-splice |
| OTDR shows a non-reflective event at a closure distance | Splice or bend in that closure. Inspect, re-splice or re-dress the tray |
| OTDR shows end of fibre short of the FDH | Cable damage at that distance. Locate the pit or route point; escalate to Construction if civil damage |
| Several ONTs on this cable down | Cable or closure fault. Escalate to Field supervisor and NOC with the OTDR distance; Node 5 for FDH side confirmation |

## Node 5: FDH and splitter

Test: at the FDH, power meter on the splitter output port for this service, and on a neighbouring port of the same splitter.

| Result | Next |
|---|---|
| This port low, neighbour port in range | Port, pigtail or patch for this service. Clean, inspect, repatch. Confirm the port allocation against the schedule |
| Both low or no light | Splitter input or feeder. Node 6 |
| Both in range | Distribution fibre between FDH and pit. Back to Node 4 with the FDH end |
| Service found patched to the wrong port | Repatch per schedule, record it, tell the NOC |

## Node 6: feeder and OLT

Test: nothing to do in the field without NOC. Report to the NOC: splitter input reading, FDH identifier, splitter identifier, how many ports affected.

| NOC reports | Next |
|---|---|
| OLT TX normal, OLT port operational | Feeder fibre or splitter input. OTDR on the feeder fibre from the FDH toward the POI with NOC agreement |
| OLT port down or SFP fault | NOC or Engineering fix. Stand by for a re-test |
| Planned works on the PON | Stop; close the visit as "affected by planned works" |

## Escalation triggers

| Trigger | Escalate to | Send |
|---|---|---|
| More than one premises affected on the same splitter or cable | NOC and Field supervisor | FDH, splitter, cable id, readings, OTDR distance |
| Civil damage, crushed conduit, pit collapse, water in pit affecting cables | Construction | Pit id, photos, what is affected |
| Fault in the feeder or OLT | NOC | Splitter input reading, FDH, PON |
| Cannot access the premises, boundary point or pit (locked, unsafe, permit) | Field supervisor and ticket owner | What is blocked and what access is needed |
| ONT online with good RX but no service | NOC (session, provisioning, RSP) | ONT RX, LEDs, serial, time observed |
| Readings fine everywhere, fault intermittent | NOC for history, Field supervisor | All readings with times; request alarm history |

## Minimum readings to record at every visit

1. ONT RX at the ONT port, 1490 nm, with time.
2. Reading at the boundary point or outlet if tested.
3. Reading at the pit end of the drop if tested.
4. ONT serial and LED state at arrival and at departure.
5. Adjacent ONT status as told by the NOC or observed.

## CUSTOMISE: company field process

- Who the technician calls before OTDR testing on a live PON: `<NOC desk>` (verify)
- Whether drops can be unmated at the multiport without a NOC call: `<fill in>`
- Standard materials carried for connector clean, patch lead swap, splice: `<fill in>`
- Supervisor and Construction escalation contacts: `<fill in>`
