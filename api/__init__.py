from flask import Flask
from flask_restful import Api

from api.KLineDayDataByStockCode import KLineDayByStockCode
from api.KlineAllStock import KlineAllStock
from api.StockList import StockList
from api.Test import Test


def register_router(app: Flask):
    api = Api(app)
    api.add_resource(StockList, '/sync/StockList')
    api.add_resource(KLineDayByStockCode, '/sync/KLineDay/<string:code>')
    api.add_resource(KlineAllStock, '/sync/KLineAllDay')
    api.add_resource(Test, '/test')
