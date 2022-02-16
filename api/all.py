from celery import chain

from api.response_code import OK
from tasks import sync_kline_day_all, sync_all_fund_flow, generate_report, sync_index_kline_day_all


def run_all_daily_task():
    # g = group([sync_index_kline_day_all.s(), sync_kline_day_all.s(),
    #            sync_all_fund_flow.s()])
    c = chain(sync_kline_day_all.s(),
              generate_report.s(model_name='lstm2', predict_day=3))
    c.delay()
    return OK
