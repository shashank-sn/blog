# Audit checklist

Run every item for each one-time place. Each item has a lens. Record `PASS`, `FAIL`, or `WARN`, with one line of evidence.

## Lenses

| Lens | Question |
|---|---|
| Live | Does the page exist, load, and show content to a signed-out visitor? |
| Accurate | Does every fact match the company's sources? |
| On message | Is every description one of the approved blocks, word for word? |
| Current | Does it describe the product as it ships today? |
| Level | Is it as good as the best three pages you found for this place? |

## Items for every place

- [ ] Live: the page loads signed out and is not a placeholder.
- [ ] Live: every link on the page works and points to the company's own domain or repo.
- [ ] Accurate: every number is on the cleared list.
- [ ] Accurate: product names, install commands and versions match the docs.
- [ ] On message: the description is an approved block, or the place has a limit shorter than every block (then use the one-line block and note the limit).
- [ ] On message: no word from `do_not_say` appears.
- [ ] Current: no feature, plan, or name that the company has retired.
- [ ] Current: the last update is within six months, or the text has no date-sensitive claim.
- [ ] Level: the first thing a reader sees says what the product does and for whom.
- [ ] Level: the page names the category in the words a buyer would search for.
- [ ] Level: there is one clear next step (install, docs, or contact).

## Extra items by place type

### Code hosting

- [ ] The README's first screen has a one-line description, an install command, and a link to docs.
- [ ] The About box has a description, a website, and topics with category and problem words.
- [ ] SECURITY.md says how to report a vulnerability.

### Registries

- [ ] The short description fits the limit and names the category.
- [ ] The long description links to docs and source.

### Agent surfaces

- [ ] Each tool or command has a description that says when to use it.
- [ ] The listing says what data the tool reads and writes.
- [ ] Install steps work as written in a clean environment.
