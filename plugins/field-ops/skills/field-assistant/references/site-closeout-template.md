# Site visit summary and photo compliance points

All plain text. Readings with units and the point measured. Times with zone. No customer personal data unless the technician includes it on purpose; lot number or service reference is enough.

## Site visit summary

```
SITE VISIT SUMMARY
REF: <ticket / work order>   SITE: <estate, lot or service reference>   DATE: <date> <zone>
TECHNICIAN: <name or id>

ISSUE
<symptom as reported, one or two lines, and what the NOC said before the visit>

TESTING
1. <time> <test> at <point> -> <reading with unit>
2. ...

FINDINGS
<what the tests show, with the confidence word: confirmed / likely / possible>

REMEDIATION
<what was done, in order; "none" if nothing was changed>
<reading after remediation, with unit and point>

FURTHER ACTION
<owner> to <action> by <date or trigger>; or "none, service restored and confirmed with customer at <time>"

TIME ON SITE: <arrive> to <depart>
MATERIALS USED: <item x qty> or "none"
```

Rules:
- TESTING lists only what the technician wrote. Missing but expected tests go after the summary as `SUGGESTED (not done): ...`.
- FINDINGS must follow from TESTING. If the tests do not support a cause, say "cause not confirmed" and name the next test under FURTHER ACTION.
- REMEDIATION states the after reading. A repair without an after reading is incomplete; say so.
- FURTHER ACTION always names an owner. If unknown, `owner: TBC`.

## Worked example

```
SITE VISIT SUMMARY
REF: WO-21877   SITE: Riverlea Stage 3, Lot 112   DATE: 6 Oct 2026 ACDT
TECHNICIAN: FT-14

ISSUE
Customer reports no internet since 4 Oct. NOC: ONT offline, LOS, last RX -30.1 dBm 1490 nm, OLT port operational, adjacent ONTs online.

TESTING
1. 09:40 ONT LEDs: power on, PON flashing, LOS on. RX at ONT port: no light.
2. 09:48 Cleaned and reseated ONT port and patch lead: no change.
3. 09:55 Power meter at wall outlet, 1490 nm: no light.
4. 10:10 Power meter at pit end of drop (boundary pit P3-112): -14.8 dBm.
5. 10:20 VFL from pit end: light visible at the lead-in conduit entry at the boundary, none at the outlet.

FINDINGS
Confirmed break or severe loss in the lead-in between the boundary pit and the wall outlet. Pit end reading is healthy, so the distribution side is cleared. Likely cause: lead-in damaged during the recent fence installation (fresh post holes 1 m from the conduit line).

REMEDIATION
Replaced lead-in drop from pit P3-112 to the wall outlet, new SC/APC connectors both ends.
10:55 RX at ONT port: -15.3 dBm 1490 nm. ONT online, PON steady, LOS off.

FURTHER ACTION
NOC to confirm ONT registered and session up; Customer advised to check fence contractor dial-before-you-dig; Field supervisor to note possible damage claim. owner: FT-14 to update ticket.

TIME ON SITE: 09:35 to 11:05
MATERIALS USED: drop cable 30 m x1, SC/APC connector x2
```

## Photo compliance points

Use for photo-check. A photo shows condition, not performance; use "appears". For each point, say what would confirm it.

| Area | Look for | Concern wording | Confirm by |
|---|---|---|---|
| Pit | Lid fitted and correct class for location; pit not collapsed; no water or silt over cables; cables entering through ducts, not the wall; slack coiled, not kinked | "pit appears to hold water", "lid appears to be the wrong class for a driveway" | Site inspection; pit schedule |
| Conduit | Ends sealed or capped; bell ends where cables enter; no crush or deformation; draw rope present where required | "conduit end appears unsealed" | Rodding or mandrel; inspection |
| Closure | Sealed, ports capped, cable glands tight; mounted or supported, not lying in silt; identifier label present and legible | "closure appears unsealed at port 2" | Open and inspect; test |
| Splice tray | Each splice in a holder with protection sleeve; fibres routed with gentle loops; no fibre crossing over the tray edge; tray lid fitted; no bare fibre | "splice protection appears missing on one splice" | Open the tray; OTDR |
| Bend radius and support | No tight bends; cable ties not pinching; minimum bend radius respected at entries (default 10 x cable diameter under load, 20 x for long term, 15 mm for G.657 cords) | "bend at the entry appears below minimum radius" | Measure; OTDR at 1550 nm |
| Labels | Cable, closure, FDH, splitter, port and drop labels present, legible, in the standard format, matching the schedule | "label appears missing on the distribution cable" | Compare with the schedule |
| FDH | Door seals intact; splitters seated; patch cords dressed with no strain; dust caps on unused ports; no water marks | "unused ports appear uncapped" | Inspection |
| Lead-in and boundary | Conduit rises to the boundary point or outlet with a sealed end; drop protected where exposed; no cable buried without conduit | "drop appears to run unprotected over the fence line" | Inspection |
| ONT and premises | ONT mounted, fibre routed without tight bends, outlet faceplate fitted, patch lead not strained, power supply secured | "patch lead appears strained at the ONT" | Inspection |
| Safety | Open pit with no barrier, traffic exposure, ladder use, confined space signs | "open pit appears unguarded" | Site rules; supervisor |

Overall line, choose one:
- OVERALL: no visible concerns
- OVERALL: concerns to verify on site (list the points)
- OVERALL: likely rework (list the points and who owns the rework)

## CUSTOMISE: company close-out rules

- Required photos per visit: `<e.g. ONT label, RX reading on meter, pit interior, lid replaced>` (verify)
- Minimum RX to close a ticket: `<-25 dBm>` (verify)
- Minimum bend radius by cable type: `<fill in>`
- Label format: `<fill in>`
- Where the summary is pasted (ticket field name only; never accessed): `<fill in>`
