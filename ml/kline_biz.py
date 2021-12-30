import app


from dao.kline_process import get_kline_by_code
from dao.mapping.kline_mapping import kline_obj_2_dataframe


def kline_process():
    result = get_kline_by_code('SZ002639')
    df = kline_obj_2_dataframe(result)
    print(df.info())



if __name__ == '__main__':
    kline_process()
