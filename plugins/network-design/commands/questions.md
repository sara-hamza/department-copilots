---
description: Produce only the questions for the designer, grouped by topic, from drawings, notes or a BOM
argument-hint: <drop the design files or paste notes>
---

Run the design-reviewer skill in **questions** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules. Read what was supplied (document-reader for PDFs, spreadsheet-reader for BOMs).
2. Walk `references/design-review-checklist.md` but output only the questions. A question is warranted when the design is silent, ambiguous or inconsistent on a checklist item; do not ask about things the design already answers.
3. Output:
```
QUESTIONS FOR DESIGNER
<project, revision>

ARCHITECTURE AND CAPACITY
1. <question> (Sheet n / p.n)

FDH AND SPLITTERS
...

FEEDER AND DISTRIBUTION
...

DROPS AND LEAD-INS
...

PITS, CONDUITS AND CIVIL
...

LABELLING AND FIBRE COUNTS
...

BOM
...

DOCUMENTATION AND HANDOVER
...
```
4. Each question is specific, answerable in one sentence, and cites where the gap was seen. Omit empty groups.
5. Input missing: if nothing was supplied, ask for the drawing set and notes and stop.
