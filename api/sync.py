from flask import (Blueprint)

from xueqiu.list import get_list

bp = Blueprint('sync', __name__, url_prefix='/sync')

DEFAULT_LENGTH = 4295

@bp.route('/list')
def list():
    data = get_list(1, 30)
    stock_list = data['data']['list']
    print(stock_list)
    return data
