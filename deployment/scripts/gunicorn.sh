#!/bin/bash

source env/bin/activate
cd src/

python manage.py migrate
python build.py
gunicorn -k uvicorn.workers.UvicornWorker -b 0.0.0.0:${WEB_PORT} config.asgi:application