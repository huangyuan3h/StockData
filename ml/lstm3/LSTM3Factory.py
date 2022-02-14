import os

from tensorflow import keras

from ml.BaseModelFactory import BaseModelFactory
from ml.data.BaseDataset import BaseDataset
from ml.lstm3.model import get_lstm3_model


class LSTM3Factory(BaseModelFactory):
    def __init__(self, name='lstm3', predict_day=3, chart_size=60, batch_size=1000, new_model=False, path=None):
        """
        data part
        """
        BaseModelFactory.__init__(name=name, predict_day=predict_day, chart_size=chart_size, batch_size=batch_size,
                                  path=path)
        self.data_set = BaseDataset(chart_size=chart_size, mask_size=predict_day, batch_size=batch_size)

        """
        model:
        """
        self.model = get_lstm3_model(n_steps=60, n_features=14, lstm_layer_size=1024) if new_model or not os.path.isfile(
            self.path) else keras.models.load_model(path)


