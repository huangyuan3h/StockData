from sqlalchemy import and_


def get_kline_by_code(code: str, limit=500):
    from dao.model.Kline import Kline
    """
    get stock data by code order by date aec
    current limit 500
    """
    return Kline.query.filter_by(code=code).order_by(Kline.timestamp.desc()).limit(limit).all()


def get_last(code: str):
    from dao.model.Kline import Kline
    result = Kline.query.filter_by(code=code).order_by(Kline.timestamp.desc()).first()
    return result


def get_stock_code_list_200_capital():
    from dao.model.Kline import Kline
    BYD_code = 'SZ002594'
    record = get_last(BYD_code)
    lines = Kline.query.filter(and_(Kline.timestamp == record.timestamp, Kline.market_capital > 2 * 10000000000)).all()
    return list(map(lambda stock: stock.code, lines))

