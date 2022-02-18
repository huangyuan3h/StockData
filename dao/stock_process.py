def get_stock_code_list():
    from dao.model.Stock import Stock
    from dao.session_maker import session_maker
    with session_maker() as session:
        stocks = session.query(Stock).all()
    return list(map(lambda stock: stock.code, stocks))
