from ml.data.verify import predict_result_by_code
from ml.lstm.LSTMFactory import LSTMFactory
from task_manager import task_manager
from tasks.sync_kline_day_all import get_all_code_list


@task_manager.celery.task()
def generate_lstm_report(predict_day=3):
    from dao.session_maker import session_maker
    from dao.model.Report import Report
    from dao.kline_process import get_last
    stock_code_list = get_all_code_list()
    factory = LSTMFactory(predict_day=predict_day)
    for c in stock_code_list:
        with session_maker() as session:
            last_record = get_last(c)
            p = predict_result_by_code(c, factory.model)
            if p is None or last_record is None:
                continue
            report = Report(code=c, predict=p, type=factory.name + '_' + str(predict_day),
                            timestamp=last_record.timestamp)
            session.add(report)
            session.commit()

