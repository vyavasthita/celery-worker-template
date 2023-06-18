import os
import smtplib
from email.mime.text import MIMEText
from .config import config_by_name


environment = os.getenv("BUILD_ENV") or "development"
config = config_by_name[environment]


class SendEmail:
    @classmethod
    def make_message(cls, sender, receiver, subject, body):
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = sender
        message["To"] = receiver

        return message

    @classmethod
    def send_email(
        cls,
        sender_name: str,
        sender_email: str,
        receiver_name: str,
        receiver_email: str,
        subject: str,
        body: str,
    ):
        sender = f"{sender_name} <{sender_email}>"
        receiver = f"{receiver_name} <{receiver_email}>"

        message = cls.make_message(sender, receiver, subject, body)

        with smtplib.SMTP(config["SMTP_SERVER"], config["SMTP_PORT"]) as server:
            server.login(config["SMTP_USER_NAME"], config["SMTP_PASSWORD"])
            server.sendmail(sender, receiver, message.as_string())
