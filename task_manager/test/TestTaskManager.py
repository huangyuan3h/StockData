import unittest
import uuid

from task_manager import Task
from task_manager.TaskManager import TaskManager


class MockTask(Task):
    def run(self):
        self.running = False


mock_task1 = MockTask('t1')

mock_task2 = MockTask('t2')

mock_task_list = [mock_task1]


class TestTaskManager(unittest.TestCase):

    def test_basic_fn(self):
        task_manager = TaskManager()
        task_manager.initial()
        self.assertIsNotNone(task_manager.pool)

        task_manager.set_task_list(mock_task_list)
        self.assertEqual(task_manager.task_list, mock_task_list)

        task_manager.add_task(mock_task2)
        self.assertEqual(len(task_manager.task_list), 2)

    def test_get_active_tasks(self):
        task_manager = TaskManager()
        task_manager.initial()

        mock_task3 = MockTask('t3', running=True)
        mock_task_list2 = [mock_task1, mock_task3]
        task_manager.set_task_list(mock_task_list2)
        active_result = task_manager.get_active_tasks()
        self.assertEqual(active_result, [mock_task3])

    def test_get_task_by_id(self):
        task_manager = TaskManager()
        task_manager.initial()

        tid = uuid.uuid4()

        mock_task3 = MockTask('t3', task_id=tid, running=True)
        mock_task_list2 = [mock_task1, mock_task3]
        task_manager.set_task_list(mock_task_list2)
        result = task_manager.get_task_by_id(tid)
        self.assertEqual(result, mock_task3)
