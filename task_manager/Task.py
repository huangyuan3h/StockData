import uuid
from abc import ABC
import celery


class Task(celery.Task, ABC):
    id = ''

    name = ''

    description = ''

    running = False

    args = None

    kwargs = None

    def __init__(self, name, task_id=uuid.uuid4(), args=[], kwargs={}, running=False):
        self.id = task_id
        self.name = name
        self.args = args
        self.running = running
        self.kwargs = kwargs

    def to_json(self):
        return {"name": self.name, "running": self.running, 'id': str(self.id)}
