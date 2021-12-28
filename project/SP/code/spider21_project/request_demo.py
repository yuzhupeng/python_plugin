import requests
from lxml import etree


# 请求头
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    'Referer': 'https://movie.douban.com/'
}

# url
url = 'https://movie.douban.com/cinema/nowplaying/changsha/'

resp = requests.get(url, headers=headers)
# with open('douban.html', 'wb') as file:
#     file.write(resp.content)

html = etree.HTML(resp.content.decode())
ul = html.xpath('//*[@id="nowplaying"]/div[2]/ul')[0]
movie_list = []
for li in ul:
    title = li.xpath('./@data-title')[0]
    score = li.xpath('./@data-score')[0]
    duration = li.xpath('./@data-duration')[0]
    psource = li.xpath('.//img/@src')[0]
    movie_dict = {
        "title": title,
        "score": score,
        "duration": duration,
        "psource": psource,
    }
    movie_list.append(movie_dict)
print(movie_list)