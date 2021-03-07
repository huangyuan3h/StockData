from flask import Flask
from dotenv import load_dotenv

load_dotenv()  # loading config
app = Flask(__name__)

import dao # import the setting

# a simple page that says hello
@app.route('/')
def hello():
    return 'Hello, World!'


from api import sync

app.register_blueprint(sync.bp)

if __name__ == '__main__':
    app.run()
