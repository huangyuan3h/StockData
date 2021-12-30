import random

import app
"""

this ml is to find the next 3 day will get big interest

so we need 63 records
"""

from dao.kline_process import get_kline_by_code
from dao.mapping.kline_mapping import kline_obj_2_dataframe
from dao.stock_process import get_stock_code_list


def kline_process():
    df = kline_obj_2_dataframe(get_kline_by_code(choose_a_random_stock_code()))
    print(df.head())


def choose_a_random_stock_code():
    stock_list = get_stock_code_list()
    return random.choice(stock_list)


if __name__ == '__main__':
    kline_process()
