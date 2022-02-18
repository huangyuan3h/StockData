from sqlalchemy import Column, String, Integer, DECIMAL, TIMESTAMP
from dao import dao


class Report(dao.Model):
    __tablename__ = 'report'
    id = Column(Integer, primary_key=True)
    code = Column(String(16))
    predict = Column(DECIMAL(16, 2))
    type = Column(String(16))
    timestamp = Column(TIMESTAMP)

    def __repr__(self):
        return "<Report(id='%d', code='%s', predict='%s')>" % (self.id, self.code, str(self.predict))
