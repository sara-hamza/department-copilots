---
description: One-page project status (RAG, progress, blockers, asks) from minutes, schedule exports, RAID logs and notes, in writing-helper status style
argument-hint: <paste notes and minutes, or name schedule/RAID files> [audience:pmo|steerco|team] [period:<week ending>]
allowed-tools: ["Bash"]
---

Run the project-copilot skill in **status** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules. If a spreadsheet is provided, apply the copilot-common spreadsheet-reader skill to profile it first and state which columns were used for milestone, baseline, forecast and % complete.
2. Read `references/status-report-template.md` for the RAG definitions (CUSTOMISE) and the one-page layout. Use the writing-helper status structure: status word first, three bullets of progress, blockers, asks.
3. Audience from an `audience:` token (default `pmo`). For `steerco`, lead with decisions and asks; for `team`, add the next-week list.
4. Produce exactly this template:

```
PROJECT STATUS: <project> | period ending <date> | prepared from <sources>

OVERALL: <GREEN|AMBER|RED> - <one line why>
SCHEDULE: <G|A|R>   COST: <G|A|R|not assessed>   SCOPE: <G|A|R>   RISK: <G|A|R>

PROGRESS THIS PERIOD
- <done, with evidence from input>
- <done>
- <done>

MILESTONES
Milestone | Baseline | Forecast | Status | Comment

BLOCKERS
<blocker> | impact | owner | since | needed to clear

ASKS (decisions or help needed)
1. <ask> | from whom | by when | consequence if not

NEXT PERIOD
- <planned>

RISKS TO WATCH (top 3)
<risk> | likelihood/impact | mitigation | owner

MISSING INFORMATION
<what was not in the input: cost data, baseline dates, owner names>
```

5. Never set COST unless cost figures were provided; write `not assessed`. Do not upgrade or downgrade a RAG the employee stated without explaining why under OVERALL.
6. If no input is given, ask for the latest minutes and the schedule export, and offer the blank template.
