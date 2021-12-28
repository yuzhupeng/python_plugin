import scrapy


class NoSplashSpider(scrapy.Spider):
    name = 'no_splash'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/s?wd=python']

    def parse(self, response):
        with open('no_splash.html', 'w') as f:
            f.write(response.body.decode('gbk', 'ignore'))
