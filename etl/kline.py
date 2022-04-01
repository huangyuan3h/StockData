import math

from sqlalchemy.orm import Session
from sqlalchemy import select
from etl.model.Kline import Kline

from etl.utils import save_data, get_target_engine

if __name__ == '__main__':
    engine = get_target_engine()
    klines = None
    per_page = 10000
    current_page = 1
    total = 3807989

    total_loop = total / 10000

    for x in range(math.ceil(total_loop)):
        current_page = x + 1

        with Session(engine) as session:
            stmt = select(Kline).limit(per_page).offset((current_page - 1) * per_page)
            klines = session.scalars(stmt).all()

        add_list = []

        for s in klines:
            add_list.append(
                Kline(code=s.code, timestamp=s.timestamp, volume=s.volume, open=s.open, high=s.high, low=s.low,
                      close=s.close, chg=s.chg, percent=s.percent, turnoverrate=s.turnoverrate, amount=s.amount,
                      pe=s.pe, pb=s.pb, ps=s.ps, pcf=s.pcf, market_capital=s.market_capital))

        save_data(add_list)
        print(f"import kline No.{current_page} finished!")
