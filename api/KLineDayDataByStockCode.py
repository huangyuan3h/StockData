from api.Response_Code import OK
from tasks import run_by_code


def start_sync_stock_by_code(code:str):
    run_by_code.delay(code)
    return OK
