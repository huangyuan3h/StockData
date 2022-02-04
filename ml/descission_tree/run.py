import app
import pandas as pd

from ml.data.BaseDataset import BaseDataset
from tasks.sync_kline_day_all import get_all_code_list

if __name__ == '__main__':
    # if not decision_tree.loaded:
    #     decision_tree.load_model('../../model_data/decision_tree.pkl')
    #
    # result = verify_by_mean_absolute_error(decision_tree)
    #
    # print(result)
    # stock_code_list = get_all_code_list()
    # code = []
    # predict = []
    # for c in stock_code_list:
    #     p = predict_result_by_code(c)
    #     if p is not None:
    #         code.append(c)
    #         predict.append(p)
    # df = pd.DataFrame({"code": code, "predict": predict})

    ds = BaseDataset()

    ds.get_data_set()
