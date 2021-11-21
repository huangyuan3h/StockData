from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from flask_apscheduler import APScheduler
from pytz import utc


class TaskManager(object):
    job_stores = {
        'default': MemoryJobStore()
    }

    executors = {
        'default': ThreadPoolExecutor(90),  # max threads: 90
        'processpool': ProcessPoolExecutor(20)  # max processes 20
    }

    job_defaults = {
        'coalesce': False,
        'max_instances': 3
    }

    _scheduler = None  # scheduler
    scheduler = None  # apscheduler_flask

    def __init__(self):
        if self._scheduler is None:
            self._scheduler = BackgroundScheduler(jobstores=self.job_stores, executors=self.executors,
                                                  faults=self.job_defaults,
                                                  timezone=utc)
            self.scheduler = APScheduler()

    def init_app(self, app):
        self.scheduler.init_app(app)

    def start(self):
        self.scheduler.start()

    def add_job(self, *args, **kwargs):
        self.scheduler.add_job(*args, **kwargs)

    def shutdown(self):
        self.scheduler.shutdown()

    def get_jobs(self):
        self.scheduler.get_jobs()
