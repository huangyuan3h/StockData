from api.response_code import OK


def sync_index_kline_by_code(code: str):
    from tasks import sync_index_kline_by_code as sync_by_code
    sync_by_code.delay(code)
    return OK


def sync_index_kline_all():
    from tasks import sync_index_kline_day_all as sync_all
    sync_all.delay()
    return OK
