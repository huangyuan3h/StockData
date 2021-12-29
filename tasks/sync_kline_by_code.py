from task_manager import task_manager
from utils.dateUtils import to_db_timestamp, to_timestamp_millisecond, get_today_millisecond
from xueqiu.kline import period_type, get_data

DEFAULT_MODE = period_type['1day']

start_date = 1514736000000  # 2018-01-01

one_day = 86400000  # 1 day millisecond

count = 244 * 5  # 244 trade days *5 years


def get_last(code):
    from dao.model.Kline import Kline
    result = Kline.query.filter_by(code=code).order_by(Kline.timestamp.desc()).first()
    return result


@task_manager.celery.task()
def sync_kline_by_code(code):
    last_record = get_last(code)
    start_date_param = start_date if (last_record is None) else (
        to_timestamp_millisecond(last_record.timestamp) + one_day)  # next day of last record

    if start_date_param == get_today_millisecond() + one_day:  # if the data has been sync skip
        return None
    data = get_data(code=code, begin=start_date_param, period=DEFAULT_MODE, count=str(count))
    kline_list = data['data']['item']
    from dao import dao
    from dao.model.Kline import Kline
    session = dao.db.session

    try:
        for i in kline_list:
            stock = Kline(code=code, timestamp=to_db_timestamp(i[0]), volume=i[1], open=i[2], high=i[3],
                          low=i[4], close=i[5],
                          chg=i[6], percent=i[7], turnoverrate=i[8], amount=i[9], pe=i[12],
                          pb=i[13], ps=i[14], pcf=i[15], market_capital=i[16])
            session.add(stock)
        session.commit()
    except:
        session.rollback()
        raise
    return data
