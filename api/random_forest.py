"""
training the model by number
"""
from ml.data.verify import predict_result_by_code
from ml.random_forest.RandomForestModelFactory import RandomForestModelFactory
from tasks import generate_decision_tree_report as report
from tasks import training_random_forest_3 as training


def training_random_forest_3(num: int):
    training.delay(batch_size=num)
    return "ok"


def predict_by_stock_code(code: str):
    factory = RandomForestModelFactory(predict_day=3)
    result = predict_result_by_code(code, factory.model)
    if result is None:
        return "not able to predict"
    else:
        return result


def generate_decision_tree_report():
    report.delay()
    return "ok"
