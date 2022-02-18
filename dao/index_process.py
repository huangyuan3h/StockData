def get_index_list():
    from dao.model.Index import Index
    from dao.session_maker import session_maker
    with session_maker() as session:
        indexes = session.query(Index).all()
    return list(map(lambda i: i.code, indexes))
