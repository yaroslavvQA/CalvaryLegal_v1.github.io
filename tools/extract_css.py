import re
import pathlib

mapping = {
    "index.html": "index.css",
    "practice-areas.html": "practice-areas.css",
    "our-approach.html": "our-approach.css",
    "our-network.html": "our-network.css",
    "attorney.html": "attorney.css",
    "jurisdictions.html": "jurisdictions.css",
    "cross-border.html": "cross-border.css",
    "privacy.html": "privacy.css",
}

base = pathlib.Path("public_html")

for html, css in mapping.items():
    page = base / html
    content = page.read_text(encoding="utf-8")
    match = re.search(r"<style>(.*?)</style>", content, flags=re.S)
    if not match:
        continue
    (base / css).write_text(match.group(1), encoding="utf-8")
    link = f'<link rel="stylesheet" href="{css}"/>'
    content = re.sub(r"<style>.*?</style>", link, content, count=1, flags=re.S)
    page.write_text(content, encoding="utf-8")