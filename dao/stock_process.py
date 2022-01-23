


def get_stock_code_list():
    from dao.model.Stock import Stock
    stocks = Stock.query.all()
    return list(map(lambda stock: stock.code, stocks))
