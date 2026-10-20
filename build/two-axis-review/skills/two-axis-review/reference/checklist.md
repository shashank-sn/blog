# Checklist

## Before the passes

- [ ] Base and head resolve to commit hashes.
- [ ] The diff is not empty.
- [ ] The spec source is recorded, or the Spec skip is stated.
- [ ] The changed-file inventory is complete.

## Each pass

- [ ] Ran in its own context, or the report says "not independent".
- [ ] Every finding has location, consequence, severity, confidence, fix and disposition.
- [ ] No finding from taste alone.
- [ ] One line names the worst issue.

## Spec pass only

- [ ] Every requirement is numbered and has a row in the trace table.
- [ ] Every `n/a` cell has a reason.

## Report

- [ ] Standards and Spec under separate headings.
- [ ] No merged score, no ranking across axes.
- [ ] Open `BLOCKING` findings are still `BLOCKING`.
- [ ] No product code was changed.
