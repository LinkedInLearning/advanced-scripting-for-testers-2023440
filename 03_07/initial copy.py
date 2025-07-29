import random

import matplotlib.pyplot as plt
from fpdf import FPDF


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

labels = [
    "Automated Passes",
    "Manual Passes",
    "Automated Failures",
    "Manual Failures",
    "Skipped",
]
plt.pie(
    [auto_passes, manual_passes, auto_failures, manual_failures, skipped_count],
    labels=labels,
)
plt.title("Test Case Statuses")
plt.savefig("test_case_statuses.png")
plt.close()

pdf = FPDF()
pdf.add_page()

pdf.image("test_case_statuses.png", x=10, y=None, w=100)

pdf.output("test_report.pdf")
