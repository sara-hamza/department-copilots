---
name: writing-helper
description: This skill should be used whenever a copilot drafts something a person will send or publish - ticket notes, handovers, customer replies, RSP responses, contractor instructions, status updates, executive briefs, job descriptions, policies, marketing copy, meeting summaries. It sets house style, tone by audience, structure, and the rewrite checklist.
version: 1.0.0
---

# Writing Helper

House style for every draft produced by a copilot.

## Defaults

- Australian English spelling (analyse, organise, programme for schedules, colour, licence as noun).
- Short sentences, one idea each. Active voice. Plain words over jargon unless the reader is technical.
- Lead with the point the reader needs. Background after.
- Dates as `6 Oct 2026`, times as `14:30 ACDT` (state the zone when readers may be interstate).
- No em-dashes. Use full stops or commas.
- Numbers: figures in tables or on their own line; money with `$` and thousands separators.

## Tone by audience

| Audience | Tone | Avoid |
|---|---|---|
| Internal ticket / handover | Terse, factual, chronological | Opinions without evidence, blame |
| Customer | Warm, plain, accountable, no internal jargon | Acronyms (ONT, PPPoE, BNG), promises of timeframes not confirmed |
| RSP / wholesale partner | Precise, technical, neutral, evidence-led | Speculation about their network, emotional language |
| Contractor | Direct, numbered actions, dates, acceptance criteria | Vague "please action ASAP" |
| Developer / property client | Professional, confident, outcome-focused | Internal process detail |
| Executive | Decisions first, then risks, then facts; one page | Narrative, build-up |
| All staff / policy | Clear, consistent terms, examples | Legalese, double negatives |

## Structure templates

**Ticket note**
```
SUMMARY: <one line>
OBSERVED: <facts, timestamps>
CHECKS DONE: <numbered>
FINDING: <likely cause / fault domain>
NEXT: <who does what>
```

**Customer reply**: acknowledge → what we found (plain English) → what happens next and when → how to reach us. One short paragraph each.

**Status update**: RAG or one-word status → three bullets of progress → blockers → asks.

**Instruction to contractor**: context (1 line) → numbered actions with due dates → evidence required (photos, test results) → acceptance criteria → contact.

## Rewrite checklist

1. Does the first sentence carry the main point?
2. Can any sentence be cut without losing meaning?
3. Any jargon the audience would not use themselves?
4. Any claim not supported by the employee's input? Remove or flag it.
5. Personal data that the audience does not need? Remove it.
6. Is the ask explicit (who, what, by when)?

## Multiple versions

When asked for variants (audiences, lengths, channels), produce them under clear headers (`VERSION A: customer email`, `VERSION B: SMS`) and keep facts identical across versions.
