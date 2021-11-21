import unittest

from task_manager import Task
from task_manager.TaskManager import TaskManager
from unittest.mock import MagicMock


class MockTask(Task):
    def run(self):
        self.running = self.fn(*self.args, **self.kwargs)


mock_fn = MagicMock(return_value=False)

mock_task1 = MockTask('t1', mock_fn)

mock_task2 = MockTask('t1', mock_fn)

mock_task_list = [mock_task1]


class TestTaskManager(unittest.TestCase):

    def test_initial(self):
        task_manager = TaskManager()
        task_manager.initial()
        self.assertIsNotNone(task_manager.pool)

        task_manager.set_task_list(mock_task_list)
        self.assertEqual(task_manager.task_list, mock_task_list)

        task_manager.add_task(mock_task2)
        self.assertEqual(len(task_manager.task_list), 2)


