---
description: Grammar, consistency and brand check as an Issue / Location / Fix table, without rewriting the piece
argument-hint: <paste the copy, or name a PDF or screenshot> [strict:yes]
---

Run the marketing-copilot skill in **proof** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules. For PDFs apply document-reader (cite page and paragraph); for screenshots apply screenshot-reader (cite the region).
2. Walk `references/proofing-checklist.md` in order: spelling and grammar (Australian English), punctuation and typography (including em-dashes to replace), numbers, dates and units, consistency (names, capitalisation, terms), brand terms and voice from `references/brand-voice-guide.md`, claims needing substantiation, links and contact details present and plausible, accessibility (alt text noted, reading level), legal and compliance flags.
3. Produce exactly this template:

```
PROOF: <piece> | <n> issues | severity: <blocking: n, should fix: n, nice to have: n>

# | Severity | Issue | Location | Fix
1 | Blocking | <what is wrong> | <para/line/page or quoted fragment> | <exact replacement text>
...

CONSISTENCY TABLE
Term or name | Variants found | Use this

CLAIMS NEEDING SUBSTANTIATION
"<claim>" | location | evidence required

PASSED
<checklist sections with no issues, so the author knows they were checked>

QUESTIONS FOR THE AUTHOR
<things only the author can resolve: intended date, which product name, approval status>
```

4. Severity: Blocking = factual, legal, brand-term or claim issues that must not publish; Should fix = grammar, consistency, clarity; Nice to have = style preference. Do not rewrite the piece; give the fix text per issue.
5. If no input is given, ask for the copy and list the checklist headings so the author knows what will be checked.
