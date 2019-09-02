FROM python:3.7.3-alpine3.9
WORKDIR /celery/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT celery worker -A proj --loglevel=info