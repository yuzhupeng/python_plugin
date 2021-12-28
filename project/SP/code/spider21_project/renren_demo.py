from urllib import request, parse
from http.cookiejar import CookieJar

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    # "Cookie": "PHPSESSID=vgvlurg78r2u0k697lulv1s8k7; SECKEY_CID2=99aacab6a22ee558ac38ad354db2e75549bd8f4a; BMAP_SECKEY2=e7ccd76a71cca7384bc9d56993ddbed2e19bbff4744b85e39bb3d65be30e7613e76ae0b8689ae7f5bb14207898aef6950e69432a9314fa542a239fa64bfb5b4545c872d04d41b1ce68e3eb5cc088e4f07e187274f150443d345d7ea0de6d32a46a17861f8b661ba842a25bfbae27cd750b5f5cc6f1242b3ca53362cfa7c1cd032e97db67c256dd3394f7aafc6ce861884436dd733d906a0637bc3be1c87c2c9f0234bf091ccf9a1b18ac47e1a89138f7325902bcbdb9abfb0944357066e37634112bd2193999fa55d12450e73582d54eff95c5578e2c2490621059f4256ee2e994c47b54f8d9ae34944b64488bbc16e8"
}


# url = "http://116.62.25.114:8081/index.php?c=station&a=loadtotal"


def get_opener():
    cookjar = CookieJar()
    handler = request.HTTPCookieProcessor(cookjar)
    opener = request.build_opener(handler)
    return opener


def login_renren(opener):
    data = {"loagin-name": "dengkaifeng", "login-password": "07315369"}
    data = parse.urlencode(data).encode('utf-8')
    login_url = "http://116.62.25.114:8081/index.php?c=login&a=checklogin"
    req = request.Request(url=login_url, headers=headers, data=data)
    opener.open(req)


def visit_profile(opener):
    url = "http://116.62.25.114:8081/index.php?c=station&a=loadtotal"
    req = request.Request(url,headers=headers)
    resp = opener.open(req)
    with open('renren.html', 'wb') as file:
        file.write(resp.read())


if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)
# req = request.Request(url,headers=headers)
# resp = request.urlopen(req)
# with open('renren_nologin.html', 'wb') as file:
#     file.write(resp.read())
