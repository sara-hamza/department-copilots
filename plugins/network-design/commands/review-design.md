---
description: Full design review of FTTP/GPON estate drawings, notes and BOM - Critical, Warning, BOM and Questions, each citing sheet or page
argument-hint: <drop the drawing PDF, design notes and BOM, or describe the design>
allowed-tools: ["Bash"]
---

Run the design-reviewer skill in **review-design** mode on:

$ARGUMENTS

Steps:
1. Apply `copilot-common` privacy rules. Read drawings with document-reader (page by page, build a DOCUMENT MAP of sheets first). Profile any BOM with the spreadsheet-reader script before reading its rows.
2. Walk every section of `references/design-review-checklist.md` in order: architecture and capacity, FDH and splitters, feeder, distribution, drops and lead-ins, pits and conduits, labelling, fibre counts and spare, documentation. Record a finding only where the design shows the problem or a required item is absent.
3. Run the BOM comparison from `references/bom-check-method.md` if a BOM was supplied; otherwise write "BOM: not supplied" in the BOM section.
4. Output the DESIGN REVIEW template: DESIGN SUMMARY, CRITICAL, WARNING, BOM, QUESTIONS. Every item cites `Sheet <n>` or `p.<n>` or the BOM row.
5. Splitter capacity vs service count is always checked and always reported, even when it passes.
6. Input missing: if no drawing, notes or BOM were supplied, output only DESIGN SUMMARY: nothing supplied and a MISSING INFORMATION list naming the files needed (drawing set, design notes, BOM, lot schedule, applicable standard).
