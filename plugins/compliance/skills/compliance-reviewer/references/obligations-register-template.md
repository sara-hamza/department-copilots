# Obligations register template

An obligations register turns a document into a list of things someone must do, by when, with proof. It is the artefact that lets a compliance lead allocate owners and an auditor see that obligations are tracked.

This is not legal advice. Outputs are for review by qualified staff.

## Extraction method

1. Read the whole document and the definitions first.
2. Search for obligation language: shall, must, will, is required to, is responsible for, agrees to, undertakes, may not, must not, shall not, ensure that, procure that, at its cost.
3. For each hit, record: the clause, who is bound, the obligation in short active voice, and its type.
4. Capture obligations hidden in definitions, schedules, service descriptions and referenced policies.
5. Capture conditional obligations ("if X occurs, Y must..."): the trigger is the due column.
6. Capture obligations on the counterparty separately; they become rights we may need to enforce and monitor.
7. Note obligations that depend on undefined terms or unsupplied documents.

## Obligation types

| Type | Example | Due / trigger column |
|---|---|---|
| One-off | Deliver as-built drawings within 20 business days of practical completion | Date or event plus period |
| Recurring | Provide a monthly service performance report by the 10th | Frequency and deadline |
| Triggered | Notify the other party within 24 hours of becoming aware of a data breach | Trigger and response time |
| Ongoing | Maintain public liability insurance of $20 million for the term | "Ongoing"; evidence is periodic (certificate annually) |
| Prohibition | Must not assign without consent | "Ongoing"; evidence is the consent process |

## Register columns

| Column | Content |
|---|---|
| Ref | Sequential ID (OBL-001) |
| Clause | Clause, section, schedule and page |
| Obligation | Short active sentence: "the company must deliver X by Y" |
| Binds | Network operator / counterparty / both |
| Type | One-off / recurring / triggered / ongoing / prohibition |
| Owner | Role, not name. `TBC` if the document does not say and no role is obvious |
| Due or trigger | Date, frequency, or trigger plus response time |
| Evidence of compliance | What will show it was done: report, certificate, ticket, email, register entry |
| Status | Not started / on track / due / overdue / complete / not applicable |
| Notes | Dependencies, undefined terms, missing schedules, conflicts |

## Output template

```
OBLIGATIONS REGISTER: <document title, version, date>
Party positions: we = <Supplier | Customer | Licensor | ...>; counterparty = <name, role>

OBLIGATIONS ON US
Ref | Clause | Obligation | Type | Owner | Due or trigger | Evidence | Status
OBL-001 | cl. 5.2 | Provide monthly service report by 10th business day | Recurring | Service delivery manager (TBC) | Monthly, 10th business day | Report sent, filed | Not started
OBL-002 | cl. 12.1 | Notify counterparty within 2 business days of a security incident affecting their data | Triggered | Security lead (TBC) | Incident awareness + 2 business days | Notification record | Not started

OBLIGATIONS ON THE COUNTERPARTY
Ref | Clause | Obligation | Type | We monitor via | Due or trigger
CP-001 | cl. 7.4 | Maintain insurance per Sched. 3 | Ongoing | Certificate of currency annually | Each renewal

NOTES
- OBL-004 depends on "Agreed Standards" which is not defined; Sched. 2 not supplied.
- Owners marked TBC to be allocated by the compliance lead.

This is not legal advice. Outputs are for review by qualified staff.
```

## Worked example (wholesale service agreement extract)

Input clause: "The Supplier will restore any Service Affecting Fault within the Restoration Target set out in Schedule 4 and will provide the Customer with a Root Cause Report within 5 Business Days of restoration of any Priority 1 Fault."

Register rows:

| Ref | Clause | Obligation | Type | Owner | Due or trigger | Evidence |
|---|---|---|---|---|---|---|
| OBL-010 | cl. 9.1 | Restore Service Affecting Faults within the Restoration Target (Sched. 4) | Triggered | NOC manager (TBC) | Fault logged + Sched. 4 target | Ticket timestamps |
| OBL-011 | cl. 9.1 | Provide Root Cause Report for each P1 fault | Triggered | Engineering lead (TBC) | Restoration + 5 business days | RCR sent, filed |

Notes: Schedule 4 not supplied; "Business Day" definition should be checked for public holiday treatment in the relevant state.

## Maintenance of the register

- Review at each contract milestone, renewal and after any variation.
- Each recurring obligation gets a calendar entry with the owner.
- Overdue items are reported to the compliance lead at the agreed cadence.
- Keep the register with the contract in the document system of record; the register is not the contract and the contract governs.

## CUSTOMISE: company register conventions

- Register system of record (spreadsheet, GRC tool): `<fill in>`
- Standard owner roles list: `<fill in>`
- Reporting cadence for overdue obligations: `<fill in>`
- Compliance lead and legal contact: `<name, role, email>`
