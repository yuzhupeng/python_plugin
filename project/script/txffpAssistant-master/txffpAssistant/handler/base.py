#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author  : fishyues
# @License : MIT
# @Contact : fishyues
# @Date    : 2020/07/22 15:48

import logging
import random
import time

import requests
from lxml import etree
from requests.cookies import RequestsCookieJar

from .. import component
from .. import exceptions


__all__ = ["BaseHandler", "GeneralHandler"]

DEFAULT_HEADER = {
    "User-Agent": """Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36""",
    "Accept-Language": "ja,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
}


class BaseHandler(object):

    def __init__(self, cookie_str=None, cookie_jar=None,
                 headers=None, sleep_time=None, logger=None,
                 encoding="utf-8", session=None, session_auto_close=True):
        self.cookie_str = cookie_str
        self.cookie_jar = cookie_jar if cookie_jar else RequestsCookieJar()
        self.sleep_time = sleep_time
        self.req_header = dict()
        self.encoding = encoding
        self.logger = logger if logger else logging.getLogger(__file__)
        self.session_auto_close = session_auto_close
        
        self.req_header.update(DEFAULT_HEADER)
        if headers:
            self.header_init(headers)

        if session:
            self.logger.debug("使用自定义session")
            self._session = session

        self.cookie_init()
        
    def __del__(self):
        if hasattr(self, "_session") and self.session_auto_close:
            self.logger.debug("关闭会话连接")
            self.session.close()

    def header_init(self, header):
        self.logger.debug("初始化请求头")
        self.req_header.update(header)

    def cookie_init(self):
        self.logger.debug("初始化cookie")
        self.session.cookies.update(self.cookie_jar)
        if self.cookie_str:
            cookie_dict = component.cookieStr2dict(self.cookie_str)
            self.session.cookies.update(cookie_dict)

    @property
    def session(self):
        if not hasattr(self, "_session"):
            self.logger.debug("创建session")
            self._session = requests.session()
        return self._session

    @property
    def session_cookieJar(self):
        return self.session.cookies

    def decode(self, content, encoding=None):
        if not encoding:
            encoding = self.encoding
        return content.decode(encoding)

    def request(self, url, method="POST", data=None,
                json_data=None, decode=True, raw=True,
                allow_redirects=False):
        def post():
            response = self.session.post(
                url=url,
                data=data,
                json=json_data,
                headers=self.req_header,
                allow_redirects=allow_redirects)
            return response

        def get():
            response = self.session.get(
                url=url,
                headers=self.req_header,
                allow_redirects=allow_redirects)
            return response

        method_map = {"POST": post, "GET": get}
        method = method.upper()

        if method not in method_map:
            raise exceptions.NotValidMethodError(
                "method '{}' is not supported.".format(method))

        if self.sleep_time:
            temp_time = round(random.uniform(0, self.sleep_time), 3)
            self.logger.debug("服务器减压睡眠: {}s".format(temp_time))
            time.sleep(temp_time)

        self.logger.debug("{}请求: {}".format(method, url))
        response = method_map[method]()
        self.logger.debug(
            "获得响应, 状态码: {}, url: {}".format(response.status_code, response.url))

        if raw:
            return response
        if decode:
            return self.decode(response.content)
        return response.content


class GeneralHandler(BaseHandler):

    def has_next_page(self, html=None, node=None):
        if html:
            node = etree.HTML(html)
            has_more = node.xpath(
                '//label[@id="taiji_search_hasMore"]/text()')
        elif xpath:
            has_more = node.xpath(
                '//label[@id="taiji_search_hasMore"]/text()')
        else:
            raise exceptions.ParameterError("至少提供一个html或node参数")

        if has_more and has_more[0] == "true":
            return True
        else:
            return False
