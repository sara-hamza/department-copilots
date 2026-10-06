---
description: 8 to 10 headline options grouped by angle (benefit, proof, news, question, local, urgency) with a recommended pick
argument-hint: <paste the brief, the copy or the announcement> [channel:web|email-subject|social|print] [count:8-10]
---

Run the marketing-copilot skill in **headlines** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules.
2. Identify the audience and the single message the headline must carry. Use the angle table in `references/audience-matrix.md` (section "Headline angles by audience") and the claims rules in `references/brand-voice-guide.md`. No headline may make a claim the input does not support.
3. Produce exactly this template:

```
HEADLINES for <piece> | audience: <audience> | channel: <channel> | message: <one line>

BENEFIT
1. <headline>
2. <headline>

PROOF OR SPECIFIC
3. <headline>
4. <headline>

NEWS OR ANNOUNCEMENT
5. <headline>
6. <headline>

QUESTION OR CURIOSITY
7. <headline>

LOCAL OR COMMUNITY
8. <headline>

URGENCY OR ACTION (only if the input gives a real date or deadline)
9. <headline>
10. <headline>

RECOMMENDED
<number> because <audience and channel fit, in one line>

CHARACTER COUNTS
# | chars | fits <channel limit from audience-matrix.md>: yes/no

CLAIMS CHECK
<any headline that implies a claim needing substantiation, and what would support it>
```

4. Email subject lines under 50 characters; social under 100; web H1 under 70 (CUSTOMISE in audience-matrix.md). Avoid superlatives the brand guide lists under "claims that need substantiation" unless the input provides the evidence.
5. If no input is given, ask for the brief or copy and the channel.
