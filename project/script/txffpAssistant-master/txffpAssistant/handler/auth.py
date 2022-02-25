#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author  : fishyues
# @License : MIT
# @Contact : fishyues
# @Date    : 2020/07/22 16:07
import json
import base64

from urllib.parse import urlparse
from lxml import etree

from .base import BaseHandler
from .. import exceptions
from .. import decorators


__all__ = ["AuthHandler", "authenticated_session"]

login_page_url = "https://pss.txffp.com/pss/app/index"

auth_url = "https://sso.txffp.com/sso/app/oauth/login"
redirect_uri = "https://pss.txffp.com/pss/app/oauth/login"


class AuthHandler(BaseHandler):

    def auth_api( self, username, password, query, valid_code=""):
        data = dict(
            response_type="code",
            redirect_uri=redirect_uri,
            client_id=query["client_id"],
            scope=query["scope"],
            state=query["state"],
            loginType="PASSWORD",
            loginName=username,
            validCode=valid_code,
            passwd=password,
        )
        content = self.request(
            url=auth_url, method="POST", data=data, raw=False)
        return content

    def _get_login_page(self):
        self.logger.debug("尝试获取登陆页面数据")
        response = self.request(
            url=login_page_url, method="GET", allow_redirects=True)
        return response

    def url_parser(self, url):
        query = dict()
        q = urlparse(url).query
        kvs = q.split("&")

        for kv in kvs:
            k = kv.split("=", 1)
            query[k[0]] = k[1]
        self.logger.debug("解析url， 得到参数：{}".format(query))
        return query

    @decorators.post_decode()
    def msg_decode(self, msg):
        if isinstance(msg, str):
            msg = msg.encode("utf8")

        if isinstance(msg, bytes):
            try:
                msg = base64.decodebytes(msg)
                return msg
            except exceptions as err:
                self.logger.debug("对msg进行base64解码失败")
            return msg
        raise TypeError("msg must be string or bytes")

    def auth_resp_parser(self, content):
        self.logger.debug("认证响应结果：{}".format(content))
        try:
            data = json.loads(content)
            if data:
                return data, True
        except json.JSONDecodeError as err:
            if not content:
                return None, False
            node = etree.HTML(content)
            taiji_note = node.xpath("//div[@id='taiji_note']/text()")[0]
            taiji_ejson = node.xpath("//div[@id='taiji_ejson']/text()")[0]
            data = json.loads(taiji_note)
            data.update(json.loads(taiji_ejson))

            if "msg" in data:
                data["msg"] = self.msg_decode(data["msg"])
            return data, False
        return None, False

    def auth_status_checker(self, content):
        data, status = self.auth_resp_parser(content)
        if status:
            self.request(
                url=data["rediectUrl"],
                method="GET",
                allow_redirects=True)
            self.logger.info("模拟登陆成功")
            return True
        else:
            self.logger.warning("模拟登陆失败, 原因：{}".format(data))
            return False

    def login(self, username, password):
        loginpage_resp = self._get_login_page()

        if not loginpage_resp:
            self.logger.error("模拟登陆失败，失败原因：获取登陆页面数据失败")
            raise exceptions.NoneResponseError("请求响应内容为空")

        query = self.url_parser(loginpage_resp.url)
        content = self.auth_api(username, password, query)
        if not content:
            self.logger.error("模拟登陆失败，失败原因：认证接口未返回数据")
            raise exceptions.NoneResponseError("请求响应内容为空")

        result = self.auth_status_checker(content)
        return result


def authenticated_session(username, password, *args, **kwargs):
    event = AuthHandler(*args, **kwargs)
    result = event.login(username, password)
    if not result:
        raise exceptions.AuthFailedError("登陆失败")
    return event.session
