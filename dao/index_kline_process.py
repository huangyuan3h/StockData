def get_last(code: str):
    from dao.model.IndexKline import IndexKline
    result = IndexKline.query.filter_by(code=code).order_by(IndexKline.timestamp.desc()).first()
    return result
