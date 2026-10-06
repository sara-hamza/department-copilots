# Department Copilots

A suite of **local-only department copilots** for staff, packaged as a Claude Code plugin marketplace.

Every plugin follows the same rule:

> **Employee provides the input manually → Claude analyses it locally → Claude returns a better answer, draft, checklist, calculation, review or decision aid → the employee decides what to do.**

No CRM, NMS, email, ticketing or system integrations. Nothing is pulled from company systems. The only data Claude sees is what the employee pastes or drops into the session, and the only thing Claude writes to disk is Sticky Notes (plain Markdown under `~/.copilots/sticky-notes/`).

## Install

Add the marketplace once, then install the plugins you want.

From GitHub (needs access to the private repo):

```bash
claude plugin marketplace add sara-hamza/department-copilots
```

Or from a local clone:

```bash
claude plugin marketplace add /path/to/department-copilots
```

```bash
claude plugin install copilot-common@department-copilots
```

```bash
claude plugin install sticky-notes@department-copilots
```

```bash
claude plugin install noc@department-copilots
```

Install `copilot-common` first. Every department plugin relies on its privacy rules and readers.

## The suite

| Department | Plugin | Commands |
|---|---|---|
| Everyone | `copilot-common` | (skills only: privacy rules, document / spreadsheet / screenshot readers, writing helper) |
| Everyone | `sticky-notes` | `/sticky-notes:note` `/sticky-notes:notes` `/sticky-notes:actions` `/sticky-notes:done` `/sticky-notes:bundle` |
| NOC | `noc` | `/noc:triage` `/noc:ticket-note` `/noc:fault-domain` `/noc:handover` `/noc:escalate` |
| Network Engineering | `network-engineering` | `/network-engineering:troubleshoot` `review-config` `review-change` `explain` `build-lab` |
| Network Design | `network-design` | `/network-design:review-design` `bom-check` `handover-notes` `questions` |
| Field Operations | `field-ops` | `/field-ops:interpret` `next-test` `site-summary` `photo-check` |
| Construction | `construction` | `/construction:defects` `blockers` `contractor-instruction` `progress-summary` |
| Project Delivery | `project-delivery` | `/project-delivery:attention` `raid` `status` `actions` `meeting-notes` |
| Customer Operations | `customer-ops` | `/customer-ops:case-summary` `missing-info` `draft-reply` `plain-english` |
| RSP / Wholesale | `rsp` | `/rsp:questions` `draft-response` `evidence-check` |
| Business Development | `business-development` | `/business-development:account-brief` `meeting-prep` `proposal` `follow-up` |
| Developer Relations | `developer-relations` | `/developer-relations:requirements` `open-items` `developer-questions` `handover` |
| Finance | `finance` | `/finance:variance` `invoice-check` `reconcile` `commentary` |
| Procurement | `procurement` | `/procurement:compare-quotes` `compare-bom` `supplier-assess` `reorder` |
| Warehouse | `warehouse` | `/warehouse:stock-analysis` `shortages` `duplicates` `forecast` |
| People / HR | `people` | `/people:jd` `interview-questions` `interview-summary` `onboarding` `policy` |
| Marketing | `marketing` | `/marketing:polish` `variants` `headlines` `proof` `faq` |
| Legal / Compliance | `compliance` | `/compliance:review` `obligations` `questions` |
| Cybersecurity | `security` | `/security:triage` `investigate` `remediate` |
| Data / Analytics | `analytics` | `/analytics:profile` `anomalies` `findings` `trends` |
| Leadership | `executive` | `/executive:brief` `decisions` `risks` |
| Training | `training` | `/training:teach` `quiz` `scenario` `review-answer` |

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
plugin/
├── .claude-plugin/marketplace.json
├── README.md
├── CLAUDE.md                  # conventions for maintaining this repo
└── plugins/
    ├── copilot-common/       # shared skills
    ├── sticky-notes/          # personal local memory
    ├── noc/                   # reference department plugin
    └── ...                    # one directory per department
```

Each department plugin has the same shape:

```
<plugin>/
├── .claude-plugin/plugin.json
├── README.md
├── commands/<mode>.md         # slash commands = modes
└── skills/<skill>/
    ├── SKILL.md               # trigger description, operating rules, output formats
    └── references/*.md        # department checklists and knowledge
```

## Maintaining

See `CLAUDE.md`. Validate everything with:

```bash
python3 scripts/validate.py
```
