from abc import ABC, abstractmethod


class Task(ABC):
    name = ''

    description = ''

    running = False

    fn = None

    args = None

    kwargs = None

    def __init__(self, name, fn, args=None, kwargs=None, running=False):
        self.name = name
        self.fn = fn
        self.args = args
        self.running = running
        self.kwargs = kwargs

    @abstractmethod
    def run(self):
        self.running = self.fn(*self.args, **self.kwargs)

    def to_json(self):
        return {"name": self.name, "running": self.running}
