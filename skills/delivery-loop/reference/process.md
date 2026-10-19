# Process notes

## Right-size

| Change | Stages |
|---|---|
| Typo, copy, config value | 1, 5, 9, 11 |
| Small bug with a local test target | 1, 2 (only if unclear), 5, 8, 9, 10, 11 |
| Feature inside one module | All, with a short spec |
| Crosses a boundary (schema, API, auth, billing) | All, full spec, slices |

Stages 9 and 11 never drop out.

## Grill: the question tree

Write the open questions as a tree, where answering a parent can remove its children. Ask only the current frontier (the questions whose parents are answered). For each, give your recommended answer and why. Before asking, search the code: a question the code can answer is not a question for the person.

## Slices

A good slice:

- crosses every layer the feature needs (schema, API, UI, tests),
- can be demoed alone,
- fits in one fresh context window,
- has one acceptance line that a test can check.

A bad slice: "add the database table" (one layer, nothing to demo).

## Two axes

| Axis | Question | Typical findings |
|---|---|---|
| Standards | Does it meet the repo's conventions and design rules? | naming, dependency direction, test strength, dead code |
| Spec | Does it do what the spec says? | missing story, wrong edge case, scope creep |

A clean diff that solves the wrong problem fails Spec. A correct diff with a naming issue passes Spec and gets a Standards note. Report both. Never average them.

## Plain-English PR body

1. What changes for the user, in one or two sentences.
2. Why, linked to the request.
3. How to check it: the steps a reviewer can follow.
4. Evidence: the `verify.md` table.
5. Known gaps: anything `NOT_RUN`, `NOT_AVAILABLE`, or out of scope.
