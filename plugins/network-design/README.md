# network-design - Design Reviewer

Drop in the exported drawing PDF, the design notes and the BOM spreadsheet and get back a design review that cites sheet and page, a drawing-vs-BOM mismatch table, a handover-pack checklist or a clean list of questions for the designer.

| Command | Use when |
|---|---|
| `/network-design:review-design <files or notes>` | Full review: Critical / Warning / BOM / Questions, each citing sheet or page |
| `/network-design:bom-check <drawing and BOM>` | Only the drawing count vs BOM count mismatch table plus UNMATCHED items |
| `/network-design:handover-notes <pack contents>` | Check a handover pack: what is present, what is missing |
| `/network-design:questions <files or notes>` | Only the questions for the designer, grouped by topic |

Requires `copilot-common` (document-reader for PDFs, spreadsheet-reader for BOMs). Works with `sticky-notes` for carrying review context between sessions.

Reference knowledge lives in `skills/design-reviewer/references/`. Splitter ratios, spare percentages, pit and conduit sizes and labelling formats there are sensible defaults marked `CUSTOMISE`; replace them with the company's design standard.
