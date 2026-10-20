"""Lowercase a post's prose. Keeps code spans, fenced code, URLs, and front-matter keys and paths."""
import re, sys

KEEP = re.compile(r"(```.*?```|`[^`]*`|\]\([^)]*\)|https?://\S+|\{%.*?%\}|\{\{.*?\}\}|<[^>]+>)", re.S)

def lower_prose(text):
    parts = KEEP.split(text)
    return "".join(p if KEEP.fullmatch(p) else p.lower() for p in parts)

def lower_front_matter(fm):
    out = []
    for line in fm.splitlines():
        m = re.match(r"^(\s*)(title|description|summary):\s*(.*)$", line)
        out.append(f"{m.group(1)}{m.group(2)}: {lower_prose(m.group(3))}" if m else line)
    return "\n".join(out)

for path in sys.argv[1:]:
    src = open(path).read()
    _, fm, body = src.split("---\n", 2)
    open(path, "w").write("---\n" + lower_front_matter(fm.rstrip("\n")) + "\n---\n" + lower_prose(body))
    print("lowercased", path)
