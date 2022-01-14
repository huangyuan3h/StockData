from api.Response_Code import OK
from celery import group


def sync_all_stock():
    from tasks.sync_kline_day_all import get_all_code_list
    from tasks import run_by_code
    codes = get_all_code_list()
    group(run_by_code.s(c) for c in codes).apply_async()
    return OK
