import json
import re
from jinja2 import Environment, FileSystemLoader, select_autoescape

input_path = "data.json"
output_path = "index.html"

with open(input_path, "r", encoding="utf-8") as f:
    data = json.load(f)


def bold_bracketed(text):
    pattern = r"\[(.*?)\]"
    replacement = r"<strong>\1</strong>"
    result = re.sub(pattern, replacement, text)
    return result


env = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape(["html", "xml"]),
)
env.filters["bold_bracketed"] = bold_bracketed
template = env.get_template("template.html")
rendered_html = template.render(data=data)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(rendered_html)

print(f"Generated {output_path}")
