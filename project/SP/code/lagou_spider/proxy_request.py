#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用requests请求代理服务器
请求http和https网页均适用
"""

import requests
import time, datetime

from mysql_model import xhx_mysql


class kd_request(object):

    def __init__(self):
        # 提取代理API接口，获取1个代理IP
        self.api_url = "http://dps.kdlapi.com/api/getdps/?orderid=943886269259897&num=1&pt=1&sep=1"

    def request_ip(self):
        # 获取API接口返回的代理IP
        proxy_ip = requests.get(self.api_url).text
        return proxy_ip

    def insert_data(self, mysql, proxy_ip):
        record_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timestamp = int(time.time())
        data = [{'ip': proxy_ip.split(':')[0], 'port': proxy_ip.split(':')[-1], 'ip_port': proxy_ip,
                 'record_time': record_time, 'timestamp': timestamp}]
        mysql.insert_into_table('ip_list', data)

    def find_data(self, mysql):
        timestamp = int(time.time()) - 180 # 查找3分钟内的数据
        result, row_count = mysql.find_all_table('ip_list', 'timestamp > %d' % timestamp)
        print('查找到{}条数据'.format(row_count))
        return result, row_count

    def find_ip(self):
        mysql = xhx_mysql()
        mysql.create_connect()
        result, row_count = self.find_data(mysql)
        if row_count == 0:
            proxy_ip = self.request_ip()
            self.insert_data(mysql, proxy_ip)
            return 'http://' + proxy_ip
        else:
            last_result = result[-1]
            proxy_ip = last_result[3]
            return 'http://' + proxy_ip


# 用户名密码认证(私密代理/独享代理)
# username = "username"
# password = "password"
# proxies = {
#     "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
#     "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
# }

# 白名单方式（需提前设置白名单）
# proxies = {
#     "http": "http://%(proxy)s/" % {"proxy": proxy_ip},
# }
#
# # 要访问的目标网页
# target_url = "https://dev.kdlapi.com/testproxy"
# #
# # # 使用代理IP发送请求
# response = requests.get(target_url, proxies=proxies)
# #
# # # 获取页面内容
# if response.status_code == 200:
#     print(response.text)