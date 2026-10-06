# construction - Construction Copilot

Paste the defect list, the site report, the contractor's update or the scope, drop in photos, and get back a prioritised defect register, a blocker analysis with contractor actions, a numbered instruction to the contractor, or a progress summary for the week.

| Command | Use when |
|---|---|
| `/construction:defects <defect list or photos>` | Prioritise defects: Severity, Location, Defect, Standard breached, Rectification, Evidence needed |
| `/construction:blockers <site report or update>` | What is stopping work: BLOCKERS by priority, DEPENDENCY, CONTRACTOR ACTIONS, PROJECT IMPACT |
| `/construction:contractor-instruction <context>` | Draft a numbered instruction to the contractor with dates and acceptance criteria |
| `/construction:progress-summary <updates for the period>` | PROGRESS SUMMARY: period, completed, in progress, blocked, next week, risks |

Requires `copilot-common` (screenshot-reader for photos, writing-helper for instructions). Works with `sticky-notes` for carrying site context between weeks.

Reference knowledge lives in `skills/construction-copilot/references/`. Rectification timeframes, standards names and contact roles there are sensible defaults marked `CUSTOMISE`; replace them with the company's construction specification and contract terms.
