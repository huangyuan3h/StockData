from api.Response_Code import OK
from tasks import sync_kline_day_all


def sync_all_stock():
    sync_kline_day_all.delay()
    return OK
