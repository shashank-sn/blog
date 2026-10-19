# Skill template

Copy this into `<place>-presence/SKILL.md`. Replace every `<...>`.

````markdown
---
name: <place>-presence
description: >-
  Audits a company's <place> presence and prepares the fixes. Asks for the
  company's sources first and does no work until it has them. Audits the live
  pages against a checklist, drafts every fix from the company's own sources,
  and returns engineering tasks and content suggestions. Never publishes. Use
  when asked to audit, fix, or set up a company's <place> pages.
license: <license>
metadata:
  version: "0.1.0"
---

# <Place> presence for a company

## Rules

1. No work before intake.
2. Every description of the company is one of its approved blocks, word for word.
3. Every number comes from the company's cleared numbers.
4. A technical fact with no source gets `[engineer: <question>]`.
5. Nothing goes live from the operator's side.
6. When two sources disagree, report the conflict.

## Workflow

```text
- [ ] 1. Intake (references/intake.md)
- [ ] 2. Audit the live state (references/audit-checklist.md)
- [ ] 3. Draft the fixes (references/fields.md, references/best-practices.md)
- [ ] 4. Check the drafts against the rules and the exemplars
- [ ] 5. Write the report: audit, engineering tasks, content suggestions
- [ ] 6. Prepare go-live (references/how-to.md)
- [ ] 7. Verify after the company publishes
```

## Files

| File | Use |
|---|---|
| `references/intake.md` | Questions to ask before any work |
| `references/audit-checklist.md` | Items, each [auto] or [read], with a lens |
| `references/fields.md` | Every field, its limit, and its source role |
| `references/best-practices.md` | How each surface works well, tied to exemplars |
| `references/exemplars.md` | Real pages with links, measurements, and the date read |
| `references/how-to.md` | Step by step: what changes and who makes it live |
| `evals/evals.json` | Test scenarios |

## Changelog

- 0.1.0: first version.
````
