# Optical interpretation: RX ranges, power meter points and OTDR signatures

Defaults are common GPON Class B+ / C+ working values. Replace with the company's field standard (see CUSTOMISE).

## 1. ONT and OLT receive levels

| Measurement | Good | Warning (investigate) | Fault |
|---|---|---|---|
| ONT RX, 1490 nm downstream, at the ONT port | -8 to -24 dBm | -24 to -27 dBm | below -27 dBm, or no light / LOS |
| OLT RX from ONT, 1310 nm upstream (from NOC) | -8 to -26 dBm | -26 to -28 dBm | below -28 dBm |
| ONT TX, 1310 nm | +0.5 to +5 dBm | outside | outside with RX fine: ONT laser |
| Splitter output at the FDH, 1490 nm (1:32) | about 17 to 18 dB below the OLT TX; typically -12 to -16 dBm | more than 1.5 dB below neighbouring ports | no light: splitter input or feeder |

Reading rules:
- RX stronger than -8 dBm suggests a wrong splitter ratio or missing attenuation; it can saturate the receiver and cause errors with a "good" number.
- A reading that moves by more than 1 dB while the connector is wiggled points at the connector, not the fibre.
- Dirty connectors and temperature move readings about 1 dB. Treat borderline as warning, not fault, until the connector is cleaned and remeasured.
- Compare with the installation record and with adjacent ONTs on the same splitter. All shifted: fault is upstream of the splitter. One shifted: drop or premises.

## 2. Power meter along the path

Measure at 1490 nm from the network side, moving outward. Expected loss per element (defaults):

| Element | Typical loss | Suspect if |
|---|---|---|
| Mated connector pair (SC/APC), clean | 0.2 to 0.5 dB | above 0.75 dB |
| Fusion splice | 0.05 to 0.1 dB | above 0.3 dB |
| Mechanical splice | 0.2 to 0.5 dB | above 0.75 dB |
| Fibre, G.652 / G.657, 1490 nm | about 0.25 dB per km | drop of several hundred metres should cost under 0.2 dB |
| 1:32 splitter | 17 to 18 dB | above 19 dB |
| 1:8 splitter | 10 to 11 dB | above 12 dB |
| 1:4 splitter | 7 to 7.5 dB | above 8.5 dB |

Path test logic: the reading at the ONT port should be within about 1 dB of the reading at the boundary point, which should be within about 1 dB of the reading at the pit side of the drop. A step larger than 1.5 dB between two points places the loss in that segment.

## 3. OTDR event signatures

Use a launch lead. Test at 1310 nm and 1550 nm where possible; 1550 nm shows bends that 1310 nm hides. Distances are from the OTDR port; subtract the launch lead.

| Signature on the trace | Reads as | Typical cause | Confirm by |
|---|---|---|---|
| Reflective event (spike) with loss | Connector or mechanical splice | Dirty, damaged or unmated connector; mechanical splice | Clean and inspect the connector at that distance; remeasure |
| Reflective event, very high reflectance, then trace drops to noise | End of fibre (open connector or clean break) | Unmated connector, cut cable, missing patch | Check the expected length: if the end is short of the known route length, it is a break or an unmated point at that distance |
| Non-reflective event (step down, no spike) | Fusion splice or bend | Splice loss, macrobend, crush | Compare 1310 vs 1550: loss much larger at 1550 is a bend; equal at both is a splice |
| Non-reflective loss larger at 1550 nm than 1310 nm | Macrobend | Tight bend in a pit, closure, tray or wall outlet; cable tie too tight; lead-in crushed | Inspect the location at that distance; relieve the bend and remeasure |
| Non-reflective loss equal at both wavelengths | Splice or crush | Poor fusion splice, crushed cable | Re-splice or replace the section |
| Gradual slope steeper than about 0.35 dB/km at 1310 nm | Fibre attenuation high | Wrong fibre, stressed cable, water ingress over a length | Compare to the as-built; check pits for water |
| "Ghost" reflective event at a multiple of a real event distance | Measurement artefact | Strong reflection echo | Change pulse width or range; it will move or vanish |
| Dead zone hiding the first tens of metres | Launch lead too short or absent | n/a | Use a launch lead of 100 m or more |
| Fibre end at the expected length, clean reflection, no abnormal events, but ONT still LOS | Path is physically fine | Wrong fibre or port at the FDH, wrong splitter port, ONT fault | Verify port allocation; swap ONT |

Reflectance guide (defaults): APC connector better than -55 dB; UPC about -45 to -50 dB; a reading worse than -35 dB usually means dirty, damaged or air gap.

## 4. Quick patterns

| Technician reports | Most likely | Next step |
|---|---|---|
| ONT Offline, 1490 RX -30.1 dBm, OLT port operational, adjacent ONTs online | Drop, lead-in or premises fibre | Power meter at the boundary point, then pit side of the drop |
| ONT LOS, no light at ONT port, adjacent ONTs online | Break or unmated point between pit and ONT | VFL from the ONT end, then OTDR from the pit |
| ONT LOS, adjacent ONTs on the same splitter also LOS | Distribution cable, closure or splitter | Check the FDH port and splitter output; escalate to NOC for OLT TX |
| RX fine at pit, -3 dB worse at ONT port | Premises fibre or outlet connector | Clean the outlet connector, inspect bends at the outlet |
| RX in range but intermittent LOS | Connector or bend moving with temperature or traffic | Wiggle test at each connector; OTDR at 1550 nm |
| RX -5 dBm | Wrong splitter ratio or missing splitter stage | Check FDH patching; do not leave it |
| OTDR end of fibre 40 m short of the route length | Break or unmated connector at that point | Locate: it is usually a pit, boundary point or outlet at that distance |
| Dying gasp then offline (from NOC) | Power at the premises | Confirm power and ONT PSU before any fibre test |

## CUSTOMISE: company field standard values

- ONT RX acceptance at install: `-14 to -22 dBm typical` (verify)
- ONT RX minimum for close-out: `-25 dBm` (verify)
- Maximum connector loss accepted: `0.5 dB` (verify); splice: `0.1 dB` (verify)
- Splitter ratios in use: `1:32` (verify; note any cascaded areas)
- OTDR pass criteria for handover: `<fill in>`
- Test set models and the exact label shown for each reading (so photos can be read): `<fill in>`
