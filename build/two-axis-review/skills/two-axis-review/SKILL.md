---
name: two-axis-review
description: >-
  Reviews a diff on two independent axes and reports them side by side:
  Standards (the repo's documented conventions plus a baseline of twelve code
  smells) and Spec (does the change implement the issue, ticket or spec, traced
  requirement by requirement to code and tests). Read-only. Use when asked to
  "review this diff", "review the PR", or run a "two-axis review".
license: MIT
metadata:
  author: Shashank SN
  version: "1.0.0"
  source: https://github.com/shashank-sn/workflows
---

# Two-axis review

One review pass cannot answer both "is this good code?" and "is this the right code?". This skill runs two passes with separate inputs and keeps their reports apart. A change can pass one axis and fail the other.

## When to use this

- "review this diff" or "review the PR"
- "run a two-axis review on this branch"
- before merge, when a change came from a coding agent

## What you need

- The repo path.
- A base revision and a head revision (commit, branch, tag, or merge-base).
- Optional: the spec (a path, an issue reference, or a spec file).
- Read access only. This skill never edits product code.

## The process

1. **Pin the fixed point.** Resolve base and head to commit hashes. Write them to `review/inventory.md`.
   Stop if: either revision does not resolve, or the diff is empty.
2. **Find the spec.** Look, in this order, for: a path the person gave, issue references in commit messages, a spec file whose name matches the branch. Record where it came from.
   If none: write "Spec axis skipped: no spec found" and run the Standards axis only. Do not guess the requirements from the code.
   If the spec was added or changed inside the same diff, say so in the inventory. A spec written with the code may describe the code instead of the need, so ask the person to confirm it is the agreed version.
3. **Inventory.** List every changed file with its change type (added, modified, deleted, renamed) in `review/inventory.md`.
4. **Standards pass.** Read the repo's rules first (`CONTRIBUTING`, `AGENTS.md`, `CLAUDE.md`, style docs, lint config). Then check the smell baseline in `reference/process.md`. Skip anything the repo's tooling already enforces.
5. **Spec pass.** Number every requirement in the spec. For each, find the call path that implements it, then the tests for its happy path, boundary, negative, failure and recovery cases (`reference/process.md`, "Tracing a requirement").
6. **Independence.** Run step 4 and step 5 in separate fresh contexts (subagents or separate sessions). The Standards reviewer gets the diff and the repo rules. The Spec reviewer gets the diff and the spec. Neither gets the other's findings or your reasoning. If you cannot, write "not independent" at the top of `review/report.md`.
7. **Write findings.** Every finding has: location (`file:line`), consequence (what goes wrong because of it), severity (`BLOCKING`, `IMPROVEMENT`, `ADVISORY`), confidence, the smallest bounded fix, and disposition (`open`, `fixed`, `accepted`, `dismissed` with reason).
8. **Report.** `review/report.md` has two sections, Standards and Spec, under separate headings. Each ends with one line naming its worst issue. Never merge the sections, average them, or rank one above the other.
9. **Re-review after fixes.** A fix changes the head revision. Run both passes again on the new head.

## What good looks like

See `examples/input.md` and `examples/output.md`: a diff that passes Standards and fails Spec.

## Guardrails

- Read-only. No edits to product code, tests or config.
- No single verdict across the axes.
- No finding from taste alone. A smell is a finding only with a consequence in this change.
- No quota. Zero findings on an axis is a valid result; say so.
- An open `BLOCKING` finding stays blocking. Accepted risk does not downgrade it.
- Never invent requirements when there is no spec.

## Output format

```text
review/
  inventory.md   base, head, spec source, changed files
  report.md      ## Standards (findings table, worst issue)
                 ## Spec (requirement trace table, findings table, worst issue)
```

Findings table columns: `id | location | consequence | severity | confidence | fix | disposition`.

## Failure modes

- **No spec:** Standards only, with the skip stated in the report.
- **Spec is vague:** list the requirements you could number, mark the rest `unclear`, and report them as Spec findings with `confidence: low`.
- **Diff too large to read in one context:** split the inventory into groups by module and run the passes per group. Report per group, then the worst issue per axis across groups.

## Changelog

- 1.0.0: first version.
