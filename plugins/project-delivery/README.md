# project-delivery - Project Copilot

Paste your meeting minutes, drop a schedule or RAID export, or dump your rough notes, and get back what actually needs your attention, a normalised RAID log, a one-page status, an actions table or structured meeting notes you can paste straight into the project channel.

| Command | Use when |
|---|---|
| `/project-delivery:attention <paste or file>` | "What actually needs my attention?" Ranked TODAY / WAITING ON / DECISIONS REQUIRED / SLIPPING / NOTHING NEEDED |
| `/project-delivery:raid <paste or file>` | Normalise a messy RAID log or notes into RISKS / ASSUMPTIONS / ISSUES / DEPENDENCIES with owner, due, status; flags stale and ownerless items |
| `/project-delivery:status <paste or file>` | One-page status report (RAG, progress, blockers, asks) for a PMO or steering audience |
| `/project-delivery:actions <paste minutes>` | Extract an ACTIONS table (who / what / when / source line) from minutes |
| `/project-delivery:meeting-notes <paste raw notes>` | Turn raw notes into DECISIONS / ACTIONS / OPEN QUESTIONS / PARKING LOT |

Requires `copilot-common` (privacy rules, spreadsheet-reader for CSV/XLSX schedules and RAID logs, document-reader for PDF minutes, writing-helper for the status template). Works well with `sticky-notes` (`/sticky-notes:bundle <project>` before `/project-delivery:attention`).

Reference knowledge lives in `skills/project-copilot/references/`. Stale-item thresholds, RAG definitions and milestone names are sensible defaults marked `CUSTOMISE`; tune them to the company's delivery framework.
