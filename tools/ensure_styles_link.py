import pathlib

base = pathlib.Path("public_html")
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
    text = page.read_text(encoding="utf-8")
    text = text.replace('href="index.css"', 'href="public_html/CSS/styles.css"')
    text = text.replace('href="practice-areas.css"', 'href="public_html/CSS/styles.css"')
    text = text.replace('href="our-approach.css"', 'href="public_html/CSS/styles.css"')
    text = text.replace('href="our-network.css"', 'href="public_html/CSS/styles.css"')
    text = text.replace('href="attorney.css"', 'href="public_html/CSS/styles.css"')
    text = text.replace('href="jurisdictions.css"', 'href="public_html/CSS/styles.css"')
    text = text.replace('href="cross-border.css"', 'href="public_html/CSS/styles.css"')
    text = text.replace('href="privacy.css"', 'href="public_html/CSS/styles.css"')
    page.write_text(text, encoding="utf-8")