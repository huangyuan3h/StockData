from abc import ABC, abstractmethod

from tensorflow import keras


class BaseModelFactory(ABC):

    def __init__(self, name='lstm', predict_day=3, chart_size=60, batch_size=1000, path=None):
        """
        data part
        """
        self.name = name
        self.predict_day = predict_day
        self.chart_size = chart_size
        self.batch_size = batch_size

        """
        model:
        """
        self.path = path if path is not None else f'model_data/{name}_{predict_day}'
        self.model = None

    def save(self):
        self.model.save(self.path, overwrite=True, include_optimizer=True)

    def load(self, path=None):
        self.model = keras.models.load_model(path if path is not None else self.path)
        return self.model

    @abstractmethod
    def predict_today_by_code(self, code):
        pass
