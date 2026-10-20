---
name: deliverable-audit
description: >-
  Audits a library of digital products for broken or missing delivery links.
  Classifies every review, maps each complaint to the deliverable it is about,
  finds the canonical file, fixes the link at the source, verifies each fix
  logged out (opens, right file type, right content), drafts a reply for every
  relevant review, and reports honest counts with the gaps that remain. Use
  when asked to "audit product links", "fix the delivery links", or "check the
  free products".
license: MIT
metadata:
  author: Shashank SN
  version: "1.1.0"
  source: https://github.com/shashank-sn/blog
---

# Deliverable audit

A broken link is a content bug with a customer attached. Fix it in the product, not just in one conversation, and count honestly.

## When to use this

- "audit the links in my products"
- "fix the delivery links people are complaining about"
- "check the free products still deliver"

## What you need

- The product list: name, product page URL, and delivery method (download, email, link in content).
- An export of every review and rating, with product and star count. Text if any.
- Where the files live (a drive, a docs workspace, a repo), with read access.
- Optional: a map of old titles to current titles, and the reply policy.

## The process

1. **Inventory.** Load every product and every review into `audit/inventory.csv`.
2. **Classify.** Tag each review `complaint`, `praise`, or `bare` (a rating with no text). Read five-star reviews too; tag a five-star review with a link problem as `complaint`.
3. **Map.** For each complaint about delivery, name the product and the deliverable the customer expected.
4. **Check as a customer.** Open each product page and its delivery path in a logged-out browser. Record what happens.
5. **Find the canonical file.** Search the file source by current title, old titles, and content. Not only by exact filename.
   Stop if: two candidates exist, or the only candidate looks incomplete (empty, a header row only, or a placeholder). Ask which file is canonical.
6. **Prepare the fix.** Write the new link and where it must change (product content, delivery email, file sharing setting) to `audit/fixes.md`. Change the product only if the person gave you access and said to; otherwise hand over the steps.
7. **Verify.** For each fixed link, logged out: it opens with no sign-in or access request, the file type matches the product page, and the content is the current version of what the page promised. Record all three in `audit/verify.md`.
   Stop if: any of the three fails. The fix is not done.
8. **Draft replies.** One per relevant review, with the working link. Same wording each time if that is the policy. Save to `audit/replies.md`. Do not post them; the person does.
9. **Report.** Write `audit/report.md` with the full counts (`reference/checklist.md`) and the residual gaps.

## What good looks like

See `examples/input.md` and `examples/output.md`.

## Guardrails

- Never call a link fixed without opening it logged out.
- Never treat an HTTP 200 as proof of the right file.
- Never raise or lower a count to make the report look better. Bare ratings are `unreadable`, not `fine`.
- No customer names, emails or order IDs in any report meant for publication.
- Do not post replies or change products unless the person told you to, for that action.

## Output format

```text
audit/
  inventory.csv   product, review id, stars, tag, deliverable
  fixes.md        product | old link | new link | where it changes
  verify.md       link | opens | file type | content | result
  replies.md      review id | reply text
  report.md       counts, fixed, still missing, unreadable, next steps
```

## Changelog

- 1.1.0: after a clean test with a fresh agent. A candidate that looks incomplete needs the person's confirmation before it counts as canonical.
- 1.0.0: first version.

## Failure modes

- **The file is gone:** list it as `missing` with the last known title and date. Suggest rebuild or retire.
- **No review export:** audit the product pages anyway and say the complaint side is unknown.
- **No logged-out browser available:** mark every fix `NOT_VERIFIED`. Do not report it as fixed.
