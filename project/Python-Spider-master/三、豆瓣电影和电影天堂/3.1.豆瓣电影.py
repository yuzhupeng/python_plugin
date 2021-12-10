
import requests
from lxml import etree

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
    'Referer':'https://movie.douban.com/'
}
url = 'https://movie.douban.com/cinema/nowplaying/beijing/'
response = requests.get(url,headers=headers)
text = response.text

html = etree.HTML(text)
#获取正在上映的电影
ul = html.xpath("//ul[@class='lists']")[0]
lis = ul.xpath("./li")
movies = []

for li in lis:
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    duration = li.xpath("@data-duration")[0]
    region = li.xpath("@data-region")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    #电影海报图片
    thumbnail = li.xpath(".//img/@src")[0]

    movie = {
        'title':title,
        'score':score,
        'duration':duration,
        'region':region,
        'director':director,
        'actors':actors,
        'thumbnail':thumbnail,
    }
    movies.append(movie)

print(movies)