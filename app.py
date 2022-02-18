from dotenv import load_dotenv
from flask import Flask

from api import register_router
from dao import dao
from task_manager import task_manager


# set configuration values
class Config(object):
    SCHEDULER_API_ENABLED = True


load_dotenv()  # loading config
app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return 'ok'


task_manager.initial(app)
celery = task_manager.celery

# register sqlalchemy
dao.register()  # data access object
register_router(app)  # register API router

if __name__ == '__main__':
    app.run()
