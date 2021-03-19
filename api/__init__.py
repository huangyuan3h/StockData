from flask import Flask
from flask_restful import Api
from api.StockList import StockList
from api.Test import Test


def register_router(app: Flask):
    api = Api(app)
    api.add_resource(StockList, '/sync/StockList')
    api.add_resource(Test, '/test')
