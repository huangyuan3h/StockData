from flask import Flask
from flask_restful import Api as FlaskApi
from importlib import import_module


class Api(object):
    app: Flask = None

    api: FlaskApi = None

    def register(self, app: Flask):
        self.app = app
        self.api = FlaskApi(app)
        import_module('api.GetTasks')

    def get_flask_api(self):
        return self.api

    def route(self, *urls, **kwargs):
        return self.api.resource(*urls, **kwargs)
