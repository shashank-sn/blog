# Example output (abridged)

## route.md

Feature, medium risk (new endpoint, reads user data), ambiguous format. Crosses API and UI. All stages, short spec.

## Grill (one message)

1. Format? Recommended: Markdown zip, one file per note. Reason: notes are already Markdown.
2. Scope: all notes, or a selection? Recommended: all notes first; selection later.
3. Size limit? Found in code: notes cap at 50 KB each, so a synchronous export is fine below 1,000 notes. Not asked.

## slices.md

1. `GET /export` returns a zip of all notes for the signed-in user, with a button on Settings. Acceptance: a user with 3 notes downloads a zip with 3 `.md` files.
2. Empty state: a user with 0 notes sees "nothing to export" and no download. Acceptance: no request is sent.

## verify.md

| Check | Command | State | Commit |
|---|---|---|---|
| tests | `npm test` | PASS | a1b2c3d |
| types | `npm run typecheck` | PASS | a1b2c3d |
| lint | `npm run lint` | PASS | a1b2c3d |
| e2e | (none declared) | NOT_CONFIGURED | a1b2c3d |

## review.md

| Standards | Spec |
|---|---|
| Zip helper duplicates `lib/archive.ts`; reuse it (fixed) | Signed-out visitor gets 500, spec says 401 (fixed, test added) |

## pr.md

Adds "export all notes" on Settings. Users get a zip with one Markdown file per note. To check: sign in, open Settings, click Export. Evidence: table above. Known gaps: no e2e suite in the repo.
