from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor
from pytz import utc

from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from flask_apscheduler import APScheduler

job_stores = {
    'default': MemoryJobStore()
}

executors = {
    'default': ThreadPoolExecutor(20),
    'process_pool': ProcessPoolExecutor(5)
}

job_defaults = {
    'coalesce': False,
    'max_instances': 3
}

_scheduler = BackgroundScheduler(jobstores=job_stores, executors=executors, faults=job_defaults, timezone=utc)

scheduler = APScheduler(scheduler=_scheduler)


def start_task_manager(app: Flask):
    scheduler.init_app(app)
    scheduler.start()
