import os
import smtplib
from collections import defaultdict
from email.message import EmailMessage

from openpyxl import Workbook

status_codes_by_date = defaultdict(list)
with open("gigtracker_fake.log", "r") as f:
    for line in f:
        if "HTTP/1.1" in line:
            status_code = line.split()[-1].strip()
            date = line.split()[0].strip()
            status_codes_by_date[date].append(status_code)

wb = Workbook()
sheet = wb.active
sheet.title = "Status Codes by Date"

sheet.append(["Date", "200", "401", "403"])

for date in status_codes_by_date.keys():
    row = [date]
    row.append(status_codes_by_date[date].count("200"))
    row.append(status_codes_by_date[date].count("401"))
    row.append(status_codes_by_date[date].count("403"))
    sheet.append(row)

wb.save("status_codes_summary.xlsx")
wb.close()

msg = EmailMessage()
msg["Subject"] = "Status Codes Summary"
msg["From"] = "me@me.com"
msg["To"] = "davewesterveld@gmail.com"
msg.set_content("Please find the status_codes_summary.xlsx attached")

with open("status_codes_summary.xlsx", "rb") as f:
    contents = f.read()

msg.add_attachment(
    contents,
    maintype="application",
    subtype="xlsx",
    filename="status_codes_summary.xlsx",
)

password = os.getenv("GMAIL_SMTP_PASSWORD")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()
    smtp.login("davewesterveld@gmail.com", password)
    smtp.send_message(msg)
