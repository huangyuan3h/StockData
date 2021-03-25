from datetime import datetime

from flask_restful import Resource

from api.Response_Code import OK
from scheduler import scheduler, sync_kline_by_code
from utils.dateUtils import get_current_timestamp_millisecond

'''
sync day kline data
'''


class KLineDayByStockCode(Resource):
    def get(self, code):
        scheduler.add_job(func=sync_kline_by_code.run, args=[code],
                          id=f'sync_kline_{code}_{get_current_timestamp_millisecond()}'
                          , next_run_time=datetime.now())
        return OK
