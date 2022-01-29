from typing import Optional

from sklearn.metrics import mean_absolute_error

from ml.data.BaseDataset import BaseDataset
from ml.data.prepare import get_stock_data, normalize_stock_data
from ml.descission_tree.model import decision_tree


def verify_by_mean_absolute_error(model):
    ds = BaseDataset(60, 10, 100)
    X, y = ds.get_data_set()
    predict = model.predict(X)
    return mean_absolute_error(y, predict)


def predict_result_by_code(code: str) -> Optional[float]:
    df = get_stock_data(code, 60)
    if len(df.index) < 60:
        return None
    nd_data = normalize_stock_data(df).to_numpy()
    nx, ny = nd_data.shape
    reshaped_data = nd_data.reshape(1, nx * ny)
    if not decision_tree.loaded:
        decision_tree.load_model()
    predicted_y = decision_tree.predict(reshaped_data)
    return float(predicted_y[0])
