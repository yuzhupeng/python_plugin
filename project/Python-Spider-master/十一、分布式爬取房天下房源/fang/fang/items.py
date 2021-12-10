# -*- coding: utf-8 -*-

import scrapy

class NewHouseItem(scrapy.Item):
    #省份
    provice = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 小区
    name = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 几句，是个列表
    rooms = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 是否在售
    sale = scrapy.Field()
    # 房天下详情页面的url
    origin_url = scrapy.Field()

class ESFHouseItem(scrapy.Item):
    # 省份
    provice = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 小区名字
    name = scrapy.Field()
    # 几室几厅
    rooms = scrapy.Field()
    # 层
    floor = scrapy.Field()
    # 朝向
    toward = scrapy.Field()
    # 年代
    year = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 建筑面积
    area = scrapy.Field()
    # 总价
    price = scrapy.Field()
    # 单价
    unit = scrapy.Field()
    # 详情页url
    origin_url = scrapy.Field()