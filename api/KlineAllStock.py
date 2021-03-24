from flask_restful import Resource

from api.Response_Code import OK


class KlineAllStock(Resource):
    def get(self):
        return OK
