import unittest
from unittest.mock import MagicMock

from task_manager import Task


class TestLogging(unittest.TestCase):

    def test_task_basic_fn(self):
        mockFn = MagicMock(return_value=False)
        t1 = Task('t1', mockFn, 1)
        self.assertEqual(t1.name, 't1')
        self.assertEqual(mockFn, t1.fn)
        self.assertEqual(t1.args, 1)
        self.assertFalse(t1.running)

        t1.start()

        self.assertTrue(t1.running)

