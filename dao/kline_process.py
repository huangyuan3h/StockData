from dao.model.Kline import Kline


def get_kline_by_code(code: str, limit=200):
    """
    get stock data by code order by date aec
    current limit 200
    """
    return Kline.query.filter_by(code=code).order_by(Kline.timestamp.desc()).limit(limit).all()
