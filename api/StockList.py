import datetime
from flask_restful import Resource
from scheduler import scheduler, sync_list


class StockList(Resource):
    def get(self):
        scheduler.add_job(func=sync_list.run, id='sync_list_' + str(datetime.datetime.now())
                          , next_run_time=datetime.datetime.now())
        return {'hello': 'world'}
