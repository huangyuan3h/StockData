from typing import Optional

from sklearn.metrics import mean_absolute_error

from ml.data.BaseDataset import BaseDataset
from ml.data.prepare import get_stock_data, normalize_stock_data


def verify_by_mean_absolute_error(model):
    ds = BaseDataset(60, 10, 100)
    X, y = ds.get_data_set()
    predict = model.predict(X)
    return mean_absolute_error(y, predict)


def predict_result_by_code(code: str, model, chart_size=60) -> Optional[float]:
    df = get_stock_data(code, chart_size)
    if len(df.index) < chart_size:
        return None
    nd_data = normalize_stock_data(df).to_numpy().tolist()
    reshaped_data = nd_data
    predicted_y = model.predict([reshaped_data])
    return float(predicted_y[0]), df
