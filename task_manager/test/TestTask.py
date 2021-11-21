import unittest
from unittest.mock import MagicMock

from task_manager import Task


class MockTasks(Task):
    def run(self):
        self.running = self.fn(*self.args, **self.kwargs)


class TestLogging(unittest.TestCase):

    def test_task_basic_fn(self):
        mock_fn = MagicMock(return_value=False)

        args = [1, '2', False]

        kwargs = {'k1': 'k1', 'k2': 'k2'}

        t1 = MockTasks(name='t1', fn=mock_fn, args=args, kwargs=kwargs)
        self.assertEqual(t1.name, 't1')
        self.assertEqual(mock_fn, t1.fn)
        self.assertEqual(t1.args, args)
        self.assertEqual(t1.kwargs, kwargs)
        self.assertFalse(t1.running)

        t1.run()
        mock_fn.assert_called_with(*args, **kwargs)

        self.assertTrue(t1.to_json() == {'name': 't1', 'running': False})
