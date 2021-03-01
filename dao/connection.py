from sqlalchemy import create_engine
import os

DEFAULT_PARAMETER = {
    'server': 'localhost',
    'port': 3306,
    'user': 'root',
    'pwd': 'root',
    'db': 'stock'
}


def get_engine():
    DEFAULT_PARAMETER.update(
        {
            'server': os.getenv("MYSQL_SERVER"),
            'port': os.getenv("MYSQL_PORT"),
            'user': os.getenv("MYSQL_USERNAME"),
            'pwd': os.getenv("MYSQL_PASSWORD"),
            'db': os.getenv("MYSQL_DB"),
        }
    )

    engine = create_engine('mysql://%(user):%(pwd)@%(server):%(port)/%(db)' % DEFAULT_PARAMETER, echo=True)
    return engine
