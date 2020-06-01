from __future__ import absolute_import
from celery import Celery

app = Celery('module', broker='redis://redis:6379/0', backend='redis://redis:6379/0', include=['module.tasks'])
