import scrapy
from JD.items import JdItem

# 1，导入分布式爬虫类
from scrapy_redis.spiders import RedisSpider


class BookSpider(RedisSpider):
    name = 'book'
    # allowed_domains = ['lingyun.tv']
    # start_urls = ['https://www.lingyun.tv/channel/movie.html']

    # 设置redis_key
    redis_key = 'movie1'

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_damains = list(filter(None, domain.split(",")))
        super(BookSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        # 获取所有图书大分类
        big_node_list = response.xpath('/html/body/div[2]/div[1]/dl/dt')
        for big_node in big_node_list[:1]:
            item = JdItem()
            item["big_category_name"] = big_node.xpath("./text()").extract_first()
            small_node_list = big_node.xpath("./following-sibling::a")
            for small_node in small_node_list:
                item["small_category_name"] = small_node.xpath("./text()").extract_first()
                item["small_category_link"] = response.urljoin(small_node.xpath("./@href").extract_first())
                yield scrapy.Request(
                    url=item["small_category_link"],
                    callback=self.parse_list,
                    meta={'item': item}
                )

    def parse_list(self, response):
        item = response.meta["item"]
        movie_list = response.xpath('/html/body/div[2]/ul/li')
        for movie in movie_list:
            item["movie_name"] = movie.xpath('./div[2]/h3/a/text()').extract_first()
            item["movie_score"] = movie.xpath('./div[2]/h3/span/text()').extract_first()
            item["movie_tag"] = movie.xpath('./div[2]/div/text()').extract_first()
            item["movie_pic"] = response.urljoin(movie.xpath('./div[1]/a/img/@data-funlazy').extract_first())
            item["movie_detail_link"] = response.urljoin(movie.xpath('./div[1]/a/@href').extract_first())
            item["movie_view_counts"] = movie.xpath('./div[1]/a/span/span[1]/text()').extract_first()
            item["movie_definition"] = movie.xpath('./div[1]/a/span/span[2]/text()').extract_first()
            yield scrapy.Request(
                url=item["movie_detail_link"],
                callback=self.parse_detail,
                meta={'item': item}
            )


    def parse_detail(self, response):
        item = response.meta["item"]
        item["movie_director"] = response.xpath('/html/body/div[2]/div[1]/div/div[1]/div[2]/div[2]/a/text()').extract_first()
        yield item
        # yield scrapy.Request(
        #     url=item["small_category_link"],
        #     callback=self.parse_detail,
        #     meta={'item': item}
        # )