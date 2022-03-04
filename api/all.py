from celery import chain

from api.response_code import OK


def run_all_daily_task():
    from tasks import sync_kline_day_all, sync_all_fund_flow, sync_index_kline_day_all
    c = chain(sync_index_kline_day_all.s(), sync_kline_day_all.s(),
              sync_all_fund_flow.s())
    c.delay()
    return OK
