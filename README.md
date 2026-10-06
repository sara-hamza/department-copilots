# Department Copilots

A suite of **local-only department copilots** for staff of a wholesale fibre network operator, packaged as Claude Code plugins. **One repo per plugin.** This repo is the marketplace index that ties them together.

Every plugin follows the same rule:

> **Employee provides the input manually → Claude analyses it locally → Claude returns a better answer, draft, checklist, calculation, review or decision aid → the employee decides what to do.**

No CRM, NMS, email, ticketing or system integrations. The only data Claude sees is what the employee pastes or drops into the session, and the only thing Claude writes to disk is Sticky Notes (plain Markdown under `~/.copilots/sticky-notes/`).

## Install

Add the marketplace once, then install the plugins you want:

```bash
claude plugin marketplace add sara-hamza/department-copilots
```

```bash
claude plugin install copilot-common@department-copilots
```

```bash
claude plugin install noc@department-copilots
```

Install `copilot-common` first. Every department plugin relies on its privacy rules and readers. The repos are private; `claude` uses your git credentials to fetch them.

## The plugins

| Repo | Plugin | What it does | Commands |
|---|---|---|---|
| [copilot-common](https://github.com/sara-hamza/copilot-common) | `copilot-common` | Shared rules and readers used by every department copilot: privacy rules, document/spreadsheet/screenshot readers, writing helper. | skills only |
| [copilot-sticky-notes](https://github.com/sara-hamza/copilot-sticky-notes) | `sticky-notes` | Personal local memory: capture notes, actions and context bundles as plain Markdown files on your own machine. | `/sticky-notes:actions`, `/sticky-notes:bundle`, `/sticky-notes:done`, `/sticky-notes:note`, `/sticky-notes:notes` |
| [copilot-noc](https://github.com/sara-hamza/copilot-noc) | `noc` | NOC Copilot: fault-domain analysis, next checks and ticket notes from pasted CLI output, alarms and screenshots. | `/noc:escalate`, `/noc:fault-domain`, `/noc:handover`, `/noc:ticket-note`, `/noc:triage` |
| [copilot-network-engineering](https://github.com/sara-hamza/copilot-network-engineering) | `network-engineering` | Network Engineer: config review, change validation, routing analysis and troubleshooting from pasted configs and logs. | `/network-engineering:build-lab`, `/network-engineering:explain`, `/network-engineering:review-change`, `/network-engineering:review-config`, `/network-engineering:troubleshoot` |
| [copilot-network-design](https://github.com/sara-hamza/copilot-network-design) | `network-design` | Design Reviewer: finds inconsistencies, missing elements and BOM mismatches in design drawings, notes and BOMs. | `/network-design:bom-check`, `/network-design:handover-notes`, `/network-design:questions`, `/network-design:review-design` |
| [copilot-field-ops](https://github.com/sara-hamza/copilot-field-ops) | `field-ops` | Field Assistant: interprets optical and test results, suggests the next test and writes site close-out notes. | `/field-ops:interpret`, `/field-ops:next-test`, `/field-ops:photo-check`, `/field-ops:site-summary` |
| [copilot-construction](https://github.com/sara-hamza/copilot-construction) | `construction` | Construction Copilot: defect prioritisation, blocker analysis, contractor instructions and progress summaries. | `/construction:blockers`, `/construction:contractor-instruction`, `/construction:defects`, `/construction:progress-summary` |
| [copilot-project-delivery](https://github.com/sara-hamza/copilot-project-delivery) | `project-delivery` | Project Copilot: finds blockers, dependencies, risks, actions and decisions in meeting notes, schedules and RAID logs. | `/project-delivery:actions`, `/project-delivery:attention`, `/project-delivery:meeting-notes`, `/project-delivery:raid`, `/project-delivery:status` |
| [copilot-customer-ops](https://github.com/sara-hamza/copilot-customer-ops) | `customer-ops` | Customer Case Assistant: summarises cases, finds missing information and drafts professional customer responses. | `/customer-ops:case-summary`, `/customer-ops:draft-reply`, `/customer-ops:missing-info`, `/customer-ops:plain-english` |
| [copilot-rsp](https://github.com/sara-hamza/copilot-rsp) | `rsp` | RSP Assistant: works out what to ask the RSP and drafts technically accurate wholesale responses. | `/rsp:draft-response`, `/rsp:evidence-check`, `/rsp:questions` |
| [copilot-business-development](https://github.com/sara-hamza/copilot-business-development) | `business-development` | BD Copilot: account briefs, meeting prep, opportunity analysis, proposal writing and follow-up plans. | `/business-development:account-brief`, `/business-development:follow-up`, `/business-development:meeting-prep`, `/business-development:proposal` |
| [copilot-developer-relations](https://github.com/sara-hamza/copilot-developer-relations) | `developer-relations` | Developer Assistant: requirements summaries, open items, stakeholder questions and handover prep for property developments. | `/developer-relations:developer-questions`, `/developer-relations:handover`, `/developer-relations:open-items`, `/developer-relations:requirements` |
| [copilot-finance](https://github.com/sara-hamza/copilot-finance) | `finance` | Finance Reviewer: variance analysis, invoice vs PO checks, reconciliations and commentary drafts from exported files. | `/finance:commentary`, `/finance:invoice-check`, `/finance:reconcile`, `/finance:variance` |
| [copilot-procurement](https://github.com/sara-hamza/copilot-procurement) | `procurement` | Procurement Assistant: quote comparison, BOM comparison, supplier assessment and reorder planning. | `/procurement:compare-bom`, `/procurement:compare-quotes`, `/procurement:reorder`, `/procurement:supplier-assess` |
| [copilot-warehouse](https://github.com/sara-hamza/copilot-warehouse) | `warehouse` | Warehouse Assistant: stock analysis, shortages, slow movers, duplicates and replenishment recommendations from stock exports. | `/warehouse:duplicates`, `/warehouse:forecast`, `/warehouse:shortages`, `/warehouse:stock-analysis` |
| [copilot-people](https://github.com/sara-hamza/copilot-people) | `people` | People Assistant: interview questions, JD improvement, structured interview summaries, onboarding plans and policy explanations. | `/people:interview-questions`, `/people:interview-summary`, `/people:jd`, `/people:onboarding`, `/people:policy` |
| [copilot-marketing](https://github.com/sara-hamza/copilot-marketing) | `marketing` | Marketing Copilot: copy improvement, audience variants, headlines, proofing and FAQ generation. | `/marketing:faq`, `/marketing:headlines`, `/marketing:polish`, `/marketing:proof`, `/marketing:variants` |
| [copilot-compliance](https://github.com/sara-hamza/copilot-compliance) | `compliance` | Compliance Reviewer: obligations, risks, dates, ambiguities and questions for legal from policies, contracts and procedures. | `/compliance:obligations`, `/compliance:questions`, `/compliance:review` |
| [copilot-security](https://github.com/sara-hamza/copilot-security) | `security` | Security Analyst: triage, investigation checklists and remediation guidance from pasted logs, alerts and config excerpts. | `/security:investigate`, `/security:remediate`, `/security:triage` |
| [copilot-analytics](https://github.com/sara-hamza/copilot-analytics) | `analytics` | Data Analyst: profiles CSV/XLSX exports, finds anomalies, duplicates, outliers and trends and explains them plainly. | `/analytics:anomalies`, `/analytics:findings`, `/analytics:profile`, `/analytics:trends` |
| [copilot-executive](https://github.com/sara-hamza/copilot-executive) | `executive` | Executive Briefing: converts reports, notes and spreadsheets into decisions, risks, priorities and executive briefs. | `/executive:brief`, `/executive:decisions`, `/executive:risks` |
| [copilot-training](https://github.com/sara-hamza/copilot-training) | `training` | Learning Coach: turns SOPs and manuals into explanations, quizzes, fault scenarios and personalised training. | `/training:quiz`, `/training:review-answer`, `/training:scenario`, `/training:teach` |

Each department skill also activates automatically when the conversation matches its description, so the commands are shortcuts rather than the only entry point.

## Shared philosophy

```
INPUT       Employee intentionally provides information.
UNDERSTAND  Claude understands the employee's goal.
REASON      Specialist department knowledge is applied.
ASSIST      Analyse / review / draft / calculate / explain.
HUMAN       Employee makes the decision or performs the action.
```

## Repository layout

```
department-copilots/            # this repo: the index
├── .claude-plugin/marketplace.json
├── README.md
├── CLAUDE.md                   # conventions for maintaining the suite
├── examples/                   # sample inputs to demo each copilot
├── scripts/validate.py         # checks every plugin against the conventions
└── plugins/<name>/             # git submodule -> github.com/sara-hamza/copilot-<name>
```

Each plugin repo has the same shape:

```
copilot-<name>/
├── .claude-plugin/plugin.json
├── README.md                   # what it does, install, commands
├── commands/<mode>.md          # slash commands = modes
└── skills/<skill>/
    ├── SKILL.md                # trigger description, operating rules, output formats
    └── references/*.md         # department checklists and knowledge
```

## Working on the suite

Clone with submodules:

```bash
git clone --recurse-submodules https://github.com/sara-hamza/department-copilots.git
```

Edit a plugin inside `plugins/<name>/`, commit and push there, then commit the updated submodule pointer here. Validate everything with:

```bash
python3 scripts/validate.py
```
