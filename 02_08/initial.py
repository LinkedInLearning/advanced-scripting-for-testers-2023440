import gspread
from google.oauth2.service_account import Credentials

# Put your service account file location here
SERVICE_ACCOUNT_FILE = "../advancedscriptingtest-ba70f9105ff9.json"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

sheet = client.open("Sample Bug Report Summary").sheet1
