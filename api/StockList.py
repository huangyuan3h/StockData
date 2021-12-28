from api.Response_Code import OK
from tasks import sync_stock_list

'''
sync all stock data
'''
def start_sync_stock_list():
    sync_stock_list.delay()
    return OK
