from sklearn.metrics import mean_absolute_error

from ml.BaseModelFactory import BaseModelFactory
from ml.data.BaseDataset import BaseDataset
from ml.data.prepare import choose_random_stock_codes


def verify_model(factory: BaseModelFactory, code_num=100) -> float:
    codes = choose_random_stock_codes(code_num)
    ds = factory.data_set
    X, y = ds.get_test_data_by_codes(codes)
    model = factory.model
    predict_y = model.predict(X)
    res = -1
    try:
        res = mean_absolute_error(predict_y, y)
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
    finally:
        return res


def verify_models(Factory: BaseModelFactory, DataSet: BaseDataset, code_num=500, mask_size=3, paths=[],
                  kline_range=150) -> []:
    codes = choose_random_stock_codes(code_num)
    ds = DataSet(mask_size=mask_size)
    X, y = ds.get_test_data_by_codes(codes, kline_range=kline_range)

    result = []
    for path in paths:
        factory = Factory(path=path)
        model = factory.model
        predict_y = model.predict(X)
        res = mean_absolute_error(predict_y, y)
        result.append(res)
    return result


def verify_by_mean_absolute_error(model):
    ds = BaseDataset(60, 10, 100)
    X, y = ds.get_data_set()
    predict = model.predict(X)
    return mean_absolute_error(y, predict)
