import uuid
from abc import ABC, abstractmethod


class Task(ABC):
    id = uuid.uuid4()

    name = ''

    description = ''

    running = False

    args = None

    kwargs = None

    def __init__(self, name, args=None, kwargs=None, running=False):
        self.name = name
        self.args = args
        self.running = running
        self.kwargs = kwargs

    @abstractmethod
    def run(self):
        pass

    def to_json(self):
        return {"name": self.name, "running": self.running, 'id': self.id}
