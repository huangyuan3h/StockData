def get_all_code_list():
    from dao.Stock import Stock
    stocks = Stock.query.all()
    codes = list(map(lambda stock: stock.code, stocks))
    return codes


def run():
    from scheduler.sync_kline_by_code import run as run_by_code
    codes = get_all_code_list()
    for code in codes: # todo: use pool = multiprocessing.Pool(4)
        run_by_code(code)
