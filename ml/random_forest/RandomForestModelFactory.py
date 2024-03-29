import os

import joblib

from ml.data.BaseDataset import BaseDataset
from ml.random_forest.RandomForestModel import RandomForestModel


class RandomForestModelFactory(object):

    def __init__(self, name='random_forest', predict_day=3, chart_size=60, batch_size=1000, new_model=False, path=None):
        """
        data part
        """
        self.name = name
        self.predict_day = predict_day
        self.chart_size = chart_size
        self.batch_size = batch_size
        self.data_set = BaseDataset(chart_size=chart_size, mask_size=predict_day, batch_size=batch_size)
        """
        model:
        """
        self.path = path if path is not None else f'model_data/{name}_{predict_day}.pkl'

        self.model = RandomForestModel(name=name, predict_day=predict_day) if new_model or not os.path.isfile(
            self.path) else joblib.load(self.path)

    def save(self, score: float, verify=True) -> bool:
        current_score = self.model.score
        if verify:
            if current_score is not None and current_score < score:
                return False
            self.model.score = score
            joblib.dump(self.model, self.path)
            return True
        else:
            self.model.score = score
            joblib.dump(self.model, self.path)
            return current_score < score
