---
description: Improve a draft (clarity, flow, brand voice, house style) and list every change made so each can be accepted or rejected
argument-hint: <paste the draft> [audience:residents|developers|rsps|internal] [length:same|shorter|longer] [channel:web|email|social|print]
---

Run the marketing-copilot skill in **polish** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules. If the draft is a PDF or screenshot, apply document-reader or screenshot-reader first.
2. Identify the audience from an `audience:` token or the text (default: residents). Apply `references/brand-voice-guide.md` (tone, terms to use and avoid, claims needing substantiation) and the writing-helper house style (Australian English, short sentences, active voice, no em-dashes).
3. Keep every fact, figure, name and date exactly as in the draft. Do not add claims. If a claim in the draft needs substantiation per the brand guide, keep it but flag it.
4. Produce exactly this template:

```
POLISHED COPY (<audience>, <channel>, length: <same|shorter|longer>)
<the improved copy>

CHANGES MADE
# | Original | Changed to | Why (clarity / tone / term / grammar / structure / length)
1 | "<fragment>" | "<fragment>" | <reason>

KEPT AS IS (deliberately)
- <thing that looked odd but was left: brand name spelling, legal wording, a quote>

CLAIMS TO SUBSTANTIATE BEFORE PUBLISHING
- "<claim>" | what evidence is needed | source in brand guide

QUESTIONS
<anything ambiguous in the draft that only the author can resolve>
```

5. The CHANGES MADE table must account for every edit; an editor should be able to rebuild the original from it. Group trivial punctuation fixes into one row.
6. If no draft is given, ask for it and state the audience options.
