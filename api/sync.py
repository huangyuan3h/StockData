import datetime

from flask import (Blueprint)

from scheduler import scheduler, sync_list

bp = Blueprint('sync', __name__, url_prefix='/sync')

DEFAULT_LENGTH = 10000  # set as default length


@bp.route('/list')
def list():
    scheduler.add_job(func=sync_list.run, id='sync_list_' + str(datetime.datetime.now())
                      , next_run_time=datetime.datetime.now())
    return {"code": '200'}
