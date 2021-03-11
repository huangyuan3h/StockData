from dotenv import load_dotenv
from flask import Flask

from api import register
from scheduler import start


# set configuration values
class Config(object):
    SCHEDULER_API_ENABLED = True


load_dotenv()  # loading config
app = Flask(__name__)
app.config.from_object(Config())

# register sqlalchemy
import dao
register(app)  # register API router
start(app)  # start task engine

if __name__ == '__main__':
    app.run()
