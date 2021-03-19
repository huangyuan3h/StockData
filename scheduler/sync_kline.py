from xueqiu.kline import period_type, get_data

DEFAULT_MODE = '60m'

start_date = 1577836800000  # 2020-01-01


def get_last(code):
    from dao import dao
    session = dao.db.session


def run():
    data = get_data(begin=start_date, period=DEFAULT_MODE, count='2')
    print(data)
    return data
