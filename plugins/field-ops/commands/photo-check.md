---
description: Read site photos (pit, closure, FDH, lead-in, ONT) and list what is visible and any compliance concerns, using "appears" wording
argument-hint: <drop one or more photos and say where they were taken>
---

Run the field-assistant skill in **photo-check** mode on:

$ARGUMENTS

1. Apply `copilot-common` privacy rules. Number the photos. Describe each with screenshot-reader site-photo rules: location cues, condition, labels, and what cannot be judged from the image.
2. For each photo, check the visible items against the "Photo compliance points" table in `references/site-closeout-template.md`: labels, splice protection and tray dressing, pit condition and lid, bend radius and cable support, conduit sealing and ends, water or debris, closure sealing, ONT mounting and fibre routing.
3. Output per photo:
```
PHOTO <n> (<where, as stated by the technician>)
VISIBLE
<what is in the frame, factual>
COMPLIANCE CONCERNS
<each as "appears ...", with what would confirm it>
NOT ASSESSABLE FROM PHOTO
<what a photo cannot show: loss, continuity, depth, label text if unreadable>
```
Then a one-line OVERALL: <no visible concerns | concerns to verify on site | likely rework>.
4. A photo is not an inspection. Never state a breach as fact; state what appears and what test or measurement would confirm it.
5. Input missing: if no photo was supplied, ask for it and list the shots that are usually needed (wide, close-up of labels, inside the closure, pit interior with lid off).
