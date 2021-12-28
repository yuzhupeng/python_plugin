# coding=utf-8
import time

from selenium import webdriver
from lxml import etree
import json


class LagouSpider(object):
    driver_path = r'E:\ChromeDriver\chromedriver.exe'

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = 'https://www.lagou.com/wn/jobs?px=new&pn=1&kd=Python&city=%E9%95%BF%E6%B2%99'

    def run(self):
        self.driver.get(self.url)
        source = self.driver.page_source
        # print(source)
        self.parse_list_page(source)

    def parse_list_page(self, source):
        html = etree.HTML(source)
        links = str(html.xpath('//*[@id="__NEXT_DATA__"]/text()')[0])
        json_dict = json.loads(links)
        result_list = json_dict["props"]["pageProps"]["initData"]["content"]["positionResult"]["result"]
        for result in result_list:
            params = {}
            params["positionId"] = result["positionId"]
            params["positionName"] = result["positionName"]
            params["companyFullName"] = result["companyFullName"]
            params["companyShortName"] = result["companyShortName"]
            params["companySize"] = result["companySize"]
            params["salary"] = result["salary"]
            params["workYear"] = result["workYear"]
            params["positionAdvantage"] = result["positionAdvantage"]
            params["link"] = 'https://www.lagou.com/wn/jobs/%s.html' % params["positionId"]
            self.request_detail_page(url=params["link"], params=params)
            time.sleep(3)

    def request_detail_page(self, url, params):
        self.driver.get(url)
        source = self.driver.page_source
        print(source)
        print('='*40)


if __name__ == '__main__':
    LagouSpider().run()