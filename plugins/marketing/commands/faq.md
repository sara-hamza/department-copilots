---
description: FAQs with answers drawn only from a brief or announcement, plus the questions the input cannot answer yet
argument-hint: <paste the brief, announcement or event notes> [audience:residents|developers|rsps|internal|media] [count:8-15]
---

Run the marketing-copilot skill in **faq** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules.
2. Identify the audience (default residents). Use the "What each audience asks first" column in `references/audience-matrix.md` to generate the questions, and `references/brand-voice-guide.md` for tone and terms. Answers come only from the input; if the input does not answer a question the audience will certainly ask, list it under NEEDS AN ANSWER rather than inventing one.
3. Produce exactly this template:

```
FAQ: <topic> | audience: <audience> | source: <brief / announcement date>

Q1. <question in the audience's words>
A. <answer from the input, plain language; "your provider" for RSP when writing for residents>

Q2. ...

NEEDS AN ANSWER (the audience will ask; the input does not say)
# | Question | Who can answer internally | Risk if unanswered

SOURCE MAP
Q# | fragment of the input the answer came from

CLAIMS CHECK
<any answer that implies a claim needing substantiation>
```

4. Order the questions as the audience would ask them: what is it, does it affect me, when, what do I do, what does it cost (for residents: refer to the provider), who do I contact. Keep answers to three sentences or fewer.
5. If no input is given, ask for the brief or announcement and the audience.
