---
name: delivery-loop
description: >-
  Runs a code change from request to an open pull request through eleven gated
  stages (route, grill, spec, slices, build, simplify, prune, dogfood, verify at
  the revision, two-axis review, ship) and leaves evidence at each stage. Stops
  before merge. Use when asked to "run the delivery loop", "build this
  properly", or "ship this end to end".
license: MIT
metadata:
  author: Shashank SN
  version: "1.0.0"
  source: https://github.com/shashank-sn/blog
---

# Delivery loop

Most coding-agent failures are skipped stages. This skill runs every stage that the change needs, and records the evidence each stage leaves.

## When to use this

- "run the delivery loop on this"
- "build this properly" or "ship this end to end"
- any change that crosses a boundary (schema, API, UI, billing, auth)

## What you need

- The request, in the person's words.
- The repo path and the base branch.
- The verification commands the repo declares (test, typecheck, lint, build). If none are declared, find the native ones and say so.
- The kinds of users the change affects (for dogfooding).
- Permission to commit and push to a feature branch. Merge is never part of this skill.

## The process

Each stage has a stop condition. Do not start a stage while the one before it is stopped.

1. **Route.** Classify type, risk, ambiguity and boundaries crossed. Pick the stages this change needs (`reference/process.md`, "Right-size"). Write the route to `loop/route.md`.
   Stop if: the request names no outcome you can check.
2. **Grill.** List the open design questions as a tree. Ask the whole current set in one message, with your recommended answer for each. Find facts in the code yourself; never ask for them.
   Stop if: any question that changes the design is unanswered.
3. **Spec.** Write `loop/spec.md`: problem, solution, numbered user stories, implementation decisions, testing decisions, out of scope.
   Stop if: a user story has no testable acceptance line.
4. **Slices.** Cut vertical slices: each one crosses every layer it needs, is demoable, and fits one fresh context. Write `loop/slices.md`.
   Stop if: a slice touches only one layer and cannot be demoed.
5. **Build.** One slice at a time. Write a failing test, make the smallest change that passes it, repeat. Run the typecheck and the affected test file often. Run the full suite once at the end.
   Stop if: a test passes before the change (it does not test the change).
6. **Simplify.** Reuse existing utilities, remove state you do not need, flatten deep conditionals, delete dead code. Behaviour must not change. Rerun the affected tests.
   Stop if: any test changes result.
7. **Prune.** Run the repo's dead-code detector if it has one. Confirm every candidate with a reference search. Keep exports, routes, reflection targets, dependency-injection targets and generated code.
   Stop if: a candidate has any reference you cannot explain.
8. **Dogfood.** Walk each user journey the diff touches, as each kind of user, including error, empty, boundary and permission branches. Write `loop/dogfood.md` with failures and paper cuts in separate lists.
   Stop if: any functional failure is open.
9. **Verify at the revision.** Run every declared check on the current commit. Record each result with one of seven states and the commit hash (`reference/checklist.md`).
   Stop if: any required check is not `PASS`.
10. **Two-axis review.** Review the diff twice, separately: Standards (repo conventions, design, tests) and Spec (does it do what `loop/spec.md` says). Report both side by side in `loop/review.md`. Do not merge or rank them.
    Stop if: either axis has a blocking finding.
11. **Ship.** Commit in logical units, push the feature branch, open a PR with a plain-English body, watch CI, and record the result. Write one line on what you learned in `loop/lesson.md`.
    Stop: always, before merge. Merge needs the person's approval.

## What good looks like

See `examples/input.md` and `examples/output.md` for one request taken through every stage.

## Guardrails

- No build before the spec is settled.
- No test at a seam you have not confirmed exists.
- No ship without a check bound to the current commit.
- No deletion without a reference search.
- No review that blends the Standards and Spec axes.
- Never turn a missing, stale or errored check into `PASS`.
- Never merge, deploy, or force-push.

## Output format

A `loop/` folder in the repo (or the session scratchpad if the repo forbids it):

```text
loop/
  route.md      type, risk, stages chosen and why
  spec.md       the spec
  slices.md     slices with their acceptance lines
  dogfood.md    journeys walked, failures, paper cuts
  verify.md     check | command | state | commit
  review.md     standards findings | spec findings
  pr.md         the PR body as opened
  lesson.md     one line
```

## Failure modes

- **Request too vague:** stay in stage 2. Ask the question tree. Do not guess.
- **No declared checks:** record them as `NOT_CONFIGURED`, run the native ones, and say so in the PR.
- **A check cannot run here:** record `NOT_AVAILABLE` with the reason. It blocks ship if it is required.
- **The change is tiny:** route says look, change, check. Stages 9 and 11 still apply.
