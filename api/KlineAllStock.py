from datetime import datetime

from flask_restful import Resource

from api.Response_Code import OK
from scheduler import scheduler, sync_kline_day_all
from utils.dateUtils import get_current_timestamp_millisecond


class KlineAllStock(Resource):
    def get(self):
        scheduler.add_job(func=sync_kline_day_all.run,
                          id=f'sync_kline_all_{get_current_timestamp_millisecond()}'
                          , next_run_time=datetime.now())
        return OK
