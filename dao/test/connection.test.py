import unittest

from dao.connection import get_engine


class connection_test(unittest.TestCase):
    def test_get_engine(self):
        engine = get_engine()
        self.assertIsNotNone(engine)



if __name__ == '__main__':
    unittest.main()
