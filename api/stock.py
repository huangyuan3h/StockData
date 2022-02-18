from api.response_code import OK
from tasks import sync_stocks


def sync_stock_list():
    """
    sync all stock data
    """
    sync_stocks.delay()
    return OK
