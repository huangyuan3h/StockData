from flask import Flask
from flask_restful import Api
from api.StockList import StockList


def register(app: Flask):
    api = Api(app)
    api.add_resource(StockList, '/sync/StockList')
