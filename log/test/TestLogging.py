import unittest
import os

from log import log


class TestLogging(unittest.TestCase):

    def test_log_basic_fn(self):
        log.warning('warning')
        log.info('info')
        log.debug('debug')
        log.error('error')
        f = open("log.log", "r")

        self.assertTrue(f.readline().rindex('warning') > 0)
        self.assertTrue(f.readline().rindex('info') > 0)
        self.assertTrue(f.readline().rindex('debug') > 0)
        self.assertTrue(f.readline().rindex('error') > 0)

        os.remove("log.log")


