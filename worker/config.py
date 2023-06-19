import os
import ast
from dotenv import load_dotenv


# The root directory
base_dir = os.path.abspath(os.path.dirname(__name__))

env_by_name = dict(development=".env.dev", automated_testing=".env.aut_test")

environment = os.getenv("BUILD_ENV")

if environment is None:
    print(
        f"'BUILD_ENV' environment variable is not set. Please set it among environments {env_by_name.keys()}"
    )

if environment not in env_by_name.keys():
    print(f"Invalid {environment}. Available Environments {env_by_name.keys()}")

print("Using 'development' environment.")

environment = "development"

for environment_file in env_by_name.values():
    load_dotenv(
        dotenv_path=os.path.join(base_dir, environment_file)
    )  # to load .env file. .flaskenv file is automatically loaded without using load_dotenv()


devlopment_config = dict(
    CELERY_BROKER_URL=os.getenv("CELERY_BROKER_URL"),
    CELERY_RESULT_BACKEND=os.getenv("CELERY_RESULT_BACKEND"),
    SMTP_SERVER=os.getenv("SMTP_SERVER"),
    SMTP_PORT=ast.literal_eval(os.getenv("SMTP_PORT")),
    SMTP_USER_NAME=os.getenv("SMTP_USER_NAME"),
    SMTP_PASSWORD=os.getenv("SMTP_PASSWORD"),
)

aut_testing_config = dict(
    CELERY_BROKER_URL=os.getenv("CELERY_BROKER_URL"),
    CELERY_RESULT_BACKEND=os.getenv("CELERY_RESULT_BACKEND"),
    SMTP_SERVER=os.getenv("SMTP_SERVER"),
    SMTP_PORT=ast.literal_eval(os.getenv("SMTP_PORT")),
    SMTP_USER_NAME=os.getenv("SMTP_USER_NAME"),
    SMTP_PASSWORD=os.getenv("SMTP_PASSWORD"),
)

config_by_name = dict(
    development=devlopment_config, automated_testing=aut_testing_config
)
