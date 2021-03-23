from xueqiu.kline import period_type, get_data
from datetime import datetime
DEFAULT_MODE = period_type['1day']

start_date = 1514736000000  # 2018-01-01

count = 2  # 244 * 5  # 244 trade days *5 years


def get_last(code):
    from dao.Kline import Kline
    result = Kline.query.filter_by(code=code).first()
    return result


def run(code):
    last_record = get_last(code)
    start_date_param = start_date if (last_record is None) else last_record['timestamp']
    data = get_data(code=code, begin=start_date_param, period=DEFAULT_MODE, count=str(count))
    kline_list = data['data']['item']
    from dao import dao
    from dao.Kline import Kline
    session = dao.db.session

    try:
        for i in kline_list:
            stock = Kline(code=code, timestamp=datetime.fromtimestamp(i[0]/1000), volume=i[1], open=i[2], high=i[3], low=i[4], close=i[5],
                          chg=i[6], percent=i[7], turnoverrate=i[8], amount=i[9], pe=i[12],
                          pb=i[13], ps=i[14], pcf=i[15], market_capital=i[16])
            session.add(stock)
        session.commit()
    except:
        session.rollback()
        raise
    return data
