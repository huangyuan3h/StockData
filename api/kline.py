from flask import jsonify

from api.response_code import OK
from dao.kline_process import get_kline_by_code
from tasks import sync_kline_by_code
from tasks import sync_kline_day_all


def sync_stock_by_code(code: str):
    sync_kline_by_code.delay(code)
    return OK


def sync_all_stock():
    sync_kline_day_all.delay()
    return OK


def get_stock_data(code: str):
    """
    get stock data by code order by date aec
    current limit 200
    """
    result = get_kline_by_code(code)
    res = list(map(lambda i: i.as_dict(), result))
    return jsonify(res)
