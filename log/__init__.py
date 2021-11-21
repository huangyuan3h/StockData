import logging
import re
import sys

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

"""
if in ut, remove append log
"""
if not (len(sys.argv) > 1 and re.search('test', sys.argv[1], re.IGNORECASE)):
    handler = logging.FileHandler('log.log', 'a', 'utf-8')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
