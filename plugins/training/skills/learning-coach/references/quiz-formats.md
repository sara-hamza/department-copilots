# Quiz formats

Questions test one idea each, come from the supplied material, and carry a hidden reference for the feedback. Answers are never shown until the learner has attempted the questions.

## Formats

| Format | Best for | Writing rule |
|---|---|---|
| Multiple choice (MCQ) | Thresholds, definitions, "which step next" | One correct option; distractors are plausible errors from the material (adjacent threshold, previous step, similar alarm). Four options. No "all of the above". |
| Short answer | Procedures, reasons, interpretations | Ask for a specific thing: "Name the two readings the SOP requires before dispatch." |
| Ordering | Procedure sequence | Give 4 to 6 steps shuffled; learner orders them. |
| Scenario (mini) | Applying a rule | Two or three lines of situation, one question: "What does the procedure say to do next?" |
| Spot the error | Critical reading | A short ticket note, config fragment or reply with one deviation from the material. |
| True or false with reason | Common misconceptions | Require the reason; a bare true/false scores partly. |
| Fill the gap | Values and names | "ONT RX below ___ dBm is classed as a fault (s. 4.2)." |

Default mix for five questions: 2 MCQ, 1 short answer, 1 ordering or scenario, 1 spot the error. Difficulty rises through the set.

## Writing rules

1. One idea per question. If it needs two ideas, split it.
2. Use the material's wording for terms, alarm names and thresholds.
3. Avoid trick questions. Difficulty comes from application, not ambiguity.
4. No negatives in the stem ("Which is NOT...") unless testing an exclusion rule the material states.
5. Every question has a hidden SOURCE reference for the feedback.
6. Every question has a hidden MODEL ANSWER that is the minimum complete answer, not an essay.
7. Distractors in MCQs should each represent a specific misunderstanding so feedback can name it.

## Question card (private to the coach)

```
Q<n>
FORMAT:
STEM:
OPTIONS (MCQ only):
MODEL ANSWER:
SOURCE: <section, page>
MISCONCEPTION PER DISTRACTOR (MCQ only):
DIFFICULTY: easy | medium | hard
```

## Presenting the quiz

```
QUIZ: <topic>, <N> questions, <format>, from <document>

Q1. <stem>
   a) ...
   b) ...
   c) ...
   d) ...

Q2. <stem>

...

Answer in any order; say 'reveal' for a hint, 'reveal all' for the answers after you have attempted them.
```

No answer key. No explanations. No "the correct answer is". If the learner answers only some questions, give feedback on those and leave the rest open.

## Feedback per question

```
Q<n>. YOUR ANSWER: <as given>
      VERDICT: correct | partly | incorrect
      WHY: <one or two lines; for MCQ, name the misconception behind the chosen distractor>
      WHERE TO READ: <section, page>
```

Scoring: correct 1, partly 0.5, incorrect 0. Report `SCORE: x of N`. Partly applies when the answer is right but incomplete, or right without the required reason.

## Reveal rules

- "reveal" on a question: give the next rung of the hint ladder (`coaching-method.md`), not the answer.
- "reveal all" before any attempt: respond "Attempt the questions first; say 'reveal' on any question for a hint." Then, if asked a second time, reveal with the note that this is on explicit second request.
- After an attempt: full feedback including model answers.

## Example set (GPON basics from an SOP; references are illustrative)

```
QUIZ: ONT offline triage, 5 questions, mixed, from <SOP title>

Q1. An ONT shows offline with last-down reason "dying gasp". According to the procedure, what is the first thing to confirm?
   a) OLT port optical levels
   b) Power at the customer premises
   c) Adjacent ONT status
   d) VLAN mapping

Q2. Name the two optical readings the procedure requires before a field dispatch for a single-premises LOS.

Q3. Put these steps in the order the procedure requires: dispatch field; check adjacent ONTs; read last-down reason; confirm planned works; ask customer to confirm ONT lights.

Q4. Ticket note: "ONT offline, LOS. RX -26 dBm. Adjacent ONTs fine. Escalated to RSP for BNG check." What does this note get wrong against the procedure?

Q5. True or false, with reason: a LOS alarm that cleared six hours ago and has not recurred is the current fault.

Answer in any order; say 'reveal' for a hint, 'reveal all' for the answers after you have attempted them.
```

(Model answers and sources are held by the coach and shown only in feedback.)

## Adapting difficulty across sessions

| Last score | Next quiz |
|---|---|
| 4.5 to 5 of 5 | Raise difficulty; more scenario and spot-the-error; fewer MCQ |
| 3 to 4 | Same difficulty; replace the missed ideas with new questions on the same ideas |
| Below 3 | Lower difficulty; return to teach mode for the missed ideas first |

## REVISE NEXT block

After feedback, list each missed or partly-correct idea with its revisit timing from the spaced repetition table in `coaching-method.md`:

```
REVISE NEXT
- <idea> (missed): tomorrow, then 3 days, 1 week, 1 month
- <idea> (partly): 3 days, 1 week, 1 month
```

## CUSTOMISE: company quiz banks

- Approved question banks by role, if any exist, and where they are kept: `<fill in>`
- Assessment pass marks and who administers formal assessments (the coach does not): `<fill in>`
- Topics that must use exact company thresholds and alarm names (list the governing document for each): `<fill in>`
