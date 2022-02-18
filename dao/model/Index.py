from sqlalchemy import Column, String
from dao import dao


class Index(dao.Model):
    __tablename__ = 'index'
    code = Column(String(16), unique=True, primary_key=True)
    name = Column(String(64), unique=True, nullable=True)

    def __repr__(self):
        return "<Index(name='%s', code='%s')>" % (self.name, self.code)
