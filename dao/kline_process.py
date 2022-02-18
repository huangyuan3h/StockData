def get_kline_by_code(code: str, limit=500):
    from dao.model.Kline import Kline
    """
    get stock data by code order by date aec
    current limit 500
    """
    from dao.session_maker import session_maker
    with session_maker() as session:
        return session.query(Kline).filter_by(code=code).order_by(Kline.timestamp.desc()).limit(limit).all()


def get_last(code: str):
    from dao.model.Kline import Kline
    from dao.session_maker import session_maker
    with session_maker() as session:
        result = session.query(Kline).filter_by(code=code).order_by(Kline.timestamp.desc()).first()
    return result
