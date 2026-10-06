# Duplicate detection rules

Duplicates in an item master cost money twice: stock held under two codes while one shows a shortage, and orders raised for an item already on the shelf. Find candidates, label confidence, and leave the merge decision to the system owner after a physical check.

## Step 1: normalise

**Codes**: uppercase; strip spaces, hyphens, dots and slashes; strip leading zeros in numeric segments (`SC-APC-001` and `SCAPC1` compare equal; keep the original for display).

**Descriptions**: lowercase; collapse whitespace; remove punctuation; expand common abbreviations before comparing; remove pack-size and colour tokens into separate fields.

| Abbreviation | Expand to |
|---|---|
| sm, smof, smf, os2 | single mode |
| mm, om3, om4 | multimode (keep the grade as an attribute) |
| f, fib, fibre, fiber | fibre |
| conn | connector |
| pt, pigtl | pigtail |
| pcd, patch, ptch | patch cord |
| apc / upc | keep as attribute, never merge across |
| mtr, m, met | metre |
| ea, each, unit | each |
| bx, box, pk, pack, ctn, carton | pack (with size if present) |
| drm, drum, reel | drum (with length if present) |
| blk, wht, ylw, grn, bl | colour attribute |

**Attributes to extract** (these decide whether two items are the same thing): fibre count (2F, 12F, 24F, 48F, 144F), connector type (SC, LC, FC) and polish (APC, UPC, PC), length (1 m, 2 m, 500 m), cable type (loose tube, tight buffer, drop, ribbon), splitter ratio (1:4, 1:8, 1:32), size (pit class, conduit diameter), voltage or model for active gear.

**Units**: each, pack (n), box (n), metre, drum (n metres), roll, kit. Two items with the same attributes but different units are a unit variant, not a true duplicate; flag separately.

## Step 2: match in passes

| Pass | Rule | Confidence |
|---|---|---|
| 1 | normalised item code identical | certain |
| 2 | barcode / EAN identical, or manufacturer part number identical | certain |
| 3 | normalised description identical and unit identical and attributes identical | likely |
| 4 | attributes identical, descriptions differ only by word order or abbreviation, unit identical | likely |
| 5 | attributes identical, unit differs (each vs pack, metre vs drum) | likely (unit variant) |
| 6 | high description similarity (token overlap at or above 80%) but an attribute missing on one side | possible |

Stop at the first pass that matches a pair. Never promote a "possible" to "likely" because the names look alike; promote only on evidence (barcode, MPN, a person checked the shelf).

## Step 3: what is NOT a duplicate

List these under NOT DUPLICATES (LOOK-ALIKES) when the employee would reasonably ask:

- Same cable, different fibre count (12F vs 24F).
- Same connector, different polish (SC/APC vs SC/UPC). Mixing these on a GPON network causes return loss problems; never merge.
- Same patch cord, different length.
- Same splitter, different ratio.
- Same ONT model, different firmware or hardware revision if the item master tracks it.
- Same item, different colour where colour is functional (cable identification).

## Step 4: present each group

```
Group 3 | likely (pass 4)
  ITM-0441  Pigtail SC/APC SM 2m           on hand 120 each
  PGT-SCAPC-2M  Pigtail 2 m SC APC single mode   on hand 35 each
  Suggested action: check shelf; if the same, consolidate to one code and move 35 across (system owner).
```

Suggested actions are for the storeperson and the system owner: "check shelf", "confirm with procurement which code the supplier uses", "consolidate", "set the unit variant as a pack of the base item". Never "merged".

## Step 5: counts and value

- Groups by confidence: certain, likely, possible.
- Items involved and combined on hand per group.
- If a cost column exists, the value of stock held under the secondary codes (what would appear on the primary code after consolidation).

## CUSTOMISE

Defaults to replace with the company's item master conventions:

- Primary code format: `<prefix>-<number>` (fill in) so the preferred code in a group can be identified
- Attributes that must never be merged across: `connector polish (APC/UPC), fibre count, splitter ratio, ONT model` (verify)
- Pack-size convention: `pack items are separate codes` or `pack is a unit on the base item` (verify)
- Token-overlap threshold for "possible": `80%` (verify)
- Who owns item master changes: `inventory system owner` (fill in)
