from __future__ import absolute_import,unicode_literals
import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoceleryproject.settings')
app = Celery('djangoceleryproject')

app.conf.enable_utc= True

# app.conf.update(timezone='Asia/Kathmandu')
app.config_from_object("django.conf:settings", namespace="CELERY")


#Celery Beat Settings
# to start celery beat cmd: -celery -A djangoceleryproject beat -l INFO
# tp start celery worker :celery -A djangoceleryproject.celery worker -l info
app.conf.beat_schedule = {
    'send-mail-every-at__ a.m': {
        'task':'send_mail_app.tasks.send_mail_func',
        'schedule': crontab(hour=16,minute=45),
        # 'args': (2,), pass the data to send_mail_app
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    
    
    
# to start celery worker
# -celery -A djangoceleryproject.celery worker -l info