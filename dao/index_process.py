def get_index_list():
    from dao.model.Index import Index
    indexes = Index.query.all()
    return list(map(lambda i: i.code, indexes))
