#!/bin/bash
source env/bin/activate
cd src/

python manage.py migrate
python build.py
uvicorn --reload --host 0.0.0.0 --port ${WEB_PORT} config.asgi:application