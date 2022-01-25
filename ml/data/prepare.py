import random
import typing

from pandas import DataFrame

from dao.kline_process import get_kline_by_code
from dao.mapping.kline_mapping import kline_obj_2_dataframe
from dao.stock_process import get_stock_code_list


def choose_a_random_stock_code() -> str:
    stock_list = get_stock_code_list()
    return random.choice(stock_list)


def get_stock_data(code=choose_a_random_stock_code(), size=500) -> DataFrame:
    return kline_obj_2_dataframe(get_kline_by_code(code, size))


def get_stock_data_greater_then_min_size(min_size=70, total_size=500) -> DataFrame:
    while True:
        df = get_stock_data(size=total_size)
        if len(df.index) > min_size:
            return df


def get_stock_data_by_size(df: DataFrame, size=70, offset=0) -> typing.Union[None, DataFrame]:
    if (offset + size) > len(df.index):
        return None
    else:
        return df[offset:offset + size]


def get_change_by_mask_size(df: DataFrame, mask_size=10, offset=0) -> float:
    last_close_price = float(df["close"][offset])
    last_n_close_price = float(df["close"][mask_size + offset + 1])
    return (last_close_price - last_n_close_price) * 100.0 / last_n_close_price
