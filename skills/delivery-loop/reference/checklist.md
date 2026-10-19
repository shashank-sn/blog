# Checklist

## The seven states

| State | Meaning |
|---|---|
| `PASS` | Ran on this commit and passed |
| `FAIL` | Ran on this commit and failed |
| `NOT_RUN` | Exists and could run, but was not run |
| `NOT_AVAILABLE` | Cannot run in this environment (say why) |
| `NOT_CONFIGURED` | The repo does not declare this check |
| `STALE` | Ran, but on an older commit |
| `ERROR` | Started and crashed before a result |

Only `PASS` on the current commit counts as a pass. Every other state is reported as itself.

## Before ship

- [ ] Every user story in `spec.md` maps to a test or a dogfood step.
- [ ] Every required check is `PASS` at the current commit hash.
- [ ] `dogfood.md` has no open functional failure.
- [ ] `review.md` has no blocking finding on either axis.
- [ ] Every deleted symbol had a reference search.
- [ ] The PR body lists known gaps.
- [ ] No secrets, `.env` files, or build artefacts are staged.
