from sqlalchemy.orm import Session
from sqlalchemy import select
from etl.model.Stock import Stock

from etl.utils import save_data, get_target_engine

if __name__ == '__main__':
    engine = get_target_engine()
    stocks = None
    with Session(engine) as session:
        stmt = select(Stock)
        stocks = session.scalars(stmt).all()

    add_list = []

    for s in stocks:
        add_list.append(Stock(code=s.code, name=s.name))

    save_data(add_list)
