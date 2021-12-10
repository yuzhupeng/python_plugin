
import scrapy

class JianshuItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    article_id = scrapy.Field()
    origin_url = scrapy.Field()
    author = scrapy.Field()
    avatar = scrapy.Field()
    pub_time = scrapy.Field()
    # read_count = scrapy.Field()
    # like_count = scrapy.Field()
    # word_count = scrapy.Field()
    # subjects = scrapy.Field()
    # comment_count = scrapy.Field()
