import random

from pandas import DataFrame
from torch.utils.data import Dataset

"""

this ml is to find the next 10 day will get big interest

so we need 70 records
"""
import app
from dao.kline_process import get_kline_by_code
from dao.mapping.kline_mapping import kline_obj_2_dataframe
from dao.stock_process import get_stock_code_list


def choose_a_random_stock_code():
    stock_list = get_stock_code_list()
    return random.choice(stock_list)


def get_stock_dataframe():
    return kline_obj_2_dataframe(get_kline_by_code(choose_a_random_stock_code()))


class StockListDataset(Dataset):
    data = []  # training data
    labels = []  # labels

    def __init__(self, chart_size=60, predict_after_size=10, total_size=10000):

        self.chart_size = chart_size
        self.predict_after_size = predict_after_size
        self.min_training_size = chart_size + predict_after_size
        self.total_size = total_size

    def get_valid_data(self):
        while True:
            df = get_stock_dataframe()
            if len(df.index) > self.min_training_size:
                return df

    def get_n_records_data(self, df: DataFrame, offset=0):
        if (offset + self.min_training_size) > len(df.index):
            return None
        else:
            return df[offset:offset + self.min_training_size]

    def get_last_n_day_change_by_percent(self, df: DataFrame, offset=0):
        last_close_price = float(df["close"][offset])
        last_n_close_price = float(df["close"][self.predict_after_size+offset])
        return (last_close_price - last_n_close_price) * 100.0 / last_n_close_price

    def get_training_dataframe(self, df: DataFrame, offset = 0):
        return df[self.predict_after_size+offset:]

    def generate_training_data_and_labels(self):

        while len(self.labels) < self.total_size:
            df = self.get_valid_data()

            loop_count = len(df.id) - self.min_training_size

            for offset in range(loop_count):
                if len(self.labels) == self.total_size:
                    break
                df2 = self.get_n_records_data(df, offset)
                percentage = self.get_last_n_day_change_by_percent(df2, offset)
                training_data = self.get_training_dataframe(df2, offset)
                ## delete code id timestamp
                del training_data['id']
                del training_data['code']
                del training_data['timestamp']

                self.data.append(training_data.to_numpy())
                self.labels.append(percentage)


def kline_process():
    stock_dataset = StockListDataset()
    stock_dataset.generate_training_data_and_labels()
    print(stock_dataset.data)
    print(stock_dataset.labels)


if __name__ == '__main__':
    kline_process()
