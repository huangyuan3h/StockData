def get_kline_by_code(code: str, limit=500):
    from dao.model.Kline import Kline
    """
    get stock data by code order by date aec
    current limit 500
    """
    return Kline.query.filter_by(code=code).order_by(Kline.timestamp.desc()).limit(limit).all()
