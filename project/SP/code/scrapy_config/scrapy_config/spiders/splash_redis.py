import scrapy


class SplashRedisSpider(scrapy.Spider):
    name = 'splash_redis'
    allowed_domains = ['baidu.com']
    start_urls = ['http://itcast.cn/']

    def parse(self, response):
        pass
