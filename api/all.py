from celery import group, chain
from api.response_code import OK
from api.lstm import generate_n_day_report
from tasks import sync_kline_day_all, sync_index_kline_day_all, sync_all_fund_flow


def run_all_daily_task():
    g = group(sync_kline_day_all.s(), sync_index_kline_day_all.s(), sync_all_fund_flow.s())
    c = chain(g.s(), generate_n_day_report.s(model='lstm', predict_day=3))
    c.delay()
    return OK

