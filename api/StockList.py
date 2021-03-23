import datetime
from flask_restful import Resource

from api.Response_Code import OK
from scheduler import scheduler, sync_list

'''
sync all stock data
'''
class StockList(Resource):
    def get(self):
        scheduler.add_job(func=sync_list.run, id='sync_list_' + str(datetime.datetime.now())
                          , next_run_time=datetime.datetime.now())
        return OK
