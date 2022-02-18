import decimal


class DictMixIn:

    def as_dict(self):
        def get_value(v: any):
            if isinstance(v, decimal.Decimal):
                return float(v)
            else:
                return v

        return {c.name: get_value(getattr(self, c.name)) for c in self.__table__.columns}
