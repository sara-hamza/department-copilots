# Structured, competency-based interview method

Structured interviews ask every candidate for a role the same questions, assess the same competencies, and rate against the same anchors. They predict job performance better than unstructured conversations and they are fairer. This file covers building the question set and summarising the notes afterwards.

## Principles

1. **Same questions for every candidate** at a given stage. Follow-up probes may vary; the core questions do not.
2. **Competencies come from the job**, not from the interviewer's preferences. Derive them from the JD outcomes.
3. **Past behaviour predicts future behaviour.** Prefer "Tell me about a time when..." over "What would you do if...". Use situational questions only where candidates could not reasonably have the experience.
4. **Rate per competency, then discuss.** Interviewers rate independently before calibrating. Overall impressions come last, from the panel, never from the assistant.
5. **Write down what was said**, not what you felt. Notes are evidence; summaries quote them.

## Choosing competencies

Pick five to seven from the JD. A typical mix:

| Type | Examples |
|---|---|
| Technical or functional | Fault isolation, network design review, contractor QA, invoice reconciliation, proposal writing |
| Problem solving | Diagnosing with incomplete information, prioritising under load |
| Communication | Writing for a customer or RSP, explaining technical detail to non-technical people |
| Working with others | Cross-team coordination, contractor or developer relationships, giving and receiving feedback |
| Ownership and judgement | Escalating at the right time, safety decisions, following process under pressure |
| Learning and adaptability | Picking up new platforms, responding to changed priorities |

## Question forms

**Past-behaviour (STAR)**: "Tell me about a time when you <competency in context>. What was the situation, what did you do, and what happened?"

**Situational**: "Imagine <realistic scenario from the role>. Walk me through what you would do and why."

**Technical walkthrough**: "Here is <a config, a drawing, a fault description>. Talk me through how you would approach it." Give the same artefact to every candidate.

**Work sample**: a short, role-relevant task done in the interview or sent beforehand, with a rubric. Best predictor; keep it short and respectful of the candidate's time.

## Standard probes

- What was your specific part in that, as distinct from the team's?
- What did you consider and reject?
- What would you do differently now?
- How did you know it had worked?
- Who did you involve and when?

## Rating anchors (1 to 4)

| Rating | Meaning |
|---|---|
| 1 | No relevant evidence, or evidence of the opposite behaviour |
| 2 | Some relevant evidence but gaps, generic, or relied on others |
| 3 | Clear, specific evidence of the competency at the level required |
| 4 | Clear evidence beyond the level required, with reflection and learning |

Write a one-line anchor per rating for each competency so interviewers rate consistently.

## Question bank by role family

**NOC Engineer**
- Fault isolation: "Tell me about a fault where the first evidence pointed one way and the cause turned out to be somewhere else. How did you work it out?" Good answers cover: layered approach, checking adjacent services, distinguishing current from historical alarms, writing down evidence, when they escalated.
- Communication under pressure: "Describe a time you had to update a partner or customer while the fault was still open." Good answers cover: factual, neutral wording, no speculation about the other side's network, clear next step and time.
- Shift work and handover: "What does a good handover contain?" Good answers cover: active incidents with owners, waiting-on items, planned work, non-obvious notes.

**Network Engineer**
- Change management: "Walk me through a change you made to a production routing policy. How did you check it and what was the rollback?" Good answers cover: pre-checks, maintenance window, staged implementation, verification commands, documented rollback, post-change monitoring.
- Design judgement: "Tell me about a time you pushed back on a design or a change." Good answers cover: evidence used, how they raised it, outcome.
- Technical walkthrough: supply a short config excerpt and ask what it does and what is wrong with it.

**Field Technician**
- Safety: "Tell me about a time you stopped work because it was not safe." Good answers cover: hazard identification, the process they followed, who they told, what changed.
- Test interpretation: "You have an ONT with no light and a good reading at the pit. What do you do next?" Good answers cover: one test at a time, cheapest first, connector inspection, OTDR from the right place, when to escalate.
- Quality: "How do you make sure your splicing and labelling meet the standard when you are under time pressure?"

**Design Engineer**
- Completeness: "How do you check a design is complete before issuing it?" Good answers cover: fibre counts, splitter capacity vs premises, BOM reconciliation against drawings, labelling, spares.
- Constraints: "Tell me about a design where site constraints forced a change. What did you do?"

**Project Coordinator / Manager**
- Prioritisation: "Tell me about a week when everything was urgent. How did you decide what to do first?" Good answers cover: blocked milestones first, overdue dependencies, decisions without owners, communicating what was parked.
- Stakeholders: "Describe a difficult conversation with a contractor or developer about a slipping date."

**Customer Operations**
- De-escalation: "Tell me about a customer who was angry about something your organisation could not directly fix." Good answers cover: acknowledgement, honest explanation of who does what, no promises they could not keep, follow-through.
- Writing: ask for a short written reply to a supplied complaint; assess clarity, tone and accuracy.

**Corporate roles (Finance, Procurement, People, Marketing)**
- Accuracy and judgement: "Tell me about a time you found an error in something that had already been approved." Good answers cover: how they verified it, who they told, how they handled the relationship.
- Process improvement: "What is a process you improved and how did you know it was better?"

## Questions to avoid, and the lawful alternative

| Do not ask | Why | Ask instead (if genuinely relevant) |
|---|---|---|
| How old are you? When did you finish school? | Age | Nothing; age is not relevant |
| Are you planning a family? Do you have children? Who looks after them? | Family responsibilities, sex | "The role involves <on-call roster / travel>. Is that something you can do?" |
| Where are you from? What is your background? | Race, nationality | "Do you have the right to work in Australia?" |
| Do you have any health conditions or disabilities? | Disability | "The role involves <specific inherent requirement>. Can you perform that, with or without adjustments?" |
| What religion are you? Do you need time off for religious reasons? | Religion | Describe the roster and ask whether it works for them |
| Are you married? Are you in a relationship? | Marital status | Nothing |
| Are you a union member? | Industrial activity | Nothing |
| Have you ever made a workers' compensation claim? | Disability, victimisation | Nothing |

If a hiring manager's input includes any of these, drop them and note `REMOVED: protected-attribute question` in the output.

## Bias cautions for interviewers

- **Similarity bias**: liking a candidate because they resemble you. Rate the evidence, not the rapport.
- **Halo and horns**: one strong or weak answer colouring every rating. Rate each competency separately.
- **First impression and recency**: early and late answers weigh more than they should. Use the notes, not memory.
- **Contrast**: rating against the previous candidate instead of the anchor.
- **Confidence as competence**: fluent speakers are not necessarily better. Look for specifics.
- **Gap and name inference**: do not infer anything from employment gaps, names, accents, photos or addresses.

## Summarising interview notes

1. Map every note to a competency. Notes that fit none go under NOT ASSESSED or are dropped if they are impressions.
2. Quote the interviewer's words. Do not paraphrase into stronger or weaker language.
3. Separate OBSERVED ("candidate described rolling back a BGP policy change after a route leak") from INTERPRETED ("suggests familiarity with change control"). Label the interpretation.
4. Record contradictions between interviewers as INTERVIEWER CONSISTENCY NOTES rather than resolving them.
5. End with what the panel needs to do next: calibrate ratings, reference check a specific claim, ask a follow-up at the next stage.
6. Never produce a score, a rank, or a hire or no-hire recommendation. The line "Rating and decision are for the panel." closes every summary.

## CUSTOMISE: company interview process

- Stages in use (screen, technical, panel, final): `<fill in>`
- Rating scale if different from 1 to 4: `<fill in>`
- Panel composition rules (for example, at least two interviewers, one from outside the team): `<fill in>`
- Where interview notes and summaries are stored and for how long: `<fill in>`
- Reference check template and who conducts it: `<fill in>`
- People team contact for recruitment questions: `<name, email>`
