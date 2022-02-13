def get_last(code: str):
    from dao.model.FundFlow import FundFlow
    result = FundFlow.query.filter_by(code=code).order_by(FundFlow.timestamp.desc()).first()
    return result
