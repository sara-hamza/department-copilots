---
description: Compare equipment counted on the drawings with the BOM - two-column mismatch table plus UNMATCHED items
argument-hint: <drop the drawing PDF and the BOM spreadsheet, or paste both lists>
allowed-tools: ["Bash"]
---

Run the design-reviewer skill in **bom-check** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules. Profile the BOM with the copilot-common spreadsheet-reader profiler (run it as that skill describes, with its own `${CLAUDE_PLUGIN_ROOT}`). If the script cannot be located, ask the engineer for a CSV export and read it directly.
2. Follow `references/bom-check-method.md`: build the drawing count per item from legends, schedules and callouts (cite the sheet for each count); normalise BOM descriptions and units; match on item type then size then quantity.
3. Output only:
```
BOM CHECK
ITEM | DRAWING (sheet) | BOM (row) | DIFFERENCE | NOTE

UNMATCHED ON DRAWING
<items counted on drawings with no BOM line>

UNMATCHED IN BOM
<BOM lines with nothing on the drawings>

COUNTING BASIS
<how each drawing count was derived; what was excluded>
```
4. Never estimate a drawing count. If a sheet does not give a countable figure, write "not countable from Sheet n" and list it under UNMATCHED ON DRAWING with a question.
5. Input missing: if only one side was supplied, say which, and list what the other side must contain.
