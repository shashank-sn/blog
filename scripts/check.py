"""Checks the workflows repo before merge.

- the marketplace lists every workflow, and each plugin has a valid plugin.json and SKILL.md
- plugin versions match their SKILL.md versions
- every relative link and image in every Markdown file resolves
- every workflow is listed on its topic page and on the home page
- every SVG figure parses and has a white background (readable in GitHub dark mode)
- every page title (the first heading) is lowercase
- every figure .svg is up to date with its .mmd source (CI runs npm run figures:check)
- no site files (HTML, CSS, Jekyll config) are left in the repo

Usage: python3 scripts/check.py
"""
import glob
import json
import os
import re
import sys
import xml.dom.minidom

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOPICS = ["build", "write", "research", "operate", "presence"]
errors = []


SKIP = ("node_modules/", ".")


def tracked(paths):
    return [p for p in paths if not p.startswith(SKIP) and "/node_modules/" not in p]


def read(path):
    return open(os.path.join(ROOT, path), encoding="utf-8").read()


def skill_version(skill_md):
    match = re.search(r'^\s*version:\s*"([\d.]+)"', skill_md, re.M)
    return match.group(1) if match else None


def check_plugins():
    market = json.loads(read(".claude-plugin/marketplace.json"))
    listed = set()
    for plugin in market.get("plugins", []):
        name, source = plugin["name"], plugin["source"].lstrip("./")
        listed.add(source)
        manifest = os.path.join(source, ".claude-plugin", "plugin.json")
        skill = os.path.join(source, "skills", name, "SKILL.md")
        if not os.path.exists(os.path.join(ROOT, manifest)):
            errors.append(f"{name}: {manifest} is missing")
            continue
        if not os.path.exists(os.path.join(ROOT, skill)):
            errors.append(f"{name}: {skill} is missing")
            continue
        pj = json.loads(read(manifest))
        if pj.get("name") != name:
            errors.append(f"{name}: plugin.json name is {pj.get('name')!r}")
        version = skill_version(read(skill))
        for label, value in (("plugin.json", pj.get("version")), ("marketplace.json", plugin.get("version"))):
            if value != version:
                errors.append(f"{name}: {label} version {value} does not match SKILL.md version {version}")
        if not re.search(rf"^name:\s*{re.escape(name)}\s*$", read(skill), re.M):
            errors.append(f"{name}: SKILL.md front matter name is not {name}")
    on_disk = {os.path.dirname(os.path.dirname(p)) for p in glob.glob("*/*/.claude-plugin/plugin.json", root_dir=ROOT)}
    for missing in sorted(on_disk - listed):
        errors.append(f"{missing}: has a plugin.json but is not in the marketplace")
    return sorted(listed)


def check_links():
    for md in tracked(glob.glob("**/*.md", root_dir=ROOT, recursive=True)):
        text = read(md)
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        targets = re.findall(r"\]\(([^)\s]+)\)", text) + re.findall(r'<img[^>]+src="([^"]+)"', text)
        for target in targets:
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            path = os.path.normpath(os.path.join(os.path.dirname(md), target.split("#")[0]))
            if not os.path.exists(os.path.join(ROOT, path)):
                errors.append(f"{md}: link to {target} does not resolve")


def check_listings(workflows):
    home = read("README.md")
    for wf in workflows:
        topic, name = wf.split("/")
        if f"]({name}/README.md)" not in read(f"{topic}/README.md"):
            errors.append(f"{wf}: not listed on {topic}/README.md")
        if f"]({wf}/README.md)" not in home:
            errors.append(f"{wf}: not listed on the home README")
        if f"@shashank-workflows" in home and f"/plugin install {name}@" not in home:
            errors.append(f"{wf}: no install line on the home README")


def check_figures():
    for svg in glob.glob("*/*/figures/*.svg", root_dir=ROOT):
        try:
            xml.dom.minidom.parse(os.path.join(ROOT, svg))
        except Exception as exc:  # noqa: BLE001 - report any parse failure
            errors.append(f"{svg}: does not parse ({exc})")
            continue
        if 'class="paper"' not in read(svg):
            errors.append(f"{svg}: no white background rect (unreadable in dark mode)")


def check_titles():
    for md in ["README.md"] + tracked(glob.glob("*/README.md", root_dir=ROOT) + glob.glob("*/*/README.md", root_dir=ROOT)):
        match = re.search(r"^#{1,2} (.+)$", read(md), re.M)
        if not match:
            errors.append(f"{md}: no title")
        elif match.group(1) != match.group(1).lower():
            errors.append(f"{md}: title is not lowercase")


def check_no_site_files():
    for pattern in ("**/*.html", "**/*.css", "_config.yml", "_layouts", "_includes", "_posts"):
        for hit in tracked(glob.glob(pattern, root_dir=ROOT, recursive=True)):
            errors.append(f"{hit}: site file left in the repo")


def main():
    workflows = check_plugins()
    check_links()
    check_listings(workflows)
    check_figures()
    check_titles()
    check_no_site_files()
    for e in errors:
        print("FAIL", e)
    print(f"{len(errors)} problem(s)" if errors else f"all checks passed ({len(workflows)} workflows)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
