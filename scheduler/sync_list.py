from xueqiu.list import get_list

DEFAULT_LENGTH = 10000  # set as default length


def sync_list(size=DEFAULT_LENGTH):
    data = get_list(1, size)
    stock_list = data['data']['list']
    for i in stock_list:
        from dao import db
        session = db.session
        try:
            from dao.Stock import Stock
            stock = Stock(code=i['symbol'], name=i['name'])
            session.merge(stock)
            session.commit()
        except:
            session.rollback()
            raise
