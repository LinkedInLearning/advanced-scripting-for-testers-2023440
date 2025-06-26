import random
from datetime import datetime, timedelta

from openpyxl import Workbook


# Helper functions
def random_datetime(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )


def random_status():
    return random.choice(["PASS", "FAIL"])


# File 1: Test Automation Results
file1 = "test_automation_results.xlsx"
wb1 = Workbook()
ws1 = wb1.active
ws1.title = "Automation Results"
ws1.append(["Test ID", "Test Name", "Status", "Duration (s)", "Timestamp"])
for i in range(1, 51):
    ws1.append(
        [
            f"TC_{i:03d}",
            f"Test_Case_{i}",
            random_status(),
            round(random.uniform(0.5, 5.0), 2),
            random_datetime(datetime(2025, 5, 20), datetime(2025, 5, 26)),
        ]
    )
wb1.save(file1)

# File 2: Manual Testing Results
file2 = "manual_testing_results.xlsx"
wb2 = Workbook()
ws2 = wb2.active
ws2.title = "Manual Results"
ws2.append(["Tester", "Test Case", "Result", "Comments", "Date"])
for i in range(1, 31):
    ws2.append(
        [
            random.choice(["Alice", "Bob", "Charlie", "Dana"]),
            f"Manual_TC_{i}",
            random_status(),
            random.choice(
                ["Looks good", "Needs review", "Failed under condition X", "N/A"]
            ),
            random_datetime(datetime(2025, 5, 20), datetime(2025, 5, 26)).date(),
        ]
    )
wb2.save(file2)
