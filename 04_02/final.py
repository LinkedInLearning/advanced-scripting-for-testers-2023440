import getpass
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "Test Email"
msg["From"] = " " # email address goes here
msg["To"] = " " # email address goes here
msg.set_content("This is a test email sent from my Python script!")


with open("test_report.pdf", "rb") as f:
    contents = f.read()
    msg.add_attachment(
        contents,
        maintype="application",
        subtype="pdf",
        filename="test_report.pdf",
    )

password = getpass.getpass()
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()
    smtp.login(" ", password) # email address goes here
    smtp.send_message(msg)
