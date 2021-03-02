from flask import (Blueprint)

from dao.Session import Session
from dao.Stock import Stock
from xueqiu.list import get_list

bp = Blueprint('sync', __name__, url_prefix='/sync')

DEFAULT_LENGTH = 4295

@bp.route('/list')
def list():
    data = get_list(1, 30)
    stock_list = data['data']['list']
    for i in stock_list:
        session = Session().get_session()
        try:
            stock = Stock(code=i.symbol, name=i.name)
            session.add(stock)
            session.commit()
        except:
            session.rollback()
            raise
    return data
