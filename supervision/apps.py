#!/usr/bin/env python
#encoding: utf-8

"""
Celery apps definitions
"""


from celery import Celery
from celery.schedules import crontab
from ConfigParser import ConfigParser
from datetime import timedelta


__all__ = [
    'cameras'
    ]

CONFIG = ConfigParser(allow_no_value=True)
CONFIG.read('/etc/supervision/supervision.ini')
CAMERAS = []
sections_cameras = filter(lambda x: x.startswith('camera_'),
                          CONFIG.sections())
for section in sections_cameras:
    CAMERAS.append(dict(CONFIG.items(section)))


cameras = Celery(
    'supervision',
    broker='amqp://',
    include=['supervision.tasks']
    )

cameras.conf.update(
    CELERY_AMQP_TASK_RESULT_EXPIRES=10,
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml'],
    CELERY_TIMEZONE = 'Indian/Antananarivo',
    CELERY_ENABLE_UTC = True,
    CELERYBEAT_SCHEDULE = {
        'download-every-2-seconds': {
            'task': 'supervision.tasks.download',
            'schedule': timedelta(seconds=2),
            'args': (CAMERAS,),
        },
        'purge-every-60-seconds': {
            'task': 'supervision.tasks.purge',
            'schedule': crontab(),
            'args': (CAMERAS,),
        }
    },
    CELERY_ROUTES = {
        'supervision.tasks.get_image': {'queue': 'download'},
        'supervision.tasks.download': {'queue': 'download'},
        'supervision.tasks.rm': {'queue': 'purge'},
        'supervision.tasks.purge_folder': {'queue': 'purge'},
        'supervision.tasks.purge': {'queue': 'purge'},
        }
    )
