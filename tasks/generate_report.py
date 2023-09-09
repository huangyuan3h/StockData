import math
from datetime import datetime

from joblib import Parallel, delayed

from log import log
from ml.get_factory import get_factory
from task_manager import task_manager


def predict_single(c: str, factory) -> None:
    from dao.report_process import get_by_code_type_date
    from dao.session_maker import session_maker
    from dao.model.Report import Report
    from dao.kline_process import get_last
    current_type = factory.name + '_' + str(factory.predict_day)
    date = datetime.today().strftime('%Y-%m-%d')
    result = get_by_code_type_date(c, current_type, date)
    if result is not None:
        return
    last_record = get_last(c)
    with session_maker() as session:
        p = factory.predict_today_by_code(c)
        if p is None or math.isnan(p) or last_record is None:
            log.info(f"data error p is {p}")
            return
        report = Report(code=c, predict=p, type=current_type,
                        timestamp=last_record.timestamp)
        session.add(report)
        session.commit()
        log.info("%s has been predicted and saved in db", c)


@task_manager.celery.task()
def generate_report(model_name='lstm', predict_day=3, *args, **kwargs):
    from dao.kline_process import get_stock_code_list_100_capital
    stock_code_list = get_stock_code_list_100_capital()
    Factory = get_factory(model_name)
    factory = Factory(predict_day=predict_day)
    Parallel(n_jobs=20, backend="threading")(delayed(predict_single)(code, factory) for code in stock_code_list)
