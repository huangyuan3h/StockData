from flask import Flask
from flask_apscheduler import APScheduler

scheduler = APScheduler()


def start(app: Flask):
    scheduler.init_app(app)
    scheduler.start()
