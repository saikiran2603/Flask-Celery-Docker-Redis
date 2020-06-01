import time
from module.celery import app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task
def new_add(x, y):
    logger.info('Got Request - Starting work ')
    time.sleep(20)
    logger.info('Work Finished ')
    return x + y
