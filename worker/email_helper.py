import os
import mailtrap as mt
from .config import config_by_name


environment = os.getenv('BUILD_ENV') or 'development'
config = config_by_name[environment]


class SendEmail:
    @classmethod
    def send_email(classmethod, name: str, sender: str, receiver: str, subject: str, body: str):
        mail = mt.Mail(
            sender=mt.Address(email=sender, name=name),
            to=[mt.Address(email=receiver)],
            subject=subject,
            text=body,
        )
        # create client and send
        client = mt.MailtrapClient(token=config['EMAIL_API_KEY'])
        client.send(mail)

