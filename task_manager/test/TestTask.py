import unittest

from task_manager import Task


class MockTasks(Task):
    def run(self):
        self.running = False


class TestLogging(unittest.TestCase):

    def test_task_basic_fn(self):

        args = [1, '2', False]

        kwargs = {'k1': 'k1', 'k2': 'k2'}

        t1 = MockTasks(name='t1', args=args, kwargs=kwargs)
        self.assertEqual(t1.name, 't1')
        self.assertEqual(t1.args, args)
        self.assertEqual(t1.kwargs, kwargs)
        self.assertFalse(t1.running)

        t1.run()

        self.assertTrue(t1.to_json() == {'name': 't1', 'running': False, 'id': t1.id})
