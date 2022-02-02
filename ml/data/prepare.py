import random
import typing

from pandas import DataFrame
from sklearn.impute import SimpleImputer


def choose_a_random_stock_code() -> str:
    from dao.stock_process import get_stock_code_list
    stock_list = get_stock_code_list()
    return random.choice(stock_list)


def get_stock_data(code=None, size=500) -> DataFrame:
    from dao.kline_process import get_kline_by_code
    from dao.mapping.kline_mapping import kline_obj_2_dataframe
    code = code if code is not None else choose_a_random_stock_code()
    return kline_obj_2_dataframe(get_kline_by_code(code, size))


def get_stock_data_greater_then_min_size(min_size=70, total_size=500) -> DataFrame:
    while True:
        df = get_stock_data(size=total_size)
        if len(df.index) > min_size:
            return df


def get_stock_data_by_size(df: DataFrame, size=70, offset=0) -> typing.Union[None, DataFrame]:
    if (offset + size) <= len(df.index):
        return df.iloc[offset:offset + size].reset_index(drop=True)
    else:
        return None


def get_change_by_mask_size(df: DataFrame, mask_size=10) -> float:
    last_close_price = float(df["close"][0])
    last_n_close_price = float(df["close"][mask_size])
    return (last_close_price - last_n_close_price) * 100.0 / last_n_close_price


def normalize_stock_data(data: DataFrame) -> DataFrame:
    return_data = data.copy()
    ## delete code id timestamp
    del return_data['id']
    del return_data['code']
    del return_data['timestamp']

    return_data['volume'] = data['volume'] / 10 ** 5
    return_data['amount'] = data['amount'] / 10 ** 7
    return_data['market_capital'] = data['market_capital'] / 10 ** 9

    return impute_data(return_data)


def impute_data(df: DataFrame) -> DataFrame:
    imp = SimpleImputer()
    return DataFrame(imp.fit_transform(df), columns=df.columns, index=df.index)
