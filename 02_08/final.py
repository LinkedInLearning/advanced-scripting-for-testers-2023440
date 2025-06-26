import gspread
from google.oauth2.service_account import Credentials

# Put your service account file location here
SERVICE_ACCOUNT_FILE = "../advancedscripting-ba70f9105ff9.json"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

sheet = client.open("Sample Bug Report Summary").sheet1

# all_values = sheet.get_all_values()

# open_count = 0
# for row in all_values:
#     if row[2] == "Open":
#         open_count += 1

# print(f"Total open bugs: {open_count}")

statuses = sheet.col_values(3)[1:]
print(statuses.count("Open"))
