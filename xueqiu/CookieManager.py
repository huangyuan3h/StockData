import requests

from utils.dateUtils import get_current_timestamp_millisecond

'''
get xueqiu cookies
'''

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'sec-ch-ua-mobile': '?0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,zh-CN;q=0.7,zh;q=0.6,ja;q=0.5',
    'Referer': 'https://www.google.com.hk/',
}

url = 'https://xueqiu.com/'

update_gap = 1000 * 60 * 60 * 24  # 1 day


def get_cookie_str():
    res = requests.get(url, headers=headers)
    cookie_str = ''
    for cookie in res.cookies:
        cookie_str += str(cookie.name) + '=' + cookie.value + ';'
    cookie_str = cookie_str[0: len(cookie_str) - 1]
    return cookie_str


class CookieManager(object):
    cookies = ''
    updated_time = None

    def update(self):
        self.cookies = get_cookie_str()
        self.updated_time = get_current_timestamp_millisecond()

    def get_cookies(self):
        if self.cookies == '' or self.updated_time is None or (
            self.updated_time + update_gap) < get_current_timestamp_millisecond():
            self.update()

        return self.cookies


cookieManager = CookieManager()

if __name__ == '__main__':
    print(cookieManager.get_cookies())
