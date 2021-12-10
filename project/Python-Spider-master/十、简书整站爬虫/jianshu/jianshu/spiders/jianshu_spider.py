# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import JianshuItem

class JianshuSpiderSpider(CrawlSpider):
    name = 'jianshu_spider'
    allowed_domains = ['jianshu.com']
    start_urls = ['http://jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z][12].*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='title']/text()").get()
        avatar = response.xpath("//a[@class='avatar']/img/@src").get()
        author = response.xpath("//span[@class='name']/a/text()").get()
        pub_time = response.xpath("//span[@class='publish-time']/text()").get().replace("*","")
        #获取文章id
        url = response.url
        url1 = url.split("?")[0]
        article_id = url1.split("/")[-1]
        #文章内容，包括标签，而不是存文本内容
        content = response.xpath("//div[@class='show-content']").get()
        # word_count = response.xpath("//span[@class='wordage']/text()").get()
        # comment_count = response.xpath("//span[@class='comments-count']/text()").get()
        # read_count = response.xpath("//span[@class='views-count']/text()").get()
        # like_count = response.xpath("//span[@class='likes-count']/text()").get()
        # subjects = ",".join(response.xpath("//div[@class='include-collection']/a/div/text()").getall())

        item = JianshuItem(
            title=title,
            avatar=avatar,
            pub_time=pub_time,
            author=author,
            origin_url=response.url,
            content=content,
            article_id=article_id,
            # subjects=subjects,
            # word_count=word_count,
            # comment_count=comment_count,
            # like_count=like_count,
            # read_count=read_count
        )
        yield item