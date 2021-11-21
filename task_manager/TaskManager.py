from concurrent.futures import ProcessPoolExecutor, Executor
from typing import List

from log import log
from task_manager import Task


class TaskManager(object):
    task_list: List = []

    pool: Executor = None

    def initial(self, work_size=4):
        self.pool = ProcessPoolExecutor(max_workers=work_size)
        log.info("task manager initial with %s pool", work_size)

    def add_task(self, task: Task):
        self.task_list.append(task)

    def set_task_list(self, tasks):
        self.task_list = tasks

    def get_active_task(self):
        print("---get active task---")
