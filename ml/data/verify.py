

from sklearn.metrics import mean_absolute_error

from ml.data.BaseDataset import BaseDataset


def verify_by_mean_absolute_error(model):
    ds = BaseDataset(60, 10, 100)
    X, y = ds.get_data_set()
    predict = model.predict(X)
    return mean_absolute_error(y, predict)

