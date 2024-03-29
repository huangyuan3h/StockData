import uuid
from typing import List

from celery import Celery
from flask import Flask

from log import log
from task_manager import Task
from task_manager.make_celery import make_celery


class TaskManager(object):
    task_list: List = []

    celery: Celery = None

    def __init__(self):
        def default_task():
            log.error("task function not initial")
        self.task = default_task

    def initial(self, app: Flask):
        self.celery = make_celery(app)
        self.task = self.celery.task
        import tasks  # import tasks

    def add_task(self, task: Task):
        self.task_list.append(task)

    def set_task_list(self, tasks):
        self.task_list = tasks

    def get_active_tasks(self):
        return list(filter(lambda t: t.running, self.task_list))

    def get_task_by_id(self, task_id):
        tid = task_id if type(task_id) == uuid.UUID else uuid.UUID(task_id)
        return next(filter(lambda t: t.id == tid, self.task_list))

    def start_task(self, task_id: str):
        t: Task = self.get_task_by_id(task_id)
        log.info("task %s has been submit to pool", t.name)
        return t
