#!/bin/bash

poetry run celery -A worker.worker worker  --autoscale 10 --loglevel=info