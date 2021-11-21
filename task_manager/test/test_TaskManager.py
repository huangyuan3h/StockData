import unittest

from task_manager.TaskManager import TaskManager


class test_TaskManager(unittest.TestCase):

    def test_initial(self):
        taskManager = TaskManager()
        taskManager.add_task()


