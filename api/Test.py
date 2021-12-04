from flask_restful import Resource
from api.Response_Code import OK
from task_manager import task_manager
from tasks.sync_kline_day_all import run


@task_manager.celery.task()
def add_together(a, b):
    return a + b




class Test(Resource):
    def get(self):
        result = add_together.delay(23, 42)
        result.get(timeout=1000)
        print(result)
        return OK
