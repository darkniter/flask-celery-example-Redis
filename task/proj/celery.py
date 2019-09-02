from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

app_celery = Celery('proj',
             broker='redis://localhost:6379/13',
             backend='redis://localhost:6379/13',
             include=['proj.tasks'])

# Optional configuration, see the application user guide.
app_celery.conf.update(
    result_expires=3600,

)
# Initialize Celery
app_celery.config['SECRET_KEY'] = 'top-secret!'
app_celery.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app_celery.config['MAIL_PORT'] = 587
app_celery.config['MAIL_USE_TLS'] = True
app_celery.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app_celery.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app_celery.config['MAIL_DEFAULT_SENDER'] = 'flask@example.com'



if __name__ == '__main__':
    app_celery.start()
