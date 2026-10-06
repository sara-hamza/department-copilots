---
description: Structured proposal draft from the inputs provided, with placeholders wherever a fact is missing; never invents pricing
argument-hint: <paste the opportunity details, requirements, scope notes, any prior proposal text; name PDFs or lot schedules if you have them>
---

Run the bd-copilot skill in **proposal** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules. Apply document-reader to any named PDF and spreadsheet-reader to any named lot schedule; cite pages and rows.
2. Follow `references/proposal-structure.md` section by section. Use writing-helper developer tone: professional, confident, outcome-focused, no internal process detail. Use `references/objection-handling.md` to pre-empt objections inside the relevant sections rather than in a separate list.
3. Produce the proposal in this structure, each section as plain text with the UPPERCASE heading:

```
PROPOSAL DRAFT: <estate / project> for <developer> | version 0.1 | <date>

1. EXECUTIVE SUMMARY
2. UNDERSTANDING OF YOUR DEVELOPMENT        (lots, stages, timing, dwelling types, from input)
3. PROPOSED SOLUTION                        (FTTP network scope: what we design, build, operate; demarcation with developer works)
4. SCOPE OF WORKS AND RESPONSIBILITIES      (table: Item | Network operator | Developer)
5. PROGRAMME                                (milestones tied to the developer's civil and settlement dates)
6. SERVICE OUTCOMES FOR RESIDENTS           (RSP choice, speed tiers available, support model)
7. COMMERCIAL TERMS                         ([PRICING: TO BE PROVIDED BY <owner>] placeholders only)
8. ASSUMPTIONS AND EXCLUSIONS
9. NEXT STEPS
10. APPENDICES                              (list what should be attached)

---
PLACEHOLDERS TO FILL (do not send until cleared)
[<placeholder>] | section | who supplies it

FACTS USED AND SOURCES
<fact> | <source>

MISSING INFORMATION
<inputs that would materially improve the draft>
```

4. Pricing, rebates, contribution amounts and contract terms are placeholders in square brackets with the owner named, never numbers, even if a "typical" figure seems obvious. Capabilities and standards are stated only if the input or the CUSTOMISE defaults in the references support them, and the CUSTOMISE ones are marked `[CONFIRM]`.
5. If no input is given, output the section skeleton with a one-line description of what each section needs, and ask for the opportunity details.
