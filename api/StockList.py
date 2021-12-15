import datetime

from api.Response_Code import OK
from task import taskManager, sync_list
from utils.dateUtils import get_current_timestamp_millisecond

'''
sync all stock data
'''


def start_sync_stock_list():
    taskManager.add_job(func=sync_list.run, id=f'sync_list_{get_current_timestamp_millisecond()}'
                        , next_run_time=datetime.datetime.now())
    return OK
