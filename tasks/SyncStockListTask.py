from task_manager import Task
from xueqiu.list import get_list

DEFAULT_LENGTH = 10000  # set as default length


class SyncStockListTask(Task):

    def run(self):
        data = get_list(1, DEFAULT_LENGTH)
        stock_list = data['data']['list']
        from dao import dao
        from dao.Stock import Stock
        session = dao.db.session

        try:
            for i in stock_list:
                stock = Stock(code=i['symbol'], name=i['name'])
                session.merge(stock)
            session.commit()
        except:
            session.rollback()
            raise
        return self
