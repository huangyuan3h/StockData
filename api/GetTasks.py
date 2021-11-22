from flask_restful import Resource

from api import api
from task_manager import task_manager


@api.route('/tasks')
class GetTasks(Resource):
    def get(self):
        return list(map(lambda t: t.to_json(), task_manager.task_list))
