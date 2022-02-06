import os

from tensorflow import keras

from ml.data.BaseDataset import BaseDataset
from ml.lstm.model import get_lstm_model


class LSTMFactory(object):
    def __init__(self, name='lstm', predict_day=3, chart_size=60, batch_size=1000, new_model=False, path=None):
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
        self.path = path if path is not None else f'model_data/{name}_{predict_day}.tf'
        self.model = get_lstm_model(n_steps=60, n_features=13, lstm_layer_size=512) if new_model or not os.path.isfile(
            self.path) else keras.models.load_model(path)

    def save(self):
        keras.models.save_model(self.model, self.path, overwrite=True, include_optimizer=True, save_format='tf')
