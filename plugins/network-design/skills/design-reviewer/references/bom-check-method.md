# BOM check method: drawings vs bill of materials

The goal is a two-column table that an engineer can hand back to the designer without further explanation. Never estimate; count or say it cannot be counted.

## Step 1: build the drawing count

Sources, in order of reliability:

1. Schedules on the drawings (cable schedule, pit schedule, splitter schedule, port schedule). Prefer these; cite the sheet.
2. Legends with quantities.
3. Callouts and symbols counted sheet by sheet. State the method ("counted P5 symbols on Sheets 3 to 7").
4. Design notes stating totals.

Record each count as: `ITEM | QTY | SHEET | METHOD`. If two sources disagree, record both and flag it as a CRITICAL finding for the review.

## Step 2: normalise the BOM

Profile the spreadsheet first (spreadsheet-reader). Then:

- Trim, lowercase and collapse spaces in descriptions.
- Expand abbreviations: `conduit P50 50m` becomes item `conduit`, size `P50`, qty `50`, unit `m`.
- Separate size or rating from the item type (splitter 1:32, pit P6, cable 48F).
- Convert units to the drawing's units (metres, each, drums to metres using the drum length if given).
- Ignore subtotal rows, header rows repeated mid-sheet, and lines with zero quantity (list them separately if they look like deleted items).
- Keep the BOM row number for every line.

## Step 3: match

Match in this order and stop at the first match:

1. Exact item code (if the drawing schedule and BOM share codes).
2. Item type plus size (pit P6, cable 48F loose tube, splitter 1:32 SC/APC).
3. Item type only, flagged "size not confirmed".

Anything left is UNMATCHED on the side it came from.

## Step 4: compare quantities

| Comparison | Treatment |
|---|---|
| Equal | Report in the table with DIFFERENCE 0 so the engineer sees it was checked |
| BOM higher by a stated allowance (wastage, drum rounding, default 5 to 10% on cable and conduit) | DIFFERENCE shown, NOTE "within allowance if wastage is x%" |
| BOM higher beyond allowance | DIFFERENCE shown, NOTE "over-ordered or scope not on drawings" |
| BOM lower | DIFFERENCE shown, NOTE "under-ordered" and treat as a review WARNING (CRITICAL for splitters, FDH, closures) |
| Drawing not countable | DIFFERENCE "n/a", NOTE "not countable from Sheet n", add a question |

## Output table

```
BOM CHECK
ITEM                     | DRAWING (sheet)  | BOM (row)   | DIFFERENCE | NOTE
Pit P6                   | 42 (Sheet 4)     | 40 (row 12) | -2         | under-ordered
Cable 48F loose tube (m) | 2,310 (Sheet 9)  | 2,500 (row 3)| +190      | within 10% wastage
Splitter 1:32 SC/APC     | 12 (Sheet 2)     | 12 (row 21) | 0          | checked
Closure 96F dome         | 6 (Sheet 9)      | n/a         | n/a        | not in BOM

UNMATCHED ON DRAWING
Closure 96F dome x6 (Sheet 9)

UNMATCHED IN BOM
Row 27: "Marker tape 500 m" (no drawing reference; may be standard allowance)

COUNTING BASIS
Pits counted from the pit schedule, Sheet 4. Cable lengths from the cable schedule, Sheet 9; drum rounding not applied. Zero-quantity BOM rows 30 to 33 ignored.
```

## Common mismatch causes (use in NOTE)

| Pattern | Likely cause |
|---|---|
| BOM cable length well above drawing route length | Drum rounding, slack allowance, or a superseded route |
| BOM pit count below drawing | Stage split: BOM covers stage 1 only |
| Splitter count differs | Ratio changed on one sheet, or FDH schedule not updated |
| Closure sizes differ | Drawing shows fibre count, BOM shows closure capacity; map one to the other |
| Items only in BOM (markers, tape, bedding sand, lids) | Standard allowances; confirm with designer rather than flagging as error |
| Items only on drawings (terminals, pedestal, pillar) | BOM template missed the item type; CRITICAL if the item is on the critical path |

## What not to do

- Do not "correct" a BOM line to make it match.
- Do not infer quantities from scale measurements on the PDF unless the engineer asks and the scale is stated; then say "scaled from drawing, approximate".
- Do not merge two BOM lines into one match without saying so.
