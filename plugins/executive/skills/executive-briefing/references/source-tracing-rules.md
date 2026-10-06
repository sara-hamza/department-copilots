# Source tracing rules

Every claim in a brief, decision or risk view must point to the document it came from. A claim that cannot be traced is removed, not softened.

## Numbering sources

List every input at the top, numbered in the order read:

```
SOURCES
S1 Finance monthly pack, Sep 2026, Finance (PDF, 14 pages)
S2 Delivery status report, week ending 26 Sep 2026, Project Delivery (DOCX)
S3 Hillcrest project paper, 29 Sep 2026, Project Delivery (PDF, 6 pages)
S4 Enterprise risk register extract, as at 30 Sep 2026 (XLSX, sheet "Register", 41 rows)
S5 RSP account notes, Sep 2026, Wholesale (pasted text)
S6 Delegations of authority, v3 (PDF)
```

Include the type and size so a reader knows how much is behind each number. Pasted text with no title: "S5 Notes pasted by <role>, <date>".

## Citation format

| Source type | Cite as |
|---|---|
| PDF | `[S1 p.4]` or `[S1 pp.4-5]` |
| Document with numbered sections | `[S3 §4.2]` |
| Spreadsheet row | `[S4 row 12]` or `[S4 sheet Register row 12]` |
| Spreadsheet figure computed by the briefing | `[S4 sum of column Exposure, rows with Status = Open]` |
| Pasted notes | `[S5 para 3]` or `[S5 line "RSP X asked..."]` |
| Email or minutes | `[S7 item 4]` |
| Two sources for one claim | `[S2 p.3; S3 §2.1]` |
| Sources that disagree | state both values in the sentence, then `[S2 p.3 says 1,840; S3 §2.1 says 1,790]` |

The citation goes at the end of the sentence or point it supports. One citation can cover a two-sentence point only if both sentences come from the same place.

## What counts as traceable

- A figure that appears in the source, or is computed from the source's own numbers with the computation stated.
- A statement the source makes in its own words or a faithful paraphrase.
- A rating or status the source assigns.

## What does not count

- A figure remembered from last month or from general knowledge.
- An inference about cause the source does not make. ("Slipped because of power" is traceable only if the source says power caused it.)
- A benchmark or "typical" comparison not in a supplied document.
- A recommendation the briefing would make itself.

If something seems important but is untraceable, put it under NOT COVERED BY THE SOURCES or "Needed before deciding", phrased as a question.

## Handling contradictions

1. Report both values with both citations in the same sentence.
2. Say which is more recent or more specific if the sources make that clear; do not pick one otherwise.
3. Add the contradiction to the "possible inconsistencies" list in the risk view or to NOT COVERED in the brief ("premises connected count differs between S2 and S3; confirm before the meeting").

## Computed figures

When the briefing computes a number from a spreadsheet (a sum, a variance, a count):
- Say the sheet, the column, the filter and the rows excluded.
- Show the input figures if there are only two or three.
- Round as the source rounds.
- Mark it "computed" so the reader knows it is not printed in the source: `[computed from S4 column Exposure, Status = Open, 17 rows]`.

## Confidentiality carry-through

If any source is marked confidential, board-only, legal privilege or commercial-in-confidence, the brief states at the top: "Contains material from S<n>, marked <classification>." The brief inherits the highest classification among its sources.

## Checklist before issuing

- Every point has a citation.
- Every citation resolves to a listed source.
- Every number in the text either appears in the cited place or is marked computed with its basis.
- Contradictions are reported, not resolved silently.
- Nothing in the brief comes from outside the sources list.
- Classification line present if any source is classified.

## CUSTOMISE

- Classification labels in use at the company: `Internal, Confidential, Board-only, Commercial-in-confidence` (verify)
- Preferred source naming for recurring packs (so briefs can be compared period to period): `Finance pack <Mon YYYY>`, `Delivery status WE <date>`, `Risk register <date>` (verify)
- Whether page numbers or section numbers are preferred for board papers: `section numbers` (verify)
