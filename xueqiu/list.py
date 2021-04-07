import requests

from xueqiu.CookieManager import cookieManager

URL = 'https://xueqiu.com/service/v5/stock/screener/quote/list'

PARAMS = {
    'market': 'CN',
    'order_by': 'symbol',
    'type': 'sh_sz',
    'orderby': 'code',
    'order': 'asc',
    'page': '1',
    'size': '30'
}

HEADERS = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'Accept': '*/*',
    'cache-control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://xueqiu.com/hq',
    'Cookie': cookieManager.get_cookies(),
}


def get_list(page=1, size=30):
    PARAMS.update({'page': page, 'size': size})
    r = requests.get(url=URL, params=PARAMS, headers=HEADERS)
    return r.json()


if __name__ == '__main__':
    data = get_list(2)
    print(data)
