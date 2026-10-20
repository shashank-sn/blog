# Example input (synthetic)

Repo: a small notes app. Base `main` at `a1b2c3d`, head `feature/archive` at `e4f5a6b`.

Spec (`specs/archive.md`):

1. A user can archive a note. Archived notes leave the main list.
2. A user can see archived notes on an Archive page.
3. Archiving a note that is already archived does nothing and returns success.

The diff adds `archive(note_id)` that sets `archived = true`, filters archived notes out of the main list, and adds tests for requirement 1. The code is clean and follows the repo's style guide.
