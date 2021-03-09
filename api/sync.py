from flask import (Blueprint)
from xueqiu.list import get_list

bp = Blueprint('sync', __name__, url_prefix='/sync')

DEFAULT_LENGTH = 10000 # set as default length


@bp.route('/list')
def list():
    data = get_list(1, DEFAULT_LENGTH)
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
    return data
