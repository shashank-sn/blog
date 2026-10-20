# Place types

Check every type. Mark a type `not relevant` only with a reason, for example "no container images".

## Code hosting

| Place | What to look at | Usual cadence |
|---|---|---|
| GitHub org page | Org description, profile README (`.github/profile/README.md`), pinned repos, verified domain | One-time |
| Main repo | README first screen, About box (description, website, topics), license, SECURITY.md | One-time |
| Releases | Release notes body, not only a tag; a changelog link | Recurring |
| GitLab or other hosts | Same as GitHub, if the company uses them | One-time |

## Package and image registries

| Place | What to look at | Usual cadence |
|---|---|---|
| Docker Hub | Org page, repo short description (100 characters), repo overview | One-time |
| Artifact Hub | Built from chart metadata (`Chart.yaml`, `artifacthub-pkg.yml`, README), so the fix is in the repo | One-time |
| PyPI, npm, crates.io, others | Package summary, long description, project URLs, keywords | One-time, checked per release |
| Helm, Terraform, or OS package indexes | Description and links from the package metadata | One-time |

## Model and dataset hubs

| Place | What to look at | Usual cadence |
|---|---|---|
| Hugging Face organization | Org card, avatar, links, collections, verified status | One-time |
| Model or dataset cards | Card text, license, tags, links back to docs | Recurring |

## Docs that agents read

| Place | What to look at | Usual cadence |
|---|---|---|
| Docs site | Home page, install page, first tutorial | One-time, checked per release |
| `llms.txt` or a docs MCP server | Whether it exists, whether it answers basic questions correctly | One-time |

## Agent surfaces

| Place | What to look at | Usual cadence |
|---|---|---|
| Public agent skill | A SKILL.md that teaches agents to install and use the product | One-time |
| Official MCP Registry | `server.json` entry, description, repo link | One-time |
| Claude connectors directory | Listing text, tools and their descriptions, policy links | One-time |
| Cursor Marketplace | Plugin listing built from the plugin manifest | One-time |
| Gemini CLI extensions gallery | Extension manifest and README in a public repo | One-time |

## Recurring places (map them, audit them later)

Company blog, changelog, community forums, social accounts, newsletters, conference talk pages. Record them in the map with `cadence: recurring`. This skill audits one-time places first.

Platforms change. Before you audit a place, read its current official docs and note the date.
