from api.response_code import OK
from tasks import sync_stock_list


def sync_stock_list():
    """
    sync all stock data
    """
    sync_stock_list.delay()
    return OK
