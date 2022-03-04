#!/bin/bash
source .venv/bin/activate
cd src/

python manage.py collectstatic --noinput
python manage.py migrate
python build.py
uvicorn --reload --host 0.0.0.0 --port ${WEB_PORT} config.asgi:application --workers $(nproc)
