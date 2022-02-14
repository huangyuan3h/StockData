def get_last(code: str):
    from dao.model.FundFlow import FundFlow
    result = FundFlow.query.filter_by(code=code).order_by(FundFlow.timestamp.desc()).first()
    return result


def get_fund_flow_by_code(code: str, limit: int):
    from dao.model.FundFlow import FundFlow
    return FundFlow.query.filter_by(code=code).order_by(FundFlow.timestamp.desc()).limit(limit).all()
