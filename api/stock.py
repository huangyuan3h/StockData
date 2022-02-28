from api.response_code import OK


def sync_stock_list():
    from tasks import sync_stocks
    """
    sync all stock data
    """
    sync_stocks.delay()
    return OK
