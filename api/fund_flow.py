from api.response_code import OK


def sync_all_fund_flow():
    from tasks import sync_all_fund_flow as sync_all
    sync_all.delay()
    return OK


def sync_fund_flow_by_code(code: str):
    from tasks import sync_fund_flow_by_code as sync_by_code
    sync_by_code.delay(code)
    return OK
