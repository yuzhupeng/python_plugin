# -*- coding: utf-8 -*-
# @Author : Young Cc
# @Time   : 2021/08/30
# @File   : 创建游览器.py


import re
import json
import html

info = r"\xa0 \xa0 \xa0 \xa0 \xa0 \xa0"
def convert_callback(matches):
    """对 HTML 中的特殊编码进行转换"""
    try:
        char_id = matches.group(1)
        return chr(int(char_id))
    except:
        return matches

s2 = re.sub("&xa(\d+)(;|(?=\s))", convert_callback, info)
print(s2)



