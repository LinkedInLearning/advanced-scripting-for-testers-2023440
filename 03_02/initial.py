from jinja2 import Environment, FileSystemLoader

loader = FileSystemLoader("./")
env = Environment(loader=loader)
template = env.get_template("template.html")

results = [
    {"test": "Test 1", "status": "Passed"},
    {"test": "Test 2", "status": "Failed"},
    {"test": "Test 3", "status": "Skipped"},
    {"test": "Test 4", "status": "Passed"},
    {"test": "Test 5", "status": "Failed"},
    {"test": "Test 6", "status": "Failed"},
]

rendered_template = template.render(
    results=results, passed_count=2, failed_count=3, skipped_count=1
)

with open("output.html", "w") as f:
    f.write(rendered_template)
