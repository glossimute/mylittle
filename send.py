import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

sender_email = os.environ.get('EMAIL_USER')
receiver_email = os.environ.get('EMAIL_RECEIVER')
subject = "Data"
body = "Data from output_1.txt:\n" + open("output_1.txt").read() + "\n" + "Data from output_3.txt:\n" + open("output_3.txt").read()

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

smtp_server = os.environ.get('EMAIL_HOST')
smtp_port = os.environ.get('EMAIL_PORT')
smtp_username = sender_email
smtp_password = os.environ.get('EMAIL_PASS')

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)
text = message.as_string()
server.sendmail(sender_email, receiver_email, text)
server.quit()
