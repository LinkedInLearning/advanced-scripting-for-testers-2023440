import getpass
import smtplib
from email.message import EmailMessage

msg = EmailMessage()

msg["Subject"] = "Test Email"
msg["From"] = "me@me.com"
msg["To"] = "davewesterveld@gmail.com"
msg.set_content("This is a test email sent from my Python script!")

password = getpass.getpass()
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()
    smtp.login("davewesterveld@gmail.com", password)
    smtp.send_message(msg)
