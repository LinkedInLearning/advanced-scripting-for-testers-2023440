import gspread
from google.oauth2.service_account import Credentials

SERVICE_ACCOUNT_FILE = "../advancedscriptingtest-ba70f9105ff9.json"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

client = gspread.authorize(creds)

sheet = client.open("Advanced Scripting").sheet1

sheet.update_acell("A1", "Hello World!")
