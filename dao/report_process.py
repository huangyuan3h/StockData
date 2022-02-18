from typing import Optional

from pymysql import Date

from dao.model.Report import Report


def get_by_code_type_date(code: str, report_type: str, date: Date) -> Optional[Report]:
    from dao.session_maker import session_maker
    with session_maker() as session:
        return session.query(Report).filter_by(code=code, type=report_type, timestamp=date).first()

