# people - People Assistant

Paste a job description, interview notes, a CV, a policy or a role outline and get back a cleaner JD, a structured interview question set, a competency-based interview summary, a 30/60/90-day onboarding plan or a plain-English policy explanation.

| Command | Use when |
|---|---|
| `/people:jd <paste JD or role notes>` | Improve a job description: structure, inclusive language, requirements vs nice-to-haves |
| `/people:interview-questions <role>` | Build a structured, competency-based question set with what good answers cover |
| `/people:interview-summary <paste notes>` | Turn interview notes into a summary by competency with quoted evidence, no verdict |
| `/people:onboarding <role and context>` | Draft a 30/60/90-day onboarding plan |
| `/people:policy <paste policy or name it>` | Explain a policy in plain English, with "the policy governs" caveat |

Requires `copilot-common`. The assistant organises and drafts; it never ranks candidates, never gives a hire or no-hire recommendation, and never infers protected attributes.

Reference knowledge lives in `skills/people-assistant/references/`. company-specific policies, approval steps and contacts are marked `CUSTOMISE`.
