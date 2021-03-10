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

register(app)
start(app)

if __name__ == '__main__':
    app.run()
