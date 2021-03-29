import time
from datetime import datetime
from numbers import Number


def to_db_timestamp(timestamp: Number):
    return datetime.fromtimestamp(timestamp / 1000)


def to_timestamp_millisecond(date: datetime):
    return round(date.timestamp() * 1000)


def get_current_timestamp_millisecond():
    return round(time.time() * 1000)


'''
eg: 2020-01-01
'''


def get_today_millisecond():
    now = datetime.now()
    today = datetime(now.year, now.month, now.day)
    return to_timestamp_millisecond(today)


