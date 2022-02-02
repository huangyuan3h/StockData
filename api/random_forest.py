"""
training the model by number
"""
from ml.data.verify import predict_result_by_code
from tasks import generate_decision_tree_report as report
from tasks import training_random_forest as training


def training_random_forest_3(num: int):
    training.delay(batch_size=num)
    return "ok"


def predict_by_stock_code(code: str):
    result = predict_result_by_code(code)
    if result is None:
        return "not able to predict"
    else:
        return {"result": result}


def generate_decision_tree_report():
    report.delay()
    return "ok"
