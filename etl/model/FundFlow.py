from sqlalchemy import Column, String, Integer, TIMESTAMP, DECIMAL
import decimal

from etl.model import Base


class FundFlow(Base):
    __tablename__ = 'fund_flow'
    id = Column(Integer, primary_key=True)
    code = Column(String(16))
    timestamp = Column(TIMESTAMP)
    main_percent = Column(DECIMAL(16, 2))  # 主力净流入比例
    huge_percent = Column(DECIMAL(16, 2))  # 超大单净流入比例
    large_percent = Column(DECIMAL(16, 2))  # 大单净流入比例
    middle_percent = Column(DECIMAL(16, 2))  # 中单净流入比例
    small_percent = Column(DECIMAL(16, 2))  # 小单净流入比例

    def __repr__(self):
        return "<FundFlow(id='%d', code='%s', timestamp='%s')>" % (self.id, self.code, str(self.timestamp))

    def as_dict(self):
        def get_value(v: any):
            if isinstance(v, decimal.Decimal):
                return float(v)
            else:
                return v

        return {c.name: get_value(getattr(self, c.name)) for c in self.__table__.columns}
