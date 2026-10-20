---
name: skill-from-setup
description: >-
  Turns a one-time setup on one public place (a GitHub README, a registry
  listing, a directory entry, a profile page) into a reusable agent skill that
  any company can run. Audits real pages on that place first, splits objective
  rules from company-specific sources, writes the SKILL.md and its reference
  files, and tests the skill with a fresh agent. Use when asked to make a skill,
  playbook, or repeatable process for a platform, listing, or profile.
license: MIT
metadata:
  author: Shashank SN
  version: "1.1.0"
  source: https://github.com/shashank-sn/workflows
---

# Skill from setup

You build a skill for one place, for example "Docker Hub repo pages" or "a Hugging Face organization page". The skill you build must work for any company. The company's own words never go in it.

## The split

Every decision in the skill you build is one of two kinds.

- **Objective:** true for every company on this place. Field limits, what the best pages do, the audit items, the steps to make a change live. These go in the skill.
- **Subjective:** different per company. Tone, approved descriptions, cleared numbers, product facts. These stay with the company. The skill only names where to find them.

Test each line you write: "Would this line be wrong for a different company?" If yes, it is subjective. Replace it with a pointer to a source.

## Workflow

```text
- [ ] 1. Name the place and its surfaces
- [ ] 2. Read the official docs for the place (date each one)
- [ ] 3. Audit real pages and pick exemplars (references/exemplar-research.md)
- [ ] 4. Write the rules: objective only
- [ ] 5. Write the skill files (references/skill-template.md)
- [ ] 6. Write test scenarios
- [ ] 7. Run a clean test with a fresh agent (references/clean-test.md)
- [ ] 8. Fix what the test found, then test again
```

### 1. Name the place

Write one sentence that names the place. Then list every surface on it that a reader sees: fields, boxes, cards, badges, linked files. Ask the person if any surface is out of scope.

### 2. Read the docs

Read the place's current official docs: field limits, required files, review rules, and how a change goes live. Save the URL and the date for each page. If a doc and a live page disagree, record both.

### 3. Exemplars

Follow `references/exemplar-research.md`. The result is a table of three to seven strong pages, each with a URL, a date, and the concrete things that make it good.

### 4. Rules

From steps 2 and 3, write:

- The fields, each with its limit and its source role (for example `one-line approved block`, `docs install page`).
- Best practices, each tied to at least one exemplar.
- Audit items. Each item is one testable sentence, marked `[auto]` (a script can check it) or `[read]` (a person or agent must read it), with a lens: Live, Accurate, On message, Current, or Level.
- The go-live steps: what changes, where, and who makes it live.

Do not include any company's facts. Use placeholders such as `<one-line approved block>`.

### 5. Skill files

Use `references/skill-template.md`. Keep SKILL.md under 500 lines. Put detail in `references/`, one level deep. Put scripts in `scripts/`. The skill you build must keep these rules:

1. No work before intake.
2. Every company description is an approved block, word for word.
3. Every number comes from the cleared list.
4. A fact with no source gets `[engineer: <question>]`.
5. Nothing goes live from the operator's side.

### 6. Test scenarios

Write `evals/evals.json` with at least three scenarios: a company with full sources, a company with a missing required source (the skill must stop and ask), and a company whose sources disagree (the skill must report the conflict). Put the sources for each scenario in `evals/fixtures/`, for an invented company. Never use a real client's facts in a fixture.

If the skill has scripts, run each script once against a fixture before step 7. A script that has never run is not ready for a clean test.

### 7. Clean test

Follow `references/clean-test.md`. A fresh agent runs the skill in an empty folder with only the skill and one company's sources.

### 8. Fix and repeat

For each problem the test finds, decide: is the skill unclear, or is a rule missing? Fix the skill, add a check that would catch the problem, and run the clean test again. Record each fix in a short changelog at the end of SKILL.md.

## Files

| File | Use |
|---|---|
| `references/exemplar-research.md` | How to find and judge the best pages on a place |
| `references/skill-template.md` | The SKILL.md skeleton for the skill you build |
| `references/clean-test.md` | How to run and judge the clean test |

## Changelog

- 1.1.0: after a clean test with a fresh agent. Exemplar measurements must come from raw pages or API responses. Test fixtures use an invented company. Scripts must run once against a fixture before the clean test.
- 1.0.0: first version.
