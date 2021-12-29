from log import log
from xueqiu.list import get_list
from task_manager import task_manager

DEFAULT_LENGTH = 10000  # set as default length


@task_manager.celery.task()
def sync_stock_list():
    log.info('sync stock start to run')
    data = get_list(1, DEFAULT_LENGTH)
    log.info("stock list contains %s has been pulled from server", len(data))
    stock_list = data['data']['list']
    from dao import dao
    from dao.model.Stock import Stock
    session = dao.db.session

    try:
        for i in stock_list:
            stock = Stock(code=i['symbol'], name=i['name'])
            session.merge(stock)
            log.info("stock %s has been added into db", i['name'])
        session.commit()
    except:
        session.rollback()
        raise
    return "finished for sync stock list"
