import pandas as pd

from ml.data.verify import predict_result_by_code
from task_manager import task_manager
from tasks.sync_kline_day_all import get_all_code_list


@task_manager.celery.task()
def generate_decision_tree_report():
    stock_code_list = get_all_code_list()
    code = []
    predict = []
    for c in stock_code_list:
        try:
            p = predict_result_by_code(c)
            if p is not None:
                code.append(c)
                predict.append(p)
        except:
            print('data error for stock: %s', c)
    df = pd.DataFrame({"code": code, "predict": predict})

    df.sort_values(by='predict', ascending=False)
    df.to_csv('report/decision_tree_10.csv')
