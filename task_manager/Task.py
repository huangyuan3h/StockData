

class Task(object):

    name = ''

    running = False

    fn = None

    def __init__(self, name, fn):
        self.name = name
        self.fn = fn

    def start(self):
        self.running = True

    def running(self):
        while self.running:
            self.running = self.fn()

        print("--finished--")
