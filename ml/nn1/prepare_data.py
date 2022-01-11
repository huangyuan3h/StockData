import random

from pandas import DataFrame

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


class PrepareData(object):

    def __init__(self, chart_size=60, predict_after_size=10):

        self.chart_size = chart_size
        self.predict_after_size = predict_after_size
        self.min_training_size = chart_size + predict_after_size

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

    def get_last_n_day_change_by_percent(self, df: DataFrame):
        last_close_price = float(df["close"][0])
        last_n_close_price = float(df["close"][self.predict_after_size])
        return (last_close_price - last_n_close_price) * 100.0 / last_n_close_price

    def get_training_dataframe(self, df: DataFrame):
        return df[self.predict_after_size:]

    def get_training_data_and_label(self):
        df = self.get_valid_data()
        df2 = self.get_n_records_data(df)
        percentage = self.get_last_n_day_change_by_percent(df2)
        training_data = self.get_training_dataframe(df2)
        ## delete code id timestamp
        del training_data['id']
        del training_data['code']
        del training_data['timestamp']

        return training_data.to_numpy(), percentage


def kline_process():
    prepareData = PrepareData()
    training_data, percentage = prepareData.get_training_data_and_label()
    print(percentage)
    print(training_data)


if __name__ == '__main__':
    kline_process()
