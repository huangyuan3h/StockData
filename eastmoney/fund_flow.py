import requests

URL = "http://push2his.eastmoney.com/api/qt/stock/fflow/daykline/get"

PARAMS = {
    "fields1": "f7",
    "fields2": "f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63",
    "secid": "1.601012"
}


def get_request_code(code: str) -> str:
    num_part = code[2:]
    return f"0.{num_part}" if code.startswith('SZ') else f"1.{num_part}"


def get_data_by_code(code: str):
    c = get_request_code(code)
    PARAMS.update({'secid': c})
    r = requests.get(url=URL, params=PARAMS)
    response = r.json()
    kline_strings = response["data"]["klines"]
    res = map(lambda x: x.split(','), kline_strings)
    return list(res)

