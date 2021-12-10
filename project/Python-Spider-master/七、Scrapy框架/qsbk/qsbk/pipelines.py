# -*- coding: utf-8 -*-

import json

#1.手动把dick转换成json格式

# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open('duanzi.json','w',encoding='utf-8')
#
#     def open_spider(self,spider):
#         print('开始爬虫')
#
#     def process_item(self, item, spider):
#         item_json = json.dumps(dict(item),ensure_ascii=False)
#         self.fp.write(item_json+'\n')
#         return item
#
#     def close_spider(self,spider):
#         self.fp.close()
#         print('爬虫结束了')

#2.适用JsonItemExporter，使用与数据量小的情况下
# from scrapy.exporters import JsonItemExporter
# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open('duanzi.json','wb')
#         self.exporter = JsonItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
#         self.exporter.start_exporting()
#
#     def open_spider(self,spider):
#         print('开始爬虫')
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self,spider):
#         self.exporter.finish_exporting()
#         self.fp.close()
#         print('爬虫结束了')


#3.JsonLinesItemExporter，适用与数据量大的情况下
from scrapy.exporters import JsonLinesItemExporter
class QsbkPipeline(object):
    def __init__(self):
        self.fp = open('duanzi.json','wb')
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')

    def open_spider(self,spider):
        print('开始爬虫')

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.fp.close()
        print('爬虫结束了')