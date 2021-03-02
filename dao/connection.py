from sqlalchemy import create_engine
import os

DEFAULT_PARAMETER = {
    'server': 'localhost',
    'port': '3306',
    'user': 'root',
    'pwd': 'root',
    'db': 'stock'
}


def get_engine():
    env_parameter = {
        'server': os.getenv("MYSQL_SERVER"),
        'port': os.getenv("MYSQL_PORT"),
        'user': os.getenv("MYSQL_USERNAME"),
        'pwd': os.getenv("MYSQL_PASSWORD"),
        'db': os.getenv("MYSQL_DB"),
    }

    filter_env = {k: v for k, v in env_parameter.items() if v is not None}

    DEFAULT_PARAMETER.update(filter_env)
    engine = create_engine('mysql+pymysql://%(user)s:%(pwd)s@%(server)s:%(port)s/%(db)s' % DEFAULT_PARAMETER, echo=True)
    return engine
