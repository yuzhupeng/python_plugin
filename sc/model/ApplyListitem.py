# -*- coding: utf-8 -*-

import scrapy

class ApplyListitem(scrapy.Item):
    ApplyNo = scrapy.Field() #管理序号
    status = scrapy.Field()  #状态
    applyman = scrapy.Field() #申请人
    applydate = scrapy.Field()#申请人
    completiondate = scrapy.Field() #完成日
    pageno=scrapy.Field() #页码