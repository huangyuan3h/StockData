from sqlalchemy.orm import Session
from sqlalchemy import select
from etl.model.IndexKline import IndexKline

from etl.utils import save_data, get_target_engine

if __name__ == '__main__':
    engine = get_target_engine()
    index_klines = None
    with Session(engine) as session:
        stmt = select(IndexKline)
        index_klines = session.scalars(stmt).all()

    add_list = []

    for s in index_klines:
        add_list.append(
            IndexKline(code=s.code, timestamp=s.timestamp, volume=s.volume, open=s.open, high=s.high, low=s.low,
                       close=s.close, chg=s.chg, percent=s.percent, turnoverrate=s.turnoverrate, amount=s.amount))

    save_data(add_list)
