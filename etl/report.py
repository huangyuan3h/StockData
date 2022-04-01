from sqlalchemy.orm import Session
from sqlalchemy import select
from etl.model.Report import Report

from etl.utils import save_data, get_target_engine

if __name__ == '__main__':
    engine = get_target_engine()
    reports = None
    with Session(engine) as session:
        stmt = select(Report)
        reports = session.scalars(stmt).all()

    add_list = []

    for s in reports:
        add_list.append(Report(code=s.code, predict=s.predict, type=s.type, timestamp=s.timestamp))

    save_data(add_list)
