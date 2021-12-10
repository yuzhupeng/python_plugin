
import requests
from lxml import etree

BASE_DOMAIN = 'http://dytt8.net'

HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
}

def get_detail_urls(url):
    '''获取详情页url'''
    response = requests.get(url, headers=HEADERS)
    text = response.text
    html = etree.HTML(text)
    # 获取电影详情的url
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    #加上域名，拼接成完整的url
    detail_urls = map(lambda url:BASE_DOMAIN + url,detail_urls)
    return detail_urls

def parse_detail_page(url):
    '''处理爬取页面'''
    movie = {}
    response= requests.get(url,headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['title'] = title

    zoomE = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoomE.xpath(".//img/@src")
    cover = imgs[0]         #电影海报
    movie['cover'] = cover
    #因为有的电影没有截图，所有这里加个异常处理
    try:
        screenshot = imgs[1]    #电影截图
        movie['screenshot'] = screenshot
    except IndexError:
        pass

    infos = zoomE.xpath(".//text()")
    for index,info in enumerate(infos):
        if info.startswith("◎年　　代"):
            info = info.replace("◎年　　代","").strip()
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = info.replace("◎产　　地", "").strip()
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = info.replace("◎类　　别", "").strip()
            movie['category'] = info
        elif info.startswith("◎豆瓣评分"):
            info = info.replace("◎豆瓣评分", "").strip()
            movie['douban_rating'] = info
        elif info.startswith("◎片　　长"):
            info = info.replace("◎片　　长", "").strip()
            movie['duration'] = info
        elif info.startswith("◎导　　演"):
            info = info.replace("◎导　　演", "").strip()
            movie['director'] = info

        #影片的主演有多个，所有要添加判断
        elif info.startswith("◎主　　演"):
            info = info.replace("◎主　　演", "").strip()
            actors = [info,]
            for x in range(index+1,len(infos)):
                actor = infos[x].strip()
                if actor.startswith("◎简　　介 "):
                    break
                actors.append(actor)
            # print(actors)
            movie['actors'] = actors

        elif info.startswith("◎简　　介 "):
            info = info.replace("◎简　　介 ", "").strip()
            for x in range(index+1,len(infos)):
                profile = infos[x].strip()
                if profile.startswith("【下载地址】"):
                    break
                # print(profile)
                movie['profile'] = profile
    #下载地址
    download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    # print(download_url)
    movie['download_url'] = download_url
    return movie

def spider():
    base_url = 'http://dytt8.net/html/gndy/dyzz/list_23_{}.html'
    movies = []
    for x in range(1,8):    #爬前7页
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            movie = parse_detail_page(detail_url)
            movies.append(movie)
            print(movie)
    print(movies)    #所有的电影信息

if __name__ == '__main__':
    spider()

