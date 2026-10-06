---
description: Find what is stopping construction - BLOCKERS by priority with impacted premises, DEPENDENCY, numbered dated CONTRACTOR ACTIONS, PROJECT IMPACT
argument-hint: <paste the site report, contractor update, or meeting notes>
---

Run the construction-copilot skill in **blockers** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules.
2. Extract every item that is stopping or delaying work. For each, name the impacted premises or stage (count if stated, "count not stated" if not), the party who can clear it, and whether it blocks a milestone.
3. Rank with the blocker rules in `references/defect-priority-matrix.md` (section "Blocker priority"): HIGH blocks a milestone or more than one stage; MED delays a stage with float; LOW is a nuisance with a workaround.
4. Output:
```
BLOCKERS
HIGH  <blocker> - impacted: <premises/stage> - owner: <who clears it> - since: <date if known>
MED   ...
LOW   ...

DEPENDENCY
<what must happen first, by whom, before each HIGH blocker clears; chains in order>

CONTRACTOR ACTIONS
1. <action> - due <date> - evidence: <what proves it is done>
2. ...

PROJECT IMPACT
<milestone> - <at risk | slipped by n days | not affected> - <why>
```
5. Dates in CONTRACTOR ACTIONS come from the input or the default timeframes in `references/contractor-instruction-template.md`; mark defaults as "(default)". Never invent a milestone date; if none is stated, write "milestone date: not provided".
6. Input missing: if the paste has no blockers, say "no blockers identified in the input" and list what a site report should contain for this analysis.
