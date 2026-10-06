# Construction QA checklist: FTTP estate build

Use to name the requirement a defect breaches, to set acceptance criteria in instructions, and to judge whether a section is ready for the next activity. Values are defaults; replace from the company's specification (CUSTOMISE at the end).

## 1. Pits

| Item | Requirement (default) | Evidence |
|---|---|---|
| Type and size per design and pit schedule | P5 drops, P6 distribution closures, P9 feeder and FDH | Photo with lid off; schedule |
| Location | Within 1 m of design position; recorded on as-built if moved | GPS or measured offset |
| Lid | Correct class for location (trafficable, driveway, footpath, verge); fitted level with surface | Photo |
| Interior | Free of silt, water and debris; cables entering through conduit bell ends; slack coiled on cable brackets | Photo |
| Conduit entries | Sealed where required; bell ends fitted; no sharp edges | Photo |
| Identifier | Label or stamp per standard, legible, matching schedule | Photo |

## 2. Conduits and trenching

| Item | Requirement (default) | Evidence |
|---|---|---|
| Size and count | Per design (P50 distribution, P100 feeder, P20 or P25 lead-in); extra conduit where design shows | Photo before backfill |
| Depth of cover | 450 mm footpath and verge, 600 mm road, 300 mm private property | Measurement photo before backfill |
| Bedding and backfill | Sand or approved material around conduit; compacted in layers | Photo; compaction record where required |
| Marker tape | Above conduit along full length | Photo before final backfill |
| Bends | Long sweep bends; no more than two 90 degree bends between pits | Photo; design |
| Continuity and proving | Rodded and roped; mandrel passed for feeder conduits | Proving record per conduit |
| Separation from other services | Per utility and spec; power separation recorded | Photo with tape measure |
| Reinstatement | Surface restored to the authority's standard; no trip hazard | Photo |
| Lead-ins | Conduit to boundary point per lot; sealed end; location recorded | Photo per lot; schedule |

## 3. Hauling

| Item | Requirement (default) | Evidence |
|---|---|---|
| Cable type and count | Per cable schedule (fibre count, loose tube or ribbon) | Drum label photo; schedule |
| Tension and lubrication | Within manufacturer limits; no damage | Haul record |
| Slack | 5 m at pass-through pits, 10 m at closure pits, as spec | Photo |
| Bend radius during and after haul | Not less than cable minimum (default 20 x diameter long term) | Photo |
| Cable ends | Capped and sealed until splicing | Photo |
| Labelling | Cable id at every pit, both ends of every run | Photo |

## 4. Splicing and closures

| Item | Requirement (default) | Evidence |
|---|---|---|
| Closure type | Per design for fibre count and pit size | Photo |
| Splice plan followed | Fibre in, fibre out, tray, position per the splice plan | Splice record |
| Splice loss | Average 0.1 dB, maximum 0.3 dB (OTDR bidirectional average) | OTDR files and summary |
| Protection | Heat-shrink sleeve on every splice, seated in holder | Photo of each tray |
| Tray dressing | Fibres routed with gentle loops, no crossing, lids fitted | Photo |
| Sealing | Base and dome sealed, glands tight, unused ports capped | Photo |
| Mounting | Closure supported on bracket, not lying in silt | Photo |
| Identifier | Closure label per standard | Photo |

## 5. FDH and splitters

| Item | Requirement (default) | Evidence |
|---|---|---|
| Installation | Plumb, secured, on correct plinth or pit; door seals intact | Photo |
| Splitters | Type and count per design; seated; labelled | Photo; schedule |
| Patching | Per port schedule; dressed without strain; dust caps on unused ports | Photo; schedule |
| Feeder termination | Fibres on correct inputs; splice records | Record |
| Power meter at splitter outputs | Within expected range and within 1.5 dB across ports | Test summary |
| Grounding and cabinet earthing (where active) | Per spec | Test record |

## 6. Testing

| Item | Requirement (default) | Evidence |
|---|---|---|
| OTDR | Every feeder and distribution fibre, 1310 and 1550 nm, bidirectional where spec requires; launch and tail leads | Files named by fibre id; summary table |
| Link loss | Within optical budget for longest path; recorded per fibre | Summary |
| Drops | Power meter or ILM at the boundary point or ONT port per premises | Table by lot |
| Results format | Fibre id, direction, length, event list, pass or fail | Spreadsheet or report |
| Failures | Listed with rectification and retest | Defect list |

## 7. As-builts and records

| Item | Requirement (default) | Evidence |
|---|---|---|
| As-built drawings | IFC set marked up with every change; pit positions; cable lengths | Marked-up set |
| Splice records | Per closure, per tray | Records |
| Port schedule as built | Lot to port to fibre | Schedule |
| Proving records | Per conduit | Records |
| Photos | Organised by pit, closure, FDH id | Folder index |
| Material reconciliation | Issued, installed, returned | Table |
| Labelling verification | Field labels match records | Confirmation |

## Readiness gates

| Next activity | Ready when |
|---|---|
| Haul | Conduits proven and roped; pits complete with lids; cable delivered and labelled |
| Splice | Haul complete with slack and labels; splice plan issued; closures delivered |
| Test | Splicing complete; FDH patched; test plan with fibre ids |
| Handover | All P1 to P3 defects closed; tests pass; as-builts and records complete |

## CUSTOMISE: company specification values

- Pit types and lid classes by location: `<fill in>`
- Depth of cover by surface: `<fill in>`
- Conduit sizes and colours: `<fill in>`
- Slack lengths: `<fill in>`
- Splice and link loss acceptance: `<fill in>`
- Test deliverable format and naming: `<fill in>`
- Specification name and revision: `<fill in>`
