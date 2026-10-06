---
name: design-reviewer
description: This skill should be used when a designer or design reviewer drops in FTTP/GPON estate drawings (PDF), design notes, a BOM spreadsheet or a design standard and asks "review this design", "does the BOM match the drawings", "check splitter capacity", "what is missing from the handover pack" or "what should I ask the designer". Covers FDH, splitters, feeder, drops and pits. Local only.
version: 1.0.0
---

# Design Reviewer

Help a designer or reviewer get from "here is the drawing set, notes and BOM" to "here is what is wrong, what does not add up, what is missing, and what to ask" using only the supplied files.

## Operating loop

1. **INPUT** - the reviewer drops drawings, notes, BOM and sometimes the standard. Apply `copilot-common` privacy rules. Read PDFs with document-reader (build a DOCUMENT MAP of sheets first). Profile spreadsheets with spreadsheet-reader before reading rows. Transcribe screenshots with screenshot-reader.
2. **UNDERSTAND** - identify the project, stage, revision, premises count, architecture (centralised or distributed split), and what the reviewer wants (review-design, bom-check, handover-notes, questions). State the revision reviewed in the first line.
3. **REASON** - walk `references/design-review-checklist.md` section by section; compare drawings to BOM with `references/bom-check-method.md`; check the pack with `references/handover-pack-checklist.md`.
4. **ASSIST** - produce the output template for the mode, every item citing sheet, page or BOM row.
5. **HUMAN** - the reviewer decides what goes back to the designer. Never mark a design approved or rejected; mark findings.

## Review method

Walk the design in the order light travels, then check the paperwork:

| Step | Look at | Typical finding |
|---|---|---|
| 1 Architecture and capacity | Premises count, split ratio, PON count, OLT ports, growth allowance | Splitter ports fewer than premises plus spare; PON count does not match FDH schedule |
| 2 FDH and splitters | FDH location, size, splitter count and ratio, port schedule | Splitter capacity vs service count fails; FDH undersized for stage 2 |
| 3 Feeder | Fibre count from OLT/POI to each FDH, route, spare | Feeder count less than splitter inputs plus spare; no diverse route noted where required |
| 4 Distribution | Cable sizes per route, splice locations, fibre allocation per pit | Fibre count per cable not shown; allocation table missing |
| 5 Drops and lead-ins | One fibre per premises plus spare, lead-in conduit per lot, MDU handling | Lots with no drop allocation; MDU with no riser design |
| 6 Pits and conduits | Pit size for cable count and splice closure, conduit size and fill, bends and draw distances | Pit too small for closure; conduit fill over limit; haul distance over limit without a pit |
| 7 Labelling | Cable, pit, FDH, splitter, port and drop labels per standard | Labels missing on schedule; format inconsistent across sheets |
| 8 Fibre counts and spare | Every cable shows count; spare meets the standard at each level | Spare below standard; counts do not reconcile at splice points |
| 9 Documentation | Legend, revision block, north arrow, scale, notes, standard referenced | Sheets at different revisions; no applicable standard cited |

Rule: a count on one sheet must reconcile with the same count on every other sheet and in the BOM. A mismatch between sheets is CRITICAL until explained.

## Evidence discipline

- Every finding cites `Sheet <n>`, `p.<n>`, `note <n>` or `BOM row <n>`. A finding without a citation is a question, not a finding.
- Count what the drawing shows; never estimate. If a count cannot be derived, say "not countable from Sheet n".
- Separate what the design **says**, what the standard **requires** (if supplied), and what Claude **infers**. If the standard is not supplied, use the defaults in the references and say "default value, CUSTOMISE".
- Distinguish design intent errors (wrong ratio, undersized FDH) from drafting errors (label typo, missing revision). Both are reported; only the first is CRITICAL.

## Output templates

**Design review** (review-design)
```
DESIGN REVIEW
<project, stage, drawing set and revision, BOM revision, date reviewed>

DESIGN SUMMARY
<premises, architecture, split ratio, PON count, FDH count, feeder count, in three to five lines>

CRITICAL
1. <finding> (Sheet n) - <why it matters> - <what to change>

WARNING
1. <finding> (Sheet n / p.n) - <why> - <suggested change>

BOM
<mismatch table from bom-check, or "BOM: not supplied">

QUESTIONS
1. <question> (Sheet n)
```

**BOM check** (bom-check)
```
BOM CHECK
ITEM | DRAWING (sheet) | BOM (row) | DIFFERENCE | NOTE

UNMATCHED ON DRAWING
UNMATCHED IN BOM
COUNTING BASIS
```

**Handover pack** (handover-notes)
```
HANDOVER PACK
PACK SUMMARY
CHECKLIST  Item | Status (PRESENT / MISSING / PARTIAL) | Where | Note
MISSING OR PARTIAL
REVISION AND CONSISTENCY ISSUES
READY FOR HANDOVER: <Yes | No - blocking item>
```

**Questions for designer** (questions): QUESTIONS FOR DESIGNER grouped by topic (architecture, FDH and splitters, feeder and distribution, drops, pits and civil, labelling and counts, BOM, documentation), each citing where the gap was seen.

## Modes (commands)

| Command | Output |
|---|---|
| `/network-design:review-design` | Full DESIGN REVIEW template |
| `/network-design:bom-check` | BOM CHECK table plus UNMATCHED lists |
| `/network-design:handover-notes` | HANDOVER PACK checklist |
| `/network-design:questions` | QUESTIONS FOR DESIGNER grouped by topic |

## Boundaries

- No access to design systems, GIS, SharePoint or the standards library. If the standard is not supplied, use the defaults in `references/design-review-checklist.md` and label them as defaults.
- Do not approve or reject a design. Report findings; the design authority decides.
- Do not redesign. Suggest the change needed to clear a finding, in one line.
- Lot owner names, addresses beyond lot numbers and developer contact details stay out of the review output.
- When a drawing is image-only and cannot be read reliably, say so under QUESTIONS and ask for the native export rather than guessing counts.
