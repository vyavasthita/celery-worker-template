import os
from celery import Celery
import smtplib
from email.mime.text import MIMEText
from .config import config_by_name


environment = os.getenv("FLASK_ENV") or "development"
config = config_by_name[environment]


app = Celery(
    "email", broker=config["CELERY_BROKER_URL"], backend=config["CELERY_RESULT_BACKEND"]
)


def make_message(sender, receiver, subject, body):
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = receiver

    return message


@app.task(name="email.send")
def send_email(
    sender_name: str,
    sender_email: str,
    receiver_name: str,
    receiver_email: str,
    subject: str,
    body: str,
) -> tuple:
    sender = f"{sender_name} <{sender_email}>"
    receiver = f"{receiver_name} <{receiver_email}>"

    message = make_message(sender, receiver, subject, body)

    with smtplib.SMTP(config["SMTP_SERVER"], config["SMTP_PORT"]) as server:
        server.login(config["SMTP_USER_NAME"], config["SMTP_PASSWORD"])
        # server.sendmail(sender, receiver, message.as_string())
