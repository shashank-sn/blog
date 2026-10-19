"""Checks the blog before merge.

Source checks (always):
  - every skill folder has a zip in downloads/ whose files match the folder byte for byte
  - every post names a skill whose folder and zip exist
  - post titles and descriptions are lowercase
  - no post file name carries a future date (UTC), which Jekyll would skip

Built-site checks (when a _site folder is given):
  - every post page was built
  - every internal href and src in the built pages resolves to a file

Usage: python3 scripts/check_site.py [path/to/_site]
"""
import os
import re
import sys
import zipfile
from datetime import datetime, timezone
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASEURL = "/blog"
errors = []


def front_matter(path):
    text = open(path, encoding="utf-8").read()
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return match.group(1) if match else ""


def field(fm, name):
    match = re.search(rf"^\s*{name}:\s*(.+)$", fm, re.M)
    return match.group(1).strip() if match else None


def check_skills_and_zips():
    skills_dir = os.path.join(ROOT, "skills")
    for name in sorted(os.listdir(skills_dir)):
        folder = os.path.join(skills_dir, name)
        if not os.path.isdir(folder):
            continue
        zip_path = os.path.join(ROOT, "downloads", f"{name}.zip")
        if not os.path.exists(zip_path):
            errors.append(f"skill {name}: downloads/{name}.zip is missing (run scripts/build-zips.sh)")
            continue
        on_disk = {}
        for dirpath, _, files in os.walk(folder):
            for f in files:
                if f == ".DS_Store":
                    continue
                full = os.path.join(dirpath, f)
                on_disk[os.path.relpath(full, skills_dir)] = open(full, "rb").read()
        with zipfile.ZipFile(zip_path) as z:
            in_zip = {n: z.read(n) for n in z.namelist() if not n.endswith("/")}
        if on_disk != in_zip:
            stale = sorted(set(on_disk) ^ set(in_zip)) or sorted(k for k in on_disk if on_disk[k] != in_zip.get(k))
            errors.append(f"skill {name}: zip does not match folder ({', '.join(stale[:5])}); run scripts/build-zips.sh")
        if not os.path.exists(os.path.join(folder, "SKILL.md")):
            errors.append(f"skill {name}: SKILL.md is missing")


def check_posts():
    posts_dir = os.path.join(ROOT, "_posts")
    slugs = []
    for f in sorted(os.listdir(posts_dir)):
        if not f.endswith(".md"):
            continue
        fm = front_matter(os.path.join(posts_dir, f))
        if f[:10] > datetime.now(timezone.utc).strftime("%Y-%m-%d"):
            errors.append(f"{f}: date is in the future (UTC), so Jekyll will not build it")
        for key in ("title", "description"):
            value = field(fm, key)
            if not value:
                errors.append(f"{f}: no {key}")
            elif value != value.lower():
                errors.append(f"{f}: {key} is not lowercase")
        if not field(fm, "lane"):
            errors.append(f"{f}: no lane, so the home page will not list it")
        skill = field(fm, "name")
        zip_path = field(fm, "zip")
        if not skill or not zip_path:
            errors.append(f"{f}: no skill name or zip")
        else:
            if not os.path.isdir(os.path.join(ROOT, "skills", skill)):
                errors.append(f"{f}: skill folder skills/{skill} is missing")
            if not os.path.exists(os.path.join(ROOT, zip_path.lstrip("/"))):
                errors.append(f"{f}: {zip_path} is missing")
        slugs.append(re.sub(r"^\d{4}-\d{2}-\d{2}-", "", f[:-3]))
    return slugs


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ("href", "src") and value:
                self.urls.append(value)


def check_built_site(site, slugs):
    for slug in slugs:
        if not os.path.exists(os.path.join(site, slug, "index.html")):
            errors.append(f"built site: page for post {slug} is missing")
    for dirpath, _, files in os.walk(site):
        for f in files:
            if not f.endswith(".html"):
                continue
            page = os.path.join(dirpath, f)
            parser = Links()
            parser.feed(open(page, encoding="utf-8").read())
            for url in parser.urls:
                path = url.split("#")[0].split("?")[0]
                if not path.startswith(BASEURL + "/") and path != BASEURL:
                    continue
                target = os.path.join(site, path[len(BASEURL):].lstrip("/"))
                if path.endswith("/") or os.path.isdir(target):
                    target = os.path.join(target, "index.html")
                if not os.path.exists(target):
                    errors.append(f"built site: {os.path.relpath(page, site)} links to {url}, which does not exist")


def main():
    check_skills_and_zips()
    slugs = check_posts()
    if len(sys.argv) > 1:
        check_built_site(sys.argv[1], slugs)
    for e in errors:
        print("FAIL", e)
    print(f"{len(errors)} problem(s)" if errors else "all checks passed")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
