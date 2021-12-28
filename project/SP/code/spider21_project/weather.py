import requests
from lxml import etree


# 请求头
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    'Referer': 'https://movie.douban.com/'
}

# url
urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        # 'http://www.weather.com.cn/textFC/gat.shtml'
    ]
city_list = []
for link in urls:
    resp = requests.get(link, headers=headers)
    html = etree.HTML(resp.content.decode())
    tbody = html.xpath('//*[@class="hanml"]/div')[0]
    for div in tbody:
        city_list = div.xpath('./table')[0]
        for index, tr in enumerate(city_list):
            if index >= 2:
                try:
                    province = tr.xpath('./td[@width=74]//a/text()')[0]
                except IndexError as e:
                    pass
                city = tr.xpath('./td[@width=83]/a/text()')[0]
                max_temper = tr.xpath('./td[@width=92]/text()')[0]
                min_temper = tr.xpath('./td[@width=86]/text()')[0]
                print(province, city, max_temper, min_temper)

# with open('douban.html', 'wb') as file:
#     file.write(resp.content)