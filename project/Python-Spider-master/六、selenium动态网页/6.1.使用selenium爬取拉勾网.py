
from selenium import webdriver
from lxml import etree
import re
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LagouSpider(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        #python职位
        self.url = 'https://www.lagou.com/jobs/list_python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput='
        self.position = []

    def run(self):
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            WebDriverWait(driver=self.driver,timeout=20).until(
                EC.presence_of_element_located((By.XPATH,"//div[@class='pager_container']/span[last()]"))
            )
            self.parse_list_page(source)
            #点“下一页”
            next_btn = self.driver.find_element_by_xpath(
                "//div[@class='pager_container']/span[last()]")
            if "pager_next_disabled" in next_btn.get_attribute("class"):
                break
            else:
                next_btn.click()
            time.sleep(1)


    def parse_list_page(self,source):
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        #每一页的所有职位的详情url
        for link in links:
            self.request_detail_page(link)
            time.sleep(1)

    def request_detail_page(self,url):
        # self.driver.get(url)
        self.driver.execute_script("window.open('%s')"%url)
        self.driver.switch_to.window(self.driver.window_handles[1])

        WebDriverWait(driver=self.driver,timeout=20).until(
            EC.presence_of_element_located((By.XPATH,"//div[@class='job-name']/span[@class='name']"))
        )
        #获取职位详情页的源代码
        source = self.driver.page_source
        self.parse_detail_page(source)
        #关闭当前详情页，并且切换到列表页
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def parse_detail_page(self,source):
        html = etree.HTML(source)
        position_name = html.xpath("//span[@class='name']/text()")[0]
        job_request_spans = html.xpath("//dd[@class='job_request']//span")
        salary = job_request_spans[0].xpath('.//text()')[0].strip()
        city = job_request_spans[1].xpath('.//text()')[0].strip()
        city = re.sub(r"[\s/]","",city)
        work_years = job_request_spans[2].xpath('.//text()')[0].strip()
        work_years = re.sub(r"[\s/]","",work_years)
        education = job_request_spans[3].xpath('.//text()')[0].strip()
        education = re.sub(r"[\s/]","",education)
        desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()
        company_name = html.xpath("//h2[@class='fl']/text()")[0].strip()
        position = {
            'name':position_name,
            'company_name':company_name,
            'salary':salary,
            'city': city,
            'work_years': work_years,
            'education': education,
            'desc': desc,
        }
        self.position.append(position)
        print(position)
        print('-'*200)

if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()