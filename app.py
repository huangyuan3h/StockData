from flask import Flask
from sqlalchemy import create_engine
app = Flask(__name__)


@app.route('/')
def hello():
    engine = create_engine('sqlite:///:memory:', echo=True)
    return "Hello World!"

if __name__ == '__main__':
    app.run()
