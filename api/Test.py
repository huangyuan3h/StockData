from flask_restful import Resource
from api.Response_Code import OK
from task.sync_kline_day_all import run


class Test(Resource):
    def get(self):
        run()
        return OK
