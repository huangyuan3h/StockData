from flask_restful import Resource

from api.Response_Code import OK

'''
sync day kline data
'''


class KLineDay(Resource):
    def get(self):
        return OK
