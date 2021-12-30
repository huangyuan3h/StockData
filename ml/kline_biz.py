import random

from pandas import DataFrame

import app
"""

this ml is to find the next 3 day will get big interest

so we need 63 records
"""

from dao.kline_process import get_kline_by_code
from dao.mapping.kline_mapping import kline_obj_2_dataframe
from dao.stock_process import get_stock_code_list

min_training_size = 63


def choose_a_random_stock_code():
    stock_list = get_stock_code_list()
    return random.choice(stock_list)


def get_stock_dataframe():
    return kline_obj_2_dataframe(get_kline_by_code(choose_a_random_stock_code()))


def get_valid_data():
    while True:
        df = get_stock_dataframe()
        if len(df.index) > min_training_size:
            return df


def get_63_records_data(df: DataFrame, offset=0):
    if (offset + min_training_size) > len(df.index):
        return None
    else:
        return df[offset:offset+min_training_size]


def get_last_3_day_change_by_percent(df: DataFrame):
    last_close_price = float(df["close"][0])
    last_4_close_price = float(df["close"][3])
    return (last_close_price-last_4_close_price)*100.0/last_4_close_price


def kline_process():
    df = get_valid_data()
    df2 = get_63_records_data(df)
    percentage = get_last_3_day_change_by_percent(df2)
    print(percentage)
    print(df2.head())


if __name__ == '__main__':
    kline_process()
