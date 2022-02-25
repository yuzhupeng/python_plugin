#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author  : fishyues
# @License : MIT
# @Contact : fishyues
# @Date    : 2020/07/22 16:06


def cookieStr2dict(cookie_text):
    """从cookie文本字符内容中提取数据，并格式化为字典类型

    Args:
        cookie_text: cookie文本

    Return:
        cookie字典
    """
    assert isinstance(cookie_text, str), "cookie_text must be string type"
    
    cookie_dict = dict()
    for line in cookie_text.split(";"):
        line = line.strip()
        if "=" not in line:
            continue
        kv = line.split("=", 1)
        if kv[0] not in cookie_dict:
            cookie_dict[kv[0]] = kv[1]
    return cookie_dict
