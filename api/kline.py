from api.Response_Code import OK
from tasks import run_by_code
from tasks import sync_kline_day_all


def sync_stock_by_code(code: str):
    run_by_code.delay(code)
    return OK


def sync_all_stock():
    sync_kline_day_all.delay()
    return OK
