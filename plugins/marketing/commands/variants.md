---
description: Audience versions of the same copy (residents, developers, RSPs, internal) with identical facts, under clear VERSION headers
argument-hint: <paste the copy or announcement> [audiences:residents,developers,rsps,internal] [channel:email|web|social|sms]
---

Run the marketing-copilot skill in **variants** mode on this input:

$ARGUMENTS

Steps:
1. Apply copilot-common privacy rules.
2. Extract the FACT LIST first: every fact, figure, date, name and commitment in the input. The fact list is the contract; every version must contain the same facts and no new ones.
3. Use `references/audience-matrix.md` for what each audience cares about, the vocabulary they use, what to lead with and what to leave out, and `references/brand-voice-guide.md` for tone. Follow writing-helper rules for multiple versions (clear VERSION headers, identical facts).
4. Default audiences: residents, developers, RSPs, internal. Produce exactly this template:

```
FACT LIST (identical across versions)
1. <fact>
2. ...

VERSION A: residents (<channel>)
<copy>

VERSION B: developers (<channel>)
<copy>

VERSION C: RSPs (<channel>)
<copy>

VERSION D: internal staff (<channel>)
<copy>

WHAT CHANGED BETWEEN VERSIONS
Audience | Leads with | Vocabulary shifts | Left out and why

FACT CHECK
<confirmation that each version contains facts 1 to n; list any version where a fact had to be omitted for channel length and flag it>
```

5. Residents: no acronyms, "your provider" for RSP, no internal process. Developers: outcomes, dates, responsibilities. RSPs: precise and technical, service and process impact. Internal: what it means for them, who to contact, what not to say externally.
6. If no input is given, ask for the copy and which audiences are needed.
