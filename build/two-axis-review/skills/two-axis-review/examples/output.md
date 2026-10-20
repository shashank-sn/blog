# Example output (synthetic, abridged)

## inventory.md

Base `a1b2c3d`, head `e4f5a6b`. Spec: `specs/archive.md` (matches branch name). Changed: `notes/store.py` (modified), `notes/views.py` (modified), `tests/test_archive.py` (added).

## report.md

### Standards

No findings. The change follows the style guide, and the smell baseline found nothing with a consequence in this change.

Worst issue: none.

### Spec

| Req | Call path | Happy | Boundary | Negative | Failure | Recovery | Finding |
|---|---|---|---|---|---|---|---|
| 1 | `views.py:40` → `store.py:22` | yes | no (last note) | no (other user's note) | n/a (in-memory store) | n/a | S2, S3 |
| 2 | none | no | no | no | n/a | n/a | S1 |
| 3 | `store.py:22` sets the flag again | no | no | no | n/a | n/a | S4 |

| id | location | consequence | severity | confidence | fix | disposition |
|---|---|---|---|---|---|---|
| S1 | `notes/views.py` | Archived notes cannot be seen anywhere. Requirement 2 is not met. | BLOCKING | high | Add an Archive view that lists `archived = true` notes for the user | open |
| S2 | `tests/test_archive.py` | No test archives the last note, so the empty main list is untested | IMPROVEMENT | medium | Add a test that archives the only note | open |
| S3 | `notes/store.py:22` | Any user can archive any note id. No owner check. | BLOCKING | high | Check the note's owner before archiving; add a negative test | open |
| S4 | `tests/test_archive.py` | Requirement 3 has no test | IMPROVEMENT | high | Add a test that archives twice and expects success | open |

Worst issue: S1, requirement 2 is not implemented.
