def get_last(code: str):
    from dao.model.FundFlow import FundFlow
    from dao.session_maker import session_maker
    with session_maker() as session:
        result = session.query(FundFlow).filter_by(code=code).order_by(FundFlow.timestamp.desc()).first()
    return result


def get_fund_flow_by_code(code: str, limit: int):
    from dao.model.FundFlow import FundFlow
    from dao.session_maker import session_maker
    with session_maker() as session:
        return session.query(FundFlow).filter_by(code=code).order_by(FundFlow.timestamp.desc()).limit(limit).all()
