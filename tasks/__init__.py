from task_manager import task_manager
from tasks.task_list import task_list


def loading_tasks():
    task_manager.set_task_list(task_list)
