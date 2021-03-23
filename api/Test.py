from flask_restful import Resource
from api.Response_Code import OK
from scheduler.sync_kline import run


class Test(Resource):
    def get(self):
        run('SH600519')
        return OK
