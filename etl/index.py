from sqlalchemy.orm import Session
from sqlalchemy import select
from etl.model.Index import Index

from etl.utils import save_data, get_target_engine

if __name__ == '__main__':
    engine = get_target_engine()
    indexes = None
    with Session(engine) as session:
        stmt = select(Index)
        indexes = session.scalars(stmt).all()

    add_list = []

    for s in indexes:
        add_list.append(Index(code=s.code, name=s.name))

    save_data(add_list)
