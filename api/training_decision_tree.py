"""
training the model by number
"""
from tasks import training_decision_tree as training


def training_decision_tree(num: int):
    training.delay(batch_size=num)
    return "ok"
