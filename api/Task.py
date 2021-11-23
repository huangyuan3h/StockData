from flask_restful import Resource

from api import api
from task_manager import task_manager, Task as TaskType


@api.route('/task/<string:task_id>')
class Task(Resource):
    """
    start a task
    """

    def post(self, task_id):
        t: TaskType = task_manager.start_task(task_id)
        return t.to_json()
