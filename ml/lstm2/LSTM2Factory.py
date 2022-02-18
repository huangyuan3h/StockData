import os

from tensorflow import keras

from ml.BaseModelFactory import BaseModelFactory
from ml.data.BaseDataset import BaseDataset
from ml.data.prepare import get_stock_data, normalize_stock_data
from ml.lstm2.model import get_lstm2_model


class LSTM2Factory(BaseModelFactory):
    def __init__(self, name='lstm2', predict_day=3, chart_size=60, batch_size=1000, new_model=False, path=None):
        """
        data part
        """
        BaseModelFactory.__init__(self, name=name, predict_day=predict_day, chart_size=chart_size,
                                  batch_size=batch_size,
                                  path=path)
        self.data_set = BaseDataset(chart_size=chart_size, mask_size=predict_day, batch_size=batch_size)

        """
        model:
        """
        self.model = get_lstm2_model(n_steps=60, n_features=14,
                                     lstm_layer_size=1024) if new_model or not os.path.isfile(
            self.path) else keras.models.load_model(path)

    def predict_today_by_code(self, code: str):
        df = self.data_set.get_today_df_by_code(code)
        if len(df.index) < self.chart_size:
            return None
        nd_data = normalize_stock_data(df).to_numpy().tolist()
        reshaped_data = nd_data
        predicted_y = self.model.predict([reshaped_data])
        return float(predicted_y[0])
