import logging


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

handler = logging.FileHandler('log.log', 'a', 'utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
