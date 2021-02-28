from sqlalchemy import create_engine


def get_engine():
    engine = create_engine('mysql://root:root@localhost:3306/stock', echo=True)
    return engine
