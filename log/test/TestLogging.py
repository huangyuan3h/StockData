import unittest
import os
import logging

from log import log

handler = logging.FileHandler('log.log', 'a', 'utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)


class TestLogging(unittest.TestCase):
    def setUp(self):
        log.addHandler(handler)

    def tearDown(self):
        log.removeHandler(handler)

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


