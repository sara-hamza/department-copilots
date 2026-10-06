# Design review checklist: FTTP / GPON greenfield estate

Walk in order. Cite the sheet for every finding. Values marked (default) are sensible industry defaults; replace them from the company's design standard (see CUSTOMISE at the end).

## 1. Architecture and capacity

| Check | Pass when | Finding severity if not |
|---|---|---|
| Premises count on the cover sheet matches the lot schedule and the developer's staging plan | Same number on every sheet that states it | CRITICAL |
| Split ratio stated and consistent (1:32 default; 1:64 or cascaded 1:4 then 1:8 only where the standard allows) | Stated once, applied everywhere | CRITICAL |
| PON count = ceiling(premises / ratio) plus growth allowance | Matches FDH splitter schedule | CRITICAL |
| OLT or POI port count covers PON count for all stages, not just stage 1 | Stated | WARNING |
| Optical budget calculated for the longest and shortest path (default Class B+ 28 dB; C+ 32 dB), with splitter loss (1:32 about 17.5 dB), connector and splice losses, and margin (3 dB default) | Shown on a sheet or in notes | CRITICAL if absent on long routes, WARNING otherwise |
| Future stages shown with the capacity reserved for them | Indicated | WARNING |

## 2. FDH and splitters

| Check | Pass when | Severity |
|---|---|---|
| FDH location shown with pit or cabinet reference, access and power if active | Shown | CRITICAL if no location |
| FDH size (splitter slots, distribution ports) covers all stages | Schedule shows slots used vs available | CRITICAL |
| Splitter capacity vs service count: splitter output ports >= premises served by that FDH plus spare (10% default) | Table shows the comparison for each FDH | CRITICAL |
| Splitter input fibres allocated from the feeder with the feeder fibre number shown | Port schedule present | WARNING |
| Splitter type and connector type match the BOM (for example SC/APC) | Match | BOM |
| Distribution port allocation lists every premises against a port | Complete | CRITICAL if lots missing |

## 3. Feeder (OLT / POI to FDH)

| Check | Pass when | Severity |
|---|---|---|
| Feeder cable fibre count >= splitter inputs for all stages plus spare (minimum 25% default or 4 fibres, whichever is greater) | Count shown and reconciles | CRITICAL |
| Route shown pit to pit with cable lengths | Shown | WARNING |
| Diverse feeder route where the standard or the contract requires it | Shown or stated not required | WARNING |
| Splice points shown with closure type and tray count | Shown | WARNING |
| Feeder fibres identified by colour code or number on the splice plan | Shown | WARNING |

## 4. Distribution (FDH to pits)

| Check | Pass when | Severity |
|---|---|---|
| Every distribution cable shows fibre count and route | Shown on the sheet or a schedule | CRITICAL |
| Fibre allocation per pit: fibres allocated = drops served from that pit plus spare | Allocation table present | CRITICAL |
| Cable count at each splice point reconciles (in = out plus terminated plus spare) | Reconciles | CRITICAL |
| Spare at distribution level meets the standard (10% default, minimum 2 fibres per cable) | Meets | WARNING |
| Closure type and size suits the fibre count and the pit size | Suits | WARNING |
| Multi-port terminals or drop closures sized for the lots they serve | Sized | WARNING |

## 5. Drops and lead-ins

| Check | Pass when | Severity |
|---|---|---|
| Every lot has a drop allocation (fibre and port) | Complete | CRITICAL |
| Lead-in conduit shown per lot to the property boundary (P20 or P25 default) with a pit or boundary point | Shown | WARNING |
| Lead-in length within the standard maximum (default 100 m) or a pit added | Within | WARNING |
| MDU and mixed-use lots have a riser or internal distribution design, not a single drop | Shown | CRITICAL for MDU |
| Corner lots, battle-axe lots and lots facing reserves have a defined boundary point | Shown | WARNING |
| Premises with no drop (parks, reserves, substations) are listed as excluded | Listed | WARNING |

## 6. Pits and conduits (civil)

| Check | Pass when | Severity |
|---|---|---|
| Pit size suits the cables and closure (defaults: P5 for drops and small closures, P6 for distribution closures, P9 for FDH feeder and large closures) | Suits | WARNING |
| Pit spacing and haul distance within the standard (default maximum 250 m straight; reduce with bends) | Within | WARNING |
| Conduit size and count per route (default P50 for distribution, P100 for feeder; two conduits minimum on feeder routes) | Shown | WARNING |
| Conduit fill within limit (default 40% by area) | Within | WARNING |
| Bend radius and number of bends between pits within the standard (default no more than two 90 degree bends) | Within | WARNING |
| Road crossings shown with method (bore or trench) and depth | Shown | WARNING |
| Shared trench with power or other utilities shows separation and the utility's requirements | Shown | CRITICAL if shared with HV and no separation |
| Pits in driveways, trafficable areas or near water flagged with the correct lid class | Shown | WARNING |

## 7. Labelling

| Check | Pass when | Severity |
|---|---|---|
| Every FDH, pit, cable, splitter and port has an identifier in the standard format | Present on the schedule and drawings | WARNING |
| Identifiers unique across the project | No duplicates | CRITICAL if duplicates |
| Label format consistent across all sheets | Consistent | WARNING |
| Drop labels link lot number to FDH port | Linked | WARNING |

## 8. Fibre counts and spare

| Level | Spare default | Finding if lower |
|---|---|---|
| Feeder | 25% or 4 fibres, whichever is greater | CRITICAL below 12.5%, otherwise WARNING |
| Distribution | 10%, minimum 2 per cable | WARNING |
| Drop | 1 spare fibre per premises on 2-fibre drops; or as standard | WARNING |
| FDH splitter ports | 10% of ports free after all stages | WARNING |

Reconciliation rule: at every splice or termination point, fibres in = fibres out + fibres terminated + fibres spare. Show the arithmetic in the review when it fails.

## 9. Documentation

| Check | Pass when | Severity |
|---|---|---|
| Every sheet has number, title, revision, date, scale, north arrow and legend | Present | WARNING |
| Revision consistent across the set, or a revision schedule explains differences | Consistent | CRITICAL if a superseded sheet is in the set |
| Applicable standard cited | Cited | WARNING |
| Design notes explain assumptions (staging, growth, excluded lots) | Present | WARNING |
| Splice plan, port schedule and BOM are present | Present | CRITICAL if any missing at IFC stage |

## Severity rules

- CRITICAL: will cause rework, a service that cannot be delivered, or a safety or compliance breach. Includes any count mismatch between sheets.
- WARNING: will cause delay, cost or operational pain; or a required item is absent but can be added without redesign.
- BOM: drawing vs BOM differences (reported in the BOM section, not duplicated under CRITICAL).
- QUESTION: the design is silent or ambiguous; cannot be judged without the designer's answer.

## CUSTOMISE: company design standard values

Replace the defaults above with the real values and cite the standard:

- Standard split ratio: `1:32` (verify)
- Optical class and budget: `Class B+ 28 dB` (verify); margin `3 dB` (verify)
- Feeder spare: `25%` (verify); distribution spare: `10%` (verify)
- Pit types and naming: `P5 / P6 / P9` (verify against the company pit schedule)
- Conduit sizes: `P50 distribution, P100 feeder` (verify)
- Maximum lead-in length: `100 m` (verify)
- Label format: `<estate>-<FDH>-<cable>-<fibre>` (verify)
- Design standard document name and revision: `<fill in>`
