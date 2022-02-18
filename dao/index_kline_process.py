def get_last(code: str):
    from dao.model.IndexKline import IndexKline
    from dao.session_maker import session_maker
    with session_maker() as session:
        result = session.query(IndexKline).filter_by(code=code).order_by(IndexKline.timestamp.desc()).first()
    return result


def get_index_kline(code: str, limit: int):
    from dao.model.IndexKline import IndexKline
    from dao.session_maker import session_maker
    with session_maker() as session:
        return session.query(IndexKline).filter_by(code=code).order_by(IndexKline.timestamp.desc()).limit(limit).all()
