
from flask import (Blueprint)

bp = Blueprint('task', __name__, url_prefix='/task')


'''
get task list
'''
@bp.route('/list')
def list():
    return 'any';
