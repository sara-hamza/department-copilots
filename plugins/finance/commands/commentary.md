---
description: Draft monthly finance commentary from the numbers provided (variance output, trial balance extract, KPI table)
argument-hint: <paste the numbers or the variance review output; say the audience (CFO pack, board, department head)>
---

Run the finance-reviewer skill in **commentary** mode on:

$ARGUMENTS

Steps:
1. Use only the figures provided. If a figure needed for a sentence is missing, leave a `[figure needed]` placeholder rather than inventing it.
2. Follow the commentary structure in `references/variance-analysis-method.md` (section "Commentary structure") and the writing-helper executive tone: point first, then the number, then the cause if supported, then the outlook or action.
3. Produce the COMMENTARY template from SKILL.md: PERIOD, HEADLINE (one or two sentences), REVENUE, OPERATING COSTS, CAPITAL, CASH AND WORKING CAPITAL (only the sections the input covers), ITEMS TO WATCH, FIGURES USED (table of every number quoted with its source line).
4. Each paragraph is three sentences at most. Every number in the prose must appear in FIGURES USED.
5. Do not add forecasts, accounting treatments or judgements about performance that the input does not support. Mark any inference with "appears" or "suggests".
