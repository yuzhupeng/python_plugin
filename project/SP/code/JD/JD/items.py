# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    # define the fields for your item here like:
    # 大分类
    big_category_name = scrapy.Field()
    # 小分类
    small_category_name = scrapy.Field()
    # 小分类链接
    small_category_link = scrapy.Field()
    # 电影名
    movie_name = scrapy.Field()
    # 电影评分
    movie_score = scrapy.Field()
    # 电影标签
    movie_tag = scrapy.Field()
    # 电影封面图片
    movie_pic = scrapy.Field()
    # 电影详情链接
    movie_detail_link = scrapy.Field()
    # 电影播放量
    movie_view_counts = scrapy.Field()
    # 电影清晰度
    movie_definition = scrapy.Field()
    # 电影导演
    movie_director = scrapy.Field()




