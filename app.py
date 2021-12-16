from dotenv import load_dotenv
from flask import Flask

from api import register_router
from task import taskManager
from dao import dao


# set configuration values
class Config(object):
    SCHEDULER_API_ENABLED = True


load_dotenv()  # loading config
app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    return 'ok'

taskManager.init_app(app)  # start task engine
taskManager.start()

# register sqlalchemy
dao.register(app)  # data access object
register_router(app)  # register API router


if __name__ == '__main__':
    app.run()
