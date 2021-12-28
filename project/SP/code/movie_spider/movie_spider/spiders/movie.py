import scrapy

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/']

    def parse(self, response):
        print(111111)
