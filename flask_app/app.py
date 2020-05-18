from flask import Flask
from celery import Celery

app = Flask(__name__)
simple_app = Celery('simple_worker', broker='redis://redis:6379/0', backend='redis://redis:6379/0')
celery_app = Celery('module', broker='redis://redis:6379/0', backend='redis://redis:6379/0')


@app.route('/simple_start_task')
def call_method():
    app.logger.info("Invoking Method ")
    r = simple_app.send_task('tasks.longtime_add', kwargs={'x': 1, 'y': 2})
    app.logger.info(r.backend)
    return r.id


@app.route('/simple_task_status/<task_id>')
def get_status(task_id):
    status = simple_app.AsyncResult(task_id, app=simple_app)
    print("Invoking Method ")
    return "Status of the Task " + str(status.state)


@app.route('/simple_task_result/<task_id>')
def task_result(task_id):
    result = simple_app.AsyncResult(task_id).result
    return "Result of the Task " + str(result)


# Celery Module based Tasks

@app.route('/module_start_task')
def module_call_method():
    app.logger.info("Invoking Method ")
    app.logger.info(celery_app.tasks)
    r = celery_app.send_task('module.tasks.new_add', kwargs={'x': 1, 'y': 2}, queue='module')
    app.logger.info(r.backend)
    return r.id


@app.route('/module_task_status/<task_id>')
def module_get_status(task_id):
    status = celery_app.AsyncResult(task_id, app=celery_app)
    print("Invoking Method ")
    return "Status of the Task " + str(status.state)


@app.route('/module_task_result/<task_id>')
def module_task_result(task_id):
    result = celery_app.AsyncResult(task_id).result
    return "Result of the Task " + str(result)
