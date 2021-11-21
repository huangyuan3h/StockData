from log import log


class Task(object):
    name = ''

    running = False

    fn = None

    args = None

    def __init__(self, name, fn, args, running=False):
        self.name = name
        self.fn = fn
        self.args = args
        self.running = running

    def start(self):
        self.running = True

    def running(self):
        while self.running:
            self.running = self.fn()

        log.info("--finished--")
