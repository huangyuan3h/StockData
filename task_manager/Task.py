import uuid
from abc import ABC, abstractmethod


class Task(ABC):
    id = ''

    name = ''

    description = ''

    running = False

    args = None

    kwargs = None

    def __init__(self, name, task_id=uuid.uuid4(), args=None, kwargs=None, running=False):
        self.id = task_id
        self.name = name
        self.args = args
        self.running = running
        self.kwargs = kwargs

    @abstractmethod
    def run(self):
        pass

    def to_json(self):
        return {"name": self.name, "running": self.running, 'id': str(self.id)}
