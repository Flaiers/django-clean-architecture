#!/bin/bash
source env/bin/activate
cd src/

python manage.py collectstatic --noinput
python manage.py migrate
python build.py
gunicorn --reload -b 0.0.0.0:${WEB_PORT} -c config/gunicorn.conf.py -k uvicorn.workers.UvicornWorker config.asgi:application