from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Stock(Base):
    __tablename__ = 'stock'
    code = Column(String, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Stock(name='%s', code='%s')>" % (self.name, self.code)
