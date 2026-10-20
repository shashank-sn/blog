# Process notes

## Smell baseline (Standards pass)

Check these after the repo's own rules. Report a smell only with its consequence in this change.

| Smell | What to look for |
|---|---|
| Mysterious name | A name that does not say what the thing does, or hides a side effect |
| Duplicated code | The same logic in two places that must change together |
| Feature envy | A function that uses another module's data more than its own |
| Data clumps | The same group of values passed around together without a type |
| Primitive obsession | Strings or numbers standing in for a domain concept with rules |
| Repeated switches | The same `switch`/`if` chain on a type in more than one place |
| Shotgun surgery | One change that forces edits in many unrelated files |
| Divergent change | One module that changes for many unrelated reasons |
| Speculative generality | Parameters, hooks or layers with no current caller |
| Message chains | `a.b().c().d()` reaching through objects it should not know |
| Middle man | A class or function that only forwards calls |
| Refused bequest | A subclass or implementation that ignores most of what it inherits |

## Tracing a requirement (Spec pass)

For each numbered requirement, fill one row:

| Req | Call path | Happy | Boundary | Negative | Failure | Recovery | Finding |
|---|---|---|---|---|---|---|---|

- **Call path:** the entry point to the code that does it, as `file:line` steps.
- **Happy:** a test of the normal case.
- **Boundary:** empty, zero, maximum, first and last.
- **Negative:** invalid input, wrong user, missing permission.
- **Failure:** a dependency fails or times out.
- **Recovery:** what state remains after a failure, and a retry.

A cell may be `n/a` only with a reason tied to the requirement. A missing call path, or a missing test where one applies, is a Spec finding.

## Severity

| Severity | Meaning |
|---|---|
| `BLOCKING` | Correctness, safety, a requirement not met, a required test missing |
| `IMPROVEMENT` | A real maintenance cost in this change, with a bounded fix |
| `ADVISORY` | Worth knowing, no change needed |
