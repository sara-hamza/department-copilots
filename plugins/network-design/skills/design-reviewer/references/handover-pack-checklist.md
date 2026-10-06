# Handover pack checklist: design to construction / operations

Use for a design handover (IFC pack to construction) and for an as-built handover (construction to operations). Mark each item PRESENT (cite the file or sheet), MISSING, or PARTIAL (say what is incomplete). An item named in a transmittal but not in the pack is MISSING.

## A. Project and revision control

| Item | Expect | Common gap |
|---|---|---|
| Transmittal or pack index listing every document with revision and date | One list | No index; cannot tell if the pack is complete |
| Cover sheet with project, stage, premises count, design authority | One sheet | Premises count differs from the lot schedule |
| Revision history with reason for each revision | On each sheet or a register | Superseded sheet still in the pack |
| Design standard and revision cited | Stated | Not cited |
| Design approval or IFC sign-off (name, date) | Recorded | Draft stamp still on sheets |

## B. Drawings (design or IFC)

| Item | Expect | Common gap |
|---|---|---|
| Locality and estate overview with staging boundaries | 1 sheet | Staging not shown |
| Civil layout: pits, conduits, routes, crossings, with sizes | Per stage | Conduit sizes missing on some routes |
| Fibre layout: feeder, distribution, drops with fibre counts | Per stage | Counts missing on short cables |
| FDH layout and splitter schedule | Per FDH | Stage 2 slots not shown |
| Splice plan per closure (tray, fibre in, fibre out, port) | Per closure | Only FDH splices shown |
| Port schedule: lot to FDH port to feeder fibre | Complete | Lots missing |
| Lead-in detail per lot type (standard, corner, battle-axe, MDU) | Standard details present | MDU riser missing |
| Standard details referenced (pit, trench, bedding, marker) | Present or referenced | Referenced details not in pack |
| Legend and symbol key | Present | Symbols used that are not in the legend |

## C. Schedules and BOM

| Item | Expect | Common gap |
|---|---|---|
| BOM by stage with item codes, quantities and units | Spreadsheet | Totals only, no stage split |
| Cable schedule (id, type, count, from, to, length) | Spreadsheet or sheet | Lengths missing |
| Pit schedule (id, type, lid class, location) | Spreadsheet or sheet | Lid class missing in trafficable areas |
| Lot schedule with premises type and status (lot, address if known, MDU count) | Spreadsheet | Excluded lots not listed |
| Optical budget calculation for longest and shortest path | Sheet or note | Absent |

## D. Approvals and third parties

| Item | Expect | Common gap |
|---|---|---|
| Developer approval of the design or the pit and pipe layout | Letter or email record | Verbal only |
| Council or road authority permits for crossings and verge works | Permit references | Not yet applied |
| Shared trench agreement and separation drawings if co-located with power | Document | Separation not confirmed |
| Easement or access arrangements for FDH and feeder route | Document or note | Easement not registered |
| Dial-before-you-dig or equivalent utility search results for the route | Results attached | Expired results |

## E. As-built handover (construction to operations) additional items

| Item | Expect | Common gap |
|---|---|---|
| As-built drawings marked up from the IFC set with changes highlighted | Full set | Only changed sheets |
| Splice records as installed (per closure, per tray) | Complete | Photos only |
| OTDR results for every feeder and distribution fibre, both directions where required | Files plus summary | One direction; missing fibres |
| Power meter or ILM results per drop or per splitter port | Summary table | Spot checks only |
| Pit and conduit proving results (rodding or mandrel) | Per conduit | Not recorded |
| GPS or GIS export of pits, FDH and route | File | Missing |
| Photos: pit interiors, closures, FDH, labels | Organised by id | Unlabelled bulk upload |
| Defect list from QA inspection with close-out status | List | Open defects at handover |
| Material reconciliation (BOM vs installed vs returned) | Table | Absent |
| Labelling verification (field labels match the schedule) | Confirmation | Not checked |

## Status rules

- PRESENT: the content is in the pack and matches the revision on the index.
- PARTIAL: the document exists but is incomplete (fewer sheets, missing stages, missing fibres, draft stamp). Say what is missing.
- MISSING: not in the pack.
- READY FOR HANDOVER is No if any item in sections A, B or C is MISSING at IFC stage, or any item in section E is MISSING at as-built stage. Name the single highest-impact blocker.

## Output template

```
HANDOVER PACK
PACK SUMMARY
<project, stage, revision, date, who supplied it>

CHECKLIST
Item | Status | Where | Note
Transmittal index | PRESENT | Transmittal_R3.pdf | lists 14 docs, pack has 13
Splice plan | PARTIAL | Sheets 11-13 | closures C7 to C9 missing
OTDR results | MISSING | - | request from contractor

MISSING OR PARTIAL
1. <item> - <usually supplied by> - <what exactly is needed>

REVISION AND CONSISTENCY ISSUES
1. <sheet n at Rev B, index says Rev C>

READY FOR HANDOVER: No - splice plan incomplete (closures C7 to C9)
```

## CUSTOMISE: company handover requirements

- Mandatory documents at IFC per company process: `<fill in>`
- Mandatory as-built deliverables and file formats (for example GIS export format): `<fill in>`
- Who signs the design approval and the as-built acceptance: `<fill in>`
- Test result thresholds for acceptance (splice loss, link loss): `<e.g. splice <= 0.1 dB average, link within budget>` (verify)
