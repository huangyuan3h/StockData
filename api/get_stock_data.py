"""
get stock data by code order by date aec
current limit 200
"""
from flask import jsonify

from dao.kline_process import get_kline_by_code


def get_stock_data(code: str):
    result = get_kline_by_code(code)
    res = list(map(lambda i: i.as_dict(), result))
    return jsonify(res)
