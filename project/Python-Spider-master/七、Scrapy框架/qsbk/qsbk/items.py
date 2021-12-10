
import scrapy

class QsbkItem(scrapy.Item):
    author = scrapy.Field()
    content = scrapy.Field()
