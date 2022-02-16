from joblib import Parallel, delayed
from dao.kline_process import get_last
from dao.stock_process import get_stock_code_list
from log import log
from task_manager import task_manager
from utils.dateUtils import to_db_timestamp
from xueqiu.kline import get_data_from_last_record


@task_manager.celery.task()
def sync_kline_by_code(code):
    last_record = get_last(code)
    data = get_data_from_last_record(code, getattr(last_record, 'timestamp', None))
    if data is None:
        log.info(f"skip sync: {code}")
        return
    kline_list = data['data']['item']
    from dao.session_maker import session_maker
    from dao.model.Kline import Kline

    with session_maker() as session:
        for i in kline_list:
            stock = Kline(code=code, timestamp=to_db_timestamp(i[0]), volume=i[1], open=i[2], high=i[3],
                          low=i[4], close=i[5],
                          chg=i[6], percent=i[7], turnoverrate=i[8], amount=i[9], pe=i[12],
                          pb=i[13], ps=i[14], pcf=i[15], market_capital=i[16])
            session.add(stock)
        session.commit()
        log.info("kline %s has been synchronized to latest", code)
    return


def get_all_code_list():
    codes = get_stock_code_list()
    return codes


@task_manager.celery.task()
def sync_kline_day_all():
    codes = get_all_code_list()
    Parallel(n_jobs=5, backend="threading")(delayed(sync_kline_by_code)(code) for code in codes)
    log.info("sync the kline task finished!!!")
