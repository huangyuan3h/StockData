"""
training the model by number
"""
from ml.get_factory import get_factory
from tasks import generate_report as report
from tasks import training_model as training


def training_lstm(model='lstm', predict_day=3, num=10):
    training.delay(model_name=model, predict_day=predict_day, batch_size=num)
    return "ok"


def predict_n_day_by_stock_code(code: str, model='lstm', predict_day=3):
    Factory = get_factory(model)
    factory = Factory(predict_day=predict_day)
    result = factory.predict_today_by_code(code)
    if result is None:
        return "not able to predict"
    else:
        return {"result": result}


def generate_n_day_report(model='lstm', predict_day=3):
    report.delay(model_name=model, predict_day=predict_day)
    return "ok"
