# -*- coding: utf-8 -*-
import scrapy
from bmx.items import BmxItem

class Bmx5Spider(scrapy.Spider):
    name = 'bmx5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/159.html']

    def parse(self, response):
        uiboxs = response.xpath("//div[@class='uibox']")[1:]
        for uibox in uiboxs:
            category = uibox.xpath(".//div[@class='uibox-title']/a/text()").get()
            urls = uibox.xpath(".//ul/li/a/img/@src").getall()
            # for url in urls:
            #     url = "https:" + url
            #     print(url)
            urls = list(map(lambda url:response.urljoin(url),urls))
            items = BmxItem(category=category,image_urls=urls)
            yield items