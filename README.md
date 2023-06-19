# Prerequisites

sudo apt update && sudo apt upgrade
sudo apt-get install rabbitmq-server

sudo apt install redis-server

celery
redis
python-dotenv

dev env
black
# Run Celery Worker
poetry run celery -A worker.worker worker  --autoscale 10 --loglevel=info

## How to Test

1. Clone the repo
    git clone https://github.com/vyavasthita/celery-worker-template

2. Go to root directory 'celery-worker-template'.
    cd celery-worker-template   

3. Do following;-
    Here we will run our celery worker which is responding for sending emails.

    a). Go to directory 'celery-worker-template'.
        cd celery-worker-template

    b). Configure poetry virtual env path (optional)
        By default poetry virtual environment path is '/home/<user>/.cache/pypoetry/virtualenvs'

        If you want to change this path then follow below steps, else ignore.

        poetry config virtualenvs.path <some-existing-path> --local

        Note: Here --local means it is applicable to current project only otherwise this would be a global setting

    c). Install python packages using poetry
        poetry install

        This command will create a virtual environment and also install all packages from poetry.lock in this
        virtual environment.

    d). In current 'celery-worker-template' directory you will find a file named '.env.sample'.
        Copy this file as '.env.dev' for development use.

        Update all configuration in '.env.dev' accordingly.

    e). Start celery worker application
        bash start_worker.sh