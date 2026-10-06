---
description: Turn an export or prior analysis into numbered plain-English findings with evidence and caveats for a non-analyst reader
argument-hint: <drop the export or paste the profile/anomaly output; say who will read the findings>
allowed-tools: ["Bash"]
---

Run the data-analyst skill in **findings** mode on:

$ARGUMENTS

Steps:
1. If a CSV/XLSX is provided and no prior analysis is pasted, apply the copilot-common spreadsheet-reader skill (run its profile_sheet.py profiler first), then compute the headline figures with a short Python snippet. Show results, not code. If prior analysis output is pasted, work from it and do not recompute unless a figure looks inconsistent.
2. Follow `references/plain-english-findings-template.md`: one finding per numbered item, each with the statement, the evidence (figure, basis, comparison), the confidence word and the caveat.
3. Produce the FINDINGS template from SKILL.md: SCOPE (what data, what period, what grain), FINDINGS 1..n ordered by importance to the stated reader, WHAT THIS DOES NOT SHOW, SUGGESTED NEXT QUESTIONS, FIGURES USED (every number with its source column and filter).
4. Plain English for the writing-helper "all staff" audience: no statistical terms without a one-phrase gloss ("outside the normal range, meaning above the 75th percentile plus 1.5 times the spread").
5. Never state a cause. Use "is associated with", "coincides with", "appears to". Put hypotheses under SUGGESTED NEXT QUESTIONS.
6. Keep to the eight most important findings unless asked for more; the rest go in one line under "Also noted".
