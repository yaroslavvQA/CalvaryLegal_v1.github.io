import pathlib
import re

base = pathlib.Path("public_html")
scripts_dir = base / "Scripts"
scripts_dir.mkdir(parents=True, exist_ok=True)

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

script_path = scripts_dir / "scripts.js"
collected = []

for html in html_files:
    page = base / html
    content = page.read_text(encoding="utf-8")
    blocks = re.findall(r"<script>(.*?)</script>", content, flags=re.S)
    if blocks:
        collected.append(f"/* {html} */")
        collected.extend(blocks)
    if 'src="public_html/Scripts/scripts.js"' not in content:
        if "</body>" in content:
            content = content.replace(
                "</body>",
                '  <script src="public_html/Scripts/scripts.js"></script>\n</body>',
                1,
            )
        else:
            content += '\n<script src="public_html/Scripts/scripts.js"></script>\n'
        page.write_text(content, encoding="utf-8")

script_path.write_text("\n\n".join(collected), encoding="utf-8")