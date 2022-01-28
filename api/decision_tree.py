"""
training the model by number
"""
from ml.data.prepare import get_stock_data, normalize_stock_data
from ml.descission_tree.model import decision_tree
from tasks import training_decision_tree as training


def training_decision_tree(num: int):
    training.delay(batch_size=num)
    return "ok"


def predict_by_stock_code(code: str):
    df = get_stock_data(code, 60)
    if len(df.index) < 60:
        return "not able to predict"
    nd_data = normalize_stock_data(df).to_numpy()
    nx, ny = nd_data.shape
    reshaped_data = nd_data.reshape(1, nx * ny)
    if not decision_tree.loaded:
        decision_tree.load_model()
    predicted_y = decision_tree.predict(reshaped_data)
    return {"result": predicted_y[0]}
