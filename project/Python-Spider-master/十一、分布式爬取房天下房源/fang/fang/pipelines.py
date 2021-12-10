# -*- coding: utf-8 -*-

from scrapy.exporters import JsonLinesItemExporter

class FangPipeline(object):
    def __init__(self):
        self.newhouse_fp = open('newhouse.json','wb')
        self.esfhouse_fp = open('esfhouse.json','wb')
        self.newhouse_exporter = JsonLinesItemExporter(self.newhouse_fp,ensure_ascii=False)
        self.esfhouse_exporter = JsonLinesItemExporter(self.esfhouse_fp,ensure_ascii=False)

    def process_item(self, item, spider):
        self.newhouse_exporter.export_item(item)
        self.esfhouse_exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.newhouse_fp.close()
        self.esfhouse_fp.close()