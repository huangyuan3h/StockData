from datetime import datetime

from api.Response_Code import OK
from utils.dateUtils import get_current_timestamp_millisecond


def start_sync_stock_by_code(code:str):
    from task import taskManager, sync_kline_by_code
    taskManager.add_job(func=sync_kline_by_code.run, args=[code],
                        id=f'sync_kline_{code}_{get_current_timestamp_millisecond()}'
                        , next_run_time=datetime.now(), executor="default")
    return OK
