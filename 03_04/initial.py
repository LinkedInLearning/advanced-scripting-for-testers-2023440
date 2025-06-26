import random

from jinja2 import Environment, FileSystemLoader


def get_test_cases(count=25):
    statuses = ["Passed", "Failed", "Skipped"]
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
