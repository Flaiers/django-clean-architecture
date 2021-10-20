#!/bin/bash

uvicorn config.asgi:application --host 0.0.0.0 --port ${WEB_PORT} --env-file ../deployment/example.env --reload