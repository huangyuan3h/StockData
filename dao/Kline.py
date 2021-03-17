from sqlalchemy import Column, String, Integer, DECIMAL, TIMESTAMP

from dao import db


class Kline(db.Model):
    __tablename__ = 'kline'
    id = Column(Integer, primary_key=True)
    code = Column(String(16))
    timestamp = Column(TIMESTAMP)
    volume = Column(Integer) # 成交量
    open = Column(DECIMAL(8, 2)) # 今开
    high = Column(DECIMAL(8, 2)) # 最高
    low = Column(DECIMAL(8, 2)) #最低
    close = Column(DECIMAL(8, 2))  # 今收
    chg = Column(DECIMAL(8, 2)) # 涨跌价
    percent = Column(DECIMAL(8, 2)) # 涨跌价

#     7: "percent"
#     8: "turnoverrate"
#     9: "amount"
#     10: "volume_post"
#     11: "amount_post"
#     12: "pe"
#     13: "pb"
#     14: "ps"
#     15: "pcf"
#     16: "market_capital"
#     17: "balance"
#     18: "hold_volume_cn"
#     19: "hold_ratio_cn"
#     20: "net_volume_cn"
#     21: "hold_volume_hk"
#     22: "hold_ratio_hk"
#     23: "net_volume_hk"
#
#
# 7: 0.99
# 8: 0.25
# 9: 6352656523
# 10: null
# 11: null
# 12: 57.2142
# 13: 17.1808
# 14: 26.8702
# 15: 59.3062
# 16: 2550533765208
# 17: null
# 18: null
# 19: null
# 20: null
# 21: null
# 22: null
# 23: null
