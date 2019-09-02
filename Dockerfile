FROM python:3.7.3-alpine3.9
WORKDIR /project
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT celery -A app worker --loglevel=info
CMD ["flask", "run"]