from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from dao.connection import get_connection_str
from dao.kline_process import get_kline_by_code


class DataAccess:
    db = None
    session = None

    def register(self, app: Flask):
        app.config['SQLALCHEMY_DATABASE_URI'] = get_connection_str()
        app.config['SQLALCHEMY_POOL_SIZE'] = 60
        app.config['SQLALCHEMY_MAX_OVERFLOW'] = -1

        self.db = SQLAlchemy(app)
        from dao.model import Stock
        from dao.model import Kline
        from dao.model import Report
        from dao.model import Index
        from dao.model import IndexKline
        from dao.model import FundFlow
        self.db.create_all()
        self.session = self.db.session


dao = DataAccess()
