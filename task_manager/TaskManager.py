from concurrent.futures import ProcessPoolExecutor, Executor
from typing import List

from log import log
from task_manager import Task


class TaskManager(object):
    task_list: List = []

    pool: Executor = None

    def initial(self, work_size=4):
        self.pool = ProcessPoolExecutor(max_workers=work_size)
        log.info("tasks manager initial with %s pool", work_size)

    def add_task(self, task: Task):
        self.task_list.append(task)

    def set_task_list(self, tasks):
        self.task_list = tasks

    def get_active_tasks(self):
        return list(filter(lambda t: t.running, self.task_list))

    def get_task_by_id(self, task_id: str):
        return next(filter(lambda t: t.id == task_id, self.task_list))

    def start_task(self, task_id: str):
        t: Task = self.get_task_by_id(task_id)
        t.running = True
        self.pool.submit(t.run, t.args, t.kwargs)
        return t.to_json()
