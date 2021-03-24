from datetime import datetime

from flask_restful import Resource

from api.Response_Code import OK
from scheduler import scheduler, sync_kline
from utils.dateUtils import get_current_timestamp_millisecond

'''
sync day kline data
'''


class KLineDayByStockCode(Resource):
    def get(self, code):
        scheduler.add_job(func=sync_kline.run, args=[code], id=f'sync_kline_{get_current_timestamp_millisecond()}'
                          , next_run_time=datetime.now())
        return OK
