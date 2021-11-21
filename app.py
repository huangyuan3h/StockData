from dotenv import load_dotenv
from flask import Flask

from api import register_router
# from tasks import taskManager
from task_manager import task_manager
from dao import dao


# set configuration values
class Config(object):
    SCHEDULER_API_ENABLED = True


load_dotenv()  # loading config
app = Flask(__name__)
app.config.from_object(Config())

# remove asp schedul but add customer
# taskManager.init_app(app)  # start tasks engine
# taskManager.start()
task_manager.initial()
# register sqlalchemy
dao.register(app)  # data access object
register_router(app)  # register API router


if __name__ == '__main__':
    app.run()
