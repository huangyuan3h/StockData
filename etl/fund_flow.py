from sqlalchemy.orm import Session
from sqlalchemy import select

from etl.model.FundFlow import FundFlow
from etl.utils import save_data, get_target_engine

if __name__ == '__main__':
    engine = get_target_engine()
    fundingFlows = None
    with Session(engine) as session:
        stmt = select(FundFlow)
        fundingFlows = session.scalars(stmt).all()

    add_list = []

    for s in fundingFlows:
        add_list.append(
            FundFlow(code=s.code, timestamp=s.timestamp, main_percent=s.main_percent, huge_percent=s.huge_percent,
                     large_percent=s.large_percent, middle_percent=s.middle_percent, small_percent=s.small_percent))

    save_data(add_list)
