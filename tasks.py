from celery import Celery
import smtplib
from email.mime.text import MIMEText

app = Celery('tasks', broker='amqp://<RABBITMQ-USER>:<RABBITMQ-PASSWORD>@localhost//')

@app.task
def send_email(recipient):
    smtp_server = "smtp.zoho.com"
    smtp_port = 587
    sender_email = "admin@rtmdemos.name.ng"
    sender_password = "aQM56Kj7T0yn"

    subject = "Test Email"
    body = "This is a test email sent using RabbitMQ and Celery."

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()
        return f"Email sent to {recipient}"
    except Exception as e:
        return str(e)