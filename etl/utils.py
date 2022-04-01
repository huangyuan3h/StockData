from urllib.parse import quote

from sqlalchemy import create_engine
from etl.model import Base
from sqlalchemy.orm import Session


def save_data(list: []):
    engine = create_engine("mysql+pymysql://root:%s@192.168.31.2/stockData" % quote('P@$$uu0rd123'), future=True)

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        session.add_all(list)
        session.commit()


def get_target_engine():
    return create_engine("mysql+pymysql://root:root@192.168.31.3/stock", future=True)
