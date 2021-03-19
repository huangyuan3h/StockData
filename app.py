from dotenv import load_dotenv
from flask import Flask

from api import register_router
from scheduler import start_task_manager
from dao import dao


# set configuration values
class Config(object):
    SCHEDULER_API_ENABLED = True


load_dotenv()  # loading config
app = Flask(__name__)
app.config.from_object(Config())

# register sqlalchemy
dao.register(app)  # data access object
register_router(app)  # register API router
start_task_manager(app)  # start task engine

if __name__ == '__main__':
    app.run()
