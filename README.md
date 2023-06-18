# Prerequisites

sudo apt update && sudo apt upgrade
sudo apt-get install rabbitmq-server

sudo apt install redis-server

celery
redis
mailtrap
python-dotenv

# Run Celery Worker
poetry run celery -A worker.worker worker  --autoscale 10 --loglevel=info
