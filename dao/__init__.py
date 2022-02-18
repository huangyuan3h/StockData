from flask import _app_ctx_stack
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session

from dao.connection import get_connection_str
from dao.kline_process import get_kline_by_code


class DataAccess:
    session = None
    Model = None

    def register(self):
        engine = create_engine(get_connection_str())
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        self.Model = declarative_base()
        self.session = scoped_session(SessionLocal, scopefunc=_app_ctx_stack.__ident_func__)
        from dao.model import Stock
        from dao.model import Kline
        from dao.model import Report
        from dao.model import Index
        from dao.model import IndexKline
        from dao.model import FundFlow
        self.Model.metadata.create_all(bind=engine)


dao = DataAccess()
