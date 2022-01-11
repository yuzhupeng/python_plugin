# -*- coding: utf-8 -*-
# @Author : Young Cc
# @Time   : 2021/08/04
# @File   : tools.py

import re
import hashlib
import time
 
from dateutil import parser
from lxml import etree


def get_md5(*args):
    """获取唯一的32位 md5 """
    m = hashlib.md5()
    for arg in args:
        m.update(str(arg).encode())

    return m.hexdigest()


def get_time_stamp(time_info: str):
    """从字符串中提取时间并转为13位时间戳"""
    if not time_info:
        return 0
    for _time_info in time_info.split("\n")[::-1]:
        if _time_info:
            time_info = _time_info
            break
    try:
            pt = parser.parse(time_info, fuzzy=True)  # 自动解析失败，重新获取，结果为 datetime 类型
            date_info = pt.strftime("%Y-%m-%d %H:%M:%S")
            return_time = int(time.mktime(time.strptime(date_info, "%Y-%m-%d %H:%M:%S")))
    except Exception:
        try:
            pt = parser.parse(time_info, fuzzy=True)  # 自动解析失败，重新获取，结果为 datetime 类型
            date_info = pt.strftime("%Y-%m-%d %H:%M:%S")
            return_time = int(time.mktime(time.strptime(date_info, "%Y-%m-%d %H:%M:%S")))
        except Exception:
            return 0

    if return_time > int(time.time()):
        return return_time - 365 * 24 * 60 * 60
    return return_time * 1000


def convert_callback(matches):
    """对 HTML 中的特殊编码进行转换"""
    try:
        char_id = matches.group(1)
        return chr(int(char_id))
    except Exception:
        return matches


def get_xpath_info(response, get_info_xpath, default_value="", is_strip=True, js_decode=False):
    """
    获取 xpath 解析后的数据
    :param response: 响应对象
    :param get_info_xpath: 获取数据的 xpath
    :param default_value: 默认返回值
    :param is_strip: 是否去除首尾空格
    :param js_decode: 是否对前端特殊编码进行解码
    """
    resp_info = response.xpath(f'string({get_info_xpath})').get(default_value)
    if js_decode:
        resp_info = re.sub("&#(\d+)(;|(?=\s))", convert_callback, resp_info)  # 前端转义编码替换
    return resp_info.strip() if is_strip else resp_info


def get_content_raw(response, get_info_xpath):
    """
    获取带 HTML 代码的正文内容
    :param response: response 对象，提供 xpath 解析
    :param get_info_xpath: 需要获取字段的 xpath，不能使用 string(.) 获取，否则得不到 JS 标签
    """
    return_info = ""
    if get_info_xpath:
        _content_info = response.xpath(get_info_xpath)
        _content_raw = etree.tostring(_content_info[0], encoding="utf-8").decode("utf-8") if _content_info else ""
        return_info = _content_raw
    return return_info


def get_html(response):
    """获取解码后的 response etree 对象"""
    try:
        html = etree.HTML(response.text)
    except:
        try:
            html = etree.HTML(response.body.decode("utf-8"))
        except:
            html = etree.HTML(response.body.decode("gbk"))

    return html
