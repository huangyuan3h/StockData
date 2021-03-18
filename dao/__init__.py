from app import app
from flask_sqlalchemy import SQLAlchemy
from dao.connection import get_connection_str

app.config['SQLALCHEMY_DATABASE_URI'] = get_connection_str()


db = SQLAlchemy(app)
from dao import Stock, Kline
db.create_all()
