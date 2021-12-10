# -*- coding: utf-8 -*-

# from selenium import webdriver
# import time
# from scrapy.http.response.html import HtmlResponse
#
#
# class SeleniumDownloadMiddleware(object):
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#
#     def process_request(self,request,spider):
#         self.driver.get(request.url)
#         time.sleep(1)
#         # try:
#         #     while True:
#         #         showmore = self.driver.find_element_by_class_name('show-more')
#         #         showmore.click()
#         #         time.sleep(0.5)
#         #         if not showmore:
#         #             break
#         # except:
#         #     pass
#         source = self.driver.page_source
#         response = HtmlResponse(url=self.driver.current_url,body=source,request=request,encoding='utf-8')
#         return response