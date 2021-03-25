from flask_restful import Resource

from api.Response_Code import OK
from scheduler import scheduler


class GetTasks(Resource):
    def get(self):
        return scheduler.get_jobs()
