---
description: Normalise messy RAID items, notes or a RAID export into RISKS / ASSUMPTIONS / ISSUES / DEPENDENCIES with owner, due and status; flags stale and ownerless items
argument-hint: <paste RAID items or notes, or name a RAID CSV or XLSX file> [as-of:<date>]
allowed-tools: ["Bash"]
---

Run the project-copilot skill in **raid** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules. If a spreadsheet is provided, apply the copilot-common spreadsheet-reader skill to profile it first; state which columns map to ID, type, description, owner, due/review date, status, likelihood, impact.
2. Classify every item using the decision table in `references/raid-method.md`: Risk (might happen), Assumption (taken as true, unverified), Issue (happening now), Dependency (we need something from someone, or someone needs something from us). Reclassify items that are in the wrong register and say so under RECLASSIFIED.
3. Apply the stale and ownerless rules in `references/attention-triage-rules.md` (CUSTOMISE thresholds; default stale = no update in 14 days or review date passed).
4. Produce exactly this template:

```
RAID LOG (normalised, as of <date>)

RISKS
ID | Risk (cause -> event -> impact) | Likelihood | Impact | Mitigation | Owner | Review by | Status | Flags

ASSUMPTIONS
ID | Assumption | Validated by | Owner | Validate by | Status | Flags

ISSUES
ID | Issue | Impact now | Action | Owner | Due | Status | Flags

DEPENDENCIES
ID | We need / They need | From / To | Needed by | Owner | Status | Flags

RECLASSIFIED
<original wording> -> <new type> because <reason>

FLAGGED
STALE: <IDs and last update>
OWNERLESS: <IDs>
NO DATE: <IDs>
DUPLICATES: <IDs that describe the same thing>

MISSING INFORMATION
<fields that could not be filled from the input>
```

5. Keep the original wording where possible; rewrite only to fit cause -> event -> impact for risks. Preserve existing IDs; number new items `NEW-1`, `NEW-2`.
6. If no input is given, ask for the RAID log or notes and offer the blank register from `references/raid-method.md`.
