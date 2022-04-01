from sqlalchemy import Column, String, Integer, DECIMAL, TIMESTAMP

from etl.model import Base

class Report(Base):
    __tablename__ = 'report'
    id = Column(Integer, primary_key=True)
    code = Column(String(16))
    predict = Column(DECIMAL(16, 2))
    type = Column(String(16))
    timestamp = Column(TIMESTAMP)

    def __repr__(self):
        return "<Report(id='%d', code='%s', predict='%s')>" % (self.id, self.code, str(self.predict))
