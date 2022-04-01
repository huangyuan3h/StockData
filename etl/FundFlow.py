from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select

from etl.model import Base
from etl.model.FundFlow import FundFlow
from urllib.parse import quote

if __name__ == '__main__':
    engine = create_engine("mysql+pymysql://root:root@192.168.31.3/stock", echo=True, future=True)
    fundingFlows = None
    with Session(engine) as session:
        stmt = select(FundFlow)
        fundingFlows = session.scalars(stmt).all()
        # session.commit()

    engine1 = create_engine("mysql+pymysql://root:%s@192.168.31.2/stockData" % quote('P@$$uu0rd123'), echo=True,
                            future=True)
    Base.metadata.create_all(engine1)
    add_list = []

    for s in fundingFlows:
        add_list.append(
            FundFlow(code=s.code, timestamp=s.timestamp, main_percent=s.main_percent, huge_percent=s.huge_percent,
                     large_percent=s.large_percent, middle_percent=s.middle_percent, small_percent=s.small_percent))

    with Session(engine1) as session:
        session.add_all(add_list)
        session.commit()
