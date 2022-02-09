import math
from datetime import datetime

from joblib import Parallel, delayed

from log import log
from ml.data.verify import predict_result_by_code
from ml.lstm.LSTMFactory import LSTMFactory
from task_manager import task_manager
from tasks.sync_kline_day_all import get_all_code_list


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
        p = predict_result_by_code(c, factory.model)
        if p is None or math.isnan(p) or last_record is None:
            return
        report = Report(code=c, predict=p, type=current_type,
                        timestamp=last_record.timestamp)
        session.add(report)
        session.commit()
        log.info("%s has been predicted and saved in db", c)


@task_manager.celery.task()
def generate_lstm_report(predict_day=3):
    stock_code_list = get_all_code_list()
    factory = LSTMFactory(predict_day=predict_day)
    Parallel(n_jobs=10, backend="threading")(delayed(predict_single)(code, factory) for code in stock_code_list)
