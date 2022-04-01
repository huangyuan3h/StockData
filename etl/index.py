from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select

from etl.model import Base
from etl.model.Index import Index
from urllib.parse import quote

if __name__ == '__main__':
    engine = create_engine("mysql+pymysql://root:root@192.168.31.3/stock", echo=True, future=True)
    indexes = None
    with Session(engine) as session:
        stmt = select(Index)
        indexes = session.scalars(stmt).all()
        print(indexes)
        # session.commit()

    engine1 = create_engine("mysql+pymysql://root:%s@192.168.31.2/stockData"%quote('P@$$uu0rd123'), echo=True, future=True)
    Base.metadata.create_all(engine1)
    add_list = []

    for s in indexes:
        add_list.append(Index(code=s.code, name=s.name))

    with Session(engine1) as session:
        session.add_all(add_list)
        session.commit()
