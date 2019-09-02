FROM python:3.7.3-alpine3.9
WORKDIR /celery/
COPY . .
ENTRYPOINT celery worker -A proj --loglevel=info