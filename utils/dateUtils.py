from datetime import datetime
import time
from numbers import Number


def to_db_timestamp(timestamp: Number):
    return datetime.fromtimestamp(timestamp / 1000)


def to_timestamp_millisecond(date: datetime):
    return round(date.timestamp() * 1000)


def get_current_timestamp_millisecond():
    return round(time.time() * 1000)
