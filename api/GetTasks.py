from flask_restful import Resource

from task_manager import task_manager


class GetTasks(Resource):
    def get(self):
        return list(map(lambda t: t.to_json(), task_manager.task_list))
