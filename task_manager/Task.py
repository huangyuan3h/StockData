from abc import ABC, abstractmethod


class Task(ABC):
    name = ''

    running = False

    fn = None

    args = None

    kwargs = None

    def __init__(self, name, fn, args, kwargs, running=False):
        self.name = name
        self.fn = fn
        self.args = args
        self.running = running
        self.kwargs = kwargs

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    @abstractmethod
    def run(self):
        self.running = self.fn(*self.args, **self.kwargs)
