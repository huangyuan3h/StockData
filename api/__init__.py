# from flask import Flask
# from flask_restful import Api as FlaskApi
#
# from api.GetTasks import GetTasks
# from api.KLineDayDataByStockCode import KLineDayByStockCode
# from api.KlineAllStock import KlineAllStock
# from api.StockList import StockList
# from api.Test import Test

from api.Api import Api

api = Api()

# def register_router(app: Flask):
#     api = FlaskApi(app)
#
#     # tasks manager part
#     api.add_resource(GetTasks, '/tasks')
#     api.add_resource()
#
#     # functional endpoint
#     api.add_resource(StockList, '/sync/StockList')
#     api.add_resource(KLineDayByStockCode, '/sync/KLineDay/<string:code>')
#     api.add_resource(KlineAllStock, '/sync/KLineAllDay')
#     api.add_resource(Test, '/test')
