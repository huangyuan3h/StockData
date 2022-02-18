from sqlalchemy import Column, String, Integer, DECIMAL, TIMESTAMP

from dao import dao
from dao.model.DictMixIn import DictMixIn


class IndexKline(dao.Model, DictMixIn):
    __tablename__ = 'index_kline'
    id = Column(Integer, primary_key=True)
    code = Column(String(16))
    timestamp = Column(TIMESTAMP)
    volume = Column(DECIMAL(16, 0))  # 成交量
    open = Column(DECIMAL(16, 2))  # 今开
    high = Column(DECIMAL(16, 2))  # 最高
    low = Column(DECIMAL(16, 2))  # 最低
    close = Column(DECIMAL(16, 2))  # 今收
    chg = Column(DECIMAL(16, 2))  # 涨跌价
    percent = Column(DECIMAL(16, 2))  # 涨跌价
    turnoverrate = Column(DECIMAL(16, 2))  # 换手率
    amount = Column(DECIMAL(16, 2))  # 成交额

    def __repr__(self):
        return "<IndexKline(id='%d', code='%s', timestamp='%s')>" % (self.id, self.code, str(self.timestamp))
