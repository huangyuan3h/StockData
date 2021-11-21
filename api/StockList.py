from flask_restful import Resource

from api.Response_Code import OK


'''
sync all stock data
'''


class StockList(Resource):

    def get(self):
        return OK

