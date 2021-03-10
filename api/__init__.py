from flask import Flask

from api import sync, task


def register(app: Flask):
    app.register_blueprint(sync.bp)
    app.register_blueprint(task.bp)
