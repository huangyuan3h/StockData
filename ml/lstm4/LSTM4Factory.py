import os

from tensorflow import keras

from ml.BaseModelFactory import BaseModelFactory
from ml.data.prepare import normalize_stock_data
from ml.lstm4.VXXDataset import VXXDataset
from ml.lstm4.model import get_lstm4_model


class LSTM4Factory(BaseModelFactory):
    def __init__(self, name='lstm4', predict_day=3, chart_size=60, batch_size=3000, new_model=False, path=None):
        """
        data part
        """
        BaseModelFactory.__init__(self, name=name, predict_day=predict_day, chart_size=chart_size,
                                  batch_size=batch_size,
                                  path=path)
        self.data_set = VXXDataset(chart_size=chart_size, mask_size=predict_day, batch_size=batch_size)

        """
        model:
        """
        if new_model or not os.path.isdir(self.path):
            self.model = get_lstm4_model()
            print(f"{self.path} new model generated")
        else:
            self.model = keras.models.load_model(self.path)
            print(f"{self.path} model loaded..")

    def predict_today_by_code(self, code: str):
        df = self.data_set.get_today_df_by_code(code)
        if len(df.index) < self.chart_size:
            return None
        nd_data = normalize_stock_data(df).to_numpy().tolist()
        reshaped_data = nd_data
        predicted_y = self.model.predict([reshaped_data])
        return float(predicted_y[0])
