"""
training the model by number
"""
from ml.descission_tree.verify import predict_result_by_code
from tasks import generate_decision_tree_report as report
from tasks import training_decision_tree as training


def training_decision_tree(num: int):
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
