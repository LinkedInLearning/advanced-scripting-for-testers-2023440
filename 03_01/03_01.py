from jinja2 import Environment, FileSystemLoader

loader = FileSystemLoader("./")
env = Environment(loader=loader)
template = env.get_template("template.html")

results = [
    {"test": "Test 1", "status": "Pass"},
    {"test": "Test 2", "status": "Fail"},
    {"test": "Test 3", "status": "Skipped"},
]

rendered_template = template.render(results=results)

with open("output.html", "w") as f:
    f.write(rendered_template)
