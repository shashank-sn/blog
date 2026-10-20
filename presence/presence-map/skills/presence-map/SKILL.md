---
name: presence-map
description: >-
  Maps every public place a company controls where buyers and AI tools read
  about it (GitHub, package and image registries, model hubs, docs, MCP and
  agent directories), sorts the places into one-time and recurring, audits the
  one-time places against the company's own sources, and drafts the fixes.
  Never publishes. Use when asked to audit a company's online presence, check
  what AI tools see about a company, or plan where a company should show up.
license: MIT
metadata:
  author: Shashank SN
  version: "1.1.0"
  source: https://github.com/shashank-sn/workflows
---

# Presence map

You help a company make its facts correct on every place it controls. You map the places, audit them, and draft fixes. A person at the company makes every change live.

## Rules

1. Do no audit and no drafting until intake is complete (step 1).
2. Every description of the company is one of its approved blocks, word for word. Do not write a new one.
3. Every number comes from the company's cleared numbers. If a number is not on that list, do not use it.
4. A technical fact with no source gets the mark `[engineer: <question>]`. Do not guess.
5. Never publish, submit, sign in, or open a pull request. Prepare the change and say who makes it live.
6. Audit the live page, not a document about the page. Record the URL and the date you read it.
7. If two sources disagree, list the conflict in the report. Do not pick one quietly.

## Workflow

Copy this list into your notes and check off each step.

```text
- [ ] 1. Intake: get the company's sources (references/sources-template.yaml)
- [ ] 2. Map: list every place, found and expected (references/places.md)
- [ ] 3. Sort: one-time or recurring, and a priority for each
- [ ] 4. Audit the one-time places (references/audit-checklist.md)
- [ ] 5. Find the best pages per place and note why they are good
- [ ] 6. Draft every fix from the sources
- [ ] 7. Write the report and hand it over
```

### 1. Intake

Ask the person for the items in `references/sources-template.yaml`. Accept a file, a repo that holds them, or answers in chat. Write the answers to `presence/sources.yaml`. If the approved descriptions or the cleared numbers are missing, stop and ask. Those two items are required.

Open each source URL and each account in the file. List any that do not load, and ask the person how to continue before step 2. A link that does not work now will be broken in every draft.

### 2. Map

Use `references/places.md` as the list of place types. For each type:

- Search for the company's page on that place. Use the company name, the product name, and the domain.
- Record what you find: URL, owner account, last update if visible.
- Record what is missing but expected. For example, a company that ships a container image and has no Docker Hub description.

Write the map to `presence/map.csv` with the columns `place, type, url, status, owner, cadence, priority, notes`. Use `status` values `live`, `stale`, `empty`, `missing`, or `not relevant`.

### 3. Sort

Set `cadence` to `one-time` (write it well once, check each quarter) or `recurring` (needs new posts or releases). Set `priority` from 1 to 3:

- 1: an agent or a buyer is likely to read it, and it is wrong or empty today.
- 2: it is read often and is only stale.
- 3: everything else.

Start with one-time places of priority 1.

### 4. Audit

For each one-time place, open the live page and check it against `references/audit-checklist.md`. Each item gets `PASS`, `FAIL`, or `WARN`, and one line of evidence (a quote or a measurement). Write the results to `presence/audit/<place>.md`.

If a place has `status: missing`, there is no page to audit. Record the check that shows it is missing (for example "HTTP 404 signed out"). Then draft the page to create in step 6, and add "create the account or page" to the engineering tasks with its owner.

### 5. Best pages

For each audited place, find at least five strong pages from companies in the same category. Pick the best three. For each one, write the URL, the date, and two or three concrete things that make it good, such as "first screen says what it does in one sentence" or "16 topics, all category and problem words". These become the bar for your draft.

### 6. Draft

Draft every field the place has. For each field, write the limit if the place has one, the text, and the source of the text (`approved block: short`, `cleared numbers: line 4`, `docs: /install`). Take each limit from the place's current official docs, with the URL and the date you read it. If you cannot read the docs, mark the limit `[unverified]`. Do not take a limit from memory. Check each draft against the best pages from step 5 and against the rules above. Write the drafts to `presence/drafts/<place>.md`.

### 7. Report

Write `presence/report.md`:

1. The map summary: counts by status and cadence.
2. Per place: a verdict (`fix now`, `fix later`, `fine`), the failed audit items, and a link to the draft.
3. Engineering tasks: changes that need a commit, a release, or an admin setting.
4. Conflicts between sources, and open `[engineer: ...]` questions.
5. For each fix, who makes it live and the exact steps.

End with the reminder that nothing in the report is live yet.

## Files

| File | Use |
|---|---|
| `references/sources-template.yaml` | The intake questions, in the form of a file the company fills in |
| `references/places.md` | Place types to check, and what matters on each |
| `references/audit-checklist.md` | The audit items, each with a lens |

## Changelog

- 1.1.0: after a clean test with a fresh agent. Intake now checks that every source URL loads. Missing places get a draft page and a "create" task. Field limits must come from current docs, not memory.
- 1.0.0: first version.
