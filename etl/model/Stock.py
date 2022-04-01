from sqlalchemy import Column, String

from etl.model import Base

class Stock(Base):
    __tablename__ = 'stock'
    code = Column(String(16), unique=True, primary_key=True)
    name = Column(String(64), unique=True, nullable=True)

    def __repr__(self):
        return "<Stock(name='%s', code='%s')>" % (self.name, self.code)
