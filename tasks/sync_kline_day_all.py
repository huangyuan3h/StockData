from task_manager import task_manager


def get_all_code_list():
    from dao.Stock import Stock
    stocks = Stock.query.all()
    codes = list(map(lambda stock: stock.code, stocks))
    return codes


@task_manager.celery.task()
def sync_kline_day_all():
    from tasks import run_by_code
    codes = get_all_code_list()
    for code in codes:
        run_by_code(code)
