from log import log
from task_manager import Task
from xueqiu.list import get_list

DEFAULT_LENGTH = 3  # set as default length


class SyncStockListTask(Task):

    async def run(self):
        log.info('sync stock start to run')
        data = get_list(1, DEFAULT_LENGTH)
        log.info("stock list contains %s has been pulled from server", len(data))
        stock_list = data['data']['list']
        from dao import dao
        from dao.Stock import Stock
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
        return self
