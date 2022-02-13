from joblib import Parallel, delayed

from dao.fund_flow_process import get_last
from eastmoney.fund_flow import get_data_by_code
from log import log
from task_manager import task_manager
from tasks.sync_kline import get_all_code_list
from utils.dateUtils import string_to_datetime


@task_manager.celery.task()
def sync_fund_flow_by_code(code: str):
    last_fund_flow = get_last(code)
    kline_list = get_data_by_code(code)

    if last_fund_flow is not None:
        kline_list = list(filter(lambda l: string_to_datetime(l[0]) > last_fund_flow.timestamp, kline_list))

    from dao.session_maker import session_maker
    from dao.model.FundFlow import FundFlow
    with session_maker() as session:
        for i in kline_list:
            fund_flow = FundFlow(code=code, timestamp=i[0], main_percent=i[6], huge_percent=i[10],
                                 large_percent=i[9], middle_percent=i[8], small_percent=i[7])
            session.add(fund_flow)
        session.commit()
        log.info("%s has been synchronized to latest", code)


@task_manager.celery.task()
def sync_all_fund_flow():
    codes = get_all_code_list()
    Parallel(n_jobs=30, backend="threading")(delayed(sync_fund_flow_by_code)(code) for code in codes)
