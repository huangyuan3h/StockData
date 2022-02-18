from celery import chain

from api.response_code import OK
from tasks import sync_kline_day_all, sync_all_fund_flow, sync_index_kline_day_all


def run_all_daily_task():
    c = chain(sync_index_kline_day_all.s(), sync_kline_day_all.s(),
              sync_all_fund_flow.s())
    c.delay()
    return OK
