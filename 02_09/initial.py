import random
from datetime import datetime

import gspread
from google.oauth2.service_account import Credentials

# Update to point to your service account file
SERVICE_ACCOUNT_FILE = "../advancedscriptingtest-ba70f9105ff9.json"

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

    # Put in your email address here so that you can access the spreadsheet
    # from your google account
    spreadsheet.share("example@gmail.com", perm_type="user", role="writer")

print(spreadsheet.url)


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
                "id": 100 + i,
                "title": f"Bug {i + 1}",
                "status": random.choice(statuses),
                "severity": random.choice(severity_levels),
            }
        )
    return bugs
