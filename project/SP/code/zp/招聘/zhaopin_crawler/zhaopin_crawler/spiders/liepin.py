# -*- coding: utf-8 -*-

import re
import langid
import scrapy
from pathlib import Path
from urllib.parse import quote
from scrapy.exceptions import CloseSpider
from zhaopin_crawler import settings
from zhaopin_crawler.utils.log import Logger
from zhaopin_crawler.items import ZhaopinCrawlerItem
from zhaopin_crawler.utils.tools import get_time_stamp, get_html, get_content_raw, get_xpath_info


class LiepinSpider(scrapy.Spider):
    name = "liepin"
    allowed_domains = ["liepin.com"]
    start_urls = ["http://liepin.com/"]

    # 基础 url 地址
    BASE_URL = "https://www.liepin.com/zhaopin/?key={key_word}"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spider_log = Logger(Path(settings.LOG_PATH, f"{self.name}.log")).logger

    def start_requests(self):
        for key_word in settings.CRAWLER_KEY_WORD_LIST:
            start_url = self.BASE_URL.format(key_word=quote(key_word))
            self.spider_log.info(f"请求列表页：{start_url}")
            yield scrapy.Request(
                url=start_url,
                headers={"Referer": "https://www.liepin.com/"},
                callback=self.parse,
                meta={"key_word": key_word}
            )

    def parse(self, response):
        """ 解析列表页 """
        self.spider_log.info(f"解析列表页：{response.url}")
        job_list = response.xpath('//ul[@class="sojob-list"]/li')
        if len(job_list) == 0:
            self.spider_log.warning(f"WARRING: 列表页 [{response.url}] 招聘数据量为 0。")
            self.spider_log.warning("↓" * 33)
            self.spider_log.warning(f"\n{response.text}")
            self.spider_log.warning("↑" * 33)
            raise CloseSpider('bandwidth_exceeded')
        self.spider_log.info(f"检索到招聘信息：{len(job_list)} 条")
        for index, job in enumerate(job_list):
            job_base_url = job.xpath('.//h3/a/@href').get()
            job_data_promid = job.xpath('.//h3/a/@data-promid').get()
            job_url = f"{job_base_url}?{job_data_promid}" if job_data_promid else job_base_url
            if job_url:
                yield scrapy.Request(
                    url=response.urljoin(job_url),
                    headers={"Referer": response.url},
                    callback=self.parse_detail,
                    meta={"dont_redirect": True, "key_word": response.meta["key_word"]}
                )

        # next_path = response.xpath('//*[contains(text(),"下一页")]/@href').get()
        # if next_path:
        #     yield scrapy.Request(
        #         url=response.urljoin(next_path),
        #         headers=self.BASE_HEADERS,
        #         callback=self.parse,
        #         meta={"key_word": response.meta["key_word"]}
        #     )

    def parse_detail(self, response):
        """ 解析详情页 """
        item = ZhaopinCrawlerItem()
        title = get_xpath_info(response, '//title')

        if "_猎头顾问招聘信息" in title:
            # 猎头顾问招聘详情页
            item["job_salary"] = get_xpath_info(response, '//p[@class="job-main-title"]')
            item["job_education"] = get_xpath_info(response, '//div[starts-with(@class,"resume")]/span[1]')
            item["job_experience"] = get_xpath_info(response, '//div[starts-with(@class,"resume")]/span[2]')
            item["job_recruiter"] = get_xpath_info(response, '//p[@class="hunter-name"]/span')
            __job_recruiter_position = get_xpath_info(response, '//p[@class="hunter-name"]')
            item["job_recruiter_position"] = "/".join(
                [job for job in __job_recruiter_position.split("/") if job.strip()]).strip()
            item["company_name"] = get_xpath_info(response, '//p[@class="company-name"]/@title')
        else:
            # 企业招聘详情页
            item["job_salary"] = get_xpath_info(response, '//p[@class="job-item-title"]')
            item["job_education"] = get_xpath_info(response, '//div[@class="job-qualifications"]/span[1]')
            item["job_experience"] = get_xpath_info(response, '//div[@class="job-qualifications"]/span[2]')
            item["job_recruiter"] = get_xpath_info(response, '//p[@class="publisher-name"]/span')
            __job_recruiter_position = get_xpath_info(response, '//p[@class="publisher-name"]/em')
            item["job_recruiter_position"] = __job_recruiter_position.replace("/", "").strip()
            item["job_recruiter_position"] = "/".join(
                [job for job in __job_recruiter_position.split("/") if job.strip()]).strip()
            item["company_name"] = get_xpath_info(response, '//div[@class="company-logo"]/p/a')

        item["publish_time"] = get_time_stamp(response.xpath('string(.)').re_first('"pubDate":\s"(.*?)"'))
        item["url"] = response.url
        item["site_id"] = ""  # TODO: 网站 ID  待处理
        item["site_name"] = ""  # TODO: 网站名称  待处理
        item["job_name"] = get_xpath_info(response, '//h1')
        item["job_number"] = ""
        item["job_date_range"] = ""
        job_description_xpath = '//div[contains(@class,"job-description")]/div[contains(@class,"content-word")]'
        item["job_description"] = get_xpath_info(response, job_description_xpath, js_decode=True)
        item["job_description_raw"] = get_content_raw(get_html(response), job_description_xpath)
        item["job_department"] = ""
        item["job_address"] = get_xpath_info(response, '//p[@class="basic-infor"]')
        item["job_advantage"] = get_xpath_info(response, '//ul[@data-selector="comp-tag-list"]//span')
        __lang = str(langid.classify(item["job_description"])[0]).lower() if item["job_description"] else ""
        item["lang"] = __lang.split("-")[0] if "-" in __lang else __lang  # zh-xxxx 取 zh
        item["company_home_url"] = ""
        item["company_logo"] = get_xpath_info(response, '//div[@class="company-logo"]/a/img/@src')
        __company_industry = response.xpath('string(//ul[@class="new-compintro"])').re_first("行业：(.*)")
        item["company_industry"] = __company_industry.strip() if __company_industry else ""
        __company_development_stage = response.xpath('string(//ul[@class="new-compintro"])').re_first("融资：(.*)")
        item["company_development_stage"] = __company_development_stage.strip() if __company_development_stage else ""
        __company_scale = response.xpath('string(//ul[@class="new-compintro"])').re_first("公司规模：(.*)")
        item["company_scale"] = __company_scale.strip() if __company_scale else ""
        item["company_description"] = get_xpath_info(response, '//div[@class="info-word"]')
        item["company_business_info"] = ""
        item["extra_info"] = ""
        self.spider_log.info(item)
        yield item
