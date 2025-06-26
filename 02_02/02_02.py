import openpyxl
import requests

workbook = openpyxl.load_workbook("sample_test_data.xlsx")
sheet = workbook.active

LOGIN_URL = "http://localhost:8002/api/login"

for header in sheet[1]:
    if header.value == "Username":
        username_col = header.column
    if header.value == "IsActive":
        is_active_col = header.column

for row in sheet.iter_rows(min_row=2, values_only=True):
    username = row[username_col - 1]
    is_active = row[is_active_col - 1]

    payload = {"username": username, "password": "test123"}

    response = requests.post(LOGIN_URL, json=payload)

    print(f"User {username}: response status code {response.status_code}")

    if is_active:
        assert response.status_code == 200
    else:
        assert response.status_code == 401
