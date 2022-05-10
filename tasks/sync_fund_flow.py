import time

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
        log.info("fund flow %s has been synchronized to latest", code)


@task_manager.celery.task()
def sync_all_fund_flow(*args, **kwargs):
    codes = get_all_code_list()

    batch_number = 500
    current_batch = 0

    while current_batch != int(len(codes)/batch_number + 1):
        batch_codes = codes[current_batch * batch_number:(current_batch + 1) * batch_number]
        try:
            Parallel(n_jobs=30, backend="threading")(delayed(sync_fund_flow_by_code)(code) for code in batch_codes)
            current_batch += 1
        except BaseException as err:
            log.error(f"sync the fund flow batch No.{current_batch} error: {err=}, {type(err)=}")
            continue
        finally:
            log.info(f"sync the fund flow batch No.{current_batch} finished")
            time.sleep(60)
    log.info("sync all the fund flow task finished!!!")

