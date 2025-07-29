import random
from datetime import datetime, timedelta

import gspread
from google.oauth2.service_account import Credentials

SERVICE_ACCOUNT_FILE = "../advancedscripting-da4417eb3e72.json"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)
try:
    spreadsheet = client.open("Bug Report Summary")
except gspread.SpreadsheetNotFound:
    spreadsheet = client.create("Bug Report Summary")

    spreadsheet.share("example@gmail.com", perm_type="user", role="writer")

print(spreadsheet.url)


def random_datetime(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )


def get_bugs():
    severity_levels = ["High", "Medium", "Low", "Critical"]
    statuses = [
        "Open",
        "In Progress",
        "In Review",
        "Information Needed",
    ]
    bugs = []
    for i in range(25):
        bugs.append(
            {
                "id": 101 + i,
                "title": f"Bug {i}",
                "status": random.choice(statuses),
                "severity": random.choice(severity_levels),
                "created_at": random_datetime(
                    datetime(2025, 5, 20), datetime(2025, 5, 26)
                ).strftime("%Y-%m-%d"),
            }
        )
    return bugs


today = datetime.now().strftime("%Y-%m-%d")
worksheet_title = f"Bug Report {today}"
try:
    current_sheet = spreadsheet.worksheet(worksheet_title)
except gspread.WorksheetNotFound:
    current_sheet = spreadsheet.add_worksheet(worksheet_title, rows="100", cols="4")
current_sheet.append_row(
    [
        "ID",
        "Title",
        "Status",
        "Severity",
        "Created At",
    ]
)
for bug in get_bugs():
    current_sheet.append_row(
        [
            bug["id"],
            bug["title"],
            bug["status"],
            bug["severity"],
            bug["created_at"],
        ]
    )

current_sheet.format("A1:D1", {"textFormat": {"bold": True}})
current_sheet.freeze(rows=1)
