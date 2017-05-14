# -*- coding: utf-8 -*-


COOKIE_FILE = "/Users/ray/Desktop/cookies.txt"
URL = "https://www.zhihu.com/"
DEFAULT_HEADERS = {
    "Content-type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Connection": "keep-alive",
    'Accept-Encoding': 'gzip',
}


def modify_cookies(filename):
    import time
    cookies = []
    with open(filename, 'r') as f:
        for cookie in f.readlines():
            cookie_splited = cookie.split("\t")
            if len(cookie_splited) == 6:
                cookie_splited.insert(4, str(int(time.time())))
                cookie = "\t".join(cookie_splited)
            cookies.append(cookie)
    with open(filename, 'w') as f:
        f.write("# Netscape HTTP Cookie File\n")
        f.write("".join(cookies))


def read_cookies(filename):
    import os
    import http.cookiejar
    cookies = http.cookiejar.MozillaCookieJar(filename=filename)
    if os.path.exists(filename):
        cookies.load()
        return cookies
    else:
        return


def unfold_cookies(cookie_jar):
    cookies_ = cookie_jar._cookies
    cookies = []
    for domain in cookies_:
        for path in cookies_[domain]:
            for cookie in cookies_[domain][path]:
                cookie = cookies_[domain][path][cookie].__dict__
                cookies.append(cookie)
    return cookies


def get_html_with_requests():
    import requests
    url = URL
    session = requests.session()
    session.cookies = read_cookies(filename=COOKIE_FILE)
    session.headers = DEFAULT_HEADERS
    return session.get(url)


def get_username(html_string):
    import re
    pattern = re.compile(r'(?<=<span class="name">)(.+)(?=</span>)')
    return re.findall(pattern, html_string)[0]


if __name__ == "__main__":
    modify_cookies(COOKIE_FILE)
    print(unfold_cookies(read_cookies(COOKIE_FILE)))
    print("你的昵称：{username}".format(username=get_username(get_html_with_requests().text)))