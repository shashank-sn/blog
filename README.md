# blog

Source for https://shashank-sn.github.io/blog/, built by GitHub Pages with Jekyll.

Each post comes with a skill you can download and run in Claude Code or any agent that reads skills.

## Publish a new post

1. Make a branch.
2. Add `_posts/YYYY-MM-DD-<slug>.md` with `layout: post`, `lane` (build, write, research, operate, presence), `order`, `title`, `description`, and `skill` (name, summary, zip). The date in the file name is never shown.
3. Add the skill folder in `skills/<name>/` and run `scripts/build-zips.sh`.
4. For a figure, add an SVG to `_includes/figs/` and include it in a `<figure class="fig">`.
5. Open a PR. The `Check` workflow builds the site with the Pages builder and runs `scripts/check_site.py`. The built site is attached to the run as the `site` artifact.
6. Merge. Pages publishes the post at `https://shashank-sn.github.io/blog/<slug>/`. Share that link.

All site text is lowercase. `scripts/lowercase.py` lowercases a post's prose and keeps code spans and links.

| Folder | What it holds |
|---|---|
| `_posts/` | The posts, in Markdown |
| `_includes/figs/` | Monochrome SVG figures |
| `skills/` | One folder per skill |
| `downloads/` | A .zip of each skill, linked from its post |
| `scripts/` | Zip builder, site check, lowercase helper |

Questions and problems go in [issues](https://github.com/shashank-sn/blog/issues). Only collaborators can open pull requests (repository setting).

Skills are MIT licensed. Posts are copyright Shashank SN.
