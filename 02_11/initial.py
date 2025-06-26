from collections import defaultdict

import gspread
import openpyxl
from google.oauth2.service_account import Credentials

# UPdate to point to your service account file
SERVICE_ACCOUNT_FILE = "../advancedscriptingtest-ba70f9105ff9.json"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

g_sheet = client.open_by_url(
    "https://docs.google.com/spreadsheets/d/1S_1difkV4ZirGJ7jO_yCcvVqW0_YyY1SS30qoWp8Iek/edit?gid=0#gid=0"
)
