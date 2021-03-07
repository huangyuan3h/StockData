
from sqlalchemy.orm import sessionmaker

from dao.connection import Connection


class Session():
    _engine = None
    _sessionTemplate = None

    def _init_session(self):
        self._engine = Connection.get_engine()
        self._sessionTemplate = sessionmaker(bind=self._engine)

    def get_session(self):
        if self._sessionTemplate is None:
            self._init_session()
        return self._sessionTemplate()
