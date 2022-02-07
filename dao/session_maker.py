from contextlib import contextmanager

from dao import dao


@contextmanager
def session_maker(session=dao.session):
    try:
        yield session
        session.commit()
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        session.rollback()
        raise
    finally:
        session.close()
