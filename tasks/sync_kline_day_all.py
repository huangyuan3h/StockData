from dao.stock_process import get_stock_code_list
from task_manager import task_manager
from log import log


def get_all_code_list():
    codes = get_stock_code_list()
    return codes


@task_manager.celery.task()
def sync_kline_day_all():
    from tasks import run_by_code
    codes = get_all_code_list()
    for code in codes:
        run_by_code(code)
        log.info("%s has been synchronized to latest", code)
