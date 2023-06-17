import os
from celery import Celery
from .email_helper import SendEmail
from .config import config_by_name


environment = os.getenv('FLASK_ENV') or 'development'
config = config_by_name[environment]


app = Celery('email', broker=config['CELERY_BROKER_URL'], backend=config['CELERY_RESULT_BACKEND'])


@app.task(name='email.send')
def send_email(name: str, sender: str, receiver: str, subject: str, body: str) -> tuple:
    SendEmail.send_email(name, sender, receiver, subject, body)