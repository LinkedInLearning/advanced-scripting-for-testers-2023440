import random

from jinja2 import Environment, FileSystemLoader


def get_test_cases(count=25):
    statuses = ["Passed", "Passed", "Failed", "Failed", "Skipped"]
    test_cases = [
        {
            "name": f"Test {i + 1}",
            "status": random.choice(statuses),
            "automated": random.choice([True, False]),
        }
        for i in range(count)
    ]
    return test_cases


test_cases = get_test_cases()

# Create a pie chart that has the following slices:
# - Automated Passes
# - Manual Passes
# - Automated Failures
# - Manual Failures
# - Skipped

auto_passes = 0
manual_passes = 0
auto_failures = 0
manual_failures = 0
skipped_count = 0

for test_case in test_cases:
    if test_case["status"] == "Passed" and test_case["automated"]:
        auto_passes += 1
    elif test_case["status"] == "Passed" and not test_case["automated"]:
        manual_passes += 1
    elif test_case["status"] == "Failed" and test_case["automated"]:
        auto_failures += 1
    elif test_case["status"] == "Failed" and not test_case["automated"]:
        manual_failures += 1
    elif test_case["status"] == "Skipped":
        skipped_count += 1


loader = FileSystemLoader("./")
env = Environment(loader=loader)
template = env.get_template("template.html")

rendered_template = template.render(
    auto_passes=auto_passes,
    manual_passes=manual_passes,
    auto_failures=auto_failures,
    manual_failures=manual_failures,
    skipped_count=skipped_count,
)

with open("output.html", "w") as f:
    f.write(rendered_template)
