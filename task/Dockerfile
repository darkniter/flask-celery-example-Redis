FROM python:3.7.3-alpine3.9
COPY requirements.txt /app/requirements.txt
WORKDIR /app/
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT celery -A proj worker --loglevel=info