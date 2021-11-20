import os
from concurrent.futures import ProcessPoolExecutor, Executor
from numbers import Number


def task(num: Number):
    print("--Executing our Task on Process {}".format(os.getpid()))
    print("--task--",num)


class TaskManager(object):
    task_list = []

    pool: Executor = None

    def initial(self, work_size = 4):
        self.pool = ProcessPoolExecutor(max_workers=work_size)

    def add_task(self, fn, args):
        print("---add task---")

    def get_active_task(self):
        print("---get active task---")
