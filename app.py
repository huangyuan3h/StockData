from dotenv import load_dotenv
from flask import Flask

from api import api
# from tasks import taskManager
from task_manager import task_manager
from dao import dao
from tasks import loading_tasks


load_dotenv()  # loading config
app = Flask(__name__)

task_manager.initial()
loading_tasks()

# register sqlalchemy
dao.register(app)  # data access object
api.register(app)  # register Api router


if __name__ == '__main__':
    app.run()
