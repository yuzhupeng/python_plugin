# -*- coding: utf-8 -*-

import scrapy

class BmxItem(scrapy.Item):
    category = scrapy.Field()
    #保存图片
    image_urls = scrapy.Field()
    images = scrapy.Field()
