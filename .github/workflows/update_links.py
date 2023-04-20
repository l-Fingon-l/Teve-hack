import re

html_file_read = "src/web-client/main.html"

with open(html_file, "r") as f:
    html_content = f.read()

patterns = [
    (r'src="\.\./', 'src="'),
    (r'src="brython/', 'src="'),
    (r'brython\(\d\)', 'brython(0)')
    (r'src="../../teveFMapOverview_all.png', 'minimap.png'),
]

for pattern, replacement in patterns:
    html_content = re.sub(pattern, replacement, html_content)

with open(html_file, "w") as f:
    f.write(html_content)
