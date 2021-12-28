# coding=utf-8
import time

import requests
from selenium import webdriver
from lxml import etree

import proxy_option
from proxy_request import kd_request


class LagouSpider(object):
    driver_path = r'E:\ChromeDriver\chromedriver.exe'

    def __init__(self, proxy=None):
        options = webdriver.ChromeOptions()
        options.add_argument(proxy)
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path, options=options)
        self.url = 'https://www.zhipin.com/c101250100-p100109/?'

    def run(self):
        for i in range(1, 10):
            url = self.url + 'page=%d&ka=page-%d' % (i, i)
            try:
                self.driver.get(url)
            except Exception as e:
                print(e.args[0])
                return
            time.sleep(3)
            source = self.driver.page_source
            result = self.parse_list_page(source)
            if result == 0:
                break


    def parse_list_page(self, source):
        html = etree.HTML(source)
        try:
            ul_list = html.xpath('//*[@class="job-list"]/ul')[0]
        except IndexError:
            try:
                status = int(html.xpath('//*[@class="text"]/h1/text()')[0])
                if status == 403:
                    print('ip被封')
                    return 0
            except Exception as e:
                try:
                    button = str(html.xpath('//*[@class="btn"]/text()')[0])
                    if button == '点击进行验证':
                        print('手动验证ip重新访问')
                    else:
                        print('ip被封')
                    return 0
                except Exception as e:
                    print('请求失败，换个ip')
                    return 0
        result_list = []
        for li in ul_list:
            params = {}
            params["job_name"] = li.xpath('.//*[@class="job-name"]/a/text()')[0]
            params["job-area"] = li.xpath('.//*[@class="job-area"]/text()')[0]
            params["job_money"] = li.xpath('.//*[@class="job-limit clearfix"]/span/text()')[0]
            params["job_work"] = li.xpath('.//*[@class="job-limit clearfix"]/p/text()')[0]
            params["job_education"] = li.xpath('.//*[@class="job-limit clearfix"]/p/text()')[1]
            params["company_name"] = li.xpath('.//*[@class="company-text"]/h3/a/text()')[0]
            result_list.append(params)
        print('=' * 100)
        print(result_list)
        # return 1


if __name__ == '__main__':
    #
    # proxy_ip = proxy_option.proxy_ip
    kd = kd_request()
    proxy_ip = kd.find_ip()
    print(proxy_ip)
    proxy = '--proxy-server={0}'.format(proxy_ip)
    LagouSpider(proxy).run()

