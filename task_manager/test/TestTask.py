import unittest
from unittest.mock import MagicMock

from task_manager import Task


class MockTasks(Task):
    def run(self):
        self.running = self.fn(*self.args, **self.kwargs)


class TestLogging(unittest.TestCase):

    def test_task_basic_fn(self):
        mockFn = MagicMock(return_value=False)

        args = [1, '2', False]

        kwargs = {'k1': 'k1', 'k2': 'k2'}

        t1 = MockTasks(name='t1', fn=mockFn, args=args, kwargs=kwargs)
        self.assertEqual(t1.name, 't1')
        self.assertEqual(mockFn, t1.fn)
        self.assertEqual(t1.args, args)
        self.assertEqual(t1.kwargs, kwargs)
        self.assertFalse(t1.running)

        t1.start()

        self.assertTrue(t1.running)

        t1.stop()
        self.assertFalse(t1.running)

        t1.run()
        mockFn.assert_called_with(*args, **kwargs)
