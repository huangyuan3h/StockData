import requests

from utils.dateUtils import get_current_timestamp_millisecond

URL = 'https://stock.xueqiu.com/v5/stock/chart/kline.json'

period_type = {'5mins': '5m', '1day': 'day'}

PARAMS = {
    'symbol': 'SH600519',  # stock code
    'begin': 1615388346474,  # timestamp
    'period': 'day',  # '1m',
    'type': 'before',  #
    'count': '-1',
    'indicator': 'kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance'
}

HEADERS = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Cookie': 'device_id=24700f9f1986800ab4fcc880530dd0ed; s=cr11nu60al; xq_a_token=a4b3e3e158cfe9745b677915691ecd794b4bf2f9; xqat=a4b3e3e158cfe9745b677915691ecd794b4bf2f9; xq_r_token=b80d3232bf315f8710d36ad2370bc777b24d5001; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTYxNzc2MzQxOCwiY3RtIjoxNjE1NzIzMjkyNTU0LCJjaWQiOiJkOWQwbjRBWnVwIn0.lIXUujg17WETI909RwWpD0lXYbHR-vfM-SrVhaefRiOKNJbnfszOYjGJmIgsjl93FWw_l6OjEI6JcTVtVh370bTjNTMxUPxPQ0kDRfdbd_X8T8NZGDDRe6L0e59Hazbohz_dktSen7BWHnytJqlIRkV3594oY8UVc4FS6Z10_a9v0xQ5fa8nsfQSabmJWocG3VB6UiUr_sj2kn_s3A1MDOTEcvXjWEo7CV_olALDi7xwY1_N8IRsntSer556dy-huGF5ueItvVnrLB1eUsUxr6ToUZISECHJ021N7c5foEaO0KAzCXBTlV_1IndNdOMkgXNNRUCVRvjcPzsw0W-GpQ; u=771615723327105; Hm_lvt_1db88642e346389874251b5a1eded6e3=1614605844,1614613218,1615723328,1617033253; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1617034824',
}


def get_data(code='SH600519', begin=get_current_timestamp_millisecond(), search_type='before', period='day', count='1'):
    PARAMS.update({'symbol': code, 'begin': begin, 'period': period, 'type': search_type,
                   'count': count})
    r = requests.get(url=URL, params=PARAMS, headers=HEADERS)
    return r.json()


if __name__ == '__main__':
    data = get_data()
    print(data)
