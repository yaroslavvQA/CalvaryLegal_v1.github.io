import pathlib

base = pathlib.Path("public_html")
css_dir = base / "CSS"
css_dir.mkdir(parents=True, exist_ok=True)

css_files = [
    "index.css",
    "practice-areas.css",
    "our-approach.css",
    "our-network.css",
    "attorney.css",
    "jurisdictions.css",
    "cross-border.css",
    "privacy.css",
]

combined = "\n\n".join(
    (base / css).read_text(encoding="utf-8")
    for css in css_files
    if (base / css).exists()
)
(css_dir / "styles.css").write_text(combined, encoding="utf-8")

html_files = [
    "index.html",
    "practice-areas.html",
    "our-approach.html",
    "our-network.html",
    "attorney.html",
    "jurisdictions.html",
    "cross-border.html",
    "privacy.html",
]

for html in html_files:
    page = base / html
    content = page.read_text(encoding="utf-8")
    for css in css_files:
        content = content.replace(
            f'href="{css}"',
            'href="public_html/CSS/styles.css"',
        )
    page.write_text(content, encoding="utf-8")