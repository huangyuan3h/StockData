import asyncio
import aiohttp

from utils.dateUtils import get_current_timestamp_millisecond
from xueqiu.CookieManager import cookieManager

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
    'Cookie': cookieManager.get_cookies(),
}


async def main(code='SH600519', begin=get_current_timestamp_millisecond(), search_type='before', period='day',
               count='1'):
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        PARAMS.update({'symbol': code, 'begin': begin, 'period': period, 'type': search_type,
                       'count': count})
        async with session.get(URL, params=PARAMS) as resp:
            return await resp.json()


def get_data(code='SH600519', begin=get_current_timestamp_millisecond(), search_type='before', period='day', count='1'):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(main(code, begin, search_type, period, count))


if __name__ == '__main__':
    data = get_data()
    print(data)
