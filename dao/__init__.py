from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from dao.connection import get_connection_str


class DataAccess:
    db = None
    session = None

    def register(self, app: Flask):
        app.config['SQLALCHEMY_DATABASE_URI'] = get_connection_str()
        self.db = SQLAlchemy(app)
        from dao.model import Stock
        self.db.create_all()
        self.session = self.db.session


dao = DataAccess()
