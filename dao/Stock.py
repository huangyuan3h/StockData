from sqlalchemy import Column, String




class Stock(connection.get_Base()):
    __tablename__ = 'stock'
    code = Column(String, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Stock(name='%s', code='%s')>" % (self.name, self.code)
