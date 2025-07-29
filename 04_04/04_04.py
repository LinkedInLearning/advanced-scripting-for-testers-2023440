import os

import requests

slack_token = os.environ.get("SLACK_BOT_TOKEN")
pdf_path = "test_report.pdf"
channel_id = "C09125JJZ4N"


with open(pdf_path, "rb") as file_content:
    file_size = os.path.getsize(pdf_path)
    file_content = file_content.read()

response = requests.post(
    "https://slack.com/api/files.getUploadURLExternal",
    data={
        "token": slack_token,
        "length": file_size,
        "filename": pdf_path,
    },
)

response_data = response.json()

upload_url = response_data["upload_url"]
file_id = response_data["file_id"]


response = requests.post(
    upload_url,
    files={"file": (pdf_path, file_content, "application/pdf")},
    data={
        "token": slack_token,
        "filename": pdf_path,
    },
)


response = requests.post(
    "https://slack.com/api/files.completeUploadExternal",
    headers={"Authorization": f"Bearer {slack_token}"},
    json={
        "files": [{"id": file_id}],
        "channel_id": channel_id,
        "initial_comment": "Here is the Test Report pdf file.",
    },
)

print(response.status_code, response.json())
