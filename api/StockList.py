import datetime

from flask_restful import Resource

from api.Response_Code import OK
from scheduler import scheduler, sync_list
from utils.dateUtils import get_current_timestamp_millisecond

'''
sync all stock data
'''


class StockList(Resource):
    def get(self):
        scheduler.add_job(func=sync_list.run, id=f'sync_list_{get_current_timestamp_millisecond()}'
                          , next_run_time=datetime.datetime.now())
        return OK
