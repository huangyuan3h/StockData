from concurrent.futures import ProcessPoolExecutor, Executor
from typing import List

from task_manager import Task


class TaskManager(object):
    task_list: List = []

    pool: Executor = None

    def initial(self, work_size=4):
        self.pool = ProcessPoolExecutor(max_workers=work_size)

    def add_task(self, task: Task):
        self.task_list.append(task)
        print("---add task---")

    def get_active_task(self):
        print("---get active task---")
