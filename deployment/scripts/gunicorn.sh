#!/bin/bash

gunicorn config.asgi:application -b 0.0.0.0:${WEB_PORT} --reload