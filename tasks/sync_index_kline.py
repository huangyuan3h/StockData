from joblib import Parallel, delayed
from dao.index_kline_process import get_last
from log import log
from task_manager import task_manager
from utils.dateUtils import to_db_timestamp
from xueqiu.kline import get_data_from_last_record


def get_index_kline_list():
    from dao.index_process import get_index_list
    index_list = get_index_list()
    return index_list


@task_manager.celery.task()
def sync_index_kline_by_code(code: str):
    last_record = get_last(code)
    data = get_data_from_last_record(code, getattr(last_record, 'timestamp', None))
    if data is None:
        log.info(f"skip sync: {code}")
        return
    index_kline_list = data['data']['item']
    from dao.session_maker import session_maker
    from dao.model.IndexKline import IndexKline
    with session_maker() as session:
        for i in index_kline_list:
            index = IndexKline(code=code, timestamp=to_db_timestamp(i[0]), volume=i[1], open=i[2], high=i[3],
                               low=i[4], close=i[5],
                               chg=i[6], percent=i[7], turnoverrate=i[8], amount=i[9])
            session.add(index)
        session.commit()
        log.info("index kline %s has been synchronized to latest", code)
    return


@task_manager.celery.task()
def sync_index_kline_day_all():
    indexes = get_index_kline_list()
    Parallel(n_jobs=30, backend="threading")(delayed(sync_index_kline_by_code)(i) for i in indexes)
    log.info("sync the index kline task finished!!!")
