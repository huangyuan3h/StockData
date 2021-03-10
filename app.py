from flask import Flask
from dotenv import load_dotenv
from scheduler import start


# set configuration values
class Config(object):
    SCHEDULER_API_ENABLED = True


load_dotenv()  # loading config
app = Flask(__name__)
app.config.from_object(Config())
start(app)

import dao  # import the setting


# a simple page that says hello
@app.route('/')
def hello():
    return 'Hello, World!'


from api import sync

app.register_blueprint(sync.bp)

if __name__ == '__main__':
    app.run()
