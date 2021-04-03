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
    'Cookie': 'device_id=24700f9f1986800ab4fcc880530dd0ed; s=cr11nu60al; xq_a_token=cc6a2aedef8a96868eb7257aef4a2ba6e222d2c6; xqat=cc6a2aedef8a96868eb7257aef4a2ba6e222d2c6; xq_r_token=3e168659e8b7d1863aff7a493cfc3398f438abe3; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTYxOTkyMzQ2NiwiY3RtIjoxNjE3NDY3MjYxOTEyLCJjaWQiOiJkOWQwbjRBWnVwIn0.S9vT0jt0RHkbERoAbXmWNpIdomJjXWQ33zxDzlpRwNfc2xytVhMhX7w7Qph5D_AYu-TjsNSIwdOOkD20u-CWZzF8ttI3gmf4lc84Oj03o1tRXlcSoRC4JPX5j23e1NWX0PaHUzHA0LixKsTDz5C-UF0scrfls385bx3sctgrN7r0k3iMuKjltVEtJ_jWZnCHg2RzCePp2bcl7dRzGfUWkdFwJNmkrMwkgJjIxqi4F4tmikU76PLlMW9AlEOSFnJ81TzQaDFZ_HrMOVbi2tGs_TgH_8-UXAO03rNz2yEKR0wrnSHCJ89GTxMH0jHUWsat6wLZDJJt1i_oXrSa_OAahA; u=331617467262469; Hm_lvt_1db88642e346389874251b5a1eded6e3=1615723328,1617033253,1617467266; is_overseas=1; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1617467272',
}


def get_data(code='SH600519', begin=get_current_timestamp_millisecond(), search_type='before', period='day', count='1'):
    PARAMS.update({'symbol': code, 'begin': begin, 'period': period, 'type': search_type,
                   'count': count})
    r = requests.get(url=URL, params=PARAMS, headers=HEADERS)
    return r.json()


if __name__ == '__main__':
    data = get_data()
    print(data)
